from __future__ import annotations

import copy
import re
from datetime import datetime, timezone

from alex_runtime.digests import sha256_json

ROUTE_BIT_SCHEMA = "ecode.route-bit/v0"
DOOR_SCHEMA = "loadinstead.door/v0"
ROUTE_PROPOSAL_SCHEMA = "loadinstead.route-proposal/v0"
LOADINSTEAD_M0_PROFILE = "loadout.runtime/loadinstead-door-router-m0"

ROUTE_BIT_KEYS = {
    "schema",
    "bit_id",
    "occurred_at",
    "source_world",
    "consequence_class",
    "payload_ref",
    "formation_ref",
    "compile_ref",
    "witness_classes",
}

COMPILE_REF_KEYS = {"compile_id", "compile_digest"}

DOOR_KEYS = {
    "schema",
    "door_id",
    "owner_world",
    "role",
    "accepts_classes",
    "protocol",
    "capability_ref",
    "status",
}

DOOR_ROLES = {"destination", "witness"}
DOOR_STATUSES = {"available", "unavailable"}
SHA256_REF_RE = re.compile(r"^sha256:[0-9a-f]{64}$")


def _unique(errors: list[str]) -> list[str]:
    return list(dict.fromkeys(errors))


def _nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _valid_string_list(value: object, *, allow_empty: bool) -> bool:
    if not isinstance(value, list):
        return False
    if not allow_empty and not value:
        return False
    if not all(_nonempty_string(item) for item in value):
        return False
    return len(value) == len(set(value))


def _valid_instant(value: object) -> bool:
    if not _nonempty_string(value):
        return False
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        instant = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    if instant.tzinfo is None:
        return False
    instant.astimezone(timezone.utc)
    return True


def validate_route_bit(bit_record: dict) -> list[str]:
    errors: list[str] = []
    if not isinstance(bit_record, dict):
        return ["BIT_NOT_OBJECT"]

    if set(bit_record) != ROUTE_BIT_KEYS:
        errors.append("BIT_SHAPE_INVALID")
    if bit_record.get("schema") != ROUTE_BIT_SCHEMA:
        errors.append("BIT_SCHEMA_INVALID")
    if not _nonempty_string(bit_record.get("bit_id")):
        errors.append("BIT_ID_REQUIRED")
    if not _valid_instant(bit_record.get("occurred_at")):
        errors.append("BIT_OCCURRED_AT_INVALID")
    if not _nonempty_string(bit_record.get("source_world")):
        errors.append("BIT_SOURCE_WORLD_REQUIRED")
    if not _nonempty_string(bit_record.get("consequence_class")):
        errors.append("BIT_CONSEQUENCE_CLASS_REQUIRED")
    if not _nonempty_string(bit_record.get("payload_ref")):
        errors.append("BIT_PAYLOAD_REF_REQUIRED")
    if not _nonempty_string(bit_record.get("formation_ref")):
        errors.append("BIT_FORMATION_REF_REQUIRED")

    compile_ref = bit_record.get("compile_ref")
    if (
        not isinstance(compile_ref, dict)
        or set(compile_ref) != COMPILE_REF_KEYS
        or not _nonempty_string(compile_ref.get("compile_id"))
        or not isinstance(compile_ref.get("compile_digest"), str)
        or SHA256_REF_RE.fullmatch(compile_ref.get("compile_digest", "")) is None
    ):
        errors.append("BIT_COMPILE_REF_INVALID")

    if not _valid_string_list(bit_record.get("witness_classes"), allow_empty=True):
        errors.append("BIT_WITNESS_CLASSES_INVALID")

    return _unique(errors)


