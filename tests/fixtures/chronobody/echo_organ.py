import json
import sys


payload = json.load(sys.stdin)
json.dump(
    {"schema": "test.echo/v0", "payload": payload},
    sys.stdout,
    sort_keys=True,
    separators=(",", ":"),
)
sys.stdout.write("\n")
