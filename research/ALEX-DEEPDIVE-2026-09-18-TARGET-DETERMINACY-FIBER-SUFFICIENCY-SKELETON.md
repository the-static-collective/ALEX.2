# TARGET-DETERMINACY / FIBER-SUFFICIENCY — Anatomy of the ALEX Research Skeleton

**Status:** RESEARCH SYNTHESIS / CROSS-INDEX  
**Authority:** none  
**Promotion:** none  
**Date:** 2026-09-18 America/Chicago

## Executive finding

A large family of ALEX research frontiers appears to share one mathematical skeleton:

> **A reduced representation may answer only the questions that remain invariant over what that representation forgot.**

This packet does **not** propose a new master schema, ontology, confidence score, or runtime. It cross-indexes existing ALEX work and identifies a reusable research test already implicit in the project.

The central relation is:

```text
full constituted state
        |
        | quotient / projection
        v
reduced representation
        |
        | target question / operation
        v
answer
```

Let a lawful quotient/projection be

```text
pi : X -> Y
```

and let a target question or deterministic operation be

```text
q : X -> Z.
```

The reduced state `Y` is sufficient for `q` exactly when there exists a map

```text
g : Y -> Z
```

such that

```text
q = g o pi.
```

Equivalently:

```text
pi(x) = pi(y)
    =>
q(x) = q(y).
```

If two full states collapse to the same projected state but require different target answers, the projection is insufficient **for that target**.

This is target-relative. The same projection may be sufficient for one question and insufficient for another.

## Why this is already ALEX rather than a new invention

The skeleton is distributed across existing ALEX work.

### #66 — FIBER-BEFORE-NEEDLE-001

ALEX already preserves the preimage/fiber before selecting a representative:

```text
f^-1(y) = {x in X | f(x)=y}
```

and already states the operational correction:

```text
IMAGE FIRST
FIBER SECOND
REPRESENTATIVE ONLY WITH A DECLARED RULE
```

### #116 — QUESTION-REACHABILITY-NOT-OPERATION-REACHABILITY-001

ALEX already states the exact factorization criterion for operation survival under collapse:

```text
f : R -> O
q : R -> C

f survives q
iff
there exists g : C -> O
such that

f = g o q
```

This is the same target-determinacy test.

### PR #18 / PR #21 — PROJECTION-INVARIANCE / PROJECTION-BREAK

The merged executable projection work already proves a neighboring law:

- materially distinct worlds may remain observer-equivalent under a bounded projection;
- one shared attributable intervention can expose a future divergence;
- that divergence does not by itself prove sufficiency, dominance, historical reality, global causality, or authority.

So the current packet should be read as a **research anatomy of existing mechanisms**, not a new constitutional layer.

## CHRONOBODY is already an ALEX organ

CHRONOBODY-001 is implemented and merged through ALEX PR #45.

Its executable role includes:

- exact-SHA body identity;
- explicit `PRESENT / INCUBATING / HELD / RETIRED / RECONSTITUTED` status;
- explicit `PRESENT_ONLY / EXPERIMENTAL / REPLAY` mode;
- deterministic routing with ambiguity refusal;
- exact materialization verification;
- historical body execution without silently mutating the body;
- execution receipts preserving body-time / source SHA / status;
- `authority: none`;
- no latest-wins rule.

That makes CHRONOBODY the concrete **reasoning-body-time coordinate** in the older #47 `THREE-CLOCK-ERASURE-001` research model:

```text
R(claim | W, O, B, C)

W = world / occurrence cut
O = observer epistemic cut / projection
B = reasoning body-time
C = LOADOUT compile identity when material
```

CHRONOBODY supplies a real executable witness for `B`.

It does **not** by itself supply `W`, `O`, or `C`, and it does not decide which coordinates a given target question needs.

That is exactly where target-determinacy / erasure pressure becomes useful.

## The research skeleton

A compact current anatomy is:

