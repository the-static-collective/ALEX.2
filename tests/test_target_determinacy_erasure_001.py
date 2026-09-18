import copy
import json
import unittest
from pathlib import Path

from research.target_determinacy_erasure_001 import evaluate_target_determinacy_case

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "target_determinacy_erasure" / "five-frontiers.json"


def load_cases() -> list[dict]:
    payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
    assert payload["specimen"] == "TARGET-DETERMINACY-ERASURE-001"
    return payload["cases"]


class TargetDeterminacyErasure001Tests(unittest.TestCase):
    def test_all_five_coarse_projections_fail_for_their_declared_targets(self):
        for case in load_cases():
            with self.subTest(case_id=case["case_id"]):
                result = evaluate_target_determinacy_case(case)
                self.assertEqual(result["disposition"], "DOES_NOT_DETERMINE")
                self.assertIsNotNone(result["violating_pair"])
                self.assertEqual(result["authority"], "none")

    def test_each_declared_refinement_restores_determinacy_in_the_finite_fixture(self):
        for case in load_cases():
            with self.subTest(case_id=case["case_id"]):
                result = evaluate_target_determinacy_case(case)
                self.assertIsNotNone(result["refinement"])
                self.assertEqual(
                    result["refinement"]["disposition"],
                    "DETERMINES_FOR_TARGET",
                )
                self.assertIsNone(result["refinement"]["violating_pair"])

    def test_semantic_equality_does_not_determine_evidence_posture(self):
        case = next(c for c in load_cases() if c["case_id"] == "semantic-evidence-posture")
        result = evaluate_target_determinacy_case(case)
        witness = result["violating_pair"]

        self.assertEqual(witness["shared_projection"], {"semantic_text": "The bank moved."})
        self.assertNotEqual(witness["left_target"], witness["right_target"])

    def test_untyped_graph_signature_does_not_determine_typed_orientation(self):
        case = next(c for c in load_cases() if c["case_id"] == "typed-role-orientation")
        result = evaluate_target_determinacy_case(case)

        self.assertEqual(
            result["violating_pair"]["shared_projection"],
            {"untyped_graph_signature": "G"},
        )

    def test_subject_occurrence_plus_surface_digest_does_not_determine_historical_binding(self):
        case = next(c for c in load_cases() if c["case_id"] == "surface-chronology")
        result = evaluate_target_determinacy_case(case)

        self.assertEqual(result["disposition"], "DOES_NOT_DETERMINE")
        self.assertEqual(
            result["refinement"]["added_fields"],
            ["publication_relation"],
        )

    def test_same_carrier_and_selector_do_not_determine_historical_reading_without_grammar_cut(self):
        case = next(c for c in load_cases() if c["case_id"] == "grammar-as-of")
        result = evaluate_target_determinacy_case(case)

        self.assertEqual(result["disposition"], "DOES_NOT_DETERMINE")
        self.assertEqual(result["refinement"]["added_fields"], ["grammar_as_of"])

    def test_observed_pre_post_history_does_not_determine_causal_model_class(self):
        case = next(c for c in load_cases() if c["case_id"] == "counterfactual-causal-world")
        result = evaluate_target_determinacy_case(case)

        self.assertEqual(result["disposition"], "DOES_NOT_DETERMINE")
        self.assertEqual(
            result["violating_pair"]["shared_projection"],
            {"observed_pre_post": "G0-E-G1"},
        )
        self.assertNotIn("caused_by", result)

    def test_positive_control_projection_can_already_determine_target(self):
        case = {
            "case_id": "positive-control",
            "target_kind": "binary_label",
            "projection_fields": ["visible"],
            "target_field": "label",
            "states": [
                {"state_id": "a", "visible": 0, "label": "left"},
                {"state_id": "b", "visible": 1, "label": "right"},
            ],
        }

        result = evaluate_target_determinacy_case(case)

        self.assertEqual(result["disposition"], "DETERMINES_FOR_TARGET")
        self.assertIsNone(result["violating_pair"])
        self.assertIsNone(result["refinement"])

    def test_duplicate_state_identity_is_refused(self):
        case = copy.deepcopy(load_cases()[0])
        case["states"][1]["state_id"] = case["states"][0]["state_id"]

        result = evaluate_target_determinacy_case(case)

        self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["reason_code"], "DUPLICATE_STATE_ID")

    def test_refinement_must_add_a_new_coordinate(self):
        case = copy.deepcopy(load_cases()[0])
        case["refinement_fields"] = ["semantic_text"]

        result = evaluate_target_determinacy_case(case)

        self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(
            result["reason_code"],
            "REFINEMENT_REPEATS_PROJECTION_FIELD",
        )

    def test_evaluator_does_not_mutate_case(self):
        case = load_cases()[0]
        before = copy.deepcopy(case)

        evaluate_target_determinacy_case(case)

        self.assertEqual(case, before)


if __name__ == "__main__":
    unittest.main()
