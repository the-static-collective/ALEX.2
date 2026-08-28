# GOODENOUGHFORNOW-001 — THE ROAD DOES NOT CHOOSE THE DOOR

**Status:** GOOD ENOUGH FOR NOW / motivating architecture note  
**Owner:** LOADOUT / LOADIN.STEAD boundary documentation  
**Runtime effect:** none  
**Schema effect:** none  
**Authority effect:** none

## Why this note exists

Recent PASSAGE-WORLD, 3rdi, ALEX, UNDERSTORY, and Storyship work makes one routing boundary easier to state:

> **LOADIN.STEAD receives rich ancestry opaquely. It preserves the road by reference and chooses the next door from declared routing jurisdiction.**

Upstream owners may produce meaning-bearing receipts describing constitution, projection, contact, attention, decoder or probe history, access ancestry, derivation, formation, or later `BECAME` interpretations. A new occurrence may carry references to those receipts.

LOADIN.STEAD must not become the interpreter of that history.

```text
UPSTREAM OWNERS
produce meaning-bearing receipts
        ↓
NEW OCCURRENCE
carries opaque references
        ↓
LOADIN.STEAD
does not interpret them
does not recompute them
does not rank their truth
does not decide whether they matter
        ↓
DECLARED ROUTING TOPOLOGY
        ↓
ROUTE PROPOSAL
        ↓
OWNER GATE
```

The router may preserve references such as:

```text
compile_ref
formation_ref
payload_ref
observer / projection refs
decoder / probe refs
access-history refs
Storyship BECAME refs
...
```

but the presence of a reference does not grant LOADIN.STEAD semantic ownership of the thing referenced.

## Core law

> **THE ROAD DOES NOT CHOOSE THE DOOR.**

The road explains how the occurrence became attributable.

LOADIN.STEAD answers a different question:

> **Given this already-formed occurrence, which declared destination owns the next proposal?**

Therefore:

```text
route != formation
route != meaning
route != support
route != truth
route != admission
route != consequence
route != authority
```

The complementary PASSAGE / LOADIN.STEAD split is:

```text
PASSAGE
preserves how attributable crossing ancestry differed

LOADIN.STEAD
preserves where the resulting occurrence may be offered next

NEITHER
gets to become the city
```

## Formation ancestry and routing topology are separately owned coordinates

Use the following orthogonality as an architectural separation, not as a claim of statistical independence in every empirical system:

```text
FORMATION ANCESTRY  ⟂  ROUTING TOPOLOGY
```

Two important controls follow.

### Control A — different formation, same route

```text
ROAD A ── formation A ──┐
                        ├── LOADIN.STEAD ──> door:R1
ROAD B ── formation B ──┘

formation A != formation B
route(A) = route(B)
```

This is lawful.

Therefore:

> **SAME ROUTE != SAME PASSAGE.**

LOADIN.STEAD must preserve the exact formation reference carried by each occurrence without interpreting why those formations differ.

### Control B — same formation, changed route topology

```text
same formed occurrence
+ registry / door topology T0
→ route proposal R0

same formed occurrence
+ registry / door topology T1
→ route proposal R1
```

This is also lawful.

Therefore:

> **DIFFERENT ROUTE != CHANGED FORMATION.**

A routing-topology change must not rewrite upstream formation ancestry.

## PASSAGE refinement — formation basis, not surface difference

PASSAGE-WORLD exists to preserve lawful interior differences even when the outside looks the same.

Do not interpret “formation-bearing” as requiring a changed final visible state.

A safer neutral model is:

```text
interior event
    ↓
owner issues attributable receipt
    ↓
receipt becomes part of lawful formation basis
    ↓
passage ancestry may differ
```

Let:

```text
B(P) = owner-issued formation-bearing receipt basis for passage P
```

PASSAGE may compare attributable bases such as `B(P0)` and `B(P1)`.

PASSAGE does not decide what deserves membership in `B(P)`. Owning systems do.

Hence:

```text
DIFFERENT FORMATION BASIS
does not require
DIFFERENT FINAL PROJECTION
```

