from __future__ import annotations

import re
from dataclasses import dataclass
from enum import Enum
from pathlib import PurePosixPath
from typing import Any


_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
_ALLOWED_RUNTIME_CONTRACTS = {"python-json-stdio/v0"}


class BodyStatus(str, Enum):
    PRESENT = "PRESENT"
    INCUBATING = "INCUBATING"
    HELD = "HELD"
    RETIRED = "RETIRED"
    RECONSTITUTED = "RECONSTITUTED"


class BodyMode(str, Enum):
    PRESENT_ONLY = "PRESENT_ONLY"
    EXPERIMENTAL = "EXPERIMENTAL"
    REPLAY = "REPLAY"


class RegistryError(ValueError):
    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code
        self.message = message


@dataclass(frozen=True)
class ChronobodyEntry:
    organ_id: str
    body_time_id: str
    status: BodyStatus
    capabilities: tuple[str, ...]
    source_repo: str
    source_branch: str | None
    source_sha: str | None
    runtime_contract: str
    entrypoint: str
    verification_workflow: str | None
    verification_run_id: int | None
    verification_result: str | None
    authority: str
    parents: tuple[str, ...]


@dataclass(frozen=True)
class Resolution:
    disposition: str
    reason_code: str | None
    entry: ChronobodyEntry | None
    candidate_body_time_ids: tuple[str, ...] = ()


_ALLOWED_BY_MODE = {
    BodyMode.PRESENT_ONLY: {BodyStatus.PRESENT},
    BodyMode.EXPERIMENTAL: {
        BodyStatus.PRESENT,
        BodyStatus.INCUBATING,
        BodyStatus.RECONSTITUTED,
    },
    BodyMode.REPLAY: {BodyStatus.RETIRED},
}


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value)


def _string_list(value: Any) -> bool:
    return isinstance(value, list) and all(_nonempty_string(item) for item in value)


def _entrypoint_is_valid(value: Any) -> bool:
    if not _nonempty_string(value):
        return False
    path = PurePosixPath(value)
    if path.is_absolute():
        return False
    return ".." not in path.parts


def _parse_status(value: Any) -> BodyStatus:
    try:
        return BodyStatus(value)
    except (TypeError, ValueError) as exc:
        raise RegistryError("UNKNOWN_BODY_STATUS", "unknown body status") from exc


def _parse_entry(value: Any) -> ChronobodyEntry:
    if not isinstance(value, dict):
        raise RegistryError("MALFORMED_ENTRY", "registry organ entry must be an object")

    organ_id = value.get("organ_id")
    body_time_id = value.get("body_time_id")
    if not _nonempty_string(organ_id) or not _nonempty_string(body_time_id):
        raise RegistryError("MALFORMED_ENTRY", "organ_id and body_time_id are required")

    status = _parse_status(value.get("status"))

    capabilities = value.get("capabilities")
    if not _string_list(capabilities) or not capabilities:
        raise RegistryError("MALFORMED_CAPABILITIES", "capabilities must be a non-empty string array")
    if len(set(capabilities)) != len(capabilities):
        raise RegistryError("DUPLICATE_CAPABILITY", "capabilities must be unique within an organ body")

    source = value.get("source")
    if not isinstance(source, dict) or not _nonempty_string(source.get("repo")):
        raise RegistryError("MALFORMED_SOURCE", "source.repo is required")
    source_repo = source["repo"]
    source_branch = source.get("branch")
    if source_branch is not None and not _nonempty_string(source_branch):
        raise RegistryError("MALFORMED_SOURCE", "source.branch must be a non-empty string when present")

    source_sha = source.get("sha")
    if status is not BodyStatus.PRESENT and source_sha is None:
        raise RegistryError("BODY_SHA_REQUIRED", "non-present bodies require source.sha")
    if source_sha is not None:
        if not isinstance(source_sha, str) or not _SHA_RE.fullmatch(source_sha):
            raise RegistryError("BODY_SHA_INVALID", "source.sha must be a lowercase 40-character hexadecimal commit SHA")
        if body_time_id != f"{organ_id}@{source_sha}":
            raise RegistryError("BODY_TIME_ID_MISMATCH", "body_time_id must bind organ_id to exact source.sha")

    runtime = value.get("runtime")
    if not isinstance(runtime, dict):
        raise RegistryError("MALFORMED_RUNTIME", "runtime object is required")
    runtime_contract = runtime.get("contract")
    entrypoint = runtime.get("entrypoint")
    if runtime_contract not in _ALLOWED_RUNTIME_CONTRACTS:
        raise RegistryError("RUNTIME_CONTRACT_UNSUPPORTED", "runtime contract is not allowlisted")
    if not _entrypoint_is_valid(entrypoint):
        raise RegistryError("ENTRYPOINT_INVALID", "entrypoint must be a repository-relative traversal-free path")

    authority = value.get("authority")
    if authority != "none":
        raise RegistryError("AUTHORITY_NOT_NONE", "Chronobody v0 entries must carry authority none")

    parents = value.get("parents", [])
    if not _string_list(parents):
        raise RegistryError("MALFORMED_PARENTS", "parents must be an array of body_time_id strings")

    verification = value.get("verification")
    verification_workflow: str | None = None
    verification_run_id: int | None = None
    verification_result: str | None = None
    if verification is not None:
        if not isinstance(verification, dict):
            raise RegistryError("MALFORMED_VERIFICATION", "verification must be an object")
        verification_workflow = verification.get("workflow")
        verification_run_id = verification.get("run_id")
        verification_result = verification.get("result")
        if verification_workflow is not None and not _nonempty_string(verification_workflow):
            raise RegistryError("MALFORMED_VERIFICATION", "verification.workflow must be a non-empty string")
        if verification_run_id is not None and (
            not isinstance(verification_run_id, int)
            or isinstance(verification_run_id, bool)
            or verification_run_id < 1
        ):
            raise RegistryError("MALFORMED_VERIFICATION", "verification.run_id must be a positive integer")
        if verification_result is not None and not _nonempty_string(verification_result):
            raise RegistryError("MALFORMED_VERIFICATION", "verification.result must be a non-empty string")

    return ChronobodyEntry(
        organ_id=organ_id,
        body_time_id=body_time_id,
        status=status,
        capabilities=tuple(capabilities),
        source_repo=source_repo,
        source_branch=source_branch,
        source_sha=source_sha,
        runtime_contract=runtime_contract,
        entrypoint=entrypoint,
        verification_workflow=verification_workflow,
        verification_run_id=verification_run_id,
        verification_result=verification_result,
        authority=authority,
        parents=tuple(parents),
    )


