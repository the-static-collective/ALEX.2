import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from alex_runtime.binocular_recursion import evaluate_binocular_recursion_case


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit an ALEX BINOCULAR-RECURSION-001 trace")
    parser.add_argument("path", nargs="?", help="JSON case path; omit to read stdin")
    args = parser.parse_args()
    try:
        raw = Path(args.path).read_text(encoding="utf-8") if args.path else sys.stdin.read()
        case = json.loads(raw)
        if not isinstance(case, dict):
            raise ValueError("case must decode to a JSON object")
        result = evaluate_binocular_recursion_case(case)
    except Exception as exc:
        print(f"binocular recursion failed to execute: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if result["disposition"] == "ACCEPT" else 1


if __name__ == "__main__":
    sys.exit(main())
