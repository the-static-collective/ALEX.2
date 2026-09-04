# ALEXDEEPDIVE — REPRESENTATION-NOT-STRUCTURE-001

Status: **RESEARCH**  
Promotion: **none**

## Ground
- Question: What is the strongest newly revealed ALEX frontier since `LIFT-IS-A-CLAIM-001`, given draft PR #99 `PARTITION-SWAP-001`?
- Desired consequence: Freeze only the smallest semantic distinction needed to keep PR #99 from overclaiming what unequal serialized macro-edge lists establish.
- Stop condition: A bounded discriminator that separates genuine quotient-graph structural change from mere macro-node relabeling/serialization change.
- Corpus/date/language/geography: ALEX.2 current `main` and PR #99 as of 2026-09-04; current graph-isomorphism documentation only as external pressure. No historical corpus.
- Authority/effect boundary: Research audit only. No merge, runtime promotion, ontology admission, graph-library dependency, or owning-world authority.
- Task shape: **AUDIT**
- Formation trace active: **yes**, only to preserve why PR #99 was selected; discovery trace remains separate from evidence path.

## Front Room orientation
The Static Collective GitBook organization was visible through the connected GitBook surface, but content retrieval for the Front Room was blocked by the connector. A bounded public-web search for the Front Room returned no result. This is access fog, not evidence about Front Room contents. No GitBook content was used as evidence in this packet.

## Governing ALEX constraints read before claim formation
- `ALEX.2/AGENTS.md`: preserve evidence/interpretation/proposal/admitted-claim and discovery/evidence-path splits; do not manufacture authority.
- `skills/alex/SKILL.md`: use the smallest adequate shape; search-result inequality is not evidence by itself; preserve direct counterexamples and residual fog.
- `skills/alex/references/research-receipt.md`: a receipt testifies to this run only; durable research remains `Promotion: none` until admitted by a named gate.

## World cut
### Included
- `main@33320e358ed53158aac8b25a19d182780b6b6e53` — prior packet `LIFT-IS-A-CLAIM-001`.
- Draft PR #99 head `1f94f6e31b5a63982677d0c2825b4e91c09c2b0c`.
- PR #99 files:
  - `experiments/partition_swap.py`
  - `tests/test_partition_swap_experiment.py`
- NetworkX graph-isomorphism documentation as external methodological pressure.

### Deliberately omitted
- PR #97 WTC material: older frontier and not needed for this discriminator.
- Other ALEX draft PRs: no stronger newly revealed seam than PR #99.
- LOADOUT/3rdi/Dogram: not needed to decide this graph-comparison boundary.
- Generic graph canonicalization/clustering architecture: not earned.

### Missing/inaccessible
- GitBook Front Room contents: connector/public retrieval unavailable in this run.
- Wolfram computation: attempted twice; connector returned transient HTTP 502. No Wolfram result is used below.

Sufficiency: **sufficient for the bounded audit**.

## Discovery trace — why this door was chosen
| ID | From | To | Move | Role | Reason |
| --- | --- | --- | --- | --- | --- |
| D1 | prior packet `LIFT-IS-A-CLAIM-001` | PR #99 | follow newly executable discriminator | motive | PR #99 was created after the previous packet and directly implements its smallest next move |
| D2 | PR #99 implementation | `macro_edges` list comparison | inspect observation predicate | discriminator | the code reports partition dependence from direct Python list inequality |
| D3 | direct inequality | graph isomorphism | adversarial reframing | counterevidence | unequal serialized labels can describe the same unlabeled structure |

Nothing in this discovery trace independently supports the final claim; support comes from the evidence path below.

## Evidence path
### E1 — PR #99 implementation
Source layer inspected: repository text at exact PR head.

`run_partition_swap_probe()` creates two lifts over the same two micro receipts and computes:

```python
observation = (
    "PARTITION_DEPENDENT_MACRO_GRAPH"
    if lifts[0]["macro_edges"] != lifts[1]["macro_edges"]
    else "NO_PARTITION_DELTA_OBSERVED"
)
```

