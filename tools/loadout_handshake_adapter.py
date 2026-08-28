import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from alex_runtime.handshake import evaluate_loadout_handshake
from tools.crucible_blind import ruleset_digest


def runtime_result_from_case(case: dict) -> dict:
    result = evaluate_loadout_handshake(case)
    survivors = list(result["receipt_survivors"])
    survivors.append(f'recompile_required:{str(result["recompile_required"]).lower()}')
    survivors = list(dict.fromkeys(survivors))
    return {
        "case_id": case["case_id"],
        "input_digest": case["input_digest"],
        "ruleset_digest": ruleset_digest(case["rule_profile"]),
        "disposition": result["disposition"],
        "reason_code": result["reason_code"],
        "receipt_survivors": survivors,
        "derived_assertions": [],
        "execution_trace_summary": {
            "terminal_state": result["execution"]["terminal_state"],
            "step_count": result["execution"]["step_count"],
        },
    }


def main() -> int:
    try:
        case = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(f"CASE is not valid JSON: {exc}", file=sys.stderr)
        return 2
    if not isinstance(case, dict):
        print("CASE must be a JSON object", file=sys.stderr)
        return 2
    try:
        result = runtime_result_from_case(case)
    except Exception as exc:
        print(f"LOADOUT handshake adapter failed: {exc}", file=sys.stderr)
        return 1
    json.dump(result, sys.stdout, sort_keys=True, separators=(",", ":"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
