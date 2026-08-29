from __future__ import annotations

import copy
import unittest
from pathlib import Path

from skills.loadout.scripts.compile_identity import compile_payload_digest, validate_compile_identity
from skills.loadout.scripts.mortal_actor import bind_mortal_actor_compiles

ROOT = Path(__file__).resolve().parents[1]
COMPILE_IDENTITY = ROOT / "skills" / "loadout" / "scripts" / "compile_identity.py"
MORTAL_ACTOR = ROOT / "skills" / "loadout" / "scripts" / "mortal_actor.py"


def make_compile(compile_id: str = "C0", parent: str | None = None) -> dict:
    record = {
        "schema": "loadout.compile/v0",
        "compile_id": compile_id,
        "parent_compile_id": parent,
        "issued_at": "2026-08-27T13:00:00Z",
        "expires_at": "2026-08-27T14:00:00Z",
        "world_cut_ref": "world-cut:room-before-merge" if compile_id == "C0" else "world-cut:room-after-merge",
        "context_pack_ref": "context-pack:room-a0" if compile_id == "C0" else "context-pack:room-a1",
        "compile_trace": {
            "id": f"compile-trace:{compile_id}",
            "source_world_ref": "world-source:MA0",
            "operation": "bounded-selection" if compile_id == "C0" else "bounded-recompile",
            "preserved_invariants": ["effect-fence"],
            "declared_loss": [],
            "producer": "loadout-test@1",
            "freshness": "2026-08-27T13:00:00Z",
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
                "scope": "specimen:MA0",
                "valid_from": "2026-08-27T13:00:00Z",
                "expires_at": "2026-08-27T14:00:00Z",
                "revocation_ref": None,
                "owner_gate_ref": "owner-gate:G0",
            }
        ],
        "owner_evidence_digest": "sha256:" + "a" * 64,
        "egress_policy_ref": "egress-policy:E0",
    }
    record["compile_digest"] = compile_payload_digest(record)
    return record


class MortalLoadoutAdapterTests(unittest.TestCase):
    def test_portable_compile_identity_is_self_consistent(self):
        c0 = make_compile()
        self.assertEqual(validate_compile_identity(c0), [])
        changed = copy.deepcopy(c0)
        changed["context_pack_ref"] = "context-pack:DIFFERENT"
        self.assertNotEqual(compile_payload_digest(changed), c0["compile_digest"])

    def test_same_compile_binding_is_reference_only(self):
        c0 = make_compile()
        result = bind_mortal_actor_compiles(
            run_id="MA-A-A0", actor_id="A", world_cut_ref="cut:A0",
            projection_ref="sha256:projection-a0", entry_compile=c0, evaluation_compile=c0,
        )
        self.assertEqual(result["recompile_relation"], "same")
        self.assertEqual(result["entry_compile_digest"], result["evaluation_compile_digest"])
        self.assertFalse(result["authority_expanded"])
        self.assertFalse(result["side_effect_executed"])

    def test_direct_child_binding_preserves_authority_fence(self):
        c0 = make_compile()
        c1 = make_compile("C1", "C0")
        result = bind_mortal_actor_compiles(
            run_id="MA-A-A1", actor_id="A", world_cut_ref="cut:A1",
            projection_ref="sha256:projection-a1", entry_compile=c0, evaluation_compile=c1,
        )
        self.assertEqual(result["schema"], "mortal_actor.loadout-binding/v0")
        self.assertEqual(result["entry_compile_id"], "C0")
        self.assertEqual(result["evaluation_compile_id"], "C1")
        self.assertEqual(result["recompile_relation"], "child")
        self.assertFalse(result["authority_expanded"])
        self.assertFalse(result["side_effect_executed"])

    def test_foreign_child_is_rejected(self):
        c0 = make_compile()
        c1 = make_compile("C1", "FOREIGN")
        with self.assertRaisesRegex(ValueError, "not an attributable child"):
            bind_mortal_actor_compiles(run_id="r", actor_id="A", world_cut_ref="c", projection_ref="p", entry_compile=c0, evaluation_compile=c1)

    def test_effect_or_egress_expansion_is_rejected(self):
        c0 = make_compile()
        for mutation in ("fence", "effects", "egress"):
            with self.subTest(mutation=mutation):
                c1 = make_compile("C1", "C0")
                if mutation == "fence":
                    c1["effect_fence_ref"] = "effect-fence:EXPANDED"
                elif mutation == "effects":
                    c1["effective_effects"].append({"effect": "world.write", "status": "allowed"})
                else:
                    c1["egress_policy_ref"] = "egress-policy:EXPANDED"
                c1["compile_digest"] = compile_payload_digest(c1)
                message = "egress policy changed" if mutation == "egress" else "effect authority changed"
                with self.assertRaisesRegex(ValueError, message):
                    bind_mortal_actor_compiles(run_id="r", actor_id="A", world_cut_ref="c", projection_ref="p", entry_compile=c0, evaluation_compile=c1)

    def test_corrupt_digest_and_blank_projection_are_rejected(self):
        c0 = make_compile()
        bad = copy.deepcopy(c0)
        bad["compile_digest"] = "sha256:" + "0" * 64
        with self.assertRaisesRegex(ValueError, "invalid entry compile"):
            bind_mortal_actor_compiles(run_id="r", actor_id="A", world_cut_ref="c", projection_ref="p", entry_compile=bad, evaluation_compile=c0)
        with self.assertRaisesRegex(ValueError, "projection_ref required"):
            bind_mortal_actor_compiles(run_id="r", actor_id="A", world_cut_ref="c", projection_ref="", entry_compile=c0, evaluation_compile=c0)

    def test_router_selection_cannot_impersonate_evidence(self):
        c0 = make_compile()
        c0["capability_bindings"].append({"capability": "source.red-note", "status": "available"})
        c0["compile_digest"] = compile_payload_digest(c0)
        result = bind_mortal_actor_compiles(run_id="r", actor_id="A", world_cut_ref="c", projection_ref="p", entry_compile=c0, evaluation_compile=c0)
        for forbidden in {"evidence", "supports", "truth", "claim_basis", "admitted", "canon"}:
            self.assertNotIn(forbidden, result)
        self.assertNotIn("source.red-note", str(result))

    def test_portable_package_never_imports_alex_runtime(self):
        for path in (COMPILE_IDENTITY, MORTAL_ACTOR):
            self.assertNotIn("alex_runtime", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
