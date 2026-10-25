import unittest

import experiments.criterion_not_policy as criterion_not_policy


class CriterionAgreementControlTests(unittest.TestCase):
    def test_one_fixture_agreement_does_not_establish_criterion_equivalence(self):
        self.assertTrue(
            hasattr(criterion_not_policy, "evaluate_criterion_agreement_control"),
            "criterion-agreement pressure probe must exist",
        )

        receipt = criterion_not_policy.evaluate_criterion_agreement_control()

        self.assertEqual(receipt["experiment"], "CRITERION-AGREEMENT-CONTROL-001")
        self.assertEqual(receipt["authority"], "none")

        baseline = receipt["baseline_fixture"]
        self.assertEqual(baseline["worst_case_ranking"], "FIXED")
        self.assertEqual(baseline["expected_cost_uniform_ranking"], "FIXED")
        self.assertTrue(baseline["verdicts_agree"])

        pressure = receipt["pressure_fixture"]
        self.assertEqual(
            pressure["costs"],
            {"ADAPTIVE": [1, 1, 1, 10], "FIXED": [4, 4, 4, 4]},
        )
        self.assertEqual(pressure["worst_case"]["ranking"], "FIXED")
        self.assertEqual(pressure["expected_cost_uniform"]["ranking"], "ADAPTIVE")
        self.assertFalse(pressure["verdicts_agree"])
        self.assertFalse(receipt["equivalence_claim_survives_pressure"])
        self.assertEqual(
            receipt["observation"],
            "VERDICT_AGREEMENT_ON_ONE_FIXTURE_DOES_NOT_ESTABLISH_CRITERION_EQUIVALENCE",
        )


if __name__ == "__main__":
    unittest.main()
