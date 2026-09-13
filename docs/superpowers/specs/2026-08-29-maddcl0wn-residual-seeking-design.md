# MADDCL0WN — Residual-Seeking Research Loop

**Date:** 2026-08-29  
**Status:** DESIGN SLICE · HUMAN CONCEPT APPROVAL RECEIVED · WRITTEN SPEC REVIEW PENDING · NO RUNTIME PROMOTION  
**Primary owner:** ALEX  
**Calculation owner:** Dogram  
**Observer-local exposure owner:** 3rdi  
**Capability/reach owner:** LOADOUT  

> **STRANGE HYPOTHESES SHOULD PAY FOR THEIR NEXT QUESTION.**

---

## 0. Decision

The recent MADDCL0WN, syzygy, CHRONOBODY, observer-cut, and LOADOUT work has crossed a useful threshold.

The next frontier is **not** another pattern generator and **not** another relation vocabulary.

The next frontier is to make a failed or incomplete formal relation produce a bounded, attributable proposal for the **next experiment most capable of distinguishing why it failed**.

Working center:

```text
RESIDUAL-PROBE-001
```

Core loop:

```text
PROPOSE RELATION
  ↓
CONSTITUTE THE RELATION
  ↓
CALCULATE RESIDUAL
  ↓
FORM LIVE EXPLANATION FAMILY
  ↓
PROPOSE DISCRIMINATING INTERVENTION
  ↓
GATE / EXECUTE OUTSIDE ALEX
  ↓
OBSERVE
  ↓
REPARTITION THE EXPLANATIONS
  ↓
REFINE / KILL / HOLD / REIFY
  ↓
PRESSURE AGAIN
```

The important change is conceptual:

```text
FAILED RELATION
  !=
USELESS RELATION
```

A structured failure can be a coordinate for the next question.

This design does **not** add a runtime operator, autonomous experiment executor, authority surface, shared ontology, truth oracle, probability engine, or automatic promotion path.

---

## 1. Ancestry: what already exists

This design is a descendant of already-landed or already-held work. It must not silently rename that work as novelty.

### ALEX `MADDCL0WN-001`

Draft PR #34 established controlled broken-decoder pressure:

```text
hold source fixed
vary declared decoder axes
project
compare
classify ash / recurrence / bifurcation / interaction / invariant / unresolved
pressure ancestry
ring only typed survivors
```

Standing membrane:

> **A BROKEN KEY DOES NOT PROVE ITS READING. IT CAN REVEAL WHAT THE READING DEPENDS ON.**

This design extends the method after classification. It does not replace it.

### Dogram `SYZYGY-RING-001`

Merged PR #14 already establishes the relation receipt:

```text
(ambient, generators, relation, residual, decoder)
```

and already keeps:

```text
exact relation
ambient dependence
decoder dependence
residual
higher syzygy / formation lift
```

Therefore **syzygy itself is not the new primitive here**.

### ALEX `SYZYGY-PRESSURE-001`

Merged PR #46 already owns research pressure around generator identity, ambient migration, decoder/parser dependence, hostile siblings, and phenomenal overclaim.

### 3rdi `SYZYGY-CUT-001`

Merged PR #9 already preserves relation exposure under a declared observer / ambient / decoder / known-at cut.

### ALEX CHRONOBODY

CHRONOBODY already makes exact historical research bodies executable without promoting them into the constituted present.

### LOADOUT executable floor

LOADOUT PR #1 already owns deterministic:

```text
REACH
FENCE
BIND
DELTA
ABLATE
TRACE
```

and preserves proposal-only reflection plus non-expanding authority.

### ALEX `THREE-CLOCK-ERASURE-001`

Issue #47 already asks which coordinates actually prevent false collapse among:

```text
world / occurrence cut
observer cut
reasoning body-time
compile constitution, if material
```

This remains a feeder crucible, not a subroutine silently absorbed by MADDCL0WN.

---

## 2. Governing compression

Current MADDCL0WN is good at asking:

```text
WHAT CHANGES WHEN THE KEY CHANGES?
```

The descendant question is:

```text
WHAT SHOULD WE CHANGE NEXT
IF WE WANT TO LEARN WHY THIS RELATION FAILED?
```

