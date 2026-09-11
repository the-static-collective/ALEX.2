from __future__ import annotations


def run_nonbijective_relabel_control_probe() -> dict[str, object]:
    """Refuse a many-to-one label map before it can masquerade as pure relabeling."""
    declared_relabeling = {"X": "P", "Y": "P"}
    source_labels = sorted(declared_relabeling)
    image_labels = sorted(set(declared_relabeling.values()))

    if len(image_labels) != len(source_labels):
        return {
            "experiment": "NONBIJECTIVE-RELABEL-CONTROL-001",
            "observation": "RELABELING_COLLAPSES_LABELS",
            "status": "REFUSE",
            "reason": "relabeling-not-bijective",
            "declared_relabeling": declared_relabeling,
            "source_labels": source_labels,
            "image_labels": image_labels,
            "authority": "none",
        }

    return {
        "experiment": "NONBIJECTIVE-RELABEL-CONTROL-001",
        "observation": "PURE_RELABELING",
        "status": "PASS",
        "declared_relabeling": declared_relabeling,
        "source_labels": source_labels,
        "image_labels": image_labels,
        "authority": "none",
    }
