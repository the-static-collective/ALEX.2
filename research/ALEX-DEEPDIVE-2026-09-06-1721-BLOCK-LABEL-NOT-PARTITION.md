# ALEXDEEPDIVE — BLOCK-LABEL-NOT-PARTITION-001

**Status:** RESEARCH  
**Promotion:** none

## Ground
- **Question:** What is the single strongest live ALEX.2 research frontier after the newest PR #107 delta?
- **Desired consequence:** Preserve the smallest attributable discriminator without promoting experimental semantics into canon or runtime authority.
- **Stop condition:** Identify whether the newly implemented `PARTITION-CHANGE-SAME-GRAPH-001` closes the prior frontier; if so, pressure the smallest immediately exposed distinction and stop.
- **Corpus/date cut:** `the-static-collective/ALEX.2`, current `main` and draft PR #107 exact head `42293701e3fe9ae8d9a44b536c7629cc5c801f10`, inspected 2026-09-06 17:21 America/Chicago. External formal terminology limited to current SageMath set-partition documentation.
- **Authority/effect boundary:** Research only. No merge, runtime promotion, ontology promotion, evidence/support promotion, or authority expansion.
- **Task shape:** AUDIT
- **Formation trace active:** no

## Orientation boundary
The Static Collective GitBook Front Room was attempted first for orientation. Organization discovery succeeded, but the connected organization-content search operation was blocked by the tool safety layer when querying `Front Room`. This is **access fog**, not evidence about Front Room contents. No absence claim is made.

## Required governance read before consequential claims
Read at current repository state:
- `AGENTS.md`
- `skills/alex/SKILL.md`
- `skills/alex/references/research-receipt.md`

Retained laws include:

```text
discovery path != evidence path
agreement != independent corroboration
access != permission to redistribute
ALEX may discover/read/compare/propose; it does not decide canon
Promotion: none means no consequence is admitted without an owning gate
```

## World cut
### Included
1. Current `main` through `b7c93d56ae0a134416e222c01c2c3439243c4ac2` before this write.
2. Previous packet `research/ALEX-DEEPDIVE-2026-09-06-1123-NO-MATERIAL-DELTA-HOLD.md`.
3. Draft PR #107 exact head `42293701e3fe9ae8d9a44b536c7629cc5c801f10`.
4. Exact PR files:
   - `experiments/partition_swap.py`
   - `tests/test_partition_swap_experiment.py`
5. Exact comparison from prior inspected PR head `5ebd930a123ec958593c6b72ad38ae2de8104328` to current head.
6. SageMath current set-partition documentation: https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/set_partition.html

### Deliberately omitted
- Adjacent repos: no owner-crossing dependency is needed for this local comparator distinction.
- Older unrelated ALEX PRs: no current evidence displaced PR #107 as the strongest frontier.
- Generic graph-isomorphism machinery: not earned by the present partition-membership issue.
- Wolfram computation: the discriminator is finite set/block equality and requires no nontrivial symbolic or numerical check.

### Missing / inaccessible
- GitBook Front Room contents for this run.
- Exact-head CI conclusion: the commit status endpoint returned `pending` with zero legacy statuses at inspection time, so no GREEN claim is made here.

### Sufficiency
**Sufficient** for the narrow semantic audit of PR #107's new partition comparator. **Unresolved** for Front Room orientation content and final CI state.

## Discovery trace
This ledger explains why the path was taken; it is not evidentiary support.

1. Attempt Front Room orientation.
2. GitBook search operation blocked → record access fog.
3. Read ALEX governance files.
4. Inspect current `main` and open PRs by recency.
5. Observe PR #107 updated after the previous packet.
6. Compare prior head `5ebd930...` to current head `4229370...`: two commits ahead, only the experiment and its test changed.
7. Read exact current implementation and tests.
8. Observe that the prior `PARTITION-CHANGE-SAME-GRAPH-001` discriminator is now implemented.
9. Pressure only the newly introduced `_partition_membership()` semantics.

## Evidence path
### E1 — material PR delta
PR #107 is open/draft at exact head:

`42293701e3fe9ae8d9a44b536c7629cc5c801f10`

GitHub reports it updated at `2026-09-06T20:39:38Z`, after the prior ALEXDEEPDIVE packet. The exact compare from the previous inspected head `5ebd930...` reports two commits ahead and modifications only to:

- `experiments/partition_swap.py`
- `tests/test_partition_swap_experiment.py`

### E2 — previous frontier is implemented
The current experiment adds:

```python
def run_partition_change_same_graph_probe():
    ...
    partition_changed = (
        _partition_membership(lifts[0]["partition"])
        != _partition_membership(lifts[1]["partition"])
    )
    macro_graph_changed = _macro_graph_differs(lifts[0], lifts[1])
```

and returns:

```text
PARTITION_CHANGE_WITHOUT_MACRO_GRAPH_CHANGE
partition_changed: true
macro_graph_changed: false
```

The test freezes that exact split. This closes the previous scope mismatch: partition change and induced macro-graph change are now represented independently.

### E3 — new comparator includes block labels
The newly added comparator is:

```python
def _partition_membership(partition: dict[str, list[str]]) -> set[tuple[str, frozenset[str]]]:
    return {
        (macro_name, frozenset(names))
        for macro_name, names in partition.items()
    }
```

Therefore the macro/block name is part of partition equality.

### E4 — direct hostile control
Consider the same underlying blocks with only block labels changed:

```text
LEFT:
X = {A,C}
Y = {B,D}

RIGHT:
P = {A,C}
Q = {B,D}
```

Current `_partition_membership()` yields unequal sets because `X/Y != P/Q`, despite identical constituent blocks.

