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
