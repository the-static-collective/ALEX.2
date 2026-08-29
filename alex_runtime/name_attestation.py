from __future__ import annotations

import re
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

TRANSFORM_SCHEMA = "alex.text-transform/v0"
TRANSFORM_RESULT_SCHEMA = "alex.text-transform-result/v0"
TRANSFORM_RECEIPT_SCHEMA = "alex.text-transform-receipt/v0"
TRANSFORM_OPERATIONS = frozenset(
    {
        "EDITORIAL_TRANSCRIPTION",
        "UNICODE_NORMALIZE",
        "CASE_NORMALIZE",
        "REMOVE_DIACRITICS",
        "TRANSLITERATE",
        "PRONUNCIATION_PROPOSAL",
        "OTHER_DECLARED",
    }
)
TRANSFORM_REQUIRED = (
    "transform_id",
    "input_ref",
    "operation",
    "input_text",
    "output_text",
    "producer",
    "method_version",
)
SHA256_REF = re.compile(r"^sha256:[0-9a-f]{64}$")


def _refuse(schema: str, reason: str) -> dict[str, Any]:
    return {
        "schema": schema,
        "disposition": "REFUSE",
        "reason": reason,
        "authority": "none",
    }


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _valid_declared_loss(value: Any) -> bool:
    return (
        isinstance(value, list)
        and all(_nonempty_string(item) for item in value)
        and len(value) == len(set(value))
    )


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


def evaluate_text_transform(record: object) -> dict[str, Any]:
    if not isinstance(record, dict):
        return _refuse(TRANSFORM_RESULT_SCHEMA, "not_an_object")
    if record.get("schema") != TRANSFORM_SCHEMA:
        return _refuse(TRANSFORM_RESULT_SCHEMA, "wrong_schema")
    if any(not _nonempty_string(record.get(field)) for field in TRANSFORM_REQUIRED):
        return _refuse(TRANSFORM_RESULT_SCHEMA, "missing_required_field")
    if record["operation"] not in TRANSFORM_OPERATIONS:
        return _refuse(TRANSFORM_RESULT_SCHEMA, "invalid_operation")
    if not SHA256_REF.fullmatch(record["input_ref"]):
        return _refuse(TRANSFORM_RESULT_SCHEMA, "invalid_input_ref")
    if not _valid_declared_loss(record.get("declared_loss")):
        return _refuse(TRANSFORM_RESULT_SCHEMA, "invalid_declared_loss")

    transform_digest = sha256_json(record)
    output_digest = sha256_json({"text": record["output_text"]})
    return {
        "schema": TRANSFORM_RESULT_SCHEMA,
        "disposition": "ACCEPT",
        "reason": None,
        "receipt": {
            "schema": TRANSFORM_RECEIPT_SCHEMA,
            "transform_id": record["transform_id"],
            "input_ref": record["input_ref"],
            "transform_digest": transform_digest,
            "output_digest": output_digest,
            "operation": record["operation"],
            "output_text": record["output_text"],
            "declared_loss": list(record["declared_loss"]),
            "authority": "none",
        },
        "authority": "none",
    }
