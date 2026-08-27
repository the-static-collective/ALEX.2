import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "tools" / "crucible.py"
ADAPTER = ROOT / "tools" / "derivation_adapter.py"
SPECIMENS = ROOT / "crucible" / "specimens"


class DerivationAdapterProcessTests(unittest.TestCase):
    def run_fixture(self, name: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(CLI),
                "--fixture",
                str(SPECIMENS / name),
                "--operation-type",
                "relation_derivation",
                "--rule-profile",
                "alex.runtime/derivation-m0",
                "--adapter",
                sys.executable,
                str(ADAPTER),
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_attention_negative_passes_real_blind_adapter(self):
        result = self.run_fixture("relation-derivation-001-attention-negative.json")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS relation-derivation-001-attention-negative", result.stdout)

    def test_evidence_positive_passes_real_blind_adapter(self):
        result = self.run_fixture("relation-derivation-001-evidence-positive.json")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS relation-derivation-001-evidence-positive", result.stdout)

    def test_adapter_rejects_non_object_case(self):
        result = subprocess.run(
            [sys.executable, str(ADAPTER)],
            cwd=ROOT,
            input="[]",
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("CASE must be a JSON object", result.stderr)


if __name__ == "__main__":
    unittest.main()
