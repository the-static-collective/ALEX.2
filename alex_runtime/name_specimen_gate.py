from __future__ import annotations

import re
from typing import Any

from alex_runtime.digests import sha256_json

PACKET_SCHEMA = "alex.name-specimen-packet/v0"
PACKET_RESULT_SCHEMA = "alex.name-specimen-packet-result/v0"
PACKET_RECEIPT_SCHEMA = "alex.name-specimen-packet-receipt/v0"

SPECIMEN_TYPES = frozenset({
    "LXX_JOSHUA",
    "MATTHEW_1_21",
    "JESUS_BARABBAS",
    "SCEVA",
    "PHILIPPIANS_2",
    "NOMEN_SACRUM",
})

FORBIDDEN_ANSWER_FIELDS = frozenset({
    "expected_answer",
    "expected_outcome",
    "favored_result",
    "survival_expected",
    "verdict",
    "conclusion",
})

PACKET_REQUIRED = (
    "packet_id",
    "specimen_type",
    "attestation_ref",
    "hypothesis_ref",
    "null_battery_ref",
    "producer",
)

SHA256_REF = re.compile(r"^sha256:[0-9a-f]{64}$")


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _valid_ref(value: Any) -> bool:
    return isinstance(value, str) and bool(SHA256_REF.fullmatch(value))


def _valid_ref_list(value: Any, *, require_nonempty: bool) -> tuple[bool, str | None]:
    if not isinstance(value, list):
        return False, "invalid_ref"
    if require_nonempty and not value:
        return False, "invalid_ref"
    if any(not _valid_ref(ref) for ref in value):
        return False, "invalid_ref"
    if len(value) != len(set(value)):
        return False, "duplicate_ref"
    return True, None


def _refuse(reason: str) -> dict[str, Any]:
    return {
        "schema": PACKET_RESULT_SCHEMA,
        "disposition": "REFUSE",
        "reason": reason,
        "authority": "none",
    }


def evaluate_name_specimen_packet(record: object) -> dict[str, Any]:
    if not isinstance(record, dict):
        return _refuse("not_an_object")
    if record.get("schema") != PACKET_SCHEMA:
        return _refuse("wrong_schema")
    if FORBIDDEN_ANSWER_FIELDS.intersection(record):
        return _refuse("favored_answer_not_allowed")
    if any(not _nonempty(record.get(field)) for field in PACKET_REQUIRED):
        return _refuse("missing_required_field")
    if record["specimen_type"] not in SPECIMEN_TYPES:
        return _refuse("invalid_specimen_type")

    for field in ("attestation_ref", "hypothesis_ref", "null_battery_ref"):
        if not _valid_ref(record[field]):
            return _refuse("invalid_ref")

    transforms_ok, transforms_reason = _valid_ref_list(
        record.get("transform_refs"), require_nonempty=False
    )
    if not transforms_ok:
        return _refuse(transforms_reason or "invalid_ref")

    receipts_ok, receipts_reason = _valid_ref_list(
        record.get("receipt_refs"), require_nonempty=True
    )
    if not receipts_ok:
        return _refuse(receipts_reason or "invalid_ref")

    material_ref = record.get("material_witness_ref")
    if material_ref is not None and not _valid_ref(material_ref):
        return _refuse("invalid_ref")

    packet_digest = sha256_json(record)
    if record["specimen_type"] == "NOMEN_SACRUM" and material_ref is None:
        return {
            "schema": PACKET_RESULT_SCHEMA,
            "disposition": "BLOCKED",
            "reason": "material_witness_required",
            "packet_digest": packet_digest,
            "specimen_type": record["specimen_type"],
            "authority": "none",
        }

    return {
        "schema": PACKET_RESULT_SCHEMA,
        "disposition": "READY",
        "reason": None,
        "receipt": {
            "schema": PACKET_RECEIPT_SCHEMA,
            "packet_id": record["packet_id"],
            "packet_digest": packet_digest,
            "specimen_type": record["specimen_type"],
            "attestation_ref": record["attestation_ref"],
            "transform_refs": list(record["transform_refs"]),
            "hypothesis_ref": record["hypothesis_ref"],
            "null_battery_ref": record["null_battery_ref"],
            "receipt_refs": list(record["receipt_refs"]),
            "material_witness_ref": material_ref,
            "authority": "none",
        },
        "authority": "none",
    }
