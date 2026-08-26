import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "crucible" / "schema"
BLIND = ROOT / "tools" / "crucible_blind.py"


class BlindContractSchemaTests(unittest.TestCase):
    def load_schema(self, name: str) -> dict:
        path = SCHEMA / name
        self.assertTrue(path.exists(), f"missing blind contract schema: {name}")
        return json.loads(path.read_text(encoding="utf-8"))

    def test_case_schema_exposes_only_runtime_inputs(self):
        schema = self.load_schema("case.schema.json")
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(
            set(schema["required"]),
            {"case_id", "operation_type", "rule_profile", "given", "attempt", "nonce", "input_digest"},
        )
        self.assertNotIn("expected", schema["properties"])
        self.assertNotIn("constitutional_laws", schema["properties"])

    def test_oracle_schema_is_harness_only_answer_contract(self):
        schema = self.load_schema("oracle.schema.json")
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(
            set(schema["required"]),
            {
                "case_id",
                "expected_disposition",
                "expected_reason_code",
                "required_survivors",
                "forbidden_outputs",
                "metamorphic_family",
            },
        )
        self.assertNotIn("given", schema["properties"])
        self.assertNotIn("attempt", schema["properties"])

    def test_runtime_result_keeps_execution_state_separate_from_disposition(self):
        schema = self.load_schema("runtime-result.schema.json")
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(
            schema["properties"]["disposition"]["enum"],
            ["ACCEPT", "REFUSE", "UNRESOLVED", "INSUFFICIENT_TO_TEST"],
        )
        summary = schema["properties"]["execution_trace_summary"]
        self.assertEqual(
            summary["properties"]["terminal_state"]["enum"],
            ["FINISHED", "SUSPENDED", "ERRORED", "CANCELLED"],
        )
        self.assertEqual(summary["properties"]["step_count"]["minimum"], 0)


class BlindBuilderTests(unittest.TestCase):
    def load_module(self):
        self.assertTrue(BLIND.exists(), "tools/crucible_blind.py must define the CASE/ORACLE split")
        spec = importlib.util.spec_from_file_location("crucible_blind_under_test", BLIND)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def specimen(self) -> dict:
        return {
            "id": "search-absence",
            "title": "Search miss is not absence",
            "constitutional_laws": ["SEARCH MISS != ABSENCE"],
            "given": {"search_observation": "S1"},
            "attempt": {"promote": "source_absence"},
            "expected": {
                "disposition": "REFUSE",
                "refusal_code": "SEARCH_COVERAGE_INSUFFICIENT",
                "required_receipt_survivors": ["search_observation:S1"],
                "forbidden_promotions": ["source_absence"],
            },
            "notes": "fixture-authoring metadata stays harness-side",
            "version": 1,
        }

    def test_build_case_strips_fixture_authoring_and_oracle_fields(self):
        blind = self.load_module()
        case = blind.build_case(self.specimen(), nonce="n-001")
        self.assertEqual(
            set(case),
            {"case_id", "operation_type", "rule_profile", "given", "attempt", "nonce", "input_digest"},
        )
        self.assertEqual(case["case_id"], "search-absence")
        self.assertEqual(case["operation_type"], "constitutional_evaluation")
        self.assertEqual(case["rule_profile"], "alex-crucible-v1")
        self.assertEqual(case["nonce"], "n-001")
        for forbidden in ["expected", "constitutional_laws", "title", "notes", "version"]:
            self.assertNotIn(forbidden, case)

    def test_build_oracle_maps_expected_without_runtime_inputs(self):
        blind = self.load_module()
        case = blind.build_case(self.specimen(), nonce="n-001")
        oracle = blind.build_oracle(self.specimen(), case)
        self.assertEqual(
            oracle,
            {
                "case_id": "search-absence",
                "expected_disposition": "REFUSE",
                "expected_reason_code": "SEARCH_COVERAGE_INSUFFICIENT",
                "required_survivors": ["search_observation:S1"],
                "forbidden_outputs": ["source_absence"],
                "metamorphic_family": None,
            },
        )
        self.assertNotIn("given", oracle)
        self.assertNotIn("attempt", oracle)

    def test_canonical_digest_ignores_object_key_order_but_not_content(self):
        blind = self.load_module()
        left = {"b": 2, "a": {"y": 4, "x": 3}}
        right = {"a": {"x": 3, "y": 4}, "b": 2}
        changed = {"a": {"x": 3, "y": 5}, "b": 2}
        self.assertEqual(blind.sha256_json(left), blind.sha256_json(right))
        self.assertNotEqual(blind.sha256_json(left), blind.sha256_json(changed))
        self.assertTrue(blind.sha256_json(left).startswith("sha256:"))

    def test_input_digest_is_over_case_before_digest_field_is_inserted(self):
        blind = self.load_module()
        case = blind.build_case(self.specimen(), nonce="n-001")
        unsigned = dict(case)
        digest = unsigned.pop("input_digest")
        self.assertEqual(digest, blind.sha256_json(unsigned))

    def test_ruleset_digest_is_stable_and_profile_specific(self):
        blind = self.load_module()
        first = blind.ruleset_digest("alex-crucible-v1")
        second = blind.ruleset_digest("alex-crucible-v1")
        other = blind.ruleset_digest("alex-crucible-v2")
        self.assertEqual(first, second)
        self.assertNotEqual(first, other)
        self.assertTrue(first.startswith("sha256:"))


if __name__ == "__main__":
    unittest.main()
