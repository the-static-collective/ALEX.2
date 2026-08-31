# ALEXDEEPDIVE — RESULT-ADMISSIBILITY-001

**Date:** 2026-08-31  
**Status:** RESEARCH / PRESSURE · NO RUNTIME CHANGE · NO AUTHORITY PROMOTION  
**Promotion:** none

## Finding

The newest NAME proving slices exposed a narrower and more general ALEX frontier than the NAME hypothesis itself:

> **A HASH-SHAPED RESULT IS NOT YET AN ADMISSIBLE RESULT.**
>
> **DOWNSTREAM ADMISSIBILITY NEEDS A BINDING TO THE EVALUATOR, THE INPUT, AND THE POLICY/CONTRACT THAT PRODUCED THE RESULT.**

The current `NAME Six-Specimen Gate` already discovered part of this law in owner review: it had to stop blindly trusting upstream `READY` state for `NOMEN_SACRUM` material-witness presence and upstream `authority: none`.

A fresh static audit shows the same class of problem remains open more generally. For ordinary `READY` specimens, the family gate accepts a hand-constructed packet result that contains a valid schema, `authority: none`, specimen type, and syntactically valid packet digest even if the purported packet receipt omits most of the fields that the packet evaluator itself requires and emits. The gate also does not establish that the result was actually produced by the declared packet evaluator, does not bind it to a specific evaluator body/policy, and does not reject repeated packet digests across different specimen types.

This does **not** show that ALEX's historical research is false. It shows that the new readiness membrane is not yet a complete provenance membrane.

---

# Ground

- **Question:** What newly surfaced in ALEX's current NAME gate work that could materially deepen ALEX's provenance architecture?
- **Desired consequence:** Identify one bounded architectural research frontier and pressure it against established attestation/provenance systems without changing runtime semantics.
- **Stop condition:** Enough evidence to distinguish a local implementation bug, a general architectural law, and the smallest next discriminator.
- **Corpus/date:** ALEX.2 `main` as observed 2026-08-31; current IETF RATS/EAT material and SLSA v1.2 documentation available on 2026-08-31.
- **Authority/effect boundary:** Research packet only. No historical, theological, canonical, runtime, or admission authority.
- **Task shape:** `AUDIT + PRESSURE`
- **Formation trace active:** yes, compact.

## Why this thread was selected

The most recent ALEX commits are tightly clustered around a single chain:

1. NAME attestation + transform proving slice;
2. `WORLD-BRIDGE-001`;
3. `NAME-NULLS-001` hostile battery;
4. NAME six-specimen gate;
5. owner-review repair of forged upstream packet state.

The merge head observed for the six-specimen gate was:

- `b957e80a847318f736ed2657f3ead925c0113e07` — `Add NAME six-specimen dive gate`
- <https://github.com/the-static-collective/ALEX.2/commit/b957e80a847318f736ed2657f3ead925c0113e07>

This thread was chosen over older symbolic/decoder frontiers because it is both newly landed and architecture-bearing: the NAME work has produced a real downstream membrane whose correctness affects any future ALEX research family, regardless of subject matter.

---

# World cut

## Included ALEX sources

- `AGENTS.md` — current contributor constitution.
- `skills/alex/SKILL.md` — provenance-first research constitution.
- `skills/alex/references/research-receipt.md` — durable packet law.
- `docs/superpowers/specs/2026-08-29-name-attestation-transform-v0-design.md`
- `docs/superpowers/specs/2026-08-29-world-bridge-001-design.md`
- `docs/superpowers/specs/2026-08-29-name-nulls-001-design.md`
- `docs/superpowers/specs/2026-08-29-name-six-specimen-gate-001-design.md`
- `alex_runtime/name_specimen_gate.py` at blob `5f0e08ef3638c95752e1efb4ea5efef293ef88f7`
- `tests/test_name_specimen_gate.py` at blob `aeeaa103bb4bf11285749e837a5db98874e33821`

## Included external primary sources

1. IETF RFC 9334, **Remote ATtestation procedureS (RATS) Architecture**, January 2023  
   <https://www.rfc-editor.org/rfc/rfc9334.html>
