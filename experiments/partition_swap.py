from __future__ import annotations


_MICRO_EDGES = (
    {
        "from": "A",
        "verb": "appoints",
        "to": "B",
        "system": "S",
        "receipt_ref": "receipt:appoints-a-b",
    },
    {
        "from": "C",
        "verb": "appoints",
        "to": "D",
        "system": "S",
        "receipt_ref": "receipt:appoints-c-d",
    },
)

_LIFTS = (
    {
        "lift_id": "role-side",
        "partition": {"X": ("A", "C"), "Y": ("B", "D")},
        "partition_rule": "group-by-edge-role",
        "preservation_target": "external-appoints-relation",
    },
    {
        "lift_id": "transaction-pair",
        "partition": {"P": ("A", "B"), "Q": ("C", "D")},
        "partition_rule": "group-by-transaction-pair",
        "preservation_target": "transaction-boundary",
    },
)


def _macro_edges(partition: dict[str, tuple[str, ...]]) -> list[dict[str, str]]:
    membership = {
        name: macro_name
        for macro_name, names in partition.items()
        for name in names
    }
    macro_edges: list[dict[str, str]] = []
    seen: set[tuple[str, str, str, str]] = set()

    for edge in _MICRO_EDGES:
        source = membership[edge["from"]]
        target = membership[edge["to"]]
        if source == target:
            continue
        identity = (source, edge["verb"], target, edge["system"])
        if identity in seen:
            continue
        seen.add(identity)
        macro_edges.append(
            {
                "from": source,
                "verb": edge["verb"],
                "to": target,
                "system": edge["system"],
            }
        )

    return macro_edges


def run_partition_swap_probe() -> dict[str, object]:
    """Measure one fixed counterexample; do not infer an intrinsic macro-node."""
    receipt_refs = [edge["receipt_ref"] for edge in _MICRO_EDGES]
    lifts = []

    for lift in _LIFTS:
        lifts.append(
            {
                "lift_id": lift["lift_id"],
                "partition": {
                    macro_name: list(names)
                    for macro_name, names in lift["partition"].items()
                },
                "partition_rule": lift["partition_rule"],
                "preservation_target": lift["preservation_target"],
                "micro_receipt_refs": list(receipt_refs),
                "macro_edges": _macro_edges(lift["partition"]),
            }
        )

    observation = (
        "PARTITION_DEPENDENT_MACRO_GRAPH"
        if lifts[0]["macro_edges"] != lifts[1]["macro_edges"]
        else "NO_PARTITION_DELTA_OBSERVED"
    )
    return {
        "experiment": "PARTITION-SWAP-001",
        "observation": observation,
        "lifts": lifts,
        "authority": "none",
    }


def run_relabel_control_probe() -> dict[str, object]:
    """Witness a serialization delta that disappears under one declared relabeling."""
    left_macro_edges = [
        {"from": "X", "verb": "appoints", "to": "Y", "system": "S"}
    ]
    right_macro_edges = [
        {"from": "P", "verb": "appoints", "to": "Q", "system": "S"}
    ]
    declared_relabeling = {"X": "P", "Y": "Q"}
    left_relabelled_macro_edges = [
        {
            "from": declared_relabeling[edge["from"]],
            "verb": edge["verb"],
            "to": declared_relabeling[edge["to"]],
            "system": edge["system"],
        }
        for edge in left_macro_edges
    ]

    observation = (
        "SERIALIZATION_DELTA_ONLY"
        if left_macro_edges != right_macro_edges
        and left_relabelled_macro_edges == right_macro_edges
        else "RELABEL_CONTROL_FAILED"
    )
    return {
        "experiment": "RELABEL-CONTROL-001",
        "observation": observation,
        "left_macro_edges": left_macro_edges,
        "right_macro_edges": right_macro_edges,
        "declared_relabeling": declared_relabeling,
        "left_relabelled_macro_edges": left_relabelled_macro_edges,
        "authority": "none",
    }