```text
                         RESEARCH CONSTITUTION
                                #64
                                 |
                                 v
                       declared world / question
                                 |
              +------------------+------------------+
              |                                     |
              v                                     v
        FREEDOM / QUOTIENT                    OBSERVER CUT
          #88 #94                            #10 #47 #69
              |                                     |
              +------------------+------------------+
                                 v
                            PROJECTION pi
                         PR #18/#21, #66
                                 |
                                 v
                              FIBER
                       compatible full states
                                 |
              +------------------+------------------+
              |                  |                  |
              v                  v                  v
          HISTORY            STRUCTURE           SEMANTICS
        #93 #106 #117      #125 #128            #127 #132
              |                  |                  |
              +------------------+------------------+
                                 v
                         TARGET / OPERATION q
                              #116
                                 |
                         does q factor?
                           /          \
                        YES            NO
                         |              |
                    ANSWERABLE         FOG
                                        |
                                        v
                               ACTIVE DISCRIMINATION
                              #39 #40 #50 #110
                                        |
                                        v
                              attributable new cut
                                        |
                                        v
                              refine compatible set
                                     #69
                                        |
                                        v
                                   try again
```

Causality (#123 / #134) sits beside this as the harder case where the compatible family includes counterfactual/intervention worlds rather than merely hidden present states.

## Existing bones and what they protect

| ALEX surface | Coordinate / distinction protected | Collapse it prevents |
|---|---|---|
| #47 THREE-CLOCK-ERASURE | world cut / observer cut / body time / compile | changed world, aperture, reasoning body, or compile impersonating one another |
| #66 FIBER-BEFORE-NEEDLE | compatible preimage | arbitrary representative impersonating unique recovery |
| #69 FOG-TOMOGRAPHY | intersection of observer fibers | one local view impersonating world identity |
| #70 APERTURE-ANCESTRY | constraint ancestry | witness count impersonating independent information |
| #72 APERTURE-TRANSVERSALITY | provenance independence vs discriminatory novelty | independent road impersonating independent cut |
| #88 DECLARED-FREEDOM-QUOTIENT | licensed representational freedom | harmless representation delta impersonating structural delta |
| #91 DECODER-DOMAIN | calculational domain | changed decoder world impersonating changed source |
| #94 JOINT-QUOTIENT | shared/joint orbit structure | identical marginals impersonating identical whole |
| #106 HISTORY-NOT-DELTA | payload vs ancestry | identical bytes impersonating identical formation |
| #110 SEPARATOR-NOT-MINIMAL | sufficiency vs necessity/minimality/cost | first successful probe impersonating required probe |
| #113 CRITERION-NOT-POLICY | performance surface vs decision criterion | fixed consequences impersonating a unique policy ranking |
| #116 QUESTION/OPERATION-REACHABILITY | target factorization | lost distinction impersonating lost capability, or vice versa |
| #117 RETROSPECTIVE-VIEW | effective/available/application chronology | later view impersonating earlier information |
| #125 LOCAL-LOADS-NOT-GLOBAL-WIRING | joint incidence / coalition structure | matching marginals impersonating matching wiring |
| #127 SENSE-FIELD-PROVENANCE | semantic role vs evidence posture | generated/repeated reading impersonating source fact |
| #128 TYPED-SPECTRUM | declared role/type orientation | untyped structural equality impersonating typed provenance equality |
| #130 SURFACE-DECLARATION-NOT-OCCURRENCE | declaration validity/publication relation | later declaration impersonating contemporaneous declaration |
| #132 GRAMMAR-PROVENANCE-CHAIN | grammar/as-of cut | current rereading impersonating historical reading |
| #134 CHANGE-POINT-NOT-CAUSAL-HINGE | counterfactual causal design | temporal adjacency impersonating causation |

## Three orders that must not collapse

The current research surface strongly suggests at least three independent orderings.

### 1. Information refinement

Does one observation distinguish everything another distinguishes for the declared state family?

This is about partitions/fibers.

### 2. Provenance independence

Did apparently multiple constraints arise through materially independent roads?

This is #70 / #72 territory.

```text
INDEPENDENT ROAD
!=
INDEPENDENT CUT
```

### 3. Operational / decision value

Does the retained distinction actually matter for a declared question, operation, policy, or cost criterion?

This is #110 / #113 / #116 territory.

Therefore:

```text
INFORMATION REFINEMENT
!=
PROVENANCE INDEPENDENCE
!=
DECISION VALUE
```

A single scalar "confidence" would erase exactly these differences.

## Constructive side: information loss is not the end of the story

#69 gives the constructive inverse.

For observer maps

```text
P_A : W -> Y_A
P_B : W -> Y_B
```

and observations `y_A, y_B`:

```text
F_A = P_A^-1(y_A)
F_B = P_B^-1(y_B)

F_joint = F_A intersect F_B
```

So the native research loop is not:

```text
projection -> loss -> stop
```

but:

```text
projection
-> retain fiber
-> acquire attributable new cuts
-> intersect/refine
-> ask target again
```

The stopping condition need not be "one hidden world remains."

A stronger and cheaper stop condition is:

> **all surviving worlds now answer the declared target identically.**

That is target determinacy without unnecessary total reconstruction.

## Active discrimination

#39 / #40 / #50 become clearer under the same anatomy.

Given surviving candidate family `F` and candidate lawful probes `p_i`, each probe predicts a partition/refinement of `F`.

The best research probe is not universally "the probe that reveals the most."

For a declared target `q`, the useful question is:

> Which bounded lawful probe refines the current fiber enough that `q` becomes invariant on the surviving cells?

This preserves:

```text
DISCRIMINATING
!=
SAFE
!=
PERMITTED
!=
CHEAPEST
!=
MINIMAL
!=
TRUE
!=
CAUSAL
```

Dogram may calculate partitions/deltas.
ALEX may pressure sufficiency, chronology, provenance, and overclaim.
LOADOUT owns capability/effect fencing.
3rdi owns observer-local availability/projection.
The owning human/world retains admission and meaning authority.

## Structural specimens already demonstrating the skeleton

### Typed incidence — #128 / Dogram #138

Two connected bipartite carriers can share:

- row/column degree multisets;
- exact adjacency characteristic polynomial;
- untyped graph isomorphism;

while failing type-preserving isomorphism.

The lost coordinate is the declared side role.

Therefore:

```text
UNTYPED ISOMORPHISM
!=
TYPED PROVENANCE EQUIVALENCE
```

### Marginals vs wiring — #125

Equal endpoint loads and aggregate incidence do not determine global relational wiring.

### Joint quotient — #94

Equal marginal quotient classes do not determine the joint orbit when one shared transformation acts on the family.

### Higher-order dependence — #83

Every pair may appear free while a larger family is jointly constrained.

Together:

```text
ALL LOW-ORDER / MARGINAL SUMMARIES
!=
JOINT STRUCTURE
```

unless a declared theorem/constitution earns that lift.

## Temporal specimens

#117, #130, and #132 can be treated as target-determinacy failures under erased chronology.

Useful axes include:

```text
subject / effective occurrence
declaration / recording occurrence
observer availability cut
grammar / decoder body-time
analysis / application occurrence
```

A later view can lawfully descend from an earlier carrier without becoming what the earlier observer possessed.

CHRONOBODY makes this especially concrete for executable reasoning:

```text
EXECUTION NOW
!=
BODY TIME NOW
```

Historical replay is a present execution of an explicitly historical body.

It is not retroactive promotion of that body into the present.

## Semantic provenance specimen — #127

A text-only projection may collapse:

```text
source quotation
generated proposal
candidate reading
user correction
model repetition
external witness
```

into the same semantic string.

That projection may answer:

```text
"What text is present?"
```

while failing:

```text
"Is this source-attested?"
"Was this the user's intended meaning?"
"How many independent attributable roots support it?"
```

Therefore:

```text
SEMANTIC EQUALITY
!=
EVIDENCE EQUALITY
```

and:

```text
REPETITION
!=
ANCESTRY
```

## Causal layer — #123 / #134

Causality is connected to the same skeleton but is stronger.

The observed chronology

```text
Gamma_pre -- encounter E -- Gamma_post
```

may be compatible with several causal worlds:

```text
A: E causes DeltaGamma
B: DeltaGamma occurs without E
C: competing K causes DeltaGamma while E also occurs
```

The observation map can collapse these worlds to the same realized history.

Therefore the causal target does not factor through bare before/after observation.

A causal design, comparison, intervention sibling, or other defensible counterfactual constitution must supply additional structure.

```text
AFTER
!=
BECAUSE OF
```

#123's controlled sibling-history idea is therefore a natural research bridge into #134 without turning ALEX into a universal causal-inference engine.

## External formal neighbors

These are methodological neighbors, not imported authority.

### Database view/query determinacy

Database theory asks whether a reduced view determines a query: if two underlying databases have the same view, must they have the same query answer?

This is the same fiber criterion.

### Statistical sufficiency / experiment comparison

Statistical sufficiency asks when a reduced statistic preserves all information required for a declared inferential target.

Blackwell-style experiment comparison distinguishes "at least as informative for every decision problem" from target-specific or incomparable information orders.

Useful anchor:

- Goel & Ginebra (2003), *When is one experiment 'always better than' another?*, DOI `10.1046/j.1467-9884.2003.00376.x`.

### Abstract interpretation / strong preservation

Abstract interpretation intentionally collapses concrete states and studies which properties/operators remain soundly or strongly preserved. Refinement restores distinctions needed by the specification language.

ALEX should not inherit abstract-interpretation semantics wholesale, but the structural neighbor is close:

```text
coarse abstraction
+
declared property family
->
preserved or refine
```

### Provenance

Database and information-science provenance work reinforces the distinction between output/content identity and derivation/formation identity.

Useful neighbor:

- Green, Karvounarakis & Tannen, *Provenance Semirings*.
- W3C PROV conceptual model / provenance rationale.

## Candidate bounded research experiment

Do **not** build a generic target-determinacy runtime first.

A smallest useful executable specimen would be `TARGET-DETERMINACY-ERASURE-001`.

Freeze a finite full state family and several projections.

For each pair `(pi, q)`:

1. enumerate fibers of `pi`;
2. test whether `q` is constant on every fiber;
3. if yes, emit `DETERMINES_FOR_TARGET`;
4. if no, emit one explicit witness pair `x,y` such that:
   `pi(x)=pi(y)` but `q(x)!=q(y)`;
5. optionally add one declared probe `p` and test whether `(pi,p)` now determines `q`;
6. preserve `authority:none`;
7. make no claim that `q` is important, true, causal, or worth executing.

Five synthetic hostile cases should be enough:

```text
A. same semantic text / different evidence posture
B. same untyped graph / reversed typed role
C. same surface+subject / different declaration chronology
D. same carrier / historical grammar vs later grammar
E. same pre/post history / different causal worlds
```

Case E should remain structurally distinct: a finite causal-model fixture can demonstrate non-identifiability, but no general causal runtime is implied.

## Why not promote a new schema yet

Existing ALEX already owns almost every required ingredient:

- fiber preservation;
- quotient/freedom declaration;
- observer-local cuts;
- body-time via CHRONOBODY;
- projection invariance/break;
- active discrimination;
- operation factorization;
- chronology/provenance boundaries;
- authority refusal.

A new primitive earns promotion only if an executable hostile specimen cannot be expressed compositionally from these pieces.

Until then:

> **COMPOSE THE BONES; DO NOT GROW A SECOND SKELETON.**

## Research questions left open

1. Is target factorization already fully expressible through existing ALEX receipt grammar, or only as a research-side calculation?
2. Which coordinates from `W,O,B,C,...` repeatedly pay rent across unrelated consumers?
3. Can a generic erasure-pressure harness remain purely finite/deterministic and avoid importing domain semantics?
4. How should stochastic targets be represented without collapsing deterministic factorization into probabilistic sufficiency?
5. When does target determinacy require joint structure rather than pairwise separation?
6. Can Dogram own the finite factorization math while ALEX owns only the claim/provenance boundary?
7. Can #39 active discrimination select target-separating probes without silently becoming a decision-policy engine?
8. Where exactly should causal counterfactual constitution remain separate from ordinary hidden-state refinement?
9. Does CHRONOBODY + 3rdi + LOADOUT + occurrence identity already supply enough coordinate provenance for #47 without any new generic temporal object?
10. Which existing holds can now be closed or narrowed as descendants once this cross-index is accepted?

## Seals

```text
A PROJECTION MAY ANSWER ONLY THE QUESTIONS
THAT ARE INVARIANT OVER WHAT IT FORGOT.

SAME IMAGE != SAME PREIMAGE.

SAME ANSWER FOR THIS TARGET
!=
SAME WORLD.

LOST DISTINCTION != LOST CAPABILITY.

PRESERVED DISTINCTION != SUFFICIENT OPERATIONAL STATE.

INDEPENDENT ROAD != INDEPENDENT CUT.

INFORMATION ORDER != PROVENANCE ORDER != DECISION ORDER.

CURRENT REREADING != HISTORICAL READING.

EXECUTION NOW != BODY TIME NOW.

AFTER != BECAUSE OF.

COMPOSE THE BONES; DO NOT GROW A SECOND SKELETON.
```

## Promotion boundary

**None.**

This packet is a cross-index and research compression only.

No new runtime, schema, ontology, truth/evidence score, authority path, causal engine, policy selector, temporal database, or shared project ownership is introduced.
