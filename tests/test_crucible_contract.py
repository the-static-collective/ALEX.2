import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "crucible" / "schema"


class CrucibleContractTests(unittest.TestCase):
    def load(self, name: str) -> dict:
        return json.loads((SCHEMA / name).read_text(encoding="utf-8"))

    def test_specimen_contract(self):
        schema = self.load("specimen.schema.json")
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        for key in ["id", "title", "constitutional_laws", "given", "attempt", "expected", "version"]:
            self.assertIn(key, schema["required"])
        expected = schema["properties"]["expected"]
        for key in ["disposition", "required_receipt_survivors", "forbidden_promotions"]:
            self.assertIn(key, expected["required"])

    def test_result_dispositions(self):
        schema = self.load("result.schema.json")
        self.assertEqual(
            schema["properties"]["disposition"]["enum"],
            ["ACCEPT", "REFUSE", "UNRESOLVED", "INSUFFICIENT_TO_TEST"],
        )

    def test_initial_fixture_corpus(self):
        expected_names = {
            "broken-ancestry.json",
            "coordinate-drift.json",
            "search-absence.json",
            "shared-lineage-corroboration.json",
            "favored-hypothesis.json",
            "serendipity-promotion.json",
            "replay-impersonation.json",
            "ghost-promotion.json",
            "yarn-promotion.json",
            "constitution-smuggling.json",
            "inherited-premise-smuggling.json",
            "remove-one-collapse.json",
        }
        specimens = ROOT / "crucible" / "specimens"
        actual_names = {p.name for p in specimens.glob("*.json")} if specimens.exists() else set()
        self.assertEqual(actual_names, expected_names)

        for name in sorted(expected_names):
            path = specimens / name
            specimen = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(specimen["id"], path.stem)
            self.assertTrue(specimen["constitutional_laws"])
            self.assertTrue(specimen["expected"]["required_receipt_survivors"])
            self.assertIn("forbidden_promotions", specimen["expected"])
