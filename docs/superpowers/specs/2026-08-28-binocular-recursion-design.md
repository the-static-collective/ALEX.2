# BINOCULAR-RECURSION-001 — Dual-Layer Research Formation

**Date:** 2026-08-28  
**Status:** ARCHITECTURAL DESIGN · IMPLEMENTATION NOT YET ADMITTED  
**Repository:** `the-static-collective/ALEX.2`

## 0. Purpose

ALEX needs a bounded research method for a recurring formation pattern:

> Hold the simplest surviving explanation and the fullest presently lawful consequence field at the same time, then inspect the unresolved tension between them without allowing either layer to silently become evidence or authority.

The method is named **`BINOCULAR-RECURSION-001`**.

It is a research-formation operator, not a truth engine.

Its compact form is:

```text
FREEZE
  ↓
COMPRESS || EXPAND
  ↓
TENSION
  ↓
ATTRIBUTABLE UPDATE
  ↓
REPEAT
```

The motivating intuition is stereoscopic rather than averaging: two views are preserved because their disparity may carry information that either view alone loses.

Hard line:

```text
COMPRESSION != TRUTH
EXPANSION != POSSIBILITY LICENSE
TENSION != EVIDENCE
NOVELTY != SUPPORT
```

---

## 1. Architectural ancestry

This design extends existing ALEX laws rather than replacing them.

Relevant inherited distinctions include:

```text
discovery path != evidence path
received premise != admitted premise
agreement != independent corroboration
projection != source
same surface != same causal state
replay match != historical identity
```

It also composes naturally with existing executable work around projection invariance and projection break:

- a bounded world or field is held fixed enough to compare views;
- a declared intervention or traversal may alter what becomes visible;
- the resulting difference is attributable only when the formation path remains receipted;
- authority must not silently expand because a new relation became visible.

`BINOCULAR-RECURSION-001` adds one missing research distinction:

```text
APERTURE POSITION != APERTURE TRAJECTORY
```

A static focus set may be identical while the ordered path through that set differs materially.

---

## 2. Research problem

A common failure mode appears when research is forced into one of two poles.

### 2.1 Overcompression

```text
"everything is really just X"
```

The researcher finds a compact generator and then erases consequences, exceptions, unresolved branches, or counterexamples that do not fit it.

### 2.2 Overexpansion

```text
"X connects to everything"
```

The researcher follows suggestive relations without preserving premise ancestry, branch conditions, or stopping rules. Interesting consequences then feed backward as if they had supported the premises that generated them.

### 2.3 Required posture

ALEX should keep both pressures live:

```text
LEFT LENS  — minimum sufficient / generative compression
RIGHT LENS — maximum presently lawful consequence expansion
DEPTH      — attributable disparity between them
```

Neither lens closes the other.

---

## 3. Core objects

Let the current constituted research field be `X_t`.

Define a compression view:

```text
C(X_t)
```

as a candidate minimum structure sufficient to account for the presently relied-upon field under declared constraints.

Define an expansion view:

```text
E_R(X_t)
```

as the presently lawful consequence closure reachable from `X_t` under an explicit relation/rule set `R_t`.

The binocular state is:

```text
B(X_t) = ( C(X_t), E_R(X_t) )
```

The tension surface is not assumed numeric:

```text
τ_t = DISPARITY( C(X_t), E_R(X_t) )
```

`τ_t` is a typed ledger of disagreement, residual, missing consequence, surplus branch, contradiction, or unresolved relation.

An update is permitted only when attributable:

```text
X_(t+1) = U(X_t, τ_t, attributable_receipts)
```

The next binocular pass is then computed from the descendant field rather than silently rewriting `X_t`.

---

## 4. The ALEX protocol

### 4.1 FREEZE

Record the current inquiry cut before recursive work begins.

At minimum preserve:

- field/world digest or bounded-context digest;
- question or H0 exactly as received;
- currently admitted premises;
- currently live unresolved premises;
- relation/rule profile used for consequence expansion;
- projection/decoder/traversal profile where material;
- authority state.

