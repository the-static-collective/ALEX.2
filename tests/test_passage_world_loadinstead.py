from __future__ import annotations

import copy
import unittest

from loadout_runtime.loadinstead import route_bit


def door_registry(status: str = "available") -> list[dict]:
    return [
        {
            "schema": "loadinstead.door/v0",
            "door_id": "door:R1",
            "owner_world": "synthetic:R1",
            "role": "destination",
            "accepts_classes": ["passage-token"],
            "protocol": "fixture-only",
            "capability_ref": "capability:synthetic-r1",
            "status": status,
        }
    ]


def bit(*, bit_id: str, formation_ref: str) -> dict:
    return {
        "schema": "ecode.route-bit/v0",
        "bit_id": bit_id,
        "occurred_at": "2026-08-28T13:30:00Z",
        "source_world": "synthetic:R0",
        "consequence_class": "passage-token",
        "payload_ref": "payload:022100",
        "formation_ref": formation_ref,
        "compile_ref": {
            "compile_id": "C1",
            "compile_digest": "sha256:" + "a" * 64,
        },
        "witness_classes": [],
    }


class PassageWorldLoadinsteadTests(unittest.TestCase):
    def test_same_payload_and_door_preserve_distinct_formation_refs(self) -> None:
        a = route_bit(bit(bit_id="bit:A", formation_ref="sha256:" + "1" * 64), door_registry())
        b = route_bit(bit(bit_id="bit:B", formation_ref="sha256:" + "2" * 64), door_registry())

        self.assertEqual(a["disposition"], "ROUTED")
        self.assertEqual(b["disposition"], "ROUTED")
        self.assertEqual(a["primary_door_ref"], "door:R1")
        self.assertEqual(b["primary_door_ref"], "door:R1")
        self.assertEqual(a["delivery_envelopes"][0]["payload_ref"], "payload:022100")
        self.assertEqual(b["delivery_envelopes"][0]["payload_ref"], "payload:022100")
        self.assertEqual(a["delivery_envelopes"][0]["formation_ref"], "sha256:" + "1" * 64)
        self.assertEqual(b["delivery_envelopes"][0]["formation_ref"], "sha256:" + "2" * 64)
        self.assertNotEqual(a["delivery_envelopes"][0]["formation_ref"], b["delivery_envelopes"][0]["formation_ref"])

    def test_route_never_attempts_admission_or_transfers_authority(self) -> None:
        proposal = route_bit(bit(bit_id="bit:A", formation_ref="sha256:" + "1" * 64), door_registry())
        self.assertEqual(proposal["admission_status"], "NOT_ATTEMPTED")
        self.assertFalse(proposal["authority_transferred"])
        self.assertEqual(proposal["delivery_envelopes"][0]["authority"], "none")

    def test_unavailable_same_door_keeps_refusal_visible_without_delivery(self) -> None:
        proposal = route_bit(bit(bit_id="bit:A", formation_ref="sha256:" + "1" * 64), door_registry("unavailable"))
        self.assertEqual(proposal["disposition"], "UNROUTABLE")
        self.assertEqual(proposal["delivery_envelopes"], [])
        self.assertEqual(proposal["rejections"], [{"door_id": "door:R1", "reason_code": "DOOR_UNAVAILABLE"}])
        self.assertEqual(proposal["admission_status"], "NOT_ATTEMPTED")

    def test_route_identity_noise_does_not_mutate_payload_or_formation(self) -> None:
        source = bit(bit_id="bit:A", formation_ref="sha256:" + "1" * 64)
        changed = copy.deepcopy(source)
        changed["bit_id"] = "bit:A-renamed-wrapper"
        a = route_bit(source, door_registry())
        b = route_bit(changed, door_registry())
        self.assertNotEqual(a["route_id"], b["route_id"])
        self.assertEqual(a["delivery_envelopes"][0]["payload_ref"], b["delivery_envelopes"][0]["payload_ref"])
        self.assertEqual(a["delivery_envelopes"][0]["formation_ref"], b["delivery_envelopes"][0]["formation_ref"])

    def test_router_does_not_emit_passage_equivalence_verdict(self) -> None:
        proposal = route_bit(bit(bit_id="bit:A", formation_ref="sha256:" + "1" * 64), door_registry())
        encoded = repr(proposal)
        self.assertNotIn("PASSAGE_DISTINCT", encoded)
        self.assertNotIn("PASSAGE_EQUIVALENT", encoded)


if __name__ == "__main__":
    unittest.main()