The method therefore moves from **residual recording** to **residual-guided discrimination**.

Not:

```text
candidate failed
→ discard candidate
```

but:

```text
candidate
→ residual r
→ candidate explanations of r
→ bounded interventions
→ predicted distinctions
→ choose one useful discriminator
→ observe
→ refine candidate family
```

The method is allowed to return:

```text
NO LAWFUL DISCRIMINATOR FOUND
```

That is a successful bounded result.

---

## 3. Constitutional non-collapses

Freeze these before any implementation proposal:

```text
RESIDUAL != ERROR MESSAGE
RESIDUAL != NOISE BY DEFAULT
RESIDUAL != EVIDENCE FOR A FAVORED EXPLANATION
ZERO RESIDUAL != TRUTH
NONZERO RESIDUAL != FALSITY OF EVERY NEARBY MODEL
DISCRIMINATOR != EXPERIMENT AUTHORITY
PROPOSED PROBE != EXECUTED PROBE
EXECUTED PROBE != CLEAN INTERVENTION
OBSERVATION != INTERPRETATION
PARTITION REFINEMENT != TRUTH VERDICT
BEST AVAILABLE QUESTION != UNIQUE BEST QUESTION
RELATION != CARRIER AUTOMATICALLY
REIFIED CARRIER != PROMOTED GENERATOR
PROMOTED GENERATOR != AUTHORITY
SAME OUTPUT != SAME CALCULATION HISTORY
SAME NAMED DECODER != SAME EXECUTABLE DECODER BODY
LOCAL EXACTNESS != GLOBAL EXACTNESS
CAPABILITY COMPOSITION != UNION OF INDEPENDENT SAFETY CLAIMS
```

Two older ALEX lines remain load-bearing:

```text
discovery path != evidence path
received premise != admitted premise
```

---

## 4. The residual object

For a declared candidate relation `R` over generators `G` in ambient `A` under decoder `D`, Dogram may calculate:

```math
r = R(G)
```

But MADDCL0WN should not assume every residual is a comparable scalar.

A practical residual receipt may be:

```yaml
residual:
  relation_receipt_ref:
  value:
  value_type:
  ambient_ref:
  decoder_ref:
  generator_refs:
  observer_cut_ref:
  body_ref:
  comparison_domain:
  exact: true|false|unknown
```

`value` may be:

- scalar defect;
- vector defect;
- unmatched edge set;
- violated constraint identities;
- surviving graph component;
- rank defect;
- type change;
- incomparability marker;
- another Dogram-owned typed calculation.

The ALEX layer must not coerce unlike residuals onto one fake numeric scale merely to rank them.

---

## 5. Residual signatures

A single residual is often insufficient to select a useful question.

Let a live candidate explanation family be:

```text
C = {c1, c2, ..., cn}
```

Each candidate should declare what it expects to happen under a bounded family of possible interventions.

A **residual signature** is not necessarily one number. It is the pattern of predicted residual behavior across declared pressure coordinates.

Example:

```text
candidate c1:
  ambient swap        -> residual disappears
  decoder-body swap   -> residual unchanged
  hidden generator    -> residual disappears

candidate c2:
  ambient swap        -> residual unchanged
  decoder-body swap   -> residual disappears
  hidden generator    -> residual unchanged

candidate c3:
  ambient swap        -> residual unchanged
  decoder-body swap   -> residual unchanged
  hidden generator    -> residual changes type
```

The point is not that those predictions are correct.

The point is that they define which intervention could separate the candidate family.

---

## 6. `RESIDUAL-PROBE-001`

### 6.1 Input

Minimum inquiry packet:

```yaml
source_refs:
held_coordinates:
relation_receipts:
candidate_explanations:
allowed_intervention_family:
forbidden_effects:
observer_cut:
stop_condition:
promotion_boundary:
```

Each candidate explanation must be attributable to a proposal or derivation path.

A candidate explanation may be boring.

Examples:

```text
parser boundary
decoder implementation drift
ambient algebra mismatch
missing generator
redundant generator
observer-local hiddenness
rounding / normalization artifact
source drift
historical inheritance
actual model inadequacy
unresolved
```

### 6.2 Candidate intervention

A proposed intervention `q` must declare:

