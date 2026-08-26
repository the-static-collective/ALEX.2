# ALEX.² Daily Slice 002 — The Seed Is Not the Key

**Date:** 2026-08-26  
**Status:** research slice / pressure test / no promotion  
**Origin:** Narrative Roam from the Front Room live frontier → Seedbank / Reconstitutive Viability  
**Authority:** none; this slice challenges and sharpens an incubating primitive. It does not amend Seedbank/ELF, Storyship, Corpus OS, Human-Witness, ALEX, or any project-owned law.

> **A seed and a key can both cross a boundary. One preserves the power to become. The other may preserve the power to act. Do not confuse them.**

## 1. The thing that looked like a law

The current Seedbank frontier contains a strong candidate formulation:

> A carrier may preserve reconstitutive viability across a boundary while authority, admission, and consequence remain local to the receiving world.

Its cleanest local equation is:

```text
viability(seed, environment, target)
```

rather than:

```text
seed.viable = true
```

That is already an important correction. Reconstitution is relational: what can become live again depends on what crossed, the receiving environment, and the target being reconstructed.

But the stronger line nearby—roughly, **zero authority survives transit**—needed an adversarial control.

The control exists.

It is the capability.

---

## 2. ATTACK — some carriers are intentionally authority-bearing

Capability-based security gives a direct counterexample to any universal claim that authority must always be locally reconstituted.

In capability systems, possession of an unforgeable capability may itself be sufficient to exercise a specified authority. Foley & Navarro-Arribas (2013) describe software capabilities in exactly this possession-entitles-action shape; their decentralized authorization model allows a held permission to be delegated, and verification can determine authorization from possession of the permission rather than from a separately reconstructed local identity/ACL grant.

Older capability work is even more explicit: capability environments were designed around distributing and revoking **access authorizations** on objects (Corsini, Frosini & Lopriore, 1984).

So this statement is too strong as a universal descriptive law:

```text
authority never crosses
```

A capability token is precisely a design in which an authority-bearing relation is packaged so that it can cross.

That does **not** break the Seedbank idea.

It tells us what kind of idea it is.

> **“Authority remains local” is a constitutional transport rule, not a universal property of carriers.**

That distinction is worth keeping.

### Sources

- Foley, S. N. & Navarro-Arribas, G. (2013), *A Bloom Filter Based Model for Decentralized Authorization*, DOI: https://doi.org/10.1002/int.21593
- Corsini, P., Frosini, G. & Lopriore, L. (1984), *Distributing and revoking access authorizations on abstract objects: A capability approach*, DOI: https://doi.org/10.1002/spe.4380141004
- Miller, M. S., Shapiro, J. S. & Yee, K.-P. (2003), *Capability Myths Demolished*: https://cgi.cse.unsw.edu.au/~cs9242/papers/Miller_YS_03.pdf

---

## 3. A cleaner separation: viability and authority are orthogonal

The pressure test suggests a two-axis model rather than one inheritance rule.

A carrier can vary independently in:

1. **reconstitutive content** — how much attributable material it carries that can help rebuild a target in a suitable environment;
2. **authority-bearing content** — how much recognized permission/control relation the receiving system accepts directly from possession or verification of the carrier.

Provisional matrix:

| | Low transported authority | High transported authority |
| --- | --- | --- |
| **Low reconstitutive content** | inert scrap / witness fragment | key, bearer token, narrow capability |
| **High reconstitutive content** | seed, source bundle, recipe, reproducible build description | deployable authority-bearing package / dangerous combined carrier |

The quadrants are not metaphysical categories. They are a design lens.

The important point is that the axes do not collapse.

A tiny bearer token may carry enormous authority and almost no reconstructive description.

A large source archive may carry enormous reconstructive potential and no permission whatsoever.

That is the difference between **seed** and **key**.

---

## 4. External control — reproducibility already looks seed-like

Software reproducibility provides a much cleaner external analogue for the Seedbank side of the matrix.

Kowalewski & Seeber (2022) show how Nix build recipes and isolated dependency descriptions allow software to be reconstructed later and transferred across machines. Their emphasis is not authority transfer. It is preservation of enough environmental and dependency structure to rebuild a computational result.

SLSA provenance uses nearly the same split in modern supply-chain language: provenance describes where, when, and how an artifact was produced so consumers can verify it against expectations and, where possible, rebuild it. The provenance is evidence for a verifier; it is not itself the verifier's policy decision.

in-toto makes the separation operational. Link metadata records commands, materials, products, and signed step evidence. The project owner's layout separately names authorized functionaries and rules. At verification time the evidence is checked against the owner-defined layout.

So three layers can be kept distinct:

```text
ARTIFACT / RECIPE / PROVENANCE
what can be reconstructed or inspected

EVIDENCE / ATTESTATION
what can be verified about formation

POLICY / AUTHORITY
what the receiving world accepts, permits, or grants
```

This is not identical to eCODE, but it is a materially independent precedent for refusing to let provenance silently become permission.

