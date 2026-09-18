import unittest

from research.change_point_not_causal_hinge_001 import witness_change_point


class ChangePointNotCausalHinge001Tests(unittest.TestCase):
    def test_encounter_plus_delta_is_association_not_cause(self):
        r = witness_change_point(encounter_ref="encounter:E", grammar_changed=True)
        self.assertEqual(r["case"], "encounter_plus_delta")
        self.assertTrue(r["temporal_association_observed"])
        self.assertEqual(r["causal_status"], "not_established")
        self.assertIsNone(r["caused_by"])

    def test_delta_without_encounter_blocks_encounter_necessity_story(self):
        r = witness_change_point(encounter_ref=None, grammar_changed=True)
        self.assertEqual(r["case"], "grammar_delta_without_encounter")
        self.assertFalse(r["temporal_association_observed"])
        self.assertEqual(r["causal_status"], "not_established")
        self.assertIsNone(r["caused_by"])

    def test_competing_event_is_retained_and_causality_remains_unresolved(self):
        r = witness_change_point(
            encounter_ref="encounter:E",
            grammar_changed=True,
            competing_event_refs=["event:K"],
        )
        self.assertEqual(r["case"], "encounter_plus_competing_event_plus_delta")
        self.assertEqual(r["competing_event_refs"], ["event:K"])
        self.assertTrue(r["temporal_association_observed"])
        self.assertEqual(r["causal_status"], "not_established")
        self.assertIsNone(r["caused_by"])

    def test_encounter_without_delta_is_not_promoted_to_effect_elsewhere(self):
        r = witness_change_point(encounter_ref="encounter:E", grammar_changed=False)
        self.assertEqual(r["case"], "encounter_without_grammar_delta")
        self.assertFalse(r["temporal_association_observed"])
        self.assertIsNone(r["caused_by"])

    def test_design_reference_is_provenance_not_automatic_causal_verdict(self):
        r = witness_change_point(
            encounter_ref="encounter:E",
            grammar_changed=True,
            causal_design_ref="design:predeclared-its-001",
        )
        self.assertEqual(r["causal_design_ref"], "design:predeclared-its-001")
        self.assertEqual(r["causal_status"], "not_established")
        self.assertIsNone(r["caused_by"])


if __name__ == "__main__":
    unittest.main()
