from __future__ import annotations

from typing import Any

_TERMINALS = {"FIXED", "CYCLE", "RESIDUAL", "DIVERGENT"}
_TENSION_TYPES = {
    "MISSING_CONSEQUENCE",
    "SURPLUS_GENERATOR",
    "UNEXPLAINED_RESIDUAL",
    "BRANCH_DEPENDENCE",
    "CONTRADICTION",
    "TRAJECTORY_DEPENDENCE",
    "STABLE_MATCH",
}


def _result(
    case_id: str,
    disposition: str,
    reason_code: str | None,
    authority_digest: str,
    terminal: str | None,
    validated_passes: int,
    tension_types: set[str] | None = None,
    receipt_survivors: set[str] | None = None,
) -> dict[str, object]:
    return {
        "schema": "alex.binocular-recursion-result/v0",
        "case_id": case_id,
        "disposition": disposition,
        "reason_code": reason_code,
        "terminal": terminal,
        "validated_passes": validated_passes,
        "tension_types": sorted(tension_types or set()),
        "receipt_survivors": sorted(receipt_survivors or set()),
        "authority_digest": authority_digest,
    }


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value)


def evaluate_binocular_recursion_case(case: dict) -> dict[str, object]:
    if not isinstance(case, dict):
        return _result("unknown-case", "INSUFFICIENT_TO_TEST", "MALFORMED_CASE", "", None, 0)

    case_id = case.get("case_id") if _nonempty_string(case.get("case_id")) else "unknown-case"
    authority = case.get("authority_digest") if _nonempty_string(case.get("authority_digest")) else ""

    if case.get("schema") != "alex.binocular-recursion-case/v0":
        return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_CASE", authority, None, 0)
    if not _nonempty_string(case.get("case_id")):
        return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_CASE", authority, None, 0)
    if not _nonempty_string(case.get("initial_field_digest")) or not _nonempty_string(case.get("authority_digest")):
        return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_CASE", authority, None, 0)

    terminal = case.get("terminal")
    if terminal not in _TERMINALS:
        return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_CASE", authority, None, 0)

    pass_limit = case.get("pass_limit")
    if not isinstance(pass_limit, int) or isinstance(pass_limit, bool) or pass_limit < 1:
        return _result(case_id, "INSUFFICIENT_TO_TEST", "INVALID_PASS_LIMIT", authority, terminal, 0)

    passes = case.get("passes")
    if not isinstance(passes, list) or not passes or len(passes) > pass_limit:
        return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_CASE", authority, terminal, 0)

    tension_types: set[str] = set()
    receipt_survivors: set[str] = set()
    previous_post: str | None = None

    for index, pass_ in enumerate(passes):
        if not isinstance(pass_, dict) or pass_.get("pass_index") != index:
            return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_PASS", authority, terminal, index, tension_types, receipt_survivors)

        pre = pass_.get("pre_field_digest")
        post = pass_.get("post_field_digest")
        if not _nonempty_string(pre) or not _nonempty_string(post):
            return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_PASS", authority, terminal, index, tension_types, receipt_survivors)
        if index == 0 and pre != case["initial_field_digest"]:
            return _result(case_id, "REFUSE", "BROKEN_PASS_ANCESTRY", authority, terminal, index, tension_types, receipt_survivors)
        if index > 0 and pre != previous_post:
            return _result(case_id, "REFUSE", "BROKEN_PASS_ANCESTRY", authority, terminal, index, tension_types, receipt_survivors)

        compression = pass_.get("compression")
        expansion = pass_.get("expansion")
        if not isinstance(compression, dict) or not isinstance(expansion, dict):
            return _result(case_id, "INSUFFICIENT_TO_TEST", "ONE_EYE_COLLAPSE", authority, terminal, index, tension_types, receipt_survivors)

        tensions = pass_.get("tensions")
        if not isinstance(tensions, list):
            return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_PASS", authority, terminal, index, tension_types, receipt_survivors)
        for tension in tensions:
            if not isinstance(tension, dict):
                return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_PASS", authority, terminal, index, tension_types, receipt_survivors)
            tension_type = tension.get("type")
            if tension_type not in _TENSION_TYPES:
                return _result(case_id, "INSUFFICIENT_TO_TEST", "UNKNOWN_TENSION_TYPE", authority, terminal, index, tension_types, receipt_survivors)
            tension_types.add(tension_type)
            refs = tension.get("receipt_refs", [])
            if isinstance(refs, list):
                receipt_survivors.update(ref for ref in refs if _nonempty_string(ref))

        previous_post = post

    return _result(case_id, "ACCEPT", None, authority, terminal, len(passes), tension_types, receipt_survivors)
