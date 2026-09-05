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


if __name__ == "__main__":
    unittest.main()
