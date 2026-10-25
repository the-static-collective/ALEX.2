from __future__ import annotations


def retrospective_view_from_retained_carrier(
    *,
    retained: dict[str, object],
    later_rule: dict[str, str],
    declared_at: int,
    applied_at: int,
) -> dict[str, object]:
    """Apply later analysis only to distinctions actually retained by the source receipt."""
    if applied_at < declared_at:
        return {
            "experiment": "LOST-DISTINCTION-NOT-RESURRECTED-001",
            "status": "REFUSE",
            "reason": "rule-not-yet-declared",
            "authority": "none",
        }

    retained_value = retained["value"]
    source_candidates = tuple(retained.get("source_candidates", ()))
    uniquely_retained = len(source_candidates) == 1

    if uniquely_retained:
        source_value = source_candidates[0]
        derived_value = later_rule.get(str(source_value))
        status = "DERIVED_FROM_RETAINED_DISTINCTION"
    else:
        source_value = None
        derived_value = later_rule.get(str(retained_value))
        status = "DISTINCTION_UNRECOVERABLE_FROM_RETAINED_CARRIER"

    return {
        "experiment": "LOST-DISTINCTION-NOT-RESURRECTED-001",
        "status": status,
        "derived_from": retained["receipt_id"],
        "retained_value": retained_value,
        "retained_source_candidates": list(source_candidates),
        "source_value": source_value,
        "derived_value": derived_value,
        "declared_at": declared_at,
        "applied_at": applied_at,
        "authority": "none",
    }
