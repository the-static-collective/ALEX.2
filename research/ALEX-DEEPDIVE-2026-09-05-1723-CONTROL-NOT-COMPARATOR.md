# ALEXDEEPDIVE — CONTROL-NOT-COMPARATOR-001

**Status:** RESEARCH  
**Promotion:** none  
**Shape:** AUDIT  
**Created:** 2026-09-05 17:23 America/Chicago

## Ground

- **Question:** What materially changed in ALEX.2 since `ANCESTRY-NOT-DELTA-001`, and does new PR #107 actually resolve the live `ORDER-SWAP-CONTROL-001` semantic frontier?
- **Desired consequence:** Distinguish a successful hostile control from repair of the classifier that motivated that control.
- **Stop condition:** Determine whether PR #107 (a) freezes the requested order-only specimen, (b) makes `_macro_graph_differs()` order-insensitive, and (c) binds the hostile specimen to the production comparison path strongly enough that the old false-positive class cannot survive.
- **Corpus:** Static Collective GitBook Front Room for orientation only; `the-static-collective/ALEX.2` current `main`; draft PR #107; prior packet `ALEX-DEEPDIVE-2026-09-05-1122-ANCESTRY-NOT-DELTA.md`; governing ALEX files.
- **Authority/effect boundary:** Read/audit plus this new durable research packet only. No merge, runtime promotion, schema promotion, or canon admission.
- **Formation trace active:** no.

## Orientation / world cut

The Static Collective GitBook Front Room was reached first and used only as an orientation membrane. Its current law remains: stable landmark -> relevant door -> bounded traversal; the room is not the world. No GitBook page beyond that orientation was needed for the evidence path.

Required ALEX governance was read before consequential claims:

- `AGENTS.md` — preserve evidence/interpretation/proposal, discovery/evidence, and authority distinctions.
- `skills/alex/SKILL.md` — smallest adequate shape; `AUDIT` fits this bounded code-contract question.
- `skills/alex/references/research-receipt.md` — receipts testify to encountered state and do not manufacture authority.

### Exact repository state observed

- `main`: `46870320fa7c081765216eaa457cb4f9ca4bc610`
- PR #107 head: `4068c0186cf2990dbb46bee1e63b80617ca234a9`
- PR #107 base: `46870320fa7c081765216eaa457cb4f9ca4bc610`
- PR #107 state: open, draft
- exact-head Actions run: `33990336488` / `crucible-contract` #398 — **success**

### Deliberately omitted doors

- WTC corkboard / PR #97 — no new evidence made it stronger than the newly implemented order-control seam.
- older ALEX drafts unrelated to partition/lift comparison — not material to this bounded frontier.
- adjacent repos — no cross-repo dependency is required to answer whether the local comparator consumes the new control semantics.
- Wolfram — no exact mathematical/statistical/temporal/geometric computation is material to this code-path audit.
- external scholarship — unnecessary; the decisive evidence is the repository's own executable comparison path and test contract.

## Discovery trace

1. Recent `main` inspection showed no commit after the prior ALEXDEEPDIVE packet.
2. Open-PR inspection revealed newly created draft PR #107: `Experiment: freeze ORDER-SWAP-CONTROL-001`.
3. PR #107 directly targets the prior run's smallest discriminator, making it the strongest new frontier.
4. Exact-head code inspection then showed the hostile control and the original comparator coexist but are not connected.

This trace explains why the seam was selected. It is not evidence for the conclusion.

## Evidence path

### E1 — PR #107 freezes the requested order-only specimen

`run_order_swap_control_probe()` constructs two macro-graph serializations with:

- identical labeled node membership: `{X, Y}`;
- identical typed directed edge membership: `{X appoints Y, Y appoints X}`;
- reversed `macro_nodes` list order;
- reversed `macro_edges` list order.

It then compares node membership with sets and edge membership with order-insensitive sets of normalized edge tuples. If raw serialization differs while labeled content is equal, it returns:

```text
SERIALIZATION_ORDER_DELTA_ONLY
```

This is the exact hostile class requested by the preceding audit.

### E2 — The test freezes that control result

`test_serialization_order_does_not_masquerade_as_structural_delta()` asserts:

- experiment = `ORDER-SWAP-CONTROL-001`;
- authority = `none`;
- observation = `SERIALIZATION_ORDER_DELTA_ONLY`;
- raw node and edge lists differ;
- node sets and normalized edge sets are equal.

So the control is not merely documentary; its intended order-only classification is executable and tested.

### E3 — Exact-head CI is green

GitHub Actions reports exact PR #107 head `4068c018...` as successful in `crucible-contract` run `33990336488` (#398).

This establishes technical compatibility with the current test floor. It does not establish that the relevant classifier was repaired.

### E4 — `_macro_graph_differs()` remains order-sensitive

The same PR head still implements:

```python
def _macro_graph_differs(left, right):
    return (
        left["macro_nodes"] != right["macro_nodes"]
        or left["macro_edges"] != right["macro_edges"]
    )
```

Ordinary list inequality is order-sensitive. Therefore the exact `left` and `right` objects used by `ORDER-SWAP-CONTROL-001` would cause `_macro_graph_differs(left, right)` to return `True`.

### E5 — The new hostile test never calls `_macro_graph_differs()`

`run_order_swap_control_probe()` performs its own separate order-insensitive membership calculation. Its test checks only that independent control path. It does **not** assert:

```python
_macro_graph_differs(left, right) is False
```

nor does it route the specimen through `run_partition_swap_probe()` or another shared comparison abstraction.

Thus the hostile control can be GREEN while the previously identified false-positive behavior remains intact in the classifier that produces `PARTITION_DEPENDENT_MACRO_GRAPH` / `NO_PARTITION_DELTA_OBSERVED`.