2. IETF RFC 9711, **The Entity Attestation Token (EAT)**, April 2025  
   <https://www.rfc-editor.org/rfc/rfc9711.html>
3. IETF draft-ietf-rats-ear-04, **EAT Attestation Results**, 26 May 2026, work in progress  
   <https://datatracker.ietf.org/doc/html/draft-ietf-rats-ear>
4. SLSA v1.2, **Build: Verifying artifacts**, Approved  
   <https://slsa.dev/spec/v1.2/verifying-artifacts>
5. SLSA v1.2, **Provenance**, Approved  
   <https://slsa.dev/spec/v1.2/provenance>
6. NIST FIPS 205, **Stateless Hash-Based Digital Signature Standard**, 13 August 2024  
   <https://csrc.nist.gov/pubs/fips/205/final>

## Deliberately omitted doors

- No attempt to adjudicate the NAME-of-JESUS historical/theological hypothesis.
- No manuscript or nomina-sacra image research.
- No change to ALEX runtime.
- No assumption that network-grade cryptographic attestation is required for a local proving slice.

## Sufficiency

**Sufficient** to establish the local structural gap and a strong cross-domain architectural analogue. **Unresolved** whether ALEX should solve the deeper binding problem by local deterministic recomputation, a content-addressed store contract, cryptographic signatures/MACs, or a layered combination.

---

# What newly surfaced in ALEX

## 1. The owner-review correction found the right class of failure

The six-specimen owner-review amendment records two hostile cases that initially passed:

- forged `READY` `NOMEN_SACRUM` without a material witness;
- upstream packet result/receipt carrying widened authority.

The resulting law is strong:

```text
RECEIPT SHAPE != RECEIPT ADMISSIBILITY
DOWNSTREAM GATE != BLIND TRUST OF UPSTREAM CLAIMED STATE
READY LABEL != PROOF THAT READY PRECONDITIONS SURVIVE
AUTHORITY NONE MUST SURVIVE EVERY MEMBRANE
```

That correction is not an isolated patch. It points at the next architectural layer.

## 2. Current family-gate validation remains partial

For a `READY` packet result, `evaluate_name_six_specimen_gate()` currently checks:

- result is a mapping;
- result schema is correct;
- result authority is `none`;
- disposition is recognized;
- receipt is a mapping with the receipt schema;
- receipt authority is `none`;
- specimen type is one of the six;
- packet digest is syntactically `sha256:<64 hex>`;
- for `NOMEN_SACRUM`, material-witness ref is syntactically valid.

For the other five specimen types, it does **not** re-check that a READY receipt contains the packet evaluator's own required/emitted provenance fields:

```text
packet_id
attestation_ref
transform_refs
hypothesis_ref
null_battery_ref
receipt_refs
material_witness_ref (where applicable)
```

Nor does it establish that the packet result was actually produced by `evaluate_name_specimen_packet()`.

### Static hostile specimen

For an ordinary specimen, this object satisfies the current READY branch's checks:

```json
{
  "schema": "alex.name-specimen-packet-result/v0",
  "disposition": "READY",
  "reason": null,
  "receipt": {
    "schema": "alex.name-specimen-packet-receipt/v0",
    "packet_digest": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "specimen_type": "LXX_JOSHUA",
    "authority": "none"
  },
  "authority": "none"
}
```

It omits the attributable road that a true packet-evaluator receipt emits.

This finding comes from direct code-path inspection of `alex_runtime/name_specimen_gate.py`; it was not inferred from documentation alone.

## 3. The test suite itself confirms that the gate accepts externally assembled result objects

`tests/test_name_specimen_gate.py` builds packet results with a helper named `packet_result()` rather than obtaining every family-gate input by executing `evaluate_name_specimen_packet()`.

That is not automatically wrong. It is a normal unit-testing technique. But it confirms the public composition boundary: the family gate is designed to consume result-shaped data, not an unforgeable evaluator return type.

Therefore the family gate owns responsibility for whatever invariants it wants to rely on downstream.

## 4. Packet digest is commitment, not origin authentication

The packet evaluator computes:

```text
packet_digest = sha256_json(record)
```