def validate_door(door_record: dict) -> list[str]:
    errors: list[str] = []
    if not isinstance(door_record, dict):
        return ["DOOR_NOT_OBJECT"]

    if set(door_record) != DOOR_KEYS:
        errors.append("DOOR_SHAPE_INVALID")
    if door_record.get("schema") != DOOR_SCHEMA:
        errors.append("DOOR_SCHEMA_INVALID")
    if not _nonempty_string(door_record.get("door_id")):
        errors.append("DOOR_ID_REQUIRED")
    if not _nonempty_string(door_record.get("owner_world")):
        errors.append("DOOR_OWNER_WORLD_REQUIRED")
    if door_record.get("role") not in DOOR_ROLES:
        errors.append("DOOR_ROLE_INVALID")
    if not _valid_string_list(door_record.get("accepts_classes"), allow_empty=False):
        errors.append("DOOR_ACCEPTS_CLASSES_INVALID")
    if not _nonempty_string(door_record.get("protocol")):
        errors.append("DOOR_PROTOCOL_REQUIRED")
    if not _nonempty_string(door_record.get("capability_ref")):
        errors.append("DOOR_CAPABILITY_REF_REQUIRED")
    if door_record.get("status") not in DOOR_STATUSES:
        errors.append("DOOR_STATUS_INVALID")

    return _unique(errors)


def _validate_or_raise(bit_record: dict, doors: list[dict]) -> None:
    errors = validate_route_bit(bit_record)
    if not isinstance(doors, list):
        errors.append("DOOR_REGISTRY_INVALID")
    else:
        for door in doors:
            errors.extend(validate_door(door))
    errors = _unique(errors)
    if errors:
        raise ValueError(",".join(errors))


def route_bit(bit_record: dict, doors: list[dict]) -> dict:
    bit = copy.deepcopy(bit_record)
    registry = copy.deepcopy(doors)
    _validate_or_raise(bit, registry)

    consequence_class = bit["consequence_class"]
    witness_classes = set(bit["witness_classes"])

    destination_candidates: list[dict] = []
    witness_candidates: list[dict] = []
    rejections: list[dict] = []

    for door in registry:
        accepted = set(door["accepts_classes"])
        destination_match = (
            door["role"] == "destination"
            and consequence_class in accepted
        )
        witness_match = (
            door["role"] == "witness"
            and bool(witness_classes.intersection(accepted))
        )

        if not destination_match and not witness_match:
            continue

        if door["status"] == "unavailable":
            rejections.append(
                {"door_id": door["door_id"], "reason_code": "DOOR_UNAVAILABLE"}
            )
            continue

        if destination_match:
            destination_candidates.append(door)
        if witness_match:
            witness_candidates.append(door)

    if len(destination_candidates) == 1:
        disposition = "ROUTED"
        primary = destination_candidates[0]
    elif not destination_candidates:
        disposition = "UNROUTABLE"
        primary = None
    else:
        disposition = "AMBIGUOUS"
        primary = None

    delivery_envelopes: list[dict] = []
    if primary is not None:
        delivery_envelopes.append(
            {
                "door_id": primary["door_id"],
                "owner_world": primary["owner_world"],
                "protocol": primary["protocol"],
                "payload_ref": bit["payload_ref"],
                "formation_ref": bit["formation_ref"],
                "bit_id": bit["bit_id"],
                "authority": "none",
            }
        )

    proposal = {
        "schema": ROUTE_PROPOSAL_SCHEMA,
        "profile": LOADINSTEAD_M0_PROFILE,
        "bit_id": bit["bit_id"],
        "bit_digest": sha256_json(bit),
        "registry_digest": sha256_json({"doors": registry}),
        "compile_ref": copy.deepcopy(bit["compile_ref"]),
        "disposition": disposition,
        "primary_door_ref": primary["door_id"] if primary is not None else None,
        "candidate_door_refs": [door["door_id"] for door in destination_candidates],
        "witness_door_refs": [door["door_id"] for door in witness_candidates],
        "rejections": rejections,
        "delivery_envelopes": delivery_envelopes,
        "admission_status": "NOT_ATTEMPTED",
        "authority_transferred": False,
    }
    proposal["route_id"] = sha256_json(proposal)
    return copy.deepcopy(proposal)
