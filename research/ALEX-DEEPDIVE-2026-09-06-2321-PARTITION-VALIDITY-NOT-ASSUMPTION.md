# ALEXDEEPDIVE — PARTITION-VALIDITY-NOT-ASSUMPTION-001

**Status:** RESEARCH  
**Promotion:** none

## Ground
- **Question:** What is the single strongest live ALEX.2 research frontier after PR #107 implemented `BLOCK-RELABEL-CONTROL-001`?
- **Desired consequence:** Preserve the smallest attributable discriminator that prevents an invalid partition-shaped receipt from being treated as a valid partition or failing as an untyped process error.
- **Stop condition:** Establish whether the new block-label/member split closes the previous frontier; if yes, audit only the immediately adjacent partition-input contract and stop.
- **Corpus/date cut:** `the-static-collective/ALEX.2`, current `main` before this write and draft PR #107 exact head `08b03ddccf71ab3598bb67e8152a6ec3afc9b9cb`, inspected 2026-09-06 23:21 America/Chicago. External terminology limited to current NetworkX partition/quotient documentation.
- **Authority/effect boundary:** Research only. No merge, runtime promotion, ontology promotion, evidence/support promotion, or authority expansion.
- **Task shape:** AUDIT
- **Formation trace active:** no

## Orientation boundary
The Static Collective GitBook Front Room was attempted first for orientation. The connected organization-list operation was blocked by the tool safety layer, and a narrow public-web search did not resolve the Front Room. This is **access fog**, not evidence about Front Room contents. No absence claim is made.

## Required governance read before consequential claims
Read at current repository state:
- `AGENTS.md`
- `skills/alex/SKILL.md`
- `skills/alex/references/research-receipt.md`

Retained laws material to this pass include:

```text
discovery path != evidence path
search miss != absence
ALEX may discover/read/compare/propose; it does not decide canon
refusal paths are first-class outcomes
Promotion: none means no consequence is admitted without an owning gate
```

## World cut
### Included
1. Current ALEX.2 `main` through `7cbc963d4b30ae09a79792c804914389fb156f1a` before this write.
2. Previous packet `research/ALEX-DEEPDIVE-2026-09-06-1721-BLOCK-LABEL-NOT-PARTITION.md`.
3. Draft PR #107 exact head `08b03ddccf71ab3598bb67e8152a6ec3afc9b9cb`.
4. Exact PR files:
   - `experiments/partition_swap.py`
   - `tests/test_partition_swap_experiment.py`
5. Exact compare from prior inspected PR head `5ebd930a123ec958593c6b72ad38ae2de8104328` to current head.
6. Exact-head GitHub Actions check run for `08b03dd...`.
7. NetworkX quotient/partition documentation as independent terminology and failure-behavior pressure.

### Deliberately omitted
- Adjacent repos: no owner-crossing dependency is needed to establish the local input-contract problem.
- Older unrelated ALEX PRs: no current evidence displaced PR #107 as the strongest frontier.
- Generic graph-isomorphism machinery: not earned.
- Wolfram computation: the discriminator is a finite coverage/disjointness contract and requires no nontrivial symbolic, statistical, temporal, geometric, or scientific computation.

### Missing / inaccessible
- GitBook Front Room contents for this run.
- Downstream consumers of this experimental helper were not searched because the local contract can be established without expanding the traversal.

### Sufficiency
**Sufficient** for the narrow audit of PR #107's partition-input semantics. **Unresolved** for Front Room orientation content and downstream adoption intent.

## Discovery trace
This ledger records why the path was taken; it is not evidentiary support.

1. Attempt Front Room orientation.
2. Connected operation blocked; narrow public search fails to resolve room → record access fog.
3. Read ALEX governance files.
4. Inspect current `main`, previous packet, and PR #107 exact head.
5. Compare prior inspected head `5ebd930...` with current head `08b03dd...`.
6. Observe four commits ahead, including `BLOCK-RELABEL-CONTROL-001` RED then fix.
7. Read exact current experiment and tests.
8. Confirm prior label-vs-membership ambiguity is now explicitly represented.
9. Audit only the immediately upstream assumption: whether objects called `partition` are validated before graph lifting/comparison.
10. Check current external quotient-graph contract for the nearest boring definition and failure behavior.

## Evidence path
### E1 — material PR delta
PR #107 is open/draft at exact head:

`08b03ddccf71ab3598bb67e8152a6ec3afc9b9cb`

The compare from `5ebd930...` reports four commits ahead. The newest two are:

