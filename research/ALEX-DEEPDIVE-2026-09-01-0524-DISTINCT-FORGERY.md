# ALEXDEEPDIVE — DISTINCT-FORGERY-001

**Date:** 2026-09-01  
**Status:** RESEARCH / AUDIT · NO RUNTIME CHANGE · NO AUTHORITY PROMOTION  
**Promotion:** none

## Finding

The previous ALEXDEEPDIVE packet ended with a second discriminator:

> Run a hostile NAME six-specimen family using six **distinct** forged packet digests and fully populated receipt-shaped fields. If that family still reaches `DIVE_READY`, digest uniqueness and receipt shape are both disproved as sufficient result-admissibility conditions.

That discriminator is now answered by the current repository itself.

After `FORGED-FAMILY-REPLAY-001`, PR #82 intentionally added the smallest gate-level repair only:

```text
same packet digest reused by two specimen types
=> REFUSE duplicate_packet_digest
```

The merge is sound for its stated scope. But the existing test helper `packet_result()` constructs six distinct packet-digest strings by hex-encoding the specimen-type names and padding them with zeros. Those strings are syntactically valid `sha256:<64 hex>` references, but they are not produced by `sha256_json(packet)`.

The baseline test then feeds those six directly constructed READY results to `evaluate_name_six_specimen_gate()` and expects:

```text
DIVE_READY
```

Therefore the current mainline test suite itself witnesses the next layer:

> **DISTINCT DIGEST CLAIMS != VERIFIED DIGEST BINDINGS.**

For the concrete Matthew specimen used in the packet tests, the lawful packet evaluator's canonical JSON digest is:

```text
sha256:2ad239591688cac651895498c2972b07e8ff9aa73dbc955188f49141c95bc6f6
```

while the family-test helper claims:

```text
sha256:6d6174746865775f315f32310000000000000000000000000000000000000000
```

The latter is the UTF-8 bytes of `matthew_1_21` rendered as hexadecimal and zero-padded. It is unique within the six-specimen helper set, but it is not the digest emitted by the upstream packet evaluator for the corresponding canonical test packet.

The narrowest surviving architectural law is therefore:

> **A CONTENT DIGEST BECOMES EVIDENCE OF BINDING ONLY WHEN THE CONSUMER CAN RESOLVE OR OTHERWISE AUTHENTICATE THE CONTENT/PRODUCER RELATION IT CLAIMS. UNIQUENESS IS ONLY A CONTRADICTION CHECK.**

This is a provenance/composition finding only. It does not adjudicate any NAME historical, textual, manuscript, or theological claim.

---

# Ground

- **Question:** After PR #82 closes repeated packet-digest reuse, does the NAME family gate now establish that each distinct digest is actually bound to a lawful upstream packet evaluation?
- **Desired consequence:** Determine whether the previous packet's second discriminator survives the new mainline repair, and identify the smallest next invariant without over-designing the runtime.
- **Stop condition:** Inspect current `main`, the PR #82 change and stated scope, the current packet evaluator, digest function, and family tests; compare one concrete helper digest against the canonical upstream digest; pressure the resulting claim against primary provenance/content-addressing standards; leave bounded discriminators.
- **Corpus/date/language/geography:** ALEX.2 `main` at `e378ffa097f05ec2529071c43a22ad4d7c5b23f9`, observed 2026-09-01; English software provenance/content-addressing standards.
- **Authority/effect boundary:** Research packet only. No runtime change, security-vulnerability designation, canon, historical claim, theological claim, publication authority, or owner admission.
- **Task shape:** `AUDIT`
- **Formation trace active:** compact only.

---

# Front Room orientation / source boundary

The Static Collective Front Room remains the orientation membrane: orient only, traverse narrowly, keep project-owned canonical evidence authoritative, and preserve fog.

A fresh GitBook API retrieval was attempted at the beginning of this run and was blocked by the host safety layer. This packet therefore uses the canonical Front Room text already retrieved in the immediately preceding ALEXDEEPDIVE context for orientation only. The failed fresh retrieval is recorded as an access limitation, not evidence that the Front Room is absent or unchanged.

No consequential claim below depends on a new GitBook revision. The ALEX repository itself is the owner-local authority for the runtime and test behavior examined here.

---

# World cut

## Current ALEX head

`main` is now:

