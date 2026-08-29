import copy
import unittest

from alex_runtime.world_bridge import evaluate_world_bridge


BASE = {
    "schema": "alex.world-bridge/v0",
    "bridge_id": "bridge-phil2-reception-001",
    "source_ref": "sha256:" + "a" * 64,
    "source_world": "B",
    "target_ref": "sha256:" + "b" * 64,
    "target_world": "D",
    "bridge_type": "theological_interpretation",
    "formulation": "Later reception interprets a Pauline NAME claim through a later theological frame.",
    "evidence_refs": [],
    "promotion_limit": "reception_relevance_only",
    "producer": "name-dive@v0",
}


class WorldBridgeTests(unittest.TestCase):
    def test_accepts_explicit_cross_world_interpretive_bridge_without_authority(self):
        result = evaluate_world_bridge(copy.deepcopy(BASE))
        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertEqual(result["receipt"]["source_world"], "B")
        self.assertEqual(result["receipt"]["target_world"], "D")
        self.assertEqual(result["receipt"]["bridge_type"], "theological_interpretation")
        self.assertEqual(result["receipt"]["authority"], "none")
        self.assertTrue(result["receipt"]["bridge_digest"].startswith("sha256:"))

    def test_direction_is_part_of_bridge_identity(self):
        forward = evaluate_world_bridge(copy.deepcopy(BASE))
        reverse_record = copy.deepcopy(BASE)
        reverse_record["source_world"], reverse_record["target_world"] = "D", "B"
        reverse_record["source_ref"], reverse_record["target_ref"] = reverse_record["target_ref"], reverse_record["source_ref"]
        reverse = evaluate_world_bridge(reverse_record)
        self.assertNotEqual(forward["receipt"]["bridge_digest"], reverse["receipt"]["bridge_digest"])

    def test_same_world_relation_is_not_a_world_bridge(self):
        record = copy.deepcopy(BASE)
        record["target_world"] = "B"
        result = evaluate_world_bridge(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "same_world_not_bridge")

    def test_invalid_world_refuses(self):
        record = copy.deepcopy(BASE)
        record["source_world"] = "Z"
        result = evaluate_world_bridge(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "invalid_world")

    def test_documented_bridge_requires_evidence(self):
        record = copy.deepcopy(BASE)
        record["bridge_type"] = "documented_association"
        result = evaluate_world_bridge(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "documented_bridge_requires_evidence")

    def test_malformed_evidence_ref_refuses(self):
        record = copy.deepcopy(BASE)
        record["bridge_type"] = "scholarly_interpretation"
        record["evidence_refs"] = ["not-a-digest"]
        result = evaluate_world_bridge(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "invalid_evidence_refs")

    def test_documented_bridge_accepts_with_attributable_evidence_ref(self):
        record = copy.deepcopy(BASE)
        record["bridge_type"] = "scholarly_interpretation"
        record["evidence_refs"] = ["sha256:" + "c" * 64]
        result = evaluate_world_bridge(record)
        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertEqual(result["receipt"]["evidence_refs"], ["sha256:" + "c" * 64])

    def test_key_reorder_does_not_change_identity(self):
        first = evaluate_world_bridge(copy.deepcopy(BASE))
        reversed_items = list(reversed(list(BASE.items())))
        second = evaluate_world_bridge(dict(reversed_items))
        self.assertEqual(first["receipt"]["bridge_digest"], second["receipt"]["bridge_digest"])

    def test_world_change_changes_identity(self):
        first = evaluate_world_bridge(copy.deepcopy(BASE))
        record = copy.deepcopy(BASE)
        record["source_world"] = "A"
        second = evaluate_world_bridge(record)
        self.assertNotEqual(first["receipt"]["bridge_digest"], second["receipt"]["bridge_digest"])

    def test_input_authority_cannot_widen_output(self):
        record = copy.deepcopy(BASE)
        record["authority"] = "canon"
        result = evaluate_world_bridge(record)
        self.assertEqual(result["authority"], "none")
        self.assertEqual(result["receipt"]["authority"], "none")


if __name__ == "__main__":
    unittest.main()
