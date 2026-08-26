# HARNESS TEST DOUBLE ONLY. It returns a valid-looking result for the wrong case.
import hashlib
import json
import sys


def digest(value):
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


case = json.load(sys.stdin)
json.dump(
    {
        "case_id": "foreign-case",
        "input_digest": case["input_digest"],
        "ruleset_digest": digest({"rule_profile": case["rule_profile"]}),
        "disposition": "REFUSE",
        "reason_code": "SEARCH_COVERAGE_INSUFFICIENT",
        "receipt_survivors": ["search_observation:S1"],
        "derived_assertions": [],
        "execution_trace_summary": {"terminal_state": "FINISHED", "step_count": 1},
    },
    sys.stdout,
)
