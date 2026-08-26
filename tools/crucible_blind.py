from __future__ import annotations

import copy
import hashlib
import json


def canonical_json_bytes(value: dict) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def sha256_json(value: dict) -> str:
    return "sha256:" + hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def ruleset_digest(rule_profile: str) -> str:
    return sha256_json({"rule_profile": rule_profile})


def build_case(
    specimen: dict,
    *,
    nonce: str,
    operation_type: str = "constitutional_evaluation",
    rule_profile: str = "alex-crucible-v1",
) -> dict:
    case = {
        "case_id": specimen["id"],
        "operation_type": operation_type,
        "rule_profile": rule_profile,
        "given": copy.deepcopy(specimen["given"]),
        "attempt": copy.deepcopy(specimen["attempt"]),
        "nonce": nonce,
    }
    case["input_digest"] = sha256_json(case)
    return case


def build_oracle(
    specimen: dict,
    case: dict,
    *,
    metamorphic_family: str | None = None,
) -> dict:
    expected = specimen["expected"]
    return {
        "case_id": case["case_id"],
        "expected_disposition": expected["disposition"],
        "expected_reason_code": expected.get("refusal_code"),
        "required_survivors": list(expected["required_receipt_survivors"]),
        "forbidden_outputs": list(expected["forbidden_promotions"]),
        "metamorphic_family": metamorphic_family,
    }