```yaml
question_id:
changes_exactly:
holds_fixed:
predicted_observation_classes_by_candidate:
required_capabilities:
expected_effects:
observer_requirements:
execution_owner:
```

ALEX may propose `q`.

ALEX does not execute `q` merely because it is informative.

### 6.3 Discrimination criterion

For the first specimen, avoid pretending to need a full Bayesian or information-theoretic engine.

Use a simpler deterministic target:

> Prefer a lawful intervention expected to split the current candidate family into at least two distinguishable observation classes while changing the fewest declared coordinates.

Candidate ranking may therefore be lexicographic:

```text
1. lawful / executable through owning gate?
2. changes exactly one declared coordinate if possible?
3. separates more than one live candidate class?
4. avoids source drift?
5. preserves comparable output type?
6. lower consequence / narrower reach preferred when discrimination is equal?
7. deterministic/replayable preferred when otherwise equal?
```

This is a research design heuristic, not a universal optimal-experiment theorem.

### 6.4 Output

ALEX emits only an inert proposal:

```yaml
residual_probe_proposal:
  source_refs:
  candidate_partition_before:
  selected_question:
  expected_partition:
  rejected_questions:
  refusal_reasons:
  authority: none
  execution: not_performed
```

---

## 7. Execution boundary

The proposed probe must cross ordinary owner-local consequence gates.

Conceptual route:

```text
ALEX
  proposes discriminating question
        ↓
LOADOUT
  computes reach / fence / bind
        ↓
OWNING WORLD GATE
  admits or refuses consequence
        ↓
EXECUTION
        ↓
3rdi
  preserves observer-local exposure / known-at cut
        ↓
Dogram
  calculates declared deltas / residuals
        ↓
ALEX
  compares observation with predicted partition
```

This ordering is illustrative, not a universal orchestration mandate.

The ownership boundary is not illustrative:

```text
ALEX DOES NOT MINT EXECUTION AUTHORITY.
LOADOUT DOES NOT MINT RESEARCH SUPPORT.
DOGRAM DOES NOT DECIDE MEANING.
3RDI DOES NOT BECOME A TRUTH SERVICE.
```

---

## 8. Partition refinement

Suppose the candidate family begins as:

```text
C0 = {c1, c2, c3, c4}
```

A probe may predict:

```text
outcome Oa -> {c1, c2}
outcome Ob -> {c3}
outcome Oc -> {c4}
```

After actual observation `Oa`, the updated family may become:

```text
C1 = {c1, c2}
```

This is useful even though neither remaining candidate is established.

ALEX should preserve:

```yaml
partition_before:
predicted_partition:
observation:
partition_after:
killed_candidates:
surviving_candidates:
unexpected_outcome:
```

An observation not represented in any candidate prediction should not be forced into the nearest bucket.

Return:

```text
MODEL FAMILY INCOMPLETE
```

and preserve the novel residual.

---

## 9. The promotion membrane: `DERIVE != REIFY != PROMOTE`

Residual-seeking MADDCL0WN will naturally discover relations among relations.

That creates a dangerous pressure toward ontology inflation.

The membrane is therefore explicit.

### 9.1 DERIVE

A relation is derived when an attributable calculation or semantic derivation produces a relation receipt.

```text
OBJECTS
  ↓
DERIVED RELATION
```

The relation may be exact, broken, local, decoder-dependent, or unresolved.

### 9.2 PRESSURE PRESENTATION

Before reification, pressure whether the relation is intrinsic to the declared target or merely an artifact of representation.

Required question:

> Did the relation appear because the structure demanded it, or because the presentation supplied redundant carriers?

### 9.3 REIFY

A derived relation may be given a durable inert identity so later operations can refer to it.

```text
RELATION RECEIPT
  ↓ declared formation lift
INERT RELATION-CARRIER
```

Reification grants:

```text
addressability
lineage
replay reference
comparison identity
```

Reification does **not** grant:

```text
authority
support
truth
execution
semantic universality
permission to act as a generator
```

### 9.4 PROMOTE

Promotion is the separate act that allows a reified relation-carrier to participate as an input/generator at a declared higher layer.

```text
REIFIED RELATION-CARRIER
  ↓ explicit gate
PROMOTED GENERATOR AT LEVEL k+1
```