The current hostile specimen yields:
- role-side lift: one directed macro edge `X --appoints--> Y`;
- transaction-pair lift: zero macro edges because each micro appointment is internal to its macro block.

The test requires those outputs and keeps `authority: none`.

Repository witness: https://github.com/the-static-collective/ALEX.2/pull/99  
Exact head: `1f94f6e31b5a63982677d0c2825b4e91c09c2b0c`

### E2 — exact structural check for the present hostile specimen
Let:

```text
G_role = ({X,Y}, {X -> Y})
G_pair = ({P,Q}, {})
```

These graphs are non-isomorphic even when macro-node names are ignored, because graph isomorphism preserves edge count and:

```text
|E(G_role)| = 1
|E(G_pair)| = 0
```

Therefore the **current specimen really does demonstrate a structural quotient-graph delta**. The packet does not reject PR #99's current concrete observation.

### E3 — direct counterexample to the implementation predicate as a general structural test
Construct a pure relabeling control:

```text
G_a = ({X,Y}, {X -> Y})
G_b = ({P,Q}, {P -> Q})
```

As serialized Python edge dictionaries/lists they differ because `X,Y != P,Q`:

```text
[{from:X, to:Y, verb:appoints, system:S}]
!=
[{from:P, to:Q, verb:appoints, system:S}]
```

But the directed graphs are isomorphic under the bijection `X -> P`, `Y -> Q` when the macro names themselves are not declared semantic labels.

This is a direct hostile counterexample to the stronger reading:

```text
serialized macro_edges inequality
=> structural macro-graph inequality
```

That implication is false in general.

### E4 — external methodological pressure
Current NetworkX documentation states that `is_isomorphic(G1, G2)` tests graph isomorphism, while node attributes are ignored unless an explicit `node_match` is supplied. The current VF2++ documentation likewise exposes graph-isomorphism mapping with node labels optional rather than inherently semantic.

- NetworkX `is_isomorphic`: https://networkx.org/documentation/networkx-3.4.2/reference/algorithms/generated/networkx.algorithms.isomorphism.is_isomorphic.html
- NetworkX VF2++ implementation/docs: https://networkx.org/documentation/latest/_modules/networkx/algorithms/isomorphism/vf2pp.html

These sources are used only to pressure the comparison shape. They do not establish an ALEX runtime requirement to adopt NetworkX.

## Claims
| ID | Claim | Class | Supporting evidence path | Counterevidence | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #99 compares the two lifts by direct serialized `macro_edges` list inequality. | observed | E1 | none | supported |
| C2 | The current PR #99 hostile specimen exhibits a genuine structural difference, not merely a label difference. | inference from exact invariant | E1 -> E2 | none found; edge-count mismatch is decisive | supported within declared specimen |
| C3 | Direct serialized inequality is not a sound general proxy for graph non-isomorphism. | inference | E3 -> E4 | could become sound if macro names are explicitly semantic identities and equality is intentionally label-sensitive | supported with scope qualifier |
| C4 | PR #99 therefore needs an explicit comparison contract before `PARTITION_DEPENDENT_MACRO_GRAPH` is generalized beyond this specimen. | proposal | C1+C2+C3 | the experiment may intentionally remain a one-off fixed specimen and never generalize | supported as smallest guardrail, not runtime mandate |

## Competing readings
### Reading A — labels are presentation only
If `X/Y` and `P/Q` are merely arbitrary macro-node names, then structural comparison should be invariant to their renaming. Under this reading:

```text
SERIALIZATION_DELTA != STRUCTURAL_DELTA
```

### Reading B — labels are semantic identity
If a lift contract declares macro-node identity/name itself to be part of the preserved semantics, then label-sensitive inequality may be intentional. In that case the result should say so explicitly; it is not ordinary unlabeled graph structure.

### Reading C — fixed-specimen probe only
PR #99 may never need a reusable graph-equivalence predicate. Because the present pair differs by edge count, the one hostile specimen already succeeds without introducing any graph-isomorphism dependency. This is the nearest boring explanation and currently the preferred implementation posture.

