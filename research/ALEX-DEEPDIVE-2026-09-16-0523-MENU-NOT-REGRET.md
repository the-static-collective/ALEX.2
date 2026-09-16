# ALEXDEEPDIVE — MENU-NOT-REGRET-001

**Status:** RESEARCH  
**Promotion:** none  
**Shape:** AUDIT  
**Created:** 2026-09-16 05:23 America/Chicago

## Ground

- **Question:** What is the strongest live ALEX research frontier newly exposed since the previous ALEXDEEPDIVE packet?
- **Desired consequence:** identify one smallest reproducible provenance failure or missing coordinate without promoting a decision theory or runtime authority.
- **Stop condition:** one exact finite discriminator, externally pressure-checked where useful, with no adjacent traversal beyond what the evidence requires.
- **Authority/effect boundary:** research only; no canon/runtime promotion; no merge; no policy recommendation.
- **Formation trace active:** no. Discovery trace is recorded separately below only to preserve why this door was opened.

## World cut

### Orientation
The Static Collective GitBook organization was reached first. The Front Room content-search operation was blocked by the connector safety boundary, so orientation is **access fog**, not evidence of absence. No GitBook claim is used below.

### Included sources
- `the-static-collective/ALEX.2` current `main` before this write: `45c30b2ccfb194b14baa0a35cc229ac57b55bfdd`.
- ALEX.2 `AGENTS.md`, `skills/alex/SKILL.md`, and `skills/alex/references/research-receipt.md` read before consequential claims.
- ALEX issue #113 `CRITERION-NOT-POLICY-001`.
- Draft PR #114 `Experiment: freeze CRITERION-NOT-POLICY-001`, exact head `5741061bc0016551a85b52ab26bb8f09270f9822`.
- Exact-head GitHub Actions `crucible-contract` run 435 / `34527669816`: completed / success.
- MIT 16.422 decision-theory notes for the ordinary opportunity-loss definition of regret.
- Cambridge / *Economics & Philosophy* article “The evolution of ambiguous beliefs” for an explicit realization-regret formula whose benchmark maximizes over the action set `A`.
- Cambridge / *Econometric Theory* article “MINIMAX REGRET TREATMENT RULES WITH FINITE SAMPLES WHEN A QUANTILE IS THE OBJECT OF INTEREST” for an explicit regret benchmark `sup_{d in D}` over the feasible rule set.
- Wolfram Language exact finite calculation described below.

### Deliberately omitted doors
Dogram #82–#84 are formation ancestry for issue #113, but PR #114 already freezes the relevant ALEX cost table. No Dogram traversal was needed to establish the newly exposed comparator-menu dependence. LOADOUT, 3rdi, other ALEX PRs, and wider GitBook pages were likewise omitted.

### Sufficiency
Sufficient for the narrow audit claim below. Not sufficient to prescribe a canonical regret semantics for ALEX.

## Discovery trace — why we looked

1. Previous ALEXDEEPDIVE state ended on the older empty-block frontier at PR #107.
2. Current repository inspection revealed a materially newer open draft, PR #114, created after the previous packet and explicitly centered on decision-criterion provenance.
3. PR #114 already pressures criterion identity, prior identity, chronology, prior sets, and coincident verdicts.
4. Its minimax-regret calculation computes the statewise oracle from the policy menu currently present in `_COSTS` but does not independently freeze pressure on **menu identity**.
5. That exposed the narrow audit question: can the minimax-regret ordering of unchanged policies change when only the comparator/action menu changes?

**Discovery trace != evidence path.** The PR's novelty explains why this question was asked; the finite calculation and decision-theory definitions below bear the claim.

## Evidence path

### E1 — repository witness
PR #114 freezes:

```text
ADAPTIVE A = (1,3,3,3)
FIXED    F = (2,2,2,2)
```

and computes minimax regret by first forming a statewise oracle from the policies in the current menu:

```python
oracle = tuple(min(a, f) for a, f in zip(adaptive, fixed))
adaptive_regret = tuple(a - o for a, o in zip(adaptive, oracle))
fixed_regret = tuple(f - o for f, o in zip(fixed, oracle))
```

For menu `{A,F}` this gives:

```text
oracle = (1,2,2,2)
regret(A) = (0,1,1,1) -> max 1
regret(F) = (1,0,0,0) -> max 1
MINIMAX_REGRET = TIE
```

This is correct for the declared two-policy menu.

### E2 — external terminology / formal pressure
Standard minimax-regret definitions make regret relative to the best achievable act/rule under each state, so the comparator/action set participates in the benchmark. MIT 16.422 describes regret as opportunity loss relative to the best possible outcome under a state. The Cambridge *Economics & Philosophy* formulation writes realization regret with `max_{a' in A}`. The 2026 *Econometric Theory* treatment-rule formulation writes `R(delta,s)=sup_{d in D}u(d,s)-u(delta,s)` and explicitly discusses restrictions on `D`.

These sources do **not** authorize an ALEX policy semantics. They support only the mathematical dependency claim: under ordinary regret definitions, the feasible/comparator set is an input to the regret benchmark.

### E3 — exact Wolfram calculation
Keep `A` and `F` unchanged and keep the criterion `minimax regret` unchanged. Add only a third available policy:

```text
G = (100,0,0,0)
```

where lower cost is better.

Wolfram exact result:

```text
menu {A,F}:
  oracle = (1,2,2,2)
  max regret(A,F) = (1,1)
  ranking among A,F = TIE

menu {A,F,G}:
  oracle = (1,0,0,0)
  max regret(A,F,G) = (3,2,99)
  ranking among unchanged A,F = FIXED < ADAPTIVE
```

