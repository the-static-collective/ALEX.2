"""RELATION-NURSERY-001: source-preserving proposal and pressure receipts.

Research-only; does not create historical truth, evidence from similarity, or
new ALEX source / claim authority. A failed interpretation remains queryable.
"""
from __future__ import annotations

from hashlib import sha256
import json

DISPOSITIONS = frozenset({"proposed", "calculated", "pressure_tested", "unresolved", "refuted"})
RESULTS = frozenset({"pass", "fail", "inconclusive"})


def _ref(v, name):
    if not isinstance(v, str) or not v.strip() or len(v) > 512:
        raise ValueError(f"{name}: bounded nonblank reference required")
    return v


def _digest(payload):
    return "sha256:" + sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False,
                           separators=(",", ":"), allow_nan=False).encode("utf8")).hexdigest()


def propose_relation(*, proposal_id, source_refs, relation_expression,
                     method_ref, author_ref):
    _ref(proposal_id, "proposal_id")
    _ref(relation_expression, "relation_expression")
    _ref(method_ref, "method_ref")
    _ref(author_ref, "author_ref")
    if not isinstance(source_refs, list) or not 2 <= len(source_refs) <= 16:
        raise ValueError("two to sixteen source references required")
    refs = [_ref(ref, "source_ref") for ref in source_refs]
    if len(set(refs)) != len(refs):
        raise ValueError("source identities must remain distinct")
    body = {"schema": "alex.relation-nursery/0.1", "proposal_id": proposal_id,
            "source_refs": refs, "relation_expression": relation_expression,
            "method_ref": method_ref, "author_ref": author_ref, "disposition": "proposed",
            "non_claims": ["source resemblance is not evidence of intentional correspondence",
                           "mathematical equality does not prove historical connection",
                           "proposing is not promoting"]}
    return {**body, "proposal_digest": _digest(body)}


def attach_pressure(proposal, *, experiment_ref, result, observation_ref, interpretation):
    if proposal.get("schema") != "alex.relation-nursery/0.1" or proposal.get("proposal_digest") is None:
        raise ValueError("versioned nursery proposal required")
    original = {k:v for k,v in proposal.items() if k != "proposal_digest"}
    if _digest(original) != proposal["proposal_digest"]:
        raise ValueError("proposal has been rewritten")
    _ref(experiment_ref, "experiment_ref")
    _ref(observation_ref, "observation_ref")
    if result not in RESULTS:
        raise ValueError("explicit pass/fail/inconclusive required")
    if interpretation not in ("not_assessed", "independently_supported", "contradicted", "unresolved"):
        raise ValueError("interpretation requires an explicit disposition")
    # The result of one experiment is not an evidentiary rank or final judgment.
    body = {"schema": "alex.relation-pressure/0.1", "proposal_ref": proposal["proposal_digest"],
            "experiment_ref": experiment_ref, "result": result, "observation_ref": observation_ref,
            "interpretation": interpretation,
            "non_claim": "experimental result does not grant source, historical or theological authority"}
    return {**body, "pressure_digest": _digest(body)}
