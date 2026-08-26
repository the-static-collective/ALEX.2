# HARNESS TEST DOUBLE ONLY. NEVER EVIDENCE OF ALEX RUNTIME CONFORMANCE.
import hashlib
import json
import sys


def digest(value):
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


case = json.load(sys.stdin)
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
