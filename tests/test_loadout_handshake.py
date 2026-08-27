import copy
import json
import unittest
from pathlib import Path

from alex_runtime.digests import sha256_json
from alex_runtime.handshake import (
    HANDSHAKE_M0_PROFILE,
    compile_payload_digest,
    evaluate_loadout_handshake,
    handshake_ruleset_digest,
    handshake_ruleset_manifest,
    validate_compile_record,
    validate_run_envelope,
)

ROOT = Path(__file__).resolve().parents[1]
RUN_ENVELOPE_SCHEMA = ROOT / "crucible" / "schema" / "run-envelope.schema.json"
LOADOUT_COMPILE_SCHEMA = ROOT / "crucible" / "schema" / "loadout-compile.schema.json"


def make_compile() -> dict:
    compile_record = {
        "schema": "loadout.compile/v0",
        "compile_id": "C0",
        "parent_compile_id": None,
        "issued_at": "2026-08-27T13:00:00Z",
        "expires_at": "2026-08-27T14:00:00Z",
        "world_cut_ref": "world-cut:W0",
        "context_pack_ref": "context-pack:CP0",
        "compile_trace": {
            "id": "compile-trace:CT0",
            "source_world_ref": "world-source:WS0",
            "operation": "bounded-selection",
            "preserved_invariants": ["mission", "stop_condition"],
            "declared_loss": ["ambient-conversation"],
            "producer": "loadout-test@1",
            "freshness": "2026-08-27T13:00:00Z",
        },
        "capability_bindings": [
            {"capability": "research.read", "status": "available"},
            {"capability": "repo.write", "status": "available"},
        ],
        "effect_fence_ref": "effect-fence:EF0",
        "effective_effects": [
            {
                "effect": "research.read",
                "status": "allowed",
                "authorization_source_ref": "owner-auth:A0",
                "scope": "repo:ALEX.2",
                "valid_from": "2026-08-27T13:00:00Z",
                "expires_at": "2026-08-27T14:00:00Z",
                "revocation_ref": None,
                "owner_gate_ref": "owner-gate:G0",
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
        "run_id": "RUN0",
        "compile_id": compile_record["compile_id"],
        "compile_digest": compile_record["compile_digest"],
        "compile_trace_ref": compile_record["compile_trace"]["id"],
        "phase": "EXECUTE",
        "expires_at": compile_record["expires_at"],
        "question": "What survives this bounded cut?",
        "task_shape": "AUDIT",
        "world_cut_ref": compile_record["world_cut_ref"],
        "context_pack_ref": compile_record["context_pack_ref"],
        "input_record_ids": ["record:R0"],
        "capability_bindings": copy.deepcopy(compile_record["capability_bindings"]),
        "effect_fence_ref": compile_record["effect_fence_ref"],
        "egress_policy_ref": compile_record["egress_policy_ref"],
        "rule_profile": HANDSHAKE_M0_PROFILE,
        "stop_condition": "one bounded handshake decision",
        "requested_outputs": ["handshake_receipt"],
    }


def make_case(compile_record: dict | None = None, audit_time: str = "2026-08-27T13:30:00Z") -> dict:
    compile_record = copy.deepcopy(compile_record or make_compile())
    case = {
        "case_id": "loadout-handshake-valid",
        "operation_type": "loadout_handshake",
        "rule_profile": HANDSHAKE_M0_PROFILE,
        "given": {
            "compile": compile_record,
            "audit": {
                "observed_at": audit_time,
                "current_owner_evidence_digest": compile_record["owner_evidence_digest"],
            },
        },
        "attempt": {
            "run_envelope": make_envelope(compile_record),
            "required_capabilities": ["research.read"],
            "requested_effects": ["research.read"],
        },
        "nonce": "test-loadout-handshake",
    }
    case["input_digest"] = sha256_json(case)
    return case


class HandshakeSchemaTests(unittest.TestCase):
    def test_public_schemas_exist_and_reject_extra_properties(self):
        self.assertTrue(RUN_ENVELOPE_SCHEMA.exists())
        self.assertTrue(LOADOUT_COMPILE_SCHEMA.exists())
        envelope_schema = json.loads(RUN_ENVELOPE_SCHEMA.read_text(encoding="utf-8"))
        compile_schema = json.loads(LOADOUT_COMPILE_SCHEMA.read_text(encoding="utf-8"))
        self.assertEqual(envelope_schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertEqual(compile_schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertFalse(envelope_schema["additionalProperties"])
        self.assertFalse(compile_schema["additionalProperties"])
        self.assertEqual(
            envelope_schema["properties"]["task_shape"]["enum"],
            ["FIND", "READ", "COMPARE", "TRACE", "DOSSIER", "AUDIT", "PRESSURE"],
        )


class CompileIdentityTests(unittest.TestCase):
    def test_compile_digest_is_over_payload_before_digest_field(self):
        compile_record = make_compile()
        digest = compile_record["compile_digest"]
        self.assertTrue(digest.startswith("sha256:"))
        self.assertEqual(len(digest), 71)
        self.assertEqual(compile_payload_digest(compile_record), digest)

        changed = copy.deepcopy(compile_record)
        changed["context_pack_ref"] = "context-pack:DIFFERENT"
        self.assertNotEqual(compile_payload_digest(changed), digest)

    def test_compile_validator_detects_digest_and_trace_failures(self):
        compile_record = make_compile()
        self.assertEqual(validate_compile_record(compile_record), [])

        bad_digest = copy.deepcopy(compile_record)
        bad_digest["compile_digest"] = "sha256:" + "0" * 64
        self.assertIn("COMPILE_DIGEST_MISMATCH", validate_compile_record(bad_digest))

        missing_trace = copy.deepcopy(compile_record)
        missing_trace["compile_trace"]["id"] = ""
        missing_trace["compile_digest"] = compile_payload_digest(missing_trace)
        self.assertIn("COMPILE_TRACE_REQUIRED", validate_compile_record(missing_trace))

    def test_handshake_ruleset_manifest_is_pinned(self):
        manifest = handshake_ruleset_manifest(HANDSHAKE_M0_PROFILE)
        self.assertEqual(manifest["profile"], HANDSHAKE_M0_PROFILE)
        self.assertEqual(manifest["rules"][0]["rule_id"], "LOADOUT-HANDSHAKE-001")
        self.assertEqual(manifest["rules"][0]["rule_version"], 1)
        digest = handshake_ruleset_digest(HANDSHAKE_M0_PROFILE)
        self.assertTrue(digest.startswith("sha256:"))
        self.assertEqual(len(digest), 71)


class EnvelopeBindingTests(unittest.TestCase):
    def test_valid_envelope_matches_compile_exactly(self):
        compile_record = make_compile()
        envelope = make_envelope(compile_record)
        self.assertEqual(validate_run_envelope(envelope, compile_record), [])

    def test_envelope_mismatch_cannot_swap_compile_room_or_fence(self):
        compile_record = make_compile()
        envelope = make_envelope(compile_record)
        mutations = {
            "compile_id": "FOREIGN",
            "compile_digest": "sha256:" + "b" * 64,
            "compile_trace_ref": "compile-trace:FOREIGN",
            "world_cut_ref": "world-cut:FOREIGN",
            "context_pack_ref": "context-pack:FOREIGN",
            "effect_fence_ref": "effect-fence:FOREIGN",
            "egress_policy_ref": "egress-policy:FOREIGN",
        }
        expected_codes = {
            "compile_id": "ENVELOPE_COMPILE_ID_MISMATCH",
            "compile_digest": "ENVELOPE_COMPILE_DIGEST_MISMATCH",
            "compile_trace_ref": "ENVELOPE_COMPILE_TRACE_MISMATCH",
            "world_cut_ref": "ENVELOPE_WORLD_CUT_MISMATCH",
            "context_pack_ref": "ENVELOPE_CONTEXT_PACK_MISMATCH",
            "effect_fence_ref": "ENVELOPE_EFFECT_FENCE_MISMATCH",
            "egress_policy_ref": "ENVELOPE_EGRESS_POLICY_MISMATCH",
        }
        for field, value in mutations.items():
            with self.subTest(field=field):
                candidate = copy.deepcopy(envelope)
                candidate[field] = value
                self.assertIn(expected_codes[field], validate_run_envelope(candidate, compile_record))

    def test_envelope_capabilities_are_bound_to_compile(self):
        compile_record = make_compile()
        envelope = make_envelope(compile_record)
        envelope["capability_bindings"] = [{"capability": "research.read", "status": "available"}]
        self.assertIn(
            "ENVELOPE_CAPABILITY_BINDINGS_MISMATCH",
            validate_run_envelope(envelope, compile_record),
        )


class HandshakeEvaluationTests(unittest.TestCase):
    def test_valid_compile_enters_alex_without_admission_semantics(self):
        case = make_case()
        result = evaluate_loadout_handshake(case)

        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertIsNone(result["reason_code"])
        self.assertFalse(result["recompile_required"])
        self.assertEqual(result["capability_gaps"], [])
        self.assertEqual(result["compile_id"], "C0")
        self.assertEqual(result["compile_digest"], case["given"]["compile"]["compile_digest"])
        self.assertEqual(result["compile_trace_ref"], "compile-trace:CT0")
        self.assertIn("compile:C0", result["receipt_survivors"])
        self.assertIn("compile_trace:compile-trace:CT0", result["receipt_survivors"])
        self.assertIn("effect_fence:effect-fence:EF0", result["receipt_survivors"])
        self.assertEqual(result["execution"], {"terminal_state": "FINISHED", "step_count": 1})
        forbidden = {"admitted", "authority", "canon", "publication", "warrant"}
        self.assertTrue(forbidden.isdisjoint(result))

    def test_expired_compile_refuses_and_requires_recompile(self):
        case = make_case(audit_time="2026-08-27T14:00:01Z")
        result = evaluate_loadout_handshake(case)

        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason_code"], "COMPILE_EXPIRED")
        self.assertTrue(result["recompile_required"])
        self.assertEqual(result["capability_gaps"], [])
        self.assertIn("compile:C0", result["receipt_survivors"])
        self.assertIn("compile_trace:compile-trace:CT0", result["receipt_survivors"])
        self.assertIn("effect_fence:effect-fence:EF0", result["receipt_survivors"])

    def test_handshake_does_not_mutate_case(self):
        case = make_case()
        before = copy.deepcopy(case)
        evaluate_loadout_handshake(case)
        self.assertEqual(case, before)


if __name__ == "__main__":
    unittest.main()
