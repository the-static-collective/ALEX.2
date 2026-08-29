import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNNER_PATH = ROOT / "tools" / "run_research_formation.py"
FAR_SIDE_ID = "far-side-pass@52c678767017c170506ce1895d3a610b6ef115b4"
BINOCULAR_ID = "binocular-recursion@c26620efc3c601eb0686825e1cfcbe1f1951f49e"


def request_value():
    return {
        "schema": "alex.research-formation-run/v0",
        "run_id": "formation-cli-001",
        "body_mode": "EXPERIMENTAL",
        "materializations": {},
        "far_side": {
            "body_time_id": FAR_SIDE_ID,
            "case": {"schema": "placeholder.far-side/v0"},
        },
        "binocular": {
            "body_time_id": BINOCULAR_ID,
            "case": {
                "schema": "placeholder.binocular/v0",
                "discovery_trigger_refs": [],
            },
        },
    }


class ResearchFormationCliTests(unittest.TestCase):
    def run_cli(self, input_text: str | None = None, path: Path | None = None):
        args = [sys.executable, str(RUNNER_PATH)]
        if path is not None:
            args.append(str(path))
        return subprocess.run(
            args,
            input=input_text,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

    def test_stdin_request_emits_canonical_structured_result(self):
        completed = self.run_cli(json.dumps(request_value()))
        self.assertEqual(completed.returncode, 0, completed.stderr)
        result = json.loads(completed.stdout)
        self.assertEqual(result["schema"], "alex.research-formation-result/v0")
        self.assertEqual(result["run_id"], "formation-cli-001")
        self.assertEqual(result["execution_state"], "REFUSED")
        self.assertEqual(result["reason_code"], "MATERIALIZATION_REQUIRED")
        self.assertEqual(result["far_side"]["route"]["body_time_id"], FAR_SIDE_ID)
        self.assertIsNone(result["bridge"])
        self.assertIsNone(result["binocular"])
        self.assertEqual(result["authority"], "none")
        self.assertEqual(
            completed.stdout,
            json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n",
        )

    def test_file_request_is_supported(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "formation.json"
            path.write_text(json.dumps(request_value()), encoding="utf-8")
            completed = self.run_cli(path=path)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(json.loads(completed.stdout)["reason_code"], "MATERIALIZATION_REQUIRED")

    def test_malformed_json_is_host_error_exit_two(self):
        completed = self.run_cli("{not-json")
        self.assertEqual(completed.returncode, 2)
        self.assertEqual(completed.stdout, "")
        self.assertIn("invalid request", completed.stderr)

    def test_bad_schema_is_host_error_exit_two(self):
        request = request_value()
        request["schema"] = "alex.research-formation-run/v999"
        completed = self.run_cli(json.dumps(request))
        self.assertEqual(completed.returncode, 2)
        self.assertEqual(completed.stdout, "")
        self.assertIn("invalid request", completed.stderr)

    def test_same_request_emits_identical_bytes(self):
        payload = json.dumps(request_value())
        left = self.run_cli(payload)
        right = self.run_cli(payload)
        self.assertEqual(left.returncode, 0, left.stderr)
        self.assertEqual(right.returncode, 0, right.stderr)
        self.assertEqual(left.stdout, right.stdout)


if __name__ == "__main__":
    unittest.main()
