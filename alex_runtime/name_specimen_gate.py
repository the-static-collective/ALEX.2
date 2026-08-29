from __future__ import annotations

import re
from typing import Any

from alex_runtime.digests import sha256_json

PACKET_SCHEMA = "alex.name-specimen-packet/v0"
PACKET_RESULT_SCHEMA = "alex.name-specimen-packet-result/v0"
PACKET_RECEIPT_SCHEMA = "alex.name-specimen-packet-receipt/v0"
GATE_SCHEMA = "alex.name-six-specimen-gate/v0"
GATE_RESULT_SCHEMA = "alex.name-six-specimen-gate-result/v0"
GATE_RECEIPT_SCHEMA = "alex.name-six-specimen-gate-receipt/v0"

SPECIMEN_TYPE_ORDER = (
    "LXX_JOSHUA",
    "MATTHEW_1_21",
    "JESUS_BARABBAS",
    "SCEVA",
    "PHILIPPIANS_2",
    "NOMEN_SACRUM",
)
SPECIMEN_TYPES = frozenset(SPECIMEN_TYPE_ORDER)

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
GATE_REQUIRED = ("gate_id", "producer")

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


def _gate_refuse(reason: str) -> dict[str, Any]:
    return {
        "schema": GATE_RESULT_SCHEMA,
        "disposition": "REFUSE",
        "reason": reason,
        "blocked_specimen_types": [],
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


def evaluate_name_six_specimen_gate(record: object) -> dict[str, Any]:
    if not isinstance(record, dict):
        return _gate_refuse("not_an_object")
    if record.get("schema") != GATE_SCHEMA:
        return _gate_refuse("wrong_schema")
    if FORBIDDEN_ANSWER_FIELDS.intersection(record):
        return _gate_refuse("favored_answer_not_allowed")
    if any(not _nonempty(record.get(field)) for field in GATE_REQUIRED):
        return _gate_refuse("missing_required_field")

    packet_results = record.get("packet_results")
    if not isinstance(packet_results, list):
        return _gate_refuse("invalid_packet_results")

    by_type: dict[str, dict[str, Any]] = {}
    blocked: list[str] = []
    packet_digests: list[str] = []

    for result in packet_results:
        if not isinstance(result, dict) or result.get("schema") != PACKET_RESULT_SCHEMA:
            return _gate_refuse("invalid_packet_result")
        if result.get("authority") != "none":
            return _gate_refuse("invalid_packet_result")
        if result.get("disposition") == "REFUSE":
            return _gate_refuse("packet_refused")

        disposition = result.get("disposition")
        if disposition == "READY":
            receipt = result.get("receipt")
            if (
                not isinstance(receipt, dict)
                or receipt.get("schema") != PACKET_RECEIPT_SCHEMA
                or receipt.get("authority") != "none"
            ):
                return _gate_refuse("invalid_packet_result")
            specimen_type = receipt.get("specimen_type")
            packet_digest = receipt.get("packet_digest")
            if specimen_type == "NOMEN_SACRUM" and not _valid_ref(
                receipt.get("material_witness_ref")
            ):
                return _gate_refuse("invalid_packet_result")
        elif disposition == "BLOCKED":
            specimen_type = result.get("specimen_type")
            packet_digest = result.get("packet_digest")
            if (
                specimen_type != "NOMEN_SACRUM"
                or result.get("reason") != "material_witness_required"
            ):
                return _gate_refuse("invalid_packet_result")
            blocked.append(specimen_type)
        else:
            return _gate_refuse("invalid_packet_result")

        if specimen_type not in SPECIMEN_TYPES or not _valid_ref(packet_digest):
            return _gate_refuse("invalid_packet_result")
        if specimen_type in by_type:
            return _gate_refuse("duplicate_specimen_type")
        by_type[specimen_type] = result
        packet_digests.append(packet_digest)

    if set(by_type) != SPECIMEN_TYPES:
        return _gate_refuse("incomplete_specimen_family")

    gate_digest = sha256_json(record)
    blocked_in_order = [kind for kind in SPECIMEN_TYPE_ORDER if kind in blocked]
    disposition = "DIVE_BLOCKED" if blocked_in_order else "DIVE_READY"
    return {
        "schema": GATE_RESULT_SCHEMA,
        "disposition": disposition,
        "reason": None,
        "blocked_specimen_types": blocked_in_order,
        "receipt": {
            "schema": GATE_RECEIPT_SCHEMA,
            "gate_id": record["gate_id"],
            "gate_digest": gate_digest,
            "specimen_types": list(SPECIMEN_TYPE_ORDER),
            "packet_digests": packet_digests,
            "authority": "none",
        },
        "authority": "none",
    }
