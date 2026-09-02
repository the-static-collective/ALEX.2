# ALEX-DEEPDIVE — ROW-PRESENT-NOT-REACHABLE-001

**Date:** 2026-09-02  
**Status:** RESEARCH / PRESSURE / NO RUNTIME CHANGE / NO AUTHORITY PROMOTION  
**Promotion:** none

## Finding

The strongest newly surfaced ALEX frontier is draft PR #92, `ELIGIBILITY-INDEPENDENCE-001`, which turns the previous `ELIGIBILITY-NOT-AUTHORITY-001` research result into an executable matrix audit.

The experiment is useful, but its strongest lawful interpretation is narrower than its title suggests:

> **A HOSTILE ROW BEING PRESENT PROVES THAT THE DATA SHAPE CAN REPRESENT THE ROW. IT DOES NOT BY ITSELF PROVE THAT THE ROW IS ADMISSIBLE OR REACHABLE UNDER THE DECLARED GRAMMAR.**

The current experiment returns `MATRIX_WITNESSED` when four Boolean row patterns are present. It does not consume an initial state, transition relation, invariant set, model checker, trace, or execution receipt. Therefore it can establish **non-collapse at the schema / counterfactual representation layer**, but it cannot yet establish dynamic independence in an owning transition system.

The durable distinction is:

```text
ROW PRESENT
!= MODEL-ADMISSIBLE STATE
!= REACHABLE STATE
!= OBSERVED STATE
```

and, correspondingly:

```text
MATRIX_WITNESSED
!= GRAMMAR_WITNESSED
!= EXECUTION_WITNESSED
```

This does not invalidate PR #92. Its own PR body already says `MATRIX_WITNESSED` means the rows are present and does not establish truth, consent, capability, authorization, execution, or outcome. The pressure result sharpens one additional boundary: **presence also does not establish semantic realizability or reachability.**

---

# ALEX research receipt

## Ground

- **Question:** Does the `ELIGIBILITY-INDEPENDENCE-001` hostile-state matrix prove that grammar eligibility is dynamically independent of observer availability, capability reachability, authorization, and execution, or only that those Boolean combinations can be represented as rows?
- **Desired consequence:** Preserve the useful executable specimen while preventing `MATRIX_WITNESSED` from silently becoming a reachability or system-behavior claim.
- **Stop condition:** Inspect the exact PR #92 experiment and tests, construct one direct countermodel, compare against established formal-method reachability semantics, and identify the smallest next discriminator.
- **Corpus / date:** ALEX.2 `main@2b9e1ea41c345d072eb22811fd003a04264f5993`, draft PR #92 head `a4c694eaa3341b38fc2b4104af942ecf9d65c67e`, prior ALEX packet `ELIGIBILITY-NOT-AUTHORITY-001`, TLA+/TLC primary documentation, and peer-reviewed Petri-net reachability literature through 2026-09-02.
- **Authority / effect boundary:** Research packet only. No runtime, Jubilee, LOADOUT, observer, consent, authorization, or project-authority promotion.
- **Task shape:** `PRESSURE` with bounded `AUDIT`.
- **Formation trace active:** no. Discovery motive remains separate from evidence support.

## World cut

### Front Room orientation

The Static Collective GitBook Front Room was reachable. It was used only to orient the run: stable landmark, bounded traversal, current project evidence outranks memory, and unresolved fog stays unresolved. No Front Room content is used as evidence for the technical claim below.

### Included project sources

1. ALEX.2 `AGENTS.md` on current `main`.
2. ALEX `skills/alex/SKILL.md` and `skills/alex/references/research-receipt.md` on current `main`.
3. Prior packet `research/ALEX-DEEPDIVE-2026-09-02-1121-ELIGIBILITY-NOT-AUTHORITY.md`.
4. Draft PR #92, `Experiment: freeze ELIGIBILITY-INDEPENDENCE-001 matrix`, head `a4c694eaa3341b38fc2b4104af942ecf9d65c67e`.
5. PR #92 experiment file `experiments/eligibility_independence.py` and test file `tests/test_eligibility_independence_experiment.py`.

### Deliberately omitted doors

- broader Jubilee theological / symbolic interpretation;
- legal or interpersonal consent semantics;
- new LOADOUT / 3rdi / Dogram traversal, because the new discriminator is internal to the ALEX experiment contract;
- production runtime implementation or schema promotion;
- generic model-checker implementation.

