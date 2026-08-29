from __future__ import annotations

import hashlib
import json
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
_BRANCH_STATUSES = {"ENTAILED", "INFERRED", "SPECULATIVE", "CONTRADICTED", "UNRESOLVED"}
_UPDATE_KINDS = {
    "NONE",
    "EVIDENCE_ADDED",
    "PREMISE_ADMITTED",
    "PREMISE_WITHDRAWN",
    "READING_CORRECTED",
    "RULE_PROFILE_CHANGED",
    "CONTRADICTION_RESOLVED",
    "OWNER_DECISION",
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


def _string_list(value: Any) -> bool:
    return isinstance(value, list) and all(_nonempty_string(item) for item in value)


def _live_consequence_refs(expansion: dict[str, Any]) -> set[str]:
    live_statuses = {"ENTAILED", "INFERRED", "UNRESOLVED"}
    return {
        branch["consequence_ref"]
        for branch in expansion["branches"]
        if branch["status"] in live_statuses
    }


def _sha256_json(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def _tension_signature(tension: dict[str, Any]) -> dict[str, object]:
    return {
        "type": tension["type"],
        "left_refs": sorted(tension["left_refs"]),
        "right_refs": sorted(tension["right_refs"]),
    }


def _binocular_state_digest(pass_: dict[str, Any]) -> str:
    payload = {
        "compression_profile_digest": pass_["compression"]["profile_digest"],
        "compression_proposal_digest": pass_["compression"]["proposal_digest"],
        "expansion_profile_digest": pass_["expansion"]["profile_digest"],
        "live_consequence_refs": sorted(_live_consequence_refs(pass_["expansion"])),
        "tensions": [_tension_signature(tension) for tension in pass_["tensions"]],
    }
    return _sha256_json(payload)


def _terminal_demonstrated(terminal: str, passes: list[dict[str, Any]], pass_limit: int) -> bool:
    state_digests = [_binocular_state_digest(pass_) for pass_ in passes]

    if terminal == "FIXED":
        if len(passes) < 2:
            return False
        left, right = passes[-2], passes[-1]
        same_profiles = (
            left["compression"]["profile_digest"] == right["compression"]["profile_digest"]
            and left["expansion"]["profile_digest"] == right["expansion"]["profile_digest"]
        )
        return same_profiles and state_digests[-2] == state_digests[-1]

    if terminal == "CYCLE":
        for left_index, digest in enumerate(state_digests):
            for right_index in range(left_index + 2, len(state_digests)):
                if state_digests[right_index] != digest:
                    continue
                intervening = state_digests[left_index + 1:right_index]
                if any(item != digest for item in intervening):
                    return True
        return False

    if terminal == "RESIDUAL":
        return any(tension["type"] != "STABLE_MATCH" for tension in passes[-1]["tensions"])

    if terminal == "DIVERGENT":
        if len(passes) < 2 or len(passes) != pass_limit:
            return False
        if len(set(state_digests)) != len(state_digests):
            return False
        previous = [_tension_signature(tension) for tension in passes[-2]["tensions"]]
        final = [_tension_signature(tension) for tension in passes[-1]["tensions"]]
        return final != previous

    return False


def _support_uses_discovery_trigger(compression: dict[str, Any], discovery_triggers: set[str]) -> bool:
    return bool(set(compression["claim_support_refs"]) & discovery_triggers)


def _branch_uses_only_declared_premises(branch: dict[str, Any], admitted: set[str]) -> bool:
    used = set(branch["used_premise_refs"])
    introduced = set(branch["introduced_premise_refs"])
    return used <= (admitted | introduced)


def _valid_compression(compression: Any) -> bool:
    if not isinstance(compression, dict):
        return False
    return (
        _nonempty_string(compression.get("profile_digest"))
        and _nonempty_string(compression.get("proposal_digest"))
        and _string_list(compression.get("formation_basis_refs"))
        and _string_list(compression.get("claim_support_refs"))
        and _string_list(compression.get("reexpanded_live_consequence_refs"))
    )


def _valid_branch_shape(branch: Any) -> bool:
    if not isinstance(branch, dict):
        return False
    return (
        _nonempty_string(branch.get("branch_id"))
        and _string_list(branch.get("parent_refs"))
        and _nonempty_string(branch.get("rule_ref"))
        and _string_list(branch.get("condition_refs"))
        and _nonempty_string(branch.get("consequence_ref"))
        and _nonempty_string(branch.get("status"))
        and _string_list(branch.get("used_premise_refs"))
        and _string_list(branch.get("introduced_premise_refs"))
    )


def _valid_expansion(expansion: Any) -> bool:
    return (
        isinstance(expansion, dict)
        and _nonempty_string(expansion.get("profile_digest"))
        and isinstance(expansion.get("branches"), list)
    )


def _valid_tension_shape(tension: Any) -> bool:
    return (
        isinstance(tension, dict)
        and _nonempty_string(tension.get("type"))
        and _string_list(tension.get("left_refs"))
        and _string_list(tension.get("right_refs"))
        and _string_list(tension.get("receipt_refs"))
    )


def _valid_update_shape(update: Any) -> bool:
    if not isinstance(update, dict):
        return False
    return (
        _nonempty_string(update.get("kind"))
        and _string_list(update.get("receipt_refs"))
        and _string_list(update.get("admit_premise_refs"))
        and _string_list(update.get("withdraw_premise_refs"))
        and _string_list(update.get("withdraw_consequence_refs"))
        and _nonempty_string(update.get("authority_digest"))
    )


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

    for field in (
        "admitted_premise_refs",
        "unresolved_premise_refs",
        "discovery_trigger_refs",
        "support_refs",
    ):
        if not _string_list(case.get(field)):
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

    discovery_triggers = set(case["discovery_trigger_refs"])
    admitted = set(case["admitted_premise_refs"])
    tension_types: set[str] = set()
    receipt_survivors: set[str] = set(case["support_refs"])
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
        if not _valid_compression(compression) or not _valid_expansion(expansion):
            return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_PASS", authority, terminal, index, tension_types, receipt_survivors)

        order_material = pass_.get("trajectory_order_material")
        trajectory = pass_.get("trajectory")
        if not isinstance(order_material, bool) or not isinstance(trajectory, list) or any(not _nonempty_string(ref) for ref in trajectory):
            return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_PASS", authority, terminal, index, tension_types, receipt_survivors)
        if order_material and len(trajectory) < 2:
            return _result(case_id, "INSUFFICIENT_TO_TEST", "TRAJECTORY_NOT_PRESERVED", authority, terminal, index, tension_types, receipt_survivors)

        branches = expansion["branches"]
        for branch in branches:
            if not _valid_branch_shape(branch):
                return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_PASS", authority, terminal, index, tension_types, receipt_survivors)
            if branch["status"] not in _BRANCH_STATUSES:
                return _result(case_id, "INSUFFICIENT_TO_TEST", "UNKNOWN_BRANCH_STATUS", authority, terminal, index, tension_types, receipt_survivors)

        tensions = pass_.get("tensions")
        if not isinstance(tensions, list):
            return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_PASS", authority, terminal, index, tension_types, receipt_survivors)
        for tension in tensions:
            if not _valid_tension_shape(tension):
                return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_PASS", authority, terminal, index, tension_types, receipt_survivors)
            tension_type = tension["type"]
            if tension_type not in _TENSION_TYPES:
                return _result(case_id, "INSUFFICIENT_TO_TEST", "UNKNOWN_TENSION_TYPE", authority, terminal, index, tension_types, receipt_survivors)
            tension_types.add(tension_type)
            receipt_survivors.update(tension["receipt_refs"])

        update = pass_.get("update")
        if not _valid_update_shape(update):
            return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_PASS", authority, terminal, index, tension_types, receipt_survivors)
        if update["kind"] not in _UPDATE_KINDS:
            return _result(case_id, "INSUFFICIENT_TO_TEST", "UNKNOWN_UPDATE_KIND", authority, terminal, index, tension_types, receipt_survivors)

        if _support_uses_discovery_trigger(compression, discovery_triggers):
            return _result(case_id, "REFUSE", "DISCOVERY_TRIGGER_AS_SUPPORT", authority, terminal, index, tension_types, receipt_survivors)

        for branch in branches:
            if not _branch_uses_only_declared_premises(branch, admitted):
                return _result(case_id, "REFUSE", "UNDECLARED_PREMISE_INJECTION", authority, terminal, index, tension_types, receipt_survivors)

        required_live = _live_consequence_refs(expansion) - set(update["withdraw_consequence_refs"])
        regenerated = set(compression["reexpanded_live_consequence_refs"])
        if required_live - regenerated:
            return _result(case_id, "REFUSE", "COMPRESSION_ERASED_LIVE_CONSEQUENCE", authority, terminal, index, tension_types, receipt_survivors)

        if update["authority_digest"] != authority:
            return _result(case_id, "REFUSE", "AUTHORITY_CHANGED", authority, terminal, index, tension_types, receipt_survivors)

        field_changed = pre != post
        attributed = update["kind"] != "NONE" and bool(update["receipt_refs"])
        if field_changed and not attributed:
            return _result(case_id, "REFUSE", "UNATTRIBUTED_UPDATE", authority, terminal, index, tension_types, receipt_survivors)

        receipt_survivors.update(update["receipt_refs"])
        admitted.difference_update(update["withdraw_premise_refs"])
        admitted.update(update["admit_premise_refs"])
        previous_post = post

    if not _terminal_demonstrated(terminal, passes, pass_limit):
        return _result(
            case_id,
            "INSUFFICIENT_TO_TEST",
            "TERMINAL_NOT_DEMONSTRATED",
            authority,
            terminal,
            len(passes),
            tension_types,
            receipt_survivors,
        )

    return _result(case_id, "ACCEPT", None, authority, terminal, len(passes), tension_types, receipt_survivors)