`FREEZE` does not mean the inquiry can never change. It means each change must descend from an attributable prior state.

### 4.2 COMPRESS

Construct one candidate minimum explanation or generator for the current field.

Compression may:

- remove redundant statements;
- identify repeated structure;
- factor a shared generator;
- expose a smaller dependency basis;
- propose an invariant under the current cut.

Compression may not:

- delete a live counterexample because it is inconvenient;
- silently convert a heuristic into a premise;
- erase branch conditions;
- relabel unresolved material as noise merely because it complicates the model;
- promote compactness into truth.

The compression result is a **proposal** unless separately supported.

### 4.3 EXPAND

From the same frozen field, follow each presently admitted relation or rule toward its logical consequence boundary.

Expansion must preserve branches.

Conceptual form:

```text
NOW
├─ if A holds → A1 → A2 → ...
├─ if B holds → B1 → B2 → ...
├─ unresolved C → unresolved frontier
└─ contradiction D → explicit break
```

Each branch records:

- parent node or premise refs;
- rule/relation used;
- branch condition;
- status: `ENTAILED | INFERRED | SPECULATIVE | CONTRADICTED | UNRESOLVED`;
- whether the branch remains inside the frozen field or introduces a proposed premise.

A proposed premise may open a separate descendant experiment. It may not be smuggled into the same expansion closure as already admitted input.

### 4.4 TENSION

Compare the compression and expansion views without averaging them away.

Minimum tension classes:

```text
MISSING_CONSEQUENCE
  compression cannot generate a live consequence found by expansion

SURPLUS_GENERATOR
  compression contains machinery not required by any surviving branch

UNEXPLAINED_RESIDUAL
  field material survives but neither view accounts for it

BRANCH_DEPENDENCE
  a conclusion exists only under a visible branch condition

CONTRADICTION
  admitted premises/rules produce mutually incompatible descendants

TRAJECTORY_DEPENDENCE
  different lawful traversal orders over the same focus membership produce different formation results

STABLE_MATCH
  compression re-expands to the same declared consequence surface under the tested cut
```

A tension class is an observation about the formation specimen. It is not support for an external claim.

### 4.5 ATTRIBUTABLE UPDATE

Only an explicit receipt may change the next constituted state.

Allowed update sources include:

- newly inspected evidence;
- explicit premise admission or withdrawal;
- corrected reading/transcription/translation;
- declared rule-profile change;
- acknowledged contradiction resolution;
- a human or owning-project decision within its authority boundary.

Not sufficient by themselves:

- novelty;
- elegance;
- recurrence;
- model confidence;
- expansion size;
- compression ratio;
- tension magnitude;
- user prompting pressure.

### 4.6 REPEAT

Run the two lenses again from the descendant field and preserve pass ancestry.

The protocol is recursive because the output of one lawful pass may change which structures become visible in the next. It is not recursive permission to cite prior model output as evidence.

---

## 5. Discovery-trigger boundary

The motivating prompt contains explicit novelty pressure: look again with the expectation that something new may become visible.

That pressure is permitted as a **discovery trigger**.

It is forbidden as support.

Hard law:

```text
THE PROMPT MAY CAUSE DISCOVERY.
THE PROMPT MAY NOT SUPPORT THE DISCOVERED CLAIM.
```

For any newly proposed relation `N`:

```text
trigger(N) = formation event that caused N to be noticed
basis(N)   = source / derivation material that bears N

trigger(N) != basis(N)
```

A lawful result may therefore say:

```text
"This traversal made relation R newly visible."
```

It may not say:

```text
"Relation R is supported because this traversal revealed it."
```

---

## 6. Ordered traversal receipt

`BINOCULAR-RECURSION-001` requires trajectory when order is materially claimed.

Conceptual sidecar:

```json
{
  "schema": "alex.binocular-traversal/v0",
  "field_digest": "sha256:...",
  "initial_projection_digest": "sha256:...",
  "policy": "bidirectional_recursive",
  "trajectory": ["A", "B", "C", "B", "A", "D", "C"],
  "pass": 3,
  "compression_profile_digest": "sha256:...",
  "expansion_profile_digest": "sha256:...",
  "authority_digest": "sha256:..."
}
```

