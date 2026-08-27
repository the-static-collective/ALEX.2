import copy

from alex_runtime import DERIVATION_M0_PROFILE, DERIVATION_RULE_ID, DERIVATION_RULE_VERSION
from alex_runtime.digests import sha256_json
from alex_runtime.predicates import semantic_predicate_allowed

DERIVATION_M0_MANIFEST = {
    "profile": DERIVATION_M0_PROFILE,
    "rules": [
        {
            "rule_id": DERIVATION_RULE_ID,
            "rule_version": DERIVATION_RULE_VERSION,
            "predicate": "SUPPORTS",
            "negative_reason_code": "ATTENTION_NOT_SUPPORT",
            "undefined_reason_code": "NO_ATTRIBUTABLE_SUPPORT_PATH",
        }
    ],
}


def ruleset_manifest(profile: str) -> dict | None:
    if profile != DERIVATION_M0_PROFILE:
        return None
    return copy.deepcopy(DERIVATION_M0_MANIFEST)


def ruleset_manifest_digest(profile: str) -> str | None:
    manifest = ruleset_manifest(profile)
    return None if manifest is None else sha256_json(manifest)


def _records_by_id(given: dict) -> dict[str, dict]:
    records = given.get("records", [])
    return {
        record["id"]: record
        for record in records
        if isinstance(record, dict) and isinstance(record.get("id"), str)
    }


def _relation(
    relations: list,
    *,
    subject_id: str,
    predicate: str,
    object_id: str,
) -> dict | None:
    for relation in relations:
        if not isinstance(relation, dict):
            continue
        if (
            relation.get("subject_id") == subject_id
            and relation.get("predicate") == predicate
            and relation.get("object_id") == object_id
        ):
            return relation
    return None


def _matching_evidence_path(
    given: dict,
    *,
    source_id: str,
    claim_id: str,
    record_ids: set[str],
) -> dict | None:
    for path in given.get("evidence_paths", []):
        if not isinstance(path, dict):
            continue
        basis_ids = path.get("basis_ids")
        witness_ids = path.get("witness_ids")
        if (
            path.get("source_id") == source_id
            and path.get("claim_id") == claim_id
            and path.get("status") == "ATTRIBUTABLE"
            and isinstance(basis_ids, list)
            and bool(basis_ids)
            and source_id in basis_ids
            and all(isinstance(basis_id, str) and basis_id in record_ids for basis_id in basis_ids)
            and isinstance(witness_ids, list)
            and bool(witness_ids)
            and all(isinstance(witness_id, str) and witness_id for witness_id in witness_ids)
        ):
            return path
    return None


def _attention_chain(given: dict, breadcrumb_id: str, records: dict[str, dict]) -> tuple[str, str] | None:
    breadcrumb = records.get(breadcrumb_id)
    if breadcrumb is None or breadcrumb.get("kind") != "breadcrumb":
        return None

    relations = given.get("relations", [])
    for search_id, search_record in records.items():
        if search_record.get("kind") != "search":
            continue
        if _relation(
            relations,
            subject_id=search_id,
            predicate="caused_by",
            object_id=breadcrumb_id,
        ) is None:
            continue
        for evidence_id, evidence_record in records.items():
            if evidence_record.get("kind") != "evidence":
                continue
            if _relation(
                relations,
                subject_id=evidence_id,
                predicate="acquired_from",
                object_id=search_id,
            ) is not None:
                return search_id, evidence_id
    return None


def _unique(items: list[str]) -> list[str]:
    return list(dict.fromkeys(items))


def _evaluation(
    case: dict,
    proposal: dict,
    *,
    disposition: str,
    reason_code: str | None,
    survivors: list[str],
    input_ids: list[str],
    conclusion_assertion_id: str | None,
) -> dict:
    attempt = case.get("attempt", {})
    return {
        "proposal_id": proposal.get("id"),
        "evaluation_id": attempt.get("evaluation_id"),
        "rule_id": DERIVATION_RULE_ID,
        "rule_version": DERIVATION_RULE_VERSION,
        "ruleset_digest": ruleset_manifest_digest(DERIVATION_M0_PROFILE),
        "input_ids": _unique(input_ids),
        "input_digest": case.get("input_digest"),
        "execution_step_id": attempt.get("execution_step_id"),
        "disposition": disposition,
        "reason_code": reason_code,
        "required_survivors": _unique(survivors),
        "conclusion_assertion_id": conclusion_assertion_id,
        "residual_fog": [],
    }


def _result(evaluation: dict, proposal: dict, conclusion_assertion: dict | None = None) -> dict:
    return {
        "proposal": proposal,
        "evaluation": evaluation,
        "conclusion_assertion": conclusion_assertion,
        "execution": {"terminal_state": "FINISHED", "step_count": 1},
    }