- `e378ffa097f05ec2529071c43a22ad4d7c5b23f9` — merge of PR #82, **Crater smash: bind NAME family packet digests**.

PR #82 explicitly states its bounded TDD intent:

1. RED: reject six different specimen types reusing one packet digest.
2. GREEN: add the smallest gate-level distinctness check only.
3. No schema change, no cryptographic redesign, no research-truth promotion.

This matters because the present deep dive should not mischaracterize the remaining seam as a failed implementation of a broader promise. The merged patch did exactly what it said it would do. The newly visible frontier begins one layer beyond that bounded landing.

## Included ALEX sources

1. `AGENTS.md` on current `main`
2. `skills/alex/SKILL.md` on current `main`
3. `skills/alex/references/research-receipt.md` on current `main`
4. `alex_runtime/name_specimen_gate.py` on current `main`
5. `alex_runtime/digests.py` on current `main`
6. `tests/test_name_specimen_gate.py` on current `main`
7. PR #82 and merge commit `e378ffa097f05ec2529071c43a22ad4d7c5b23f9`
8. `research/ALEX-DEEPDIVE-2026-08-31-2322-FORGED-FAMILY-REPLAY.md`

## Included external primary sources

1. IETF RATS Endorsements draft-09, March 2026, extending the RFC 9334 architecture discussion of Verifier and Relying Party appraisal policy.
2. SLSA provenance / artifact verification specification, current published project documentation.
3. Open Container Initiative Image Specification — Content Descriptor, current standards text.

## Deliberately omitted doors

- no NAME manuscript, translation, nomen-sacrum, or theological adjudication;
- no runtime patch;
- no signature/key-management design;
- no claim that local ALEX must adopt RATS, SLSA, OCI, in-toto, or network-grade attestation;
- no traversal into unrelated Static Collective repositories;
- no attempt to promote a test-fixture artifact into a production exploit claim.

## Missing / inaccessible sources

- fresh GitBook Front Room retrieval was blocked by the host safety layer;
- no checked-out local repository process was available in this run, so the canonical-digest comparison was reproduced from the exact current `canonical_json_bytes()` / `sha256_json()` algorithm and test fixture rather than by invoking the repository's Python module directly.

## Sufficiency

**Sufficient** to establish that current test fixtures use six distinct but non-upstream-derived digest claims and that the family gate accepts them as `DIVE_READY`. **Unresolved** which trust/composition boundary the owning project wants next.

---

# Acquisitions

| ID | Provider | Item and locus | Method/time | Resolution | Rights/egress |
| --- | --- | --- | --- | --- | --- |
| A1 | GitHub | ALEX.2 `main` branch | branch API | exact head SHA | public repo |
| A2 | GitHub | PR #82 + merge commit | PR/commit API | exact patch + stated scope | public repo |
| A3 | GitHub | `alex_runtime/name_specimen_gate.py` | raw/current file | exact source | public repo |
| A4 | GitHub | `alex_runtime/digests.py` | raw/current file | exact source | public repo |
| A5 | GitHub | `tests/test_name_specimen_gate.py` | raw/current file | exact source | public repo |
| A6 | local computation | six helper digests + one canonical Matthew packet digest | exact reproduced algorithms/fixtures | deterministic values | no external byte egress |
| A7 | IETF Datatracker | RATS Endorsements draft-09 | web read | primary standards draft | public |
| A8 | SLSA | provenance / verification docs | web read | primary project spec | public |
| A9 | OCI | Image Spec Content Descriptor | web read | standards text | public |

---

# Current mainline behavior

## 1. PR #82 adds a distinctness membrane

The family gate now keeps a list of observed packet digests and refuses if one appears twice:

```python
if packet_digest in packet_digests:
    return _gate_refuse("duplicate_packet_digest")
```

This correctly kills the exact hostile specimen preserved by `FORGED-FAMILY-REPLAY-001`.

The new regression test mutates all six packet-result receipts to share the first digest and confirms `REFUSE / duplicate_packet_digest`.

This is a useful contradiction detector and should remain even if a stronger provenance membrane is later added.

## 2. The ordinary six-READY test does not use upstream evaluator outputs

The current `packet_result(specimen_type)` test helper directly constructs result dictionaries. For READY specimens it creates a receipt with:

```python
"packet_digest": "sha256:" + specimen_type.lower().encode().hex()[:64].ljust(64, "0")
```

The six resulting strings are:

```text
LXX_JOSHUA
sha256:6c78785f6a6f7368756100000000000000000000000000000000000000000000

MATTHEW_1_21
sha256:6d6174746865775f315f32310000000000000000000000000000000000000000

JESUS_BARABBAS
sha256:6a657375735f6261726162626173000000000000000000000000000000000000

SCEVA
sha256:7363657661000000000000000000000000000000000000000000000000000000

PHILIPPIANS_2
sha256:7068696c69707069616e735f3200000000000000000000000000000000000000

NOMEN_SACRUM
sha256:6e6f6d656e5f73616372756d0000000000000000000000000000000000000000
```

All six satisfy the gate's SHA-256-shaped regex and all six are distinct.

The baseline test `test_six_ready_packets_make_dive_ready_without_authority()` passes this helper-built family to the gate and expects `DIVE_READY`.

Thus the previous packet's second hostile family is not merely predicted by static inspection; a semantically equivalent family already serves as the ordinary positive fixture.

## 3. Concrete digest comparison

The packet evaluator does not derive packet identity from the specimen name. It computes:

```python
packet_digest = sha256_json(record)
```

where `sha256_json()` hashes canonical JSON bytes of the entire packet mapping.

Using the exact `BASE_PACKET` fixture from `tests/test_name_specimen_gate.py`, the current algorithm yields:

```text
canonical upstream packet digest:
sha256:2ad239591688cac651895498c2972b07e8ff9aa73dbc955188f49141c95bc6f6
```

But the helper-built READY result for the same `MATTHEW_1_21` specimen claims:

```text
helper digest claim:
sha256:6d6174746865775f315f32310000000000000000000000000000000000000000
```

These are unequal.

This does **not** mean the positive family test is defective for unit-test purposes; synthetic results are common and useful. It means that the family gate's acceptance semantics currently cannot distinguish a lawful upstream-produced result from a sufficiently well-shaped synthetic one.

That is precisely the composition frontier under audit.

---

# Why the digest is currently not independently replayable from the receipt

A tempting repair would be: "the family gate should simply recompute `packet_digest` from the receipt."

The present schemas make that impossible without changing the contract.

The upstream digest hashes the **entire input packet record**. The READY receipt carries many packet fields, but it does not carry at least the packet's `producer`, and the packet evaluator currently permits additional non-forbidden fields that would also alter the canonical JSON digest.

Therefore:

```text
packet receipt
!=
complete hashed packet record
```

and in general:

```text
sha256_json(receipt-derived reconstruction)
!= guaranteed original packet_digest
```

This yields a second narrow law:

> **A DIGEST CLAIM THAT COMMITS MORE STATE THAN THE CONSUMER CAN RESOLVE IS NOT LOCALLY REPLAYABLE BY THAT CONSUMER.**

That does not make the digest useless. It means the consumer needs one of several explicit boundaries: access to the original packet, a resolvable content-addressed packet reference, an authenticated evaluator result, a sealed in-process result channel, or another owner-chosen mechanism.

---

# Claims ledger

| ID | Claim | Class | Supporting evidence path | Counterevidence | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #82 intentionally adds only packet-digest distinctness at the family gate. | observed / source testimony | A2 | none | supported |
| C2 | Current positive family fixtures use six distinct SHA-shaped digest strings constructed from specimen names. | observed | A5 + A6 | fixtures are synthetic by design | supported |
| C3 | Those six digest strings are accepted by the current family gate as part of a `DIVE_READY` positive fixture. | observed from test contract + source | A3 + A5 | not a checked-out repository execution in this run | strongly supported; current test declares expected behavior |
| C4 | For the current Matthew base packet, the helper digest is not equal to the canonical `sha256_json(BASE_PACKET)` digest. | deterministic computation | A4 + A5 + A6 | none under exact current fixture/algorithm | supported |
| C5 | Digest uniqueness establishes upstream packet provenance. | proposal | none | C2-C4 | disproved / overstrong |
| C6 | A downstream consumer needs either independently checkable content binding or an explicit trust boundary if it relies on a claimed digest as upstream provenance. | architectural inference | C2-C5 + A7-A9 | trusted same-process composition may supply the boundary without independent signatures | supported as design constraint, mechanism unresolved |
| C7 | The current receipt alone is sufficient to recompute the original packet digest. | proposal | none | packet digest covers full input; receipt omits producer and may omit arbitrary extra input fields | disproved under current open mapping contract |
| C8 | PR #82 is therefore "wrong" or should be reverted. | proposal | none | it correctly closes its stated repeated-digest contradiction and remains useful as a cheap guard | rejected |