**Sufficiency:** sufficient for the bounded semantic distinction; insufficient to state which concrete Jubilee states are actually reachable, because no owning transition grammar for the matrix is supplied.

## Acquisitions

| ID | Provider | Item / locus | Method / resolution | Rights / egress |
| --- | --- | --- | --- | --- |
| A1 | GitBook | Static Collective Front Room search result | orientation only | no durable external bytes |
| A2 | GitHub | ALEX.2 `AGENTS.md` | exact current public file | public text only |
| A3 | GitHub | ALEX skill + research receipt | exact current public files | public text only |
| A4 | GitHub | PR #92 metadata + files + exact head commit | exact public PR/commit | public text only |
| A5 | GitHub | prior `ELIGIBILITY-NOT-AUTHORITY-001` packet | exact current public file | public text only |
| A6 | Web | Lamport, Matthews, Tuttle, Yu, “Specifying and Verifying Systems With TLA+” | primary technical paper / exact PDF text and page visual | no source bytes committed |
| A7 | Consensus / IEEE metadata | Qi, Su, Zhou, Abusorrah, “A State-Equation-Based Backward Approach to a Legal Firing Sequence Existence Problem in Petri Nets,” IEEE TSMC:S 53 (2023), 4968–4979 | peer-reviewed paper metadata + abstract | no source bytes committed |
| A8 | Web | Petri-net reachability literature on state-equation solutions vs legal firing sequences | extracted scholarly text | no source bytes committed |

## Source roads

- https://github.com/the-static-collective/ALEX.2/pull/92
- https://github.com/the-static-collective/ALEX.2/commit/a4c694eaa3341b38fc2b4104af942ecf9d65c67e
- https://github.com/the-static-collective/ALEX.2/blob/main/research/ALEX-DEEPDIVE-2026-09-02-1121-ELIGIBILITY-NOT-AUTHORITY.md
- https://lamport.azurewebsites.net/pubs/spec-and-verifying.pdf
- https://consensus.app/papers/a-stateequationbased-backward-approach-to-a-legal-firing-qi-su/d9f7d6fbe5af5697835077b559928f7f/
- https://doi.org/10.1109/TSMC.2023.3238213

## Witnesses and readings

### W1 — PR #92 declares a representation-level experiment

PR #92 says its bounded design is to add an experimental / non-canonical matrix auditor that checks whether a **single declared handoff can represent the hostile rows** from the prior research packet. It explicitly says:

```text
MATRIX_WITNESSED means the rows are present
```

and separately refuses truth, consent, capability, authorization, execution, outcome, runtime primitive, public schema, or owner-authority promotion.

This is already disciplined framing.

### W2 — the evaluator checks row predicates only

The current experiment defines four predicates:

```text
grammar_eligible = true, authorized = false, executed = false
grammar_eligible = true, observer_available = false
grammar_eligible = true, capability_reachable = false
structural_edge = true, grammar_eligible = false
```

`audit_eligibility_matrix()` returns `MATRIX_WITNESSED` exactly when each predicate matches at least one supplied row.

It does not validate:

```text
an Init predicate
an invariant set
a Next / transition relation
path existence
row provenance
whether every row belongs to one actual grammar execution space
whether a row was generated by the grammar identified by grammar_id
whether a row was ever observed in an execution trace
```

This is not a bug relative to the PR’s stated representation-level scope. It is the reason the result must remain scoped to that layer.

### W3 — direct countermodel

Take the exact PR #92 row set and declare a hypothetical owning grammar `G*` with the invariant:

```text
grammar_eligible
=>
observer_available AND capability_reachable
```

The PR #92 matrix still contains all four required hostile patterns, so its current auditor returns `MATRIX_WITNESSED`.

But two required rows violate `G*` immediately:

```text
eligible-hidden:
  grammar_eligible = true
  observer_available = false

eligible-unreachable:
  grammar_eligible = true
  capability_reachable = false
```

Therefore:

```text
all required rows present
DOES NOT ENTAIL
all required rows are legal states of G*
```

The same argument is even stronger for reachability: a state can satisfy static invariants and still have no legal path from the declared initial state.

This is a direct refusal of the overclaim, not a refusal of the matrix artifact.

### W4 — TLA+ supplies the missing semantic layer

Lamport et al. describe a typical TLA+ specification with:

```text
Init
Next
Liveness
```

where `Init` describes legal initial states and `Next` specifies possible successive-state steps. TLC then explores **reachable states** generated by those behaviors.

