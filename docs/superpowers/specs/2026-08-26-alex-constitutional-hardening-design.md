# ALEX — Constitutional Hardening v0

**Date:** 2026-08-26

**Status:** approved architectural amendment; design-only, no production runtime claimed

**Applies to:** Alexandria Floor, ALEX DESK, `@alex`, formation trace, research receipts, and later runtime work.

## Design sentence

> **ALEX must preserve not only provenance, but the limits of what an observation, inheritance, dependency, or replay can legitimately establish.**

These changes do not add research cleverness. They harden five false-inference boundaries already implicit in the floor:

```text
what could search see?
  -> what did the inquiry inherit?
    -> which apparent witnesses share ancestry?
      -> what is actually load-bearing?
        -> can the machine refuse the fake conclusion?
```

Priority order:

```text
CRUCIBLE
  -> SEARCH COVERAGE
    -> INHERITED PREMISES / CAUSAL DEBT
      -> REMOVE-ONE REPLAY
        -> DEPENDENCY FAMILIES
```

The order is architectural, not epistemic rank. Each later piece may be represented in the constitution before its runtime behavior exists.

---

## Constitutional additions

Add these lines to the live ALEX distinctions:

```text
SEARCH MISS != ABSENCE
ABSENCE CLAIM REQUIRES DECLARED COVERAGE

RECEIVED PREMISE != ADMITTED PREMISE
HISTORICAL INHERITANCE != EVIDENTIARY AUTHORITY

APPARENT MULTIPLICITY != INDEPENDENT ANCESTRY
AGREEMENT != INDEPENDENT CORROBORATION

REPLAY SUCCESS != DEPENDENCY ROBUSTNESS
SUPPORT COUNT != LOAD-BEARING DIVERSITY
```

No one of these declares a claim false. They prevent a bounded observation from silently becoming a stronger claim than the observation can bear.

---

# 1. ALEX CRUCIBLE — executable constitutional specimens

ALEX already contains many refusal laws in prose. They should become machine-readable fixtures before a production research runtime is allowed to claim constitutional compliance.

The Crucible is **not** the ALEX runtime and does not choose the production language. It is a portable contract that any implementation can be tested against.

## Fixture contract

Each specimen should preserve at minimum:

```text
crucible_specimen
  id
  title
  constitutional_laws[]
  given
  attempt
  expected
    disposition
    refusal_code?
    required_receipt_survivors[]
    forbidden_promotions[]
  notes?
  version
```

Suggested dispositions:

```text
ACCEPT
REFUSE
UNRESOLVED
INSUFFICIENT_TO_TEST
```

A refusal must be attributable. The machine may not merely return `false`; the fixture should require a stable refusal code and specify what evidence, residue, or uncertainty must survive in the receipt.

## Initial specimen families

```text
broken-ancestry
coordinate-drift
search-absence
shared-lineage-corroboration
favored-hypothesis
serendipity-promotion
replay-impersonation
ghost-promotion
yarn-promotion
constitution-smuggling
inherited-premise-smuggling
remove-one-collapse
```

The fixture format should be boring JSON with a published JSON Schema. A tiny reference harness may validate fixtures and compare implementation results, but it must remain separable from the eventual ALEX runtime.

### Crucible law

> **The floor comes with its own gravity test.**

A production implementation that cannot run or translate the Crucible contract has not yet demonstrated conformance to the floor.

---

# 2. SEARCH COVERAGE — observation of what search could actually see

ALEX already refuses source-level absence from an index miss. That refusal needs a first-class witness describing the search aperture.

## Record

```text
search_observation
  id
  corpus_id
  corpus_version?
  query
  query_type
  index_id
  index_version
  fields_searched[]
  record_types_searched[]
  page_or_reading_scope[]
  pagination_complete
  unreadable_or_missing_ranges[]
  exclusions[]
  truncation
  filters[]
  result_ids[]
  result_count
  observed_at
  producer
  coverage_status
```

Suggested `coverage_status` values:

```text
DECLARED_COMPLETE_FOR_SCOPE
PARTIAL
TRUNCATED
UNKNOWN
NOT_APPLICABLE
```