---

# Counterevidence and nearest boring explanations

## 1. Synthetic fixtures are normal

The strongest boring explanation is simply that `packet_result()` is a convenient unit-test helper. Unit tests often construct downstream objects directly rather than exercising the full upstream pipeline.

That is true and materially weakens any claim of a security defect.

But it does not erase the architectural observation. The gate accepts plain mappings, and the positive test documents that a direct result-shaped mapping is valid input. If the intended contract is "only values emitted by `evaluate_name_specimen_packet()` may enter here," that invariant currently lives in caller discipline rather than the function or data model.

## 2. Local same-process trust may be enough

If the intended runtime always does:

```text
packet object
-> evaluate_name_specimen_packet(packet)
-> immediate in-memory result
-> evaluate_name_six_specimen_gate(results)
```

with no persistence, deserialization, user-controlled result construction, or cross-process boundary, then evaluator ancestry may be guaranteed by composition rather than cryptography.

In that world, adding signatures would be needless machinery.

The unresolved question is not "how do we cryptographically secure this?" It is:

> **WHAT EXACTLY IS THE ADMISSIBLE CALLING BOUNDARY?**

## 3. Closing the receipt schema would improve consistency but not authenticate origin

Requiring every READY receipt field and rejecting unknown fields would make result shape stronger. It still would not prove that the result came from the upstream evaluator.

A caller could synthesize every required field and six unique digests.

Thus:

```text
CLOSED SHAPE != EVALUATOR ANCESTRY
```

## 4. Digest distinctness remains valuable

The new duplicate-digest guard is not invalidated by this packet. It cheaply catches an impossible-or-suspicious relation under the current packet model and makes malformed family composition easier to refuse.

The relationship is:

```text
DISTINCTNESS = useful necessary consistency check
DISTINCTNESS != sufficient provenance check
```

---

# External pressure

## IETF RATS

The RATS architecture separates:

```text
Evidence -> Verifier -> Attestation Result -> Relying Party
```

and keeps Verifier appraisal policy distinct from Relying Party appraisal policy for Attestation Results.

The useful pressure here is structural: an upstream evaluator producing a result does not eliminate the downstream consumer's responsibility to decide what makes that result admissible for its own operation.

This is analogy, not a proposal that ALEX become a remote-attestation system.

## SLSA

SLSA verification treats provenance as more than a syntactically valid record. A verifier checks producer/platform trust and verifies that the statement's `subject` digest matches the actual artifact being evaluated.

The relevant pressure is:

```text
claimed digest
+
actual subject/content
+
verification
=> checkable binding
```

not merely:

```text
claimed digest is well-shaped and unique
=> binding
```

Again, the lesson is structural; local ALEX may satisfy its trust boundary in a much simpler way.

## OCI Content Descriptors

OCI's descriptor specification states the content-addressing relation particularly cleanly: a digest identifies content because the consumer can independently hash the targeted bytes and compare the computed digest to the descriptor's claimed digest. The spec explicitly recommends verifying retrieved content against the digest when content comes from untrusted sources.

That creates a precise contrast for ALEX:

```text
OCI-style content identifier:
claimed digest + targeted content + independent recomputation

current NAME family gate:
claimed digest + receipt semantics + syntax/distinctness checks
```

The second may be lawful under a trusted local composition boundary, but it is not independently content-verifying in the OCI sense.

Bridge type: **formal architecture analogy**, not shared mechanism or genealogy.

---

# Discovery trace

| ID | From | To | Move | Role | Reason |
| --- | --- | --- | --- | --- | --- |
| D1 | prior `FORGED-FAMILY-REPLAY-001` | current main | replay successor | motive | prior packet named unique-forgery as next discriminator |
| D2 | current main | PR #82 | recent-change inspection | evidence | PR landed after prior packet |
| D3 | PR #82 | bounded distinctness law | correction | evidence | avoid overclaiming intended scope |
| D4 | current tests | `packet_result()` helper | source read | evidence | ordinary positive fixture directly constructs six results |
| D5 | helper formula | six distinct digest strings | exact computation | evidence | confirms new duplicate guard is satisfied |
| D6 | `BASE_PACKET` + `sha256_json` | canonical Matthew digest | exact computation | evidence | tests actual upstream digest contract |
| D7 | helper digest vs canonical digest | distinct-but-unbound finding | comparison | inference | answers prior discriminator |
| D8 | RATS / SLSA / OCI | consumer verification boundary | formal analogy | pressure | test whether local survivor matches mature provenance patterns |