That formalism preserves exactly the distinction needed here:

```text
an assignment of variable values
!=
a state reachable under Init and Next
```

A Boolean tuple is not dynamically witnessed merely because it is expressible in the variable vocabulary.

### W5 — Petri-net reachability supplies an independent false-positive analogue

Qi, Su, Zhou, and Abusorrah (2023, IEEE Transactions on Systems, Man, and Cybernetics: Systems) explicitly study the case where a non-negative integer solution satisfies the Petri-net state equation but **no legal firing sequence exists**, so the marking is nonreachable.

The important analogy is not Petri-net identity. It is the general failure mode:

```text
STATIC / ALGEBRAIC COMPATIBILITY
!=
DYNAMIC REACHABILITY
```

This is especially useful because it demonstrates that even a mathematically constrained candidate can remain only a potential state until a lawful path exists.

## Claims

| ID | Claim | Class | Supporting evidence path | Counterevidence / limit | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #92 proves the data shape can preserve the required non-collapse combinations without authority promotion. | observed + inference | W1 + W2 | only at representation layer | supported |
| C2 | `MATRIX_WITNESSED` currently proves those combinations are reachable under the declared grammar. | overclaim | none | W2 + W3 + W4 + W5 | disproved |
| C3 | A model-admissibility check alone would be enough to prove reachability. | overclaim | none | W4 + W5 | disproved in general |
| C4 | The useful next distinction is `ROW_PRESENT != MODEL_ADMISSIBLE != REACHABLE != OBSERVED`. | proposal strongly supported | W2–W5 | exact labels remain local vocabulary | survivor, not promoted |
| C5 | PR #92 should be discarded because it lacks reachability semantics. | overcorrection | none | W1: its stated purpose is narrower and useful | refused |
| C6 | A future consumer may lawfully promote representation evidence to reachability if an owning grammar supplies an explicit generator / validator / trace relation. | proposal | W4 + W5 | mechanism depends on owning grammar | live |

## Hypothesis lineage — PRESSURE

### H0 verbatim seed

From PR #92:

> `MATRIX_WITNESSED` means the rows are present.

### H1 — overstrong reading

```text
MATRIX_WITNESSED
=>
the hostile states are dynamically possible under the named grammar
```

**Verdict:** disproved.

A consumer can write rows that violate the named grammar’s invariants or that satisfy invariants but remain unreachable from its initial state.

### H2 — corrected survivor

```text
MATRIX_WITNESSED
=
the supplied record contains explicit counterfactual rows preserving the requested relation distinctions
```

This is a valid representation / schema-separation witness.

It does not entail grammar validity or path existence.

### H3 — cross-domain survivor

A common formal distinction survives across TLA+ reachability and Petri-net firing semantics:

```text
CANDIDATE STATE DESCRIPTION
!=
LAWFULLY REACHED STATE
```

This is a formal analogy, not genealogy and not evidence that ALEX should adopt either formalism wholesale.

## Hypothesis-loss receipts

| Transition | What survived | What was removed | Why removed | Recoverable |
| --- | --- | --- | --- | --- |
| H0 → H1 | explicit hostile rows | representation-only scope | deliberately overstrong literalization for pressure | yes |
| H1 → H2 | executable non-collapse witness | reachability / system-behavior claim | direct countermodel + formal reachability semantics | yes |
| H2 → H3 | state-description vs dynamic-state distinction | ALEX/Jubilee-specific vocabulary | cross-domain move cannot carry local ontology | yes |

## Bridge Ledger

| Move | Type | Evidence bearing | Promotion limit |
| --- | --- | --- | --- |
| TLA+ `Init/Next` → ALEX matrix | formal analogy | demonstrates why reachability requires transition semantics, not tuple presence | does not require ALEX to use TLA+ |
| Petri state equation → ALEX matrix | formal analogy / direct false-positive pattern | demonstrates constrained candidate ≠ reachable state | ALEX matrix is not a Petri net |
| PR #92 matrix → grammar independence | local inference | supports representational non-collapse only | cannot establish dynamic independence without owner grammar |

## Pressure

