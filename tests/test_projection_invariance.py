import copy
import json
import unittest
from pathlib import Path

from alex_runtime.projection_invariance import evaluate_projection_invariance_case

ROOT = Path(__file__).resolve().parents[1]
SPECIMENS = ROOT / "tests" / "fixtures" / "projection_invariance"


def load_case(name: str) -> dict:
    return json.loads((SPECIMENS / name).read_text(encoding="utf-8"))


class ProjectionInvarianceTests(unittest.TestCase):
    def test_clean_pair_accepts_when_hidden_world_difference_does_not_cross_projection(self):
        case = load_case("clean.json")

        result = evaluate_projection_invariance_case(case)

        self.assertEqual(result["case_id"], case["case_id"])
        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertIsNone(result["reason_code"])
        self.assertIsNone(result["leaking_boundary"])
        self.assertEqual(
            result["receipt_survivors"],
            ["receipt:left-world", "receipt:observer-cut", "receipt:right-world"],
        )

    def test_projection_leak_is_named_before_downstream_derivation_difference(self):
        case = load_case("projection-leak.json")

        result = evaluate_projection_invariance_case(case)

        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason_code"], "PROJECTION_LEAK")
        self.assertEqual(result["leaking_boundary"], "PROJECTION")
        self.assertIn("receipt:hidden-state-taint", result["receipt_survivors"])

    def test_declared_narrative_transform_allows_only_receipted_narrative_difference(self):
        case = load_case("foreshadow-control.json")

        result = evaluate_projection_invariance_case(case)

        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertIsNone(result["reason_code"])
        self.assertIsNone(result["leaking_boundary"])
        self.assertIn("transform:foreshadow-001", result["receipt_survivors"])

    def test_unreceipted_narrative_difference_is_a_leak(self):
        case = load_case("foreshadow-control.json")
        case["right"]["receipt_refs"].remove("transform:foreshadow-001")

        result = evaluate_projection_invariance_case(case)

        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason_code"], "NARRATIVE_LEAK")
        self.assertEqual(result["leaking_boundary"], "NARRATIVE")

    def test_authority_change_is_refused_even_when_projection_is_invariant(self):
        case = load_case("clean.json")
        case["right"]["authority_digest"] = "sha256:ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"

        result = evaluate_projection_invariance_case(case)

        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason_code"], "AUTHORITY_CHANGED")
        self.assertEqual(result["leaking_boundary"], "AUTHORITY")

    def test_visible_input_mismatch_is_not_an_invariance_trial(self):
        case = load_case("clean.json")
        case["right"]["visible_input_digest"] = "sha256:ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"

        result = evaluate_projection_invariance_case(case)

        self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["reason_code"], "VISIBLE_INPUT_NOT_EQUIVALENT")
        self.assertIsNone(result["leaking_boundary"])

    def test_observer_constraint_mismatch_is_not_an_invariance_trial(self):
        case = load_case("clean.json")
        case["right"]["observer_constraints_digest"] = "sha256:ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"

        result = evaluate_projection_invariance_case(case)

        self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["reason_code"], "OBSERVER_CONSTRAINTS_NOT_EQUIVALENT")
        self.assertIsNone(result["leaking_boundary"])

    def test_worlds_must_be_materially_distinct(self):
        case = load_case("clean.json")
        case["right"]["world_digest"] = case["left"]["world_digest"]

        result = evaluate_projection_invariance_case(case)

        self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["reason_code"], "WORLDS_NOT_MATERIALLY_DISTINCT")

    def test_evaluator_does_not_mutate_source_case(self):
        case = load_case("clean.json")
        before = copy.deepcopy(case)

        evaluate_projection_invariance_case(case)

        self.assertEqual(case, before)

    def test_result_carries_no_external_authority_surface(self):
        case = load_case("clean.json")

        result = evaluate_projection_invariance_case(case)

        forbidden = {"authority", "admitted", "canon", "publication", "warrant", "execution_authority"}
        self.assertTrue(forbidden.isdisjoint(result))


if __name__ == "__main__":
    unittest.main()
