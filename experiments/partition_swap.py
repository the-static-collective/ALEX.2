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


def _lift_receipt(
    *,
    lift_id: str,
    partition: dict[str, tuple[str, ...]],
    partition_rule: str,
    preservation_target: str,
) -> dict[str, object]:
    return {
        "lift_id": lift_id,
        "partition": {
            macro_name: list(names)
            for macro_name, names in partition.items()
        },
        "partition_rule": partition_rule,
        "preservation_target": preservation_target,
        "micro_receipt_refs": [edge["receipt_ref"] for edge in _MICRO_EDGES],
        "macro_nodes": list(partition),
        "macro_edges": _macro_edges(partition),
    }


def _macro_graph_differs(left: dict[str, object], right: dict[str, object]) -> bool:
    return (
        left["macro_nodes"] != right["macro_nodes"]
        or left["macro_edges"] != right["macro_edges"]
    )


def run_partition_swap_probe() -> dict[str, object]:
    """Measure one fixed counterexample; do not infer an intrinsic macro-node."""
    lifts = [
        _lift_receipt(
            lift_id=lift["lift_id"],
            partition=lift["partition"],
            partition_rule=lift["partition_rule"],
            preservation_target=lift["preservation_target"],
        )
        for lift in _LIFTS
    ]

    observation = (
        "PARTITION_DEPENDENT_MACRO_GRAPH"
        if _macro_graph_differs(lifts[0], lifts[1])
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


def run_isolated_node_control_probe() -> dict[str, object]:
    """Keep empty edge projections while preserving a macro-node-count delta."""
    two_node_partition = {"P": ("A", "B"), "Q": ("C", "D")}
    one_node_partition = {"Z": ("A", "B", "C", "D")}
    lifts = [
        _lift_receipt(
            lift_id="two-isolated-nodes",
            partition=two_node_partition,
            partition_rule="group-by-transaction-pair",
            preservation_target="declared-macro-node-existence",
        ),
        _lift_receipt(
            lift_id="one-isolated-node",
            partition=one_node_partition,
            partition_rule="group-all-names",
            preservation_target="declared-macro-node-existence",
        ),
    ]

    observation = (
        "PARTITION_DEPENDENT_MACRO_GRAPH"
        if _macro_graph_differs(lifts[0], lifts[1])
        else "NO_PARTITION_DELTA_OBSERVED"
    )
    return {
        "experiment": "ISOLATED-NODE-CONTROL-001",
        "observation": observation,
        "lifts": lifts,
        "authority": "none",
    }


def run_order_swap_control_probe() -> dict[str, object]:
    """Witness order-only serialization drift without changing labeled graph content."""
    first_edge = {"from": "X", "verb": "appoints", "to": "Y", "system": "S"}
    second_edge = {"from": "Y", "verb": "appoints", "to": "X", "system": "S"}
    left = {
        "macro_nodes": ["X", "Y"],
        "macro_edges": [first_edge, second_edge],
    }
    right = {
        "macro_nodes": ["Y", "X"],
        "macro_edges": [second_edge, first_edge],
    }

    left_edges = {tuple(sorted(edge.items())) for edge in left["macro_edges"]}
    right_edges = {tuple(sorted(edge.items())) for edge in right["macro_edges"]}
    same_labeled_content = (
        set(left["macro_nodes"]) == set(right["macro_nodes"])
        and left_edges == right_edges
    )
    raw_serialization_differs = (
        left["macro_nodes"] != right["macro_nodes"]
        and left["macro_edges"] != right["macro_edges"]
    )
    observation = (
        "SERIALIZATION_ORDER_DELTA_ONLY"
        if raw_serialization_differs and same_labeled_content
        else "ORDER_CONTROL_FAILED"
    )
    return {
        "experiment": "ORDER-SWAP-CONTROL-001",
        "observation": observation,
        "left": left,
        "right": right,
        "authority": "none",
    }