No A/F statewise cost moved. No prior was introduced or changed. The minimax-regret criterion did not change. Only the available comparator menu changed.

## Claims

| ID | Claim | Class | Supporting evidence path | Counterevidence | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #114 materially supersedes the previous no-delta state as a live ALEX frontier. | observed | current repo / PR #114 exact head | PR remains draft/non-canonical | supported locally |
| C2 | PR #114 correctly separates statewise costs from criterion-dependent rankings. | observed | PR #114 finite witness | none found in inspected finite arithmetic | supported for fixture |
| C3 | Under the regret construction used by PR #114, regret is not an intrinsic property of one policy's cost vector; it also depends on the comparator/action menu used to construct the statewise oracle. | inference backed by exact calculation + scholarly definition | E1 -> E2 -> E3 | alternative ALEX contract could intentionally freeze the menu implicitly as part of the experiment | supported as dependency claim |
| C4 | The current PR receipts the oracle values but does not hostile-test a same-policies/same-criterion/different-menu case. | observed | PR #114 diff and issue #113 controls C1–C8 | the current `_COSTS` object implicitly exposes the two-policy menu | supported |
| C5 | ALEX should add a generic decision-theory runtime or canonical feasible-set ontology. | proposal | none | exceeds demonstrated need | **not earned** |

## Finding

The newly exposed non-collapse is:

```text
POLICY COST VECTOR
!=
REGRET VECTOR

MINIMAX-REGRET CRITERION
!=
COMPARATOR / FEASIBLE POLICY MENU

SAME POLICIES + SAME COSTS + SAME CRITERION
!=
SAME REGRET RANKING
WHEN THE COMPARATOR MENU CHANGES
```

Candidate seal:

> **REGRET REMEMBERS WHAT ELSE COULD HAVE BEEN DONE.**

More mechanically:

```text
REGRET RECEIPT = POLICY COSTS + STATE SPACE + COMPARATOR MENU + REGRET CRITERION
```

where this equality is a research anatomy, not a promoted schema.

## Contradictions and alternatives

### Competing reading A — no bug; menu already implicit
The frozen `_COSTS` dictionary contains exactly `ADAPTIVE` and `FIXED`, and the returned receipt includes `costs`. A consumer can therefore reconstruct the current menu. On this reading there is no arithmetic defect and no missing data in the current fixture.

### Competing reading B — still a provenance seam
Issue #113's anatomy explicitly names `POLICY / ACTION SET`, but its hostile controls pressure criterion and prior identity, not the fact that minimax regret is **menu-relative**. A later replay that compares the same named policies after adding/removing an admissible policy could attribute a changed regret ranking to the policies or criterion unless menu identity is treated as a first-class consumed input.

Both readings can be true simultaneously: the present fixture is replayable while the unpressured dependency remains a future failure surface.

## Pressure

- **Direct counterexample:** E3. Same A/F vectors and same minimax-regret criterion; adding G changes A-vs-F from tie to FIXED winning.
- **Nearest boring explanation:** minimax regret is definitionally benchmark-relative; the result is ordinary opportunity-loss arithmetic, not a new ALEX ontology.
- **Independence/lineage:** MIT and Cambridge sources are separate publications, but conceptual lineage is not established as independent; all may descend from standard Savage-style regret theory. Independence is therefore **unknown** and unnecessary for the exact finite counterexample.
- **Anachronism/memorization:** not material; current source text/formulae were retrieved, and the finite calculation is exact.
- **Rights/egress:** only public documentation/article text and repository text were sent to external services. No local corpus/page bytes were egressed.
- **Replay impersonation:** exact arithmetic replay does not establish that ALEX must adopt this definition universally; it establishes only what follows under PR #114's current regret construction.
- **Forced equilibrium:** avoided. The alternative “menu already implicit; no code change needed” remains live.

## Residual fog

1. Whether future ALEX consumers will ever compare regret receipts across changing admissible policy menus is not established.
2. Whether `policy/action set` should be a separately named receipt coordinate or whether the existing `costs` mapping is already the smallest sufficient carrier remains unresolved.
3. No claim is made about randomized/mixed policies, dominance pruning, endogenous feasibility, or infinite action spaces; those doors are deliberately unopened.

## Smallest next discriminators / repo-worthy moves

1. **`MENU-RELATIVE-REGRET-001`** — add one hostile control using exactly `A`, `F`, and `G=(100,0,0,0)`; require the receipt to show `{A,F}: TIE` and `{A,F,G}: FIXED`, while asserting A/F costs and criterion identity are unchanged.
2. If that control reveals no practical ambiguity because `costs` already fully receipts the menu, **stop** and document the consumed-menu dependency in the experiment rather than adding machinery.
3. Only if a real replay consumer can erase or mutate the menu, add the smallest explicit coordinate such as `comparator_menu` / `feasible_policy_set_ref`; do not build a generic decision runtime.

## Receipt

- **Researcher/agent:** ALEXDEEPDIVE automation / ChatGPT
- **Tool/model boundary:** GitBook orientation attempt; GitHub repository/PR inspection and durable write; public web scholarship retrieval; Wolfram Language exact arithmetic.
- **External byte egress:** public repository text and public scholarly/web material only; no source corpus or private research bytes.
- **Durable location:** `research/ALEX-DEEPDIVE-2026-09-16-0523-MENU-NOT-REGRET.md`
- **Promotion:** none
