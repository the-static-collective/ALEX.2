"""ELIGIBILITY-INDEPENDENCE-001 experimental discriminator.

This module is deliberately outside ``alex_runtime``. It audits whether a supplied
single-handoff matrix contains the hostile rows named by the ALEX research packet.
A witnessed matrix is not authority, consent, execution, truth, runtime canon,
grammar validity, reachability, or observation.
"""

from __future__ import annotations

from typing import Any, Callable


RESULT_SCHEMA = "alex.experiment.eligibility-independence-result/v0"
TINY_GRAMMAR_RESULT_SCHEMA = "alex.experiment.eligibility-tiny-grammar-result/v0"
GRAMMAR_RELABEL_RESULT_SCHEMA = "alex.experiment.grammar-id-relabel-result/v0"


Witness = tuple[str, Callable[[dict[str, Any]], bool]]

REQUIRED_WITNESSES: tuple[Witness, ...] = (
    (
        "eligible_without_authority_or_execution",
        lambda row: row.get("grammar_eligible") is True
        and row.get("authorized") is False
        and row.get("executed") is False,
    ),
    (
        "eligible_while_observer_unavailable",
        lambda row: row.get("grammar_eligible") is True
        and row.get("observer_available") is False,
    ),
    (
        "eligible_while_capability_unreachable",
        lambda row: row.get("grammar_eligible") is True
        and row.get("capability_reachable") is False,
    ),
    (
        "structural_edge_without_eligibility",
        lambda row: row.get("structural_edge") is True
        and row.get("grammar_eligible") is False,
    ),
)


def audit_eligibility_matrix(record: dict[str, Any]) -> dict[str, Any]:
    rows = record.get("rows", [])
    missing = [
        name
        for name, predicate in REQUIRED_WITNESSES
        if not any(predicate(row) for row in rows)
    ]
    return {
        "schema": RESULT_SCHEMA,
        "disposition": "MATRIX_WITNESSED" if not missing else "MATRIX_INCOMPLETE",
        "missing_witnesses": missing,
        "grammar_id": record.get("grammar_id"),
        "handoff_id": record.get("handoff_id"),
        "authority": "none",
    }


def audit_tiny_grammar_row(
    row: dict[str, Any], *, grammar_id: str
) -> dict[str, Any]:
    """Apply one deliberately tiny legal-state invariant to one supplied row.

    The countermodel grammar says that any grammar-eligible state must also have
    both observer availability and capability reachability. A row that violates
    that invariant is not a legal state and therefore cannot be reachable under
    this tiny grammar. Passing the invariant establishes admissibility only; it
    does not prove path reachability or execution.
    """

    rejected = row.get("grammar_eligible") is True and (
        row.get("observer_available") is not True
        or row.get("capability_reachable") is not True
    )
    return {
        "schema": TINY_GRAMMAR_RESULT_SCHEMA,
        "disposition": "GRAMMAR_REJECTED" if rejected else "GRAMMAR_ADMISSIBLE",
        "reason": (
            "eligible_requires_observer_and_capability" if rejected else None
        ),
        "grammar_id": grammar_id,
        "row_id": row.get("row_id"),
        "reachable_under_tiny_grammar": False if rejected else None,
        "authority": "none",
    }


def audit_grammar_id_relabeling(
    row: dict[str, Any], *, first_grammar_id: str, second_grammar_id: str
) -> dict[str, Any]:
    """Measure whether changing only ``grammar_id`` changes evaluated semantics.

    ``GRAMMAR_ID_UNBOUND`` is a measurement about this fixed experimental
    function: the two labels differ while the semantic observation is identical.
    It does not establish what either named grammar actually means.
    """

    first = audit_tiny_grammar_row(row, grammar_id=first_grammar_id)
    second = audit_tiny_grammar_row(row, grammar_id=second_grammar_id)
    semantic_fields = (
        "schema",
        "disposition",
        "reason",
        "row_id",
        "reachable_under_tiny_grammar",
        "authority",
    )
    semantic_observation_equal = all(
        first.get(field) == second.get(field) for field in semantic_fields
    )
    labels_differ = first_grammar_id != second_grammar_id
    return {
        "schema": GRAMMAR_RELABEL_RESULT_SCHEMA,
        "disposition": (
            "GRAMMAR_ID_UNBOUND"
            if labels_differ and semantic_observation_equal
            else "RELABELING_NOT_DISCRIMINATING"
        ),
        "semantic_observation_equal": semantic_observation_equal,
        "grammar_ids": [first_grammar_id, second_grammar_id],
        "row_id": row.get("row_id"),
        "authority": "none",
    }
