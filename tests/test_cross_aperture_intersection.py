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

    def test_non_singleton_fog_never_selects_representative(self) -> None:
        result = evaluate_cross_aperture_case(load_case("non_singleton_fog"))

        self.assertEqual(result["disposition"], "FOG")
        self.assertEqual(result["reason_code"], "NON_SINGLETON_COMPATIBLE_SET")
        self.assertEqual(result["final_compatible_states"], ["a", "b"])
        self.assertIsNone(result["unique_representative"])
        self.assertIsNone(result["selection_basis"])
        self.assertEqual(result["authority"], "none")

    def test_redundant_and_correlated_cuts_do_not_gain_information_by_title(self) -> None:
        redundant = evaluate_cross_aperture_case(load_case("redundant_aperture"))
        correlated = evaluate_cross_aperture_case(load_case("correlated_agreement"))

        self.assertEqual(redundant["lineage"][-1]["effect"], "REDUNDANT")
        self.assertEqual(correlated["lineage"][-1]["effect"], "REDUNDANT")
        self.assertEqual(correlated["lineage"][-1]["relation_declaration"], "correlated")
        self.assertEqual(redundant["final_compatible_states"], correlated["final_compatible_states"])
        self.assertIsNone(redundant["unique_representative"])
        self.assertIsNone(correlated["unique_representative"])

    def test_empty_intersection_is_model_break_not_reality_verdict(self) -> None:
        result = evaluate_cross_aperture_case(load_case("model_break"))

        self.assertEqual(result["disposition"], "MODEL_BREAK")
        self.assertEqual(result["reason_code"], "INCONSISTENT_OBSERVATIONS")
        self.assertEqual(result["lineage"][-1]["effect"], "BREAK")
        self.assertEqual(result["final_compatible_states"], [])
        self.assertIsNone(result["unique_representative"])
        self.assertIsNone(result["selection_basis"])
        self.assertEqual(result["authority"], "none")

    def test_malformed_cases_return_stable_reason_codes(self) -> None:
        expectations = {
            "invalid_world_domain": "INVALID_WORLD_DOMAIN",
            "invalid_cuts": "INVALID_CUTS",
            "duplicate_cut_id": "DUPLICATE_CUT_ID",
            "duplicate_map_id": "DUPLICATE_MAP_ID",
            "incomplete_observation_map": "INCOMPLETE_OBSERVATION_MAP",
            "invalid_map_output": "INVALID_MAP_OUTPUT",
            "invalid_observed_output": "INVALID_OBSERVED_OUTPUT",
            "invalid_relation": "INVALID_RELATION_DECLARATION",
        }
        for name, reason in expectations.items():
            with self.subTest(name=name):
                result = evaluate_cross_aperture_case(load_case(name))
                self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
                self.assertEqual(result["reason_code"], reason)
                self.assertEqual(result["initial_compatible_states"], [])
                self.assertEqual(result["lineage"], [])
                self.assertEqual(result["final_compatible_states"], [])
                self.assertIsNone(result["unique_representative"])
                self.assertIsNone(result["selection_basis"])
                self.assertEqual(result["authority"], "none")

    def test_non_dict_case_is_malformed(self) -> None:
        result = evaluate_cross_aperture_case(None)

        self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["reason_code"], "MALFORMED_CASE")
        self.assertEqual(result["lineage"], [])
        self.assertEqual(result["authority"], "none")

    def test_missing_relation_declaration_normalizes_to_unknown(self) -> None:
        result = evaluate_cross_aperture_case(load_case("missing_relation"))

        self.assertNotEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["lineage"][0]["relation_declaration"], "unknown")
        self.assertEqual(result["final_compatible_states"], ["a"])


if __name__ == "__main__":
    unittest.main()
