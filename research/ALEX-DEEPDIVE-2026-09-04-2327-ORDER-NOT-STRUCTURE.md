# ALEXDEEPDIVE — ORDER-NOT-STRUCTURE-001

**Status:** RESEARCH  
**Promotion:** none  
**Task shape:** AUDIT  
**Created:** 2026-09-04 23:27 America/Chicago

## Finding

Draft PR #99 materially advanced since the previous ALEXDEEPDIVE packet by implementing `ISOLATED-NODE-CONTROL-001`. The new control closes the specific blind spot identified in `EDGE-LIST-NOT-GRAPH-001`: macro-node existence is now carried separately from the macro-edge projection, and a two-isolated-node quotient is distinguished from a one-isolated-node quotient even when both have empty edge lists.

That successful repair exposes a narrower remaining boundary in `_macro_graph_differs()`:

```text
ORDERED SERIALIZATION != GRAPH STRUCTURE
```

The current helper declares a macro-graph difference whenever either `macro_nodes` lists or `macro_edges` lists differ by ordinary Python list equality. Because both are emitted in construction/insertion order, two structurally identical macro-graphs can be classified as different solely because the same nodes or edges were serialized in a different order.

This is a prospective false-positive class, not a demonstrated failure of PR #99's existing frozen specimens. The present positive specimens still establish real structural differences.

## Ground

- **Question:** After `ISOLATED-NODE-CONTROL-001`, does PR #99's current graph-difference predicate distinguish structural graph change from serialization-order change?
- **Desired consequence:** Name the smallest remaining discriminator without promoting a generic graph runtime.
- **Stop condition:** Either find a direct order-only counterexample to `_macro_graph_differs()` or show that current code normalizes order before comparison.
- **Corpus:** ALEX.2 `main@a0a0ea3b568932fac0f7129f2182c104ab6ccdbc`; draft PR #99 head `b81b8d5338e4043be56405d442dec439bf4852f7`; current NetworkX 3.6.1 documentation used only as external comparison.
- **Authority/effect boundary:** research audit only; no merge recommendation, runtime authority, ontology promotion, or owning-project admission.
- **Formation trace active:** no.

## World cut

### Included

1. `ALEX.2/AGENTS.md` on current `main`.
2. `skills/alex/SKILL.md` on current `main`.
3. `skills/alex/references/research-receipt.md` on current `main`.
4. PR #99 code at exact head `b81b8d5338e4043be56405d442dec439bf4852f7`.
5. Previous packet `ALEX-DEEPDIVE-2026-09-04-1729-EDGE-LIST-NOT-GRAPH.md` as discovery context only.
6. NetworkX 3.6.1 isomorphism documentation as an external formal comparison.

### Deliberately omitted

- No adjacent Static Collective repo was needed; the live delta and counterexample are wholly local to PR #99.
- No generic graph library implementation was imported into ALEX.
- No Wolfram call was needed: the discriminator is a discrete software-semantics counterexample requiring no material symbolic/numeric computation.

### Missing / inaccessible

- Static Collective GitBook Front Room orientation was attempted first through the connected GitBook surface, but organization listing/search was blocked by the connector safety layer. This is **access fog**, not evidence about Front Room contents.

**Sufficiency:** sufficient for the bounded audit.

## Discovery trace

This ledger records why the frontier was selected; it is not evidentiary support.

1. Previous packet identified that edge lists alone erase isolated macro-nodes.
2. PR #99 advanced after that packet and implemented `ISOLATED-NODE-CONTROL-001`.
3. Reading the repair showed `_macro_graph_differs()` now compares both node and edge lists directly.
4. That exposed insertion/order sensitivity as the next narrower possible false-positive class.

## Evidence path

### E1 — governing ALEX contract

`AGENTS.md` requires preserving evidence/interpretation/proposal distinctions and forbids silent authority expansion. `skills/alex/SKILL.md` requires the smallest adequate research shape, direct counterexamples where consequential, and visible access fog. `research-receipt.md` requires discovery trace and evidence path to remain separate.

### E2 — exact PR #99 implementation

At head `b81b8d5338e4043be56405d442dec439bf4852f7`:

```python
def _lift_receipt(...):
    return {
        ...
        "macro_nodes": list(partition),
        "macro_edges": _macro_edges(partition),
    }


def _macro_graph_differs(left, right):
    return (
        left["macro_nodes"] != right["macro_nodes"]
        or left["macro_edges"] != right["macro_edges"]
    )
```

`macro_nodes` therefore preserves partition dictionary insertion order, while `_macro_edges()` appends edges in `_MICRO_EDGES` traversal order. `_macro_graph_differs()` compares both as ordered lists.

### E3 — new isolated-node control

The newly added `ISOLATED-NODE-CONTROL-001` compares:

```text
{P:{A,B}, Q:{C,D}} -> macro_nodes [P,Q], macro_edges []
{Z:{A,B,C,D}}       -> macro_nodes [Z],   macro_edges []
```

and correctly returns `PARTITION_DEPENDENT_MACRO_GRAPH`. This repairs the previous edge-list-only blind spot.

### E4 — external comparison

NetworkX 3.6.1 defines graph isomorphism by whether graphs are isomorphic and exposes mappings between differently named nodes; node labels are optional semantic constraints rather than list-position constraints. Its current documentation therefore provides a mature comparison showing that graph structural equivalence is not ordinarily defined by equality of a particular node/edge listing order.

