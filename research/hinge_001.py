from __future__ import annotations

from typing import Any

GRAMMAR_SCHEMA = "alex.hinge-grammar/v0"
DELTA_SCHEMA = "alex.hinge-grammar-delta/v0"


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _refuse(reason: str) -> dict[str, Any]:
    return {
        "schema": DELTA_SCHEMA,
        "disposition": "REFUSE",
        "reason": reason,
        "authority": "none",
        "meaning_verdict": "none",
    }


def _rule_map(snapshot: object) -> dict[str, str] | None:
    if not isinstance(snapshot, dict):
        return None
    if snapshot.get("schema") != GRAMMAR_SCHEMA:
        return None
    if any(not _nonempty(snapshot.get(k)) for k in ("grammar_ref", "carrier", "source_ref")):
        return None
    rules = snapshot.get("rules")
    if not isinstance(rules, list):
        return None

    out: dict[str, str] = {}
    for rule in rules:
        if not isinstance(rule, dict):
            return None
        selector = rule.get("selector")
        relation = rule.get("relation")
        if not _nonempty(selector) or not _nonempty(relation):
            return None
        if selector in out:
            return None
        out[selector] = relation
    return out


def resolve_selector(snapshot: object, selector: str) -> str | None:
    rules = _rule_map(snapshot)
    if rules is None or not _nonempty(selector):
        return None
    return rules.get(selector)


def witness_grammar_delta(
    pre: object,
    encounter_ref: str,
    post: object,
    probes: object,
) -> dict[str, Any]:
    """
    Witness a bounded delta between two declared interpretive grammars.

    The function does not decide whether either grammar is true, better, canonical,
    or authoritative. It also does not infer that the encounter caused the change.
    It only records the before/after rule delta under an explicit encounter reference.
    """
    pre_rules = _rule_map(pre)
    post_rules = _rule_map(post)
    if pre_rules is None or post_rules is None:
        return _refuse("invalid_grammar_snapshot")
    assert isinstance(pre, dict) and isinstance(post, dict)

    if not _nonempty(encounter_ref):
        return _refuse("missing_encounter_ref")
    if pre["carrier"] != post["carrier"]:
        return _refuse("carrier_changed")
    if pre["source_ref"] != post["source_ref"]:
        return _refuse("source_changed")
    if not isinstance(probes, list) or any(not _nonempty(p) for p in probes):
        return _refuse("invalid_probes")
    if len(probes) != len(set(probes)):
        return _refuse("duplicate_probe")

    pre_keys = set(pre_rules)
    post_keys = set(post_rules)

    added = [
        {"selector": key, "relation": post_rules[key]}
        for key in sorted(post_keys - pre_keys)
    ]
    removed = [
        {"selector": key, "relation": pre_rules[key]}
        for key in sorted(pre_keys - post_keys)
    ]
    retargeted = [
        {
            "selector": key,
            "before": pre_rules[key],
            "after": post_rules[key],
        }
        for key in sorted(pre_keys & post_keys)
        if pre_rules[key] != post_rules[key]
    ]
    unchanged = [
        {"selector": key, "relation": pre_rules[key]}
        for key in sorted(pre_keys & post_keys)
        if pre_rules[key] == post_rules[key]
    ]

    probe_results = []
    changed_probe_count = 0
    for selector in probes:
        before = pre_rules.get(selector)
        after = post_rules.get(selector)
        changed = before != after
        if changed:
            changed_probe_count += 1
        probe_results.append(
            {
                "selector": selector,
                "before": before,
                "after": after,
                "changed": changed,
            }
        )

    grammar_changed = bool(added or removed or retargeted)

    return {
        "schema": DELTA_SCHEMA,
        "disposition": "ACCEPT",
        "reason": None,
        "encounter_ref": encounter_ref,
        "source_ref": pre["source_ref"],
        "carrier": pre["carrier"],
        "pre_grammar_ref": pre["grammar_ref"],
        "post_grammar_ref": post["grammar_ref"],
        "added_rules": added,
        "removed_rules": removed,
        "retargeted_rules": retargeted,
        "unchanged_rules": unchanged,
        "probe_results": probe_results,
        "grammar_changed": grammar_changed,
        "constitutive_candidate": grammar_changed and changed_probe_count > 0,
        "causal_status": "not_established",
        "authority": "none",
        "meaning_verdict": "none",
    }
