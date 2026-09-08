from pathlib import Path
import unittest


class PartitionSwapExperimentTests(unittest.TestCase):
    def test_same_micro_receipts_can_yield_different_macro_graphs(self):
        module_path = Path("experiments/partition_swap.py")
        self.assertTrue(module_path.exists(), "PARTITION-SWAP-001 experiment is not implemented")

        from experiments.partition_swap import run_partition_swap_probe

        result = run_partition_swap_probe()

        self.assertEqual(result["experiment"], "PARTITION-SWAP-001")
        self.assertEqual(result["authority"], "none")
        self.assertEqual(result["observation"], "PARTITION_DEPENDENT_MACRO_GRAPH")

        role_side, transaction_pair = result["lifts"]
        self.assertEqual(role_side["micro_receipt_refs"], transaction_pair["micro_receipt_refs"])
        self.assertEqual(role_side["micro_receipt_refs"], ["receipt:appoints-a-b", "receipt:appoints-c-d"])
        self.assertEqual(
            role_side["macro_edges"],
            [{"from": "X", "verb": "appoints", "to": "Y", "system": "S"}],
        )
        self.assertEqual(transaction_pair["macro_edges"], [])
        self.assertNotEqual(role_side["macro_edges"], transaction_pair["macro_edges"])

    def test_pure_relabeling_is_not_classified_as_structural_delta(self):
        from experiments.partition_swap import run_relabel_control_probe

        result = run_relabel_control_probe()

        self.assertEqual(result["experiment"], "RELABEL-CONTROL-001")
        self.assertEqual(result["authority"], "none")
        self.assertEqual(result["observation"], "SERIALIZATION_DELTA_ONLY")
        self.assertNotEqual(result["left_macro_edges"], result["right_macro_edges"])
        self.assertEqual(result["left_relabelled_macro_edges"], result["right_macro_edges"])
        self.assertEqual(result["declared_relabeling"], {"X": "P", "Y": "Q"})

    def test_isolated_macro_nodes_are_not_erased_by_empty_edge_lists(self):
        from experiments.partition_swap import run_isolated_node_control_probe

        result = run_isolated_node_control_probe()

        self.assertEqual(result["experiment"], "ISOLATED-NODE-CONTROL-001")
        self.assertEqual(result["authority"], "none")
        self.assertEqual(result["observation"], "PARTITION_DEPENDENT_MACRO_GRAPH")

        two_node, one_node = result["lifts"]
        self.assertEqual(two_node["micro_receipt_refs"], one_node["micro_receipt_refs"])
        self.assertEqual(two_node["macro_edges"], [])
        self.assertEqual(one_node["macro_edges"], [])
        self.assertEqual(two_node["macro_nodes"], ["P", "Q"])
        self.assertEqual(one_node["macro_nodes"], ["Z"])
        self.assertNotEqual(two_node["macro_nodes"], one_node["macro_nodes"])

    def test_serialization_order_does_not_masquerade_as_structural_delta(self):
        from experiments.partition_swap import run_order_swap_control_probe

        result = run_order_swap_control_probe()

        self.assertEqual(result["experiment"], "ORDER-SWAP-CONTROL-001")
        self.assertEqual(result["authority"], "none")
        self.assertEqual(result["observation"], "SERIALIZATION_ORDER_DELTA_ONLY")
        self.assertNotEqual(result["left"]["macro_nodes"], result["right"]["macro_nodes"])
        self.assertNotEqual(result["left"]["macro_edges"], result["right"]["macro_edges"])
        self.assertEqual(set(result["left"]["macro_nodes"]), set(result["right"]["macro_nodes"]))
        self.assertEqual(
            {tuple(sorted(edge.items())) for edge in result["left"]["macro_edges"]},
            {tuple(sorted(edge.items())) for edge in result["right"]["macro_edges"]},
        )

    def test_order_swap_control_is_consumed_by_macro_graph_comparator(self):
        from experiments.partition_swap import _macro_graph_differs, run_order_swap_control_probe

        result = run_order_swap_control_probe()

        self.assertFalse(_macro_graph_differs(result["left"], result["right"]))

    def test_macro_graph_comparator_still_detects_genuine_node_or_edge_delta(self):
        from experiments.partition_swap import _macro_graph_differs

        left = {
            "macro_nodes": ["X", "Y"],
            "macro_edges": [{"from": "X", "verb": "appoints", "to": "Y", "system": "S"}],
        }
        missing_edge = {"macro_nodes": ["X", "Y"], "macro_edges": []}
        missing_node = {"macro_nodes": ["X"], "macro_edges": []}

        self.assertTrue(_macro_graph_differs(left, missing_edge))
        self.assertTrue(_macro_graph_differs(missing_edge, missing_node))

    def test_partition_change_can_survive_without_macro_graph_change(self):
        from experiments.partition_swap import run_partition_change_same_graph_probe

        result = run_partition_change_same_graph_probe()

        self.assertEqual(result["experiment"], "PARTITION-CHANGE-SAME-GRAPH-001")
        self.assertEqual(result["authority"], "none")
        self.assertTrue(result["partition_changed"])
        self.assertFalse(result["macro_graph_changed"])
        self.assertEqual(result["observation"], "PARTITION_CHANGE_WITHOUT_MACRO_GRAPH_CHANGE")

        left, right = result["lifts"]
        self.assertNotEqual(left["partition"], right["partition"])
        self.assertEqual(set(left["macro_nodes"]), set(right["macro_nodes"]))
        self.assertEqual(
            {tuple(sorted(edge.items())) for edge in left["macro_edges"]},
            {tuple(sorted(edge.items())) for edge in right["macro_edges"]},
        )

    def test_block_relabel_does_not_masquerade_as_membership_change(self):
        from experiments.partition_swap import run_block_relabel_control_probe

        result = run_block_relabel_control_probe()

        self.assertEqual(result["experiment"], "BLOCK-RELABEL-CONTROL-001")
        self.assertEqual(result["authority"], "none")
        self.assertFalse(result["block_membership_changed"])
        self.assertTrue(result["block_labels_changed"])
        self.assertEqual(result["observation"], "BLOCK_LABEL_DELTA_ONLY")
        self.assertNotEqual(result["left_partition"], result["right_partition"])

    def test_invalid_partitions_refuse_before_macro_projection(self):
        from experiments.partition_swap import run_invalid_partition_refusal_probe

        result = run_invalid_partition_refusal_probe()

        self.assertEqual(result["experiment"], "INVALID-PARTITION-REFUSAL-001")
        self.assertEqual(result["authority"], "none")
        self.assertEqual(result["observation"], "INVALID_PARTITIONS_REFUSED")

        overlap, uncovered = result["cases"][:2]
        self.assertEqual(overlap["status"], "REFUSE")
        self.assertEqual(overlap["reason"], "partition-overlap")
        self.assertEqual(overlap["duplicates"], ["A"])
        self.assertEqual(overlap["missing"], [])
        self.assertNotIn("macro_edges", overlap)

        self.assertEqual(uncovered["status"], "REFUSE")
        self.assertEqual(uncovered["reason"], "partition-uncovered")
        self.assertEqual(uncovered["duplicates"], [])
        self.assertEqual(uncovered["missing"], ["D"])
        self.assertNotIn("macro_edges", uncovered)

    def test_combined_overlap_and_uncovered_partition_preserves_both_failures(self):
        from experiments.partition_swap import run_invalid_partition_refusal_probe

        result = run_invalid_partition_refusal_probe()

        self.assertEqual(len(result["cases"]), 3)
        both = result["cases"][2]
        self.assertEqual(both["status"], "REFUSE")
        self.assertEqual(both["reason"], "partition-overlap-and-uncovered")
        self.assertEqual(both["duplicates"], ["A"])
        self.assertEqual(both["missing"], ["D"])
        self.assertNotIn("macro_edges", both)


if __name__ == "__main__":
    unittest.main()
