from __future__ import annotations

import copy

from alex_runtime import DERIVATION_M0_PROFILE
from alex_runtime.derivation import (
    _matching_evidence_path,
    _records_by_id,
    evaluate_relation_case,
)
from alex_runtime.handshake import validate_compile_record

LOCAL_SUPPORT_PROFILE = "alex.runtime/local-support-m0"
LOCAL_SUPPORT_RULE_ID = "LOCAL-SUPPORT-001"
LOCAL_SUPPORT_RULE_VERSION = 1


def _nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _projection_valid(projection: object) -> bool:
    return (
        isinstance(projection, dict)
        and projection.get("schema") == "mortal_actor.3rdi-handoff/v0"
        and _nonempty(projection.get("projection_digest"))
        and _nonempty(projection.get("field_id"))
        and _nonempty(projection.get("cut_id"))
        and _nonempty(projection.get("observer"))
        and isinstance(projection.get("visible_occurrence_ids"), list)
    )


def _survivors(*, projection: dict, compile_record: dict, claim_id: object, proposal: dict) -> list[str]:
    values: list[str] = []
    for prefix, value in (
        ("projection", projection.get("projection_digest")),
        ("compile", compile_record.get("compile_id")),
        ("compile_digest", compile_record.get("compile_digest")),
        ("claim_request", claim_id),
        ("relation_proposal", proposal.get("id")),
    ):
        if _nonempty(value):
            values.append(f"{prefix}:{value}")
    return list(dict.fromkeys(values))


def _result(
    *,
    attempt: dict,
    projection: dict,
    compile_record: dict,
    proposal: dict,
    local_disposition: str,
    reason_code: str | None,
    required_local_basis_ids: list[str] | None = None,
    missing_local_basis_ids: list[str] | None = None,
    derivation: dict | None = None,
) -> dict:
    claim_id = attempt.get("claim_id")
    return {
        "profile": LOCAL_SUPPORT_PROFILE,
        "rule_id": LOCAL_SUPPORT_RULE_ID,
        "rule_version": LOCAL_SUPPORT_RULE_VERSION,
        "claim_id": claim_id,
        "cut_id": projection.get("cut_id") if isinstance(projection, dict) else None,
        "observer": projection.get("observer") if isinstance(projection, dict) else None,
        "projection_digest": projection.get("projection_digest") if isinstance(projection, dict) else None,
        "compile_id": compile_record.get("compile_id") if isinstance(compile_record, dict) else None,
        "compile_digest": compile_record.get("compile_digest") if isinstance(compile_record, dict) else None,
        "local_disposition": local_disposition,
        "reason_code": reason_code,
        "required_local_basis_ids": sorted(set(required_local_basis_ids or [])),
        "missing_local_basis_ids": sorted(set(missing_local_basis_ids or [])),
        "derivation": derivation,
        "receipt_survivors": _survivors(
            projection=projection if isinstance(projection, dict) else {},
            compile_record=compile_record if isinstance(compile_record, dict) else {},
            claim_id=claim_id,
            proposal=proposal if isinstance(proposal, dict) else {},
        ),
    }


def _derivation_case(case: dict) -> dict:
    source = copy.deepcopy(case)
    source["operation_type"] = "relation_derivation"
    source["rule_profile"] = DERIVATION_M0_PROFILE
    return source


def evaluate_local_support_case(case: dict) -> dict:
    source = copy.deepcopy(case) if isinstance(case, dict) else {}
    given = source.get("given", {}) if isinstance(source.get("given"), dict) else {}
    attempt = source.get("attempt", {}) if isinstance(source.get("attempt"), dict) else {}
    proposal = attempt.get("relation_proposal", {}) if isinstance(attempt.get("relation_proposal"), dict) else {}
    projection = given.get("projection_handoff", {}) if isinstance(given.get("projection_handoff"), dict) else {}
    compile_record = given.get("evaluation_compile", {}) if isinstance(given.get("evaluation_compile"), dict) else {}

    if source.get("operation_type") != "local_support" or source.get("rule_profile") != LOCAL_SUPPORT_PROFILE:
        return _result(
            attempt=attempt,
            projection=projection,
            compile_record=compile_record,
            proposal=proposal,
            local_disposition="local_basis_unresolved",
            reason_code="PROFILE_OUTSIDE_LOCAL_SUPPORT",
        )

    if not _nonempty(attempt.get("claim_id")):
        return _result(
            attempt=attempt,
            projection=projection,
            compile_record=compile_record,
            proposal=proposal,
            local_disposition="local_basis_unresolved",
            reason_code="CLAIM_ID_REQUIRED",
        )

    if not _projection_valid(projection):
        return _result(
            attempt=attempt,
            projection=projection,
            compile_record=compile_record,
            proposal=proposal,
            local_disposition="projection_mismatch",
            reason_code="PROJECTION_INVALID",
        )

    if projection.get("projection_digest") != attempt.get("expected_projection_digest"):
        return _result(
            attempt=attempt,
            projection=projection,
            compile_record=compile_record,
            proposal=proposal,
            local_disposition="projection_mismatch",
            reason_code="PROJECTION_DIGEST_MISMATCH",
        )

    compile_errors = validate_compile_record(compile_record)
    if (
        compile_errors
        or compile_record.get("compile_id") != attempt.get("expected_evaluation_compile_id")
        or compile_record.get("compile_digest") != attempt.get("expected_evaluation_compile_digest")
    ):
        return _result(
            attempt=attempt,
            projection=projection,
            compile_record=compile_record,
            proposal=proposal,
            local_disposition="compile_mismatch",
            reason_code="COMPILE_MISMATCH",
        )

    records = _records_by_id(given)
    path = _matching_evidence_path(
        given,
        source_id=proposal.get("subject_id"),
        claim_id=proposal.get("object_id"),
        record_ids=set(records),
    )

    if path is None:
        derivation = evaluate_relation_case(_derivation_case(source))
        underlying = derivation.get("evaluation", {})
        disposition = underlying.get("disposition")
        return _result(
            attempt=attempt,
            projection=projection,
            compile_record=compile_record,
            proposal=proposal,
            local_disposition=(
                "local_basis_counterpressured" if disposition == "REFUSE" else "local_basis_unresolved"
            ),
            reason_code=underlying.get("reason_code") or "NO_ATTRIBUTABLE_SUPPORT_PATH",
            derivation=derivation,
        )

    required = [item for item in path.get("basis_ids", []) if isinstance(item, str)]
    visible = {
        item for item in projection.get("visible_occurrence_ids", []) if isinstance(item, str)
    }
    missing = sorted(set(required) - visible)
    if missing:
        return _result(
            attempt=attempt,
            projection=projection,
            compile_record=compile_record,
            proposal=proposal,
            local_disposition="basis_outside_projection",
            reason_code="LOCAL_BASIS_OUTSIDE_PROJECTION",
            required_local_basis_ids=required,
            missing_local_basis_ids=missing,
        )

    derivation = evaluate_relation_case(_derivation_case(source))
    underlying = derivation.get("evaluation", {})
    disposition = underlying.get("disposition")
    if disposition == "ACCEPT":
        local_disposition = "local_basis_accept"
    elif disposition == "REFUSE":
        local_disposition = "local_basis_counterpressured"
    else:
        local_disposition = "local_basis_unresolved"
    return _result(
        attempt=attempt,
        projection=projection,
        compile_record=compile_record,
        proposal=proposal,
        local_disposition=local_disposition,
        reason_code=underlying.get("reason_code"),
        required_local_basis_ids=required,
        derivation=derivation,
    )
