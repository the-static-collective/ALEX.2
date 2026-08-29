import copy
import unittest

from alex_runtime.name_specimen_gate import (
    evaluate_name_six_specimen_gate,
    evaluate_name_specimen_packet,
)


REF_A = "sha256:" + "a" * 64
REF_B = "sha256:" + "b" * 64
REF_C = "sha256:" + "c" * 64
REF_D = "sha256:" + "d" * 64
REF_E = "sha256:" + "e" * 64
REF_F = "sha256:" + "f" * 64

SPECIMEN_TYPES = [
    "LXX_JOSHUA",
    "MATTHEW_1_21",
    "JESUS_BARABBAS",
    "SCEVA",
    "PHILIPPIANS_2",
    "NOMEN_SACRUM",
]

BASE_PACKET = {
    "schema": "alex.name-specimen-packet/v0",
    "packet_id": "packet-matthew-1-21",
    "specimen_type": "MATTHEW_1_21",
    "attestation_ref": REF_A,
    "transform_refs": [REF_B],
    "hypothesis_ref": REF_C,
    "null_battery_ref": REF_D,
    "receipt_refs": [REF_E],
    "producer": "alex-pilot@1",
}


def packet_result(specimen_type: str, *, blocked: bool = False) -> dict:
    if blocked:
        return {
            "schema": "alex.name-specimen-packet-result/v0",
            "disposition": "BLOCKED",
            "reason": "material_witness_required",
            "packet_digest": "sha256:" + specimen_type.lower().encode().hex()[:64].ljust(64, "0"),
            "specimen_type": specimen_type,
            "authority": "none",
        }
    return {
        "schema": "alex.name-specimen-packet-result/v0",
        "disposition": "READY",
        "reason": None,
        "receipt": {
            "schema": "alex.name-specimen-packet-receipt/v0",
            "packet_id": f"packet-{specimen_type.lower()}",
            "packet_digest": "sha256:" + specimen_type.lower().encode().hex()[:64].ljust(64, "0"),
            "specimen_type": specimen_type,
            "attestation_ref": REF_A,
            "transform_refs": [],
            "hypothesis_ref": REF_C,
            "null_battery_ref": REF_D,
            "receipt_refs": [REF_E],
            "material_witness_ref": REF_F if specimen_type == "NOMEN_SACRUM" else None,
            "authority": "none",
        },
        "authority": "none",
    }


class NameSpecimenPacketTests(unittest.TestCase):
    def test_text_first_packet_is_ready_and_freezes_authority(self):
        record = copy.deepcopy(BASE_PACKET)
        record["authority"] = "canon"
        result = evaluate_name_specimen_packet(record)
        self.assertEqual(result["disposition"], "READY")
        self.assertEqual(result["reason"], None)
        self.assertEqual(result["receipt"]["specimen_type"], "MATTHEW_1_21")
        self.assertEqual(result["receipt"]["authority"], "none")
        self.assertTrue(result["receipt"]["packet_digest"].startswith("sha256:"))

    def test_nomen_sacrum_without_material_witness_is_blocked(self):
        record = copy.deepcopy(BASE_PACKET)
        record["packet_id"] = "packet-nomen-sacrum"
        record["specimen_type"] = "NOMEN_SACRUM"
        result = evaluate_name_specimen_packet(record)
        self.assertEqual(result["disposition"], "BLOCKED")
        self.assertEqual(result["reason"], "material_witness_required")
        self.assertEqual(result["authority"], "none")

    def test_nomen_sacrum_with_material_witness_is_ready(self):
        record = copy.deepcopy(BASE_PACKET)
        record["packet_id"] = "packet-nomen-sacrum"
        record["specimen_type"] = "NOMEN_SACRUM"
        record["material_witness_ref"] = REF_F
        result = evaluate_name_specimen_packet(record)
        self.assertEqual(result["disposition"], "READY")
        self.assertEqual(result["receipt"]["material_witness_ref"], REF_F)

    def test_malformed_reference_refuses(self):
        record = copy.deepcopy(BASE_PACKET)
        record["attestation_ref"] = "sha256:not-a-digest"
        result = evaluate_name_specimen_packet(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "invalid_ref")

    def test_duplicate_transform_reference_refuses(self):
        record = copy.deepcopy(BASE_PACKET)
        record["transform_refs"] = [REF_B, REF_B]
        result = evaluate_name_specimen_packet(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "duplicate_ref")

    def test_duplicate_receipt_reference_refuses(self):
        record = copy.deepcopy(BASE_PACKET)
        record["receipt_refs"] = [REF_E, REF_E]
        result = evaluate_name_specimen_packet(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "duplicate_ref")

    def test_forbidden_answer_field_refuses(self):
        record = copy.deepcopy(BASE_PACKET)
        record["expected_outcome"] = "favored hypothesis survives"
        result = evaluate_name_specimen_packet(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "favored_answer_not_allowed")

    def test_key_order_does_not_change_packet_identity(self):
        first = evaluate_name_specimen_packet(copy.deepcopy(BASE_PACKET))
        reordered = {key: BASE_PACKET[key] for key in reversed(list(BASE_PACKET))}
        second = evaluate_name_specimen_packet(reordered)
        self.assertEqual(
            first["receipt"]["packet_digest"],
            second["receipt"]["packet_digest"],
        )


class SixSpecimenGateTests(unittest.TestCase):
    def make_gate(self) -> dict:
        return {
            "schema": "alex.name-six-specimen-gate/v0",
            "gate_id": "name-six-specimen-001",
            "packet_results": [packet_result(specimen) for specimen in SPECIMEN_TYPES],
            "producer": "alex-pilot@1",
        }

    def test_one_blocked_specimen_blocks_dive_and_names_blocker(self):
        gate = self.make_gate()
        gate["packet_results"][-1] = packet_result("NOMEN_SACRUM", blocked=True)
        result = evaluate_name_six_specimen_gate(gate)
        self.assertEqual(result["disposition"], "DIVE_BLOCKED")
        self.assertEqual(result["blocked_specimen_types"], ["NOMEN_SACRUM"])
        self.assertEqual(result["authority"], "none")

    def test_six_ready_packets_make_dive_ready_without_authority(self):
        gate = self.make_gate()
        gate["authority"] = "canon"
        result = evaluate_name_six_specimen_gate(gate)
        self.assertEqual(result["disposition"], "DIVE_READY")
        self.assertEqual(result["blocked_specimen_types"], [])
        self.assertEqual(result["authority"], "none")

    def test_missing_specimen_type_refuses(self):
        gate = self.make_gate()
        gate["packet_results"].pop()
        result = evaluate_name_six_specimen_gate(gate)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "incomplete_specimen_family")

    def test_duplicate_specimen_type_refuses(self):
        gate = self.make_gate()
        gate["packet_results"][-1] = packet_result("PHILIPPIANS_2")
        result = evaluate_name_six_specimen_gate(gate)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "duplicate_specimen_type")

    def test_packet_refusal_refuses_family_gate(self):
        gate = self.make_gate()
        gate["packet_results"][0] = {
            "schema": "alex.name-specimen-packet-result/v0",
            "disposition": "REFUSE",
            "reason": "invalid_ref",
            "authority": "none",
        }
        result = evaluate_name_six_specimen_gate(gate)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "packet_refused")


if __name__ == "__main__":
    unittest.main()