Primary documentation:
- https://networkx.org/documentation/stable/reference/algorithms/isomorphism.html
- https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.isomorphism.vf2pp.vf2pp_is_isomorphic.html

This is comparison evidence only. It does not impose NetworkX semantics or a dependency on ALEX.

## Direct counterexample

Construct two receipts representing the same labeled directed macro-graph:

```text
LEFT
macro_nodes = ["P", "Q"]
macro_edges = [
  {from:"P", verb:"appoints", to:"Q", system:"S"},
  {from:"Q", verb:"appoints", to:"P", system:"S"}
]

RIGHT
macro_nodes = ["Q", "P"]
macro_edges = [
  {from:"Q", verb:"appoints", to:"P", system:"S"},
  {from:"P", verb:"appoints", to:"Q", system:"S"}
]
```

The node set and typed directed edge set are identical. Only serialization order differs. Yet current `_macro_graph_differs(LEFT, RIGHT)` returns `True` because Python list equality is order-sensitive.

A smaller node-only control also suffices when the graph contains two isolated labeled vertices:

```text
LEFT  macro_nodes = ["P", "Q"], macro_edges = []
RIGHT macro_nodes = ["Q", "P"], macro_edges = []
```

Current code classifies these as different despite identical labeled graph content.

## Claims

| ID | Claim | Class | Support | Counterevidence | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #99 now preserves macro-node existence separately from macro-edge lists. | observed | E2, E3 | none found | supported |
| C2 | `ISOLATED-NODE-CONTROL-001` closes the exact `same empty edges / different node count` blind spot from the previous packet. | inference from executable code/test | E3 | only frozen specimen coverage | supported within specimen |
| C3 | `_macro_graph_differs()` is order-sensitive because it compares node/edge lists directly. | observed | E2 | none | supported |
| C4 | Order-only serialization changes can produce a false structural-delta observation. | inference + direct counterexample | E2 + counterexample | current frozen fixtures do not exercise this case | supported |
| C5 | PR #99 therefore needs a generic graph-isomorphism engine. | proposal | none | smaller normalization/control is adequate | rejected / not earned |
| C6 | Existing PR #99 positive specimens are invalid. | inference | none | their node-count or edge-count/content differences are genuine | rejected |

## Contradictions and alternatives

### Competing reading A — order is intentionally semantic

If PR #99 intends `macro_nodes` and `macro_edges` to be **ordered sequences** where ordering itself is part of the declared lift semantics, then list inequality is not a bug. But the current observation is named `PARTITION_DEPENDENT_MACRO_GRAPH`, not `PARTITION_DEPENDENT_SERIALIZED_LIFT`, and no explicit order-semantics field declares sequence position as graph structure.

**Unresolved:** whether ordering is intended to be receipt presentation only or a constitutive semantic property.

### Competing reading B — frozen specimen only

The experiment may intentionally compare only its own deterministic serialization, in which case the helper is adequate for the current fixtures and should simply remain private and non-generalized.

This is the nearest boring explanation and is plausible.

## Pressure

- **Direct counterexample:** same labeled node/edge sets in different list order trigger `_macro_graph_differs()`.
- **Nearest boring explanation:** helper is a fixture-local convenience, not intended as a general graph comparator.
- **Dependency/independence:** NetworkX is independent external precedent for graph-isomorphism semantics, but ALEX need not adopt it.
- **Serendipity trap:** none; frontier follows directly from the previous discriminator being implemented.
- **Replay impersonation:** no replay identity claim made.
- **Authority pressure:** no graph comparison result can mint historical truth, canon, actor intent, or owning-project admission.

## Rights / egress

- Only public repository text and public NetworkX documentation were sent through external connected/search surfaces.
- No private corpus, copyrighted scan, credentials, or local page bytes were egressed.
- Public access is not treated as permission to redistribute any source corpus; only minimal code excerpts necessary for audit are reproduced here.

## Residual fog

1. Whether sequence order is intentionally part of the lift's semantic contract is not declared.
2. PR #99 remains draft and experimental; future commits may narrow or replace `_macro_graph_differs()`.
3. The current audit did not execute the branch test suite locally; findings are from exact-head source inspection and a deterministic language-level counterexample.

## Smallest next discriminators

1. **ORDER-SWAP-CONTROL-001** — construct two macro receipts with identical labeled node and typed-edge sets but reversed list order; require the experiment to classify them as `SERIALIZATION_ORDER_DELTA_ONLY`, not structural partition change.
2. If order is intended to be semantically meaningful, add an explicit `ordering_semantics` / `sequence_is_structural` declaration and rename the observation accordingly rather than letting Python insertion order imply it.
3. If a reusable comparator is later required, first normalize the bounded representation (e.g. compare node sets plus canonicalized typed-edge tuples) before considering a general isomorphism dependency.

## Compact law

```text
NODES PRESENT != NODE LIST ORDER
EDGES PRESENT != EDGE LIST ORDER
SERIALIZATION ORDER != GRAPH STRUCTURE

THE RECEIPT MAY PRESERVE ORDER.
THE COMPARATOR MUST SAY WHETHER ORDER COUNTS.
```

## Receipt

- **Researcher/agent:** ALEXDEEPDIVE automated research pass
- **Tool/model boundary:** GitBook orientation attempt; GitHub exact-head source inspection/write; web primary documentation lookup; no Wolfram result used
- **External byte egress:** public text only
- **Durable location:** `research/ALEX-DEEPDIVE-2026-09-04-2327-ORDER-NOT-STRUCTURE.md`
- **Promotion:** none
