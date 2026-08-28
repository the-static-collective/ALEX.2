import copy
import json
import unittest
from pathlib import Path

from alex_runtime.mediated_support import evaluate_mediated_support_case
from tools.crucible_blind import build_case

ROOT = Path(__file__).resolve().parents[1]
PAIR_FIXTURES = ROOT / "tests" / "fixtures" / "mediated_support"
DERIVATION_SPECIMENS = ROOT / "crucible" / "specimens"


def load_derivation_case(name: str, nonce: str) -> dict:
    specimen = json.loads((DERIVATION_SPECIMENS / name).read_text(encoding="utf-8"))
    return build_case(
        specimen,
        nonce=nonce,
        operation_type="relation_derivation",
        rule_profile="alex.runtime/derivation-m0",
    )


def load_pair() -> dict:
    pair = json.loads((PAIR_FIXTURES / "mediated-support-001.json").read_text(encoding="utf-8"))
    for side_name in ("left", "right"):
        side = pair[side_name]
        fixture = side.pop("derivation_fixture")
        side["derivation_case"] = load_derivation_case(fixture, nonce=f"mediated-{side_name}")
    return pair


def rename_evidence_basis(case: dict, suffix: str) -> dict:
    updated = copy.deepcopy(case)
    old_source = updated["attempt"]["relation_proposal"]["subject_id"]
    new_source = f"{old_source}-{suffix}"
    old_path = updated["attempt"]["relation_proposal"]["basis_ids"][1]
    new_path = f"{old_path}-{suffix}"

    for record in updated["given"]["records"]:
        if record.get("id") == old_source:
            record["id"] = new_source

    for path in updated["given"]["evidence_paths"]:
        if path.get("id") == old_path:
            path["id"] = new_path
            path["source_id"] = new_source
            path["basis_ids"] = [new_source if value == old_source else value for value in path["basis_ids"]]

    proposal = updated["attempt"]["relation_proposal"]
    proposal["subject_id"] = new_source
    proposal["basis_ids"] = [new_source, new_path]
    updated["attempt"]["conclusion_assertion_id"] = f"AS-{suffix}"
    return updated


class MediatedSupportTests(unittest.TestCase):
    def test_interest_difference_with_fixed_evidence_has_zero_direct_support_effect(self):
        result = evaluate_mediated_support_case(load_pair())

        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertIsNone(result["reason_code"])
        self.assertEqual(result["mediation_status"], "DIRECT_EFFECT_ZERO")
        self.assertFalse(result["support_changed"])
        self.assertEqual(
            result["left"]["evidence_basis_digest"],
            result["right"]["evidence_basis_digest"],
        )
        self.assertEqual(
            result["left"]["support_result_digest"],
            result["right"]["support_result_digest"],
        )

    def test_interest_receipt_may_not_enter_gate2_support_basis(self):
        case = load_pair()
        right = case["right"]
        right["selection"]["consumed_interest_receipt_refs"] = ["interest:q"]
        right["derivation_case"]["attempt"]["relation_proposal"]["basis_ids"].append("interest:q")

        result = evaluate_mediated_support_case(case)

        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason_code"], "INTEREST_AS_SUPPORT")

    def test_consumed_interest_may_change_support_only_through_changed_evidence(self):
        case = load_pair()
        right = case["right"]
        right["selection"] = {
            "policy_digest": "sha256:interest-selector-v1",
            "receipt_refs": ["selection:interest-guided"],
            "consumed_interest_receipt_refs": ["interest:q"],
        }
        right["bounded_context_digest"] = "sha256:context-interest-guided"
        right["projection_digest"] = "sha256:projection-interest-guided"
        right["derivation_case"] = rename_evidence_basis(right["derivation_case"], "guided")

        result = evaluate_mediated_support_case(case)

        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertIsNone(result["reason_code"])
        self.assertEqual(result["mediation_status"], "LAWFUL_MEDIATION")
        self.assertNotEqual(
            result["left"]["evidence_basis_digest"],
            result["right"]["evidence_basis_digest"],
        )
        self.assertIn("interest:q", result["receipt_survivors"])
        self.assertIn("selection:interest-guided", result["receipt_survivors"])

    def test_population_claim_requires_selection_formation(self):
        case = load_pair()
        case["claim_class"] = "POPULATION_GENERALIZATION"
        case["right"]["selection"] = {
            "policy_digest": None,
            "receipt_refs": [],
            "consumed_interest_receipt_refs": [],
        }

        result = evaluate_mediated_support_case(case)

        self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["reason_code"], "SELECTION_FORMATION_REQUIRED")

    def test_object_local_support_does_not_require_selection_history(self):
        case = load_pair()
        case["right"]["selection"] = {
            "policy_digest": None,
            "receipt_refs": [],
            "consumed_interest_receipt_refs": [],
        }

        result = evaluate_mediated_support_case(case)

        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertEqual(result["mediation_status"], "DIRECT_EFFECT_ZERO")

    def test_evaluator_does_not_mutate_source_case(self):
        case = load_pair()
        before = copy.deepcopy(case)
        evaluate_mediated_support_case(case)
        self.assertEqual(case, before)

    def test_result_carries_no_external_authority_surface(self):
        result = evaluate_mediated_support_case(load_pair())
        forbidden = {"authority", "admitted", "canon", "publication", "warrant", "execution_authority"}
        self.assertTrue(forbidden.isdisjoint(result))

    def test_malformed_side_is_insufficient(self):
        case = load_pair()
        case["right"]["projection_digest"] = ""

        result = evaluate_mediated_support_case(case)

        self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["reason_code"], "MALFORMED_CASE")

    def test_claim_identity_must_match_both_derivation_cases(self):
        case = load_pair()
        case["right"]["derivation_case"]["attempt"]["relation_proposal"]["object_id"] = "OTHER"
        result = evaluate_mediated_support_case(case)
        self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["reason_code"], "CLAIM_ID_MISMATCH")


if __name__ == "__main__":
    unittest.main()
