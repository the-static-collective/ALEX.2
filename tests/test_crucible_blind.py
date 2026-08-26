import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "crucible" / "schema"
BLIND = ROOT / "tools" / "crucible_blind.py"
FIXTURES = ROOT / "tests" / "fixtures"


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


class MetamorphicSiblingTests(unittest.TestCase):
    def load_module(self):
        spec = importlib.util.spec_from_file_location("crucible_blind_metamorphic", BLIND)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertTrue(
            hasattr(module, "metamorphic_sibling"),
            "Blind Crucible must generate runtime surface siblings without changing semantics",
        )
        return module

    def base_case(self, blind) -> dict:
        specimen = {
            "id": "surface-pressure",
            "given": {
                "relations": [
                    {"from": "A", "predicate": "near", "to": "B"},
                    {"from": "B", "predicate": "near", "to": "C"},
                ]
            },
            "attempt": {"promote": "source_absence"},
            "expected": {
                "disposition": "REFUSE",
                "refusal_code": "SEARCH_COVERAGE_INSUFFICIENT",
                "required_receipt_survivors": [],
                "forbidden_promotions": ["source_absence"],
            },
        }
        return blind.build_case(specimen, nonce="base-nonce")

    def test_sibling_changes_surface_identity_but_preserves_operation(self):
        blind = self.load_module()
        base = self.base_case(blind)
        sibling = blind.metamorphic_sibling(base, suffix="-m1", nonce="sibling-nonce")
        self.assertEqual(sibling["case_id"], "surface-pressure-m1")
        self.assertEqual(sibling["nonce"], "sibling-nonce")
        self.assertNotEqual(sibling["input_digest"], base["input_digest"])
        self.assertEqual(sibling["operation_type"], base["operation_type"])
        self.assertEqual(sibling["rule_profile"], base["rule_profile"])
        self.assertEqual(sibling["attempt"], base["attempt"])

    def test_sibling_reorders_relations_adds_distractor_and_does_not_mutate_parent(self):
        blind = self.load_module()
        base = self.base_case(blind)
        original_relations = json.loads(json.dumps(base["given"]["relations"]))
        distractor = {"from": "X", "predicate": "unrelated", "to": "Y"}
        sibling = blind.metamorphic_sibling(
            base,
            suffix="-m2",
            nonce="sibling-2",
            distractor_relation=distractor,
        )
        self.assertEqual(base["given"]["relations"], original_relations)
        self.assertEqual(sibling["given"]["relations"][:2], list(reversed(original_relations)))
        self.assertEqual(sibling["given"]["relations"][-1], distractor)

    def test_surface_siblings_keep_reference_adapter_disposition_stable(self):
        blind = self.load_module()
        base = self.base_case(blind)
        sibling = blind.metamorphic_sibling(
            base,
            suffix="-m3",
            nonce="sibling-3",
            distractor_relation={"from": "X", "predicate": "unrelated", "to": "Y"},
        )
        dispositions = []
        for case in [base, sibling]:
            completed = subprocess.run(
                [sys.executable, str(FIXTURES / "adapter_relation_surface_reference.py")],
                input=json.dumps(case),
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
            result = json.loads(completed.stdout)
            dispositions.append(result["disposition"])
        self.assertEqual(dispositions, ["REFUSE", "REFUSE"])


if __name__ == "__main__":
    unittest.main()
