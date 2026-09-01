# ALEX-DEEPDIVE — TRUST-BOUNDARY-CARRY-001

**Date:** 2026-09-01  
**Status:** RESEARCH / AUDIT · NO RUNTIME CHANGE · NO AUTHORITY PROMOTION  
**Promotion:** none

## Finding

PR #84 materially advances the NAME gate by proving a lawful happy path:

```text
six packet mappings
  -> evaluate_name_specimen_packet(...)
  -> six actual packet-result objects
  -> evaluate_name_six_specimen_gate(...)
  -> DIVE_READY
```

That is important, but it answers only an **existence / compatibility** question:

> Can the downstream gate consume results genuinely emitted by the upstream evaluator?

It does **not** answer the separate **admissibility / portability** question:

> When a packet-result-shaped object reaches the downstream gate, what makes its claimed upstream ancestry trustworthy?

The current repository therefore now exposes a sharper boundary than the prior distinct-forgery audit:

```text
LAWFUL COMPOSITION PATH EXISTS
!=
THE DOWNSTREAM GATE ENFORCES THAT PATH
```

The strongest survivor of this pass is:

> **DIRECT COMPOSITION MAY BE A SUFFICIENT LOCAL TRUST BOUNDARY, BUT ITS ASSURANCE DOES NOT AUTOMATICALLY TRAVEL WITH A SERIALIZED RESULT.**

This suggests ALEX should choose the transport contract before adding cryptographic or replay machinery.

---

# ALEX research receipt

## Ground

- **Question:** What does the newly landed lawful-ancestry composition test establish, and what trust decision remains unresolved?
- **Desired consequence:** Narrow the next implementation decision so ALEX does not overbuild signatures, stores, or replay machinery before deciding whether packet results are boundary-local or portable.
- **Stop condition:** A source-grounded distinction between direct composition, portable result transport, and consumer-local appraisal, plus the smallest discriminator that can decide ALEX's v0 contract.
- **Corpus/date/language/geography:** ALEX.2 `main` at `e38d977ccad55096e3097841805962482c5369e3`; current NAME gate implementation and tests; IETF RATS RFC 9334; SLSA v1.2 provenance/build requirements; in-toto public documentation. English; no geographic restriction.
- **Authority/effect boundary:** Research only. No runtime, schema, canon, theological, or historical promotion. No source corpora or private research bytes committed.
- **Task shape:** AUDIT
- **Formation trace active:** no

## World cut

### Included

- ALEX.2 `AGENTS.md` on current `main`.
- ALEX skill and research-receipt contract on current `main`.
- Commit `e38d977ccad55096e3097841805962482c5369e3` / PR #84.
- `tests/test_name_specimen_gate.py` on current `main`.
- `alex_runtime/name_specimen_gate.py` on current `main`.
- IETF RFC 9334 Remote ATtestation procedureS (RATS) Architecture.
- SLSA v1.2 provenance and build requirements.
- in-toto getting-started documentation.

### Deliberately omitted

- The historical/theological content of the six NAME specimens; this audit is about result ancestry and transport semantics only.
- Adjacent Static Collective repos; no neighboring project was required to resolve this boundary.
- Cryptographic implementation selection; the contract question precedes mechanism choice.

### Missing / inaccessible

- Fresh GitBook Front Room retrieval was attempted but blocked by the connector safety layer. This is access fog, not evidence of absence or change.
- No explicit current ALEX document was found in this bounded cut declaring whether `alex.name-specimen-packet-result/v0` is permitted to cross persistence / serialization / process boundaries.

### Sufficiency

Sufficient to identify the unresolved contract boundary. Insufficient to decide the owner intent of portable versus boundary-local result transport without an explicit repository declaration.

---

## Acquisitions