The trajectory is formation ancestry, not evidentiary support.

Two runs with the same focus membership but different ordered trajectories must not be silently canonicalized into one formation identity when the result differs.

---

## 7. Terminal states

A bounded recursive run must stop or report why it cannot.

Required terminal family:

```text
FIXED
  another pass yields no material typed tension delta under the declared profiles

CYCLE
  the run revisits a prior binocular state or small repeating family

RESIDUAL
  a stable compression/consequence core exists with unresolved remainder

DIVERGENT
  successive passes keep producing structurally new unresolved material under the bounded pass limit

REFUSE
  a constitutional violation invalidates the run

INSUFFICIENT_TO_TEST
  required receipts, premises, traversal, or rule declarations are missing
```

`FIXED` means stable under this operator and cut. It does not mean true.

---

## 8. Executable evaluator contract

The first implementation should be a pure Python evaluator following the pattern of `projection_invariance.py` and `projection_break.py`.

Proposed public function:

```python
def evaluate_binocular_recursion_case(case: dict) -> dict[str, object]:
    ...
```

The evaluator does **not** perform open-ended language-model reasoning. It audits a supplied formation trace for constitutional validity.

Input concept:

```json
{
  "case_id": "specimen-001",
  "field_digest": "sha256:...",
  "authority_digest": "sha256:...",
  "passes": [
    {
      "pass": 0,
      "trajectory": ["A", "B", "A", "C"],
      "compression": {
        "proposal_digest": "sha256:...",
        "basis_refs": ["r1", "r2"]
      },
      "expansion": {
        "closure_digest": "sha256:...",
        "branch_receipts": ["b1", "b2"],
        "introduced_premise_refs": []
      },
      "tensions": [
        {"type": "MISSING_CONSEQUENCE", "receipt_refs": ["b2", "r2"]}
      ],
      "update": {
        "kind": "NONE",
        "receipt_refs": []
      }
    }
  ],
  "terminal": "RESIDUAL"
}
```

Output concept:

```json
{
  "case_id": "specimen-001",
  "disposition": "ACCEPT",
  "reason_code": null,
  "terminal": "RESIDUAL",
  "validated_passes": 1,
  "tension_types": ["MISSING_CONSEQUENCE"],
  "receipt_survivors": ["b1", "b2", "r1", "r2"]
}
```

`ACCEPT` means only that the supplied research formation obeys the declared protocol.

It does not accept the researched claim as true.

---

## 9. Required refusal cases

The evaluator must refuse or mark insufficient at least these cases.

### 9.1 `DISCOVERY_TRIGGER_AS_SUPPORT`

A novelty cue, prompt, search motive, or traversal receipt appears in `basis_refs` as if it supported the newly proposed claim.

Disposition: `REFUSE`.

### 9.2 `UNDECLARED_PREMISE_INJECTION`

Expansion reaches a conclusion using a premise not present in the frozen/admitted field and not declared as a proposed descendant premise.

Disposition: `REFUSE`.

### 9.3 `COMPRESSION_ERASED_LIVE_CONSEQUENCE`

A live branch supported by admitted premises is absent from the compression/re-expansion comparison without an attributable withdrawal/refutation receipt.

Disposition: `REFUSE`.

### 9.4 `ONE_EYE_COLLAPSE`

The run supplies only compression or only expansion while claiming a binocular result.

Disposition: `INSUFFICIENT_TO_TEST`.

### 9.5 `TRAJECTORY_NOT_PRESERVED`

Order-dependent formation is claimed but only unordered focus membership is supplied.

Disposition: `INSUFFICIENT_TO_TEST`.

### 9.6 `AUTHORITY_CHANGED`

Authority digest changes inside the recursive operator without a separately authorized owner transition.

Disposition: `REFUSE`.

### 9.7 `UNATTRIBUTED_UPDATE`

`X_(t+1)` differs materially from `X_t` but no update receipt explains the change.

Disposition: `REFUSE`.

---

## 10. Hostile controls