`DECLARED_COMPLETE_FOR_SCOPE` never means historically complete. It means the named query ran over the declared searchable scope without a known coverage hole.

## Absence claim rule

A source-level or corpus-level absence assertion must identify the exact `search_observation` records that make the negative inference possible.

Examples:

```text
NO MATCH IN INDEX X UNDER COVERAGE C
```

may be established.

```text
THIS NEVER OCCURS IN THE SOURCE TRADITION
```

requires a materially broader argument and cannot be earned by a single index miss.

Hard rule:

> **A search miss is an observation about a declared search aperture. It is not an observation of the universe outside that aperture.**

---

# 3. INHERITED PREMISES / CAUSAL DEBT

Research often begins downstream from assumptions that were not established in the present inquiry. ALEX should preserve them without treating inheritance as authority.

## Record

```text
inherited_premise
  id
  formulation
  arrived_from
  source_record_ids[]?
  entered_as
  evidence_path_ids[]?
  examined
  authority_claimed
  authority_admitted
  consequences_if_false[]
  status
  created_at
  producer
```

Suggested `entered_as` values:

```text
catalog_identity
editorial_date
translation_choice
quotation_attribution
secondary_claim
prior_summary
bibliographic_inheritance
question_presupposition
human_instruction
model_output
other
```

Suggested `status` values:

```text
UNEXAMINED
EXAMINED_SUPPORTED
EXAMINED_CONTRADICTED
EXAMINED_UNRESOLVED
REPLACED
REFUSED
```

`authority_claimed` records what authority arrived attached to the premise. `authority_admitted` records what the current inquiry or owning human actually accepts for the present purpose.

The default is no silent admission.

## PEEL integration

PEEL should be able to answer:

> **Which parts of this conclusion did this inquiry establish, and which parts did it merely inherit?**

An inherited premise may remain useful. The point is not to distrust all inheritance; it is to expose what would otherwise remain invisible causal debt.

---

# 4. REMOVE-ONE .LEEP — structural dependency replay

Ordinary `.LEEP` asks what a receipt can reconstruct. Counterfactual `.LEEP` asks what remains reconstructible after one declared dependency is removed or replaced.

This is a bounded structural test, not probabilistic confidence scoring.

## Procedure

1. Replay normally under the declared receipt.
2. Select exactly one eligible dependency.
3. Remove it or replace it with a declared alternate.
4. Replay again without rewriting the original receipt.
5. Preserve the delta and classify the structural consequence.

Eligible dependency classes may include:

```text
source
reading
translation
assumed_identity
model
bridge
inherited_premise
support_path
```

## Result classes

```text
SURVIVES_REMOVAL
DEGRADES
CHANGES_VERDICT
COLLAPSES
INSUFFICIENT_TO_TEST
```

A remove-one result should preserve:

```text
counterfactual_replay
  base_replay_receipt_id
  removed_dependency_id
  removed_dependency_type
  replacement_id?
  base_result
  counterfactual_result
  consequence_class
  lost_outputs[]
  surviving_outputs[]
  changed_assertions[]
  residual_fog[]
  created_at
  producer
```

Hard rule:

> **Twelve supports may still be one plank. Count does not establish structural diversity.**

This operation does not retroactively erase the removed dependency from history. It creates a new attributed counterfactual test.

---

# 5. DEPENDENCY FAMILIES — ancestry-aware multiplicity

Historical research regularly presents many apparent witnesses that descend from one underlying source, edition, bibliography, OCR, model, or retrieval lineage.

ALEX should preserve that dependence explicitly enough to prevent fake corroboration.

## Record / projection

```text
dependency_family
  id
  member_record_ids[]
  shared_ancestor_ids[]
  dependency_basis[]
  independence_status
  scope
  evidence_record_ids[]
  created_at
  producer
```

Suggested `dependency_basis` values:

```text
same_carrier
same_edition
quotation_chain
shared_scan
shared_ocr
shared_model_family
shared_training_or_retrieval_lineage
shared_bibliography
shared_translation
other_declared
```

Suggested `independence_status` values:

