from __future__ import annotations

from typing import Any


def evaluate_cross_aperture_case(case: dict) -> dict[str, Any]:
    """Evaluate one finite, already-declared cross-aperture specimen.

    This first GREEN slice intentionally implements only the canonical
    non-empty/singleton terminal path. Broader terminal and malformed-input
    behavior is earned by later hostile tests.
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

    representative = compatible[0]
    return {
        "case_id": case["case_id"],
        "world_domain_id": case["world_domain_id"],
        "disposition": "IDENTIFIED_WITHIN_DECLARED_MODEL",
        "reason_code": None,
        "initial_compatible_states": world_states,
        "lineage": lineage,
        "final_compatible_states": list(compatible),
        "unique_representative": representative,
        "selection_basis": "singleton_in_declared_model",
        "authority": "none",
    }
