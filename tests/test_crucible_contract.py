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
            "attention-trace-support-independence.json",
            "bounded-suspension.json",
            "pressure-loss-survivor.json",
            "creative-recurrence-independence.json",
            "relation-derivation-001-attention-negative.json",
            "relation-derivation-001-evidence-positive.json",
            "loadout-handshake-valid.json",
            "loadout-handshake-stale-compile.json",
            "loadout-handshake-owner-drift.json",
            "loadout-handshake-permission-drift.json",
            "loadout-handshake-capability-gap.json",
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

    def test_attention_ancestor_remains_historical_shape(self):
        path = ROOT / "crucible" / "specimens" / "attention-trace-support-independence.json"
        specimen = json.loads(path.read_text(encoding="utf-8"))
        self.assertIn("breadcrumb", specimen["given"])
        self.assertIn("search", specimen["given"])
        self.assertIn("evidence", specimen["given"])
        self.assertNotIn("records", specimen["given"])
        self.assertNotIn("relation_proposal", specimen["attempt"])

    def test_hardening_record_contracts(self):
        search = self.load("search-observation.schema.json")
        self.assertEqual(
            search["properties"]["coverage_status"]["enum"],
            ["DECLARED_COMPLETE_FOR_SCOPE", "PARTIAL", "TRUNCATED", "UNKNOWN", "NOT_APPLICABLE"],
        )
        for key in [
            "id", "corpus_id", "query", "query_type", "index_id", "index_version",
            "fields_searched", "record_types_searched", "page_or_reading_scope",
            "pagination_complete", "unreadable_or_missing_ranges", "exclusions",
            "truncation", "filters", "result_ids", "result_count", "observed_at",
            "producer", "coverage_status",
        ]:
            self.assertIn(key, search["required"])

        premise = self.load("inherited-premise.schema.json")
        self.assertEqual(
            premise["properties"]["status"]["enum"],
            ["UNEXAMINED", "EXAMINED_SUPPORTED", "EXAMINED_CONTRADICTED", "EXAMINED_UNRESOLVED", "REPLACED", "REFUSED"],
        )
        self.assertIn("authority_claimed", premise["required"])
        self.assertIn("authority_admitted", premise["required"])

        family = self.load("dependency-family.schema.json")
        self.assertEqual(
            family["properties"]["independence_status"]["enum"],
            ["DEPENDENT", "PARTIALLY_DEPENDENT", "INDEPENDENT_WITHIN_DECLARED_SCOPE", "UNKNOWN"],
        )
        self.assertIn("member_record_ids", family["required"])
        self.assertIn("shared_ancestor_ids", family["required"])

        replay = self.load("counterfactual-replay.schema.json")
        self.assertEqual(
            replay["properties"]["consequence_class"]["enum"],
            ["SURVIVES_REMOVAL", "DEGRADES", "CHANGES_VERDICT", "COLLAPSES", "INSUFFICIENT_TO_TEST"],
        )
        self.assertIn("base_replay_receipt_id", replay["required"])

    def test_runtime_conformance_not_claimed_in_public_docs(self):
        phrase = "CRUCIBLE RUNTIME CONFORMANCE IS NOT YET CLAIMED"
        paths = [
            ROOT / "README.md",
            ROOT / "docs" / "superpowers" / "specs" / "2026-08-25-alexandria-floor-design.md",
            ROOT / "docs" / "superpowers" / "specs" / "2026-08-26-alex-constitutional-hardening-design.md",
        ]
        for path in paths:
            self.assertIn(phrase, path.read_text(encoding="utf-8"), str(path))
