from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from alex_runtime.commons import evaluate_commons_deposit  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 1:
        print(json.dumps({"disposition":"REFUSE","reason":"usage"}))
        return 2
    try:
        record=json.loads(Path(args[0]).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        print(json.dumps({"disposition":"REFUSE","reason":"invalid_input"}))
        return 2
    result=evaluate_commons_deposit(record)
    print(json.dumps(result,sort_keys=True))
    return 0 if result["disposition"]=="ACCEPT" else 1


if __name__=="__main__":
    raise SystemExit(main())
