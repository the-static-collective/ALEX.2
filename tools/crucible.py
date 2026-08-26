import argparse
import json
import secrets
import subprocess
import sys
from pathlib import Path

try:
    from tools.crucible_blind import build_case, build_oracle, ruleset_digest
except ModuleNotFoundError:  # direct `python tools/crucible.py` execution
    from crucible_blind import build_case, build_oracle, ruleset_digest


DISPOSITIONS = {"ACCEPT", "REFUSE", "UNRESOLVED", "INSUFFICIENT_TO_TEST"}
TERMINAL_STATES = {"FINISHED", "SUSPENDED", "ERRORED", "CANCELLED"}
RESULT_KEYS = {
    "case_id",
    "input_digest",
    "ruleset_digest",
    "disposition",
    "reason_code",
    "receipt_survivors",
    "derived_assertions",
    "execution_trace_summary",
}


def _valid_string_list(value) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value)


def validate_runtime_result(case: dict, actual: dict) -> list[str]:
    errors: list[str] = []

    actual_keys = set(actual)
    for missing in sorted(RESULT_KEYS - actual_keys):
        errors.append(f"missing result key: {missing}")
    for unexpected in sorted(actual_keys - RESULT_KEYS):
        errors.append(f"unexpected result key: {unexpected}")

    if actual.get("case_id") != case["case_id"]:
        errors.append("case_id mismatch")
    if actual.get("input_digest") != case["input_digest"]:
        errors.append("input_digest mismatch")
    if actual.get("ruleset_digest") != ruleset_digest(case["rule_profile"]):
        errors.append("ruleset_digest mismatch")

    if actual.get("disposition") not in DISPOSITIONS:
        errors.append("invalid disposition")

    reason_code = actual.get("reason_code")
    if reason_code is not None and not isinstance(reason_code, str):
        errors.append("reason_code must be string or null")

    if not _valid_string_list(actual.get("receipt_survivors")):
        errors.append("receipt_survivors must be a list of strings")
    if not _valid_string_list(actual.get("derived_assertions")):
        errors.append("derived_assertions must be a list of strings")

    summary = actual.get("execution_trace_summary")
    if not isinstance(summary, dict):
        errors.append("execution_trace_summary must be an object")
    else:
        summary_keys = set(summary)
        if summary_keys != {"terminal_state", "step_count"}:
            errors.append("execution_trace_summary keys mismatch")
        if summary.get("terminal_state") not in TERMINAL_STATES:
            errors.append("invalid execution terminal_state")
        step_count = summary.get("step_count")
        if isinstance(step_count, bool) or not isinstance(step_count, int) or step_count < 0:
            errors.append("invalid execution step_count")

    return errors


def compare_result(case: dict, oracle: dict, actual: dict) -> list[str]:
    errors: list[str] = []

    if oracle["case_id"] != case["case_id"]:
        errors.append("oracle case_id mismatch")
    if actual.get("disposition") != oracle["expected_disposition"]:
        errors.append("disposition mismatch")
    if actual.get("reason_code") != oracle["expected_reason_code"]:
        errors.append("reason_code mismatch")

    survivors = set(actual.get("receipt_survivors", []))
    for required in oracle["required_survivors"]:
        if required not in survivors:
            errors.append(f"missing required receipt survivor: {required}")

    outputs = set(actual.get("derived_assertions", []))
    for forbidden in oracle["forbidden_outputs"]:
        if forbidden in outputs:
            errors.append(f"forbidden derived output: {forbidden}")

    return errors


def run_fixture(
    fixture_path: Path,
    adapter_argv: list[str],
    *,
    nonce: str | None = None,
) -> int:
    specimen = json.loads(fixture_path.read_text(encoding="utf-8"))
    specimen_id = specimen.get("id", fixture_path.stem)

    if not adapter_argv:
        print(f"FAIL {specimen_id}: adapter command is empty")
        return 1

    case = build_case(specimen, nonce=nonce or secrets.token_hex(16))
    oracle = build_oracle(specimen, case)

    completed = subprocess.run(
        adapter_argv,
        input=json.dumps(case, sort_keys=True, separators=(",", ":")),
        text=True,
        capture_output=True,
        check=False,
        shell=False,
    )
    if completed.returncode != 0:
        detail = completed.stderr.strip() or completed.stdout.strip() or "no adapter output"
        print(f"FAIL {specimen_id}: adapter exited {completed.returncode}: {detail}")
        return 1

    try:
        actual = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        print(f"FAIL {specimen_id}: adapter stdout is not one JSON object: {exc}")
        return 1

    if not isinstance(actual, dict):
        print(f"FAIL {specimen_id}: adapter result must be a JSON object")
        return 1

    errors = validate_runtime_result(case, actual)
    if not errors:
        errors.extend(compare_result(case, oracle, actual))
    if errors:
        print(f"FAIL {specimen_id}: {'; '.join(errors)}")
        return 1

    print(f"PASS {specimen_id}")
    return 0


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run one ALEX Crucible specimen against an adapter")
    parser.add_argument("--fixture", required=True, type=Path)
    parser.add_argument("--adapter", nargs=argparse.REMAINDER, required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return run_fixture(args.fixture, args.adapter)


if __name__ == "__main__":
    sys.exit(main())
