# ALEXDEEPDIVE — CONTENT-ADDRESS-NOT-INDEPENDENCE-001

**Status:** RESEARCH  
**Promotion:** none  
**Created:** 2026-09-20 23:21 America/Chicago  
**Task shape:** AUDIT

## Finding

PR #141 (`RELATION-NURSERY-001`) materially advanced after the previous ALEXDEEPDIVE cut from `f561cf61305e25d14dab9893f048599400768497` to `c25759f5444d44983758f5816b872055f4bec79f`. The new commits add a content-addressed `pressure_digest` and a replay/sibling test.

That is a useful provenance improvement, but the new test name exposes a narrower semantic boundary: `test_pressure_receipt_has_independent_stable_identity` proves deterministic content identity and sibling distinction. It does not prove source/witness independence, independent ancestry, or independent corroboration.

```text
CONTENT-ADDRESSED IDENTITY != INDEPENDENT LINEAGE
STABLE REPLAY DIGEST != INDEPENDENT CORROBORATION
DISTINCT SIBLING DIGEST != INDEPENDENT ANCESTRY
RECEIPT IDENTITY != EVIDENTIARY INDEPENDENCE
```

This does not invalidate the new digest mechanism. The mechanism is correctly useful for immutable/replayable receipt identity. The pressure is on terminology and on any downstream inference that might read `independent stable identity` as evidentiary independence.

## Ground

- Question: what single live ALEX frontier is newly earned by current evidence?
- Desired consequence: distinguish the newly added content-addressed pressure identity from ALEX's separate lineage/independence semantics.
- Stop condition: establish whether the new PR #141 delta closes, changes, or sharpens the prior `INDEPENDENCE-REQUIRES-LINEAGE-001` frontier.
- Authority/effect boundary: research only; no canon/runtime/merge/evidence authority.
- Formation trace active: no.

## Orientation

The Static Collective GitBook Front Room orientation path was attempted first. The available GitBook connector exposed organization-scoped search/site operations but did not expose the organization identifier needed to enter the page in this run. This is access fog, not absence. No GitBook claim is used as evidence below.

## World cut

### Included

- `the-static-collective/ALEX.2` `main`, pre-write head `13b7e3477731b9cffe6483f4aa013016aca003d6`.
- Open PR #141, exact inspected head `c25759f5444d44983758f5816b872055f4bec79f`.
- PR #141 commit sequence and changed files.
- `ALEX.2/AGENTS.md`.
- `skills/alex/SKILL.md`.
- `skills/alex/references/research-receipt.md`.
- Immediately previous durable packet `research/ALEX-DEEPDIVE-2026-09-20-1728-NO-MATERIAL-DELTA-HOLD.md`.

### Deliberately omitted

Adjacent repositories, broad scholarship, web research, and computation were not traversed. The new delta is a local semantics/provenance issue fully discriminable from the ALEX code, tests, and constitutional rules. No external source is needed to establish what the test does and does not prove.

### Sufficiency

Sufficient for this bounded audit. Not sufficient to establish the independence of any real historical/source witness; no such claim is made.

## Evidence path

1. Required ALEX governance was read before consequential claims.
2. Recent `main` history established that the previous packet was the current pre-write main head.
3. Open PRs by update time showed PR #141 updated after the previous cut.
4. PR #141 commit history showed two new commits after the previously inspected `f561cf...` head: `e33f7d6a346a90c68e48241152eebd46b27c1b17` (`test: require content-addressed pressure receipts`) and `c25759f5444d44983758f5816b872055f4bec79f` (`feat: content-address relation pressure receipts`).
5. Exact-head changed-file inspection showed `attach_pressure()` now hashes the pressure body into `pressure_digest`.
6. The new test constructs the same pressure receipt twice and a sibling pressure receipt once; it asserts replay digest equality and sibling digest inequality under the test name `test_pressure_receipt_has_independent_stable_identity`.
7. ALEX constitutional law separately states `agreement != independent corroboration` and requires lineage evidence before independence promotion.

## Discovery trace

- D1: previous frontier concerned `independently_supported` without lineage.
- D2: PR #141 changed after that audit.
- D3: commit names pointed to content-addressed pressure receipts.
- D4: the new test name used `independent stable identity`, prompting a check against ALEX's established independence vocabulary.

D1–D4 explain why the audit occurred. They are not themselves evidence of source independence.

