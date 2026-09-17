from __future__ import annotations

from datetime import datetime


def run_nonbijective_relabel_control_probe() -> dict[str, object]:
    """Refuse a many-to-one label map before it can masquerade as pure relabeling."""
    declared_relabeling = {"X": "P", "Y": "P"}
    source_labels = sorted(declared_relabeling)
    image_labels = sorted(set(declared_relabeling.values()))

    if len(image_labels) != len(source_labels):
        return {"experiment": "NONBIJECTIVE-RELABEL-CONTROL-001", "observation": "RELABELING_COLLAPSES_LABELS", "status": "REFUSE", "reason": "relabeling-not-bijective", "declared_relabeling": declared_relabeling, "source_labels": source_labels, "image_labels": image_labels, "authority": "none"}
    return {"experiment": "NONBIJECTIVE-RELABEL-CONTROL-001", "observation": "PURE_RELABELING", "status": "PASS", "declared_relabeling": declared_relabeling, "source_labels": source_labels, "image_labels": image_labels, "authority": "none"}


def run_capture_collision_control_probe() -> dict[str, object]:
    """Refuse a bijective-looking rename whose image captures a pre-existing destination label."""
    declared_relabeling = {"X": "P", "Y": "Q"}
    destination_scope_labels = {"P", "R"}
    image_labels = set(declared_relabeling.values())
    colliding_labels = sorted(image_labels & destination_scope_labels)
    if colliding_labels:
        return {"experiment": "RELABEL-CAPTURE-CONTROL-001", "observation": "RELABELING_CAPTURES_EXISTING_LABEL", "status": "REFUSE", "reason": "relabeling-destination-collision", "declared_relabeling": declared_relabeling, "destination_scope_labels": sorted(destination_scope_labels), "colliding_labels": colliding_labels, "authority": "none"}
    return {"experiment": "RELABEL-CAPTURE-CONTROL-001", "observation": "CAPTURE_AVOIDING_RELABELING", "status": "PASS", "declared_relabeling": declared_relabeling, "destination_scope_labels": sorted(destination_scope_labels), "colliding_labels": [], "relabelled_labels": sorted(image_labels), "authority": "none"}


def run_partial_relabel_scope_control_probe() -> dict[str, object]:
    """Refuse an incomplete relabel map when no completion/scope rule is declared."""
    declared_source_labels = {"X", "Y"}
    declared_relabeling = {"X": "P"}
    unmapped_source_labels = sorted(declared_source_labels - set(declared_relabeling))
    if unmapped_source_labels:
        return {"experiment": "PARTIAL-RELABEL-SCOPE-001", "observation": "PARTIAL_RELABEL_REQUIRES_SCOPE_RULE", "status": "REFUSE", "reason": "relabeling-scope-undeclared", "declared_source_labels": sorted(declared_source_labels), "declared_relabeling": declared_relabeling, "unmapped_source_labels": unmapped_source_labels, "authority": "none"}
    return {"experiment": "PARTIAL-RELABEL-SCOPE-001", "observation": "TOTAL_RELABELING_DOMAIN_DECLARED", "status": "PASS", "declared_source_labels": sorted(declared_source_labels), "declared_relabeling": declared_relabeling, "unmapped_source_labels": [], "authority": "none"}


def run_posthoc_relabel_chronology_control_probe() -> dict[str, object]:
    """Refuse applying a later relabel declaration as if it named an earlier observation."""
    observed_labels = ["X", "Y"]
    declared_relabeling = {"X": "P", "Y": "Q"}
    observation_at = "2026-09-13T12:00:00Z"
    relabel_declared_at = "2026-09-13T12:05:00Z"
    observation_time = datetime.fromisoformat(observation_at.replace("Z", "+00:00"))
    relabel_time = datetime.fromisoformat(relabel_declared_at.replace("Z", "+00:00"))
    if relabel_time > observation_time:
        return {"experiment": "POSTHOC-RELABEL-CHRONOLOGY-001", "observation": "RELABELING_CANNOT_REWRITE_PRIOR_OBSERVATION", "status": "REFUSE", "reason": "relabeling-postdates-observation", "observed_labels": observed_labels, "declared_relabeling": declared_relabeling, "observation_at": observation_at, "relabel_declared_at": relabel_declared_at, "authority": "none"}
    return {"experiment": "POSTHOC-RELABEL-CHRONOLOGY-001", "observation": "RELABELING_AVAILABLE_AT_OBSERVATION", "status": "PASS", "observed_labels": observed_labels, "declared_relabeling": declared_relabeling, "observation_at": observation_at, "relabel_declared_at": relabel_declared_at, "relabelled_labels": [declared_relabeling[label] for label in observed_labels], "authority": "none"}


def run_retrospective_relabel_descendant_probe() -> dict[str, object]:
    """Apply a later relabel only in a descendant view while preserving the T0 source receipt."""
    source = {
        "receipt_id": "observation:t0",
        "observed_labels": ["X", "Y"],
        "observation_at": "2026-09-13T12:00:00Z",
        "payload": {"X": "left", "Y": "right"},
    }
    source_snapshot = {
        "receipt_id": source["receipt_id"],
        "observed_labels": list(source["observed_labels"]),
        "observation_at": source["observation_at"],
        "payload": dict(source["payload"]),
    }
    declared_relabeling = {"X": "P", "Y": "Q"}
    relabel_declared_at = "2026-09-13T12:05:00Z"
    applied_at = "2026-09-13T12:10:00Z"
    descendant = {
        "receipt_id": "analysis:t2",
        "derived_from": source["receipt_id"],
        "declared_relabeling": declared_relabeling,
        "relabel_declared_at": relabel_declared_at,
        "applied_at": applied_at,
        "labels": [declared_relabeling[label] for label in source["observed_labels"]],
        "payload": {declared_relabeling[label]: value for label, value in source["payload"].items()},
        "authority": "none",
    }
    return {
        "experiment": "RETROSPECTIVE-RELABEL-DESCENDANT-001",
        "status": "PASS",
        "observation": "LATER_RELABEL_APPLIES_TO_DESCENDANT_NOT_SOURCE",
        "source_receipt": source,
        "source_unchanged": source == source_snapshot,
        "descendant_view": descendant,
        "authority": "none",
    }