| ID | Provider | Item and locus | Resolution | Rights / egress |
| --- | --- | --- | --- | --- |
| A1 | GitHub | ALEX.2 commit `e38d977...` / PR #84 | exact diff | public repository |
| A2 | GitHub | `tests/test_name_specimen_gate.py` @ main | full text | public repository |
| A3 | GitHub | `alex_runtime/name_specimen_gate.py` @ main | full text | public repository |
| A4 | GitHub | `AGENTS.md`, `skills/alex/SKILL.md`, research receipt | full text | public repository |
| A5 | RFC Editor | RFC 9334 | primary standards document | public |
| A6 | SLSA | v1.2 provenance/build requirements | primary project specification | public |
| A7 | in-toto | getting-started documentation | primary project docs | public |

---

## Claims

| ID | Claim | Class | Supporting evidence path | Counterevidence / limit | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #84 proves that six real outputs of `evaluate_name_specimen_packet()` can compose to `DIVE_READY`. | observed | A1 -> added test -> evaluator outputs -> family gate assertion | test proves one constructed happy path, not all possible transport modes | supported |
| C2 | The ordinary helper `packet_result()` still manufactures packet-result-shaped dictionaries directly rather than obtaining them from the upstream evaluator. | observed | A2 -> helper + ordinary positive family test | helper is test scaffolding and may intentionally bypass production ancestry | supported |
| C3 | The family gate still accepts result-shaped dictionaries by validating declared fields/invariants; it has no check that a READY object was actually emitted by `evaluate_name_specimen_packet()`. | observed | A3 -> `evaluate_name_six_specimen_gate()` | Python object origin may be guaranteed externally by a caller contract | supported |
| C4 | Direct same-entity / same-process composition can be a legitimate trust arrangement if the boundary is declared. | source testimony / inference | A5 -> combined roles may communicate via function calls; same-entity interaction can provide stronger confidence | RATS is an architectural analogy, not authority over ALEX semantics | supported as analogy |
| C5 | Trust in an attestation/provenance result does not arise from shape alone; downstream reliance depends on producer trust and consumer policy. | source testimony | A5 -> Verifier produces Attestation Result; Relying Party appraises it under its own policy; authentic result is required | RATS concerns remote attestation, not ALEX research packets | supported as structural precedent |
| C6 | When provenance crosses a boundary as a portable artifact, mature systems usually preserve an authenticity or verification relation to the producer / subject. | source testimony | A6/A7 -> producer trust boundary, signatures, subject/material checks | local trusted pipelines can use lighter mechanisms | supported |
| C7 | Therefore ALEX should decide whether packet results are boundary-local or portable before choosing signatures/replay/store design. | inference / proposal | C1-C6 | a third contract could exist (e.g. portable only through a trusted wrapper) | live proposal |

---

## What PR #84 actually proves

The new test does three useful things.

### 1. It proves interface compatibility

The packet evaluator's real `READY` output is accepted by the family gate without translation or repair.

That matters because a consumer contract can easily drift away from its producer even when each side has isolated unit tests.

### 2. It proves lawful digests naturally satisfy the new distinctness rule

Six distinct specimen packets evaluated upstream produce six distinct packet digests in the constructed fixture. The family gate preserves those exact digests in its own receipt.

This demonstrates that PR #82's distinct-digest refusal does not break the intended composition path.

### 3. It creates a positive ancestry witness

There is now an executable specimen of the route that the architecture appears to prefer:

```text
packet
 -> packet evaluator
 -> packet result
 -> family gate
```

That is stronger than documentation alone.

But it remains a **witness of one lawful route**, not an enforcement mechanism that excludes alternate routes.

---

## What it does not prove

The ordinary positive helper remains:

```text
packet_result(specimen_type)
 -> hand-constructed result dict
 -> family gate
 -> DIVE_READY
```

Those helper digests are syntactically valid and distinct but are not computed from packet mappings by `sha256_json(record)`.

The current gate checks, among other things:

```text
result schema
result authority == none
READY receipt schema
READY receipt authority == none
NOMEN_SACRUM material witness validity
known specimen type
valid SHA-shaped packet digest
distinct specimen types
distinct packet digests
complete six-specimen family
```

It does not receive the original packet and therefore cannot recompute the packet digest. It also does not authenticate the evaluator as producer.

So the surviving distinction is:

```text
HAPPY-PATH ANCESTRY WITNESS
!=
ANCESTRY ENFORCEMENT
```

