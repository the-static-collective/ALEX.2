import copy
import unittest

from alex_runtime.world_bridge import evaluate_world_bridge


BASE = {
    "schema": "alex.world-bridge/v0",
    "bridge_id": "bridge-review-001",
    "source_ref": "sha256:" + "a" * 64,
    "source_world": "B",
    "target_ref": "sha256:" + "b" * 64,
    "target_world": "D",
    "bridge_type": "documented_association",
    "formulation": "A documented cross-world association.",
    "evidence_refs": ["sha256:" + "c" * 64],
    "promotion_limit": "association_only",
    "producer": "world-bridge-review@v0",
}


class WorldBridgeReviewTests(unittest.TestCase):
    def test_documented_bridge_cannot_use_source_endpoint_as_bridge_evidence(self):
        record = copy.deepcopy(BASE)
        record["evidence_refs"] = [record["source_ref"]]
        result = evaluate_world_bridge(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "bridge_evidence_must_be_distinct")

    def test_documented_bridge_cannot_use_target_endpoint_as_bridge_evidence(self):
        record = copy.deepcopy(BASE)
        record["evidence_refs"] = [record["target_ref"]]
        result = evaluate_world_bridge(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "bridge_evidence_must_be_distinct")


if __name__ == "__main__":
    unittest.main()
