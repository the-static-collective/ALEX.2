import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "tools" / "run_binocular_recursion.py"
SPECIMENS = ROOT / "tests" / "fixtures" / "binocular_recursion"


class BinocularRunnerTests(unittest.TestCase):
    def test_file_input_accepts_lawful_case(self):
        completed = subprocess.run([sys.executable, str(RUNNER), str(SPECIMENS / "lawful-residual.json")], capture_output=True, text=True, check=False)
        self.assertEqual(completed.returncode, 0)
        self.assertEqual(json.loads(completed.stdout)["disposition"], "ACCEPT")

    def test_stdin_input_accepts_lawful_case(self):
        payload = (SPECIMENS / "lawful-residual.json").read_text(encoding="utf-8")
        completed = subprocess.run([sys.executable, str(RUNNER)], input=payload, capture_output=True, text=True, check=False)
        self.assertEqual(completed.returncode, 0)
        self.assertEqual(json.loads(completed.stdout)["terminal"], "RESIDUAL")

    def test_evaluator_refusal_maps_to_exit_one(self):
        case = json.loads((SPECIMENS / "lawful-residual.json").read_text(encoding="utf-8"))
        case["passes"][0]["compression"]["claim_support_refs"].append("trigger:prompt-001")
        completed = subprocess.run([sys.executable, str(RUNNER)], input=json.dumps(case), capture_output=True, text=True, check=False)
        self.assertEqual(completed.returncode, 1)
        self.assertEqual(json.loads(completed.stdout)["reason_code"], "DISCOVERY_TRIGGER_AS_SUPPORT")

    def test_malformed_json_maps_to_exit_two(self):
        completed = subprocess.run([sys.executable, str(RUNNER)], input="{not-json", capture_output=True, text=True, check=False)
        self.assertEqual(completed.returncode, 2)
        self.assertEqual(completed.stdout, "")
        self.assertIn("binocular recursion failed to execute:", completed.stderr)


if __name__ == "__main__":
    unittest.main()
