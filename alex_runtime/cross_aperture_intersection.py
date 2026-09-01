from __future__ import annotations

from typing import Any

_ALLOWED_RELATIONS = {"independent", "correlated", "unknown"}


def _best_case_id(case: Any) -> str:
    if isinstance(case, dict):
        value = case.get("case_id")
        if isinstance(value, str) and value:
            return value
    return "unknown-case"


def _best_world_domain_id(case: Any) -> str | None:
    if isinstance(case, dict):
        value = case.get("world_domain_id")
        if isinstance(value, str) and value:
            return value
    return None


def _insufficient(case: Any, reason_code: str) -> dict[str, Any]:
    return {
        "case_id": _best_case_id(case),
        "world_domain_id": _best_world_domain_id(case),
        "disposition": "INSUFFICIENT_TO_TEST",
        "reason_code": reason_code,
        "initial_compatible_states": [],
        "lineage": [],
        "final_compatible_states": [],
        "unique_representative": None,
        "selection_basis": None,
        "authority": "none",
    }


def _validation_reason(case: Any) -> str | None:
    if not isinstance(case, dict):
        return "MALFORMED_CASE"

    case_id = case.get("case_id")
    world_domain_id = case.get("world_domain_id")
    if not isinstance(case_id, str) or not case_id or not isinstance(world_domain_id, str) or not world_domain_id:
        return "MALFORMED_CASE"

    world_states = case.get("world_states")
    if (
        not isinstance(world_states, list)
        or not world_states
        or any(not isinstance(state, str) or not state for state in world_states)
        or len(world_states) != len(set(world_states))
    ):
        return "INVALID_WORLD_DOMAIN"

    cuts = case.get("cuts")
    if not isinstance(cuts, list) or not cuts or any(not isinstance(cut, dict) for cut in cuts):
        return "INVALID_CUTS"

    cut_ids: list[str] = []
    map_ids: list[str] = []
    for cut in cuts:
        cut_id = cut.get("cut_id")
        map_id = cut.get("map_id")
        if not isinstance(cut_id, str) or not cut_id or not isinstance(map_id, str) or not map_id:
            return "INVALID_CUTS"
        cut_ids.append(cut_id)
        map_ids.append(map_id)

    if len(cut_ids) != len(set(cut_ids)):
        return "DUPLICATE_CUT_ID"
    if len(map_ids) != len(set(map_ids)):
        return "DUPLICATE_MAP_ID"

    expected_keys = set(world_states)
    for cut in cuts:
        observation_map = cut.get("map")
        if not isinstance(observation_map, dict) or set(observation_map) != expected_keys:
            return "INCOMPLETE_OBSERVATION_MAP"

    for cut in cuts:
        observation_map = cut["map"]
        if any(not isinstance(value, str) or not value for value in observation_map.values()):
            return "INVALID_MAP_OUTPUT"

    for cut in cuts:
        observed = cut.get("observed")
        if not isinstance(observed, str) or not observed:
            return "INVALID_OBSERVED_OUTPUT"

    for cut in cuts:
        relation = cut.get("relation_declaration", "unknown")
        if relation not in _ALLOWED_RELATIONS:
            return "INVALID_RELATION_DECLARATION"

    return None


def evaluate_cross_aperture_case(case: dict) -> dict[str, Any]:
    """Intersect finite, explicitly declared observer fibers in supplied order.

    The evaluator consumes already-declared maps and observations. It does not
    infer observer cuts, rank witnesses, diagnose model breaks, select from
    non-singleton fog, or mint semantic authority.
    """

    reason = _validation_reason(case)
    if reason is not None:
        return _insufficient(case, reason)

    world_states = list(case["world_states"])
    compatible = list(world_states)
    lineage: list[dict[str, Any]] = []

    for cut in case["cuts"]:
        compatible_before = list(compatible)
        fiber_states = [state for state in world_states if cut["map"][state] == cut["observed"]]
        fiber_set = set(fiber_states)
        compatible = [state for state in compatible_before if state in fiber_set]

        if not compatible:
            effect = "BREAK"
        elif compatible == compatible_before:
            effect = "REDUNDANT"
        else:
            effect = "REFINE"

        lineage.append(
            {
                "cut_id": cut["cut_id"],
                "map_id": cut["map_id"],
                "observed": cut["observed"],
                "relation_declaration": cut.get("relation_declaration", "unknown"),
                "fiber_states": fiber_states,
                "compatible_before": compatible_before,
                "compatible_after": list(compatible),
                "effect": effect,
            }
        )

    if len(compatible) == 0:
        disposition = "MODEL_BREAK"
        reason_code = "INCONSISTENT_OBSERVATIONS"
        representative = None
        selection_basis = None
    elif len(compatible) == 1:
        disposition = "IDENTIFIED_WITHIN_DECLARED_MODEL"
        reason_code = None
        representative = compatible[0]
        selection_basis = "singleton_in_declared_model"
    else:
        disposition = "FOG"
        reason_code = "NON_SINGLETON_COMPATIBLE_SET"
        representative = None
        selection_basis = None

    return {
        "case_id": case["case_id"],
        "world_domain_id": case["world_domain_id"],
        "disposition": disposition,
        "reason_code": reason_code,
        "initial_compatible_states": world_states,
        "lineage": lineage,
        "final_compatible_states": list(compatible),
        "unique_representative": representative,
        "selection_basis": selection_basis,
        "authority": "none",
    }
