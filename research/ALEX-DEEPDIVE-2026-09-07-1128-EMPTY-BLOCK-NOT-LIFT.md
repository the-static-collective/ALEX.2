# ALEXDEEPDIVE — EMPTY-BLOCK-NOT-LIFT-001

Status: **RESEARCH**  
Promotion: **none**

## Ground

- **Question:** After `INVALID-PARTITION-REFUSAL-001` landed on draft PR #107, what is the smallest still-live validity boundary in the partition-swap experimental carrier?
- **Desired consequence:** identify one falsifiable next discriminator without widening ALEX runtime authority or importing a generic graph ontology.
- **Stop condition:** stop once the new exact head is audited against the prior validity frontier and one smaller hostile specimen is established.
- **Corpus/date/language/geography:** `the-static-collective/ALEX.2`, exact repository and PR heads inspected 2026-09-07; current NetworkX 3.6.1 documentation/source; Wolfram MathWorld set-partition terminology.
- **Authority/effect boundary:** research only. No canon, runtime, merge, evidence, support, or owner authority is granted here.
- **Task shape:** `AUDIT`
- **Formation trace active:** no.

## World cut

### Included

- ALEX.2 `AGENTS.md` on default branch.
- ALEX portable skill: `skills/alex/SKILL.md`.
- ALEX research receipt contract: `skills/alex/references/research-receipt.md`.
- Current `main` observed before this packet: `3d56cbc191315d799c8e48faf0f944cbfc3687d8`.
- Draft PR #107 exact head: `4ade4542f6fa5603d608b604436e66a0ac61da69`.
- PR #107 files `experiments/partition_swap.py` and `tests/test_partition_swap_experiment.py` at that exact head.
- Exact-head GitHub Actions check run for `4ade4542...`.
- NetworkX 3.6.1 `is_partition` documentation/source.
- Wolfram MathWorld, *Stirling Number of the Second Kind*, for the conventional nonempty-block formulation of set partitions.

### Deliberately omitted

No adjacent Static Collective repository was opened. The newly revealed evidence is fully local to ALEX.2 PR #107; traversal outward would not improve this discriminator.

### Missing / inaccessible

The connected GitBook Front Room entry was attempted first for orientation, but organization discovery was blocked by the connector safety layer. This is **access fog**, not evidence about GitBook contents.

Wolfram MCP was invoked because the combinatorial boundary was mathematically relevant, but the connector returned an HTTP 404 during its MCP probe. Exact counting below was therefore independently checked locally and kept separate from interpretation.

**Sufficiency:** sufficient for the narrow audit.

## Discovery trace

Discovery trace is intentionally separate from evidence support:

1. Prior ALEXDEEPDIVE packet left `INVALID-PARTITION-REFUSAL-001` as the smallest live discriminator.
2. PR #107 changed after that packet; exact head is now `4ade4542f6fa5603d608b604436e66a0ac61da69`.
3. The new head adds `_partition_refusal()` and `run_invalid_partition_refusal_probe()`.
4. Auditing the validator's remaining acceptance region revealed an untested case: an explicitly declared block with zero constituents.

The prior frontier explains **why this location was inspected**. It does not itself support the new claim.

## Evidence path

### E1 — ALEX governance

`AGENTS.md` requires refusal paths to be first-class outcomes and forbids silent collapse of evidence/interpretation/proposal/admitted claim. It also states that ALEX may discover, read, compare, and propose but does not decide canon or manufacture authority.

Source: `https://github.com/the-static-collective/ALEX.2/blob/main/AGENTS.md`

### E2 — Exact implementation delta

PR #107 head `4ade4542f6fa5603d608b604436e66a0ac61da69` is commit:

> `fix: refuse invalid partitions before macro projection`

Its `_partition_refusal(partition)` computes:

- duplicate constituent names;
- constituents missing from `_MICRO_NODES`;
- unexpected constituent names.

It returns `REFUSE` for overlap, uncovered, or unexpected membership; otherwise it returns `None`. `_lift_receipt()` invokes this refusal check before `_macro_edges()`.

Source commit: `https://github.com/the-static-collective/ALEX.2/commit/4ade4542f6fa5603d608b604436e66a0ac61da69`

### E3 — Hostile tests now present