Promotion must preserve its level and ancestry.

Never rewrite:

```text
relation at level k
```

as though it had always been:

```text
primitive generator at level k
```

---

## 10. `REDUNDANT-PRESENTATION-001`

This is the mandatory hostile sibling for relation reification.

### 10.1 Failure being attacked

A generating presentation can contain redundant carriers.

Adding a redundant generator can create a visible relation without creating a new intrinsic dimension of the generated object.

Therefore:

```text
MORE RELATIONS IN THIS PRESENTATION
  !=
MORE INTRINSIC STRUCTURE IN THE TARGET
```

### 10.2 Tiny mathematical specimen

Compare a rank-two target under two presentations.

Minimal presentation:

```text
G1 = {e1, e2}
```

Redundant presentation:

```text
G2 = {e1, e2, e1 + e2}
```

`G2` introduces a nontrivial relation among the presented generators:

```text
-e1 - e2 + (e1 + e2) = 0
```

but the generated rank remains two.

This is useful precisely because the relation is real **in the presentation** while failing to establish a new target dimension.

### 10.3 Reification pressure

Before relation-carrier promotion, ask:

```text
Does the relation survive removal of redundant generators?
Does it survive alternate minimal generating presentations?
Does its role change when presentation ancestry changes?
Is it intrinsic, presentation-relative, or unresolved?
```

Possible classification:

```text
INTRINSIC_CANDIDATE
PRESENTATION_RELATIVE
REDUNDANCY_GHOST
UNRESOLVED
```

These are research classifications only.

---

## 11. Feeder crucible A — `RELATION-CONSTITUTION-001`

### H0

A relation receipt may need to preserve the **exact executable constitution** of the decoder/calculator when implementation identity can change whether the relation holds.

### Specimen

Hold one source fixed.

Run nominally the same named decoder under:

```text
A: ambient Ω1 + decoder D@sha1
B: ambient Ω2 + decoder D@sha1
C: ambient Ω1 + decoder D@sha2
D: ambient Ω1 + decoder D@sha1 + observer missing one generator
```

Expected classifications may include:

```text
A vs B -> AMBIENT_BREAK
A vs C -> DECODER_CONSTITUTION_BREAK
A vs D -> AVAILABILITY_BREAK
```

The especially useful control is:

```text
same output
!=
same calculation history
```

### Kill condition

If exact decoder-body identity never prevents false collapse across hostile specimens, keep it as optional provenance rather than a first-class relation coordinate.

### Status

```text
PRESSURE / HOLD
```

Do not universalize this coordinate before it pays rent.

---

## 12. Feeder crucible B — `COMPOSITE-REACH-001`

This belongs to LOADOUT.

### H0

Individually bounded capabilities can compose into an end-to-end reachable effect that no single capability advertises.

Example:

```text
READ
TRANSFORM
PUBLISH
```

may each be individually lawful while:

```text
READ + TRANSFORM + PUBLISH
```

creates a route to an undeclared external effect.

### Important naming correction

Do **not** call this a capability syzygy merely because it emerged during syzygy work.

The primary object is:

```text
interaction-born reachability
```

Dogram may later calculate a formal interaction object if useful, but LOADOUT owns the capability consequence question.

### Smallest specimen

Use three inert fake adapters.

Require:

- each adapter individually passes ordinary bind pressure;
- all pairs remain within declared reach;
- one triple composition exposes an undeclared end-to-end effect;
- no authority field expands;
- the parent compile remains immutable;
- the result is a refusal or bounded interaction receipt, not automatic remediation.

---

## 13. Feeder crucible C — `THREE-CLOCK-ERASURE-001`

Existing ALEX issue #47 remains the owner.

Its principle composes directly with this design:

> **A coordinate earns survival only when removing it creates a false collapse that can no longer be attributed correctly.**

Residual-seeking work should therefore resist receipt bloat.

Potential relation coordinates:

```text
ambient
decoder
observer cut
body-time
compile constitution
formation ancestry
```

must earn survival by preventing a demonstrated collapse.

The target is not maximal provenance.

The target is:

```text
MINIMUM RECEIPT CAPABLE OF KEEPING UNLIKE HISTORIES UNLIKE
```

