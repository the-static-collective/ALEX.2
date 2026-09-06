# ALEXDEEPDIVE — PARTITION-NOT-QUOTIENT-001

Status: **RESEARCH**  
Promotion: **none**

## Ground
- Question: What is the strongest live ALEX frontier newly revealed since `CONTROL-NOT-COMPARATOR-001`?
- Desired consequence: identify the smallest remaining discriminator without widening runtime authority or graph semantics.
- Stop condition: one materially new, exact-head frontier with a direct counterexample and a bounded next move.
- Corpus: `the-static-collective/ALEX.2` current `main` plus draft PR #107 exact head; NetworkX quotient-graph documentation only as external terminology pressure.
- Authority and effect boundary: research packet only; no canon, runtime, merge, ontology, or authority promotion.
- Task shape: **AUDIT**.
- Formation trace active: no.

## World cut
### Included
- `main@f9f695cc598dbf69350dbad8e003f00a6123ae4d`
- PR #107 `agent/crater-smash-order-swap-control@5ebd930a123ec958593c6b72ad38ae2de8104328`
- `AGENTS.md` on current main
- `skills/alex/SKILL.md` on current main
- `skills/alex/references/research-receipt.md` on current main
- NetworkX quotient-graph documentation: <https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.minors.quotient_graph.html>

### Deliberately omitted
- Adjacent repos: no owner-local dependency became necessary.
- WTC/Darkness Visible research: no stronger fresh delta than PR #107.
- Older ALEX experimental branches: inspected only through open-PR recency sufficient to establish that #107 is the current moving seam.

### Missing / inaccessible
- Static Collective GitBook Front Room orientation was attempted first. The connected organization operation was blocked by the tool safety layer. This is **access fog**, not evidence about Front Room contents.

Sufficiency: **sufficient for this bounded audit**.

## Newly observed delta

Since the previous packet, PR #107 moved from the earlier control-only state to exact head `5ebd930a123ec958593c6b72ad38ae2de8104328`.

At that head:

```python
def _macro_graph_differs(left, right):
    return (
        set(left["macro_nodes"]) != set(right["macro_nodes"])
        or _edge_membership(left) != _edge_membership(right)
    )
```

and `ORDER-SWAP-CONTROL-001` now calls that shared comparator directly. The tests also require `_macro_graph_differs(result["left"], result["right"])` to be false while preserving genuine node/edge-delta positives.

Therefore the previous frontier is closed at this branch head:

```text
CONTROL BINDS COMPARATOR
SERIALIZATION ORDER != LABELED GRAPH MEMBERSHIP
```

This is a real semantic repair, not merely another specimen.

## Strongest surviving frontier

The experiment still returns:

```text
NO_PARTITION_DELTA_OBSERVED
```

when `_macro_graph_differs(...)` is false.

But `_macro_graph_differs` compares the **induced labeled macro-graph**, not the underlying partition itself.

A partition is an input to the quotient/lift. Different partitions can induce the same macro-node labels and macro-edge membership.

Direct hostile specimen using the experiment's fixed micro edges:

```text
A --appoints--> B
C --appoints--> D
```

Partition L:

```text
X = {A,C}
Y = {B,D}
```

Partition R:

```text
X = {A}
Y = {B,C,D}
```

Both induce the same current simple typed macro-graph:

```text
macro_nodes = {X,Y}
macro_edges = {X --appoints/S--> Y}
```

Yet the partitions are plainly different: `C` moved from `X` to `Y`.

Therefore:

```text
SAME MACRO-GRAPH
!=
SAME PARTITION

NO MACRO-GRAPH DELTA OBSERVED
!=
NO PARTITION DELTA OBSERVED
```

## External terminology pressure

NetworkX documents `quotient_graph(G, partition, ...)` as returning a quotient graph **under a specified partition/equivalence relation**, with the partition blocks forming the nodes of the returned graph. This independently preserves the conceptual distinction between the partition supplied and the quotient graph produced from it.

This external source is terminology/structure pressure only. ALEX does not depend on NetworkX and no external graph runtime is proposed.

## Claims

