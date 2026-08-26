import json
import sys

specimen = json.load(sys.stdin)
json.dump(
    {
        "specimen_id": specimen["id"],
        "disposition": "ACCEPT",
        "receipt_survivors": [],
        "promotions": ["source_absence"],
    },
    sys.stdout,
)
