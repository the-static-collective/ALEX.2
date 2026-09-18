from pathlib import Path
import json
import sys

from alex_runtime.commons import evaluate_commons_deposit

def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(json.dumps({"disposition":"REFUSE","reason":"usage"}))
        return 2
    try:
        record=json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    except (OSError,json.JSONDecodeError):
        print(json.dumps({"disposition":"REFUSE","reason":"invalid_input"}))
        return 2
    result=evaluate_commons_deposit(record)
    print(json.dumps(result,sort_keys=True))
    return 0 if result["disposition"]=="ACCEPT" else 1

if __name__=="__main__":
    raise SystemExit(main(sys.argv))
