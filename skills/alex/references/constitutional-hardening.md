# Constitutional hardening

Read this reference when a research result depends on search absence, inherited assumptions, apparent source multiplicity, structural dependency, or constitutional refusal behavior.

## Live distinctions

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

These laws constrain inference. They do not automatically make the underlying claim false.

## Search coverage

Preserve a `search_observation` whenever a negative search result becomes load-bearing.

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

Use one of:

```text
DECLARED_COMPLETE_FOR_SCOPE
PARTIAL
TRUNCATED
UNKNOWN
NOT_APPLICABLE
```

A search miss supports only a statement about the declared search aperture unless broader evidence exists.

## Inherited premises / causal debt

Use an `inherited_premise` when a conclusion or inquiry starts with an assumption supplied by a catalog, editor, prior summary, model, secondary source, bibliography, question presupposition, or other upstream carrier.

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

Suggested statuses:

```text
UNEXAMINED
EXAMINED_SUPPORTED
EXAMINED_CONTRADICTED
EXAMINED_UNRESOLVED
REPLACED
REFUSED
```

Do not silently copy `authority_claimed` into `authority_admitted`.

When material, PEEL should answer:

> Which parts of this conclusion did this inquiry establish, and which did it merely inherit?

## Dependency families

Use a `dependency_family` when several apparent witnesses share materially relevant ancestry.

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

Suggested dependency bases include:

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

Suggested independence statuses:

```text
DEPENDENT
PARTIALLY_DEPENDENT
INDEPENDENT_WITHIN_DECLARED_SCOPE
UNKNOWN
```

A family does not merge record identity. It records a dependency finding for a declared scope.

## Remove-one `.LEEP`

After ordinary replay succeeds, a bounded counterfactual replay may remove or replace exactly one declared dependency.

Eligible classes include:

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

Return one of:

```text
SURVIVES_REMOVAL
DEGRADES
CHANGES_VERDICT
COLLAPSES
INSUFFICIENT_TO_TEST
```

Preserve:

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

The operation creates a descendant test. It never rewrites the historical receipt.

## ALEX Crucible

The constitutional laws should be expressible as machine-readable specimens independent of the production runtime language.

Minimum fixture contract:

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

A refusal is incomplete if the implementation discards evidence, uncertainty, ancestry, or residue the fixture requires to survive.

Initial families should include at least:

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

## Desk projection

The ALEX Desk may later expose:

- a coverage lens;
- a causal-debt lens;
- a dependency-family lens;
- a remove-one replay selector.

Keep these boundaries live:

```text
collapsed family != merged identity
hidden dependency != independence
many cards != many witnesses
remove-one visualization != causal proof
```

## Receipt additions

When material, durable receipts should preserve resolvable references to:

```text
search_coverage[]
inherited_premises[]
dependency_families[]
counterfactual_replays[]
crucible_results[]
```

## Compact hardening check

Before making a consequential negative, inherited, independence, or robustness claim, ask:

```text
COVERAGE — what could the search actually see?
DEBT — what premise arrived without being established here?
ANCESTRY — how many apparently separate supports share a parent?
LOAD — what changes if one declared dependency is removed?
REFUSAL — would a Crucible specimen force the machine to reject the stronger claim?
```

> **Search only testifies to what it could see. Inheritance only testifies to what arrived. Multiplicity only testifies to count until ancestry is known. Replay only testifies to what survives the declared test.**
