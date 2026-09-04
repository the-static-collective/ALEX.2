# ALEXDEEPDIVE — EDGE-LIST-NOT-GRAPH-001

Status: **RESEARCH**  
Promotion: **none**

## Ground
- Question: What is the strongest newly revealed ALEX frontier since `REPRESENTATION-NOT-STRUCTURE-001`, given the new `RELABEL-CONTROL-001` commits on draft PR #99?
- Desired consequence: Preserve the successful relabeling correction while identifying the smallest remaining false structural-equivalence class in the current experiment.
- Stop condition: One exact hostile specimen plus one bounded repo-worthy discriminator; no generic graph runtime unless forced.
- Corpus/date/language/geography: ALEX.2 `main` and draft PR #99 as of 2026-09-04; current NetworkX documentation only as external methodological pressure.
- Authority/effect boundary: Research audit only. No merge, runtime promotion, graph-library dependency, ontology admission, historical claim, or owning-world authority.
- Task shape: **AUDIT**
- Formation trace active: **yes**, only to preserve why this newly changed PR was selected. Discovery trace remains separate from evidence path.

## Front Room orientation
The Static Collective GitBook organization was reached first, but Front Room content search was blocked by the connected surface during this run. This is recorded as access fog only. No substitute GitBook content was treated as Front Room orientation or as evidence.

## Governing ALEX constraints read before claim formation
- `ALEX.2/AGENTS.md`: preserve object/carrier and evidence/interpretation/proposal/admitted-claim distinctions; discovery path remains distinct from evidence path; ALEX does not manufacture source authority.
- `skills/alex/SKILL.md`: use the smallest adequate research shape, keep direct counterexamples and nearest boring explanations visible, and do not promote an experiment beyond what its exact witness establishes.
- `skills/alex/references/research-receipt.md`: a durable receipt testifies to this run only; `Promotion: none` keeps the result outside canon/runtime authority.

## World cut
### Included
- `main@d64e91dd79287cf06e5f4d355acebf067d3b36bf` — prior packet `REPRESENTATION-NOT-STRUCTURE-001`.
- Draft PR #99 current head `0511a8a44395ee2fd0d5f43ca804d195e0d0975d`.
- New PR #99 commits after the prior audited head:
  - `8d7b1bcbde92fdb1b9c98013354c2b49fbefedec` — `test: define RELABEL-CONTROL-001 discriminator`.
  - `0511a8a44395ee2fd0d5f43ca804d195e0d0975d` — `experiment: add RELABEL-CONTROL-001`.
- PR #99 files:
  - `experiments/partition_swap.py`
  - `tests/test_partition_swap_experiment.py`
- Current NetworkX graph/isomorphism documentation as external pressure.

### Deliberately omitted
- PR #97 WTC research: not needed for this graph-representation boundary.
- PR #92 and older executable seams: no stronger newly revealed delta than PR #99's exact completion of the previous discriminator.
- LOADOUT, 3rdi, Dogram: not needed for this bounded structural audit.
- Generic canonical labeling, VF2 integration, graph hashes, or community detection: not earned.

### Missing/inaccessible
- GitBook Front Room contents: connector search was blocked in this run.

Sufficiency: **sufficient for the bounded audit**.

## Discovery trace — why this door was chosen
| ID | From | To | Move | Role | Reason |
| --- | --- | --- | --- | --- | --- |
| D1 | prior `REPRESENTATION-NOT-STRUCTURE-001` | PR #99 new commits | replay prior next discriminator | motive | `RELABEL-CONTROL-001` was the exact smallest next move named by the prior packet and has now landed on the draft branch |
| D2 | relabel control | `macro_edges` representation | inspect what the control actually compares | discriminator | the new control correctly separates a pure node-name serialization delta from the frozen structural delta |
| D3 | `macro_edges` only | isolated macro-nodes | adversarial counterexample | counterevidence | an edge list does not encode isolated nodes, while the lift's partition does preserve them elsewhere |

Nothing in this discovery trace independently supports the final claim; support comes from the evidence path below.

## Evidence path
### E1 — the prior discriminator was implemented
PR #99 now contains `run_relabel_control_probe()`. It compares:

```text
X --appoints--> Y
P --appoints--> Q
```

under the declared relabeling `X -> P`, `Y -> Q` and returns `SERIALIZATION_DELTA_ONLY` when the renamed left edge equals the right edge. The test requires both the pre-relabel inequality and post-relabel equality while preserving `authority: none`.

This is a successful implementation of the prior packet's `RELABEL-CONTROL-001` request.

Repository witness: https://github.com/the-static-collective/ALEX.2/pull/99  
Exact head: `0511a8a44395ee2fd0d5f43ca804d195e0d0975d`

### E2 — the current partition observation still compares only edge lists
`run_partition_swap_probe()` computes each lift's `partition` and `macro_edges`, but its observation predicate is:

```python
observation = (
    "PARTITION_DEPENDENT_MACRO_GRAPH"
    if lifts[0]["macro_edges"] != lifts[1]["macro_edges"]
    else "NO_PARTITION_DELTA_OBSERVED"
)
```

The complete lift output does preserve partition membership, so macro-node existence has not vanished from the receipt. But the **classification predicate** ignores that node information.

### E3 — direct hostile false-negative
Hold the current four micro-names and two receipts fixed:

```text
A --appoints--> B
C --appoints--> D
```

Compare two declared lifts:

```text
Lift L2:
  P = {A,B}
  Q = {C,D}

Lift L1:
  Z = {A,B,C,D}
```

In both lifts every micro-edge is internal to a macro block, so:

```text
macro_edges(L2) = []
macro_edges(L1) = []
```

The current edge-list comparison therefore yields no partition delta.

But the quotient structures are not isomorphic as graphs because:

```text
|V(L2)| = 2
|V(L1)| = 1
|E(L2)| = |E(L1)| = 0
```

Graph isomorphism preserves vertex count. Thus identical empty edge lists can hide a real structural difference.

This counterexample requires no probabilistic, symbolic, or external computation.

### E4 — external methodological pressure
Current NetworkX documentation defines a graph as a collection of nodes together with a collection of edges. Its `Graph`/`DiGraph` objects store nodes and edges separately, and its graph-isomorphism interface tests graph structure while optionally applying declared node/edge semantic matchers.

Primary/current documentation:
- https://networkx.org/documentation/stable/reference/introduction.html
- https://networkx.org/documentation/stable/reference/classes/graph.html
- https://networkx.org/documentation/networkx-3.4.2/reference/algorithms/generated/networkx.algorithms.isomorphism.is_isomorphic.html

These sources pressure the representation boundary only. They do not imply that ALEX should add NetworkX as a dependency.

## Claims
| ID | Claim | Class | Supporting evidence path | Counterevidence | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #99 now implements the prior `RELABEL-CONTROL-001` and correctly distinguishes its pure renaming specimen from the original partition swap. | observed | E1 | none found | supported at exact PR head |
| C2 | The current `PARTITION-SWAP-001` classification predicate compares only `macro_edges`, even though the receipt also carries partition membership. | observed | E2 | none | supported |
| C3 | Equal macro-edge lists do not generally imply equal/isomorphic macro-graphs because isolated macro-nodes can differ. | inference from direct counterexample | E3 -> E4 | would not matter if the experiment's contract intentionally defines its observation as edge-projection delta rather than graph delta | supported with scope qualifier |
| C4 | The smallest remaining guardrail is to include macro-node existence/count in the structural discriminator or rename the observation to state explicitly that it witnesses edge-projection delta only. | proposal | C2+C3 | the experiment may remain a one-off whose only positive specimen already differs by edge count | supported as bounded next move, not runtime mandate |

## Contradictions and competing readings
### Reading A — `macro_graph` means graph structure
Then the current negative branch is too strong: `macro_edges` equality can miss isolated-node differences. The comparison contract must include the macro-node set, even if only via a simple invariant such as node count for this specimen family.

### Reading B — the experiment only measures cross-block edge projection
Then the implementation can remain edge-only, but `PARTITION_DEPENDENT_MACRO_GRAPH` / `NO_PARTITION_DELTA_OBSERVED` overstates the predicate. A narrower name such as `PARTITION_DEPENDENT_MACRO_EDGES` would match what was actually measured.

