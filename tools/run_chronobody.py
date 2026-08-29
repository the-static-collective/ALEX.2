from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from alex_runtime.chronobody import (  # noqa: E402
    BodyMode,
    ChronobodyEntry,
    execute_body,
    parse_registry,
    resolve_body,
)
from alex_runtime.digests import canonical_json_bytes  # noqa: E402


REGISTRY_PATH = ROOT / "chronobody" / "registry.v0.json"
_REQUEST_SCHEMA = "alex.chronobody-run-request/v0"
_RESULT_SCHEMA = "alex.chronobody-run-result/v0"


class RequestError(ValueError):
    pass


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value)


def _load_registry() -> tuple[ChronobodyEntry, ...]:
    value = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    return parse_registry(value)


def _route_payload(resolution) -> dict[str, object]:
    return {
        "disposition": resolution.disposition,
        "reason_code": resolution.reason_code,
        "body_time_id": resolution.entry.body_time_id if resolution.entry is not None else None,
        "candidate_body_time_ids": list(resolution.candidate_body_time_ids),
    }


def _execution_payload(execution) -> dict[str, object]:
    return {
        "execution_state": execution.execution_state,
        "reason_code": execution.reason_code,
        "receipt": execution.receipt,
        "output": execution.output,
        "stderr": execution.stderr,
    }


def _base_result(route: dict[str, object]) -> dict[str, object]:
    return {
        "schema": _RESULT_SCHEMA,
        "disposition": route["disposition"],
        "reason_code": route["reason_code"],
        "route": route,
        "execution": None,
        "authority": "none",
    }


def _validate_request(request: object) -> tuple[
    str,
    BodyMode | None,
    str | None,
    str | None,
    dict[str, str],
    dict[str, object],
]:
    if not isinstance(request, dict):
        raise RequestError("request must be a JSON object")
    if request.get("schema") != _REQUEST_SCHEMA:
        raise RequestError(f"schema must be {_REQUEST_SCHEMA}")

    capability = request.get("capability")
    if not _nonempty_string(capability):
        raise RequestError("capability must be a non-empty string")

    raw_mode = request.get("mode")
    mode: BodyMode | None
    try:
        mode = BodyMode(raw_mode)
    except (TypeError, ValueError):
        mode = None

    organ_id = request.get("organ_id")
    if organ_id is not None and not _nonempty_string(organ_id):
        raise RequestError("organ_id must be a non-empty string when present")

    body_time_id = request.get("body_time_id")
    if body_time_id is not None and not _nonempty_string(body_time_id):
        raise RequestError("body_time_id must be a non-empty string when present")

    materializations = request.get("materializations", {})
    if not isinstance(materializations, dict) or not all(
        _nonempty_string(key) and _nonempty_string(value)
        for key, value in materializations.items()
    ):
        raise RequestError("materializations must map body_time_id strings to local path strings")

    payload = request.get("payload")
    if not isinstance(payload, dict):
        raise RequestError("payload must be a JSON object")

    return capability, mode, organ_id, body_time_id, dict(materializations), payload


def evaluate_request(
    request: object,
    entries: tuple[ChronobodyEntry, ...] | list[ChronobodyEntry],
) -> dict[str, object]:
    capability, mode, organ_id, body_time_id, materializations, payload = _validate_request(request)

    if mode is None:
        route = {
            "disposition": "REFUSED",
            "reason_code": "UNKNOWN_BODY_MODE",
            "body_time_id": None,
            "candidate_body_time_ids": [],
        }
        return _base_result(route)

    resolution = resolve_body(
        entries,
        capability,
        mode,
        organ_id=organ_id,
        body_time_id=body_time_id,
    )
    route = _route_payload(resolution)
    result = _base_result(route)

    if resolution.disposition != "ROUTED" or resolution.entry is None:
        return result

    materialization = materializations.get(resolution.entry.body_time_id)
    if materialization is None:
        result["disposition"] = "REFUSED"
        result["reason_code"] = "MATERIALIZATION_REQUIRED"
        return result

    execution = execute_body(
        resolution.entry,
        materialization,
        payload,
        mode,
    )
    result["execution"] = _execution_payload(execution)
    result["disposition"] = execution.execution_state
    result["reason_code"] = execution.reason_code
    return result


def _read_request(path_arg: str | None) -> object:
    if path_arg is None or path_arg == "-":
        return json.load(sys.stdin)
    return json.loads(Path(path_arg).read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) > 1:
        print("invalid request: expected zero or one input path", file=sys.stderr)
        return 2

    try:
        request = _read_request(args[0] if args else None)
        entries = _load_registry()
        result = evaluate_request(request, entries)
    except (OSError, UnicodeError, json.JSONDecodeError, RequestError, ValueError) as exc:
        print(f"invalid request: {exc}", file=sys.stderr)
        return 2

    sys.stdout.buffer.write(canonical_json_bytes(result) + b"\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