### E5 — external formal terminology
Current SageMath documentation defines an **unordered partition of a set** as a set of pairwise disjoint nonempty subsets whose union is the base set. Its set-partition representation is built from the blocks themselves; external names such as `X`, `Y`, `P`, `Q` are not part of the mathematical partition identity.

This external source supplies terminology/definition pressure only. It does not authorize ALEX semantics.

## Claims
| ID | Claim | Class | Supporting evidence path | Counterevidence / alternative | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #107 materially advanced after the previous packet. | observed | E1 | none found | supported |
| C2 | `PARTITION-CHANGE-SAME-GRAPH-001` now explicitly separates partition change from macro-graph change. | observed | E2 | CI final state was not established in this run. | supported as code/test content; execution status unresolved |
| C3 | `_partition_membership()` currently treats block-label changes as partition changes. | observed + direct evaluation | E3 + E4 | This is lawful if ALEX intentionally defines a **labeled partition receipt**, not an unlabeled set partition. | supported |
| C4 | In standard set-partition terminology, renaming only the external block identifiers does not create a new set partition. | scholarly/software-documentation claim | E5 | ALEX may deliberately use a stronger labeled object than the standard mathematical partition. | supported as terminology pressure |
| C5 | The next smallest discriminator is to separate **block-label delta** from **block-membership delta**. | proposal | C3 + C4 | If macro names are intentionally semantic identities, the contract should state that explicitly rather than call the comparator plain partition membership. | live |

## Contradictions and competing readings
### Reading A — mathematical partition semantics
`partition_changed` should answer whether the constituent blocks changed, independent of arbitrary macro-node names. Under this reading, the current comparator is over-sensitive.

### Reading B — labeled partition receipt semantics
ALEX may intend each macro name to be a declared identity-bearing label. Under that contract, `X:{A,C}` and `P:{A,C}` are intentionally different receipt objects even if they induce the same unlabeled partition.

### Consequence
The code does not yet distinguish these two meanings. The ambiguity is not evidence that either one is wrong; it means the field name `partition_changed` currently carries more semantics than are declared.

## Direct counterexample
Smallest hostile specimen:

```text
LEFT partition receipt:
X = {A,C}
Y = {B,D}

RIGHT partition receipt:
P = {A,C}
Q = {B,D}
```

No constituent changes block. Only the external macro names change.

Current result under `_partition_membership()`:

```text
partition_changed = true
```

Standard unlabeled set-partition reading:

```text
block_membership_changed = false
block_labels_changed = true
```

Therefore:

```text
BLOCK LABEL != BLOCK MEMBERSHIP
LABELED PARTITION RECEIPT != UNLABELED SET PARTITION
PARTITION DELTA MUST SAY WHICH OBJECT CHANGED
```

## Nearest boring explanation
This is most likely a **naming/modeling ambiguity**, not a deep combinatorics defect. The implementation needed stable macro names for receipts and simply included them in equality. The research risk appears only when that receipt-level equality is described with the broader term `partition_changed`.

## Dependency / independence
- This run depends on the exact PR #107 implementation and is a descendant of the prior partition-vs-macro-graph frontier.
- The new hostile specimen is a fresh discriminator derived from the newly introduced comparator; it is not independent corroboration of the earlier ALEXDEEPDIVE chain.
- SageMath is independent terminology pressure, not evidence about ALEX intent.

## Rights / egress
- Repository text was read and written through the connected GitHub surface.
- No source corpora, scans, private research material, or credentials were committed.
- No local page bytes were sent to external model providers.
- Public SageMath documentation was consulted only as external formal reference.
- Durable effect is limited to this new Markdown research packet.

## Residual fog
1. Whether macro-node names are intended as semantic identities or merely serialization labels is not explicitly declared by the inspected experimental contract.
2. Final exact-head CI state was unresolved at inspection time; no GREEN claim is promoted.
3. No downstream consumer search was opened because no consumer dependency is required to establish the comparator ambiguity itself.
4. Front Room orientation content remained inaccessible.

## Smallest next discriminators / repo-worthy moves
1. **`BLOCK-RELABEL-CONTROL-001`** — hold block contents fixed, rename only block identifiers, and emit separately:
   ```text
   block_membership_changed: false
   block_labels_changed: true
   ```
2. If block labels are intentionally identity-bearing, rename the current predicate/result toward **`labeled_partition_receipt_changed`** and document that it is stronger than mathematical set-partition equality.
3. Only if an actual consumer needs both semantics, retain two comparators; do not introduce a generic partition/graph framework yet.

## Finding
**THE PREVIOUS FRONTIER CLOSED; THE NEXT ONE IS LABEL IDENTITY.**

PR #107 now preserves `partition_changed` separately from `macro_graph_changed`. The immediately exposed boundary is that its partition comparator also includes macro-block names. The smallest next question is therefore not another graph question:

```text
DOES RENAMING A BLOCK CHANGE THE PARTITION,
OR ONLY THE LABELED RECEIPT?
```

ALEX should preserve whichever answer the owning contract chooses, but it should not let the two meanings silently collapse.

## Receipt
- **Created:** 2026-09-06 17:21 America/Chicago
- **Researcher/agent:** ALEXDEEPDIVE / ChatGPT
- **Tool/model boundary:** GitBook connector orientation attempt; GitHub connected repository reads/writes; public web documentation lookup; no Wolfram computation used
- **External byte egress:** none beyond repository text and public documentation accessed through connected/public research surfaces
- **Durable location:** `research/ALEX-DEEPDIVE-2026-09-06-1721-BLOCK-LABEL-NOT-PARTITION.md`
- **Promotion:** none
