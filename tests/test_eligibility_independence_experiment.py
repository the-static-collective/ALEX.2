import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).parents[1] / "experiments" / "eligibility_independence.py"


def load_experiment():
    if not MODULE_PATH.exists():
        raise AssertionError("ELIGIBILITY-INDEPENDENCE-001 experiment module is missing")
    spec = importlib.util.spec_from_file_location("eligibility_independence", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


BASE = {
    "schema": "alex.experiment.eligibility-independence/v0",
    "grammar_id": "jubilee-little-yes-probe",
    "handoff_id": "handoff-001",
    "rows": [
        {
            "row_id": "eligible-no-authority",
            "structural_edge": True,
            "grammar_eligible": True,
            "observer_available": True,
            "capability_reachable": True,
            "authorized": False,
            "selected": False,
            "executed": False,
        },
        {
            "row_id": "eligible-hidden",
            "structural_edge": True,
            "grammar_eligible": True,
            "observer_available": False,
            "capability_reachable": True,
            "authorized": True,
            "selected": False,
            "executed": False,
        },
        {
            "row_id": "eligible-unreachable",
            "structural_edge": True,
            "grammar_eligible": True,
            "observer_available": True,
            "capability_reachable": False,
            "authorized": True,
            "selected": False,
            "executed": False,
        },
        {
            "row_id": "edge-not-eligible",
            "structural_edge": True,
            "grammar_eligible": False,
            "observer_available": True,
            "capability_reachable": True,
            "authorized": True,
            "selected": False,
            "executed": False,
        },
    ],
}


class EligibilityIndependenceExperimentTests(unittest.TestCase):
    def test_required_hostile_rows_are_witnessed_without_authority(self):
        result = load_experiment().audit_eligibility_matrix(BASE)
        self.assertEqual(result["disposition"], "MATRIX_WITNESSED")
        self.assertEqual(result["missing_witnesses"], [])
        self.assertEqual(result["grammar_id"], BASE["grammar_id"])
        self.assertEqual(result["handoff_id"], BASE["handoff_id"])
        self.assertEqual(result["authority"], "none")

    def test_representable_row_can_be_rejected_by_separate_tiny_grammar(self):
        experiment = load_experiment()
        matrix_result = experiment.audit_eligibility_matrix(BASE)
        grammar_result = experiment.audit_tiny_grammar_row(
            BASE["rows"][1], grammar_id=BASE["grammar_id"]
        )

        self.assertEqual(matrix_result["disposition"], "MATRIX_WITNESSED")
        self.assertEqual(grammar_result["disposition"], "GRAMMAR_REJECTED")
        self.assertEqual(
            grammar_result["reason"],
            "eligible_requires_observer_and_capability",
        )
        self.assertFalse(grammar_result["reachable_under_tiny_grammar"])
        self.assertEqual(grammar_result["row_id"], "eligible-hidden")
        self.assertEqual(grammar_result["authority"], "none")


if __name__ == "__main__":
    unittest.main()