## Contradictions and alternatives
- The current PR title/body says it proves two declared lifts can preserve the same micro receipts while producing different macro-graphs. For the frozen specimen, that statement survives because one quotient has one edge and the other has zero.
- The implementation's *mechanism* for deciding difference is broader than the mathematical fact it currently needs. This is not presently a false positive on the frozen specimen; it is a latent semantic ambiguity if reused.
- `partition_rule` and `preservation_target` differ between lifts. Those are explanatory declarations, not evidence that the resulting graphs are non-isomorphic.

## Dependency / independence
- Repository observations E1 and the test derive from the same PR branch and are not independent corroboration.
- E2/E3 are direct mathematical checks on the serialized specimen/hostile control, independent of NetworkX as a software implementation.
- NetworkX E4 is an external methodological precedent only; independence from ALEX code is clear, but it is not evidence about ALEX's intended semantics.

## Pressure
- Direct counterexample: pure macro-node renaming changes serialized edge dictionaries without changing graph structure.
- Nearest boring explanation: the experiment is intentionally fixed and the present edge-count difference makes sophisticated equivalence unnecessary.
- API/framework claim verification: NetworkX behavior checked against current project documentation; no third-party blog relied upon.
- Wolfram: attempted for exact `IsomorphicGraphQ` checks; connector returned HTTP 502. The exact conclusions used here follow from elementary invariants and explicit bijection, not from an implied Wolfram result.
- Rights/egress: only public repository text and public documentation were sent to external search/computation surfaces; no local/private corpora or page bytes were egressed.

## Finding

The new frontier is not "partition choice affects the lift"—PR #99 has now frozen that successfully for its chosen specimen. The sharper boundary is:

```text
REPRESENTATION DELTA
!=
STRUCTURAL DELTA
```

More specifically:

```text
serialized macro-edge inequality
!=
graph non-isomorphism
```

unless the comparison contract explicitly declares macro-node names/attributes to be semantic.

The current PR #99 specimen **still survives** this pressure because its two quotient graphs differ in edge count (`1 != 0`), so they cannot be isomorphic. The issue is prospective reuse, not a defect in the present mathematical counterexample.

## Smallest next discriminators / repo-worthy moves
1. **RELABEL-CONTROL-001** — add one pure renaming control with the same single directed macro-edge under different macro-node names; require the experiment to classify it separately from the current edge-count-changing partition swap.
2. **Name the comparison contract** — for this experiment only, state whether `macro_graph_delta` means label-sensitive serialization delta or structure modulo declared node/edge semantics. Do not add a generic graph library if the fixed specimen can use simple invariants.
3. **Stop if one-off** — if PR #99 is explicitly frozen as a single specimen and no caller consumes its observation generically, document the scope and avoid further machinery.

## Compact law

```text
THE PARTITION CAN CHANGE THE GRAPH.
THE SERIALIZATION CAN CHANGE WITHOUT CHANGING THE GRAPH.
THE RECEIPT MUST SAY WHICH DIFFERENCE IT WITNESSED.
```

## Residual fog
- Whether future N↔V↔S lifts treat macro names as semantic identities, display labels, or generated local handles is not yet declared.
- Whether PR #99 will remain a one-off experimental specimen or become reusable comparison code is unresolved.
- GitBook Front Room orientation remained inaccessible; no absence claim is inferred.

## Receipt
- Created: 2026-09-04 11:22 America/Chicago
- Researcher/agent: ChatGPT / ALEXDEEPDIVE
- ALEX main inspected: `33320e358ed53158aac8b25a19d182780b6b6e53`
- PR #99 head inspected: `1f94f6e31b5a63982677d0c2825b4e91c09c2b0c`
- Tool/model boundary: GitBook connector attempted for orientation; GitHub connected repository reads/writes; public web for current NetworkX documentation; Wolfram connector attempted but returned transient 502 and contributed no result.
- External byte egress: public repository text/documentation only; no private/local corpus bytes.
- Durable location: `research/ALEX-DEEPDIVE-2026-09-04-1122-REPRESENTATION-NOT-STRUCTURE.md`
- Promotion: **none**
