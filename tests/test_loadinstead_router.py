import copy
import unittest

from loadout_runtime.loadinstead import (
    DOOR_SCHEMA,
    LOADINSTEAD_M0_PROFILE,
    ROUTE_BIT_SCHEMA,
    ROUTE_PROPOSAL_SCHEMA,
    route_bit,
    validate_door,
    validate_route_bit,
)


def make_bit(**overrides):
    bit = {
        "schema": ROUTE_BIT_SCHEMA,
        "bit_id": "bit-001",
        "occurred_at": "2026-08-28T19:00:00Z",
        "source_world": "daily-slice",
        "consequence_class": "repository_work",
        "payload_ref": "receipt://daily-slice/bit-001",
        "formation_ref": "ecode://history/bit-001",
        "compile_ref": {
            "compile_id": "loadout-compile-001",
            "compile_digest": "sha256:" + "a" * 64,
        },
        "witness_classes": ["research_accounting"],
    }
    bit.update(overrides)
    return bit


def make_door(
    door_id,
    *,
    owner_world,
    role,
    accepts_classes,
    protocol,
    status="available",
):
    return {
        "schema": DOOR_SCHEMA,
        "door_id": door_id,
        "owner_world": owner_world,
        "role": role,
        "accepts_classes": list(accepts_classes),
        "protocol": protocol,
        "capability_ref": f"capability://{door_id}",
        "status": status,
    }


class LoadinsteadRouterTests(unittest.TestCase):
    def test_routes_repository_work_to_single_forge_door_and_alex_witness(self):
        bit = make_bit()
        doors = [
            make_door(
                "forge",
                owner_world="FORGE",
                role="destination",
                accepts_classes=["repository_work"],
                protocol="forge.work-envelope/v0",
            ),
            make_door(
                "alex-witness",
                owner_world="ALEX",
                role="witness",
                accepts_classes=["research_accounting"],
                protocol="alex.route-witness/v0",
            ),
        ]
        result = route_bit(bit, doors)
        self.assertEqual(result["schema"], ROUTE_PROPOSAL_SCHEMA)
        self.assertEqual(result["profile"], LOADINSTEAD_M0_PROFILE)
        self.assertEqual(result["disposition"], "ROUTED")
        self.assertEqual(result["primary_door_ref"], "forge")
        self.assertEqual(result["candidate_door_refs"], ["forge"])
        self.assertEqual(result["witness_door_refs"], ["alex-witness"])
        self.assertFalse(result["authority_transferred"])
        self.assertEqual(result["admission_status"], "NOT_ATTEMPTED")
        self.assertEqual(result["delivery_envelopes"][0]["authority"], "none")
        self.assertEqual(
            result["delivery_envelopes"][0]["protocol"],
            "forge.work-envelope/v0",
        )
        self.assertRegex(result["route_id"], r"^sha256:[0-9a-f]{64}$")

    def test_zero_available_destination_owners_is_unroutable(self):
        bit = make_bit(consequence_class="relationship_crossing", witness_classes=[])
        result = route_bit(bit, [])
        self.assertEqual(result["disposition"], "UNROUTABLE")
        self.assertIsNone(result["primary_door_ref"])
        self.assertEqual(result["candidate_door_refs"], [])
        self.assertEqual(result["delivery_envelopes"], [])

    def test_multiple_available_destination_owners_is_ambiguous_and_never_silently_tiebreaks(self):
        bit = make_bit(witness_classes=[])
        doors = [
            make_door(
                "forge-a",
                owner_world="FORGE-A",
                role="destination",
                accepts_classes=["repository_work"],
                protocol="forge.work-envelope/v0",
            ),
            make_door(
                "forge-b",
                owner_world="FORGE-B",
                role="destination",
                accepts_classes=["repository_work"],
                protocol="forge.work-envelope/v0",
            ),
        ]
        result = route_bit(bit, doors)
        self.assertEqual(result["disposition"], "AMBIGUOUS")
        self.assertIsNone(result["primary_door_ref"])
        self.assertEqual(result["candidate_door_refs"], ["forge-a", "forge-b"])
        self.assertEqual(result["delivery_envelopes"], [])

    def test_matching_unavailable_door_is_preserved_as_rejection(self):
        bit = make_bit(witness_classes=[])
        doors = [
            make_door(
                "forge",
                owner_world="FORGE",
                role="destination",
                accepts_classes=["repository_work"],
                protocol="forge.work-envelope/v0",
                status="unavailable",
            )
        ]
        result = route_bit(bit, doors)
        self.assertEqual(result["disposition"], "UNROUTABLE")
        self.assertEqual(
            result["rejections"],
            [{"door_id": "forge", "reason_code": "DOOR_UNAVAILABLE"}],
        )

    def test_unavailable_witness_does_not_block_primary_route(self):
        bit = make_bit()
        doors = [
            make_door(
                "forge",
                owner_world="FORGE",
                role="destination",
                accepts_classes=["repository_work"],
                protocol="forge.work-envelope/v0",
            ),
            make_door(
                "alex-witness",
                owner_world="ALEX",
                role="witness",
                accepts_classes=["research_accounting"],
                protocol="alex.route-witness/v0",
                status="unavailable",
            ),
        ]
        result = route_bit(bit, doors)
        self.assertEqual(result["disposition"], "ROUTED")
        self.assertEqual(result["primary_door_ref"], "forge")
        self.assertEqual(result["witness_door_refs"], [])
        self.assertIn(
            {"door_id": "alex-witness", "reason_code": "DOOR_UNAVAILABLE"},
            result["rejections"],
        )

    def test_invalid_bit_is_rejected_instead_of_reinterpreted(self):
        bit = make_bit()
        del bit["consequence_class"]
        self.assertIn("BIT_SHAPE_INVALID", validate_route_bit(bit))
        with self.assertRaisesRegex(ValueError, "BIT_SHAPE_INVALID"):
            route_bit(bit, [])

    def test_invalid_door_is_rejected_instead_of_repaired(self):
        door = make_door(
            "forge",
            owner_world="FORGE",
            role="destination",
            accepts_classes=["repository_work"],
            protocol="forge.work-envelope/v0",
        )
        door["role"] = "router-and-owner"
        self.assertIn("DOOR_ROLE_INVALID", validate_door(door))
        with self.assertRaisesRegex(ValueError, "DOOR_ROLE_INVALID"):
            route_bit(make_bit(witness_classes=[]), [door])

    def test_same_inputs_replay_to_same_route_identity(self):
        bit = make_bit()
        doors = [
            make_door(
                "forge",
                owner_world="FORGE",
                role="destination",
                accepts_classes=["repository_work"],
                protocol="forge.work-envelope/v0",
            )
        ]
        first = route_bit(copy.deepcopy(bit), copy.deepcopy(doors))
        second = route_bit(copy.deepcopy(bit), copy.deepcopy(doors))
        self.assertEqual(first, second)

    def test_formation_change_changes_route_identity_without_changing_surface_route(self):
        bit = make_bit(witness_classes=[])
        doors = [
            make_door(
                "forge",
                owner_world="FORGE",
                role="destination",
                accepts_classes=["repository_work"],
                protocol="forge.work-envelope/v0",
            )
        ]
        first = route_bit(bit, doors)
        changed = make_bit(
            witness_classes=[],
            formation_ref="ecode://history/bit-001-descendant",
        )
        second = route_bit(changed, doors)
        self.assertEqual(first["primary_door_ref"], second["primary_door_ref"])
        self.assertNotEqual(first["route_id"], second["route_id"])


if __name__ == "__main__":
    unittest.main()
