from __future__ import annotations

import json
import unittest
from pathlib import Path

from alex_runtime.cross_aperture_intersection import evaluate_cross_aperture_case

FIXTURE = Path(__file__).parent / "fixtures" / "cross_aperture_intersection_001.json"


def load_case(name: str) -> dict:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))[name]


class CrossApertureIntersectionTests(unittest.TestCase):
    def test_canonical_three_cut_lineage_identifies_only_within_declared_model(self) -> None:
        result = evaluate_cross_aperture_case(load_case("canonical"))

        self.assertEqual(result["disposition"], "IDENTIFIED_WITHIN_DECLARED_MODEL")
        self.assertIsNone(result["reason_code"])
        self.assertEqual([len(step["compatible_after"]) for step in result["lineage"]], [4, 2, 1])
        self.assertEqual([step["effect"] for step in result["lineage"]], ["REFINE", "REFINE", "REFINE"])
        self.assertEqual(result["final_compatible_states"], ["a"])
        self.assertEqual(result["unique_representative"], "a")
        self.assertEqual(result["selection_basis"], "singleton_in_declared_model")
        self.assertEqual(result["authority"], "none")


if __name__ == "__main__":
    unittest.main()
