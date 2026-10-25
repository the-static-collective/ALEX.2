from __future__ import annotations

from typing import Any

from alex_runtime.derivation import evaluate_relation_case
from alex_runtime.digests import sha256_json

MEDIATED_SUPPORT_RULE_ID = "MEDIATED-SUPPORT-001"
_ALLOWED_CLAIM_CLASSES = {"OBJECT_LOCAL", "POPULATION_GENERALIZATION"}
_COMPARABLE_DERIVATION_DISPOSITIONS = {"ACCEPT", "REFUSE"}


def _string_list(value: Any) -> list[str] | None:
    if not isinstance(value, list):
        return None
    if any(not isinstance(item, str) or not item for item in value):
        return None
    if len(value) != len(set(value)):
        return None
    return list(value)


def _valid_side(side: Any) -> bool:
    if not isinstance(side, dict):
        return False
    if not isinstance(side.get("projection_digest"), str) or not side["projection_digest"]:
        return False
    if not isinstance(side.get("bounded_context_digest"), str) or not side["bounded_context_digest"]:
        return False
    if _string_list(side.get("interest_receipt_refs")) is None:
        return False
    selection = side.get("selection")
    if not isinstance(selection, dict):
        return False
    if selection.get("policy_digest") is not None and (
        not isinstance(selection["policy_digest"], str) or not selection["policy_digest"]
    ):
        return False
    if _string_list(selection.get("receipt_refs")) is None:
        return False
    if _string_list(selection.get("consumed_interest_receipt_refs")) is None:
        return False
    return isinstance(side.get("derivation_case"), dict)


def _proposal_claim_id(side: dict) -> str | None:
    attempt = side.get("derivation_case", {}).get("attempt")
    proposal = attempt.get("relation_proposal") if isinstance(attempt, dict) else None
    value = proposal.get("object_id") if isinstance(proposal, dict) else None
    return value if isinstance(value, str) and value else None


def _support_signature(result: dict) -> dict[str, Any]:
    evaluation = result.get("evaluation") if isinstance(result, dict) else None
    conclusion = result.get("conclusion_assertion") if isinstance(result, dict) else None
    if not isinstance(evaluation, dict):
        return {
            "disposition": "INVALID",
            "reason_code": "INVALID_DERIVATION_RESULT",
            "conclusion": None,
        }

    semantic_conclusion = None
    if isinstance(conclusion, dict):
        semantic_conclusion = {
            "subject_id": conclusion.get("subject_id"),
            "predicate": conclusion.get("predicate"),
            "object_id": conclusion.get("object_id"),
            "scope": conclusion.get("scope"),
        }

    return {
        "disposition": evaluation.get("disposition"),
        "reason_code": evaluation.get("reason_code"),
        "conclusion": semantic_conclusion,
    }


def _evidence_basis(result: dict) -> list[str]:
    evaluation = result.get("evaluation") if isinstance(result, dict) else None
    ids = evaluation.get("input_ids") if isinstance(evaluation, dict) else None
    if not isinstance(ids, list):
        return []
    return [item for item in ids if isinstance(item, str) and item]


def _derivation_comparable(result: dict) -> bool:
    evaluation = result.get("evaluation") if isinstance(result, dict) else None
    if not isinstance(evaluation, dict):
        return False
    return evaluation.get("disposition") in _COMPARABLE_DERIVATION_DISPOSITIONS


def _formation_refs(side: dict) -> set[str]:
    selection = side["selection"]
    return set(side["interest_receipt_refs"]) | set(selection["receipt_refs"]) | set(
        selection["consumed_interest_receipt_refs"]
    )


def _receipt_survivors(left: dict, right: dict, left_result: dict, right_result: dict) -> list[str]:
    survivors = _formation_refs(left) | _formation_refs(right)
    for result in (left_result, right_result):
        evaluation = result.get("evaluation") if isinstance(result, dict) else None
        refs = evaluation.get("required_survivors") if isinstance(evaluation, dict) else None
        if isinstance(refs, list):
            survivors.update(ref for ref in refs if isinstance(ref, str) and ref)
    return sorted(survivors)


def _selection_formation_complete(side: dict) -> bool:
    selection = side["selection"]
    policy = selection["policy_digest"]
    receipts = selection["receipt_refs"]
    consumed = selection["consumed_interest_receipt_refs"]
    if not isinstance(policy, str) or not policy or not receipts:
        return False
    return set(consumed).issubset(set(side["interest_receipt_refs"]))


def _interest_signature(side: dict) -> dict[str, Any]:
    return {
        "interest_receipt_refs": sorted(side["interest_receipt_refs"]),
        "consumed_interest_receipt_refs": sorted(side["selection"]["consumed_interest_receipt_refs"]),
    }


def _side_summary(side: dict, derivation_result: dict) -> dict[str, str]:
    evidence_basis = _evidence_basis(derivation_result)
    return {
        "projection_digest": side["projection_digest"],
        "bounded_context_digest": side["bounded_context_digest"],
        "evidence_basis_digest": sha256_json({"input_ids": evidence_basis}),
        "support_result_digest": sha256_json(_support_signature(derivation_result)),
    }


def _result(
    *,
    case_id: str,
    claim_id: str,
    disposition: str,
    reason_code: str | None,
    mediation_status: str | None,
    support_changed: bool,
    left: dict[str, str] | None = None,
    right: dict[str, str] | None = None,
    receipt_survivors: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "case_id": case_id,
        "claim_id": claim_id,
        "disposition": disposition,
        "reason_code": reason_code,
        "mediation_status": mediation_status,
        "support_changed": support_changed,
        "left": left,
        "right": right,
        "receipt_survivors": receipt_survivors or [],
    }


