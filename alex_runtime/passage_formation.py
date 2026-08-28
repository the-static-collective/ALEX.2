from __future__ import annotations

from alex_runtime.digests import sha256_json


def _nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _string_list(value: object) -> bool:
    return isinstance(value, list) and all(_nonempty(item) for item in value)


def _validate_loadout(binding: object) -> bool:
    return (
        isinstance(binding, dict)
        and binding.get("schema") == "mortal_actor.loadout-binding/v0"
        and _nonempty(binding.get("projection_ref"))
        and _nonempty(binding.get("entry_compile_id"))
        and _nonempty(binding.get("entry_compile_digest"))
        and _nonempty(binding.get("evaluation_compile_id"))
        and _nonempty(binding.get("evaluation_compile_digest"))
        and binding.get("authority_expanded") is False
        and binding.get("side_effect_executed") is False
    )


def _validate_projection(handoff: object) -> bool:
    required_lists = (
        "visible_occurrence_ids",
        "contact_ids",
        "attention_event_ids",
        "decoder_application_ids",
        "stance_ids",
    )
    return (
        isinstance(handoff, dict)
        and handoff.get("schema") == "mortal_actor.3rdi-handoff/v0"
        and _nonempty(handoff.get("projection_digest"))
        and _nonempty(handoff.get("cut_id"))
        and _nonempty(handoff.get("observer"))
        and all(_string_list(handoff.get(key)) for key in required_lists)
    )


def _validate_local_support(result: object) -> bool:
    return (
        isinstance(result, dict)
        and result.get("profile") == "alex.runtime/local-support-m0"
        and _nonempty(result.get("claim_id"))
        and _nonempty(result.get("cut_id"))
        and _nonempty(result.get("projection_digest"))
        and _nonempty(result.get("compile_id"))
        and _nonempty(result.get("compile_digest"))
        and _nonempty(result.get("local_disposition"))
        and isinstance(result.get("receipt_survivors"), list)
        and isinstance(result.get("derivation"), dict)
    )


def _validate_result_occurrence(result: object) -> bool:
    return (
        isinstance(result, dict)
        and set(result) == {"id", "payload_ref"}
        and _nonempty(result.get("id"))
        and _nonempty(result.get("payload_ref"))
    )


def bind_passage_formation(
    *,
    road_id: str,
    loadout_binding: dict,
    projection_handoff: dict,
    local_support_result: dict,
    result_occurrence: dict,
) -> dict:
    if not _nonempty(road_id):
        raise ValueError("RESULT_OCCURRENCE_INVALID")
    if not _validate_loadout(loadout_binding):
        raise ValueError("LOADOUT_BINDING_INVALID")
    if not _validate_projection(projection_handoff):
        raise ValueError("PROJECTION_HANDOFF_INVALID")
    if not _validate_local_support(local_support_result):
        raise ValueError("LOCAL_SUPPORT_RESULT_INVALID")
    if not _validate_result_occurrence(result_occurrence):
        raise ValueError("RESULT_OCCURRENCE_INVALID")

    projection_digest = projection_handoff["projection_digest"]
    if (
        loadout_binding["projection_ref"] != projection_digest
        or local_support_result["projection_digest"] != projection_digest
    ):
        raise ValueError("PROJECTION_BINDING_MISMATCH")
    if local_support_result["cut_id"] != projection_handoff["cut_id"]:
        raise ValueError("CUT_BINDING_MISMATCH")
    if (
        local_support_result["compile_id"] != loadout_binding["evaluation_compile_id"]
        or local_support_result["compile_digest"]
        != loadout_binding["evaluation_compile_digest"]
    ):
        raise ValueError("COMPILE_BINDING_MISMATCH")

    derivation = local_support_result["derivation"]
    evaluation = derivation.get("evaluation") if isinstance(derivation, dict) else None
    if (
        local_support_result.get("local_disposition") != "local_basis_accept"
        or not isinstance(evaluation, dict)
        or evaluation.get("disposition") != "ACCEPT"
        or not _nonempty(evaluation.get("conclusion_assertion_id"))
        or not _nonempty(evaluation.get("evaluation_id"))
        or not _nonempty(evaluation.get("ruleset_digest"))
        or not _string_list(evaluation.get("input_ids"))
    ):
        raise ValueError("LOCAL_SUPPORT_NOT_FORMED")

    basis = {
        "entry_compile_id": loadout_binding["entry_compile_id"],
        "entry_compile_digest": loadout_binding["entry_compile_digest"],
        "evaluation_compile_id": loadout_binding["evaluation_compile_id"],
        "evaluation_compile_digest": loadout_binding["evaluation_compile_digest"],
        "projection_digest": projection_digest,
        "cut_id": projection_handoff["cut_id"],
        "observer": projection_handoff["observer"],
        "contact_ids": sorted(set(projection_handoff["contact_ids"])),
        "attention_event_ids": sorted(set(projection_handoff["attention_event_ids"])),
        "decoder_application_ids": sorted(set(projection_handoff["decoder_application_ids"])),
        "stance_ids": sorted(set(projection_handoff["stance_ids"])),
        "claim_id": local_support_result["claim_id"],
        "derivation_evaluation_id": evaluation["evaluation_id"],
        "derivation_ruleset_digest": evaluation["ruleset_digest"],
        "derivation_input_ids": sorted(set(evaluation["input_ids"])),
        "conclusion_assertion_id": evaluation["conclusion_assertion_id"],
    }
    basis_digest = sha256_json(basis)
    receipt = {
        "schema": "passage_world.alex-formation/v0",
        "road_id": road_id,
        "result_occurrence_id": result_occurrence["id"],
        "payload_ref": result_occurrence["payload_ref"],
        "formation_basis": basis,
        "formation_basis_digest": basis_digest,
        "authority_transferred": False,
        "admission_status": "NOT_ATTEMPTED",
    }
    receipt["formation_id"] = sha256_json(receipt)
    return receipt
