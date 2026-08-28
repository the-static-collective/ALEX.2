import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFERENCE = ROOT / "skills" / "alex" / "references" / "binocular-recursion.md"
SKILL = ROOT / "skills" / "alex" / "SKILL.md"


class BinocularReferenceTests(unittest.TestCase):
    def test_reference_preserves_core_non_collapses(self):
        text = REFERENCE.read_text(encoding="utf-8")
        for phrase in ("FREEZE → COMPRESS || EXPAND → TENSION → UPDATE → REPEAT", "discovery trigger != support", "introduced premise != admitted premise", "ACCEPT != researched claim accepted as true"):
            self.assertIn(phrase, text)

    def test_alex_skill_routes_binocular_recursion(self):
        self.assertIn("references/binocular-recursion.md", SKILL.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
