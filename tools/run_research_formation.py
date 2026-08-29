from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from alex_runtime.chronobody import parse_registry  # noqa: E402
from alex_runtime.digests import canonical_json_bytes  # noqa: E402
from alex_runtime.research_formation import (  # noqa: E402
    ResearchFormationRequestError,
    evaluate_research_formation_run,
)


REGISTRY_PATH = ROOT / "chronobody" / "registry.v0.json"


def _load_registry():
    return parse_registry(json.loads(REGISTRY_PATH.read_text(encoding="utf-8")))


def _read_request(path_arg: str | None) -> object:
    if path_arg is None or path_arg == "-":
        return json.load(sys.stdin)
    return json.loads(Path(path_arg).read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) > 1:
        print("invalid request: expected zero or one input path", file=sys.stderr)
        return 2

    try:
        request = _read_request(args[0] if args else None)
        entries = _load_registry()
        result = evaluate_research_formation_run(request, entries)
    except (
        OSError,
        UnicodeError,
        json.JSONDecodeError,
        ResearchFormationRequestError,
        ValueError,
    ) as exc:
        print(f"invalid request: {exc}", file=sys.stderr)
        return 2

    sys.stdout.buffer.write(canonical_json_bytes(result) + b"\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
