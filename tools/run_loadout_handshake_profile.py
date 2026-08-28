import copy
import json
import secrets
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from alex_runtime.handshake import compile_payload_digest
from tools.crucible import run_case
from tools.crucible_blind import build_case, build_oracle, ruleset_digest

PROFILE_PATH = ROOT / "crucible" / "profiles" / "alex.runtime.loadout-handshake-m0.json"
SPECIMENS = ROOT / "crucible" / "specimens"
PROFILE_ID = "alex.runtime/loadout-handshake-m0"
OPERATION_TYPE = "loadout_handshake"


def _metamorphic_specimen(specimen: dict) -> dict:
    sibling = copy.deepcopy(specimen)
    token = secrets.token_hex(8)
    sibling["id"] = f'{specimen["id"]}-meta-{token}'

    compile_record = sibling["given"]["compile"]
    envelope = sibling["attempt"]["run_envelope"]
    expected = sibling["expected"]

    old_compile_id = compile_record["compile_id"]
    old_parent_id = compile_record.get("parent_compile_id")
    old_trace_id = compile_record["compile_trace"]["id"]
    old_fence_ref = compile_record["effect_fence_ref"]
    old_run_id = envelope["run_id"]

    new_compile_id = f"{old_compile_id}-meta-{token}"
    new_parent_id = None if old_parent_id is None else f"{old_parent_id}-meta-{token}"
    new_trace_id = f"{old_trace_id}-meta-{token}"
    new_fence_ref = f"{old_fence_ref}-meta-{token}"
    new_run_id = f"{old_run_id}-meta-{token}"

    compile_record["compile_id"] = new_compile_id
    compile_record["parent_compile_id"] = new_parent_id
    compile_record["compile_trace"]["id"] = new_trace_id
    compile_record["effect_fence_ref"] = new_fence_ref
    compile_record["capability_bindings"].reverse()
    compile_record["effective_effects"].reverse()
    compile_record["compile_digest"] = compile_payload_digest(compile_record)

    envelope["run_id"] = new_run_id
    envelope["compile_id"] = new_compile_id
    envelope["compile_digest"] = compile_record["compile_digest"]
    envelope["compile_trace_ref"] = new_trace_id
    envelope["effect_fence_ref"] = new_fence_ref
    envelope["capability_bindings"] = copy.deepcopy(compile_record["capability_bindings"])

    replacements = {
        f"compile:{old_compile_id}": f"compile:{new_compile_id}",
        f"compile_trace:{old_trace_id}": f"compile_trace:{new_trace_id}",
        f"effect_fence:{old_fence_ref}": f"effect_fence:{new_fence_ref}",
    }
    if old_parent_id is not None:
        replacements[f"parent_compile:{old_parent_id}"] = f"parent_compile:{new_parent_id}"
    expected["required_receipt_survivors"] = [
        replacements.get(item, item) for item in expected["required_receipt_survivors"]
    ]
    return sibling


def build_metamorphic_case(specimen: dict) -> dict:
    sibling = _metamorphic_specimen(specimen)
    return build_case(
        sibling,
        nonce=secrets.token_hex(16),
        operation_type=OPERATION_TYPE,
        rule_profile=PROFILE_ID,
    )


def run_profile() -> tuple[int, dict]:
    profile = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
    adapter = profile["runtime_adapter"]
    adapter_argv = [sys.executable, str(ROOT / adapter["path"])]

    passed = 0
    failed = 0
    family_counts: dict[str, int] = {}

    for family in profile["fixture_families"]:
        family_id = family["id"]
        family_counts[family_id] = 0
        for fixture_id in family["fixtures"]:
            specimen = json.loads((SPECIMENS / f"{fixture_id}.json").read_text(encoding="utf-8"))
            original = build_case(
                specimen,
                nonce=secrets.token_hex(16),
                operation_type=OPERATION_TYPE,
                rule_profile=PROFILE_ID,
            )
            original_oracle = build_oracle(specimen, original, metamorphic_family=family_id)
            original_code = run_case(original, original_oracle, adapter_argv)
            family_counts[family_id] += 1
            passed += int(original_code == 0)
            failed += int(original_code != 0)

            sibling_specimen = _metamorphic_specimen(specimen)
            sibling = build_case(
                sibling_specimen,
                nonce=secrets.token_hex(16),
                operation_type=OPERATION_TYPE,
                rule_profile=PROFILE_ID,
            )
            sibling_oracle = build_oracle(sibling_specimen, sibling, metamorphic_family=family_id)
            sibling_code = run_case(sibling, sibling_oracle, adapter_argv)
            family_counts[family_id] += 1
            passed += int(sibling_code == 0)
            failed += int(sibling_code != 0)

    summary = {
        "profile": profile["id"],
        "ruleset_digest": ruleset_digest(profile["rule_profile"]),
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
        print(f"LOADOUT handshake profile failed to execute: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
