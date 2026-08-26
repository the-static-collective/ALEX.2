import argparse
import json
import subprocess
import sys
from pathlib import Path


def compare_result(specimen: dict, actual: dict) -> list[str]:
    expected = specimen["expected"]
    errors: list[str] = []

    if actual.get("specimen_id") != specimen["id"]:
        errors.append("specimen_id mismatch")
    if actual.get("disposition") != expected["disposition"]:
        errors.append("disposition mismatch")
    if expected.get("refusal_code") != actual.get("refusal_code"):
        errors.append("refusal_code mismatch")

    survivors = set(actual.get("receipt_survivors", []))
    for required in expected["required_receipt_survivors"]:
        if required not in survivors:
            errors.append(f"missing required receipt survivor: {required}")

    promotions = set(actual.get("promotions", []))
    for forbidden in expected["forbidden_promotions"]:
        if forbidden in promotions:
            errors.append(f"forbidden promotion: {forbidden}")

    return errors


def run_fixture(fixture_path: Path, adapter_argv: list[str]) -> int:
    specimen = json.loads(fixture_path.read_text(encoding="utf-8"))
    specimen_id = specimen.get("id", fixture_path.stem)

    if not adapter_argv:
        print(f"FAIL {specimen_id}: adapter command is empty")
        return 1

    completed = subprocess.run(
        adapter_argv,
        input=json.dumps(specimen),
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

    errors = compare_result(specimen, actual)
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