This is valuable. It gives deterministic content identity for a packet record.

But at the family gate, the digest arrives as a string inside an untrusted result-shaped mapping. The gate checks only digest syntax. It does not:

- resolve the digest to a stored packet;
- recompute the packet evaluator on that packet;
- verify that the result is bound to a specific evaluator identity/version;
- verify a signature/MAC from a trusted evaluator;
- bind the result to a named appraisal policy/contract;
- reject a repeated packet digest used for multiple distinct specimen types.

So the current gate proves:

```text
THIS INPUT CONTAINS A SHA-256-SHAPED CLAIM
```

not yet:

```text
THIS READY RESULT DESCENDS FROM THE DECLARED PACKET UNDER THE DECLARED EVALUATOR CONTRACT
```

---

# External pressure: established attestation architectures

## IETF RATS: two-stage appraisal, not blind result consumption

RFC 9334 separates three relevant roles:

```text
Attester -> Evidence -> Verifier -> Attestation Results -> Relying Party
```

The Verifier appraises Evidence under an **Appraisal Policy for Evidence**. The Relying Party then applies its own **Appraisal Policy for Attestation Results** before making an application-specific decision.

This is unusually close to the ALEX membrane now forming:

```text
packet -> packet evaluator -> packet result -> family gate
```

The key RATS lesson is not “use remote attestation.” It is structural:

> **The downstream consumer does not treat the mere shape of an Attestation Result as sufficient. It has a trust relationship with the Verifier and applies a separate downstream appraisal policy.**

RFC 9334 explicitly discusses trust anchors for Verifiers and says the Relying Party trusts a Verifier capable of appraising the Attester. It also distinguishes Evidence from Attestation Results rather than allowing one to impersonate the other.

### Mapping to ALEX

| RATS | Possible ALEX analogue |
| --- | --- |
| Evidence | packet record + referenced occurrences |
| Verifier | exact packet evaluator body/contract |
| Appraisal Policy for Evidence | packet schema + semantic readiness contract |
| Attestation Result | `alex.name-specimen-packet-result/v0` |
| Relying Party | six-specimen gate |
| Appraisal Policy for Attestation Results | family-gate admissibility contract |
| Verifier trust anchor | exact evaluator body/version/store authority, potentially cryptographic later |

This is a **formal analogy**, not a claim that historical research packets are security attestations.

## RFC 9711 / EAR: verifier identity, policy identity, and freshness context survive downstream

RFC 9711 standardized EAT in April 2025. The current May 2026 EAR draft goes further for Attestation Results. Its appraisal structure includes, among other things:

- verifier identity;
- appraisal policy identifiers;
- optional nonce/freshness binding;
- explicit distinction between claims with Attester authority and claims with Verifier authority.

The May 2026 draft says the policy identifier list records which appraisal policies were used, and its examples carry an `ear_verifier_id` including developer/build identity. It also preserves freshness context through nonce claims.

This directly pressures an ALEX question:

> If a downstream ALEX gate relies on `READY`, which exact evaluator body and which exact readiness contract produced that `READY`?

A digest of the packet alone cannot answer that.

## SLSA v1.2: provenance is not useful until verified against trust and expectations

SLSA v1.2 is Approved. Its verification procedure does not stop at “the provenance object parses.” It recommends:

1. verify the builder identity against configured roots of trust;
2. verify the provenance envelope signature;
3. verify that the statement subject matches the artifact digest;
4. verify expected build type and external parameters.

SLSA also states that provenance is verifiable information about where, when, and how an artifact was produced.

The relevant architectural continuity is:

```text
DIGEST BINDING + PRODUCER IDENTITY + EXPECTATION/POLICY CHECK
```

not digest syntax alone.

## NIST: digest and signer authentication are different jobs

NIST FIPS 205 states that digital signatures detect unauthorized modification and authenticate the identity of the signatory.

ALEX should not infer from this that every local receipt needs a public-key signature. The useful boundary is more basic:

```text
HASH / DIGEST -> content commitment / identity primitive
AUTHENTICATED RESULT -> who/what is entitled to make this result claim
```

