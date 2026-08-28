import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "far_side_lab.py"
FIXTURES = ROOT / "tests" / "fixtures" / "far_side"


class FarSideCliTests(unittest.TestCase):
    def test_file_input_emits_survivor_result(self):
        completed = subprocess.run(
            [sys.executable, str(TOOL), str(FIXTURES / "survivor.json")],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        result = json.loads(completed.stdout)
        self.assertEqual(result["final_status"], "FAR_SIDE_SURVIVOR")

    def test_stdin_input_emits_no_novelty_as_success(self):
        payload = (FIXTURES / "no-new-dimension.json").read_text(encoding="utf-8")
        completed = subprocess.run(
            [sys.executable, str(TOOL), "-"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            input=payload,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        result = json.loads(completed.stdout)
        self.assertEqual(result["final_status"], "NO_NEW_DIMENSION_EARNED")

    def test_malformed_json_exits_two_without_traceback(self):
        completed = subprocess.run(
            [sys.executable, str(TOOL), "-"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            input="{not-json",
        )
        self.assertEqual(completed.returncode, 2)
        self.assertIn("invalid JSON", completed.stderr)
        self.assertNotIn("Traceback", completed.stderr)


if __name__ == "__main__":
    unittest.main()