This is not automatically a defect. It becomes a defect only if the contract allows untrusted or reconstructed result objects to enter the family gate while downstream semantics rely on upstream evaluation having occurred.

---

## Primary-source pressure

### IETF RATS: locality can be a real trust boundary

RFC 9334 explicitly permits multiple roles to exist in one entity. Interactions between such roles can happen through function calls, sockets, local buses, or other non-network channels. The RFC notes that such arrangements can provide stronger confidence in the correctness of supplied information.

That is a direct structural precedent for a lightweight ALEX contract:

```text
packet evaluator + family gate
inside one declared trusted process / component
```

Under that contract, ALEX may not need a signature between the two functions. The caller topology itself carries the assurance.

But RFC 9334 also keeps roles and appraisal responsibilities distinct: a Verifier produces an Attestation Result; a Relying Party uses its own appraisal policy, and by default does not simply believe an attester is compliant. The result must be authentic relative to the relying party's trust assumptions.

Source: https://www.rfc-editor.org/rfc/rfc9334.html

### SLSA: producer trust boundary matters

SLSA's provenance guidance emphasizes that trustworthy provenance is generated inside the identified producer / build-platform trust boundary, and downstream verification checks integrity and the producer identity needed to rely on it.

This does not imply ALEX should adopt SLSA signatures. It supports the narrower principle:

```text
claim about origin
requires a declared origin trust relation
```

Source: https://slsa.dev/spec/v1.2/provenance  
Source: https://slsa.dev/spec/v1.2/build-requirements

### in-toto: portable chain evidence requires carried linkage

in-toto uses signed layout/link metadata so downstream verification can establish that intended steps were performed by authorized functionaries and that materials/products match the declared chain.

Again, this is a portability precedent rather than an implementation prescription.

Source: https://in-toto.io/docs/getting-started/

---

## The three contracts ALEX could lawfully choose

### Contract A — boundary-local results

```text
packet-result objects are ephemeral
family gate is called only with direct evaluator outputs
no persistence / deserialization / external construction is supported
```

Then the trust relation is largely architectural:

```text
trusted caller topology -> trusted evaluator invocation -> consumer
```

The current happy-path test becomes highly relevant evidence for this contract.

Possible hardening would be mostly documentation / API surface reduction, not cryptography.

### Contract B — portable results

```text
packet-result objects may be persisted, transmitted, reconstructed, or loaded later
```

Then the result must carry or resolve enough information to establish the origin relation independently of Python object history.

Possible mechanisms include, without choosing one yet:

- original packet retrieval + deterministic replay;
- content-addressed result store whose writer boundary is trusted;
- authenticated / signed result envelope;
- verifier/evaluator identity + result digest + trust policy;
- a higher-order receipt referencing both input packet digest and evaluator identity/version.

The mechanism must be selected against actual threat and deployment boundaries.

### Contract C — portable only through an owning wrapper

ALEX could allow serialized transport only through a separate trusted composition artifact that owns the binding.

For example:

```text
packet
 -> evaluator
 -> result
 -> composition receipt / bundle
 -> family gate
```

The raw result remains insufficient alone; the wrapper carries the verified ancestry relation.

This can preserve small packet receipts without pretending each receipt is independently self-authenticating.

---

## Nearest boring explanation

The simplest explanation is that `evaluate_name_six_specimen_gate()` was designed as a pure structural evaluator inside a trusted local Python composition, while tests use hand-built objects merely to isolate family-gate semantics.

If so, the current code may be correct for its intended deployment.

The missing piece is not more validation. It is a written contract such as:

```text
v0 packet results are process-local evaluator outputs.
Persisted or reconstructed packet-result objects are outside contract.
```

That one sentence would materially change the interpretation of the prior forgery specimens: they would remain useful hostile boundary tests, but would test an unsupported caller rather than a runtime vulnerability.

---

## Direct counterexample to over-hardening

Suppose ALEX adds signatures to every packet result but all components remain inside one trusted process, no result is ever persisted, and the signing key is accessible to the same process that constructs the objects.