### Reading C — frozen specimen only
The current positive specimen remains valid because one lift has one macro-edge and the other has none. If no generic caller consumes the negative branch, documentation may be enough. This is the nearest boring explanation and still argues against adding a graph library.

## Dependency / independence
- E1 and E2 are observations from the same PR branch; the test and implementation are not independent corroboration.
- E3 is an independently constructed mathematical counterexample against the predicate's general negative reading.
- NetworkX documentation is independent external methodological precedent but is not evidence of ALEX intent.

## Pressure
- Direct counterexample: one-node empty quotient versus two-node empty quotient; identical `macro_edges=[]`, non-isomorphic node sets.
- Nearest boring explanation: PR #99 is a bounded one-off experiment and may never need a reusable graph-equivalence predicate.
- Representation check: the lift receipt already carries `partition`, so the missing information is not destroyed; it is omitted only from the classification predicate.
- API/framework claim verification: graph/isomorphism behavior checked against current NetworkX project documentation, not a third-party summary.
- Wolfram: not used; the decisive invariant is exact vertex count and requires no computational authority.
- Rights/egress: only public repository text and public NetworkX documentation were used externally. No private corpora, credentials, or page bytes were egressed.

## Finding

`RELABEL-CONTROL-001` successfully kills the prior ambiguity that every serialized label difference is structural. The newly exposed boundary is different:

```text
EDGE LIST != GRAPH
```

More precisely:

```text
same macro_edges
!=
same macro-node set
!=
isomorphic macro-graph
```

The present PR #99 positive specimen still survives untouched. The hazard is the **negative classification**: `NO_PARTITION_DELTA_OBSERVED` can be emitted when two lifts have identical cross-block edges but structurally different isolated macro-node sets.

The receipt already contains enough information to avoid this error because each lift preserves its declared `partition`. No new graph engine is required to freeze the next discriminator.

## Smallest next discriminators / repo-worthy moves
1. **ISOLATED-NODE-CONTROL-001** — same micro receipts, compare `{A,B}|{C,D}` against `{A,B,C,D}`; require the experiment not to call identical empty macro-edge lists `NO_PARTITION_DELTA_OBSERVED` if its claimed object is the macro-graph.
2. **Name the measured object** — either compare both declared macro-node sets and macro-edges, or rename the observation contract to `MACRO_EDGE_PROJECTION_DELTA` so isolated-node structure is explicitly outside scope.
3. **Stop if fixed-specimen only** — if no caller needs general graph equivalence, freeze the control/documentation and do not add NetworkX, canonicalization, or graph hashing.

## Compact law

```text
A GRAPH HAS NODES AND EDGES.
AN EDGE PROJECTION CAN FORGET A NODE.
A RECEIPT MAY PRESERVE WHAT A PREDICATE IGNORES.
NAME THE OBJECT THAT WAS ACTUALLY COMPARED.
```

## Residual fog
- Whether future N↔V↔S lifts treat isolated macro-nodes as semantically meaningful is not yet declared.
- Whether `PARTITION-SWAP-001` will remain a fixed hostile specimen or become a reusable comparison surface remains unresolved.
- GitBook Front Room orientation remained inaccessible through the connected search surface; no absence claim is inferred.

## Receipt
- Created: 2026-09-04 17:29 America/Chicago
- Researcher/agent: ChatGPT / ALEXDEEPDIVE
- ALEX main inspected: `d64e91dd79287cf06e5f4d355acebf067d3b36bf`
- PR #99 head inspected: `0511a8a44395ee2fd0d5f43ca804d195e0d0975d`
- Tool/model boundary: GitBook connected surface attempted first for orientation; GitHub connected repository reads/writes; public web for current NetworkX documentation; no Wolfram computation used.
- External byte egress: public repository text/documentation only; no private/local corpus bytes.
- Durable location: `research/ALEX-DEEPDIVE-2026-09-04-1729-EDGE-LIST-NOT-GRAPH.md`
- Promotion: **none**
