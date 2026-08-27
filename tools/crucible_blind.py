from __future__ import annotations

import copy
import sys
from pathlib import Path

try:
    from alex_runtime.digests import canonical_json_bytes, sha256_json
    from alex_runtime.derivation import ruleset_manifest
except ModuleNotFoundError:  # direct `python tools/...` execution
    ROOT = Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from alex_runtime.digests import canonical_json_bytes, sha256_json
    from alex_runtime.derivation import ruleset_manifest


def ruleset_digest(rule_profile: str) -> str:
    manifest = ruleset_manifest(rule_profile)
    if manifest is not None:
        return sha256_json(manifest)
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


def metamorphic_sibling(
    case: dict,
    *,
    suffix: str,
    nonce: str,
    distractor_relation: dict | None = None,
) -> dict:
    sibling = copy.deepcopy(case)
    sibling["case_id"] = case["case_id"] + suffix
    sibling["nonce"] = nonce

    relations = sibling.get("given", {}).get("relations")
    if isinstance(relations, list):
        relations.reverse()
        if distractor_relation is not None:
            relations.append(copy.deepcopy(distractor_relation))
    elif distractor_relation is not None:
        raise ValueError("distractor_relation requires given.relations to be a list")

    sibling.pop("input_digest", None)
    sibling["input_digest"] = sha256_json(sibling)
    return sibling
