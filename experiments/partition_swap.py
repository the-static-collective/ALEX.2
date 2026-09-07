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

_MICRO_NODES = frozenset(
    endpoint
    for edge in _MICRO_EDGES
    for endpoint in (edge["from"], edge["to"])
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


def _partition_refusal(
    partition: dict[str, tuple[str, ...]],
) -> dict[str, object] | None:
    counts: dict[str, int] = {}
    for names in partition.values():
        for name in names:
            counts[name] = counts.get(name, 0) + 1

    duplicates = sorted(name for name, count in counts.items() if count > 1)
    present = set(counts)
    missing = sorted(_MICRO_NODES - present)
    unexpected = sorted(present - _MICRO_NODES)

    if duplicates:
        reason = "partition-overlap"
    elif missing:
        reason = "partition-uncovered"
    elif unexpected:
        reason = "partition-unexpected"
    else:
        return None

    return {
        "status": "REFUSE",
        "reason": reason,
        "duplicates": duplicates,
        "missing": missing,
        "unexpected": unexpected,
    }


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
    serialized_partition = {
        macro_name: list(names)
        for macro_name, names in partition.items()
    }
    base_receipt = {
        "lift_id": lift_id,
        "partition": serialized_partition,
        "partition_rule": partition_rule,
        "preservation_target": preservation_target,
        "micro_receipt_refs": [edge["receipt_ref"] for edge in _MICRO_EDGES],
    }
    refusal = _partition_refusal(partition)
    if refusal is not None:
        return {**base_receipt, **refusal}

    return {
        **base_receipt,
        "macro_nodes": list(partition),
        "macro_edges": _macro_edges(partition),
    }


def _edge_membership(graph: dict[str, object]) -> set[tuple[tuple[str, str], ...]]:
    return {
        tuple(sorted(edge.items()))
        for edge in graph["macro_edges"]
    }


def _macro_graph_differs(left: dict[str, object], right: dict[str, object]) -> bool:
    """Compare already-labeled graph membership, not serialization order."""
    return (
        set(left["macro_nodes"]) != set(right["macro_nodes"])
        or _edge_membership(left) != _edge_membership(right)
    )


def _block_membership(partition: dict[str, list[str]]) -> set[frozenset[str]]:
    """Compare constituent blocks independently of their external labels."""
    return {frozenset(names) for names in partition.values()}


def _block_labels(partition: dict[str, list[str]]) -> set[str]:
    """Compare only the declared external labels on partition blocks."""
    return set(partition)


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
        else "NO_MACRO_GRAPH_DELTA_OBSERVED"
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
        else "NO_MACRO_GRAPH_DELTA_OBSERVED"
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

    same_labeled_content = not _macro_graph_differs(left, right)
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


def run_partition_change_same_graph_probe() -> dict[str, object]:
    """Preserve a block-membership delta that the induced labeled macro-graph cannot see."""
    left_partition = {"X": ("A", "C"), "Y": ("B", "D")}
    right_partition = {"X": ("A",), "Y": ("B", "C", "D")}
    lifts = [
        _lift_receipt(
            lift_id="left-membership",
            partition=left_partition,
            partition_rule="declared-left-membership",
            preservation_target="partition-membership",
        ),
        _lift_receipt(
            lift_id="right-membership",
            partition=right_partition,
            partition_rule="declared-right-membership",
            preservation_target="partition-membership",
        ),
    ]

    partition_changed = (
        _block_membership(lifts[0]["partition"])
        != _block_membership(lifts[1]["partition"])
    )
    macro_graph_changed = _macro_graph_differs(lifts[0], lifts[1])
    observation = (
        "PARTITION_CHANGE_WITHOUT_MACRO_GRAPH_CHANGE"
        if partition_changed and not macro_graph_changed
        else "PARTITION_GRAPH_CONTROL_FAILED"
    )
    return {
        "experiment": "PARTITION-CHANGE-SAME-GRAPH-001",
        "observation": observation,
        "partition_changed": partition_changed,
        "macro_graph_changed": macro_graph_changed,
        "lifts": lifts,
        "authority": "none",
    }


def run_block_relabel_control_probe() -> dict[str, object]:
    """Separate block-label delta from constituent block-membership delta."""
    left_partition = {"X": ["A", "C"], "Y": ["B", "D"]}
    right_partition = {"P": ["A", "C"], "Q": ["B", "D"]}

    block_membership_changed = (
        _block_membership(left_partition) != _block_membership(right_partition)
    )
    block_labels_changed = _block_labels(left_partition) != _block_labels(right_partition)
    observation = (
        "BLOCK_LABEL_DELTA_ONLY"
        if block_labels_changed and not block_membership_changed
        else "BLOCK_RELABEL_CONTROL_FAILED"
    )
    return {
        "experiment": "BLOCK-RELABEL-CONTROL-001",
        "observation": observation,
        "block_membership_changed": block_membership_changed,
        "block_labels_changed": block_labels_changed,
        "left_partition": left_partition,
        "right_partition": right_partition,
        "authority": "none",
    }


def run_invalid_partition_refusal_probe() -> dict[str, object]:
    """Refuse malformed partition-shaped inputs before macro projection."""
    overlap_partition = {"X": ("A", "B"), "Y": ("A", "C", "D")}
    uncovered_partition = {"X": ("A", "B"), "Y": ("C",)}
    cases = [
        _lift_receipt(
            lift_id="overlap-hostile",
            partition=overlap_partition,
            partition_rule="hostile-overlap",
            preservation_target="partition-validity",
        ),
        _lift_receipt(
            lift_id="uncovered-hostile",
            partition=uncovered_partition,
            partition_rule="hostile-uncovered",
            preservation_target="partition-validity",
        ),
    ]
    refused = all(case.get("status") == "REFUSE" for case in cases)
    observation = (
        "INVALID_PARTITIONS_REFUSED"
        if refused
        else "INVALID_PARTITION_REFUSAL_FAILED"
    )
    return {
        "experiment": "INVALID-PARTITION-REFUSAL-001",
        "observation": observation,
        "cases": cases,
        "authority": "none",
    }