def _malformed_result(case_id: Any, claim_id: Any) -> dict[str, Any]:
    safe_case_id = case_id if isinstance(case_id, str) and case_id else "unknown-case"
    safe_claim_id = claim_id if isinstance(claim_id, str) and claim_id else "unknown-claim"
    return _result(
        case_id=safe_case_id,
        claim_id=safe_claim_id,
        disposition="INSUFFICIENT_TO_TEST",
        reason_code="MALFORMED_CASE",
        mediation_status=None,
        support_changed=False,
    )


def evaluate_mediated_support_case(case: dict) -> dict[str, Any]:
    if not isinstance(case, dict):
        return _malformed_result(None, None)

    case_id = case.get("case_id")
    claim_id = case.get("claim_id")
    claim_class = case.get("claim_class")
    left = case.get("left")
    right = case.get("right")

    if (
        not isinstance(case_id, str)
        or not case_id
        or not isinstance(claim_id, str)
        or not claim_id
        or claim_class not in _ALLOWED_CLAIM_CLASSES
        or not _valid_side(left)
        or not _valid_side(right)
    ):
        return _malformed_result(case_id, claim_id)

    if _proposal_claim_id(left) != claim_id or _proposal_claim_id(right) != claim_id:
        return _result(
            case_id=case_id,
            claim_id=claim_id,
            disposition="INSUFFICIENT_TO_TEST",
            reason_code="CLAIM_ID_MISMATCH",
            mediation_status=None,
            support_changed=False,
        )

    left_result = evaluate_relation_case(left["derivation_case"])
    right_result = evaluate_relation_case(right["derivation_case"])
    left_summary = _side_summary(left, left_result)
    right_summary = _side_summary(right, right_result)
    support_changed = left_summary["support_result_digest"] != right_summary["support_result_digest"]
    survivors = _receipt_survivors(left, right, left_result, right_result)

    if not _derivation_comparable(left_result) or not _derivation_comparable(right_result):
        return _result(
            case_id=case_id,
            claim_id=claim_id,
            disposition="INSUFFICIENT_TO_TEST",
            reason_code="DERIVATION_NOT_COMPARABLE",
            mediation_status=None,
            support_changed=support_changed,
            left=left_summary,
            right=right_summary,
            receipt_survivors=survivors,
        )

    if _formation_refs(left).intersection(_evidence_basis(left_result)) or _formation_refs(right).intersection(
        _evidence_basis(right_result)
    ):
        return _result(
            case_id=case_id,
            claim_id=claim_id,
            disposition="REFUSE",
            reason_code="INTEREST_AS_SUPPORT",
            mediation_status=None,
            support_changed=support_changed,
            left=left_summary,
            right=right_summary,
            receipt_survivors=survivors,
        )

    if claim_class == "POPULATION_GENERALIZATION" and (
        not _selection_formation_complete(left) or not _selection_formation_complete(right)
    ):
        return _result(
            case_id=case_id,
            claim_id=claim_id,
            disposition="INSUFFICIENT_TO_TEST",
            reason_code="SELECTION_FORMATION_REQUIRED",
            mediation_status=None,
            support_changed=support_changed,
            left=left_summary,
            right=right_summary,
            receipt_survivors=survivors,
        )

    if _interest_signature(left) == _interest_signature(right):
        return _result(
            case_id=case_id,
            claim_id=claim_id,
            disposition="INSUFFICIENT_TO_TEST",
            reason_code="INTEREST_CONTROL_NOT_DIFFERENT",
            mediation_status=None,
            support_changed=support_changed,
            left=left_summary,
            right=right_summary,
            receipt_survivors=survivors,
        )

    evidence_changed = left_summary["evidence_basis_digest"] != right_summary["evidence_basis_digest"]
    if not evidence_changed:
        if support_changed:
            return _result(
                case_id=case_id,
                claim_id=claim_id,
                disposition="REFUSE",
                reason_code="INTEREST_AS_SUPPORT",
                mediation_status=None,
                support_changed=True,
                left=left_summary,
                right=right_summary,
                receipt_survivors=survivors,
            )
        return _result(
            case_id=case_id,
            claim_id=claim_id,
            disposition="ACCEPT",
            reason_code=None,
            mediation_status="DIRECT_EFFECT_ZERO",
            support_changed=False,
            left=left_summary,
            right=right_summary,
            receipt_survivors=survivors,
        )

    consuming_sides = [
        side
        for side in (left, right)
        if bool(side["selection"]["consumed_interest_receipt_refs"])
    ]
    context_changed = left["bounded_context_digest"] != right["bounded_context_digest"]
    if (
        context_changed
        and consuming_sides
        and all(_selection_formation_complete(side) for side in consuming_sides)
    ):
        return _result(
            case_id=case_id,
            claim_id=claim_id,
            disposition="ACCEPT",
            reason_code=None,
            mediation_status="LAWFUL_MEDIATION",
            support_changed=support_changed,
            left=left_summary,
            right=right_summary,
            receipt_survivors=survivors,
        )

    return _result(
        case_id=case_id,
        claim_id=claim_id,
        disposition="INSUFFICIENT_TO_TEST",
        reason_code="SELECTION_FORMATION_REQUIRED",
        mediation_status=None,
        support_changed=support_changed,
        left=left_summary,
        right=right_summary,
        receipt_survivors=survivors,
    )
