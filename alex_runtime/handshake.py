from __future__ import annotations

import copy
from datetime import datetime, timezone

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


def _parse_instant(value: str) -> datetime:
    if not _nonempty_string(value):
        raise ValueError("timestamp required")
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    instant = datetime.fromisoformat(normalized)
    if instant.tzinfo is None:
        raise ValueError("timestamp must be offset-aware")
    return instant.astimezone(timezone.utc)


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


def _survivors(compile_record: dict, envelope: dict, extras: list[str] | None = None) -> list[str]:
    trace = compile_record.get("compile_trace", {})
    survivors = [
        f'compile:{compile_record.get("compile_id")}',
        f'compile_trace:{trace.get("id")}',
        f'effect_fence:{compile_record.get("effect_fence_ref")}',
        f'owner_evidence_digest:{compile_record.get("owner_evidence_digest")}',
    ]
    if isinstance(envelope, dict) and _nonempty_string(envelope.get("run_id")):
        survivors.append(f'run_envelope:{envelope["run_id"]}')
    survivors.extend(extras or [])
    return list(dict.fromkeys(survivors))


def _handshake_result(
    compile_record: dict,
    envelope: dict,
    *,
    disposition: str,
    reason_code: str | None,
    recompile_required: bool,
    capability_gaps: list[str] | None = None,
    extra_survivors: list[str] | None = None,
) -> dict:
    trace = compile_record.get("compile_trace", {}) if isinstance(compile_record, dict) else {}
    return {
        "compile_id": compile_record.get("compile_id") if isinstance(compile_record, dict) else None,
        "compile_digest": compile_record.get("compile_digest") if isinstance(compile_record, dict) else None,
        "compile_trace_ref": trace.get("id") if isinstance(trace, dict) else None,
        "disposition": disposition,
        "reason_code": reason_code,
        "recompile_required": recompile_required,
        "capability_gaps": list(capability_gaps or []),
        "receipt_survivors": _survivors(compile_record, envelope, extra_survivors) if isinstance(compile_record, dict) else [],
        "execution": {"terminal_state": "FINISHED", "step_count": 1},
    }


def _available_capabilities(compile_record: dict) -> set[str]:
    return {
        binding.get("capability")
        for binding in compile_record.get("capability_bindings", [])
        if isinstance(binding, dict)
        and binding.get("status") == "available"
        and _nonempty_string(binding.get("capability"))
    }


def _effect_entry(compile_record: dict, effect: str) -> dict | None:
    for entry in compile_record.get("effective_effects", []):
        if isinstance(entry, dict) and entry.get("effect") == effect:
            return entry
    return None


def _effect_entry_is_current_and_attributable(entry: dict, observed: datetime) -> bool:
    if entry.get("status") != "allowed":
        return False
    if not _nonempty_string(entry.get("authorization_source_ref")):
        return False
    if not _nonempty_string(entry.get("owner_gate_ref")):
        return False
    if not _nonempty_string(entry.get("scope")):
        return False
    if entry.get("revocation_ref") is not None:
        return False
    try:
        valid_from = _parse_instant(entry.get("valid_from"))
        expires_at = _parse_instant(entry.get("expires_at"))
    except (TypeError, ValueError):
        return False
    return valid_from <= observed < expires_at


def evaluate_loadout_handshake(case: dict, *, now: str | None = None) -> dict:
    source = copy.deepcopy(case)
    given = source.get("given", {}) if isinstance(source, dict) else {}
    attempt = source.get("attempt", {}) if isinstance(source, dict) else {}
    compile_record = given.get("compile", {}) if isinstance(given, dict) else {}
    envelope = attempt.get("run_envelope", {}) if isinstance(attempt, dict) else {}

    if source.get("operation_type") != "loadout_handshake":
        return _handshake_result(
            compile_record,
            envelope,
            disposition="INSUFFICIENT_TO_TEST",
            reason_code="OPERATION_OUTSIDE_PROFILE",
            recompile_required=False,
        )
    if source.get("rule_profile") != HANDSHAKE_M0_PROFILE:
        return _handshake_result(
            compile_record,
            envelope,
            disposition="INSUFFICIENT_TO_TEST",
            reason_code="RULE_PROFILE_OUTSIDE_PROFILE",
            recompile_required=False,
        )

    compile_errors = validate_compile_record(compile_record)
    if compile_errors:
        return _handshake_result(
            compile_record,
            envelope,
            disposition="INSUFFICIENT_TO_TEST",
            reason_code="COMPILE_INVALID",
            recompile_required=True,
        )

    envelope_errors = validate_run_envelope(envelope, compile_record)
    if envelope_errors:
        return _handshake_result(
            compile_record,
            envelope,
            disposition="REFUSE",
            reason_code="ENVELOPE_INVALID",
            recompile_required=False,
        )

    audit = given.get("audit", {}) if isinstance(given, dict) else {}
    observed_at = now if now is not None else audit.get("observed_at")
    try:
        observed = _parse_instant(observed_at)
        expires = _parse_instant(compile_record["expires_at"])
    except (TypeError, ValueError):
        return _handshake_result(
            compile_record,
            envelope,
            disposition="INSUFFICIENT_TO_TEST",
            reason_code="AUDIT_TIME_INVALID",
            recompile_required=True,
        )

    if observed >= expires:
        return _handshake_result(
            compile_record,
            envelope,
            disposition="REFUSE",
            reason_code="COMPILE_EXPIRED",
            recompile_required=True,
        )

    required_capabilities = attempt.get("required_capabilities", [])
    if not isinstance(required_capabilities, list) or not all(isinstance(item, str) for item in required_capabilities):
        return _handshake_result(
            compile_record,
            envelope,
            disposition="INSUFFICIENT_TO_TEST",
            reason_code="CAPABILITY_REQUIREMENTS_INVALID",
            recompile_required=False,
        )
    available = _available_capabilities(compile_record)
    gaps = list(dict.fromkeys(capability for capability in required_capabilities if capability not in available))
    if gaps:
        return _handshake_result(
            compile_record,
            envelope,
            disposition="INSUFFICIENT_TO_TEST",
            reason_code="CAPABILITY_GAP",
            recompile_required=True,
            capability_gaps=gaps,
            extra_survivors=[f"capability_gap:{capability}" for capability in gaps],
        )

    requested_effects = attempt.get("requested_effects", [])
    if not isinstance(requested_effects, list) or not all(isinstance(item, str) for item in requested_effects):
        return _handshake_result(
            compile_record,
            envelope,
            disposition="INSUFFICIENT_TO_TEST",
            reason_code="EFFECT_REQUESTS_INVALID",
            recompile_required=False,
        )
    for effect in dict.fromkeys(requested_effects):
        entry = _effect_entry(compile_record, effect)
        if entry is None or entry.get("status") != "allowed":
            return _handshake_result(
                compile_record,
                envelope,
                disposition="REFUSE",
                reason_code="EFFECT_OUTSIDE_FENCE",
                recompile_required=False,
                extra_survivors=[f"effect_refused:{effect}"],
            )
        if not _effect_entry_is_current_and_attributable(entry, observed):
            return _handshake_result(
                compile_record,
                envelope,
                disposition="REFUSE",
                reason_code="EFFECT_FENCE_UNATTRIBUTABLE",
                recompile_required=False,
                extra_survivors=[f"effect_refused:{effect}"],
            )

    return _handshake_result(
        compile_record,
        envelope,
        disposition="ACCEPT",
        reason_code=None,
        recompile_required=False,
    )