- `c015d3702834fd5e667cce202d32f3048482de27` — `test: freeze block relabel control RED`
- `08b03ddccf71ab3598bb67e8152a6ec3afc9b9cb` — `fix: distinguish block labels from partition membership`

Only the experiment and its test are modified in this compare.

### E2 — previous frontier is implemented
Current code adds separate helpers:

```python
def _block_membership(partition):
    return {frozenset(names) for names in partition.values()}


def _block_labels(partition):
    return set(partition)
```

and `run_block_relabel_control_probe()` returns independently:

```text
block_membership_changed: false
block_labels_changed: true
observation: BLOCK_LABEL_DELTA_ONLY
```

The exact-head test freezes that result. This closes the previous `BLOCK-LABEL-NOT-PARTITION-001` frontier at the experimental level.

### E3 — exact-head CI is green
GitHub Actions reports one exact-head check run named `contract` for `08b03dd...`; it completed with conclusion `success` at `2026-09-07T03:38:51Z`.

This establishes carrier/test success only. It does not promote the experiment's semantics into authority.

### E4 — partition validity is assumed, not checked
`_macro_edges(partition)` constructs constituent membership with:

```python
membership = {
    name: macro_name
    for macro_name, names in partition.items()
    for name in names
}
```

No preceding validation establishes that:

1. every micro constituent appears in exactly one block;
2. no constituent appears in multiple blocks;
3. the declared blocks cover the micro-node universe used by `_MICRO_EDGES`.

The current tests exercise only valid partitions.

### E5 — overlap can be silently resolved by dictionary overwrite
For an overlap-shaped receipt such as:

```text
X = {A,B}
Y = {A,C,D}
```

the dictionary comprehension assigns `A` twice. Python mapping construction retains one value for the duplicate key; therefore one block assignment for `A` silently wins in the `membership` projection rather than producing an explicit invalid-partition outcome.

The resulting macro projection can therefore depend on construction order of the labeled blocks even though block serialization order was previously removed from graph comparison semantics.

This is not a claim that the current fixed specimens are invalid; they are valid. It identifies an unguarded input class.

### E6 — omission becomes a raw lookup failure
For an omission-shaped receipt that leaves a micro-edge endpoint uncovered, `_macro_edges()` later executes:

```python
source = membership[edge["from"]]
target = membership[edge["to"]]
```

An uncovered endpoint is therefore not represented as an ALEX refusal receipt; it becomes an ordinary missing-key exception.

This matters because `AGENTS.md` explicitly requires refusal paths to be tested as first-class outcomes when implementation begins.

### E7 — independent formal/API pressure
Current NetworkX quotient-graph documentation states that a dict/list partition must be a **valid partition**: each graph node must occur in exactly one block. The implementation checks partition validity and raises a specific graph exception when that condition fails.

NetworkX is not imported as ALEX authority. It supplies the nearest boring graph-library contract for the same object name and operation class.

## Claims
| ID | Claim | Class | Supporting evidence path | Counterevidence / alternative | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #107 materially advanced after the previous packet. | observed | E1 | none found | supported |
| C2 | `BLOCK-RELABEL-CONTROL-001` now separates block labels from constituent block membership. | observed | E2 | experimental only; no authority promotion | supported |
| C3 | Exact-head `contract` CI succeeded for `08b03dd...`. | observed | E3 | green carrier != semantic authority | supported |
| C4 | The current lift path does not validate disjointness or coverage before treating an input as a partition. | observed | E4 | fixed internal specimens happen to satisfy the contract | supported |
| C5 | Overlapping block membership can be collapsed by the local membership dictionary instead of refused. | inference directly from code semantics | E4 + E5 | no public caller currently demonstrated to pass hostile input | supported as reachable helper behavior; consumer exposure unresolved |
| C6 | Missing coverage can surface as a raw lookup failure rather than an attributable refusal outcome. | inference directly from code semantics | E4 + E6 | a caller may validate elsewhere, but no such local guard is present in the inspected experiment | supported locally; external guard unresolved |
| C7 | The smallest next discriminator is partition validity/refusal, not another equality comparator. | proposal | C4–C6 + governance refusal law | if this experiment is permanently closed over immutable valid fixtures, validation may be unnecessary; then that closure should be explicit | live |

## Contradictions and competing readings
### Reading A — helper is a fixture-local experiment
All partitions are hard-coded and valid. On this reading, general input validation is unnecessary because `_macro_edges()` is not a public/general partition API.

### Reading B — helper semantics are becoming reusable
PR #107 has successively generalized comparison semantics across edge lists, nodes, order, partition membership, and labels. On this reading, the word `partition` is beginning to carry a reusable contract, and invalid partition-shaped values should not silently enter the graph-lift path.

