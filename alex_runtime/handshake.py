from __future__ import annotations

import copy

from alex_runtime.digests import sha256_json

HANDSHAKE_M0_PROFILE = "alex.runtime/loadout-handshake-m0"
HANDSHAKE_RULE_ID = "LOADOUT-HANDSHAKE-001"
HANDSHAKE_RULE_VERSION = 1

HANDSHAKE_M0_MANIFEST = {
    "profile": HANDSHAKE_M0_PROFILE,
    "rules": [
        {
            "rule_id": HANDSHAKE_RULE_ID,
            "rule_version": HANDSHAKE_RULE_VERSION,
            "run_envelope_schema": "alex.run-envelope/v0",
            "compile_schema": "loadout.compile/v0",
        }
    ],
}

RUN_ENVELOPE_KEYS = {
    "schema",
    "run_id",
    "compile_id",
    "compile_digest",
    "compile_trace_ref",
    "phase",
    "expires_at",
    "question",
    "task_shape",
    "world_cut_ref",
    "context_pack_ref",
    "input_record_ids",
    "capability_bindings",
    "effect_fence_ref",
    "egress_policy_ref",
    "rule_profile",
    "stop_condition",
    "requested_outputs",
}

COMPILE_KEYS = {
    "schema",
    "compile_id",
    "parent_compile_id",
    "issued_at",
    "expires_at",
    "world_cut_ref",
    "context_pack_ref",
    "compile_trace",
    "capability_bindings",
    "effect_fence_ref",
    "effective_effects",
    "owner_evidence_digest",
    "egress_policy_ref",
    "compile_digest",
}

TASK_SHAPES = {"FIND", "READ", "COMPARE", "TRACE", "DOSSIER", "AUDIT", "PRESSURE"}


def handshake_ruleset_manifest(profile: str) -> dict | None:
    if profile != HANDSHAKE_M0_PROFILE:
        return None
    return copy.deepcopy(HANDSHAKE_M0_MANIFEST)


def handshake_ruleset_digest(profile: str) -> str | None:
    manifest = handshake_ruleset_manifest(profile)
    return None if manifest is None else sha256_json(manifest)


def compile_payload_digest(compile_record: dict) -> str:
    payload = copy.deepcopy(compile_record)
    payload.pop("compile_digest", None)
    return sha256_json(payload)


def _nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_compile_record(compile_record: dict) -> list[str]:
    errors: list[str] = []
    if not isinstance(compile_record, dict):
        return ["COMPILE_NOT_OBJECT"]
    if set(compile_record) != COMPILE_KEYS:
        errors.append("COMPILE_SHAPE_INVALID")
    if compile_record.get("schema") != "loadout.compile/v0":
        errors.append("COMPILE_SCHEMA_INVALID")
    if not _nonempty_string(compile_record.get("compile_id")):
        errors.append("COMPILE_ID_REQUIRED")

    trace = compile_record.get("compile_trace")
    if not isinstance(trace, dict) or not _nonempty_string(trace.get("id")):
        errors.append("COMPILE_TRACE_REQUIRED")

    digest = compile_record.get("compile_digest")
    if not _nonempty_string(digest) or digest != compile_payload_digest(compile_record):
        errors.append("COMPILE_DIGEST_MISMATCH")

    for key in (
        "issued_at",
        "expires_at",
        "world_cut_ref",
        "context_pack_ref",
        "effect_fence_ref",
        "owner_evidence_digest",
        "egress_policy_ref",
    ):
        if not _nonempty_string(compile_record.get(key)):
            errors.append(f"COMPILE_{key.upper()}_REQUIRED")

    if not isinstance(compile_record.get("capability_bindings"), list):
        errors.append("COMPILE_CAPABILITY_BINDINGS_INVALID")
    if not isinstance(compile_record.get("effective_effects"), list):
        errors.append("COMPILE_EFFECTIVE_EFFECTS_INVALID")
    parent = compile_record.get("parent_compile_id")
    if parent is not None and not _nonempty_string(parent):
        errors.append("COMPILE_PARENT_ID_INVALID")
    return list(dict.fromkeys(errors))


def validate_run_envelope(envelope: dict, compile_record: dict) -> list[str]:
    errors: list[str] = []
    if not isinstance(envelope, dict):
        return ["ENVELOPE_NOT_OBJECT"]
    if set(envelope) != RUN_ENVELOPE_KEYS:
        errors.append("ENVELOPE_SHAPE_INVALID")
    if envelope.get("schema") != "alex.run-envelope/v0":
        errors.append("ENVELOPE_SCHEMA_INVALID")
    if envelope.get("task_shape") not in TASK_SHAPES:
        errors.append("ENVELOPE_TASK_SHAPE_INVALID")
    if envelope.get("rule_profile") != HANDSHAKE_M0_PROFILE:
        errors.append("ENVELOPE_RULE_PROFILE_INVALID")

    trace = compile_record.get("compile_trace") if isinstance(compile_record, dict) else None
    trace_id = trace.get("id") if isinstance(trace, dict) else None
    comparisons = (
        ("compile_id", compile_record.get("compile_id"), "ENVELOPE_COMPILE_ID_MISMATCH"),
        ("compile_digest", compile_record.get("compile_digest"), "ENVELOPE_COMPILE_DIGEST_MISMATCH"),
        ("compile_trace_ref", trace_id, "ENVELOPE_COMPILE_TRACE_MISMATCH"),
        ("expires_at", compile_record.get("expires_at"), "ENVELOPE_EXPIRY_MISMATCH"),
        ("world_cut_ref", compile_record.get("world_cut_ref"), "ENVELOPE_WORLD_CUT_MISMATCH"),
        ("context_pack_ref", compile_record.get("context_pack_ref"), "ENVELOPE_CONTEXT_PACK_MISMATCH"),
        ("effect_fence_ref", compile_record.get("effect_fence_ref"), "ENVELOPE_EFFECT_FENCE_MISMATCH"),
        ("egress_policy_ref", compile_record.get("egress_policy_ref"), "ENVELOPE_EGRESS_POLICY_MISMATCH"),
    )
    for field, expected, code in comparisons:
        if envelope.get(field) != expected:
            errors.append(code)
    if envelope.get("capability_bindings") != compile_record.get("capability_bindings"):
        errors.append("ENVELOPE_CAPABILITY_BINDINGS_MISMATCH")

    for key in ("run_id", "phase", "question", "stop_condition"):
        if not _nonempty_string(envelope.get(key)):
            errors.append(f"ENVELOPE_{key.upper()}_REQUIRED")
    for key in ("input_record_ids", "capability_bindings", "requested_outputs"):
        if not isinstance(envelope.get(key), list):
            errors.append(f"ENVELOPE_{key.upper()}_INVALID")
    return list(dict.fromkeys(errors))
