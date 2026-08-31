import copy
import unittest

from experiments.far_side.model import (
    DIMENSIONAL_NOVELTY_TYPES,
    NOVELTY_TYPES,
    REQUIRED_PRESSURES,
    TRAVERSAL_AXES,
    normalize_statement,
    validate_far_side_case,
)


VALID_CASE = {
    "case_id": "far-side:minimal",
    "h0": "Something new may become visible.",
    "baseline": {
        "claims": [
            {"id": "b:1", "statement": "Route is not host topology."},
            {"id": "b:2", "statement": "Opening is not transition."},
        ],
        "invariants": ["inv:route-host-distinction", "inv:opening-transition-distinction"],
    },
    "traversals": [
        {
            "id": "t:scale",
            "axis": "SCALE",
            "transform": "whole-to-parts",
            "invariants": ["inv:route-host-distinction"],
            "losses": [],
            "receipt_ref": "receipt:t:scale",
        },
        {
            "id": "t:direction",
            "axis": "DIRECTION",
            "transform": "result-to-formation",
            "invariants": ["inv:route-host-distinction"],
            "losses": [],
            "receipt_ref": "receipt:t:direction",
        },
        {
            "id": "t:representation",
            "axis": "REPRESENTATION",
            "transform": "prose-to-graph",
            "invariants": ["inv:route-host-distinction"],
            "losses": [],
            "receipt_ref": "receipt:t:representation",
        },
    ],
    "candidate": {
        "statement": "The selected route does not exhaust the available field.",
        "required_targets": ["inv:route-host-distinction"],
        "regenerated_targets": ["inv:route-host-distinction"],
        "novelty": [],
    },
    "pressure": [
        {"kind": kind, "status": "PASS", "receipt_ref": f"receipt:pressure:{kind.lower()}"}
        for kind in sorted(REQUIRED_PRESSURES)
    ],
}


class FarSideModelTests(unittest.TestCase):
    def test_statement_normalization_is_whitespace_only(self):
        self.assertEqual(
            normalize_statement("  Route  is\nnot   topology. "),
            "Route is not topology.",
        )

    def test_validation_accepts_minimal_receipted_case(self):
        valid, reason = validate_far_side_case(VALID_CASE)
        self.assertTrue(valid)
        self.assertIsNone(reason)

    def test_validation_requires_a_nonempty_baseline(self):
        case = copy.deepcopy(VALID_CASE)
        case["baseline"]["claims"] = []
        case["baseline"]["invariants"] = []
        valid, reason = validate_far_side_case(case)
        self.assertFalse(valid)
        self.assertEqual(reason, "INSUFFICIENT_BASELINE")

    def test_validation_requires_receipted_traversals(self):
        case = copy.deepcopy(VALID_CASE)
        del case["traversals"][0]["receipt_ref"]
        valid, reason = validate_far_side_case(case)
        self.assertFalse(valid)
        self.assertEqual(reason, "INSUFFICIENT_RECEIPT")

    def test_enums_preserve_spec_distinctions(self):
        self.assertEqual(
            NOVELTY_TYPES,
            {
                "NEW_WORDING",
                "NEW_REPRESENTATION",
                "NEW_DERIVATION",
                "NEW_RELATION",
                "NEW_INVARIANT",
                "NEW_PREDICTION",
            },
        )
        self.assertEqual(
            DIMENSIONAL_NOVELTY_TYPES,
            {"NEW_DERIVATION", "NEW_RELATION", "NEW_INVARIANT", "NEW_PREDICTION"},
        )
        self.assertIn("REPRESENTATION", TRAVERSAL_AXES)
        self.assertIn("METAPHOR_REMOVAL", REQUIRED_PRESSURES)


if __name__ == "__main__":
    unittest.main()
