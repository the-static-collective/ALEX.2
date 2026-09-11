import unittest


class PartitionRelabelScopeTests(unittest.TestCase):
    def test_nonbijective_relabel_refuses_instead_of_laundering_a_quotient(self):
        from experiments.relabel_scope import run_nonbijective_relabel_control_probe

        result = run_nonbijective_relabel_control_probe()

        self.assertEqual(result["experiment"], "NONBIJECTIVE-RELABEL-CONTROL-001")
        self.assertEqual(result["authority"], "none")
        self.assertEqual(result["status"], "REFUSE")
        self.assertEqual(result["reason"], "relabeling-not-bijective")
        self.assertEqual(result["observation"], "RELABELING_COLLAPSES_LABELS")
        self.assertEqual(result["declared_relabeling"], {"X": "P", "Y": "P"})
        self.assertEqual(result["source_labels"], ["X", "Y"])
        self.assertEqual(result["image_labels"], ["P"])
        self.assertNotIn("left_relabelled_macro_edges", result)

    def test_colliding_relabel_refuses_before_destination_capture(self):
        from experiments.relabel_scope import run_capture_collision_control_probe

        result = run_capture_collision_control_probe()

        self.assertEqual(result["experiment"], "RELABEL-CAPTURE-CONTROL-001")
        self.assertEqual(result["authority"], "none")
        self.assertEqual(result["status"], "REFUSE")
        self.assertEqual(result["reason"], "relabeling-destination-collision")
        self.assertEqual(result["observation"], "RELABELING_CAPTURES_EXISTING_LABEL")
        self.assertEqual(result["declared_relabeling"], {"X": "P", "Y": "Q"})
        self.assertEqual(result["destination_scope_labels"], ["P", "R"])
        self.assertEqual(result["colliding_labels"], ["P"])
        self.assertNotIn("relabelled_labels", result)


if __name__ == "__main__":
    unittest.main()
