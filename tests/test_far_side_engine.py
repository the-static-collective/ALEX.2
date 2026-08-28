import copy
import unittest

from experiments.far_side.engine import evaluate_far_side_case
from tests.test_far_side_model import VALID_CASE


class FarSideEngineTests(unittest.TestCase):
    def test_three_distinct_axes_and_full_regeneration_can_reach_no_novelty_success(self):
        result = evaluate_far_side_case(copy.deepcopy(VALID_CASE))

        self.assertEqual(result["final_status"], "NO_NEW_DIMENSION_EARNED")
        self.assertIsNone(result["reason_code"])
        self.assertEqual(
            result["traversal_axes"],
            ["DIRECTION", "REPRESENTATION", "SCALE"],
        )
        self.assertEqual(result["surviving_invariants"], ["inv:route-host-distinction"])
        self.assertEqual(result["missing_targets"], [])
        self.assertEqual(result["novelty_delta"], [])

    def test_fewer_than_three_material_axes_is_insufficient(self):
        case = copy.deepcopy(VALID_CASE)
        case["traversals"][2]["axis"] = "SCALE"

        result = evaluate_far_side_case(case)

        self.assertEqual(result["final_status"], "INSUFFICIENT_RECEIPT")
        self.assertEqual(result["reason_code"], "INSUFFICIENT_TRAVERSAL_DIVERSITY")

    def test_some_but_not_all_required_targets_yields_partial_survivor(self):
        case = copy.deepcopy(VALID_CASE)
        case["candidate"]["required_targets"] = [
            "inv:route-host-distinction",
            "inv:opening-transition-distinction",
        ]
        case["candidate"]["regenerated_targets"] = ["inv:route-host-distinction"]

        result = evaluate_far_side_case(case)

        self.assertEqual(result["final_status"], "PARTIAL_SURVIVOR")
        self.assertEqual(result["missing_targets"], ["inv:opening-transition-distinction"])

    def test_zero_required_targets_regenerated_is_compression_failure(self):
        case = copy.deepcopy(VALID_CASE)
        case["candidate"]["regenerated_targets"] = []

        result = evaluate_far_side_case(case)

        self.assertEqual(result["final_status"], "COMPRESSION_FAILED_REGENERATION")
        self.assertEqual(result["reason_code"], "NO_REQUIRED_TARGET_REGENERATED")

    def test_evaluator_does_not_mutate_input(self):
        case = copy.deepcopy(VALID_CASE)
        before = copy.deepcopy(case)
        evaluate_far_side_case(case)
        self.assertEqual(case, before)

    def test_result_has_no_authority_surface(self):
        result = evaluate_far_side_case(copy.deepcopy(VALID_CASE))
        forbidden = {
            "authority",
            "support",
            "evidence",
            "canon",
            "admitted",
            "publication",
            "execution_authority",
        }
        self.assertTrue(forbidden.isdisjoint(result))

    def test_dimensional_novelty_plus_passing_pressure_earns_survivor(self):
        case = copy.deepcopy(VALID_CASE)
        case["candidate"]["novelty"] = [
            {
                "type": "NEW_DERIVATION",
                "statement": "A closed cubic route leaves a 1-regular residual field.",
                "discriminator": "Compare the Hamiltonian-cycle sibling with a Hamiltonian path.",
                "receipt_ref": "receipt:novelty:residual",
            }
        ]

        result = evaluate_far_side_case(case)

        self.assertEqual(result["final_status"], "FAR_SIDE_SURVIVOR")
        self.assertEqual(len(result["novelty_delta"]), 1)
        self.assertEqual(result["novelty_delta"][0]["type"], "NEW_DERIVATION")

    def test_exact_baseline_duplicate_does_not_count_as_novelty(self):
        case = copy.deepcopy(VALID_CASE)
        case["candidate"]["novelty"] = [
            {
                "type": "NEW_RELATION",
                "statement": "  Route   is not\n host topology. ",
                "discriminator": "Would differ under an exhaustive-host claim.",
                "receipt_ref": "receipt:novelty:duplicate",
            }
        ]

        result = evaluate_far_side_case(case)

        self.assertEqual(result["final_status"], "NO_NEW_DIMENSION_EARNED")
        self.assertEqual(result["novelty_delta"], [])

    def test_wording_only_delta_is_reported_but_does_not_earn_new_dimension(self):
        case = copy.deepcopy(VALID_CASE)
        case["candidate"]["novelty"] = [
            {
                "type": "NEW_WORDING",
                "statement": "The traveled road is smaller than the road field.",
                "discriminator": "Compare semantic content against baseline manually.",
                "receipt_ref": "receipt:novelty:wording",
            }
        ]

        result = evaluate_far_side_case(case)

        self.assertEqual(result["final_status"], "NO_NEW_DIMENSION_EARNED")
        self.assertEqual(result["novelty_delta"][0]["type"], "NEW_WORDING")

    def test_failed_metaphor_removal_prevents_survivor(self):
        case = copy.deepcopy(VALID_CASE)
        case["candidate"]["novelty"] = [
            {
                "type": "NEW_INVARIANT",
                "statement": "A residual relation remains after removing the route.",
                "discriminator": "Compute graph difference after relabeling all metaphors.",
                "receipt_ref": "receipt:novelty:invariant",
            }
        ]
        for check in case["pressure"]:
            if check["kind"] == "METAPHOR_REMOVAL":
                check["status"] = "FAIL"

        result = evaluate_far_side_case(case)

        self.assertEqual(result["final_status"], "PARTIAL_SURVIVOR")
        self.assertEqual(result["reason_code"], "HOSTILE_PRESSURE_FAILED")
        self.assertEqual(result["pressure_failures"], ["METAPHOR_REMOVAL"])

    def test_missing_required_pressure_receipt_is_insufficient(self):
        case = copy.deepcopy(VALID_CASE)
        case["pressure"] = [
            check for check in case["pressure"] if check["kind"] != "HOLDOUT"
        ]

        result = evaluate_far_side_case(case)

        self.assertEqual(result["final_status"], "INSUFFICIENT_RECEIPT")
        self.assertEqual(result["reason_code"], "MISSING_REQUIRED_PRESSURE")

    def test_relabeling_case_and_receipt_ids_does_not_change_structural_status(self):
        left = copy.deepcopy(VALID_CASE)
        right = copy.deepcopy(VALID_CASE)
        right["case_id"] = "far-side:banana-labels"
        for index, traversal in enumerate(right["traversals"]):
            traversal["id"] = f"banana:{index}"
            traversal["receipt_ref"] = f"receipt:banana:{index}"
        for index, check in enumerate(right["pressure"]):
            check["receipt_ref"] = f"receipt:pressure:banana:{index}"

        left_result = evaluate_far_side_case(left)
        right_result = evaluate_far_side_case(right)

        self.assertEqual(left_result["final_status"], right_result["final_status"])
        self.assertEqual(left_result["traversal_axes"], right_result["traversal_axes"])
        self.assertEqual(left_result["surviving_invariants"], right_result["surviving_invariants"])
        self.assertEqual(left_result["missing_targets"], right_result["missing_targets"])


if __name__ == "__main__":
    unittest.main()
