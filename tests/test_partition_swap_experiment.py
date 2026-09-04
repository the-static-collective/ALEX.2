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


if __name__ == "__main__":
    unittest.main()
