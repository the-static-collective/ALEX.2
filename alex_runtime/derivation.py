import copy

from alex_runtime import DERIVATION_M0_PROFILE, DERIVATION_RULE_ID, DERIVATION_RULE_VERSION
from alex_runtime.digests import sha256_json

DERIVATION_M0_MANIFEST = {
    "profile": DERIVATION_M0_PROFILE,
    "rules": [
        {
            "rule_id": DERIVATION_RULE_ID,
            "rule_version": DERIVATION_RULE_VERSION,
            "predicate": "SUPPORTS",
            "negative_reason_code": "ATTENTION_NOT_SUPPORT",
            "undefined_reason_code": "NO_ATTRIBUTABLE_SUPPORT_PATH",
        }
    ],
}


def ruleset_manifest(profile: str) -> dict | None:
    if profile != DERIVATION_M0_PROFILE:
        return None
    return copy.deepcopy(DERIVATION_M0_MANIFEST)


def ruleset_manifest_digest(profile: str) -> str | None:
    manifest = ruleset_manifest(profile)
    return None if manifest is None else sha256_json(manifest)
