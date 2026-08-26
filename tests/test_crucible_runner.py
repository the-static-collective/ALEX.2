import unittest
from tools.crucible import compare_result


class CompareResultTests(unittest.TestCase):
    def specimen(self):
        return {
            "id": "search-absence",
            "expected": {
                "disposition": "REFUSE",
                "refusal_code": "SEARCH_COVERAGE_INSUFFICIENT",
                "required_receipt_survivors": ["search_observation:S1"],
                "forbidden_promotions": ["source_absence"],
            },
        }

    def test_cheating_result_fails(self):
        errors = compare_result(self.specimen(), {
            "specimen_id": "search-absence",
            "disposition": "ACCEPT",
            "receipt_survivors": [],
            "promotions": ["source_absence"],
        })
        joined = " ".join(errors)
        self.assertIn("disposition", joined)
        self.assertIn("search_observation:S1", joined)
        self.assertIn("source_absence", joined)

    def test_required_refusal_passes(self):
        errors = compare_result(self.specimen(), {
            "specimen_id": "search-absence",
            "disposition": "REFUSE",
            "refusal_code": "SEARCH_COVERAGE_INSUFFICIENT",
            "receipt_survivors": ["search_observation:S1"],
            "promotions": [],
        })
        self.assertEqual(errors, [])

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "tools" / "crucible.py"
FIXTURES = ROOT / "tests" / "fixtures"


class ProcessRunnerTests(unittest.TestCase):
    def write_specimen(self, directory: str) -> Path:
        path = Path(directory) / "specimen.json"
        path.write_text(
            json.dumps({
                "id": "search-absence",
                "title": "temporary search absence specimen",
                "constitutional_laws": ["SEARCH MISS != ABSENCE"],
                "given": {"search_observation": "S1"},
                "attempt": {"promote": "source_absence"},
                "expected": {
                    "disposition": "REFUSE",
                    "refusal_code": "SEARCH_COVERAGE_INSUFFICIENT",
                    "required_receipt_survivors": ["search_observation:S1"],
                    "forbidden_promotions": ["source_absence"],
                },
                "version": 1,
            }),
            encoding="utf-8",
        )
        return path

    def run_adapter(self, adapter_name: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmp:
            fixture = self.write_specimen(tmp)
            return subprocess.run(
                [
                    sys.executable,
                    str(CLI),
                    "--fixture",
                    str(fixture),
                    "--adapter",
                    sys.executable,
                    str(FIXTURES / adapter_name),
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )

    def test_cheating_adapter_exits_one(self):
        result = self.run_adapter("adapter_accepts_everything.py")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("FAIL search-absence", result.stdout)

    def test_required_refusal_adapter_exits_zero(self):
        result = self.run_adapter("adapter_refuses_correctly.py")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS search-absence", result.stdout)