## Observed delta

The pressure receipt body now contains:

- `proposal_ref`
- `experiment_ref`
- `result`
- `observation_ref`
- `interpretation`
- `non_claim`

and returns a deterministic `pressure_digest = sha256(canonical-json(body))`.

The replay test establishes:

- same body -> same digest;
- changed sibling body -> different digest;
- siblings can retain the same proposal reference.

Those are content-address/replay properties.

## Claims

| ID | Claim | Class | Supporting evidence path | Counterevidence | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #141 materially advanced after the previous packet. | observed | PR commit history + exact current head | none observed | supported |
| C2 | The new mechanism content-addresses pressure receipt bodies. | observed | `attach_pressure()` exact-head implementation | hash collision is theoretically possible but irrelevant to the semantic distinction here | supported |
| C3 | The new replay/sibling test establishes deterministic content identity, not lineage independence. | inference from executable assertions | test inputs/assertions + ALEX independence law | test-name `independent` could mean object-level independence rather than evidentiary independence | supported with terminology caveat |
| C4 | The prior `INDEPENDENCE-REQUIRES-LINEAGE-001` frontier remains open. | inference | pressure receipt still permits `interpretation="independently_supported"` with opaque `observation_ref`; new digest adds identity, not ancestry | a later composition layer may intentionally own lineage validation | retained |
| C5 | Renaming the test/field semantics is smaller than adding lineage machinery if object identity was the intended meaning. | proposal | nearest boring explanation + smallest-change rule | downstream code may already distinguish the terms clearly | proposed |

## Contradictions and alternatives

1. **Terminology-only reading:** `independent stable identity` means the pressure receipt has an identity independent of the proposal's identity, not that its evidence is independent. This is the nearest boring explanation and is fully compatible with the assertions.
2. **Evidentiary-independence reading:** the phrase could be read as independent corroboration. The test does not establish that stronger meaning.
3. **Composition-layer reading:** `attach_pressure()` may intentionally accept caller testimony and leave lineage validation to another layer. If so, this audit should not force lineage logic into the constructor.

No evidence found requires treating the digest mechanism itself as defective.

## Direct counterexample

Two pressure receipts can have distinct `pressure_digest` values while both observations descend from the same underlying witness or dependency family. Distinct content is sufficient for distinct content addresses; it is not sufficient for independent ancestry.

Likewise, an exact replay has the same digest, but digest equality says the declared body replayed exactly; it does not establish that the body accurately describes an independent witness.

## Nearest boring explanation

The test author used `independent` in the software-object sense: the pressure receipt has its own stable identity separate from the proposal and from sibling pressure receipts. If that is the intended scope, the implementation is coherent and the smallest fix is vocabulary, not architecture.

## Rights / egress

Only connected GitHub repository text/metadata and attempted GitBook orientation were used. No source corpora, private research material, copyrighted scans, or local page bytes were sent to external research providers. Access is not treated as redistribution permission.

## Residual fog

- The owning intent behind the word `independent` in the new test name is not directly documented.
- PR #141 remains draft; semantics may still change before landing.
- The intended owner of lineage validation remains unresolved: constructor, composition layer, or explicit testimony boundary.
- Content-address collision/security properties are outside this audit; no cryptographic adequacy claim is made beyond observing SHA-256 canonical-body hashing.

## Smallest next discriminators

1. **`DIGEST-NOT-INDEPENDENCE-001`**: construct two distinct pressure receipts whose observation refs are explicitly declared descendants of the same dependency family; require distinct digests while preserving `independence: not_established` or equivalent at the owning lineage layer.
2. Rename `test_pressure_receipt_has_independent_stable_identity` to something unambiguous such as `test_pressure_receipt_has_own_stable_content_identity` if object identity is the intended meaning.
3. Retain the prior **`INDEPENDENCE-REQUIRES-LINEAGE-001`** discriminator for `interpretation="independently_supported"`; content addressing does not close it.

## Receipt

- Researcher/agent: ALEXDEEPDIVE
- Tool/model boundary: connected GitHub repository surfaces; GitBook orientation attempted but organization-scoped access unresolved; no external scholarship or computation needed.
- External byte egress: none beyond connected project-source retrieval.
- Durable location: `research/ALEX-DEEPDIVE-2026-09-20-2321-CONTENT-ADDRESS-NOT-INDEPENDENCE.md`
- Promotion: none
