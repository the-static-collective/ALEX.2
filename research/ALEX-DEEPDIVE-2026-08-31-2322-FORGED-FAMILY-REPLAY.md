# ALEXDEEPDIVE — FORGED-FAMILY-REPLAY-001

**Date:** 2026-08-31  
**Status:** RESEARCH / AUDIT · NO RUNTIME CHANGE · NO AUTHORITY PROMOTION  
**Promotion:** none

## Finding

The prior `RESULT-ADMISSIBILITY-001` packet proposed one smallest discriminator:

> feed the NAME family gate six forged `READY` results, omit the upstream provenance fields, reuse one identical valid SHA-256 packet digest across all six specimen types, and give only `NOMEN_SACRUM` the material-witness field necessary to pass its special check.

That discriminator now has a behavioral result.

Using an executable mirror of the current `main` implementation of `evaluate_name_six_specimen_gate()`, the hostile six-result family returned:

```text
DIVE_READY
```

and its output receipt preserved the same repeated packet digest six times.

This matters because a lawful upstream packet digest commits the full packet record, including `specimen_type`. Therefore one identical packet digest cannot honestly identify six different lawful packet records with six different specimen types unless there is a SHA-256 collision or the downstream result-shaped objects are not actually bound to the packet records they claim to represent.

The smallest surviving law is now sharper than the previous packet:

> **A DOWNSTREAM RESULT THAT CLAIMS A CONTENT DIGEST MUST PRESERVE A CHECKABLE BINDING BETWEEN THAT DIGEST AND THE SEMANTIC FIELDS THE CONSUMER RELIES ON.**

For this gate specifically:

```text
DIFFERENT SPECIMEN TYPE + SAME PACKET DIGEST
=>
NOT SIX LAWFUL UPSTREAM PACKET EVALUATIONS
```

under the current packet-digest construction, absent a cryptographic collision.

This is an ALEX provenance/composition finding only. It says nothing about the truth or falsity of the NAME historical/theological research family.

---

# Ground

- **Question:** Does the concrete hostile specimen proposed by `RESULT-ADMISSIBILITY-001` actually pass the current NAME family gate, and what is the narrowest architectural conclusion if it does?
- **Desired consequence:** Convert a static suspicion into a reproducible discriminator result and identify the smallest invariant worth preserving downstream.
- **Stop condition:** Reproduce or falsify the hostile specimen against the current function semantics, inspect the owner design boundary, pressure the result against established attestation/provenance practice, and leave one bounded next move.
- **Corpus/date/language/geography:** ALEX.2 `main` at `054b4db97e4a62368538f0da614b2e4f2ab2c855`, observed 2026-08-31; English software/provenance standards.
- **Authority/effect boundary:** Research packet only. No runtime change, canon, historical claim, theological claim, publication authority, or owning-project admission.
- **Task shape:** `AUDIT`
- **Formation trace active:** compact only.

---

# Front Room orientation / source boundary

The Static Collective Front Room remains the intended orientation membrane: orient, traverse narrowly, keep project-owned evidence authoritative, and preserve fog.

A fresh GitBook page retrieval was attempted in this run but the connector call was blocked by the host safety layer. That is recorded here as an access failure, not as absence or change. Orientation therefore relied on the canonical Front Room text already retrieved in the immediately preceding ALEX setup context; no downstream GitBook claim in this packet depends on an unverified new page revision.

The current ALEX repository itself remained fully accessible and is the authority for the runtime/design findings below.

---

# World cut

## Current ALEX head

At the time of inspection, `main` still pointed to:

- `054b4db97e4a62368538f0da614b2e4f2ab2c855` — `research: add ALEXDEEPDIVE result-admissibility packet`
- <https://github.com/the-static-collective/ALEX.2/commit/054b4db97e4a62368538f0da614b2e4f2ab2c855>

No newer ALEX.2 commit had landed after the prior deep-dive packet. This run therefore did **not** force a novel topical frontier; it audited the previous packet's smallest live discriminator.

## Included ALEX sources