def parse_registry(value: object) -> tuple[ChronobodyEntry, ...]:
    if not isinstance(value, dict) or value.get("schema") != "alex.chronobody-registry/v0":
        raise RegistryError("MALFORMED_REGISTRY", "registry schema must be alex.chronobody-registry/v0")

    organs = value.get("organs")
    if not isinstance(organs, list):
        raise RegistryError("MALFORMED_REGISTRY", "registry organs must be an array")

    entries = tuple(_parse_entry(item) for item in organs)
    body_ids = [entry.body_time_id for entry in entries]
    if len(set(body_ids)) != len(body_ids):
        raise RegistryError("DUPLICATE_BODY_TIME_ID", "body_time_id values must be unique")

    return entries


def resolve_body(
    entries: tuple[ChronobodyEntry, ...] | list[ChronobodyEntry],
    capability: str,
    mode: BodyMode,
    organ_id: str | None = None,
    body_time_id: str | None = None,
) -> Resolution:
    if not isinstance(mode, BodyMode):
        return Resolution("REFUSED", "UNKNOWN_BODY_MODE", None)
    if not _nonempty_string(capability):
        return Resolution("REFUSED", "CAPABILITY_REQUIRED", None)

    entries_tuple = tuple(entries)

    if body_time_id is not None:
        exact = next((entry for entry in entries_tuple if entry.body_time_id == body_time_id), None)
        if exact is None:
            return Resolution("UNAVAILABLE", "BODY_TIME_NOT_REGISTERED", None)
        if organ_id is not None and exact.organ_id != organ_id:
            return Resolution("REFUSED", "ORGAN_MISMATCH", None, (exact.body_time_id,))
        if capability not in exact.capabilities:
            return Resolution("REFUSED", "CAPABILITY_MISMATCH", None, (exact.body_time_id,))
        if exact.status is BodyStatus.HELD:
            return Resolution("REFUSED", "BODY_NOT_EXECUTABLE", None, (exact.body_time_id,))
        if exact.status not in _ALLOWED_BY_MODE[mode]:
            return Resolution("REFUSED", "BODY_MODE_MISMATCH", None, (exact.body_time_id,))
        return Resolution("ROUTED", None, exact, (exact.body_time_id,))

    if mode is BodyMode.REPLAY:
        return Resolution("REFUSED", "EXACT_BODY_TIME_REQUIRED", None)

    candidates = [entry for entry in entries_tuple if capability in entry.capabilities]
    if organ_id is not None:
        candidates = [entry for entry in candidates if entry.organ_id == organ_id]

    eligible = [entry for entry in candidates if entry.status in _ALLOWED_BY_MODE[mode]]
    eligible_ids = tuple(sorted(entry.body_time_id for entry in eligible))

    if not eligible:
        return Resolution("UNAVAILABLE", "NO_ELIGIBLE_BODY", None)
    if len(eligible) > 1:
        return Resolution("AMBIGUOUS", "MULTIPLE_ELIGIBLE_BODIES", None, eligible_ids)

    return Resolution("ROUTED", None, eligible[0], eligible_ids)
