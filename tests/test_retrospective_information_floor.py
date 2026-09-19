import unittest

from experiments.retrospective_information_floor import retrospective_view_from_retained_carrier


class RetrospectiveInformationFloorTests(unittest.TestCase):
    def test_collapsed_carrier_does_not_resurrect_a_or_b(self):
        retained = {
            "receipt_id": "receipt:t0-collapsed",
            "value": "X",
            "source_candidates": ("a", "b"),
        }
        rule = {"a": "P", "b": "Q"}

        result = retrospective_view_from_retained_carrier(
            retained=retained,
            later_rule=rule,
            declared_at=20,
            applied_at=30,
        )

        self.assertEqual(result["status"], "DISTINCTION_UNRECOVERABLE_FROM_RETAINED_CARRIER")
        self.assertIsNone(result["source_value"])
        self.assertIsNone(result["derived_value"])
        self.assertEqual(result["retained_source_candidates"], ["a", "b"])
        self.assertEqual(result["authority"], "none")

    def test_retained_distinction_can_support_later_view(self):
        retained = {
            "receipt_id": "receipt:t0-raw-a",
            "value": "a",
            "source_candidates": ("a",),
        }
        rule = {"a": "P", "b": "Q"}

        result = retrospective_view_from_retained_carrier(
            retained=retained,
            later_rule=rule,
            declared_at=20,
            applied_at=30,
        )

        self.assertEqual(result["status"], "DERIVED_FROM_RETAINED_DISTINCTION")
        self.assertEqual(result["source_value"], "a")
        self.assertEqual(result["derived_value"], "P")
        self.assertEqual(result["derived_from"], "receipt:t0-raw-a")

    def test_rule_cannot_apply_before_declaration(self):
        result = retrospective_view_from_retained_carrier(
            retained={"receipt_id": "receipt:t0", "value": "a", "source_candidates": ("a",)},
            later_rule={"a": "P"},
            declared_at=20,
            applied_at=10,
        )

        self.assertEqual(result["status"], "REFUSE")
        self.assertEqual(result["reason"], "rule-not-yet-declared")
        self.assertEqual(result["authority"], "none")


if __name__ == "__main__":
    unittest.main()
