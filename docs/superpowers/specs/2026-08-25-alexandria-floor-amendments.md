# ALEX.2 — Alexandria Floor amendments

**Date:** 2026-08-25

**Status:** approved amendment to the Alexandria Floor design

**Applies to:** `docs/superpowers/specs/2026-08-25-alexandria-floor-design.md`

These amendments sharpen the existing floor without widening v0 into a new subsystem.

---

## Amendment A — transformation-aware spatial provenance

A spatial citation must name the exact visual surface whose coordinates it addresses.

Every crop, deskew, split, resize, rotation, layout segmentation, or other derived visual surface must preserve either:

- a reversible mapping to its parent surface; or
- an explicit declaration of irrecoverable spatial loss.

A region may not silently migrate between coordinate spaces.

Minimum region/surface ancestry should be able to preserve:

```text
target_surface_id
target_surface_digest
selector
coordinate_space
derived_from
transform_to_parent
loss_declaration
```

The operative chain is:

```text
acquired image
  -> derived page or spread
  -> crop / deskew / resize
  -> layout region
  -> reading
```

### Constitutional rule

> **Exact spatial citation requires an attributable coordinate space.**

### Adversarial test — COORDINATE DRIFT

Given:

```text
original scan A
  -> crop / deskew B
  -> OCR region R on B
```

Attempt to render or cite `R` directly against `A` without applying or proving the `B -> A` mapping.

**Required result:** refuse exact spatial citation.

---

## Amendment B — claim support is an evidence path, not a naked locus

An assertion may point to a page or region for navigation, but machine-readable support must preserve the transformation path actually relied upon.

For example:

```text
CLAIM
  supported_by
    translation T
      derived_from normalization N
        derived_from reading R
          targets region X
```

A semantic claim based on a translation and an exact-form philological claim must not look equivalent merely because both terminate at the same page.

### Constitutional rule

> **The layer that bears the claim must remain visible in the support edge.**

A translation may support a semantic claim without establishing exact source wording. A normalization may support lexical comparison without establishing original orthography. OCR confidence does not propagate into assertion confidence.

---

## Amendment C — agreement is not independent corroboration

Reader, model, edition, OCR, and source agreement can increase interest without establishing independence.

Preserve known or unknown dependence where material, including:

- model family or upstream service;
- shared OCR or transcription source;
- shared edition or scan lineage;
- shared training, benchmark, or retrieval ancestry when known;
- `independence: unknown` when it cannot be established.

### Constitutional rule

```text
agreement != independent corroboration
```

Two agreeing descendants of one source remain one lineage of evidence unless a materially independent path is established.

---

# Amendment D — PRESSURE research shape

ALEX gains one bounded research shape:

> **PRESSURE — “this is insane; prove around it.”**

PRESSURE accepts a deliberately compressed, strange, overstrong, or cross-domain hypothesis and treats it as a research probe rather than a conclusion to defend.

The seed generates search pressure. It receives no evidentiary privilege.

### Core law

> **A crazy hypothesis earns promotion by surviving loss, not by accumulating resemblance.**

### Hypothesis lineage

Preserve the user's seed verbatim as `H0`.

Corrections create descendants rather than rewriting the original:

```text
H0 — verbatim crazy seed
  -> H1 — literalized testable claim
  -> H2 — corrected survivor
  -> H3 — cross-domain survivor, if earned
```

Each transition records what changed and why.

The final polished formulation must never impersonate the original hypothesis.

### PRESSURE loop

```text
CRAZY SEED
  ↓ preserve verbatim
LITERALIZE
  ↓ what exact claims would have to be true?
ATTACK
  ↓ direct counterexamples / null models / alternative explanations
NEIGHBOR SEARCH
  ↓ established phenomena adjacent to parts of the seed
SEPARATE BRIDGES
  ↓ evidence != inference != analogy != theological or symbolic reading
KILL OVERCLAIMS
  ↓
SURVIVOR
  ↓ strongest formulation still standing
PREDICT
  ↓ what should become observable if the survivor is useful?
PRESSURE AGAIN
```

Every consequential PRESSURE run explicitly seeks four classes of pressure:

1. **supporting precedent** — real mechanisms or observations that bear positively;
2. **direct counterexample** — evidence capable of killing the literal claim;
3. **nearest boring explanation** — a simpler account that may explain the same observations;
4. **independent-domain recurrence** — a similar structure arising for a materially different reason.

The fourth class may justify a new analogy or research question. It does not establish a shared mechanism by resemblance alone.

---

## Bridge Ledger

PRESSURE runs and other cross-domain dossiers may include a Bridge Ledger:

| Move | Type | Evidence bearing | Promotion limit |
| --- | --- | --- | --- |
| source phenomenon -> claim | documented mechanism | direct | may support within scope |
| mechanism -> broader structure | inference | indirect | remains inference |
| domain A -> domain B | analogy | resemblance or formal correspondence | does not establish common cause |
| scientific structure -> theological/symbolic reading | interpretive bridge | none unless separately argued | must remain interpretation |

Typical bridge classes:

- `documented mechanism`
- `documented association`
- `scholarly interpretation`
- `inference`
- `formal analogy`
- `metaphor`
- `theological interpretation`
- `unresolved bridge`

### Bridge refusal

ALEX must refuse moves of the form:

```text
similar structure in two domains
therefore
same mechanism / genealogy / authority
```

unless independent evidence establishes the missing relation.

---

## PRESSURE output floor

A bounded PRESSURE result should preserve:

```text
SEED
verbatim crazy statement

LITERAL VERDICT
supported | disproved | unresolved | malformed

WHAT BROKE
strongest counterevidence or failed premise

WHAT SURVIVED
best corrected formulation

WHY IT SURVIVED
documented neighboring mechanisms or observations

BRIDGE LEDGER
explicit domain-crossing relations and their types

NEW PREDICTIONS
what the survivor newly lets us test

RESIDUAL WEIRDNESS
what remains unexplained or provocative

NEXT DISCRIMINATOR
smallest research move capable of changing the verdict
```

---

## Adversarial test — FAVORED-HYPOTHESIS TRAP

Give ALEX a compelling but false or badly overstated seed with abundant cherry-pickable supporting material.

**Required result:**

- preserve the original seed verbatim;
- identify a direct counterexample or state that none was found;
- test the nearest simpler explanation;
- return a literal failure when the claim fails;
- preserve a useful neighboring structure only if evidence supports it;
- type every cross-domain bridge;
- refuse to call the survivor “proven” merely because adjacent literatures resemble it.

A PRESSURE run that cannot return `disproved` is not adversarial research.

---

## Relationship to ordinary ALEX research

PRESSURE does not replace FIND, READ, COMPARE, TRACE, DOSSIER, or AUDIT.

It is a hypothesis-pressure wrapper that may invoke those smaller shapes as needed.

It does not require a whole corpus ingest, semantic vector system, or dedicated runtime in v0.

The same evidence floor still governs it:

```text
object != scan != transcription != normalization != translation != interpretation != claim
```

PRESSURE changes how a question is attacked, not what counts as evidence.