The first fixture family should include the motivating intervention as one member, plus controls that separate useful mechanism from prompt vibe.

```text
ORIGINAL
  bidirectional recursive return + far-side compression + novelty cue

NO_NEW
  remove explicit novelty demand

ONE_WAY
  traverse once from beginning to end

ONE_PASS
  remove recursion

MECHANICAL
  preserve the operator while replacing poetic language with bare instructions
```

ALEX does not assume what these controls will show.

The discriminating hypothesis is:

> If materially similar lawful discoveries survive `NO_NEW` and `MECHANICAL` but weaken under `ONE_WAY` or `ONE_PASS`, ordered recursive re-encounter is a better candidate explanation than novelty pressure alone.

This remains an empirical/specimen-level result, not a universal cognitive law.

---

## 11. Relationship to existing ALEX protocols

### PRESSURE

`BINOCULAR-RECURSION-001` may operate inside PRESSURE.

PRESSURE asks what survives attack. Binocular recursion adds a particular paired operation:

```text
compress survivor
||
expand survivor consequences
→ inspect mismatch
```

### `{ PEEL. SLEEP .LEEP }`

Formation trace is complementary.

- `PEEL.` may expose how a binocular pass formed;
- `SLEEP` may hold one to three materially live compression or consequence formulations;
- `.LEEP` may replay an attributable pass.

Replay identity remains separate from truth.

### PROJECTION-BREAK-001

`PROJECTION-BREAK-001` asks where equivalent observer worlds first diverge under the same attributable intervention.

`BINOCULAR-RECURSION-001` asks whether two simultaneous research views of one constituted field expose a typed disparity and whether recursive updates remain attributable.

They can be composed but neither subsumes the other.

---

## 12. Dogram boundary

Dogram may calculate deterministic properties of a binocular specimen, for example:

- first differing boundary between traces;
- reachability closure under an explicit graph;
- remove-one effects;
- four-cell interaction patterns;
- re-expansion equality or difference under declared deterministic operators.

Hard boundary:

```text
DOGRAM CALCULATES DISPARITY.
ALEX CLASSIFIES RESEARCH FORMATION.
HUMAN / OWNER ADMITS CONSEQUENCE.
```

A Dogram receipt may be consumed by ALEX as a calculation receipt. It is not evidence by itself.

---

## 13. Implementation shape

After design approval, the implementation should remain small:

```text
alex_runtime/
  binocular_recursion.py

tools/
  run_binocular_recursion.py

tests/
  test_binocular_recursion.py
  fixtures/
    binocular_recursion/

skills/alex/references/
  binocular-recursion.md
```

The implementation should reuse existing digest/receipt conventions where possible and should not introduce a model dependency, network dependency, or generalized workflow engine.

---

## 14. Acceptance criteria

The first implementation is complete only when:

1. a lawful dual-layer specimen returns `ACCEPT` without promoting its conclusions;
2. novelty/discovery pressure used as support returns `REFUSE`;
3. undeclared premise injection returns `REFUSE`;
4. compression that silently erases a live consequence returns `REFUSE`;
5. an order-dependent case without trajectory returns `INSUFFICIENT_TO_TEST`;
6. authority drift returns `REFUSE`;
7. fixed, cycle, residual, and divergent terminal states are machine-distinguishable;
8. repeated evaluation of the same valid specimen is deterministic;
9. the runner performs JSON-in / JSON-out only;
10. the portable ALEX reference explains the method without claiming universal cognitive or evidentiary authority.

---

## 15. Constitutional compression

```text
FREEZE THE FIELD.

HOLD AT ONCE:
  THE SMALLEST THING THAT EXPLAINS IT
  AND
  EVERYTHING THAT LAWFULLY FOLLOWS FROM IT.

DO NOT AVERAGE THE DIFFERENCE.
RECEIPT THE TENSION.

CHANGE THE FIELD ONLY BY ATTRIBUTABLE UPDATE.
REPEAT.

NEWLY VISIBLE != NEWLY TRUE.
TRIGGER != SUPPORT.
STABILITY != TRUTH.
```
