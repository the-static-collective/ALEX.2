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


if __name__ == "__main__":
    unittest.main()
