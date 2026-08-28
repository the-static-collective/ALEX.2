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