```text
DEPENDENT
PARTIALLY_DEPENDENT
INDEPENDENT_WITHIN_DECLARED_SCOPE
UNKNOWN
```

A dependency family is not an ontology-wide permanent grouping. It is an attributable finding for a declared research scope.

## Desk lens

ALEX DESK should eventually support a dependency-family lens that can visually compress or bracket apparent multiplicity while leaving every witness individually addressable.

Example:

```text
6 apparent witnesses
  -> dependency lens
1 shared family + 1 independent witness
```

The lens must never delete members or claim independence where ancestry is unknown.

---

# Interaction between the five hardening moves

These mechanisms should compose without collapse.

Example:

```text
search_observation S says query Q had partial coverage

result R1, R2, R3 appear to support assertion A

PEEL exposes inherited premise P:
  "R1 and R2 are independent editions"

Dependency analysis shows:
  R1 -> Edition E
  R2 -> quotes R1
  R3 -> different carrier but same old editorial emendation

remove-one replay deletes E

A changes verdict
```

The correct result is not automatically “A is false.” The correct result is that the original support structure was less independent and more load-bearing than its visible multiplicity implied.

The Crucible should be able to force a conforming implementation to preserve that distinction.

---

# ALEX DESK consequence

The Desk gains three useful projections without becoming more authoritative:

1. **coverage lens** — shows which negative search observations had what aperture;
2. **causal-debt lens** — exposes inherited premises beneath a claim;
3. **dependency-family lens** — compresses fake multiplicity while preserving member identities.

Remove-one replay can be invoked from a desk arrangement, but the visual action only selects the dependency to test. The replay engine and evidence receipts determine the result.

Hard Desk additions:

```text
collapsed family != merged identity
hidden dependency != independence
many cards != many witnesses
remove-one visualization != causal proof
```

---

# Receipt consequence

Durable research receipts should be able to include, when material:

```text
search_coverage[]
inherited_premises[]
dependency_families[]
counterfactual_replays[]
crucible_results[]
```

A compact answer need not dump all fields, but any load-bearing absence claim, inherited premise, independence claim, or remove-one conclusion must retain a resolvable path to its supporting record.

---

# Failure conditions

Redesign if ALEX:

- turns `0 results` into source absence without a coverage witness;
- treats a catalog, editor, prior answer, or question presupposition as admitted authority merely because it arrived upstream;
- counts descendants as independent corroboration without ancestry analysis;
- uses remove-one replay as a numeric confidence score;
- deletes the original receipt when running a counterfactual replay;
- collapses a dependency family into a single witness identity;
- makes Crucible fixtures dependent on one production language or UI;
- allows an implementation to “pass” a refusal specimen while discarding the evidence or residue the refusal was required to preserve.

---

# Implementation order

## Gate A — Crucible contract

Create machine-readable specimen schema, initial fixtures, stable refusal codes, and a language-neutral result contract. A reference harness may exist only to validate the contract and compare submitted results.

## Gate B — Search coverage

Add `search_observation` to the first exact-search proof. Make the existing Search Absence test consume a real coverage record.

## Gate C — Inherited premise ledger

Add optional premise records and require at least one specimen where an upstream identity or attribution is received but not admitted.

## Gate D — Remove-one replay

Extend `.LEEP` with one-dependency counterfactual replay and receipt-preserving result classes.

## Gate E — Dependency families

Represent shared ancestry strongly enough that corroboration logic and the Desk can distinguish apparent count from independence.

Each gate should be testable and reviewable on its own. Later gates do not need to block the one-book floor unless their failure is required to make a claim that the specimen actually exercises.

---

## Crucible runtime gate

**CRUCIBLE RUNTIME CONFORMANCE IS NOT YET CLAIMED**

Before the one-book runtime claims constitutional conformance, a real runtime
adapter must execute the applicable Crucible specimens. Contract self-tests and
fake adapters are insufficient.

---

## Seal

> **Search only testifies to what it could see.**
>
> **Inheritance only testifies to what arrived.**
>
> **Multiplicity only testifies to count until ancestry is known.**
>
> **Replay only testifies to what survives the declared test.**
>
> **The Crucible makes the machine prove it knows the difference.**
