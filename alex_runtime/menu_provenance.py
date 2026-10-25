from __future__ import annotations

from collections.abc import Iterable, Mapping


def summarize_menu(
    representative_successors: Mapping[str, Iterable[str]],
) -> dict[str, object]:
    """Summarize representative-local possibility without universalizing the union."""
    if not representative_successors:
        raise ValueError("representative family must be non-empty")

    representatives = {
        str(representative): sorted(set(successors))
        for representative, successors in representative_successors.items()
    }
    successor_sets = [set(successors) for successors in representatives.values()]
    may = set().union(*successor_sets)
    must = set.intersection(*successor_sets)

    contributors = {
        successor: sorted(
            representative
            for representative, successors in representatives.items()
            if successor in successors
        )
        for successor in sorted(may)
    }

    return {
        "experiment": "MENU-PROVENANCE-001",
        "may": sorted(may),
        "must": sorted(must),
        "contributors": contributors,
        "representatives": dict(sorted(representatives.items())),
        "authority": "none",
    }