---

## 14. Feeder crucible D — observer-local residuals

3rdi already proves that the same surface can expose different relation spaces under different lawful cuts.

Residual-seeking work inherits the stronger consequence:

```text
SAME CANDIDATE RELATION
+ DIFFERENT LAWFUL PROJECTION
→ DIFFERENT RESIDUAL MAY BE LEGITIMATE
```

A historical residual therefore needs to remain addressable as:

```text
RESIDUAL UNDER PROJECTION P AT CUT T
```

rather than later being rewritten as globally wrong merely because hidden information became visible.

Potential outcome vocabulary:

```text
EXACT_UNDER_PROJECTION
BROKEN_AFTER_DISCLOSURE
AMBIENT_BREAK
DECODER_BREAK
AVAILABILITY_BREAK
BODY_BREAK
UNKNOWN
```

3rdi owns exposure. ALEX owns the later comparison and claim discipline.

---

## 15. `RESIDUAL-SEEKING MADDCL0WN` full loop

The complete research loop becomes:

```text
0   PRESERVE H0
1   TYPE SOURCE / WORLD / CUT
2   DECLARE BASELINE DECODER AND AMBIENT
3   DECLARE RELATION CANDIDATE
4   CALCULATE RESIDUAL
5   CLASSIFY WHAT THE RESIDUAL ACTUALLY IS
6   BUILD LIVE EXPLANATION FAMILY
7   DECLARE ALLOWED INTERVENTION FAMILY
8   PREDICT WHICH CANDIDATES EACH INTERVENTION WOULD SEPARATE
9   REFUSE POST-HOC OR MULTI-COORDINATE SMUGGLING
10  PROPOSE THE NARROWEST USEFUL DISCRIMINATOR
11  ROUTE THROUGH LOADOUT / OWNER GATE
12  EXECUTE, IF ADMITTED
13  PRESERVE OBSERVER-LOCAL RECEIPT
14  CALCULATE NEW DELTA / RESIDUAL
15  REPARTITION EXPLANATION FAMILY
16  KILL WHAT THE OBSERVATION ACTUALLY KILLED
17  PRESERVE UNEXPECTED OUTCOMES AS NEW RESIDUALS
18  PRESSURE DERIVE / REIFY / PROMOTE BOUNDARY
19  REPEAT OR STOP
```

Stopping conditions include:

```text
one candidate remains but is not yet supported
no lawful discriminator exists
remaining candidates predict identical bounded observations
probe cost/reach exceeds declared boundary
source drift prevents clean comparison
output types become incomparable
model family is incomplete
question is answered at the declared scope
```

---

## 16. Hostile controls

### 16.1 Favored-question laundering

Choose the probe that is most likely to produce the desired answer rather than the one that separates candidate explanations.

```text
REFUSE / CONFIRMATION-SEEKING
```

### 16.2 Post-hoc candidate family

Inspect the observation, then invent the candidate explanations that make it look maximally discriminating.

```text
DISCOVERY ONLY / NOT PROSPECTIVE DISCRIMINATION
```

### 16.3 Multi-coordinate intervention

Change ambient, decoder, source normalization, and observer cut in one probe.

```text
INSUFFICIENT_TO_ATTRIBUTE
```

### 16.4 Hidden source drift

The source itself changes while the experiment is described as a decoder intervention.

```text
REFUSE / SOURCE_DRIFT
```

### 16.5 Type coercion

One candidate predicts graph disconnection and another predicts a scalar defect; the harness forces both into a numeric ranking.

```text
REFUSE / RESIDUAL_TYPE_COLLAPSE
```

### 16.6 Oracle leakage

The discriminator selector sees the hidden correct answer or evaluation oracle.

```text
REFUSE / ORACLE_LEAK
```

### 16.7 Observer leakage

Later-visible evidence is silently injected into an earlier observer's residual or candidate family.

```text
REFUSE / HINDSIGHT_LAUNDERING
```

### 16.8 Decoder-name laundering

Two different executable decoder bodies are treated as identical because they share the same user-facing name.

```text
PRESSURE / DECODER_CONSTITUTION_UNKNOWN
```

### 16.9 Redundancy ghost promotion