But the opposite counterfeit must also be refused:

```text
DIFFERENT TELEMETRY
!=
DIFFERENT PASSAGE
```

A timestamp, UUID, serialization order, wrapper identity, passive logging event, or other incidental telemetry cannot manufacture passage distinction merely because it is different.

## The long ladder — no arrow is automatic

The current research pile suggests a useful boring checklist:

```text
REACHABLE
  ↓
ENCOUNTERED
  ↓
ATTENDED
  ↓
DECODED
  ↓
ACTIVATED
  ↓
USED
  ↓
FORMATION-BEARING
  ↓
CONSEQUENCE PROPOSED
  ↓
ROUTED
  ↓
ADMITTED
  ↓
WORLD MUTATED
```

**No arrow is automatic.**

Important non-collapses:

```text
reachable != encountered
encountered != attended
attended != decoded
decoded != activated
activated != used
used != formation-bearing
formation-bearing != consequence proposed
consequence proposed != routed
routed != admitted
admitted != world mutated
```

Two additional boundaries are especially useful:

```text
USED != CONSEQUENTIAL
```

An actor may inspect or use something without that use changing the descendant formation.

And:

```text
CONSEQUENTIAL != MUTATED WORLD
```

An event may change local formation without granting authority to mutate external topology.

## Why rich ancestry stays opaque here

LOADIN.STEAD should not ask:

```text
is the claim true?
is it supported?
was a decoder passive or an active probe?
did interest mediate formation?
was access historically available?
was the passage distinct?
did Storyship BECAME differ?
should the destination accept it?
should the world mutate?
```

Those are owner-local questions.

LOADIN.STEAD may ask only the routing questions admitted by its declared contract, such as whether the typed route bit is valid and which available declared door owns the relevant consequence class.

Rich ancestry is carried so that downstream owners can peel it if they have the capability and authority to do so. The router itself does not peel it.

## Parked frontiers — preserve, do not architect here

The following remain useful pressure material but are deliberately **not** promoted into LOADIN.STEAD semantics by this note:

### DECODER-PROBE-001

Candidate distinction:

```text
passive decoder != world-changing probe
```

3rdi may witness the application; ALEX / Projection Break may pressure whether the event became intervention-bearing. LOADIN.STEAD only preserves resulting references.

### MEDIATED-FORMATION-001

Candidate chain:

```text
interest
→ attributable consumption
→ changed context
→ changed evidence
→ changed derivation
→ formation MAY differ
```

Never:

```text
interest ───────────────→ formation
```

without attributable intermediate receipts.

### ACCESS-ANCESTRY-001

Candidate UNDERSTORY ladder:

```text
reachable
!= encountered
!= attended
!= decoded
!= activated
!= used
```

Later activation must not rewrite earlier cuts.

### PASSAGE-RECTANGLE-001

Candidate neutral 2×2 hostile proof for interactions that pairwise comparisons can miss:

```text
                  selection S0      selection S1
hidden H0              P00               P01
hidden H1              P10               P11
```

The neutral proof should consume owner receipts without learning what `H` or `S` mean.

### STORYSHIP-TRIVARIANT-001

Storyship may use PASSAGE receipts as hostile pressure on its `BECAME` coordinate. Storyship remains a sibling / downstream consumer, not a routing owner.

### PASSAGE-MUTATION-001

Keep last.

```text
passage difference != topology mutation
```

A future topology change requires an explicit owning-world mutation proposal, authority check, admission, and mutation receipt. PASSAGE may witness the before / mutation / after chain but cannot manufacture mutation authority.

## Reopen condition

Do not promote any parked distinction merely because it is interesting.

Reopen this architecture only when a concrete executable owner cannot express a required behavior or hostile control without making one of these distinctions first-class.

Until then:

> **IMPORTANT ENOUGH TO RETAIN != MATURE ENOUGH TO ARCHITECT.**

Preserve the receipt. Keep the router dumb. Keep building.

## Seal

> **LOADIN.STEAD PRESERVES THE ROAD BY REFERENCE. THE ROAD DOES NOT CHOOSE THE DOOR.**