| ID | Claim | Class | Evidence path | Counterevidence | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #107 now makes the order-swap control pass through `_macro_graph_differs`. | observed | PR #107 exact-head source + tests | none found | supported at exact head |
| C2 | `_macro_graph_differs` compares macro-node and typed-edge membership, not partition membership. | observed | exact-head function body | none | supported |
| C3 | Two different partitions can induce the same macro-graph under the experiment's current projection. | inference from explicit counterexample | fixed micro-edge fixture + two declared partitions | would fail if their induced graph differed; it does not under current rules | supported for specimen |
| C4 | `NO_PARTITION_DELTA_OBSERVED` overstates what the comparator establishes. | inference | C2 + C3 | label could be defended only if "partition delta" were intentionally defined as quotient-graph delta; no such definition was found | supported, scoped |
| C5 | ALEX needs a general partition-equivalence or graph-isomorphism engine. | proposal | none | current problem is fixable by naming or one control | **not earned** |

## Contradictions and alternatives

### Reading A — narrow naming bug
The comparator is correct for its intended job; only the negative observation name is too broad.

This is the nearest boring explanation and currently the preferred reading.

### Reading B — intended observational equivalence
The experiment may intend to identify partitions only up to their induced macro-graph. If so, identical quotient output is legitimately “no delta” **at the chosen observational surface**, but the receipt should say that explicitly.

### Reading C — partition identity is semantically material
If downstream work needs to distinguish two lifts with the same quotient graph but different constituent membership, the receipt needs a separate partition-level comparator. That requirement is not yet established.

## Pressure
- Quote-to-page check: not applicable; repository source inspected directly.
- Visual/coordinate check: not applicable.
- Edition identity: exact Git SHA pinned.
- OCR/translation: not applicable.
- Independence/lineage: PR #107 descends from the same PARTITION-SWAP witness family; this is not independent corroboration.
- Direct counterexample: L/R partitions above.
- Nearest boring explanation: observation-name overreach rather than algorithmic failure.
- Replay impersonation: green control closes only the comparator-order issue; it does not prove all partition semantics are represented.
- Ghost promotion: no prior packet is treated as canon; this packet is a descendant audit only.

## Discovery trace boundary

Discovery motive: previous packet left `CONTROL-BINDS-COMPARATOR-001` unresolved.  
Evidence path: exact PR #107 source/test changes show that issue is now repaired; inspection of the resulting negative observation exposed the partition/quotient distinction.

The previous frontier explains **why this file was inspected**. It is not evidence for the new claim.

## Residual fog
- CI commit status endpoint for exact head returned `pending` with zero legacy statuses; no exact-head CI success is claimed here.
- PR #107 remains draft and diverged from current main; branch correctness does not imply landing authority.
- It is unresolved whether downstream consumers care about partition identity when quotient outputs coincide.
- No external scholarly claim is needed beyond quotient-graph terminology; NetworkX is not imported as authority over ALEX semantics.

## Smallest next discriminators
1. **PARTITION-CHANGE-SAME-GRAPH-001** — freeze the L/R specimen above; require the receipt to preserve `partition_changed: true` while `macro_graph_changed: false`.
2. Rename the negative macro-graph observation to **`NO_MACRO_GRAPH_DELTA_OBSERVED`** unless a stronger partition-level comparison is deliberately added.
3. Only if a real consumer needs it, add a separate partition-membership comparison. Do **not** widen `_macro_graph_differs` to conflate lift identity with graph identity.

## Compact law

```text
PARTITION != QUOTIENT GRAPH

PARTITION CHANGE MAY SURVIVE
WITHOUT MACRO-GRAPH CHANGE.

THE COMPARATOR NOW SAYS WHAT THE GRAPH DID.
THE RECEIPT MUST NOT PRETEND IT SAW MORE.
```

## Receipt
- Created: 2026-09-05 23:24 America/Chicago
- Researcher/agent: ALEXDEEPDIVE scheduled research pass
- Tool/model boundary: GitBook connector orientation attempt; GitHub repository/PR exact-head reads; public NetworkX documentation search. No local corpus or private bytes exported.
- External byte egress: repository source already hosted on GitHub; no local/private source corpus sent to external models.
- Durable location: `research/ALEX-DEEPDIVE-2026-09-05-2324-PARTITION-NOT-QUOTIENT.md`
- Promotion: **none**
