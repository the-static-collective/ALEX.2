import unittest

from alex_runtime.name_nulls import evaluate_name_null_battery
from tests.test_name_nulls import make_battery


class NameNullBatteryReviewTests(unittest.TestCase):
    def test_battery_cannot_predeclare_expected_answer(self):
        battery = make_battery()
        battery["expected_answer"] = "favored hypothesis survives"
        result = evaluate_name_null_battery(battery)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "favored_answer_not_allowed")

    def test_control_cannot_predeclare_expected_outcome(self):
        battery = make_battery()
        battery["controls"][0]["expected_outcome"] = "still hits"
        result = evaluate_name_null_battery(battery)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "favored_answer_not_allowed")

    def test_control_cannot_mark_survival_expected(self):
        battery = make_battery()
        battery["controls"][1]["survival_expected"] = True
        result = evaluate_name_null_battery(battery)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "favored_answer_not_allowed")


if __name__ == "__main__":
    unittest.main()
