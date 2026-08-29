from __future__ import annotations

import re
from typing import Any

from alex_runtime.digests import sha256_json

BATTERY_SCHEMA = "alex.name-null-battery/v0"
BATTERY_RESULT_SCHEMA = "alex.name-null-battery-result/v0"
BATTERY_RECEIPT_SCHEMA = "alex.name-null-battery-receipt/v0"
WORLDS = frozenset({"A", "B", "C", "D"})
EXECUTOR_OWNERS = frozenset({"ALEX", "3rdi", "Dogram", "Wolfram", "external"})
REQUIRED_CONTROL_TYPES = (
    "COMMON_NAME",
    "REFERENT_SHUFFLE",
    "DECODER_SWAP",
    "WORLD_CUTOFF",
    "LABEL_BLIND",
    "EDGE_ABLATION",
)
REQUIRED_CONTROL_TYPE_SET = frozenset(REQUIRED_CONTROL_TYPES)
BATTERY_REQUIRED = (
    "battery_id",
    "hypothesis_ref",
    "target_ref",
    "target_world",
    "producer",
)
CONTROL_REQUIRED = (
    "control_id",
    "control_type",
    "changed_dimension",
    "next_discriminator",
    "executor_owner",
)
SHA256_REF = re.compile(r"^sha256:[0-9a-f]{64}$")


def _refuse(reason: str) -> dict[str, Any]:
    return {
        "schema": BATTERY_RESULT_SCHEMA,
        "disposition": "REFUSE",
        "reason": reason,
        "authority": "none",
    }


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _valid_invariants(value: Any) -> bool:
    return (
        isinstance(value, list)
        and len(value) == len(set(value))
        and all(_nonempty(item) for item in value)
    )


def evaluate_name_null_battery(record: object) -> dict[str, Any]:
    if not isinstance(record, dict):
        return _refuse("not_an_object")
    if record.get("schema") != BATTERY_SCHEMA:
        return _refuse("wrong_schema")
    if any(not _nonempty(record.get(field)) for field in BATTERY_REQUIRED):
        return _refuse("missing_required_field")
    if not SHA256_REF.fullmatch(record["hypothesis_ref"]) or not SHA256_REF.fullmatch(record["target_ref"]):
        return _refuse("invalid_ref")
    if record["target_world"] not in WORLDS:
        return _refuse("invalid_world")

    controls = record.get("controls")
    if not isinstance(controls, list) or not controls:
        return _refuse("invalid_controls")

    control_types: list[str] = []
    for control in controls:
        if not isinstance(control, dict):
            return _refuse("invalid_controls")
        if any(not _nonempty(control.get(field)) for field in CONTROL_REQUIRED):
            return _refuse("invalid_controls")
        control_type = control["control_type"]
        if control_type not in REQUIRED_CONTROL_TYPE_SET:
            return _refuse("invalid_controls")
        control_types.append(control_type)

    if len(control_types) != len(set(control_types)):
        return _refuse("duplicate_control_type")
    if set(control_types) != REQUIRED_CONTROL_TYPE_SET:
        return _refuse("incomplete_control_family")

    controls_by_type = {control["control_type"]: control for control in controls}
    for control_type in REQUIRED_CONTROL_TYPES:
        control = controls_by_type[control_type]
        if control["executor_owner"] not in EXECUTOR_OWNERS:
            return _refuse("invalid_executor_owner")
        invariants = control.get("preserved_invariants")
        if not _valid_invariants(invariants):
            return _refuse("invalid_controls")
        if control["changed_dimension"] in invariants:
            return _refuse("control_dimension_conflict")

    battery_digest = sha256_json(record)
    return {
        "schema": BATTERY_RESULT_SCHEMA,
        "disposition": "ACCEPT",
        "reason": None,
        "receipt": {
            "schema": BATTERY_RECEIPT_SCHEMA,
            "battery_id": record["battery_id"],
            "battery_digest": battery_digest,
            "hypothesis_ref": record["hypothesis_ref"],
            "target_ref": record["target_ref"],
            "target_world": record["target_world"],
            "control_types": list(REQUIRED_CONTROL_TYPES),
            "control_ids": [controls_by_type[t]["control_id"] for t in REQUIRED_CONTROL_TYPES],
            "authority": "none",
        },
        "authority": "none",
    }