At the exact PR head, `test_invalid_partitions_refuse_before_macro_projection` verifies two cases:

- overlap: `A` occurs in two blocks;
- uncovered: `D` occurs in no block.

Both must return `status: REFUSE` and must not contain `macro_edges`.

Source: `https://github.com/the-static-collective/ALEX.2/blob/4ade4542f6fa5603d608b604436e66a0ac61da69/tests/test_partition_swap_experiment.py`

### E4 — Exact-head verification

GitHub Actions check `contract` completed successfully on exact head `4ade4542f6fa5603d608b604436e66a0ac61da69` on 2026-09-07.

Check run: `https://github.com/the-static-collective/ALEX.2/actions/runs/34129136500/job/101764775429`

This establishes technical GREEN for the checked contract. It does **not** establish semantic completeness, merge authority, or runtime promotion.

### E5 — External terminology pressure

NetworkX 3.6.1 documents a partition as a family of pairwise-disjoint sets whose union is the universe. Its current implementation of `is_partition` checks coverage/disjointness through cardinalities:

```python
return len(G) == len(nodes) == sum(len(c) for c in communities)
```

Source: `https://networkx.org/documentation/stable/_modules/networkx/algorithms/community/community_utils.html`

Notably, this implementation does **not** reject an additional empty community by itself. That is direct counterpressure against pretending a library's validity predicate settles ALEX's intended semantics.

Wolfram MathWorld's current entry for Stirling numbers of the second kind uses the standard combinatorial convention that a partition into `m` blocks is a partition into `m` **nonempty** sets.

Source: `https://mathworld.wolfram.com/StirlingNumberoftheSecondKind.html`

These external sources therefore expose a convention boundary rather than supplying ALEX authority.

## Finding

### The previous frontier is closed

**Observed:** PR #107 now validates overlap, omission, and unexpected constituents before macro projection, and its hostile overlap/uncovered tests pass at exact head.

Therefore:

```text
INVALID PARTITION-SHAPED INPUT
!=
RAW MISSING-KEY CRASH

REFUSAL PRECEDES MACRO PROJECTION
```

is now represented by the experimental carrier for the tested invalidity classes.

### The smaller surviving frontier

`_partition_refusal()` does not inspect whether a declared partition block is empty.

Consider the exact hostile specimen:

```python
partition = {
    "X": ("A", "B", "C", "D"),
    "Y": (),
}
```

Given the current `_MICRO_NODES = {A,B,C,D}`:

- duplicates = `[]`
- missing = `[]`
- unexpected = `[]`

so `_partition_refusal()` returns `None`.

`_lift_receipt()` then emits:

```text
macro_nodes = ["X", "Y"]
macro_edges = []
```

Thus the present implementation can mint a declared macro node `Y` that has no constituent micro node at all.

That is a different question from the already-protected isolated-node control. An **isolated macro node** may contain constituents while having no projected edges. An **empty block** contains no constituents.

```text
ISOLATED MACRO NODE != EMPTY PARTITION BLOCK
NO PROJECTED EDGES != NO CONSTITUENTS
DECLARED LABEL != EARNED LIFT
```

## Exact combinatorial check

For four constituents assigned to two labeled block names `X` and `Y`:

- all labeled assignments: `2^4 = 16`;
- assignments that use both labels: `16 - 2 = 14`;
- assignments leaving one declared label empty: `2`.

The current overlap/coverage/unexpected-node checks distinguish none of those two empty-block assignments from the 14 onto assignments, provided the empty label is explicitly retained as a dictionary key.

This arithmetic is computation only. It does not decide whether ALEX **should** permit empty declared blocks.

## Claims

| ID | Claim | Class | Supporting path | Counterevidence / alternative | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #107 closes the tested overlap/uncovered refusal frontier before macro projection. | observed | E2 → E3 → E4 | only tested classes are established | supported, bounded |
| C2 | Current `_partition_refusal()` accepts an explicitly empty block when all micro nodes otherwise occur exactly once. | inference from executable source | E2 + hostile substitution | no exact-head test executes this specimen yet | strongly supported; discriminator needed |
| C3 | Accepting that specimen causes `_lift_receipt()` to emit a macro-node label with no constituent members. | inference from executable source | E2 + hostile substitution | could be intentional placeholder semantics | strongly supported; meaning unresolved |
| C4 | Standard mathematical usage commonly treats partition blocks as nonempty. | scholarly/reference claim | E5 MathWorld | NetworkX's `is_partition` implementation itself permits extra empty communities | convention-dependent |
| C5 | ALEX should reject empty blocks. | proposal | C2–C4 | empty labeled blocks may be intentionally meaningful in this experiment | **not admitted** |

