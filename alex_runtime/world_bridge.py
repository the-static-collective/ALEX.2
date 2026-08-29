from __future__ import annotations

import re
from typing import Any

from alex_runtime.digests import sha256_json

WORLD_BRIDGE_SCHEMA = "alex.world-bridge/v0"
WORLD_BRIDGE_RESULT_SCHEMA = "alex.world-bridge-result/v0"
WORLD_BRIDGE_RECEIPT_SCHEMA = "alex.world-bridge-receipt/v0"
SOURCE_WORLDS = frozenset({"A", "B", "C", "D"})
BRIDGE_TYPES = frozenset({
    "documented_mechanism",
    "documented_association",
    "scholarly_interpretation",
    "inference",
    "formal_analogy",
    "metaphor",
    "theological_interpretation",
    "unresolved_bridge",
})
DOCUMENTED_BRIDGE_TYPES = frozenset({
    "documented_mechanism",
    "documented_association",
    "scholarly_interpretation",
})
REQUIRED = (
    "bridge_id",
    "source_ref",
    "source_world",
    "target_ref",
    "target_world",
    "bridge_type",
    "formulation",
    "promotion_limit",
    "producer",
)
SHA256_REF = re.compile(r"^sha256:[0-9a-f]{64}$")


def _refuse(reason: str) -> dict[str, Any]:
    return {
        "schema": WORLD_BRIDGE_RESULT_SCHEMA,
        "disposition": "REFUSE",
        "reason": reason,
        "authority": "none",
    }


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _valid_refs(value: Any) -> bool:
    return (
        isinstance(value, list)
        and len(value) == len(set(value))
        and all(isinstance(ref, str) and SHA256_REF.fullmatch(ref) for ref in value)
    )


def evaluate_world_bridge(record: object) -> dict[str, Any]:
    if not isinstance(record, dict):
        return _refuse("not_an_object")
    if record.get("schema") != WORLD_BRIDGE_SCHEMA:
        return _refuse("wrong_schema")
    if any(not _nonempty(record.get(field)) for field in REQUIRED):
        return _refuse("missing_required_field")
    if record["source_world"] not in SOURCE_WORLDS or record["target_world"] not in SOURCE_WORLDS:
        return _refuse("invalid_world")
    if record["source_world"] == record["target_world"]:
        return _refuse("same_world_not_bridge")
    if not SHA256_REF.fullmatch(record["source_ref"]) or not SHA256_REF.fullmatch(record["target_ref"]):
        return _refuse("invalid_occurrence_ref")
    if record["bridge_type"] not in BRIDGE_TYPES:
        return _refuse("invalid_bridge_type")
    evidence_refs = record.get("evidence_refs")
    if not _valid_refs(evidence_refs):
        return _refuse("invalid_evidence_refs")
    if record["bridge_type"] in DOCUMENTED_BRIDGE_TYPES and not evidence_refs:
        return _refuse("documented_bridge_requires_evidence")
    if record["bridge_type"] in DOCUMENTED_BRIDGE_TYPES:
        endpoints = {record["source_ref"], record["target_ref"]}
        if any(ref in endpoints for ref in evidence_refs):
            return _refuse("bridge_evidence_must_be_distinct")

    bridge_digest = sha256_json(record)
    return {
        "schema": WORLD_BRIDGE_RESULT_SCHEMA,
        "disposition": "ACCEPT",
        "reason": None,
        "receipt": {
            "schema": WORLD_BRIDGE_RECEIPT_SCHEMA,
            "bridge_id": record["bridge_id"],
            "bridge_digest": bridge_digest,
            "source_ref": record["source_ref"],
            "source_world": record["source_world"],
            "target_ref": record["target_ref"],
            "target_world": record["target_world"],
            "bridge_type": record["bridge_type"],
            "formulation": record["formulation"],
            "evidence_refs": list(evidence_refs),
            "promotion_limit": record["promotion_limit"],
            "authority": "none",
        },
        "authority": "none",
    }