The current NAME runtime is strong on the first and intentionally minimal on the second.

---

# Counterevidence and nearest boring explanation

## Counterevidence 1 — this is a local proving slice, not an adversarial distributed protocol

The strongest boring explanation is that `name_specimen_gate.py` is intentionally small and local. If the only lawful caller obtains packet results by directly calling `evaluate_name_specimen_packet()` in the same trusted process and immediately passes those Python dictionaries to the family gate, issuer authentication adds little practical value.

Under that deployment contract, public-key signing would be unnecessary complexity.

**Consequence:** do not prematurely import RATS/EAT/SLSA wire/security machinery into ALEX.

## Counterevidence 2 — the gate is intentionally not supposed to recompute historical research

The owner-review amendment explicitly says the family evaluator does not recompute the underlying historical research; it validates only the invariants necessary for the packet result to mean what its declared disposition says.

That boundary should remain.

The new finding therefore does **not** imply:

```text
FAMILY GATE MUST RESEARCH EVERYTHING AGAIN
```

It implies only:

```text
FAMILY GATE MUST KNOW WHY IT IS ENTITLED TO TRUST THE UPSTREAM RESULT CONTRACT IT CONSUMES
```

## Counterevidence 3 — `packet_digest` indirectly commits to `producer`

The source packet includes `producer`, and the packet digest hashes the full record. Therefore, if the original packet can be resolved by digest, producer identity is indirectly committed.

This is useful and may make a local content-addressed solution sufficient.

But the current family gate does not resolve that packet, so the producer is not available at the decision surface. A commitment to inaccessible data is not the same thing as verified downstream provenance.

---

# Hypothesis lineage

## H0 — surfaced by the code

> A downstream ALEX gate must not trust an upstream `READY` label merely because the result has the right schema and hash-shaped references.

## H1 — literalized

> Every ALEX research receipt should be cryptographically signed by its producer.

**Verdict:** overstrong / not earned.

Why it broke:

- local in-process deterministic composition may not need cryptographic signatures;
- ALEX is not presently a hostile distributed verifier network;
- a content-addressed store plus exact evaluator replay may provide stronger semantic assurance with less machinery.

## H2 — corrected survivor

> A downstream gate that relies on an upstream evaluative disposition must have an attributable, verifiable binding between **input occurrence**, **evaluator body/contract**, and **result occurrence** sufficient for that trust boundary.

This can be satisfied by different mechanisms depending on deployment:

```text
same trusted process:
  direct evaluator call / opaque typed result

persisted local store:
  resolvable input digest + evaluator identity + deterministic replay

cross-process or untrusted transport:
  authenticated envelope/signature/MAC + trust/policy configuration
```

**Verdict:** strongly supported as an architectural law; mechanism remains unresolved.

## H3 — cross-domain survivor

> **Receipt admissibility is a two-stage relation: first establish what a producer concluded from its inputs; then establish whether this consumer is entitled to rely on that conclusion for this purpose.**

This survives across ALEX, RATS, and SLSA as a formal architecture pattern without asserting shared genealogy.

---

# Claims ledger

| ID | Claim | Class | Support | Counterevidence | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | The current family gate re-checks only a subset of READY packet-receipt invariants. | observed | `alex_runtime/name_specimen_gate.py` blob `5f0e08e...` | none found | supported |
| C2 | An ordinary READY result can omit packet provenance fields and still satisfy the current gate path. | inference from executable code path | same source; required fields absent from READY-branch validation | not executed in this run against a checkout | strongly supported / execution specimen recommended |
| C3 | The gate does not establish that a result was produced by `evaluate_name_specimen_packet()`. | observed | gate consumes arbitrary mappings; tests hand-construct result mappings | trusted-process calling convention may establish this externally | supported |
| C4 | The gate does not reject repeated packet digests across distinct specimen types. | observed | `packet_digests.append(...)` with no uniqueness check | SHA collision is not the issue; forged/replayed result input is | supported |
| C5 | RATS separates Evidence appraisal from downstream Attestation Result appraisal. | source testimony / standard | RFC 9334 | security domain differs from historical research | supported analogue |
| C6 | Current EAR work preserves verifier identity, policy identifiers, and freshness context in attestation results. | source testimony / work in progress | draft-ietf-rats-ear-04, 2026-05-26 | draft may change | supported, non-final |
| C7 | SLSA v1.2 verification requires producer trust/signature plus subject and expectation checks, not schema parsing alone. | source testimony / approved specification | SLSA v1.2 verification | software supply chain domain differs | supported analogue |
| C8 | ALEX therefore needs public-key signatures now. | proposal | weak | local deterministic replay may suffice | **not supported** |
| C9 | ALEX needs an explicit result-admissibility binding at any boundary where result-shaped data can be supplied independently of the evaluator call. | inference/proposal | C1-C7 | unnecessary if caller/result are unforgeably same-process by construction | strong candidate |

