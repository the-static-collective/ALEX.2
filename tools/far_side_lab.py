from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from alex_runtime.digests import canonical_json_bytes
from experiments.far_side.engine import evaluate_far_side_case


def _read_payload(path: str) -> object:
    text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
    return json.loads(text)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Evaluate one experimental FAR-SIDE receipt.")
    parser.add_argument("path", nargs="?", default="-", help="JSON file path or - for stdin")
    args = parser.parse_args(argv)

    try:
        payload = _read_payload(args.path)
    except (OSError, json.JSONDecodeError) as exc:
        message = "invalid JSON" if isinstance(exc, json.JSONDecodeError) else f"cannot read input: {exc}"
        print(message, file=sys.stderr)
        return 2

    result = evaluate_far_side_case(payload)
    sys.stdout.buffer.write(canonical_json_bytes(result) + b"\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
