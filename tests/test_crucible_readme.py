import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "crucible" / "README.md"


class BlindCrucibleDocumentationTests(unittest.TestCase):
    def readme(self) -> str:
        return README.read_text(encoding="utf-8")

    def test_adapter_visibility_is_explicitly_case_only(self):
        text = self.readme()
        self.assertIn("The adapter receives **CASE only**.", text)
        self.assertIn("ORACLE remains harness-only", text)
        self.assertIn("A canonical specimen may contain its expected outcome", text)

    def test_open_repo_pressure_is_metamorphic_not_secret(self):
        text = self.readme().lower()
        self.assertIn("metamorphic, not secret", text)
        self.assertIn("open repository", text)

    def test_runtime_conformance_disclaimer_survives_gate_one(self):
        text = self.readme()
        self.assertIn("It does not prove an ALEX runtime conforms.", text)
        self.assertIn("CRUCIBLE RUNTIME CONFORMANCE IS NOT YET CLAIMED", text)


if __name__ == "__main__":
    unittest.main()
