import hashlib
import json


def canonical_json_bytes(value: dict) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def sha256_json(value: dict) -> str:
    return "sha256:" + hashlib.sha256(canonical_json_bytes(value)).hexdigest()
