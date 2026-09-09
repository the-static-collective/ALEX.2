import unittest
from fractions import Fraction

from experiments.criterion_not_policy import evaluate_frozen_policy_table


class CriterionNotPolicyExperimentTests(unittest.TestCase):
    def test_same_statewise_table_supports_distinct_lawful_rankings(self):
        receipt = evaluate_frozen_policy_table()

        self.assertEqual(receipt["authority"], "none")
        self.assertEqual(receipt["state_space"], ["a", "b", "c", "d"])
        self.assertEqual(receipt["costs"], {
            "ADAPTIVE": [1, 3, 3, 3],
            "FIXED": [2, 2, 2, 2],
        })

        self.assertEqual(receipt["worst_case"], {
            "criterion": "worst_case_cost",
            "ADAPTIVE": 3,
            "FIXED": 2,
            "ranking": "FIXED",
        })
        self.assertEqual(receipt["expected_cost_heavy"], {
            "criterion": "expected_cost",
            "prior": [Fraction(3, 4), Fraction(1, 12), Fraction(1, 12), Fraction(1, 12)],
            "ADAPTIVE": Fraction(3, 2),
            "FIXED": Fraction(2, 1),
            "ranking": "ADAPTIVE",
        })
        self.assertEqual(receipt["expected_cost_uniform"], {
            "criterion": "expected_cost",
            "prior": [Fraction(1, 4)] * 4,
            "ADAPTIVE": Fraction(5, 2),
            "FIXED": Fraction(2, 1),
            "ranking": "FIXED",
        })
        self.assertEqual(receipt["minimax_regret"], {
            "criterion": "minimax_regret",
            "oracle": [1, 2, 2, 2],
            "ADAPTIVE_regret": [0, 1, 1, 1],
            "FIXED_regret": [1, 0, 0, 0],
            "ADAPTIVE": 1,
            "FIXED": 1,
            "ranking": "TIE",
        })

        self.assertEqual(
            receipt["observation"],
            "STATEWISE_COST_TABLE_DOES_NOT_SELECT_POLICY_WITHOUT_CRITERION",
        )

    def test_criterion_identity_is_preserved_even_when_verdict_agrees(self):
        receipt = evaluate_frozen_policy_table()

        self.assertEqual(receipt["worst_case"]["ranking"], "FIXED")
        self.assertEqual(receipt["expected_cost_uniform"]["ranking"], "FIXED")
        self.assertNotEqual(
            receipt["worst_case"]["criterion"],
            receipt["expected_cost_uniform"]["criterion"],
        )


if __name__ == "__main__":
    unittest.main()
