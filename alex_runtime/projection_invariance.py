from __future__ import annotations

from typing import Any


_SIDE_FIELDS = (
    "world_digest",
    "observer_constraints_digest",
    "visible_input_digest",
    "bounded_context_digest",
    "projection_digest",
    "derivation_digest",
    "serialization_digest",
    "narrative_digest",
    "authority_digest",
)

_BOUNDARY_CHECKS = (
    ("bounded_context_digest", "LOADOUT", "LOADOUT_LEAK"),
    ("projection_digest", "PROJECTION", "PROJECTION_LEAK"),
    ("derivation_digest", "DERIVATION", "DERIVATION_LEAK"),
    ("serialization_digest", "SERIALIZATION", "SERIALIZATION_LEAK"),
    ("narrative_digest", "NARRATIVE", "NARRATIVE_LEAK"),
    ("authority_digest", "AUTHORITY", "AUTHORITY_CHANGED"),
)


def _result(
    case_id: str,
    disposition: str,
    reason_code: str | None,
    leaking_boundary: str | None,
    receipt_survivors: list[str],
) -> dict[str, Any]:
    return {
        "case_id": case_id,
        "disposition": disposition,
        "reason_code": reason_code,
        "leaking_boundary": leaking_boundary,
        "receipt_survivors": receipt_survivors,
    }


def _receipt_refs(side: Any) -> list[str]:
    if not isinstance(side, dict):
        return []
    refs = side.get("receipt_refs")
    if not isinstance(refs, list):
        return []
    return [ref for ref in refs if isinstance(ref, str) and ref]


def _survivors(left: Any, right: Any) -> list[str]:
    return sorted(set(_receipt_refs(left)) | set(_receipt_refs(right)))


def _valid_side(side: Any) -> bool:
    if not isinstance(side, dict):
        return False
    for field in _SIDE_FIELDS:
        value = side.get(field)
        if not isinstance(value, str) or not value:
            return False
    refs = side.get("receipt_refs")
    if not isinstance(refs, list):
        return False
    if any(not isinstance(ref, str) or not ref for ref in refs):
        return False
    if len(refs) != len(set(refs)):
        return False
    return True


def _valid_declared_transform(transform: Any) -> bool:
    if transform is None:
        return True
    if not isinstance(transform, dict):
        return False
    if set(transform) != {"boundary", "receipt_ref"}:
        return False
    return transform.get("boundary") == "NARRATIVE" and isinstance(transform.get("receipt_ref"), str) and bool(
        transform["receipt_ref"]
    )


def _transform_allows_narrative_difference(transform: Any, left: dict, right: dict) -> bool:
    if not isinstance(transform, dict) or transform.get("boundary") != "NARRATIVE":
        return False
    receipt_ref = transform.get("receipt_ref")
    if not isinstance(receipt_ref, str) or not receipt_ref:
        return False
    return receipt_ref in left["receipt_refs"] and receipt_ref in right["receipt_refs"]


def evaluate_projection_invariance_case(case: dict) -> dict[str, Any]:
    """Evaluate one pair of already-formed observer-local projection witnesses.

    This function does not project a world and does not derive historical truth.
    It checks whether hidden differences outside a declared observer-local view
    leaked across successive bounded transformations.
    """

    case_id = case.get("case_id", "unknown-case") if isinstance(case, dict) else "unknown-case"
    if not isinstance(case_id, str) or not case_id:
        case_id = "unknown-case"

    if not isinstance(case, dict):
        return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_CASE", None, [])

    left = case.get("left")
    right = case.get("right")
    survivors = _survivors(left, right)

    if not _valid_side(left) or not _valid_side(right):
        return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_PROJECTION_WITNESS", None, survivors)

    transform = case.get("declared_transform")
    if not _valid_declared_transform(transform):
        return _result(case_id, "INSUFFICIENT_TO_TEST", "INVALID_DECLARED_TRANSFORM", None, survivors)

    if left["world_digest"] == right["world_digest"]:
        return _result(case_id, "INSUFFICIENT_TO_TEST", "WORLDS_NOT_MATERIALLY_DISTINCT", None, survivors)

    if left["observer_constraints_digest"] != right["observer_constraints_digest"]:
        return _result(case_id, "INSUFFICIENT_TO_TEST", "OBSERVER_CONSTRAINTS_NOT_EQUIVALENT", None, survivors)

    if left["visible_input_digest"] != right["visible_input_digest"]:
        return _result(case_id, "INSUFFICIENT_TO_TEST", "VISIBLE_INPUT_NOT_EQUIVALENT", None, survivors)

    for field, boundary, reason_code in _BOUNDARY_CHECKS:
        if left[field] == right[field]:
            continue
        if boundary == "NARRATIVE" and _transform_allows_narrative_difference(transform, left, right):
            continue
        return _result(case_id, "REFUSE", reason_code, boundary, survivors)

    return _result(case_id, "ACCEPT", None, None, survivors)
