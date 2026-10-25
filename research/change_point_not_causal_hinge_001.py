from __future__ import annotations

from typing import Any

SCHEMA = "alex.change-point-not-causal-hinge/v0"


def witness_change_point(
    *,
    encounter_ref: str | None,
    grammar_changed: bool,
    competing_event_refs: list[str] | None = None,
    causal_design_ref: str | None = None,
) -> dict[str, Any]:
    """Classify temporal association without manufacturing causal attribution.

    This deliberately tiny witness does not perform causal inference.  It keeps
    encounter presence, observed grammar delta, and competing events separate.
    A causal design reference is retained as provenance only; this experiment
    never promotes it into a caused-by verdict.
    """
    competing = list(competing_event_refs or [])
    if any(not isinstance(ref, str) or not ref.strip() for ref in competing):
        return {
            "schema": SCHEMA,
            "disposition": "REFUSE",
            "reason": "invalid_competing_event_ref",
            "authority": "none",
        }

    encounter_present = isinstance(encounter_ref, str) and bool(encounter_ref.strip())
    temporal_association_observed = encounter_present and grammar_changed

    if not encounter_present and grammar_changed:
        case = "grammar_delta_without_encounter"
    elif encounter_present and grammar_changed and competing:
        case = "encounter_plus_competing_event_plus_delta"
    elif encounter_present and grammar_changed:
        case = "encounter_plus_delta"
    elif encounter_present:
        case = "encounter_without_grammar_delta"
    else:
        case = "no_encounter_no_grammar_delta"

    return {
        "schema": SCHEMA,
        "disposition": "ACCEPT",
        "case": case,
        "encounter_ref": encounter_ref if encounter_present else None,
        "grammar_changed": grammar_changed,
        "competing_event_refs": competing,
        "temporal_association_observed": temporal_association_observed,
        "causal_design_ref": causal_design_ref,
        "causal_status": "not_established",
        "caused_by": None,
        "authority": "none",
        "meaning_verdict": "none",
    }
