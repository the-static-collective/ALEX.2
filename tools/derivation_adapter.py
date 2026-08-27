import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from alex_runtime.derivation import evaluate_relation_case


def runtime_result_from_case(case: dict) -> dict:
    result = evaluate_relation_case(case)
    evaluation = result["evaluation"]
    conclusion = result["conclusion_assertion"]
    execution = result["execution"]

    return {
        "case_id": case["case_id"],
        "input_digest": case["input_digest"],
        "ruleset_digest": evaluation["ruleset_digest"],
        "disposition": evaluation["disposition"],
        "reason_code": None if evaluation["disposition"] == "ACCEPT" else evaluation["reason_code"],
        "receipt_survivors": evaluation["required_survivors"],
        "derived_assertions": [] if conclusion is None else [
            f'{conclusion["subject_id"]} --{conclusion["predicate"]}--> {conclusion["object_id"]}'
        ],
        "execution_trace_summary": {
            "terminal_state": execution["terminal_state"],
            "step_count": execution["step_count"],
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
        print(f"derivation adapter failed: {exc}", file=sys.stderr)
        return 1

    json.dump(result, sys.stdout, sort_keys=True, separators=(",", ":"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