## Claims

| ID | Claim | Class | Supporting evidence path | Counterevidence / limit | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #107 successfully freezes an executable order-only serialization specimen. | observed | E1 + E2 | The specimen is synthetic and bounded. | supported |
| C2 | PR #107 exact-head CI is green. | observed | E3 | GREEN != semantic completeness != merge authority. | supported |
| C3 | `_macro_graph_differs()` remains order-sensitive on PR #107. | observed | E4 | If list order were intentionally structural, this would be valid, but the new control explicitly classifies order-only drift as non-structural. | supported |
| C4 | The new test does not prove that the production/local classifier rejects order-only permutations. | observed/inference | E4 + E5 | It proves the separate control path behaves as intended. | supported |
| C5 | A hostile control that bypasses the classifier it is meant to constrain can coexist with the original false positive. | inference from executable paths | E1-E5 | This is local to the present experiment; no claim is made about generic testing practice. | supported |
| C6 | The next smallest move is to bind the order-swap specimen to the shared comparator contract, not to add more graph machinery. | proposal | C1-C5 | A deliberate decision to keep `_macro_graph_differs()` representation-sensitive would instead require narrowing its name and observation semantics. | proposed |

## Contradictions and competing readings

### Reading A — “ORDER-SWAP-CONTROL-001 is green, therefore the order-sensitivity frontier is resolved.”

**Counterevidence:** the control uses a separate set-based comparison while `_macro_graph_differs()` remains list-order-sensitive. The control witnesses the distinction but does not enforce it on the classifier.

### Reading B — “The control is useless because it does not repair the comparator.”

Too strong. The control is valuable because it makes the intended semantic distinction explicit and executable. It is a valid hostile specimen. What is missing is only the binding from that specimen to the shared classifier contract.

### Reading C — “Just replace everything with generic graph isomorphism.”

Not earned. The current specimen only requires permutation-insensitive equality for already-labeled nodes and typed directed edges. Relabeling equivalence is separately handled by `RELABEL-CONTROL-001`. A general isomorphism engine would widen the problem before the local contract demands it.

### Nearest boring explanation

PR #107 implemented exactly the requested hostile control as an isolated experiment and intentionally avoided widening the older carrier. The remaining gap is ordinary integration scope: the test proves the counterexample exists but does not yet make the shared comparator consume that counterexample.

## Audit pressure

- **Direct counterexample:** apply `_macro_graph_differs()` conceptually to the exact left/right objects from `ORDER-SWAP-CONTROL-001`; because both lists are reversed, the current function returns `True` despite equal labeled graph content.
- **Alternative semantics:** if serialization order is intended to count, the control's phrase `does_not_masquerade_as_structural_delta` and observation `SERIALIZATION_ORDER_DELTA_ONLY` conflict with `_macro_graph_differs()`'s current semantics. One side must be narrowed or unified.
- **Dependency/independence:** PR #107 descends from the PARTITION-SWAP witness lineage. It is not independent corroboration; it is a targeted descendant discriminator.
- **Authority:** PR remains draft; experiment outputs retain `authority: none`; no merge or promotion was performed.
- **Rights/egress:** only public GitBook orientation text and public repository metadata/code were read. No local corpus, private research material, or copyrighted source bytes were egressed.

## Finding

PR #107 resolves the **specimen gap**, not yet the **classifier gap**.

```text
HOSTILE CONTROL EXISTS
!=
SHARED CLASSIFIER OBEYS CONTROL

CONTROL GREEN
!=
FALSE-POSITIVE CLASS REMOVED

WITNESS THE DISTINCTION
!=
BIND THE DISTINCTION
```

The strongest live frontier is therefore **CONTROL-NOT-COMPARATOR-001**: a control is only constraining when the semantic path that makes consequential classifications is forced to survive it.

This is not an argument for generic graph isomorphism. The local requirement is smaller:

```text
same labeled macro-node membership
+ same typed directed macro-edge membership
+ different serialization order
=> no structural delta
```

## Residual fog

- The audit did not inspect every historical PR #107 commit because the exact current head, test body, comparator body, and exact-head CI are sufficient for the bounded question.
- The experiment presently mixes three notions: representation equality, labeled-content equality, and relabeling equivalence. They are intentionally not collapsed here.
- It remains a design choice whether `_macro_graph_differs()` should become order-insensitive or whether it should be renamed/narrowed as a representation-delta comparator and a separate structural comparator introduced. No choice is promoted by this packet.

## Smallest next discriminators / repo-worthy moves

1. **`CONTROL-BINDS-COMPARATOR-001`** — feed the exact ORDER-SWAP left/right specimen through `_macro_graph_differs()` (or its successor) and require `False` for structural delta. This is the smallest decisive test.
2. If representation order must remain observable, split the result surface explicitly: `SERIALIZATION_DELTA` vs `LABELED_GRAPH_CONTENT_DELTA`; do not overload one boolean with both meanings.
3. Keep generic isomorphism, canonical graph hashing, and external graph dependencies on HOLD until a specimen requires equivalence beyond fixed labels + typed-edge membership.

## Receipt

- **Created:** 2026-09-05 17:23 America/Chicago
- **Researcher/agent:** ALEXDEEPDIVE
- **Tool/model boundary:** connected GitBook orientation; connected GitHub repository/PR/code/CI reads and durable write; no Wolfram computation; no external scholarly source required
- **External byte egress:** public repository/GitBook text and metadata only
- **Durable location:** `research/ALEX-DEEPDIVE-2026-09-05-1723-CONTROL-NOT-COMPARATOR.md`
- **Promotion:** none
