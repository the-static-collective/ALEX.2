import copy
import json
import secrets
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.crucible import run_case
from tools.crucible_blind import (
    build_case,
    build_oracle,
    metamorphic_sibling,
    ruleset_digest,
    sha256_json,
)

PROFILE_PATH = ROOT / "crucible" / "profiles" / "alex.runtime.derivation-m0.json"
SPECIMENS = ROOT / "crucible" / "specimens"


def _prepare_metamorphic_case(case: dict, fixture_id: str) -> dict:
    token = secrets.token_hex(8)
    sibling = metamorphic_sibling(
        case,
        suffix=f"-meta-{token}",
        nonce=secrets.token_hex(16),
    )

    records = sibling.get("given", {}).get("records")
    relations = sibling.get("given", {}).get("relations")
    if not isinstance(records, list) or not isinstance(relations, list):
        raise ValueError("derivation profile requires given.records and given.relations arrays")

    distractor_origin_id = f"D0-{token}"
    distractor_result_id = f"D1-{token}"
    distractor_relation_id = f"RD-{token}"
    records.extend(
        [
            {"id": distractor_origin_id, "kind": "distractor_origin"},
            {"id": distractor_result_id, "kind": "distractor_result"},
        ]
    )
    relations.append(
        {
            "id": distractor_relation_id,
            "subject_id": distractor_result_id,
            "predicate": "derived_from",
            "object_id": distractor_origin_id,
        }
    )
    sibling.pop("input_digest", None)
    sibling["input_digest"] = sha256_json(sibling)
    return sibling


def run_profile() -> tuple[int, dict]:
    profile = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
    profile_id = profile["id"]
    rule_profile = profile["rule_profile"]
    operation_type = profile["operation_types"][0]
    adapter = profile["runtime_adapter"]
    adapter_path = ROOT / adapter["path"]
    adapter_argv = [sys.executable, str(adapter_path)]

    passed = 0
    failed = 0
    family_counts: dict[str, int] = {}

    for family in profile["fixture_families"]:
        family_id = family["id"]
        family_counts[family_id] = 0

        for fixture_id in family["fixtures"]:
            specimen_path = SPECIMENS / f"{fixture_id}.json"
            specimen = json.loads(specimen_path.read_text(encoding="utf-8"))
            case = build_case(
                specimen,
                nonce=secrets.token_hex(16),
                operation_type=operation_type,
                rule_profile=rule_profile,
            )
            oracle = build_oracle(specimen, case, metamorphic_family=family_id)

            original_code = run_case(case, oracle, adapter_argv)
            family_counts[family_id] += 1
            if original_code == 0:
                passed += 1
            else:
                failed += 1

            sibling = _prepare_metamorphic_case(case, fixture_id)
            sibling_oracle = copy.deepcopy(oracle)
            sibling_oracle["case_id"] = sibling["case_id"]
            sibling_oracle["metamorphic_family"] = family_id

            sibling_code = run_case(sibling, sibling_oracle, adapter_argv)
            family_counts[family_id] += 1
            if sibling_code == 0:
                passed += 1
            else:
                failed += 1

    summary = {
        "profile": profile_id,
        "ruleset_digest": ruleset_digest(rule_profile),
        "runtime_adapter": f'{adapter["path"]}@{adapter["version"]}',
        "families": family_counts,
        "passed": passed,
        "failed": failed,
    }
    return (0 if failed == 0 else 1), summary


def main() -> int:
    try:
        exit_code, summary = run_profile()
    except Exception as exc:
        print(f"derivation profile failed to execute: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
