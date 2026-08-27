import copy
import unittest

from alex_runtime.digests import sha256_json
from alex_runtime.handshake import HANDSHAKE_M0_PROFILE, compile_payload_digest, evaluate_loadout_handshake


def make_compile(*, compile_id: str = "C0", parent_compile_id: str | None = None) -> dict:
    compile_record = {
        "schema": "loadout.compile/v0",
        "compile_id": compile_id,
        "parent_compile_id": parent_compile_id,
        "issued_at": "2026-08-27T13:00:00Z",
        "expires_at": "2026-08-27T14:00:00Z",
        "world_cut_ref": "world-cut:W0",
        "context_pack_ref": "context-pack:CP0",
        "compile_trace": {
            "id": f"compile-trace:CT-{compile_id}",
            "source_world_ref": "world-source:WS0",
            "operation": "bounded-selection",
            "preserved_invariants": ["mission"],
            "declared_loss": [],
            "producer": "loadout-test@1",
            "freshness": "2026-08-27T13:00:00Z",
        },
        "capability_bindings": [
            {"capability": "research.read", "status": "available"},
            {"capability": "repo.write", "status": "available"},
        ],
        "effect_fence_ref": f"effect-fence:EF-{compile_id}",
        "effective_effects": [
            {
                "effect": "research.read",
                "status": "allowed",
                "authorization_source_ref": f"owner-auth:A-{compile_id}",
                "scope": "repo:ALEX.2",
                "valid_from": "2026-08-27T13:00:00Z",
                "expires_at": "2026-08-27T14:00:00Z",
                "revocation_ref": None,
                "owner_gate_ref": f"owner-gate:G-{compile_id}",
            }
        ],
        "owner_evidence_digest": "sha256:" + "a" * 64,
        "egress_policy_ref": "egress-policy:E0",
    }
    compile_record["compile_digest"] = compile_payload_digest(compile_record)
    return compile_record


def make_envelope(compile_record: dict) -> dict:
    return {
        "schema": "alex.run-envelope/v0",
        "run_id": f'RUN-{compile_record["compile_id"]}',
        "compile_id": compile_record["compile_id"],
        "compile_digest": compile_record["compile_digest"],
        "compile_trace_ref": compile_record["compile_trace"]["id"],
        "phase": "EXECUTE",
        "expires_at": compile_record["expires_at"],
        "question": "May this bounded run enter ALEX?",
        "task_shape": "AUDIT",
        "world_cut_ref": compile_record["world_cut_ref"],
        "context_pack_ref": compile_record["context_pack_ref"],
        "input_record_ids": [],
        "capability_bindings": copy.deepcopy(compile_record["capability_bindings"]),
        "effect_fence_ref": compile_record["effect_fence_ref"],
        "egress_policy_ref": compile_record["egress_policy_ref"],
        "rule_profile": HANDSHAKE_M0_PROFILE,
        "stop_condition": "one handshake decision",
        "requested_outputs": ["handshake_receipt"],
    }


def make_case(compile_record: dict, *, requested_effect: str = "research.read") -> dict:
    case = {
        "case_id": f'handshake-{compile_record["compile_id"]}',
        "operation_type": "loadout_handshake",
        "rule_profile": HANDSHAKE_M0_PROFILE,
        "given": {
            "compile": copy.deepcopy(compile_record),
            "audit": {
                "observed_at": "2026-08-27T13:30:00Z",
                "current_owner_evidence_digest": compile_record["owner_evidence_digest"],
            },
        },
        "attempt": {
            "run_envelope": make_envelope(compile_record),
            "required_capabilities": [requested_effect],
            "requested_effects": [requested_effect],
        },
        "nonce": f'nonce-{compile_record["compile_id"]}',
    }
    case["input_digest"] = sha256_json(case)
    return case


class OwnerEvidenceDriftTests(unittest.TestCase):
    def test_owner_evidence_change_requires_child_compile(self):
        case = make_case(make_compile())
        prior_digest = case["given"]["compile"]["owner_evidence_digest"]
        current_digest = "sha256:" + "b" * 64
        case["given"]["audit"]["current_owner_evidence_digest"] = current_digest
        case.pop("input_digest", None)
        case["input_digest"] = sha256_json(case)

        result = evaluate_loadout_handshake(case)

        self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["reason_code"], "OWNER_EVIDENCE_CHANGED")
        self.assertTrue(result["recompile_required"])
        self.assertIn(
            f"owner_evidence_changed:{prior_digest}->{current_digest}",
            result["receipt_survivors"],
        )


class ChildCompileTests(unittest.TestCase):
    def test_child_compile_keeps_context_but_not_parent_permission(self):
        parent = make_compile(compile_id="C0")
        parent["effective_effects"].append(
            {
                "effect": "repo.write",
                "status": "allowed",
                "authorization_source_ref": "owner-auth:PARENT-WRITE",
                "scope": "repo:ALEX.2",
                "valid_from": "2026-08-27T13:00:00Z",
                "expires_at": "2026-08-27T14:00:00Z",
                "revocation_ref": None,
                "owner_gate_ref": "owner-gate:PARENT-WRITE",
            }
        )
        parent["compile_digest"] = compile_payload_digest(parent)

        child = make_compile(compile_id="C1", parent_compile_id="C0")
        self.assertEqual(child["context_pack_ref"], parent["context_pack_ref"])
        self.assertEqual(child["world_cut_ref"], parent["world_cut_ref"])
        self.assertNotEqual(child["compile_id"], parent["compile_id"])
        self.assertFalse(any(entry["effect"] == "repo.write" for entry in child["effective_effects"]))

        result = evaluate_loadout_handshake(make_case(child, requested_effect="repo.write"))

        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason_code"], "EFFECT_OUTSIDE_FENCE")
        self.assertIn("compile:C1", result["receipt_survivors"])
        self.assertIn("parent_compile:C0", result["receipt_survivors"])
        self.assertIn("effect_refused:repo.write", result["receipt_survivors"])
        self.assertNotIn("owner-auth:PARENT-WRITE", result["receipt_survivors"])


if __name__ == "__main__":
    unittest.main()
