import copy
import json
import unittest
from pathlib import Path

from alex_runtime.projection_break import evaluate_projection_break_case

ROOT = Path(__file__).resolve().parents[1]
SPECIMENS = ROOT / "tests" / "fixtures" / "projection_break"


def load_case(name: str = "hidden-adjacency.json") -> dict:
    return json.loads((SPECIMENS / name).read_text(encoding="utf-8"))


class ProjectionBreakTests(unittest.TestCase):
    def test_same_intervention_can_reveal_a_future_projection_difference(self):
        case = load_case()

        result = evaluate_projection_break_case(case)

        self.assertEqual(result["case_id"], case["case_id"])
        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertIsNone(result["reason_code"])
        self.assertEqual(result["pre_disposition"], "ACCEPT")
        self.assertEqual(result["break_boundary"], "PROJECTION")
        self.assertIn("intervention:edge-touch-001", result["receipt_survivors"])
        self.assertIn("receipt:hidden-adjacency-left", result["receipt_survivors"])
        self.assertIn("receipt:hidden-adjacency-right", result["receipt_survivors"])

    def test_shared_intervention_must_be_attributable_on_both_post_worlds(self):
        case = load_case()
        case["post"]["right"]["receipt_refs"].remove("intervention:edge-touch-001")

        result = evaluate_projection_break_case(case)

        self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["reason_code"], "INTERVENTION_NOT_ATTRIBUTABLE")
        self.assertIsNone(result["break_boundary"])

    def test_pre_worlds_must_actually_be_projection_invariant(self):
        case = load_case()
        case["pre"]["right"]["projection_digest"] = "sha256:already-different"

        result = evaluate_projection_break_case(case)

        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason_code"], "PRECONDITION_NOT_INVARIANT")
        self.assertEqual(result["pre_reason_code"], "PROJECTION_LEAK")

    def test_post_worlds_must_receive_the_same_declared_input(self):
        case = load_case()
        case["post"]["right"]["visible_input_digest"] = "sha256:different-intervention-input"

        result = evaluate_projection_break_case(case)

        self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["reason_code"], "POST_INPUT_NOT_EQUIVALENT")

    def test_authority_may_not_change_as_part_of_the_break(self):
        case = load_case()
        case["post"]["right"]["authority_digest"] = "sha256:changed-authority"

        result = evaluate_projection_break_case(case)

        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason_code"], "AUTHORITY_CHANGED")
        self.assertEqual(result["break_boundary"], "AUTHORITY")

    def test_no_future_difference_is_not_a_break(self):
        case = load_case()
        for field in (
            "bounded_context_digest",
            "projection_digest",
            "derivation_digest",
            "serialization_digest",
            "narrative_digest",
        ):
            case["post"]["right"][field] = case["post"]["left"][field]

        result = evaluate_projection_break_case(case)

        self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["reason_code"], "NO_BREAK_OBSERVED")
        self.assertIsNone(result["break_boundary"])

    def test_hidden_difference_receipts_must_survive_the_intervention(self):
        case = load_case()
        case["post"]["left"]["receipt_refs"].remove("receipt:hidden-adjacency-left")

        result = evaluate_projection_break_case(case)

        self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["reason_code"], "HIDDEN_DIFFERENCE_NOT_ATTRIBUTABLE")

    def test_evaluator_does_not_mutate_source_case(self):
        case = load_case()
        before = copy.deepcopy(case)

        evaluate_projection_break_case(case)

        self.assertEqual(case, before)

    def test_result_carries_no_external_authority_surface(self):
        result = evaluate_projection_break_case(load_case())

        forbidden = {"authority", "admitted", "canon", "publication", "warrant", "execution_authority"}
        self.assertTrue(forbidden.isdisjoint(result))


if __name__ == "__main__":
    unittest.main()
