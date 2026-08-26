# HARNESS TEST DOUBLE ONLY. It intentionally exploits any leaked ORACLE.
import hashlib
import json
import sys


def digest(value):
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


payload = json.load(sys.stdin)

# Old vulnerable boundary: if the answer key is visible, copy it and pass.
if "expected" in payload:
    expected = payload["expected"]
    result = {
        "specimen_id": payload["id"],
        "disposition": expected["disposition"],
        "receipt_survivors": expected["required_receipt_survivors"],
        "promotions": [],
    }
    if "refusal_code" in expected:
        result["refusal_code"] = expected["refusal_code"]
    json.dump(result, sys.stdout)
    raise SystemExit(0)

# Blind boundary: no ORACLE is visible, so the cheater guesses badly.
case = payload
json.dump(
    {
        "case_id": case["case_id"],
        "input_digest": case["input_digest"],
        "ruleset_digest": digest({"rule_profile": case["rule_profile"]}),
        "disposition": "ACCEPT",
        "reason_code": None,
        "receipt_survivors": [],
        "derived_assertions": ["source_absence"],
        "execution_trace_summary": {"terminal_state": "FINISHED", "step_count": 1},
    },
    sys.stdout,
)
