from __future__ import annotations

import copy
from typing import Any

from .chronobody import (
    BodyMode,
    ChronobodyEntry,
    ExecutionResult,
    execute_body,
    resolve_body,
)
from .digests import sha256_json


_REQUEST_SCHEMA = "alex.research-formation-run/v0"
_RESULT_SCHEMA = "alex.research-formation-result/v0"
_BRIDGE_SCHEMA = "alex.research-formation-bridge/v0"


class ResearchFormationRequestError(ValueError):
    pass


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value)


def _route_payload(resolution) -> dict[str, object]:
    return {
        "disposition": resolution.disposition,
        "reason_code": resolution.reason_code,
        "body_time_id": resolution.entry.body_time_id if resolution.entry is not None else None,
        "candidate_body_time_ids": list(resolution.candidate_body_time_ids),
    }


def _execution_payload(execution: ExecutionResult) -> dict[str, object]:
    return {
        "execution_state": execution.execution_state,
        "reason_code": execution.reason_code,
        "receipt": execution.receipt,
        "output": execution.output,
        "stderr": execution.stderr,
    }


def _stage_payload(route: dict[str, object], execution: ExecutionResult | None) -> dict[str, object]:
    return {
        "route": route,
        "execution": _execution_payload(execution) if execution is not None else None,
        "result": execution.output if execution is not None else None,
    }


def _base_result(run_id: str, mode: BodyMode) -> dict[str, object]:
    return {
        "schema": _RESULT_SCHEMA,
        "run_id": run_id,
        "body_mode": mode.value,
        "execution_state": "REFUSED",
        "reason_code": None,
        "far_side": None,
        "bridge": None,
        "binocular": None,
        "authority": "none",
    }


def _validate_stage(value: Any, name: str) -> tuple[str, dict[str, object]]:
    if not isinstance(value, dict):
        raise ResearchFormationRequestError(f"{name} must be an object")
    body_time_id = value.get("body_time_id")
    case = value.get("case")
    if not _nonempty_string(body_time_id):
        raise ResearchFormationRequestError(f"{name}.body_time_id must be a non-empty string")
    if not isinstance(case, dict):
        raise ResearchFormationRequestError(f"{name}.case must be a JSON object")
    return body_time_id, copy.deepcopy(case)


def _validate_request(request: object) -> tuple[
    str,
    BodyMode,
    dict[str, str],
    str,
    dict[str, object],
    str,
    dict[str, object],
]:
    if not isinstance(request, dict):
        raise ResearchFormationRequestError("request must be a JSON object")
    if request.get("schema") != _REQUEST_SCHEMA:
        raise ResearchFormationRequestError(f"schema must be {_REQUEST_SCHEMA}")

    run_id = request.get("run_id")
    if not _nonempty_string(run_id):
        raise ResearchFormationRequestError("run_id must be a non-empty string")

    try:
        mode = BodyMode(request.get("body_mode"))
    except (TypeError, ValueError) as exc:
        raise ResearchFormationRequestError("body_mode is unknown") from exc

    materializations = request.get("materializations")
    if not isinstance(materializations, dict) or not all(
        _nonempty_string(key) and _nonempty_string(value)
        for key, value in materializations.items()
    ):
        raise ResearchFormationRequestError(
            "materializations must map body_time_id strings to local path strings"
        )

    far_body_id, far_case = _validate_stage(request.get("far_side"), "far_side")
    binocular_body_id, binocular_case = _validate_stage(request.get("binocular"), "binocular")

    return (
        run_id,
        mode,
        dict(materializations),
        far_body_id,
        far_case,
        binocular_body_id,
        binocular_case,
    )


def _run_exact_stage(
    entries: tuple[ChronobodyEntry, ...] | list[ChronobodyEntry],
    *,
    capability: str,
    body_time_id: str,
    materializations: dict[str, str],
    payload: dict[str, object],
    mode: BodyMode,
) -> tuple[dict[str, object], ExecutionResult | None]:
    resolution = resolve_body(
        entries,
        capability,
        mode,
        body_time_id=body_time_id,
    )
    route = _route_payload(resolution)
    if resolution.disposition != "ROUTED" or resolution.entry is None:
        return route, None

    materialization = materializations.get(resolution.entry.body_time_id)
    if materialization is None:
        route = dict(route)
        route["disposition"] = "REFUSED"
        route["reason_code"] = "MATERIALIZATION_REQUIRED"
        return route, None

    execution = execute_body(
        resolution.entry,
        materialization,
        payload,
        mode,
    )
    return route, execution


def _stop_from_stage(
    result: dict[str, object],
    stage_name: str,
    route: dict[str, object],
    execution: ExecutionResult | None,
) -> dict[str, object]:
    result[stage_name] = _stage_payload(route, execution)
    if execution is None:
        result["execution_state"] = route["disposition"]
        result["reason_code"] = route["reason_code"]
    else:
        result["execution_state"] = execution.execution_state
        result["reason_code"] = execution.reason_code
    return result


def evaluate_research_formation_run(
    request: object,
    entries: tuple[ChronobodyEntry, ...] | list[ChronobodyEntry],
) -> dict[str, object]:
    (
        run_id,
        mode,
        materializations,
        far_body_id,
        far_case,
        binocular_body_id,
        binocular_case,
    ) = _validate_request(request)

    result = _base_result(run_id, mode)

    far_route, far_execution = _run_exact_stage(
        entries,
        capability="far_side_pressure",
        body_time_id=far_body_id,
        materializations=materializations,
        payload=far_case,
        mode=mode,
    )
    result["far_side"] = _stage_payload(far_route, far_execution)
    if far_execution is None or far_execution.execution_state != "COMPLETED":
        return _stop_from_stage(result, "far_side", far_route, far_execution)

    far_receipt_ref = sha256_json(far_execution.receipt)
    bridge = {
        "schema": _BRIDGE_SCHEMA,
        "kind": "DISCOVERY_TRIGGER_ONLY",
        "from_stage": "far_side",
        "to_stage": "binocular",
        "receipt_ref": far_receipt_ref,
        "authority": "none",
    }
    result["bridge"] = bridge

    discovery_refs = binocular_case.get("discovery_trigger_refs")
    if not isinstance(discovery_refs, list) or not all(
        _nonempty_string(item) for item in discovery_refs
    ):
        result["execution_state"] = "REFUSED"
        result["reason_code"] = "BINOCULAR_DISCOVERY_REFS_INVALID"
        return result
    if far_receipt_ref not in discovery_refs:
        discovery_refs.append(far_receipt_ref)

    binocular_route, binocular_execution = _run_exact_stage(
        entries,
        capability="binocular_formation_audit",
        body_time_id=binocular_body_id,
        materializations=materializations,
        payload=binocular_case,
        mode=mode,
    )
    result["binocular"] = _stage_payload(binocular_route, binocular_execution)
    if binocular_execution is None or binocular_execution.execution_state != "COMPLETED":
        return _stop_from_stage(
            result,
            "binocular",
            binocular_route,
            binocular_execution,
        )

    result["execution_state"] = "COMPLETED"
    result["reason_code"] = None
    return result