### Consequence
The evidence does **not** earn a generic partition framework. It does earn one explicit discriminator that establishes whether invalid partition-shaped input is outside the experiment's domain or a first-class REFUSE case.

## Direct counterexamples
### Overlap hostile specimen

```text
MICRO universe used by receipts: {A,B,C,D}

X = {A,B}
Y = {A,C,D}
```

`A` belongs to two declared blocks. A valid partition cannot contain that overlap. Current local membership construction can silently retain one `A -> block` assignment.

### Coverage hostile specimen

```text
X = {A,B}
Y = {C}
# D omitted
```

When processing the fixed `C -> D` micro receipt, `membership["D"]` has no entry. Current behavior is an ordinary lookup failure, not a typed experimental observation or attributable `REFUSE` result.

Therefore:

```text
PARTITION-SHAPED DATA != VALID PARTITION
VALID COMPARISON != VALID INPUT
SILENT OVERWRITE != REFUSAL
RAW EXCEPTION != ATTRIBUTABLE REFUSAL RECEIPT
```

## Nearest boring explanation
This is most likely **fixture-local code gradually acquiring reusable semantics**. The original experiment did not need validation because every input was authored in the same file. Successive discriminators have made the helper names and outputs increasingly general without yet creating an explicit domain boundary.

No deeper graph-theoretic defect is required to explain the gap.

## Dependency / independence
- This run is a descendant of the prior comparator-audit chain; it is not independent corroboration.
- The hostile overlap/coverage specimens are newly derived from the now-explicit partition semantics.
- NetworkX documentation is independent terminology/API-behavior pressure, not evidence about Static Collective intent.
- Exact-head CI is independent execution evidence for the carrier, but it does not test the hostile validity class identified here.

## Rights / egress
- Repository text was read and written through the connected GitHub surface.
- No source corpora, scans, private research material, credentials, or copyrighted source bodies were committed.
- No local page bytes were sent to external model providers.
- Public NetworkX documentation was consulted as external formal/API reference only.
- Durable effect is limited to this new Markdown research packet.

## Residual fog
1. Whether `_macro_edges()` is intended to remain permanently closed over internal fixtures or become a reusable experimental helper is not explicitly declared.
2. No downstream consumer was opened, by design; therefore external pre-validation remains unknown.
3. Empty-block semantics were not pursued because overlap and coverage already provide smaller, load-bearing hostile cases.
4. Front Room orientation content remained inaccessible.
5. No claim is made that NetworkX's exact exception model should be adopted; only the validity boundary is relevant.

## Smallest next discriminators / repo-worthy moves
1. **`INVALID-PARTITION-REFUSAL-001`** — freeze one overlap case and one uncovered-node case. Require a first-class non-authoritative refusal/result before `_macro_edges()` constructs a quotient projection.
2. If this experiment is intentionally fixture-closed, make that domain explicit in the helper/receipt contract and test that only the frozen micro-node universe is admitted; do not build a generic validator.
3. Only if a real caller needs reusable partition input, add the smallest local validator for **exactly-one-block-per-constituent** and preserve the refusal reason (`OVERLAP`, `UNCOVERED`, optionally `EXTRANEOUS`) separately from graph comparison.

## Finding
**THE LABEL FRONTIER CLOSED; THE NEXT FRONTIER IS INPUT VALIDITY.**

PR #107 now correctly distinguishes block-label change from block-membership change. But the experiment still crosses one unguarded boundary before all those comparators:

```text
IT CALLS A MAPPING A PARTITION
BEFORE PROVING IT IS A PARTITION.
```

For the current frozen fixtures this causes no failure. For hostile or reusable input, overlap can be silently collapsed and missing coverage can become an untyped lookup exception. Under ALEX's own implementation law, the next smallest useful discriminator is therefore not another graph-equivalence test but a refusal test.

```text
PARTITION-SHAPED DATA != VALID PARTITION
VALIDITY PRECEDES QUOTIENT COMPARISON
REFUSAL IS A RESULT, NOT A CRASH
```

## Receipt
- **Created:** 2026-09-06 23:21 America/Chicago
- **Researcher/agent:** ALEXDEEPDIVE / ChatGPT
- **Tool/model boundary:** GitBook connector orientation attempt; GitHub connected repository reads/writes; public web documentation lookup; no Wolfram computation used
- **External byte egress:** none beyond repository text and public documentation accessed through connected/public research surfaces
- **Durable location:** `research/ALEX-DEEPDIVE-2026-09-06-2321-PARTITION-VALIDITY-NOT-ASSUMPTION.md`
- **Promotion:** none
