import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from alex_runtime.chronobody import parse_registry
from tools.run_chronobody import evaluate_request


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "chronobody" / "registry.v0.json"
RUNNER_PATH = ROOT / "tools" / "run_chronobody.py"
FAR_SIDE_ID = "far-side-pass@52c678767017c170506ce1895d3a610b6ef115b4"
BINOCULAR_ID = "binocular-recursion@c26620efc3c601eb0686825e1cfcbe1f1951f49e"


def load_entries():
    return parse_registry(json.loads(REGISTRY_PATH.read_text(encoding="utf-8")))


def request_value():
    return {
        "schema": "alex.chronobody-run-request/v0",
        "capability": "far_side_pressure",
        "mode": "EXPERIMENTAL",
        "organ_id": "far-side-pass",
        "body_time_id": FAR_SIDE_ID,
        "materializations": {},
        "payload": {"schema": "test.case/v0"},
    }


class ChronobodyCommittedRegistryTests(unittest.TestCase):
    def test_committed_registry_pins_exact_first_two_body_times(self):
        entries = load_entries()
        self.assertEqual(
            {entry.body_time_id for entry in entries},
            {FAR_SIDE_ID, BINOCULAR_ID},
        )
        self.assertTrue(all(entry.status.value == "INCUBATING" for entry in entries))
        self.assertTrue(all(entry.authority == "none" for entry in entries))


class ChronobodyRunRequestTests(unittest.TestCase):
    def test_missing_materialization_is_structured_refusal_after_exact_route(self):
        result = evaluate_request(request_value(), load_entries())
        self.assertEqual(result["schema"], "alex.chronobody-run-result/v0")
        self.assertEqual(result["disposition"], "REFUSED")
        self.assertEqual(result["reason_code"], "MATERIALIZATION_REQUIRED")
        self.assertEqual(result["route"]["disposition"], "ROUTED")
        self.assertEqual(result["route"]["body_time_id"], FAR_SIDE_ID)
        self.assertIsNone(result["execution"])
        self.assertEqual(result["authority"], "none")

    def test_unregistered_exact_body_does_not_fall_back(self):
        request = request_value()
        request["body_time_id"] = "far-side-pass@1111111111111111111111111111111111111111"
        result = evaluate_request(request, load_entries())
        self.assertEqual(result["disposition"], "UNAVAILABLE")
        self.assertEqual(result["reason_code"], "BODY_TIME_NOT_REGISTERED")
        self.assertIsNone(result["execution"])

    def test_present_only_does_not_execute_incubating_body(self):
        request = request_value()
        request["mode"] = "PRESENT_ONLY"
        result = evaluate_request(request, load_entries())
        self.assertEqual(result["disposition"], "REFUSED")
        self.assertEqual(result["reason_code"], "BODY_MODE_MISMATCH")


class ChronobodyCliTests(unittest.TestCase):
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
        request = request_value()
        completed = self.run_cli(json.dumps(request))
        self.assertEqual(completed.returncode, 0, completed.stderr)
        result = json.loads(completed.stdout)
        self.assertEqual(result["reason_code"], "MATERIALIZATION_REQUIRED")
        self.assertEqual(completed.stdout, json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n")

    def test_file_request_is_supported(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "request.json"
            path.write_text(json.dumps(request_value()), encoding="utf-8")
            completed = self.run_cli(path=path)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(json.loads(completed.stdout)["reason_code"], "MATERIALIZATION_REQUIRED")

    def test_malformed_json_is_host_error_exit_two(self):
        completed = self.run_cli("{not-json")
        self.assertEqual(completed.returncode, 2)
        self.assertEqual(completed.stdout, "")
        self.assertIn("invalid request", completed.stderr)


if __name__ == "__main__":
    unittest.main()
