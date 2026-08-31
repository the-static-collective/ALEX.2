from __future__ import annotations

from typing import Any


TRAVERSAL_AXES = {
    "SCALE",
    "DIRECTION",
    "OBJECT_RELATION",
    "REPRESENTATION",
    "TIME",
    "COMPRESSION_REGENERATION",
}

NOVELTY_TYPES = {
    "NEW_WORDING",
    "NEW_REPRESENTATION",
    "NEW_DERIVATION",
    "NEW_RELATION",
    "NEW_INVARIANT",
    "NEW_PREDICTION",
}

DIMENSIONAL_NOVELTY_TYPES = {
    "NEW_DERIVATION",
    "NEW_RELATION",
    "NEW_INVARIANT",
    "NEW_PREDICTION",
}

PRESSURE_KINDS = {
    "NEAREST_BORING",
    "METAPHOR_REMOVAL",
    "REPRESENTATION_SWAP",
    "RELABEL",
    "PARAMETER_SWAP",
    "HOLDOUT",
    "REGENERATION_FAILURE",
}

REQUIRED_PRESSURES = {
    "NEAREST_BORING",
    "METAPHOR_REMOVAL",
    "REPRESENTATION_SWAP",
    "RELABEL",
    "HOLDOUT",
    "REGENERATION_FAILURE",
}


def normalize_statement(text: str) -> str:
    return " ".join(text.split())


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _valid_string_list(value: Any) -> bool:
    return isinstance(value, list) and all(_nonempty_string(item) for item in value)


def validate_far_side_case(case: object) -> tuple[bool, str | None]:
    if not isinstance(case, dict):
        return False, "INSUFFICIENT_RECEIPT"

    if not _nonempty_string(case.get("case_id")) or not _nonempty_string(case.get("h0")):
        return False, "INSUFFICIENT_RECEIPT"

    baseline = case.get("baseline")
    if not isinstance(baseline, dict):
        return False, "INSUFFICIENT_BASELINE"
    claims = baseline.get("claims")
    invariants = baseline.get("invariants")
    if not isinstance(claims, list) or not isinstance(invariants, list) or (not claims and not invariants):
        return False, "INSUFFICIENT_BASELINE"
    for claim in claims:
        if not isinstance(claim, dict):
            return False, "INSUFFICIENT_BASELINE"
        if not _nonempty_string(claim.get("id")) or not _nonempty_string(claim.get("statement")):
            return False, "INSUFFICIENT_BASELINE"
    if not _valid_string_list(invariants):
        return False, "INSUFFICIENT_BASELINE"

    traversals = case.get("traversals")
    if not isinstance(traversals, list) or not traversals:
        return False, "INSUFFICIENT_RECEIPT"
    for traversal in traversals:
        if not isinstance(traversal, dict):
            return False, "INSUFFICIENT_RECEIPT"
        if traversal.get("axis") not in TRAVERSAL_AXES:
            return False, "INSUFFICIENT_RECEIPT"
        if not _nonempty_string(traversal.get("id")):
            return False, "INSUFFICIENT_RECEIPT"
        if not _nonempty_string(traversal.get("transform")):
            return False, "INSUFFICIENT_RECEIPT"
        if not _nonempty_string(traversal.get("receipt_ref")):
            return False, "INSUFFICIENT_RECEIPT"
        if not _valid_string_list(traversal.get("invariants")):
            return False, "INSUFFICIENT_RECEIPT"
        if not _valid_string_list(traversal.get("losses")):
            return False, "INSUFFICIENT_RECEIPT"

    candidate = case.get("candidate")
    if not isinstance(candidate, dict) or not _nonempty_string(candidate.get("statement")):
        return False, "INSUFFICIENT_RECEIPT"
    if not _valid_string_list(candidate.get("required_targets")):
        return False, "INSUFFICIENT_RECEIPT"
    if not _valid_string_list(candidate.get("regenerated_targets")):
        return False, "INSUFFICIENT_RECEIPT"

    novelty = candidate.get("novelty")
    if not isinstance(novelty, list):
        return False, "INSUFFICIENT_RECEIPT"
    for item in novelty:
        if not isinstance(item, dict):
            return False, "INSUFFICIENT_RECEIPT"
        if item.get("type") not in NOVELTY_TYPES:
            return False, "INSUFFICIENT_RECEIPT"
        if not _nonempty_string(item.get("statement")):
            return False, "INSUFFICIENT_RECEIPT"
        if not _nonempty_string(item.get("discriminator")):
            return False, "INSUFFICIENT_RECEIPT"
        if not _nonempty_string(item.get("receipt_ref")):
            return False, "INSUFFICIENT_RECEIPT"

    pressure = case.get("pressure")
    if not isinstance(pressure, list):
        return False, "INSUFFICIENT_RECEIPT"
    for check in pressure:
        if not isinstance(check, dict):
            return False, "INSUFFICIENT_RECEIPT"
        if check.get("kind") not in PRESSURE_KINDS:
            return False, "INSUFFICIENT_RECEIPT"
        if check.get("status") not in {"PASS", "FAIL", "NOT_APPLICABLE"}:
            return False, "INSUFFICIENT_RECEIPT"
        if not _nonempty_string(check.get("receipt_ref")):
            return False, "INSUFFICIENT_RECEIPT"

    return True, None