---

# Bridge ledger

| Move | Type | Evidence bearing | Promotion limit |
| --- | --- | --- | --- |
| RATS Verifier -> ALEX evaluator | formal analogy | architecture only | does not import security semantics automatically |
| RATS Attestation Result -> ALEX packet result | formal analogy | two-stage appraisal pattern | not historical evidence |
| SLSA provenance verifier -> ALEX family gate | formal analogy | producer/input/policy binding pattern | not software-supply-chain equivalence |
| NIST signature role -> possible ALEX authenticated envelope | documented mechanism + proposal | establishes what signatures can do | does not require signatures in v0 |

---

# Pressure

- **Quote-to-page check:** external claims were drawn from directly opened standards/specification pages; no manuscript quotation used.
- **Visual surface check:** not applicable; no image evidence inspected.
- **Edition/spec identity:** RFC 9334 final; RFC 9711 final; SLSA v1.2 Approved; EAR explicitly treated as a May 2026 Internet-Draft/work in progress.
- **Dependency/lineage check:** RATS/EAT/EAR are one standards family and are not counted as independent corroboration of each other. SLSA is an independent software-supply-chain architecture. NIST is independent cryptographic standards guidance.
- **Direct counterexample:** a syntactically valid ordinary READY result can omit most packet receipt fields on the current code path; repeated digest use is not rejected.
- **Nearest boring explanation:** proving-slice code trusts a local caller and therefore has not yet needed a persisted/untrusted result boundary.
- **Serendipity trap:** the NAME theme did not support this finding; recent NAME implementation changes merely exposed the membrane to inspect.
- **Replay impersonation:** specifically active. A SHA-shaped packet digest is not treated here as proof that the corresponding packet/evaluator execution was replayed.
- **Forced-equilibrium:** avoided. The structural gap is stronger than the case for any particular cryptographic remedy.

---

# PRESSURE verdict

- **Seed:** `RECEIPT SHAPE != RECEIPT ADMISSIBILITY`
- **Literal verdict:** supported.
- **What broke:** the overstrong idea that every ALEX result now needs a digital signature.
- **What survived:** downstream reliance on an evaluative result needs an attributable binding to the result's input and evaluator contract, appropriate to the actual trust boundary.
- **Why it survived:** current ALEX source still accepts result-shaped objects whose upstream provenance is not established locally; independent mature architectures explicitly separate content identity from trusted appraisal.
- **New prediction:** as more ALEX evaluators compose by passing persisted JSON results rather than direct function returns, this same failure class will recur unless result-admissibility becomes a reusable membrane.
- **Residual weirdness:** ALEX independently arrived at `DOWNSTREAM GATE != BLIND TRUST OF UPSTREAM CLAIMED STATE` immediately before this external comparison; the similarity is architecturally useful but not evidence of genealogy.

---

# Smallest next discriminators / repo-worthy moves

## 1. Add one hostile executable specimen before designing a framework

Create a test that gives the six-specimen gate six hand-forged `READY` results with:

- correct schemas;
- `authority: none`;
- six distinct specimen types;
- the **same** syntactically valid packet digest;
- omitted packet provenance fields except those currently inspected;
- a syntactically valid `material_witness_ref` only for `NOMEN_SACRUM`.

**Expected under current code:** likely `DIVE_READY` by direct code-path analysis.  
**Desired research discriminator:** decide whether this should be lawful under the declared gate contract. If not, freeze the failing specimen before changing semantics.