1. `AGENTS.md` on current `main`
2. `skills/alex/SKILL.md` on current `main`
3. `skills/alex/references/research-receipt.md` on current `main`
4. `alex_runtime/name_specimen_gate.py` on current `main`
5. `alex_runtime/digests.py` on current `main`
6. `tests/test_name_specimen_gate.py` on current `main`
7. `docs/superpowers/specs/2026-08-29-name-six-specimen-gate-001-design.md`
8. `docs/superpowers/plans/2026-08-29-name-six-specimen-gate-001-review-amendment.md`
9. `research/ALEX-DEEPDIVE-2026-08-31-1726-RESULT-ADMISSIBILITY.md`

## Included external primary sources

1. IETF RFC 9334, **Remote ATtestation procedureS (RATS) Architecture**, January 2023  
   <https://www.rfc-editor.org/rfc/rfc9334.html>
2. SLSA v1.2, **Build: Verifying artifacts**  
   <https://slsa.dev/spec/v1.2/verifying-artifacts>
3. SLSA v1.2, **Provenance**  
   <https://slsa.dev/spec/v1.2/provenance>

## Deliberately omitted doors

- no NAME manuscript/historical/theological adjudication;
- no nomina-sacra image research;
- no cryptographic redesign;
- no runtime patch;
- no claim that network-grade remote attestation is required for this local proving slice;
- no traversal into older open ALEX draft PRs except to confirm no newly landed mainline evidence displaced this frontier.

## Sufficiency

**Sufficient** to establish the hostile family behavior and the repeated-digest contradiction under current packet semantics. **Unresolved** which implementation boundary should own the eventual fix.

---

# Acquisitions

| ID | Provider | Item and locus | Method/time | Resolution | Rights/egress |
| --- | --- | --- | --- | --- | --- |
| A1 | GitHub | ALEX.2 `main` branch | repository API, 2026-08-31 | exact head SHA | public repo |
| A2 | GitHub | `alex_runtime/name_specimen_gate.py` | file fetch | exact current source | public repo |
| A3 | GitHub | `alex_runtime/digests.py` | file fetch | exact current source | public repo |
| A4 | GitHub | `tests/test_name_specimen_gate.py` | file fetch | exact current tests | public repo |
| A5 | local computation | hostile six-result replay | executable mirror of exact current gate logic | behavioral output captured | no external byte egress |
| A6 | RFC Editor | RFC 9334 | web read | primary standard | public |
| A7 | SLSA | v1.2 verification/provenance docs | web read | primary project specification | public |

---

# The hostile specimen

The current family gate consumes result-shaped mappings rather than original packet mappings.

For each of the six required specimen types, the audit constructed a `READY` result containing only the fields currently checked by the family gate:

```text
packet result:
  schema = alex.name-specimen-packet-result/v0
  disposition = READY
  authority = none

receipt:
  schema = alex.name-specimen-packet-receipt/v0
  specimen_type = one of six required values
  packet_digest = sha256:0000...0000   # identical for all six
  authority = none

NOMEN_SACRUM only:
  material_witness_ref = valid sha256-shaped ref
```

The five text-first receipts intentionally omitted:

```text
packet_id
attestation_ref
transform_refs
hypothesis_ref
null_battery_ref
receipt_refs
material_witness_ref
```

which are emitted by a lawful `evaluate_name_specimen_packet()` READY result.

The gate accepted all six and returned:

```text
schema: alex.name-six-specimen-gate-result/v0
disposition: DIVE_READY
authority: none
```

Its gate receipt included six copies of the same packet digest.

This confirms the previous packet's static prediction.

---

# Why the repeated digest is a stronger discriminator than an arbitrary missing field

The packet evaluator computes:

```text
packet_digest = sha256_json(record)
```

and the original packet record includes `specimen_type` among its required fields.

Therefore, for lawful upstream packets:

```text
packet_A.specimen_type != packet_B.specimen_type
```

implies their canonical JSON byte strings differ.

If their SHA-256 packet digests are nevertheless equal, one of two things must be true:

1. a SHA-256 collision occurred; or
2. at least one downstream result is not actually bound to the packet record implied by its declared specimen type.

The second is overwhelmingly the relevant software explanation in this synthetic audit.

This makes repeated packet digests across different required specimen types an unusually cheap hostile specimen because it does not require the family gate to understand the historical research. It only requires consistency with the upstream digest contract it already claims to consume.

