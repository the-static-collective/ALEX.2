from __future__ import annotations

import copy
import hashlib
import json


def compile_payload_digest(compile_record: dict) -> str:
    payload = copy.deepcopy(compile_record)
    payload.pop("compile_digest", None)
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_compile_identity(compile_record: dict) -> list[str]:
    if not isinstance(compile_record, dict):
        return ["COMPILE_NOT_OBJECT"]
    errors: list[str] = []
    if compile_record.get("schema") != "loadout.compile/v0":
        errors.append("COMPILE_SCHEMA_INVALID")
    if not _nonempty(compile_record.get("compile_id")):
        errors.append("COMPILE_ID_REQUIRED")
    parent = compile_record.get("parent_compile_id")
    if parent is not None and not _nonempty(parent):
        errors.append("COMPILE_PARENT_ID_INVALID")
    if not _nonempty(compile_record.get("world_cut_ref")):
        errors.append("COMPILE_WORLD_CUT_REQUIRED")
    if not _nonempty(compile_record.get("context_pack_ref")):
        errors.append("COMPILE_CONTEXT_PACK_REQUIRED")
    trace = compile_record.get("compile_trace")
    if not isinstance(trace, dict) or not _nonempty(trace.get("id")):
        errors.append("COMPILE_TRACE_REQUIRED")
    if not _nonempty(compile_record.get("effect_fence_ref")):
        errors.append("COMPILE_EFFECT_FENCE_REQUIRED")
    if not isinstance(compile_record.get("effective_effects"), list):
        errors.append("COMPILE_EFFECTS_INVALID")
    if not _nonempty(compile_record.get("egress_policy_ref")):
        errors.append("COMPILE_EGRESS_POLICY_REQUIRED")
    digest = compile_record.get("compile_digest")
    if not _nonempty(digest) or digest != compile_payload_digest(compile_record):
        errors.append("COMPILE_DIGEST_MISMATCH")
    return list(dict.fromkeys(errors))