- **Exact source check:** PR #92 head remained `a4c694eaa3341b38fc2b4104af942ecf9d65c67e` when re-read near completion; the experiment body and test fixture were inspected from that exact head.
- **Quote-to-page check:** repository claims use exact public PR/commit text. TLA+ claims were checked against the primary PDF text and page-1 visual surface.
- **Visual surface:** one TLA+ PDF page was visually inspected; no spatial claim depends on coordinates.
- **Translation pressure:** none; technical sources are English.
- **Independence / lineage:** PR #92 descends directly from the previous ALEXDEEPDIVE packet and is not independent corroboration of that packet. The TLA+ and Petri-net sources are independent formal analogues, not evidence of ALEX ontology.
- **Direct counterexample:** `G*` above permits the matrix auditor to return `MATRIX_WITNESSED` even while two required rows violate a declared invariant.
- **Nearest boring explanation:** PR #92 is simply a schema / counterfactual fixture proving that the fields were not collapsed. If so, it is already mostly correct; the main risk is semantic naming drift, not implementation failure.
- **Replay impersonation check:** a replayed or hand-authored row must not impersonate a reachable or historically observed state without a separate lineage/path receipt.
- **Serendipity trap:** no symbolic recurrence is used as support.
- **Wolfram boundary:** a Wolfram context request was attempted because exact formal checking would have been useful, but the connector returned a transient network error. No Wolfram result is relied upon in this packet.

## PRESSURE verdict

- **Seed:** `MATRIX_WITNESSED` means the hostile rows are present.
- **Literal verdict:** **supported at representation layer; disproved if read as dynamic reachability.**
- **What broke:** any implication from row presence to grammar-admissibility, path existence, or observed system behavior.
- **What survived:** the matrix is a useful executable non-collapse witness showing that ALEX can keep grammar eligibility distinct from authorization, observer availability, capability reachability, structural presence, and execution in a counterfactual record.
- **Why it survived:** the PR already refuses authority and truth promotion, and the implementation performs exactly the bounded row-presence audit it claims to perform.
- **Residual weirdness:** the experiment is named `eligibility_independence`, while the executable proof currently establishes **representational separability**, not mathematical/statistical/dynamic independence. That naming may be harmless inside `experiments/`, but it is the main promotion hazard.
- **Next discriminator:** introduce an explicit toy grammar with `Init`, state invariants, and a tiny `Next` relation, then ask separately which hostile rows are (a) syntactically representable, (b) invariant-admissible, and (c) reachable.

## Residual fog

1. The owning Jubilee transition grammar has not been formalized here, so this packet does not claim which hostile combinations ought to be reachable in the real intended system.
2. The PR is draft and may narrow its vocabulary before merge.
3. `independence` could intentionally mean only “fields are not definitionally collapsed.” If that is the intended technical meaning, the code is already close to the right proof and only naming/documentation pressure remains.
4. No CI status contexts were returned for the current PR head during this pass; absence of returned statuses is not evidence of test failure or success.

## Smallest next discriminators

1. **`REPRESENTABLE-NOT-REACHABLE-001`** — add a tiny experimental grammar whose invariant forbids one of the supplied hostile rows; require the matrix audit to remain `MATRIX_WITNESSED` while a separate grammar audit rejects that row. This freezes the layer split executablely.
2. **Rename or document the disposition boundary** — one sentence is enough: `MATRIX_WITNESSED witnesses supplied counterfactual row coverage only; it does not establish grammar validity, reachability, or observation.` No production primitive required.
3. **Only if a real consumer appears:** add path-level witness semantics (`Init`, `Next`, or an owning trace/generator receipt). Do not build generic model-checking machinery merely to strengthen an experiment.

## Compact law

> **THE MATRIX CAN WITNESS THAT WE DID NOT COLLAPSE THE WORDS.**  
> **THE GRAMMAR MUST WITNESS WHETHER THE STATE IS LAWFUL TO IT.**  
> **THE WALK MUST WITNESS WHETHER THE STATE CAN BE REACHED.**  
> **THE TRACE MUST WITNESS WHETHER IT ACTUALLY HAPPENED.**

## Receipt

- **Created:** 2026-09-02 17:30 America/Chicago
- **Researcher / agent:** ALEXDEEPDIVE automation pass
- **Tool / model boundary:** GitBook orientation; GitHub exact repo/PR inspection and durable write; public web primary-source inspection; Consensus scholarly discovery/fetch; local Boolean replay; Wolfram attempted but unavailable due transient network error.
- **External byte egress:** public repository/document text only; no private/local source bytes sent outward.
- **Durable location:** `research/ALEX-DEEPDIVE-2026-09-02-1730-ROW-PRESENT-NOT-REACHABLE.md`
- **Promotion:** none
