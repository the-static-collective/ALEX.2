import subprocess
import tempfile
import unittest
from pathlib import Path

from alex_runtime.chronobody import BodyMode, execute_body, parse_registry
from alex_runtime.digests import sha256_json


REPO = "the-static-collective/ALEX.2"
ECHO_FIXTURE = Path(__file__).parent / "fixtures" / "chronobody" / "echo_organ.py"


def run_git(root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return completed.stdout.strip()


def committed_body(root: Path, script: str, *, organ_id="test-organ"):
    subprocess.run(["git", "init", str(root)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    run_git(root, "config", "user.email", "chronobody@example.test")
    run_git(root, "config", "user.name", "Chronobody Test")
    run_git(root, "remote", "add", "origin", "https://github.com/the-static-collective/ALEX.2.git")
    tools = root / "tools"
    tools.mkdir(parents=True, exist_ok=True)
    (tools / "organ.py").write_text(script, encoding="utf-8")
    run_git(root, "add", ".")
    run_git(root, "commit", "-m", "body")
    sha = run_git(root, "rev-parse", "HEAD")
    value = {
        "schema": "alex.chronobody-registry/v0",
        "organs": [
            {
                "organ_id": organ_id,
                "body_time_id": f"{organ_id}@{sha}",
                "status": "INCUBATING",
                "capabilities": ["test_capability"],
                "source": {
                    "repo": REPO,
                    "branch": "test/body",
                    "sha": sha,
                },
                "runtime": {
                    "contract": "python-json-stdio/v0",
                    "entrypoint": "tools/organ.py",
                },
                "authority": "none",
                "parents": [],
            }
        ],
    }
    return parse_registry(value)[0], sha


class ChronobodyExecutionTests(unittest.TestCase):
    def test_clean_body_executes_and_receipts_exact_body_time(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            entry, sha = committed_body(root, ECHO_FIXTURE.read_text(encoding="utf-8"))
            payload = {"alpha": 1, "nested": {"z": True}}
            result = execute_body(entry, root, payload, BodyMode.EXPERIMENTAL, timeout_seconds=2)

            self.assertEqual(result.execution_state, "COMPLETED")
            self.assertIsNone(result.reason_code)
            self.assertEqual(result.output, {"schema": "test.echo/v0", "payload": payload})
            self.assertEqual(result.stderr, "")
            self.assertEqual(result.receipt["receipt_type"], "alex.chronobody-execution/v0")
            self.assertEqual(result.receipt["organ_id"], "test-organ")
            self.assertEqual(result.receipt["body_time_id"], f"test-organ@{sha}")
            self.assertEqual(result.receipt["organ_status"], "INCUBATING")
            self.assertEqual(result.receipt["body_mode"], "EXPERIMENTAL")
            self.assertEqual(result.receipt["source_sha"], sha)
            self.assertEqual(result.receipt["runtime_contract"], "python-json-stdio/v0")
            self.assertEqual(result.receipt["entrypoint"], "tools/organ.py")
            self.assertEqual(result.receipt["input_digest"], sha256_json(payload))
            self.assertEqual(result.receipt["output_digest"], sha256_json(result.output))
            self.assertEqual(result.receipt["execution_state"], "COMPLETED")
            self.assertEqual(result.receipt["exit_code"], 0)
            self.assertEqual(result.receipt["authority"], "none")

    def test_exit_one_with_valid_json_is_evaluated_completion(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            entry, _ = committed_body(
                root,
                "import json, sys\njson.dump({'schema':'test.refusal/v0','disposition':'REFUSE'}, sys.stdout, sort_keys=True, separators=(',',':'))\nsys.stdout.write('\\n')\nraise SystemExit(1)\n",
            )
            result = execute_body(entry, root, {"x": 1}, BodyMode.EXPERIMENTAL, timeout_seconds=2)
            self.assertEqual(result.execution_state, "COMPLETED")
            self.assertIsNone(result.reason_code)
            self.assertEqual(result.output["disposition"], "REFUSE")
            self.assertEqual(result.receipt["exit_code"], 1)
            self.assertEqual(result.receipt["execution_state"], "COMPLETED")
            self.assertEqual(result.receipt["output_digest"], sha256_json(result.output))

    def test_non_evaluated_nonzero_exit_is_visible_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            entry, _ = committed_body(
                root,
                "import sys\nsys.stderr.write('boom\\n')\nraise SystemExit(3)\n",
            )
            result = execute_body(entry, root, {"x": 1}, BodyMode.EXPERIMENTAL, timeout_seconds=2)
            self.assertEqual(result.execution_state, "FAILED")
            self.assertEqual(result.reason_code, "PROCESS_EXIT_NONZERO")
            self.assertEqual(result.receipt["exit_code"], 3)
            self.assertIn("boom", result.stderr)
            self.assertIsNone(result.output)
            self.assertIsNone(result.receipt["output_digest"])

    def test_invalid_json_stdout_is_visible_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            entry, _ = committed_body(root, "print('not-json')\n")
            result = execute_body(entry, root, {"x": 1}, BodyMode.EXPERIMENTAL, timeout_seconds=2)
            self.assertEqual(result.execution_state, "FAILED")
            self.assertEqual(result.reason_code, "INVALID_JSON_OUTPUT")
            self.assertEqual(result.receipt["exit_code"], 0)
            self.assertIsNone(result.output)

    def test_timeout_is_visible_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            entry, _ = committed_body(root, "import time\ntime.sleep(2)\n")
            result = execute_body(entry, root, {"x": 1}, BodyMode.EXPERIMENTAL, timeout_seconds=0.01)
            self.assertEqual(result.execution_state, "FAILED")
            self.assertEqual(result.reason_code, "TIMEOUT")
            self.assertIsNone(result.receipt["exit_code"])

    def test_materialization_refusal_prevents_execution(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            entry, _ = committed_body(root, "raise RuntimeError('must never execute')\n")
            (root / "dirty.txt").write_text("uncommitted\n", encoding="utf-8")
            result = execute_body(entry, root, {"x": 1}, BodyMode.EXPERIMENTAL, timeout_seconds=2)
            self.assertEqual(result.execution_state, "REFUSED")
            self.assertEqual(result.reason_code, "DIRTY_BODY")
            self.assertIsNone(result.receipt["exit_code"])

    def test_direct_execution_cannot_bypass_body_mode(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            entry, _ = committed_body(root, ECHO_FIXTURE.read_text(encoding="utf-8"))
            result = execute_body(entry, root, {"x": 1}, BodyMode.PRESENT_ONLY, timeout_seconds=2)
            self.assertEqual(result.execution_state, "REFUSED")
            self.assertEqual(result.reason_code, "BODY_MODE_MISMATCH")


if __name__ == "__main__":
    unittest.main()
