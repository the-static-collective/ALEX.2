from __future__ import annotations

from typing import Any

from alex_runtime.digests import sha256_json

ATTESTATION_SCHEMA = "alex.name-attestation/v0"
ATTESTATION_RESULT_SCHEMA = "alex.name-attestation-result/v0"
ATTESTATION_RECEIPT_SCHEMA = "alex.name-attestation-receipt/v0"
SOURCE_WORLDS = frozenset({"A", "B", "C", "D"})
REFERENT_CONFIDENCE = frozenset({"high", "medium", "low", "unresolved"})
ATTESTATION_REQUIRED = (
    "attestation_id",
    "source_world",
    "artifact_id",
    "locus",
    "language",
    "script",
    "raw_form",
    "reading_status",
    "referent",
    "referent_confidence",
)


def _refuse(schema: str, reason: str) -> dict[str, Any]:
    return {
        "schema": schema,
        "disposition": "REFUSE",
        "reason": reason,
        "authority": "none",
    }


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def evaluate_name_attestation(record: object) -> dict[str, Any]:
    if not isinstance(record, dict):
        return _refuse(ATTESTATION_RESULT_SCHEMA, "not_an_object")
    if record.get("schema") != ATTESTATION_SCHEMA:
        return _refuse(ATTESTATION_RESULT_SCHEMA, "wrong_schema")
    if any(not _nonempty_string(record.get(field)) for field in ATTESTATION_REQUIRED):
        return _refuse(ATTESTATION_RESULT_SCHEMA, "missing_required_field")
    if record["source_world"] not in SOURCE_WORLDS:
        return _refuse(ATTESTATION_RESULT_SCHEMA, "invalid_source_world")
    if record["referent_confidence"] not in REFERENT_CONFIDENCE:
        return _refuse(ATTESTATION_RESULT_SCHEMA, "invalid_referent_confidence")

    digest = sha256_json(record)
    return {
        "schema": ATTESTATION_RESULT_SCHEMA,
        "disposition": "ACCEPT",
        "reason": None,
        "receipt": {
            "schema": ATTESTATION_RECEIPT_SCHEMA,
            "attestation_id": record["attestation_id"],
            "attestation_digest": digest,
            "source_world": record["source_world"],
            "raw_form": record["raw_form"],
            "authority": "none",
        },
        "authority": "none",
    }