## Contradictions and competing readings

### Reading A — empty block is malformed

If a macro node is supposed to be a lift of one or more micro constituents, an empty block manufactures a macro identity without any lower-order carrier. Under this reading the current validator is incomplete.

### Reading B — empty block is a declared placeholder

The experiment may intentionally treat declared macro labels as part of the input vocabulary, including presently unoccupied labels. Under that reading `Y=()` is not malformed; it is an explicit empty slot, and rejecting it would erase declared information.

### Reading C — fixture-local code does not deserve generic partition semantics

The narrowest boring explanation is that this is an experimental fixture with four fixed micro nodes, not a reusable partition library. The right move may be to document its admissible domain rather than chase every mathematical convention.

No present source resolves A vs B. Therefore this packet does not call the behavior a bug.

## Direct counterevidence

NetworkX 3.6.1's `is_partition` source accepts a family containing an additional empty set when the nonempty sets already cover every graph node exactly once. This demonstrates that even a mature graph library's operative partition predicate does not automatically enforce the nonempty-block convention.

Therefore:

```text
MATHEMATICAL TERM "PARTITION"
!=
UNIVERSALLY IDENTICAL SOFTWARE CONTRACT
```

ALEX must declare which object it means.

## Dependency / independence uncertainty

The MathWorld combinatorial convention and NetworkX software behavior are independent enough to expose a real convention split, but no genealogy analysis was performed. They are not treated as corroborating votes.

The strongest claim remains source-local to PR #107 and does not depend on either external source.

## Rights / egress

- Repository material inspected through the connected GitHub surface and public GitHub URLs.
- Public NetworkX and MathWorld documentation were read through web retrieval.
- No private corpus bytes, scans, or research materials were sent externally.
- Wolfram MCP was attempted for exact combinatorial verification but failed before computation with an HTTP 404 MCP probe response.
- No source corpus was committed. This packet contains only research observations and small synthetic examples.

## Residual fog

1. Whether an empty macro block is intentionally meaningful as a declared placeholder is not specified in the inspected experimental contract.
2. No exact-head hostile test currently freezes the empty-block behavior.
3. PR #107 remains draft; technical GREEN does not imply merge or promotion authority.
4. GitBook Front Room contents were inaccessible in this run, so no orientation statement from that room is asserted.

## Smallest next discriminators / repo-worthy moves

1. **`EMPTY-BLOCK-CONTROL-001`** — feed `{"X": ("A","B","C","D"), "Y": ()}` through `_lift_receipt()` and force an explicit outcome. The test should not silently inherit semantics from the word *partition*.
2. If empty blocks are **invalid**, require attributable `REFUSE` with a narrow reason such as `partition-empty-block`, before macro projection.
3. If empty blocks are **valid declared placeholders**, freeze that deliberately and distinguish `declared_macro_labels` from `occupied_macro_nodes`, so `DECLARED LABEL != CONSTITUENT-BEARING LIFT` remains visible.

No generic partition package, graph-isomorphism engine, or new ALEX runtime primitive is earned.

## Compact law

```text
OVERLAP VALIDATION != COMPLETE PARTITION SEMANTICS
ISOLATED NODE != EMPTY BLOCK
DECLARED LABEL != CONSTITUENT-BEARING LIFT

EMPTY-BLOCK SEMANTICS MUST BE DECLARED,
NOT INHERITED FROM A NAME.
```

## Receipt

- Created: 2026-09-07 11:28 America/Chicago run window
- Researcher/agent: ALEXDEEPDIVE automated research pass
- Tool/model boundary: GitBook connector orientation attempt; GitHub connected repository inspection/write; public web documentation; Wolfram MCP attempted but unavailable; local exact arithmetic check
- External byte egress: no private/source corpus byte egress
- Durable location: `research/ALEX-DEEPDIVE-2026-09-07-1128-EMPTY-BLOCK-NOT-LIFT.md`
- Promotion: **none**
