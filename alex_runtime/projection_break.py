from __future__ import annotations

from typing import Any

from alex_runtime.projection_invariance import evaluate_projection_invariance_case


_REQUIRED_SIDE_FIELDS = (
    "world_digest",
    "observer_constraints_digest",
    "visible_input_digest",
    "bounded_context_digest",
    "projection_digest",
    "derivation_digest",
    "serialization_digest",
    "narrative_digest",
    "authority_digest",
)

_BREAK_CHECKS = (
    ("bounded_context_digest", "LOADOUT"),
    ("projection_digest", "PROJECTION"),
    ("derivation_digest", "DERIVATION"),
    ("serialization_digest", "SERIALIZATION"),
    ("narrative_digest", "NARRATIVE"),
)


def _case_id(case: Any) -> str:
    if isinstance(case, dict):
        value = case.get("case_id")
        if isinstance(value, str) and value:
            return value
    return "unknown-case"


def _receipt_refs(side: Any) -> list[str]:
    if not isinstance(side, dict):
        return []
    refs = side.get("receipt_refs")
    if not isinstance(refs, list):
        return []
    return [ref for ref in refs if isinstance(ref, str) and ref]


def _valid_side(side: Any) -> bool:
    if not isinstance(side, dict):
        return False
    for field in _REQUIRED_SIDE_FIELDS:
        value = side.get(field)
        if not isinstance(value, str) or not value:
            return False
    refs = side.get("receipt_refs")
    if not isinstance(refs, list):
        return False
    if any(not isinstance(ref, str) or not ref for ref in refs):
        return False
    return len(refs) == len(set(refs))


def _survivors(*sides: Any, extra: list[str] | None = None) -> list[str]:
    refs: set[str] = set()
    for side in sides:
        refs.update(_receipt_refs(side))
    if extra:
        refs.update(ref for ref in extra if isinstance(ref, str) and ref)
    return sorted(refs)


def _result(
    case_id: str,
    disposition: str,
    reason_code: str | None,
    *,
    pre_disposition: str | None = None,
    pre_reason_code: str | None = None,
    break_boundary: str | None = None,
    receipt_survivors: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "case_id": case_id,
        "disposition": disposition,
        "reason_code": reason_code,
        "pre_disposition": pre_disposition,
        "pre_reason_code": pre_reason_code,
        "break_boundary": break_boundary,
        "receipt_survivors": receipt_survivors or [],
    }


