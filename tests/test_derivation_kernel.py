import copy
import json
import unittest
from pathlib import Path

from alex_runtime.derivation import evaluate_relation_case, ruleset_manifest, ruleset_manifest_digest
from alex_runtime.digests import sha256_json
from tools.crucible_blind import build_case

ROOT = Path(__file__).resolve().parents[1]
SPECIMENS = ROOT / "crucible" / "specimens"


def load_case(name: str) -> dict:
    specimen = json.loads((SPECIMENS / name).read_text(encoding="utf-8"))
    return build_case(
        specimen,
        nonce=f"test-{name}",
        operation_type="relation_derivation",
        rule_profile="alex.runtime/derivation-m0",
    )


def redigest(case: dict) -> None:
    case.pop("input_digest", None)
    case["input_digest"] = sha256_json(case)


class RulesetManifestTests(unittest.TestCase):
    def test_derivation_m0_manifest_pins_rule_and_version(self):
        manifest = ruleset_manifest("alex.runtime/derivation-m0")
        self.assertEqual(manifest["profile"], "alex.runtime/derivation-m0")
        self.assertEqual(manifest["rules"][0]["rule_id"], "RELATION-DERIVATION-001")
        self.assertEqual(manifest["rules"][0]["rule_version"], 1)
        self.assertEqual(manifest["rules"][0]["predicate"], "SUPPORTS")

    def test_ruleset_digest_changes_if_manifest_changes(self):
        digest = ruleset_manifest_digest("alex.runtime/derivation-m0")
        self.assertTrue(digest.startswith("sha256:"))
        self.assertEqual(len(digest), 71)


class RelationDerivationTests(unittest.TestCase):
    def test_attention_chain_refuses_support(self):
        case = load_case("relation-derivation-001-attention-negative.json")
        result = evaluate_relation_case(case)

        self.assertEqual(result["execution"], {"terminal_state": "FINISHED", "step_count": 1})
        self.assertEqual(result["evaluation"]["disposition"], "REFUSE")
        self.assertEqual(result["evaluation"]["reason_code"], "ATTENTION_NOT_SUPPORT")
        self.assertIsNone(result["conclusion_assertion"])
        for survivor in [
            "record:B1",
            "record:Q1",
            "record:E1",
            "record:C1",
            "relation_proposal:RP1",
            "evaluation:EV1",
        ]:
            self.assertIn(survivor, result["evaluation"]["required_survivors"])

    def test_attributable_evidence_path_accepts_support(self):
        case = load_case("relation-derivation-001-evidence-positive.json")
        result = evaluate_relation_case(case)

        self.assertEqual(result["evaluation"]["disposition"], "ACCEPT")
        self.assertIsNone(result["evaluation"]["reason_code"])
        self.assertEqual(
            result["conclusion_assertion"],
            {
                "id": "AS1",
                "subject_id": "E1",
                "predicate": "SUPPORTS",
                "object_id": "C1",
                "scope": "candidate_claim:C1",
                "derived_by_evaluation_id": "EV1",
            },
        )
        self.assertIn("evidence_path:EP1", result["evaluation"]["required_survivors"])
        self.assertIn("conclusion_assertion:AS1", result["evaluation"]["required_survivors"])

    def test_missing_evidence_path_is_insufficient_when_not_attention_case(self):
        case = load_case("relation-derivation-001-evidence-positive.json")
        case["given"]["evidence_paths"] = []
        redigest(case)

        result = evaluate_relation_case(case)

        self.assertEqual(result["evaluation"]["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["evaluation"]["reason_code"], "NO_ATTRIBUTABLE_SUPPORT_PATH")
        self.assertIsNone(result["conclusion_assertion"])

    def test_evidence_path_requires_source_in_its_basis(self):
        case = load_case("relation-derivation-001-evidence-positive.json")
        case["given"]["evidence_paths"][0]["basis_ids"] = []
        redigest(case)

        result = evaluate_relation_case(case)

        self.assertEqual(result["evaluation"]["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["evaluation"]["reason_code"], "NO_ATTRIBUTABLE_SUPPORT_PATH")
        self.assertIsNone(result["conclusion_assertion"])

    def test_proposal_must_carry_evidence_path_in_declared_basis(self):
        case = load_case("relation-derivation-001-evidence-positive.json")
        case["attempt"]["relation_proposal"]["basis_ids"] = ["E1"]
        redigest(case)

        result = evaluate_relation_case(case)

        self.assertEqual(result["evaluation"]["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["evaluation"]["reason_code"], "PROPOSAL_BASIS_INSUFFICIENT")
        self.assertIsNone(result["conclusion_assertion"])

    def test_support_conclusion_requires_declared_scope(self):
        case = load_case("relation-derivation-001-evidence-positive.json")
        case["attempt"]["relation_proposal"]["scope"] = ""
        redigest(case)

        result = evaluate_relation_case(case)

        self.assertEqual(result["evaluation"]["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["evaluation"]["reason_code"], "MISSING_PROPOSAL_SCOPE")
        self.assertIsNone(result["conclusion_assertion"])

    def test_non_supports_predicate_is_outside_profile(self):
        case = load_case("relation-derivation-001-evidence-positive.json")
        case["attempt"]["relation_proposal"]["predicate"] = "RESEMBLES"
        redigest(case)

        result = evaluate_relation_case(case)

        self.assertEqual(result["evaluation"]["disposition"], "REFUSE")
        self.assertEqual(result["evaluation"]["reason_code"], "PREDICATE_OUTSIDE_PROFILE")
        self.assertIsNone(result["conclusion_assertion"])

    def test_missing_proposal_record_is_insufficient(self):
        case = load_case("relation-derivation-001-evidence-positive.json")
        case["given"]["records"] = [record for record in case["given"]["records"] if record["id"] != "C1"]
        redigest(case)

        result = evaluate_relation_case(case)

        self.assertEqual(result["evaluation"]["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["evaluation"]["reason_code"], "MISSING_PROPOSAL_RECORD")
        self.assertIsNone(result["conclusion_assertion"])

    def test_operation_outside_profile_is_insufficient(self):
        case = load_case("relation-derivation-001-evidence-positive.json")
        case["operation_type"] = "constitutional_evaluation"
        redigest(case)

        result = evaluate_relation_case(case)

        self.assertEqual(result["evaluation"]["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["evaluation"]["reason_code"], "OPERATION_OUTSIDE_PROFILE")
        self.assertIsNone(result["conclusion_assertion"])

    def test_rule_profile_outside_derivation_m0_is_insufficient(self):
        case = load_case("relation-derivation-001-evidence-positive.json")
        case["rule_profile"] = "alex.runtime/other-profile"
        redigest(case)

        result = evaluate_relation_case(case)

        self.assertEqual(result["evaluation"]["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["evaluation"]["reason_code"], "RULE_PROFILE_OUTSIDE_PROFILE")
        self.assertIsNone(result["conclusion_assertion"])

    def test_accept_does_not_emit_admission_state(self):
        case = load_case("relation-derivation-001-evidence-positive.json")
        result = evaluate_relation_case(case)

        forbidden = {"admitted", "authority", "canon", "publication", "warrant"}
        self.assertTrue(forbidden.isdisjoint(result["evaluation"]))
        self.assertTrue(forbidden.isdisjoint(result["conclusion_assertion"]))

    def test_source_case_is_not_mutated(self):
        case = load_case("relation-derivation-001-evidence-positive.json")
        before = copy.deepcopy(case)

        evaluate_relation_case(case)

        self.assertEqual(case, before)


if __name__ == "__main__":
    unittest.main()
