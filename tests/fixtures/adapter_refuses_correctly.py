# HARNESS TEST DOUBLE ONLY. NEVER EVIDENCE OF ALEX RUNTIME CONFORMANCE.
import json
import sys

specimen = json.load(sys.stdin)
expected = specimen["expected"]
result = {
    "specimen_id": specimen["id"],
    "disposition": expected["disposition"],
    "receipt_survivors": expected["required_receipt_survivors"],
    "promotions": [],
}
if "refusal_code" in expected:
    result["refusal_code"] = expected["refusal_code"]
json.dump(result, sys.stdout)