## 2. Specify `RESULT-ADMISSIBILITY-001` as a local contract, not a crypto mandate

Minimum candidate fields/relations:

```text
input_ref / input_digest
result_ref / result_digest
evaluator_body_ref or evaluator_contract_ref
policy/schema version
producer / evaluator identity
produced_at or occurrence anchor when time matters
authority: none
```

Then define one of three admissibility modes explicitly:

```text
DIRECT       — result came from direct trusted evaluator invocation
REPLAYED     — input resolved and deterministic evaluator replay matched
AUTHENTICATED — persisted/external result verified under a declared trust mechanism
```

Do not let these modes imply historical correctness.

## 3. Keep appraisal policy identity separate from evaluator identity

The strongest extraction from RATS/EAR/SLSA is not “sign everything.” It is:

```text
WHO/WHAT EVALUATED != WHAT RULES IT APPLIED != WHAT INPUT IT SAW != WHAT RESULT IT EMITTED
```

ALEX already separates object/carrier/transform/claim well. The next membrane may need the same separation for evaluative receipts.

---

# Discovery trace

| ID | From | To | Move | Role | Reason |
| --- | --- | --- | --- | --- | --- |
| D1 | Front Room | ALEX recent commits | orientation | motive | current request required strongest live frontier |
| D2 | six-specimen merge | owner-review amendment | audit | evidence | amendment named blind upstream trust explicitly |
| D3 | amendment | current evaluator source | pressure | evidence | test whether correction generalized |
| D4 | evaluator source | forged READY specimen | adversarial construction | counterexample | identify minimum accepted surface |
| D5 | ALEX membrane | RFC 9334/RFC 9711/EAR | formal comparison | analogy | test whether mature attestation systems separate appraisal stages |
| D6 | ALEX membrane | SLSA v1.2 | independent formal comparison | analogy | pressure producer/input/policy binding |
| D7 | digest semantics | NIST FIPS 205 | boundary check | evidence | distinguish digest identity from signer authentication |

`D1-D7` explain why this research happened. They are not evidence for the NAME hypothesis.

---

# Residual fog

1. The current repository may have an intended calling convention outside `name_specimen_gate.py` that guarantees all packet results originate from direct evaluator calls. That convention was not found in the bounded sources inspected here.
2. A future content-addressed occurrence store may make deterministic replay the natural trust mechanism, avoiding signatures for local use.
3. The right granularity of evaluator identity is unresolved: source commit, body registry SHA, semantic contract digest, or a combination.
4. Freshness may be irrelevant for immutable historical packet evaluation but important for mutable availability/rights/observer-cut claims. Do not import nonce semantics universally.
5. EAR draft-04 is work in progress and must not be treated as final IETF standard text.

---

# Compact law extracted

```text
CONTENT DIGEST != PRODUCER AUTHENTICATION
RESULT SHAPE != RESULT ADMISSIBILITY
READY != PROOF OF THE ROAD TO READY
UPSTREAM RESULT != DOWNSTREAM PERMISSION TO RELY

ADMISSIBLE RESULT
  = attributable input
  + attributable evaluator contract
  + attributable result
  + consumer-local reliance rule
```

The last equation is a research proposal, not runtime law.

---

# Receipt

- **Created:** 2026-08-31
- **Researcher/agent:** ALEXDEEPDIVE automated research pass
- **Tool/model boundary:** GitBook orientation; GitHub source inspection and durable write; public-web primary standards/specification research. No local manuscript bytes or private corpora were egressed.
- **External byte egress:** none from ALEX-held source corpora; only public repository/source URLs were queried.
- **Durable location:** `research/ALEX-DEEPDIVE-2026-08-31-1726-RESULT-ADMISSIBILITY.md`
- **Promotion:** none

> **THE RECEIPT MAY BE OPAQUE ABOUT THE EVIDENCE IT DOES NOT NEED TO RECOMPUTE. IT MAY NOT BE OPAQUE ABOUT WHY THIS CONSUMER IS ENTITLED TO RELY ON ITS DISPOSITION.**
