from __future__ import annotations

import json
from collections import defaultdict
from typing import Any

SPECIMEN = "TARGET-DETERMINACY-ERASURE-001"


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _string_list(value: Any, *, allow_empty: bool = False) -> bool:
    return (
        isinstance(value, list)
        and (allow_empty or bool(value))
        and all(_nonempty(item) for item in value)
        and len(value) == len(set(value))
    )


def _canonical(value: Any) -> str | None:
    try:
        return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    except (TypeError, ValueError):
        return None


def _invalid(case_id: str, reason: str) -> dict[str, Any]:
    return {
        "specimen": SPECIMEN,
        "case_id": case_id,
        "disposition": "INSUFFICIENT_TO_TEST",
        "reason_code": reason,
        "target_kind": None,
        "projection_fields": [],
        "target_field": None,
        "fiber_count": None,
        "violating_pair": None,
        "refinement": None,
        "authority": "none",
    }


def _projection_value(state: dict[str, Any], fields: list[str]) -> dict[str, Any]:
    return {field: state[field] for field in fields}


def _find_violation(
    states: list[dict[str, Any]],
    projection_fields: list[str],
    target_field: str,
) -> tuple[int, dict[str, Any] | None]:
    fibers: dict[tuple[str, ...], list[dict[str, Any]]] = defaultdict(list)
    for state in sorted(states, key=lambda item: item["state_id"]):
        key = tuple(_canonical(state[field]) or "" for field in projection_fields)
        fibers[key].append(state)

    for fiber_key in sorted(fibers):
        fiber = fibers[fiber_key]
        for index, left in enumerate(fiber):
            left_target = _canonical(left[target_field])
            for right in fiber[index + 1 :]:
                if left_target != _canonical(right[target_field]):
                    return len(fibers), {
                        "left_state_id": left["state_id"],
                        "right_state_id": right["state_id"],
                        "shared_projection": _projection_value(left, projection_fields),
                        "left_target": left[target_field],
                        "right_target": right[target_field],
                    }

    return len(fibers), None


def evaluate_target_determinacy_case(case: object) -> dict[str, Any]:
    """Evaluate target constancy on finite projection fibers.

    This research harness does not infer semantics, causality, truth, authority,
    or policy. It only checks whether every state collapsed by a declared finite
    projection agrees on one declared target field. An optional refinement adds
    more observed fields and repeats the same test.
    """

    if not isinstance(case, dict):
        return _invalid("unknown-case", "MALFORMED_CASE")

    case_id = case.get("case_id")
    if not _nonempty(case_id):
        return _invalid("unknown-case", "INVALID_CASE_ID")

    target_kind = case.get("target_kind")
    target_field = case.get("target_field")
    projection_fields = case.get("projection_fields")
    refinement_fields = case.get("refinement_fields", [])
    states = case.get("states")

    if not _nonempty(target_kind):
        return _invalid(case_id, "INVALID_TARGET_KIND")
    if not _nonempty(target_field):
        return _invalid(case_id, "INVALID_TARGET_FIELD")
    if not _string_list(projection_fields):
        return _invalid(case_id, "INVALID_PROJECTION_FIELDS")
    if not _string_list(refinement_fields, allow_empty=True):
        return _invalid(case_id, "INVALID_REFINEMENT_FIELDS")
    if set(projection_fields) & set(refinement_fields):
        return _invalid(case_id, "REFINEMENT_REPEATS_PROJECTION_FIELD")
    if not isinstance(states, list) or len(states) < 2:
        return _invalid(case_id, "INSUFFICIENT_STATE_FAMILY")

    state_ids: list[str] = []
    required_fields = set(projection_fields) | set(refinement_fields) | {target_field}
    for state in states:
        if not isinstance(state, dict):
            return _invalid(case_id, "MALFORMED_STATE")
        state_id = state.get("state_id")
        if not _nonempty(state_id):
            return _invalid(case_id, "INVALID_STATE_ID")
        state_ids.append(state_id)
        if any(field not in state for field in required_fields):
            return _invalid(case_id, "MISSING_REQUIRED_FIELD")
        if any(_canonical(state[field]) is None for field in required_fields):
            return _invalid(case_id, "NON_JSON_FIELD_VALUE")

    if len(state_ids) != len(set(state_ids)):
        return _invalid(case_id, "DUPLICATE_STATE_ID")

    fiber_count, violation = _find_violation(states, projection_fields, target_field)
    disposition = "DETERMINES_FOR_TARGET" if violation is None else "DOES_NOT_DETERMINE"

    refinement: dict[str, Any] | None = None
    if refinement_fields:
        refined_projection = [*projection_fields, *refinement_fields]
        refined_fiber_count, refined_violation = _find_violation(
            states,
            refined_projection,
            target_field,
        )
        refinement = {
            "added_fields": list(refinement_fields),
            "projection_fields": refined_projection,
            "fiber_count": refined_fiber_count,
            "disposition": (
                "DETERMINES_FOR_TARGET"
                if refined_violation is None
                else "DOES_NOT_DETERMINE"
            ),
            "violating_pair": refined_violation,
        }

    return {
        "specimen": SPECIMEN,
        "case_id": case_id,
        "disposition": disposition,
        "reason_code": None,
        "target_kind": target_kind,
        "projection_fields": list(projection_fields),
        "target_field": target_field,
        "fiber_count": fiber_count,
        "violating_pair": violation,
        "refinement": refinement,
        "authority": "none",
    }
