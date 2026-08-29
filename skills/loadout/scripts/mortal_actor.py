from __future__ import annotations

from .compile_identity import validate_compile_identity


def _required_string(value: object, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} required")
    return value


def bind_mortal_actor_compiles(
    *,
    run_id: str,
    actor_id: str,
    world_cut_ref: str,
    projection_ref: str,
    entry_compile: dict,
    evaluation_compile: dict,
) -> dict:
    run_id = _required_string(run_id, "run_id")
    actor_id = _required_string(actor_id, "actor_id")
    world_cut_ref = _required_string(world_cut_ref, "world_cut_ref")
    projection_ref = _required_string(projection_ref, "projection_ref")

    entry_errors = validate_compile_identity(entry_compile)
    if entry_errors:
        raise ValueError(f"invalid entry compile: {','.join(entry_errors)}")
    evaluation_errors = validate_compile_identity(evaluation_compile)
    if evaluation_errors:
        raise ValueError(f"invalid evaluation compile: {','.join(evaluation_errors)}")

    same = evaluation_compile["compile_id"] == entry_compile["compile_id"]
    child = evaluation_compile.get("parent_compile_id") == entry_compile["compile_id"]
    if not same and not child:
        raise ValueError("evaluation compile is not an attributable child")

    if child:
        if evaluation_compile["effect_fence_ref"] != entry_compile["effect_fence_ref"]:
            raise ValueError("effect authority changed during mortal recompile")
        if evaluation_compile["effective_effects"] != entry_compile["effective_effects"]:
            raise ValueError("effect authority changed during mortal recompile")
        if evaluation_compile["egress_policy_ref"] != entry_compile["egress_policy_ref"]:
            raise ValueError("egress policy changed during mortal recompile")

    return {
        "schema": "mortal_actor.loadout-binding/v0",
        "run_id": run_id,
        "actor_id": actor_id,
        "world_cut_ref": world_cut_ref,
        "projection_ref": projection_ref,
        "entry_compile_id": entry_compile["compile_id"],
        "entry_compile_digest": entry_compile["compile_digest"],
        "evaluation_compile_id": evaluation_compile["compile_id"],
        "evaluation_compile_digest": evaluation_compile["compile_digest"],
        "recompile_relation": "same" if same else "child",
        "effect_fence_ref": evaluation_compile["effect_fence_ref"],
        "authority_expanded": False,
        "side_effect_executed": False,
    }
