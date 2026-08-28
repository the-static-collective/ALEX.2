from __future__ import annotations

import copy
import unittest
from pathlib import Path

from alex_runtime.handshake import (
    compile_payload_digest as alex_compile_payload_digest,
    validate_compile_record,
)
from skills.loadout.scripts.compile_identity import (
    compile_payload_digest,
    validate_compile_identity,
)
from skills.loadout.scripts.mortal_actor import bind_mortal_actor_compiles

ROOT = Path(__file__).resolve().parents[1]
COMPILE_IDENTITY = ROOT / "skills" / "loadout" / "scripts" / "compile_identity.py"
MORTAL_ACTOR = ROOT / "skills" / "loadout" / "scripts" / "mortal_actor.py"


def make_compile(compile_id: str = "C0", parent_compile_id: str | None = None) -> dict:
    record = {
        "schema": "loadout.compile/v0",
        "compile_id": compile_id,
        "parent_compile_id": parent_compile_id,
        "issued_at": "2026-08-28T13:00:00Z",
        "expires_at": "2026-08-28T14:00:00Z",
        "world_cut_ref": "world-cut:room-a0",
        "context_pack_ref": "context-pack:room-a0",
        "compile_trace": {
            "id": f"compile-trace:{compile_id}",
            "source_world_ref": "world-source:room",
            "operation": "bounded-selection",
            "preserved_invariants": ["mission", "stop_condition"],
            "declared_loss": [],
            "producer": "loadout-test@1",
            "freshness": "2026-08-28T13:00:00Z",
        },
        "capability_bindings": [
            {"capability": "3rdi.project", "status": "available"},
            {"capability": "alex.evaluate", "status": "available"},
        ],
        "effect_fence_ref": "effect-fence:EF0",
        "effective_effects": [
            {
                "effect": "research.read",
                "status": "allowed",
                "authorization_source_ref": "owner-auth:A0",
                "scope": "repo:ALEX.2",
                "valid_from": "2026-08-28T13:00:00Z",
                "expires_at": "2026-08-28T14:00:00Z",
                "revocation_ref": None,
                "owner_gate_ref": "owner-gate:G0",
            }
        ],
        "owner_evidence_digest": "sha256:" + "a" * 64,
        "egress_policy_ref": "egress-policy:E0",
    }
    record["compile_digest"] = compile_payload_digest(record)
    return record


def child_compile(parent: dict) -> dict:
    child = copy.deepcopy(parent)
    child["compile_id"] = "C1"
    child["parent_compile_id"] = parent["compile_id"]
    child["world_cut_ref"] = "world-cut:room-a1"
    child["context_pack_ref"] = "context-pack:room-a1"
    child["compile_trace"]["id"] = "compile-trace:C1"
    child["compile_digest"] = compile_payload_digest(child)
    return child


class MortalLoadoutBindingTests(unittest.TestCase):
    def test_digest_helper_matches_alex_handshake(self) -> None:
        c0 = make_compile()
        self.assertEqual(compile_payload_digest(c0), alex_compile_payload_digest(c0))
        self.assertEqual(validate_compile_identity(c0), [])
        self.assertEqual(validate_compile_record(c0), [])

    def test_child_binding_preserves_immutable_compile_ancestry(self) -> None:
        c0 = make_compile()
        c1 = child_compile(c0)
        receipt = bind_mortal_actor_compiles(
            run_id="MA-A-A1",
            actor_id="A",
            world_cut_ref="cut:A1",
            projection_ref="sha256:" + "b" * 64,
            entry_compile=c0,
            evaluation_compile=c1,
        )
        self.assertEqual(receipt["schema"], "mortal_actor.loadout-binding/v0")
        self.assertEqual(receipt["entry_compile_id"], "C0")
        self.assertEqual(receipt["evaluation_compile_id"], "C1")
        self.assertEqual(receipt["recompile_relation"], "child")
        self.assertFalse(receipt["authority_expanded"])
        self.assertFalse(receipt["side_effect_executed"])

    def test_same_compile_is_lawful_without_fabricating_child(self) -> None:
        c0 = make_compile()
        receipt = bind_mortal_actor_compiles(
            run_id="MA-A-A0",
            actor_id="A",
            world_cut_ref="cut:A0",
            projection_ref="sha256:" + "c" * 64,
            entry_compile=c0,
            evaluation_compile=c0,
        )
        self.assertEqual(receipt["recompile_relation"], "same")
        self.assertEqual(receipt["entry_compile_digest"], receipt["evaluation_compile_digest"])

    def test_hostile_mutations_are_refused(self) -> None:
        c0 = make_compile()
        c1 = child_compile(c0)

        bad_parent = copy.deepcopy(c1)
        bad_parent["parent_compile_id"] = "FOREIGN"
        bad_parent["compile_digest"] = compile_payload_digest(bad_parent)
        with self.assertRaisesRegex(ValueError, "not an attributable child"):
            bind_mortal_actor_compiles(run_id="R", actor_id="A", world_cut_ref="W", projection_ref="P", entry_compile=c0, evaluation_compile=bad_parent)

        for field, value, message in (
            ("effect_fence_ref", "effect-fence:EXPANDED", "effect authority changed"),
            ("egress_policy_ref", "egress-policy:CHANGED", "egress policy changed"),
        ):
            mutated = copy.deepcopy(c1)
            mutated[field] = value
            mutated["compile_digest"] = compile_payload_digest(mutated)
            with self.assertRaisesRegex(ValueError, message):
                bind_mortal_actor_compiles(run_id="R", actor_id="A", world_cut_ref="W", projection_ref="P", entry_compile=c0, evaluation_compile=mutated)

        expanded = copy.deepcopy(c1)
        expanded["effective_effects"].append({"effect": "world.write", "status": "allowed"})
        expanded["compile_digest"] = compile_payload_digest(expanded)
        with self.assertRaisesRegex(ValueError, "effect authority changed"):
            bind_mortal_actor_compiles(run_id="R", actor_id="A", world_cut_ref="W", projection_ref="P", entry_compile=c0, evaluation_compile=expanded)

        corrupt = copy.deepcopy(c1)
        corrupt["compile_digest"] = "sha256:" + "0" * 64
        with self.assertRaisesRegex(ValueError, "invalid evaluation compile"):
            bind_mortal_actor_compiles(run_id="R", actor_id="A", world_cut_ref="W", projection_ref="P", entry_compile=c0, evaluation_compile=corrupt)

        with self.assertRaisesRegex(ValueError, "projection_ref required"):
            bind_mortal_actor_compiles(run_id="R", actor_id="A", world_cut_ref="W", projection_ref="", entry_compile=c0, evaluation_compile=c0)

    def test_binding_cannot_launder_capability_selection_into_evidence(self) -> None:
        c0 = make_compile()
        c0["capability_bindings"].append({"capability": "source.red-note", "status": "available"})
        c0["compile_digest"] = compile_payload_digest(c0)
        receipt = bind_mortal_actor_compiles(run_id="R", actor_id="A", world_cut_ref="W", projection_ref="P", entry_compile=c0, evaluation_compile=c0)
        encoded = repr(receipt).lower()
        for forbidden in ("evidence", "supports", "truth", "claim_basis", "admitted", "canon", "source.red-note"):
            self.assertNotIn(forbidden, encoded)

    def test_portable_loadout_modules_do_not_import_alex_runtime(self) -> None:
        for path in (COMPILE_IDENTITY, MORTAL_ACTOR):
            self.assertNotIn("alex_runtime", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
