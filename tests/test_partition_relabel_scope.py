import unittest


class PartitionRelabelScopeTests(unittest.TestCase):
    def test_nonbijective_relabel_refuses_instead_of_laundering_a_quotient(self):
        from experiments.relabel_scope import run_nonbijective_relabel_control_probe
        result = run_nonbijective_relabel_control_probe()
        self.assertEqual(result["status"], "REFUSE")
        self.assertEqual(result["reason"], "relabeling-not-bijective")
        self.assertEqual(result["authority"], "none")

    def test_colliding_relabel_refuses_before_destination_capture(self):
        from experiments.relabel_scope import run_capture_collision_control_probe
        result = run_capture_collision_control_probe()
        self.assertEqual(result["status"], "REFUSE")
        self.assertEqual(result["reason"], "relabeling-destination-collision")
        self.assertEqual(result["colliding_labels"], ["P"])
        self.assertEqual(result["authority"], "none")

    def test_partial_relabel_without_scope_refuses_implicit_completion(self):
        from experiments.relabel_scope import run_partial_relabel_scope_control_probe
        result = run_partial_relabel_scope_control_probe()
        self.assertEqual(result["status"], "REFUSE")
        self.assertEqual(result["reason"], "relabeling-scope-undeclared")
        self.assertEqual(result["unmapped_source_labels"], ["Y"])
        self.assertEqual(result["authority"], "none")

    def test_posthoc_relabel_refuses_rewriting_an_earlier_observation(self):
        from experiments.relabel_scope import run_posthoc_relabel_chronology_control_probe
        result = run_posthoc_relabel_chronology_control_probe()
        self.assertEqual(result["experiment"], "POSTHOC-RELABEL-CHRONOLOGY-001")
        self.assertEqual(result["status"], "REFUSE")
        self.assertEqual(result["reason"], "relabeling-postdates-observation")
        self.assertEqual(result["observed_labels"], ["X", "Y"])
        self.assertNotIn("relabelled_labels", result)
        self.assertNotIn("rewritten_observation", result)
        self.assertEqual(result["authority"], "none")

    def test_later_relabel_may_form_descendant_without_rewriting_source(self):
        from experiments.relabel_scope import run_retrospective_relabel_descendant_probe
        result = run_retrospective_relabel_descendant_probe()
        self.assertEqual(result["experiment"], "RETROSPECTIVE-RELABEL-DESCENDANT-001")
        self.assertEqual(result["status"], "PASS")
        self.assertTrue(result["source_unchanged"])
        source = result["source_receipt"]
        descendant = result["descendant_view"]
        self.assertEqual(source["observed_labels"], ["X", "Y"])
        self.assertEqual(source["payload"], {"X": "left", "Y": "right"})
        self.assertEqual(descendant["derived_from"], source["receipt_id"])
        self.assertEqual(descendant["labels"], ["P", "Q"])
        self.assertEqual(descendant["payload"], {"P": "left", "Q": "right"})
        self.assertEqual(descendant["relabel_declared_at"], "2026-09-13T12:05:00Z")
        self.assertEqual(descendant["applied_at"], "2026-09-13T12:10:00Z")
        self.assertEqual(descendant["authority"], "none")
        self.assertEqual(result["authority"], "none")


if __name__ == "__main__":
    unittest.main()
