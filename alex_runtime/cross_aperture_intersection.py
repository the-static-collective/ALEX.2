from __future__ import annotations

from typing import Any


def evaluate_cross_aperture_case(case: dict) -> dict[str, Any]:
    """Evaluate one finite, already-declared cross-aperture specimen.

    V0 computes ordered compatible-set intersections only. It does not infer
    observer maps, rank witnesses, diagnose model breaks, or mint authority.
    Full malformed-input refusal semantics are added by the next TDD slice.
    """

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