def evaluate_projection_break_case(case: dict) -> dict[str, Any]:
    """Test whether one shared intervention lawfully exposes a future difference.

    The evaluator first requires two materially different worlds to be observer-
    equivalent under the existing projection-invariance contract. It then checks
    that the same attributable intervention reaches both worlds under equivalent
    observer constraints and visible input. A later difference may be accepted
    as the first observed break, but authority may not change as part of it.

    This function does not prove the hidden structural difference is sufficient
    or dominant. It proves only that the supplied break remains attributable to
    the declared intervention plus preserved hidden-difference receipts.
    """

    case_id = _case_id(case)
    if not isinstance(case, dict):
        return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_CASE")

    pre = case.get("pre")
    post = case.get("post")
    intervention = case.get("intervention")
    hidden = case.get("hidden_difference")

    if not isinstance(pre, dict) or not isinstance(post, dict):
        return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_CASE")

    pre_left = pre.get("left")
    pre_right = pre.get("right")
    post_left = post.get("left")
    post_right = post.get("right")

    if not all(_valid_side(side) for side in (pre_left, pre_right, post_left, post_right)):
        return _result(case_id, "INSUFFICIENT_TO_TEST", "MALFORMED_PROJECTION_WITNESS")

    pre_result = evaluate_projection_invariance_case(
        {
            "case_id": f"{case_id}:pre",
            "left": pre_left,
            "right": pre_right,
        }
    )
    pre_disposition = pre_result["disposition"]
    pre_reason_code = pre_result["reason_code"]

    if pre_disposition != "ACCEPT":
        disposition = "REFUSE" if pre_disposition == "REFUSE" else "INSUFFICIENT_TO_TEST"
        return _result(
            case_id,
            disposition,
            "PRECONDITION_NOT_INVARIANT",
            pre_disposition=pre_disposition,
            pre_reason_code=pre_reason_code,
            receipt_survivors=_survivors(pre_left, pre_right),
        )

    if not isinstance(intervention, dict):
        return _result(
            case_id,
            "INSUFFICIENT_TO_TEST",
            "INVALID_INTERVENTION",
            pre_disposition=pre_disposition,
            pre_reason_code=pre_reason_code,
            receipt_survivors=_survivors(pre_left, pre_right),
        )

    intervention_ref = intervention.get("receipt_ref")
    policy_digest = intervention.get("policy_digest")
    if not isinstance(intervention_ref, str) or not intervention_ref or not isinstance(policy_digest, str) or not policy_digest:
        return _result(
            case_id,
            "INSUFFICIENT_TO_TEST",
            "INVALID_INTERVENTION",
            pre_disposition=pre_disposition,
            pre_reason_code=pre_reason_code,
            receipt_survivors=_survivors(pre_left, pre_right),
        )

    survivors = _survivors(pre_left, pre_right, post_left, post_right, extra=[intervention_ref])

    if intervention_ref not in _receipt_refs(post_left) or intervention_ref not in _receipt_refs(post_right):
        return _result(
            case_id,
            "INSUFFICIENT_TO_TEST",
            "INTERVENTION_NOT_ATTRIBUTABLE",
            pre_disposition=pre_disposition,
            pre_reason_code=pre_reason_code,
            receipt_survivors=survivors,
        )

    if post_left["observer_constraints_digest"] != post_right["observer_constraints_digest"]:
        return _result(
            case_id,
            "INSUFFICIENT_TO_TEST",
            "POST_OBSERVER_CONSTRAINTS_NOT_EQUIVALENT",
            pre_disposition=pre_disposition,
            pre_reason_code=pre_reason_code,
            receipt_survivors=survivors,
        )

    if post_left["visible_input_digest"] != post_right["visible_input_digest"]:
        return _result(
            case_id,
            "INSUFFICIENT_TO_TEST",
            "POST_INPUT_NOT_EQUIVALENT",
            pre_disposition=pre_disposition,
            pre_reason_code=pre_reason_code,
            receipt_survivors=survivors,
        )

    if post_left["world_digest"] == post_right["world_digest"]:
        return _result(
            case_id,
            "INSUFFICIENT_TO_TEST",
            "POST_WORLDS_NOT_MATERIALLY_DISTINCT",
            pre_disposition=pre_disposition,
            pre_reason_code=pre_reason_code,
            receipt_survivors=survivors,
        )

    if not isinstance(hidden, dict):
        return _result(
            case_id,
            "INSUFFICIENT_TO_TEST",
            "HIDDEN_DIFFERENCE_NOT_ATTRIBUTABLE",
            pre_disposition=pre_disposition,
            pre_reason_code=pre_reason_code,
            receipt_survivors=survivors,
        )

    hidden_left = hidden.get("left_receipt_ref")
    hidden_right = hidden.get("right_receipt_ref")
    hidden_valid = (
        isinstance(hidden_left, str)
        and bool(hidden_left)
        and isinstance(hidden_right, str)
        and bool(hidden_right)
        and hidden_left != hidden_right
        and hidden_left in _receipt_refs(pre_left)
        and hidden_left in _receipt_refs(post_left)
        and hidden_right in _receipt_refs(pre_right)
        and hidden_right in _receipt_refs(post_right)
    )
    if not hidden_valid:
        return _result(
            case_id,
            "INSUFFICIENT_TO_TEST",
            "HIDDEN_DIFFERENCE_NOT_ATTRIBUTABLE",
            pre_disposition=pre_disposition,
            pre_reason_code=pre_reason_code,
            receipt_survivors=survivors,
        )

    pre_authority = pre_left["authority_digest"]
    if (
        pre_right["authority_digest"] != pre_authority
        or post_left["authority_digest"] != pre_authority
        or post_right["authority_digest"] != pre_authority
    ):
        return _result(
            case_id,
            "REFUSE",
            "AUTHORITY_CHANGED",
            pre_disposition=pre_disposition,
            pre_reason_code=pre_reason_code,
            break_boundary="AUTHORITY",
            receipt_survivors=survivors,
        )

    for field, boundary in _BREAK_CHECKS:
        if post_left[field] != post_right[field]:
            return _result(
                case_id,
                "ACCEPT",
                None,
                pre_disposition=pre_disposition,
                pre_reason_code=pre_reason_code,
                break_boundary=boundary,
                receipt_survivors=survivors,
            )

    return _result(
        case_id,
        "INSUFFICIENT_TO_TEST",
        "NO_BREAK_OBSERVED",
        pre_disposition=pre_disposition,
        pre_reason_code=pre_reason_code,
        receipt_survivors=survivors,
    )
