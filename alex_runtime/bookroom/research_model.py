from __future__ import annotations

from dataclasses import replace

from alex_runtime.derivation import evaluate_relation_case

from .records import ResearchAssertion, ResearchPressure
from .store import BookRoomStore, RecordNotFound


class ResearchModelError(RuntimeError):
    pass


class ResearchJurisdictionMismatch(ResearchModelError):
    pass


class MissingResearchBasis(ResearchModelError):
    pass


def _require_same_room(store: BookRoomStore, assertion: ResearchAssertion, *, evidence_locus_id: str) -> None:
    try:
        locus = store.get_source_locus(evidence_locus_id)
    except RecordNotFound as exc:
        raise MissingResearchBasis(
            f"{assertion.assertion_id} requires source locus {evidence_locus_id}"
        ) from exc
    if locus.room_id != assertion.room_id:
        raise ResearchJurisdictionMismatch(
            f"{assertion.assertion_id} crosses Book Room jurisdiction via {evidence_locus_id}"
        )


def append_assertion(store: BookRoomStore, assertion: ResearchAssertion) -> ResearchAssertion:
    if assertion.supersedes_assertion_id is not None:
        try:
            parent = store.get_research_assertion(assertion.supersedes_assertion_id)
        except RecordNotFound as exc:
            raise MissingResearchBasis(
                f"{assertion.assertion_id} names missing superseded research assertion "
                f"{assertion.supersedes_assertion_id}"
            ) from exc
        if parent.room_id != assertion.room_id:
            raise ResearchJurisdictionMismatch("research assertion lineage crosses room jurisdiction")
    return store.append_research_assertion(assertion)


def append_counterpressure(store: BookRoomStore, pressure: ResearchPressure) -> ResearchPressure:
    assertion = store.get_research_assertion(pressure.assertion_id)
    if assertion.room_id != pressure.room_id:
        raise ResearchJurisdictionMismatch("research pressure crosses room jurisdiction")
    if assertion.book_cut_id != pressure.book_cut_id:
        raise ResearchJurisdictionMismatch("research pressure crosses Book Cut jurisdiction")
    return store.append_research_pressure(pressure)


def evaluate_support(
    store: BookRoomStore,
    *,
    assertion_id: str,
    evidence_locus_id: str,
    witness_refs: tuple[str, ...],
    case_id: str,
    evidence_path_id: str,
    proposal_id: str,
    evaluation_id: str,
    execution_step_id: str,
    conclusion_assertion_id: str,
) -> dict:
    assertion = store.get_research_assertion(assertion_id)
    _require_same_room(store, assertion, evidence_locus_id=evidence_locus_id)

    case = {
        "case_id": case_id,
        "operation_type": "relation_derivation",
        "rule_profile": "alex.runtime/derivation-m0",
        "given": {
            "records": [
                {"id": evidence_locus_id, "kind": "evidence"},
                {"id": assertion_id, "kind": "candidate_claim"},
            ],
            "relations": [],
            "evidence_paths": [
                {
                    "id": evidence_path_id,
                    "source_id": evidence_locus_id,
                    "claim_id": assertion_id,
                    "basis_ids": [evidence_locus_id],
                    "witness_ids": list(witness_refs),
                    "status": "ATTRIBUTABLE",
                }
            ],
        },
        "attempt": {
            "relation_proposal": {
                "id": proposal_id,
                "subject_id": evidence_locus_id,
                "predicate": "SUPPORTS",
                "object_id": assertion_id,
                "scope": f"research_assertion:{assertion_id}",
                "proposed_by": "bookroom",
                "basis_ids": [evidence_locus_id, evidence_path_id],
            },
            "evaluation_id": evaluation_id,
            "execution_step_id": execution_step_id,
            "conclusion_assertion_id": conclusion_assertion_id,
        },
    }

    result = evaluate_relation_case(case)
    store.append_relation_proposal(assertion_id, result["proposal"])
    store.append_relation_evaluation(assertion_id, result["evaluation"])
    return result


def retire_assertion(
    store: BookRoomStore,
    assertion_id: str,
    *,
    retired_assertion_id: str,
    created_at: str,
) -> ResearchAssertion:
    parent = store.get_research_assertion(assertion_id)
    retired = replace(
        parent,
        assertion_id=retired_assertion_id,
        lifecycle="RETIRED",
        created_at=created_at,
        supersedes_assertion_id=parent.assertion_id,
    )
    return append_assertion(store, retired)