The added signature may provide little or no new separation while increasing key-management complexity and creating a false impression that semantic correctness is cryptographically proven.

Therefore:

```text
CRYPTOGRAPHIC BINDING
!=
AUTOMATICALLY STRONGER ARCHITECTURE
```

The benefit exists only relative to a declared boundary / adversary / portability need.

---

## Contradictions and alternatives

1. **Alternative: schema completeness is enough.** Rejected as a general claim. A complete but invented receipt can still be invented.
2. **Alternative: distinct packet digests prove ancestry.** Rejected. Distinctness proves a relation among claims, not their producer lineage.
3. **Alternative: every result must be signed.** Not earned. Same-process direct composition may already provide sufficient confidence for the intended v0 boundary.
4. **Alternative: recompute packet digest downstream.** Currently blocked unless the downstream consumer also receives or resolves the complete original packet mapping; the receipt is not the complete hashed packet.
5. **Alternative: trust the Python object identity.** Object identity can help only while remaining inside a controlled live process; it does not survive ordinary serialization as provenance.

---

## Bridge ledger

| Move | Type | Evidence bearing | Promotion limit |
| --- | --- | --- | --- |
| RATS combined-role function call -> ALEX direct evaluator composition | formal architectural analogy | supports plausibility of a local trust boundary | does not make RATS normative for ALEX |
| RATS relying-party appraisal -> family-gate local invariants | formal analogy | supports consumer-local policy distinction | no identity of security goals claimed |
| SLSA producer trust boundary -> ALEX evaluator origin | formal analogy | supports explicit producer/boundary declaration | no requirement to adopt SLSA levels/signatures |
| in-toto portable signed links -> possible ALEX portable result wrapper | formal analogy | demonstrates one mature portability pattern | implementation not selected |

---

## Residual fog

- Owner intent for packet-result portability is not explicitly declared in the bounded sources inspected.
- It is unknown whether future ALEX runtimes plan to persist these result objects, pass them between processes, or expose them to other repositories.
- Threat model is undeclared: accidental misuse, hostile caller, stale replay, cross-process tampering, and multi-user boundaries require different machinery.
- The current gate's `producer` field is required but does not itself establish producer authenticity.
- Whether a composition wrapper already exists elsewhere in the repo was not needed for this cut and was not globally searched after the local boundary became sufficient.

---

## Smallest next discriminators

1. **Freeze the v0 transport contract in one testable sentence.** Choose whether `alex.name-specimen-packet-result/v0` is (A) process-local only, (B) portable, or (C) portable only inside an owning composition wrapper.
2. **If process-local:** add one hostile API-boundary test or wrapper proving reconstructed/deserialized result dictionaries are outside the supported entry path, or reduce the public surface so the family gate normally receives only evaluator outputs.
3. **If portable:** create the smallest persisted-result round-trip specimen and require a resolvable ancestry check. Do not choose signatures until that specimen defines the actual trust boundary.

---

## Verdict

The previous pass asked whether lawful ancestry had an executable positive path. PR #84 answers **yes**.

The surviving frontier is no longer “can these evaluators compose?” It is:

> **WHERE DOES THE TRUST BOUNDARY END?**

The cleanest ALEX law from this pass is:

```text
DIRECT COMPOSITION CAN CARRY LOCAL CONFIDENCE.
SERIALIZATION DOES NOT CARRY THAT CONFIDENCE FOR FREE.
PORTABILITY REQUIRES A DECLARED BINDING MECHANISM OR OWNER TRUST CONTRACT.
```

No cryptographic redesign is yet earned.

## Receipt

- **Created:** 2026-09-01
- **Researcher / agent:** ALEXDEEPDIVE automated research pass
- **Tool/model boundary:** GitHub connector inspection + public web primary-source research; no local corpus bytes; no OCR/HTR; no source-image analysis
- **External byte egress:** public repository text and public standards/docs only
- **Durable location:** `research/ALEX-DEEPDIVE-2026-09-01-1130-TRUST-BOUNDARY-CARRY.md`
- **Promotion:** none
