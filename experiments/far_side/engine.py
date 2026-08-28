from __future__ import annotations

from typing import Any

from alex_runtime.digests import sha256_json
from experiments.far_side.model import (
    DIMENSIONAL_NOVELTY_TYPES,
    REQUIRED_PRESSURES,
    normalize_statement,
    validate_far_side_case,
)


def _baseline_digest(case: dict[str, Any]) -> str:
    return sha256_json(case["baseline"])


def _receipt_survivors(case: dict[str, Any]) -> list[str]:
    refs = [item["receipt_ref"] for item in case["traversals"]]
    refs.extend(item["receipt_ref"] for item in case["candidate"]["novelty"])
    refs.extend(item["receipt_ref"] for item in case["pressure"])
    return sorted(set(refs))


def _surviving_invariants(case: dict[str, Any]) -> list[str]:
    invariant_sets = [set(item["invariants"]) for item in case["traversals"]]
    if not invariant_sets:
        return []
    return sorted(set.intersection(*invariant_sets))


def _result(
    case_id: str,
    final_status: str,
    reason_code: str | None,
    baseline_digest: str | None,
    traversal_axes: list[str],
    surviving_invariants: list[str],
    regenerated_targets: list[str],
    missing_targets: list[str],
    novelty_delta: list[dict[str, str]],
    pressure_failures: list[str],
    receipt_survivors: list[str],
) -> dict[str, object]:
    return {
        "case_id": case_id,
        "final_status": final_status,
        "reason_code": reason_code,
        "baseline_digest": baseline_digest,
        "traversal_axes": traversal_axes,
        "surviving_invariants": surviving_invariants,
        "regenerated_targets": regenerated_targets,
        "missing_targets": missing_targets,
        "novelty_delta": novelty_delta,
        "pressure_failures": pressure_failures,
        "receipt_survivors": receipt_survivors,
    }


def evaluate_far_side_case(case: object) -> dict[str, object]:
    case_id = case.get("case_id", "unknown-case") if isinstance(case, dict) else "unknown-case"
    if not isinstance(case_id, str) or not case_id:
        case_id = "unknown-case"

    valid, reason = validate_far_side_case(case)
    if not valid:
        return _result(case_id, reason or "INSUFFICIENT_RECEIPT", reason, None, [], [], [], [], [], [], [])

    assert isinstance(case, dict)
    baseline_digest = _baseline_digest(case)
    axes = sorted({item["axis"] for item in case["traversals"]})
    survivors = _surviving_invariants(case)
    receipts = _receipt_survivors(case)

    if len(axes) < 3:
        return _result(
            case_id,
            "INSUFFICIENT_RECEIPT",
            "INSUFFICIENT_TRAVERSAL_DIVERSITY",
            baseline_digest,
            axes,
            survivors,
            [],
            [],
            [],
            [],
            receipts,
        )

    required = sorted(set(case["candidate"]["required_targets"]))
    regenerated = sorted(set(case["candidate"]["regenerated_targets"]))
    regenerated_required = sorted(set(required) & set(regenerated))
    missing = sorted(set(required) - set(regenerated))

    if required and not regenerated_required:
        return _result(
            case_id,
            "COMPRESSION_FAILED_REGENERATION",
            "NO_REQUIRED_TARGET_REGENERATED",
            baseline_digest,
            axes,
            survivors,
            regenerated,
            missing,
            [],
            [],
            receipts,
        )

    if missing:
        return _result(
            case_id,
            "PARTIAL_SURVIVOR",
            "PARTIAL_REGENERATION",
            baseline_digest,
            axes,
            survivors,
            regenerated,
            missing,
            [],
            [],
            receipts,
        )

    # Novelty and pressure gates are added in Task 3.
    return _result(
        case_id,
        "NO_NEW_DIMENSION_EARNED",
        None,
        baseline_digest,
        axes,
        survivors,
        regenerated,
        [],
        [],
        [],
        receipts,
    )
