from __future__ import annotations

import copy

from alex_runtime import DERIVATION_M0_PROFILE
from alex_runtime.derivation import _matching_evidence_path, _records_by_id, evaluate_relation_case
from alex_runtime.handshake import validate_compile_record

LOCAL_SUPPORT_PROFILE = "alex.runtime/local-support-m0"
LOCAL_SUPPORT_RULE_ID = "LOCAL-SUPPORT-001"
LOCAL_SUPPORT_RULE_VERSION = 1


def _nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _unique(values: list[str]) -> list[str]:
    return list(dict.fromkeys(value for value in values if isinstance(value, str) and value))


def _result(
    *,
    attempt: dict,
    projection: dict,
    compile_record: dict,
    local_disposition: str,
    reason_code: str | None,
    required_local_basis_ids: list[str] | None = None,
    missing_local_basis_ids: list[str] | None = None,
    derivation: dict | None = None,
) -> dict:
    claim_id = attempt.get("claim_id")
    projection_digest = projection.get("projection_digest") if isinstance(projection, dict) else None
    compile_id = compile_record.get("compile_id") if isinstance(compile_record, dict) else None
    compile_digest = compile_record.get("compile_digest") if isinstance(compile_record, dict) else None
    proposal = attempt.get("relation_proposal") if isinstance(attempt.get("relation_proposal"), dict) else {}
    survivors: list[str] = []
    if _nonempty(projection_digest):
        survivors.append(f"projection:{projection_digest}")
    if _nonempty(compile_id):
        survivors.append(f"compile:{compile_id}")
    if _nonempty(compile_digest):
        survivors.append(f"compile_digest:{compile_digest}")
    if _nonempty(claim_id):
        survivors.append(f"claim_request:{claim_id}")
    if _nonempty(proposal.get("id")):
        survivors.append(f'relation_proposal:{proposal["id"]}')
    return {
        "profile": LOCAL_SUPPORT_PROFILE,
        "rule_id": LOCAL_SUPPORT_RULE_ID,
        "rule_version": LOCAL_SUPPORT_RULE_VERSION,
        "claim_id": claim_id,
        "cut_id": projection.get("cut_id") if isinstance(projection, dict) else None,
        "observer": projection.get("observer") if isinstance(projection, dict) else None,
        "projection_digest": projection_digest,
        "compile_id": compile_id,
        "compile_digest": compile_digest,
        "local_disposition": local_disposition,
        "reason_code": reason_code,
        "required_local_basis_ids": sorted(set(required_local_basis_ids or [])),
        "missing_local_basis_ids": sorted(set(missing_local_basis_ids or [])),
        "derivation": derivation,
        "receipt_survivors": _unique(survivors),
    }


def _derivation_case(source: dict) -> dict:
    given = source.get("given", {})
    attempt = source.get("attempt", {})
    return {
        "operation_type": "relation_derivation",
        "rule_profile": DERIVATION_M0_PROFILE,
        "given": {
            "records": copy.deepcopy(given.get("records", [])),
            "evidence_paths": copy.deepcopy(given.get("evidence_paths", [])),
            "relations": copy.deepcopy(given.get("relations", [])),
        },
        "attempt": {
            "relation_proposal": copy.deepcopy(attempt.get("relation_proposal", {})),
            "evaluation_id": attempt.get("evaluation_id"),
            "execution_step_id": attempt.get("execution_step_id"),
            "conclusion_assertion_id": attempt.get("conclusion_assertion_id"),
        },
        "input_digest": source.get("input_digest"),
    }


def evaluate_local_support_case(case: dict) -> dict:
    source = copy.deepcopy(case) if isinstance(case, dict) else {}
    given = source.get("given", {}) if isinstance(source.get("given"), dict) else {}
    attempt = source.get("attempt", {}) if isinstance(source.get("attempt"), dict) else {}
    projection = given.get("projection_handoff", {}) if isinstance(given.get("projection_handoff"), dict) else {}
    compile_record = given.get("evaluation_compile", {}) if isinstance(given.get("evaluation_compile"), dict) else {}

    if source.get("operation_type") != "local_support" or source.get("rule_profile") != LOCAL_SUPPORT_PROFILE:
        return _result(
            attempt=attempt,
            projection=projection,
            compile_record=compile_record,
            local_disposition="local_basis_unresolved",
            reason_code="OPERATION_OUTSIDE_PROFILE",
        )

    if not _nonempty(attempt.get("claim_id")):
        return _result(
            attempt=attempt,
            projection=projection,
            compile_record=compile_record,
            local_disposition="local_basis_unresolved",
            reason_code="CLAIM_ID_REQUIRED",
        )

    projection_valid = (
        projection.get("schema") == "mortal_actor.3rdi-handoff/v0"
        and _nonempty(projection.get("projection_digest"))
        and _nonempty(projection.get("cut_id"))
        and _nonempty(projection.get("observer"))
        and isinstance(projection.get("visible_occurrence_ids"), list)
    )
    if (
        not projection_valid
        or projection.get("projection_digest") != attempt.get("expected_projection_digest")
    ):
        return _result(
            attempt=attempt,
            projection=projection,
            compile_record=compile_record,
            local_disposition="projection_mismatch",
            reason_code="PROJECTION_IDENTITY_MISMATCH",
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
            local_disposition="compile_mismatch",
            reason_code="COMPILE_IDENTITY_MISMATCH",
        )

    proposal = attempt.get("relation_proposal") if isinstance(attempt.get("relation_proposal"), dict) else {}
    records = _records_by_id(given)
    source_id = proposal.get("subject_id")
    object_id = proposal.get("object_id")
    path = _matching_evidence_path(
        given,
        source_id=source_id,
        claim_id=object_id,
        record_ids=set(records),
    ) if _nonempty(source_id) and _nonempty(object_id) else None

    if path is not None:
        required = [basis_id for basis_id in path.get("basis_ids", []) if isinstance(basis_id, str)]
        visible = set(projection.get("visible_occurrence_ids", []))
        missing = sorted(set(required) - visible)
        if missing:
            return _result(
                attempt=attempt,
                projection=projection,
                compile_record=compile_record,
                local_disposition="basis_outside_projection",
                reason_code="LOCAL_BASIS_OUTSIDE_PROJECTION",
                required_local_basis_ids=required,
                missing_local_basis_ids=missing,
            )

    derivation = evaluate_relation_case(_derivation_case(source))
    underlying = derivation.get("evaluation", {}).get("disposition")
    if underlying == "ACCEPT":
        disposition = "local_basis_accept"
    elif underlying == "REFUSE":
        disposition = "local_basis_counterpressured"
    else:
        disposition = "local_basis_unresolved"
    reason = derivation.get("evaluation", {}).get("reason_code")
    required = path.get("basis_ids", []) if path is not None else []
    return _result(
        attempt=attempt,
        projection=projection,
        compile_record=compile_record,
        local_disposition=disposition,
        reason_code=reason,
        required_local_basis_ids=required,
        derivation=derivation,
    )