### Sources

- Kowalewski, M. & Seeber, P. (2022), *Sustainable packaging of quantum chemistry software with the Nix package manager*, DOI: https://doi.org/10.1002/qua.26872
- SLSA v1.2, provenance / verification model: https://slsa.dev/spec/v1.2/
- in-toto, Getting Started / layout and link verification: https://in-toto.io/docs/getting-started/
- in-toto overview: https://in-toto.io/docs/what-is-in-toto/

---

## 5. The stronger candidate primitive

The original formulation can now be sharpened without pretending the counterexample does not exist.

### H0 — weaker / vulnerable

```text
a carrier preserves viability;
authority stays local
```

### H1 — stronger / testable

```text
reconstitutive potential and authority are independently transportable dimensions
```

A receiving architecture may therefore impose a constitutional rule:

```text
TRANSPORT(reconstitutive_material) = allowed
TRANSPORT(authority) = stripped / refused / re-bound locally
```

That is a choice about the membrane.

It is not a claim that carriers are naturally incapable of carrying authority.

This makes the local gate more important, not less. The gate is not merely discovering a natural absence of authority. It is actively enforcing a transport discipline:

> **Whatever the source believed it could do there does not become permission to do it here merely because the source arrived intact.**

That is closer to a constitution than a conservation law.

---

## 6. The four carrier question

Every crossing specimen may benefit from asking four independent questions:

```text
1. WHAT INFORMATION CROSSED?
2. WHAT CAN BE RECONSTITUTED FROM IT HERE?
3. WHAT AUTHORITY, IF ANY, DOES THE CARRIER PURPORT TO BEAR?
4. WHAT AUTHORITY DOES THIS RECEIVING WORLD ACTUALLY RECOGNIZE?
```

Questions 3 and 4 are intentionally separate.

A forged `authority: granted` declaration answers #3 and should not answer #4.

A real bearer capability in a capability system may answer both #3 and #4—because that receiving system is intentionally constituted to recognize possession as authority.

A Seedbank/ELF architecture can choose not to.

That makes `A5 + forged authority` in VIABILITY-WITHOUT-AUTHORITY-001 more than a tamper test. It becomes a discriminator between **carrier semantics** and **receiving-world constitution**.

---

## 7. New crucible candidate — SEED-KEY-SEPARATION-001

Use four tiny carriers against two fresh receiving runtimes.

```text
S0  recipe + tests + provenance; no credential
K0  valid narrow capability; almost no reconstructive material
SK  S0 + valid narrow capability
FK  S0 + forged claim "authority: granted"
```

Measure independently:

```text
reconstruction_success
formation_verification
claimed_authority
recognized_authority
executed_effect
```

Expected discriminators:

- `S0` may reconstruct capability while receiving zero authority.
- `K0` may carry authority while reconstructing almost nothing.
- `SK` demonstrates that the two dimensions can coexist.
- `FK` must not acquire recognized authority merely by assertion.

Then repeat under two materially different receiving constitutions:

1. a local-gate world where imported authority is always stripped and rebound;
2. a capability-recognizing world where possession of a valid capability is intentionally authoritative.

If the same carrier produces different recognized authority under those two worlds, that is evidence that **authority is relational to receiving constitution**, just as viability is relational to environment and target.

---

## 8. What changed

Before the roam, the interesting thought was:

> preserve power-to-become without power-over.

After the attack, the better thought is:

> **Power-to-become and power-over are separate cargo dimensions. The Static Collective's interesting move is not discovering that authority cannot travel. It is designing membranes where authority does not silently survive travel.**

That is a much harder and more defensible claim.

It also explains why provenance matters so much. Formation history can increase reconstitutive confidence without increasing authority.

```text
more evidence
    !=
more permission
```

And it explains the dangerous opposite:

```text
less information
    !=
less authority
```

A key can be tiny.

---

## 9. Residual fog

Still unresolved:

- Is **recognized authority** best modeled as `authority(carrier, receiver, policy, time)` rather than a property of either carrier or destination alone?
- Should an Ark be constitutionally prohibited from carrying bearer capabilities, or may it carry them as inert evidence that must be cryptographically neutered / rewrapped before admission?
- Can a carrier preserve an authority *lineage* without preserving exercisable authority? That may be the exact bridge needed by Human-Witness and legal/trust work.
- Does “re-bind locally” preserve continuity of delegation, or does it necessarily create a new authority event with ancestry to the old one?
- Which failure cases distinguish legitimate delegation from smuggled ambient authority?

No promotion is earned yet.

The immediate useful correction is smaller:

> **SEED ≠ KEY.**
>
> **Viability and authority can both travel. Treat their transport as separate decisions.**

⟦ SEED-KEY-SEPARATION · RECONSTITUTION:RELATIONAL · AUTHORITY:RELATIONAL · SILENT-INHERITANCE:REFUSED · CRUCIBLE:OPEN ⟧
