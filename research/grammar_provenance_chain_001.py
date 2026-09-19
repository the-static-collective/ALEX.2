from __future__ import annotations

from typing import Any

GRAMMAR_SCHEMA = "alex.hinge-grammar/v0"
READING_SCHEMA = "alex.grammar-reading/v0"


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _refuse(reason: str) -> dict[str, Any]:
    return {
        "schema": READING_SCHEMA,
        "disposition": "REFUSE",
        "reason": reason,
        "authority": "none",
        "meaning_verdict": "none",
    }


def _rules(grammar: object) -> dict[str, str] | None:
    if not isinstance(grammar, dict) or grammar.get("schema") != GRAMMAR_SCHEMA:
        return None
    if any(not _nonempty(grammar.get(k)) for k in ("grammar_ref", "carrier", "source_ref", "available_from")):
        return None
    rules = grammar.get("rules")
    if not isinstance(rules, list):
        return None
    out: dict[str, str] = {}
    for rule in rules:
        if not isinstance(rule, dict):
            return None
        selector, relation = rule.get("selector"), rule.get("relation")
        if not _nonempty(selector) or not _nonempty(relation) or selector in out:
            return None
        out[selector] = relation
    return out


def witness_reading_at_cut(
    grammar: object,
    selector: str,
    subject_cut: str,
    applied_at: str,
) -> dict[str, Any]:
    """Receipt a reading while keeping grammar availability distinct from subject time.

    ISO-like timestamps are compared lexicographically by this bounded fixture; callers must
    use one normalized representation. A later grammar may reread an older carrier, but that
    result is retrospective and may not impersonate the historical reading available then.
    """
    rules = _rules(grammar)
    if rules is None:
        return _refuse("invalid_grammar_snapshot")
    if any(not _nonempty(v) for v in (selector, subject_cut, applied_at)):
        return _refuse("invalid_cut")
    assert isinstance(grammar, dict)
    if applied_at < grammar["available_from"]:
        return _refuse("grammar_not_yet_available")
    if applied_at < subject_cut:
        return _refuse("application_precedes_subject")

    relation = rules.get(selector)
    retrospective = grammar["available_from"] > subject_cut
    return {
        "schema": READING_SCHEMA,
        "disposition": "ACCEPT",
        "reason": None,
        "source_ref": grammar["source_ref"],
        "carrier": grammar["carrier"],
        "selector": selector,
        "relation": relation,
        "grammar_ref": grammar["grammar_ref"],
        "grammar_available_from": grammar["available_from"],
        "subject_cut": subject_cut,
        "applied_at": applied_at,
        "binding_mode": "retrospective_rereading" if retrospective else "historical_reading",
        "available_at_subject_cut": not retrospective,
        "authority": "none",
        "meaning_verdict": "none",
    }