`DISCOVERY TRACE != EVIDENCE PATH` remains in force.

---

# What changed since the previous packet

## Previous hostile condition: one digest reused across six specimen types

**Closed on main.** PR #82 now refuses it with `duplicate_packet_digest`.

## Previous next discriminator: six unique forged digests

**Survives and is stronger than expected.** Current ordinary positive fixtures already use six distinct non-upstream-derived digest claims.

## Previous possibility: perhaps digest uniqueness would be enough for the proving slice

**Broken as a provenance claim.** It remains useful only as a consistency condition.

## New narrower survivor

> **UNIQUE IS A PROPERTY OF THE CLAIM SET. VERIFIED IS A RELATION BETWEEN THE CLAIM AND ITS SOURCE. DO NOT COLLAPSE THEM.**

A second equivalent form:

> **CONTENT ADDRESS WITHOUT RESOLVABLE CONTENT OR AN AUTHENTICATED PRODUCER BOUNDARY IS A CLAIMED ADDRESS, NOT A DOWNSTREAM-VERIFIED BINDING.**

---

# Residual fog

1. Is `evaluate_name_six_specimen_gate()` intended to accept deserialized/persisted packet results, or only trusted in-process outputs?
2. If results may persist or cross a process boundary, where is the original packet expected to live so `packet_digest` can be resolved and replayed?
3. Does ALEX already have a local content-addressed occurrence/store suitable for packet resolution without inventing a new subsystem?
4. If the gate is intended to be in-process only, should the contract state that explicitly and should tests include at least one composition test that generates all six results through `evaluate_name_specimen_packet()`?
5. Should result receipts carry evaluator/producer identity, or is that redundant under the intended local call boundary?
6. Because the input packet mapping is open to extra fields, what exactly is the stable public meaning of `packet_digest`: identity of the entire received mapping, or identity of a declared closed packet schema?
7. A fresh Front Room retrieval was unavailable in this run; no claim is made about any live-frontier wording change there.

---

# Smallest next discriminators / repo-worthy moves

1. **Add one end-to-end composition test without changing production code:** construct six lawful packet mappings, call `evaluate_name_specimen_packet()` on each, pass only those returned results into `evaluate_name_six_specimen_gate()`, and assert `DIVE_READY`. This freezes the intended happy-path ancestry and reveals whether the current fixture helper is merely convenience or the de facto public result contract.
2. **Choose and write down the trust boundary before adding mechanism:** one sentence is enough — e.g. "family-gate packet results are trusted same-process evaluator outputs" or "family-gate packet results may be persisted/deserialized and therefore must be independently replayable/authenticated." These imply very different minimal designs.
3. **If persisted/deserialized results are in scope, test one resolvability failure before designing signatures:** give the gate a valid unique digest whose corresponding packet cannot be resolved/replayed. Expected behavior should be explicitly decided (`REFUSE`, `BLOCKED`, or trusted-by-contract). That test will reveal whether ALEX needs packet storage/replay, evaluator identity, or neither.

---

# Receipt

- **Created:** 2026-09-01
- **Researcher or agent:** ChatGPT / ALEXDEEPDIVE
- **Tool and model boundary:** GitBook orientation attempt; GitHub repository/PR/file reads and durable write; local deterministic SHA-256/JSON computation reproducing current repo algorithm; public web reads of IETF/SLSA/OCI primary technical sources. No external model received local page bytes or private corpus material.
- **External byte egress:** Public repository text and public standards only; no private source corpus.
- **Durable location:** `research/ALEX-DEEPDIVE-2026-09-01-0524-DISTINCT-FORGERY.md`
- **Promotion:** none

---

## Seal

> **PR #82 CLOSED THE REPEATED-DIGEST CONTRADICTION IT WAS DESIGNED TO CLOSE.**
>
> **THE NEXT LAYER IS NOT MORE UNIQUENESS. IT IS BINDING.**
>
> **UNIQUE DIGEST CLAIM != VERIFIED CONTENT RELATION.**