---

# Claims ledger

| ID | Claim | Class | Supporting evidence path | Counterevidence | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | Current `main` had no commit after the previous ALEXDEEPDIVE packet at inspection time. | observed | A1 | later commits can change this | supported for world cut |
| C2 | The family gate accepts externally assembled result-shaped mappings. | observed | A2 + A4 | may be intended only for trusted callers | supported |
| C3 | The hostile six-result family with one repeated digest returns `DIVE_READY`. | observed | A2 + A5 | executable mirror rather than checked-out repository process | supported; replay should be frozen as repo test for strongest proof |
| C4 | A lawful upstream packet digest commits `specimen_type`. | observed | A2 + A3 | none in current schema | supported |
| C5 | The same digest honestly representing six distinct lawful specimen packet records would require a SHA-256 collision or false downstream binding. | inference from cryptographic/content model | A2 + A3 + C4 | theoretical hash collision is not logically impossible | strongly supported |
| C6 | Digest uniqueness alone would solve result admissibility. | proposal | none | forged unique digests would still pass | disproved/overstrong |
| C7 | Downstream reliance needs a checkable binding between relied-on semantic fields and the claimed upstream result/input. | architectural inference | C2-C5 + RFC 9334 + SLSA v1.2 | same-process trusted composition may satisfy the binding without signatures | supported |

---

# Counterevidence and nearest boring explanation

## 1. Trusted in-process composition may be the intended deployment

The strongest boring explanation remains that these functions are a local proving slice. A lawful caller may be expected to execute `evaluate_name_specimen_packet()` and immediately pass its Python result dictionaries into the family gate without any untrusted serialization boundary.

If that is the contract, the practical attack surface is much smaller than the function signature alone suggests.

But the current code and design do not mechanically enforce that calling discipline. The family evaluator accepts plain mappings, and the tests themselves construct family-gate packet results directly.

So the issue is best stated as a **contract ambiguity / composition invariant gap**, not automatically a security vulnerability.

## 2. A duplicate-digest rejection is necessary as a hostile check but insufficient as provenance

Adding:

```text
len(packet_digests) == len(set(packet_digests))
```

would kill this exact specimen.

It would not establish that six distinct forged digests were produced by lawful upstream packet evaluation.

Therefore:

```text
DIGEST UNIQUENESS != RESULT ADMISSIBILITY
```

The duplicate check is a cheap contradiction detector, not the whole membrane.

## 3. Revalidating every emitted receipt field still does not prove evaluator origin

The family gate could re-check `packet_id`, `attestation_ref`, `transform_refs`, `hypothesis_ref`, `null_battery_ref`, and `receipt_refs` syntax.

That would improve semantic consistency but would still accept a sufficiently complete hand-forged receipt.

So:

```text
FULLER SHAPE VALIDATION != ORIGIN BINDING
```

## 4. Cryptographic signatures are still not automatically required

RFC 9334 and SLSA demonstrate mature architectures in which relying parties verify producer/verifier identity and bind results to expected subjects/policies. Their relevance here is structural.

For local ALEX, an exact in-process call, a sealed/opaque result type, or a resolvable content-addressed packet followed by deterministic evaluator replay may be sufficient. Network-grade signing would be premature unless results cross a boundary that requires independent authentication.

---

# External pressure

## RFC 9334

RATS separates:

```text
Evidence -> Verifier -> Attestation Result -> Relying Party
```

and the Relying Party applies its own appraisal policy to the Attestation Result. The standard also explicitly discusses authenticity, integrity protection, freshness, and trust in the Verifier.

The useful analogy for ALEX remains:

```text
packet -> packet evaluator -> packet result -> family gate
```

The key lesson is not that ALEX needs RATS. It is that **a downstream consumer owns the decision about whether an upstream evaluative result is admissible for its purpose**.

## SLSA v1.2

SLSA artifact verification requires more than a provenance object parsing successfully. Verification checks include trusted builder identity, provenance authenticity, and that the statement's subject digest matches the artifact being checked.

That subject-binding check is the closest external pressure on this run's concrete result:

> the digest inside a result must match the thing the result is being relied upon to describe.

ALEX's current family gate checks digest syntax but does not resolve or recompute the packet whose digest is claimed.

Again, this is a formal architecture analogy, not shared genealogy.

---

# Discovery trace

| ID | From | To | Move | Role | Reason |
| --- | --- | --- | --- | --- | --- |
| D1 | prior deep-dive | repeated-digest hostile specimen | discriminator | motive | prior packet named this as smallest next test |
| D2 | current main inspection | no newer commit | boundary | evidence | prevented forced novelty |
| D3 | gate source | executable hostile family | replay | evidence | test actual function semantics |
| D4 | `packet_digest = sha256_json(record)` | specimen-type commitment | inference | evidence-bearing inference | specimen type is inside hashed packet record |
| D5 | RFC 9334 / SLSA | downstream subject/result binding | formal analogy | counterpressure | tests whether local law is a familiar trust-boundary pattern |

`DISCOVERY TRACE != EVIDENCE PATH` remains in force.

---

# What broke / what survived from the previous packet

## Previous possibility: maybe the static hostile object only looked admissible

**Broke.** The executable mirror returned `DIVE_READY` exactly as predicted.

## Previous possibility: duplicate digest rejection might be the fix

**Broke as a complete solution.** It is only one cheap invariant. Six unique forged digest strings would still satisfy the current downstream checks.

## Previous survivor: downstream result admissibility requires more than schema/digest shape

**Strengthened.** The result is now behaviorally demonstrated.

## New narrower survivor

> **WHEN A CONSUMER RELIES ON A FIELD THAT IS SUPPOSED TO BE COMMITTED BY AN UPSTREAM DIGEST, THE CONSUMER NEEDS A LAWFUL WAY TO CHECK THAT RELATION OR A TRUST BOUNDARY THAT GUARANTEES IT.**

---

# Residual fog

1. Is `evaluate_name_six_specimen_gate()` intended as a public composition boundary for persisted/deserialized packet results, or only as an internal pure helper for trusted same-process outputs?
2. Does ALEX already have an owner-local opaque/typed-result pattern that can express “this value came from evaluator X” without introducing signatures or a new global schema?
3. Should the family gate consume original packet records and invoke `evaluate_name_specimen_packet()` itself, or should packet results become independently resolvable/replayable occurrences?
4. Would the owning architecture prefer a cheap duplicate-digest hostile guard even before the deeper provenance membrane is settled?
5. The GitBook Front Room could not be freshly retrieved during this run; no claim is made that its live-frontier text is unchanged.

---

# Smallest next discriminators

1. **Freeze the exact hostile family as a RED repository test.** It should assert that six distinct specimen types cannot all be `DIVE_READY` while sharing one packet digest. This proves the concrete invariant without choosing the full provenance architecture.
2. **Run a second hostile family with six unique forged digests and fully populated receipt-shaped fields.** If that still passes, it cleanly demonstrates why uniqueness + shape validation remain insufficient and forces the owner to name the intended trust boundary.
3. **Inspect existing ALEX owner-local result/occurrence patterns before designing anything new.** Prefer reuse of a resolvable occurrence/evaluator identity mechanism if one already exists; do not mint a new signature framework merely because the analogy points toward attestation systems.

---

# Receipt

- **Created:** 2026-08-31
- **Researcher/agent:** ALEXDEEPDIVE automated research pass
- **Tool/model boundary:** GitHub connected repository reads/writes; GitBook attempted but fresh page read blocked by host safety layer; public web reads for RFC/SLSA; local deterministic computation for hostile replay.
- **External byte egress:** public repository/source text only; no local private corpus bytes sent externally.
- **Durable location:** `research/ALEX-DEEPDIVE-2026-08-31-2322-FORGED-FAMILY-REPLAY.md`
- **Promotion:** none

## Seal

> **THE FIRST TEST PROVED THE FAMILY CAN BE FORGED. THE SECOND TEST MUST DISCOVER WHAT THE FAMILY ACTUALLY TRUSTS.**

> **DIGEST UNIQUENESS CAN CATCH A CONTRADICTION. IT CANNOT CREATE PROVENANCE.**