def evaluate_relation_case(case: dict) -> dict:
    source = copy.deepcopy(case)
    given = source.get("given", {})
    attempt = source.get("attempt", {})
    proposal = copy.deepcopy(attempt.get("relation_proposal", {}))
    records = _records_by_id(given)
    record_ids = set(records)

    proposal_id = proposal.get("id")
    evaluation_id = attempt.get("evaluation_id")
    subject_id = proposal.get("subject_id")
    object_id = proposal.get("object_id")
    predicate = proposal.get("predicate")
    scope = proposal.get("scope")
    proposal_basis_ids = proposal.get("basis_ids", [])

    base_survivors = []
    if isinstance(proposal_id, str):
        base_survivors.append(f"relation_proposal:{proposal_id}")
    if isinstance(evaluation_id, str):
        base_survivors.append(f"evaluation:{evaluation_id}")

    if source.get("operation_type") != "relation_derivation":
        return _result(
            _evaluation(
                source,
                proposal,
                disposition="INSUFFICIENT_TO_TEST",
                reason_code="OPERATION_OUTSIDE_PROFILE",
                survivors=base_survivors,
                input_ids=list(proposal_basis_ids) if isinstance(proposal_basis_ids, list) else [],
                conclusion_assertion_id=None,
            ),
            proposal,
        )

    if source.get("rule_profile") != DERIVATION_M0_PROFILE:
        return _result(
            _evaluation(
                source,
                proposal,
                disposition="INSUFFICIENT_TO_TEST",
                reason_code="RULE_PROFILE_OUTSIDE_PROFILE",
                survivors=base_survivors,
                input_ids=list(proposal_basis_ids) if isinstance(proposal_basis_ids, list) else [],
                conclusion_assertion_id=None,
            ),
            proposal,
        )

    if not semantic_predicate_allowed(DERIVATION_M0_PROFILE, predicate):
        return _result(
            _evaluation(
                source,
                proposal,
                disposition="REFUSE",
                reason_code="PREDICATE_OUTSIDE_PROFILE",
                survivors=base_survivors,
                input_ids=list(proposal_basis_ids) if isinstance(proposal_basis_ids, list) else [],
                conclusion_assertion_id=None,
            ),
            proposal,
        )

    if not isinstance(scope, str) or not scope.strip():
        return _result(
            _evaluation(
                source,
                proposal,
                disposition="INSUFFICIENT_TO_TEST",
                reason_code="MISSING_PROPOSAL_SCOPE",
                survivors=base_survivors,
                input_ids=list(proposal_basis_ids) if isinstance(proposal_basis_ids, list) else [],
                conclusion_assertion_id=None,
            ),
            proposal,
        )

    if subject_id not in records or object_id not in records:
        survivors = list(base_survivors)
        if subject_id in records:
            survivors.insert(0, f"record:{subject_id}")
        if object_id in records:
            survivors.insert(0, f"record:{object_id}")
        return _result(
            _evaluation(
                source,
                proposal,
                disposition="INSUFFICIENT_TO_TEST",
                reason_code="MISSING_PROPOSAL_RECORD",
                survivors=survivors,
                input_ids=list(proposal_basis_ids) if isinstance(proposal_basis_ids, list) else [],
                conclusion_assertion_id=None,
            ),
            proposal,
        )

    evidence_path = _matching_evidence_path(
        given,
        source_id=subject_id,
        claim_id=object_id,
        record_ids=record_ids,
    )
    if evidence_path is not None:
        path_id = evidence_path.get("id")
        basis_set = set(proposal_basis_ids) if isinstance(proposal_basis_ids, list) else set()
        if not isinstance(path_id, str) or subject_id not in basis_set or path_id not in basis_set:
            return _result(
                _evaluation(
                    source,
                    proposal,
                    disposition="INSUFFICIENT_TO_TEST",
                    reason_code="PROPOSAL_BASIS_INSUFFICIENT",
                    survivors=[f"record:{subject_id}", f"record:{object_id}", *base_survivors],
                    input_ids=list(proposal_basis_ids) if isinstance(proposal_basis_ids, list) else [],
                    conclusion_assertion_id=None,
                ),
                proposal,
            )

        conclusion_id = attempt.get("conclusion_assertion_id")
        conclusion = {
            "id": conclusion_id,
            "subject_id": subject_id,
            "predicate": "SUPPORTS",
            "object_id": object_id,
            "scope": scope,
            "derived_by_evaluation_id": evaluation_id,
        }
        survivors = [
            f"record:{subject_id}",
            f"record:{object_id}",
            f"evidence_path:{path_id}",
            *base_survivors,
            f"conclusion_assertion:{conclusion_id}",
        ]
        input_ids = [*proposal_basis_ids, path_id]
        return _result(
            _evaluation(
                source,
                proposal,
                disposition="ACCEPT",
                reason_code=None,
                survivors=survivors,
                input_ids=input_ids,
                conclusion_assertion_id=conclusion_id,
            ),
            proposal,
            conclusion,
        )

    attention = _attention_chain(given, subject_id, records)
    if attention is not None:
        search_id, evidence_id = attention
        survivors = [
            f"record:{subject_id}",
            f"record:{search_id}",
            f"record:{evidence_id}",
            f"record:{object_id}",
            *base_survivors,
        ]
        return _result(
            _evaluation(
                source,
                proposal,
                disposition="REFUSE",
                reason_code="ATTENTION_NOT_SUPPORT",
                survivors=survivors,
                input_ids=[
                    *(proposal_basis_ids if isinstance(proposal_basis_ids, list) else []),
                    search_id,
                    evidence_id,
                ],
                conclusion_assertion_id=None,
            ),
            proposal,
        )

    return _result(
        _evaluation(
            source,
            proposal,
            disposition="INSUFFICIENT_TO_TEST",
            reason_code="NO_ATTRIBUTABLE_SUPPORT_PATH",
            survivors=[f"record:{subject_id}", f"record:{object_id}", *base_survivors],
            input_ids=list(proposal_basis_ids) if isinstance(proposal_basis_ids, list) else [],
            conclusion_assertion_id=None,
        ),
        proposal,
    )