A relation appears only because a redundant generator was added and is then promoted as a new intrinsic object.

```text
REFUSE / REDUNDANCY_GHOST
```

### 16.10 Capability union fallacy

Three individually lawful capabilities are assumed safe in composition without checking reachable end-to-end effects.

```text
REFUSE / COMPOSITE_REACH_UNKNOWN
```

---

## 17. First executable specimen, if this written spec is later approved

No implementation is authorized by this document.

The smallest useful future specimen should be synthetic and deterministic.

### Frozen specimen

One held source `S`.

Three candidate relations:

```text
R1 -> residual signature family A
R2 -> residual signature family B
R3 -> residual signature family C
```

Three permitted interventions:

```text
q1 -> ambient swap
q2 -> decoder-body swap
q3 -> reveal one hidden generator
```

Before execution, the fixture declares each candidate's predicted outcome class under each `q`.

The selector must choose one question that separates at least two candidates while changing only one declared coordinate.

Then execute against a hidden synthetic fixture outcome.

Success is **not** choosing the true candidate.

Success is:

```text
1. no oracle leakage;
2. exact attribution of changed coordinate;
3. lawful proposal-only output before gate;
4. deterministic candidate partition refinement after observation;
5. unexpected outcomes remain representable;
6. no promotion from relation to carrier or authority;
7. no cross-organ ownership collapse.
```

---

## 18. Promotion ladder

Keep the ladder explicit:

```text
OVERNIGHT SCOUTPASTE
  ↓
DESIGN SLICE
  ↓ written-spec review
HOSTILE SYNTHETIC SPECIMEN
  ↓
OWNER-LOCAL EXECUTABLE RECEIPTS
  ↓
CROSS-ORGAN COMPOSED SPECIMEN
  ↓
REPLAY / ERASURE / REDUNDANCY PRESSURE
  ↓
METHOD CANDIDATE
  ↓
NORMATIVE PROMOTION ONLY IF IT PAYS RENT
```

Nothing in this document promotes:

```text
MADDCL0WN to universal method
RESIDUAL-PROBE to ALEX kernel
higher syzygy to ontology
relation-carriers to shared schema
body SHA to metaphysical identity
LOADOUT capability interaction to syzygy
observer-local exactness to global truth
```

---

## 19. Kill conditions

Kill or split this design if any of the following occur:

1. A residual-guided selector performs no better than a fixed probe order on the declared specimen family.
2. The method requires a probabilistic truth model before a deterministic discrimination specimen can work.
3. Candidate explanations cannot declare prospectively distinguishable outcomes without smuggling the oracle.
4. Residual typing becomes a universal ontology rather than owner-local calculational output.
5. Relation reification cannot be kept separate from promotion.
6. Redundant-presentation controls show that the apparent higher-order structure is presentation artifact across the useful cases.
7. LOADOUT must acquire ALEX research semantics to gate the probe.
8. 3rdi must acquire global truth semantics to preserve residual exposure.
9. Dogram must acquire semantic evidence authority to calculate residuals.
10. The receipt grows without demonstrated false-collapse prevention.

A killed design is a successful research result if the failure is attributable.

---

## 20. Durable compression

The overnight material reduces to four statements:

```text
RELATIONS CAN HAVE RELATIONS.
FAILURES HAVE SHAPE.
THE SHAPE OF FAILURE CAN SELECT A BETTER QUESTION.
A BETTER QUESTION STILL NEEDS AN ORDINARY GATE BEFORE IT CAN TOUCH THE WORLD.
```

And the promotion membrane is:

```text
DERIVE
  !=
REIFY
  !=
PROMOTE
```

with one hostile warning:

```text
A RELATION CAN BE REAL IN A PRESENTATION
WITHOUT BEING A NEW DIMENSION OF THE TARGET.
```

---

## Seal

> **MADDCL0WN SHOULD NOT JUST GENERATE STRANGE HYPOTHESES.**  
> **IT SHOULD MAKE EACH STRANGE HYPOTHESIS PAY FOR THE NEXT QUESTION.**

And when the question itself asks for consequence:

> **PROPOSE THE QUESTION. KEEP THE RECEIPT. LET THE OWNING WORLD DECIDE WHETHER IT GETS ASKED.**
