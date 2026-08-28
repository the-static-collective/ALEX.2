# LOADOUT × LOADINSTEAD — Dual-Hand Door Router m0

**Date:** 2026-08-28  
**Status:** approved architecture / first executable slice  
**Incubating owner:** `the-static-collective/ALEX.2`  
**Reason for incubation:** the executable ALEX × LOADOUT handshake already lives here; a dedicated LOADOUT repository is not currently present. This placement does not transfer semantic ownership to ALEX.

> **LOADOUT prepares the room. LOADINSTEAD finds the room.**

Compact pair:

```text
LOADOUT
world/run <- selected context + capability

LOADINSTEAD
new occurrence -> selected destination/world
```

The pair is intentionally asymmetric and complementary:

```text
LEFT HAND / IN                         RIGHT HAND / OUT

available world                       new eCODE bit
      |                                     |
      v                                     v
   LOADOUT                              LOADINSTEAD
      |                                     |
      v                                     v
 bounded run                         bounded route proposal
```

Neither hand admits consequence.

---

## 1. Why this exists

The current ALEX × LOADOUT boundary gives LOADOUT a clear inward responsibility: freeze a mortal task world, compile context, bind available capabilities, carry attributable effect fences, and hand a bounded run envelope to ALEX.

The missing dual operation is outward.

A run can produce a new eCODE-shaped occurrence that clearly belongs somewhere else:

- repository-shaped work belongs behind a FORGE door;
- research-accounting material may belong behind an ALEX door;
- relationship-crossing material may belong behind a STORYSHIP door;
- later domains may expose their own doors without teaching eCODE every project topology.

Without an explicit outward router, three bad patterns become tempting:

1. eCODE becomes a universal project router and silently learns every world;
2. the producing runtime writes directly into destination worlds and bypasses their gates;
3. ambiguous material is silently filed into whichever repository or subsystem is easiest to reach.

LOADINSTEAD exists to prevent those collapses.

---

## 2. Founding laws

The existing LOADOUT law remains:

> **Knowledge may load. Capability may bind. Authority does not silently expand.**

LOADINSTEAD adds the dual law:

> **A route may be proposed. A destination may be addressed. Authority does not travel merely because the bit traveled.**

Hard distinctions:

```text
LOADOUT != LOADINSTEAD
LOADINSTEAD != destination gate
route != admit
route != execute
route != publish
route != merge
route != canon
available door != owning door
similarity != jurisdiction
misroute != lost bit
unroutable != refused by destination
ambiguous != permission to pick silently
transport success != admission
```

The owning world remains sovereign over consequence.

---

## 3. Jurisdictions

### 3.1 LOADOUT owns inward mortal compilation

LOADOUT answers:

> **What should this run be able to see and attempt?**

It compiles context and capability into a bounded session.

### 3.2 LOADINSTEAD owns outward destination resolution

LOADINSTEAD answers:

> **Given this new typed occurrence, which declared door owns the next attempted crossing?**

It may:

- validate a bounded eCODE route bit;
- inspect a bounded declared door registry;
- find doors whose declared jurisdiction matches the bit's typed consequence class;
- distinguish destination doors from witness doors;
- return `ROUTED`, `AMBIGUOUS`, or `UNROUTABLE`;
- produce a deterministic route receipt;
- preserve unavailable and rejected candidates with reason codes;
- prepare delivery envelopes for an external transport layer.

It does **not**:

- infer historical truth;
- reinterpret the payload to force a route;
- invent a consequence class that was not supplied;
- choose arbitrarily among multiple owning doors;
- call a destination's admission decision successful;
- expand effect authority;
- mutate the destination;
- become a durable semantic store.

Constitutional profile:

```text
authority minted: none
promotion: none
durability: route receipt
side effects in m0: none
```

### 3.3 Destination doors own admission

A destination door identifies an owning world and a transport/protocol boundary. It does not imply that every delivered bit is accepted.

The destination may:

- accept;
- refuse;
- hold unresolved;
- transform into a local proposal;
- request more provenance;
- require human or project authority.

Those are downstream events and receive downstream receipts.

---

## 4. FORGE is a door family, not the router

FORGE remains a provider-neutral repository-work boundary.

```text
LOADINSTEAD
   |
   | consequence_class = repository_work
   v
FORGE DOOR FAMILY
   |
   +-- forge/github
   +-- forge/gitlab
   +-- forge/forgejo
   +-- forge/gitea
   +-- forge/local-git
```

LOADINSTEAD determines that the next crossing is repository-shaped.

FORGE determines how repository-shaped work is represented and transported across a repository boundary.

The selected forge/provider still does not own project admission merely because transport succeeded.

```text
LOADINSTEAD != FORGE
FORGE != GitHub
GitHub write != project canon
PR opened != merge admitted
```

---

## 5. m0 refuses semantic guessing

The first executable router does not use embeddings, LLM classification, keyword scoring, or opaque heuristics.

The bit arrives with a typed `consequence_class`.

The door registry declares which consequence classes each door owns or witnesses.

Routing is therefore a transparent set-membership decision.

This is intentionally boring.

If the ecosystem later needs a classifier that proposes a `consequence_class`, that classifier is a separate upstream event whose proposal and uncertainty must remain attributable. LOADINSTEAD consumes the typed result; it does not hide classification inside routing.

---

## 6. eCODE route bit

m0 accepts exactly this logical shape:

```yaml
schema: ecode.route-bit/v0
bit_id: bit-...
occurred_at: 2026-08-28T19:00:00Z
source_world: some-world
consequence_class: repository_work
payload_ref: receipt://...
formation_ref: ecode://history/...
compile_ref:
  compile_id: loadout-...
  compile_digest: sha256:...
witness_classes:
  - research_accounting
```

Fields:

- `bit_id` — stable local identity supplied by the producer;
- `occurred_at` — offset-aware occurrence timestamp;
- `source_world` — world that produced the bit;
- `consequence_class` — typed next-consequence class; routing does not infer it;
- `payload_ref` — resolvable reference to the carried material rather than an ambient object dump;
- `formation_ref` — attributable eCODE/history reference explaining how the bit became reachable;
- `compile_ref` — LOADOUT compile identity under which the bit was produced, when applicable;
- `witness_classes` — optional additional classes that may receive observation-only copies.

A bit is not admitted evidence merely because it conforms to this shape.

---

## 7. Declared door contract

m0 doors use:

```yaml
schema: loadinstead.door/v0
door_id: forge
owner_world: FORGE
role: destination
accepts_classes:
  - repository_work
protocol: forge.work-envelope/v0
capability_ref: capability://forge
status: available
```

Witness example:

```yaml
schema: loadinstead.door/v0
door_id: alex-witness
owner_world: ALEX
role: witness
accepts_classes:
  - research_accounting
protocol: alex.route-witness/v0
capability_ref: capability://alex
status: available
```

Required fields:

```text
schema
door_id
owner_world
role
accepts_classes[]
protocol
capability_ref
status
```

Enums:

```text
role   = destination | witness
status = available | unavailable
```

Door declarations are registry testimony. They do not prove that the owner will admit a delivered bit.

---

## 8. Deterministic routing algorithm

For bit `B` and registry `D`:

### 8.1 Destination candidates

A door is a destination candidate iff:

```text
door.role == destination
AND door.status == available
AND B.consequence_class in door.accepts_classes
```

Then:

```text
0 candidates -> UNROUTABLE
1 candidate  -> ROUTED
>1 candidates -> AMBIGUOUS
```

No tie-breaker exists in m0.

Ambiguity is a truthful state.

### 8.2 Witness candidates

A witness door is selected iff:

```text
door.role == witness
AND door.status == available
AND intersection(B.witness_classes, door.accepts_classes) is non-empty
```

Witness selection does not affect primary destination resolution.

### 8.3 Unavailable matches

A matching but unavailable door is retained in the route trace with reason `DOOR_UNAVAILABLE`.

It does not become a candidate merely because it would otherwise own the class.

---

## 9. Route proposal / receipt

m0 returns one deterministic object:

```yaml
schema: loadinstead.route-proposal/v0
profile: loadout.runtime/loadinstead-door-router-m0
route_id: sha256:...
bit_id: bit-...
bit_digest: sha256:...
compile_ref:
  compile_id: loadout-...
  compile_digest: sha256:...
disposition: ROUTED
primary_door_ref: forge
candidate_door_refs:
  - forge
witness_door_refs:
  - alex-witness
rejections: []
delivery_envelopes:
  - door_id: forge
    owner_world: FORGE
    protocol: forge.work-envelope/v0
    payload_ref: receipt://...
    formation_ref: ecode://history/...
    authority: none
admission_status: NOT_ATTEMPTED
authority_transferred: false
```

`route_id` is the repository-local canonical SHA-256 digest of the route payload excluding `route_id` itself.

The route object is both proposal and receipt of the deterministic routing decision.

It is **not** a destination receipt.

---

## 10. Delivery envelopes

m0 prepares, but does not send, delivery envelopes.

A delivery envelope contains only what the selected door needs to attempt the next crossing:

```text
door_id
owner_world
protocol
payload_ref
formation_ref
bit_id
route_id
authority = none
```

The transport layer may later deliver this envelope through MCP, local IPC, HTTP, Git, file drop, queue, or another adapter.

Transport choice is not jurisdiction.

Transport success is not admission.

---

## 11. LOADOUT / LOADINSTEAD symmetry

The hands compose without becoming one state machine.

```text
ambient world
    |
    v
 LOADOUT
    |
    | compile_id + compile_digest
    v
 bounded run
    |
    | produces typed eCODE bit
    v
 LOADINSTEAD
    |
    | route_id + delivery envelope
    v
 destination door
    |
    | local gate decision
    v
 admitted / refused / unresolved consequence
```

Every important transition can therefore retain a distinct receipt:

```text
compile receipt
run receipt
eCODE formation receipt
route receipt
transport receipt
destination admission receipt
```

No receipt impersonates the next one.

---

## 12. Incubation boundary inside ALEX.2

The executable m0 package lives beside, not inside, the ALEX research kernel:

```text
loadout_runtime/
  __init__.py
  loadinstead.py

alex_runtime/
  ... unchanged research kernel ...
```

The package may temporarily reuse the repository-local canonical JSON digest helper. This is an incubation convenience, not a claim that ALEX owns LOADINSTEAD.

A future dedicated LOADOUT repository may lift `loadout_runtime/` with its tests and contract unchanged.

No ALEX evidence or derivation code imports LOADINSTEAD in m0.

---

## 13. First fixture doors

Tests may use the following registry as fixtures only:

```text
FORGE
  role: destination
  owns: repository_work

ALEX
  role: destination or witness depending on fixture
  owns/witnesses: research_accounting

STORYSHIP
  role: destination
  owns: relationship_crossing
```

These fixtures demonstrate the contract. They are not a universal registry or canon of every Static Collective project.

---

## 14. Failure requirements

The router must preserve these outcomes explicitly:

### Invalid bit

Return validation errors; do not fabricate a route.

### Invalid door

Reject the registry entry; do not silently repair it.

### No owning door

`UNROUTABLE` with no primary door and no delivery envelope.

### Multiple owning doors

`AMBIGUOUS` with all candidates named and no primary door.

### Owning door unavailable

If no other available owner matches, `UNROUTABLE`; preserve the unavailable match in rejections.

### Witness unavailable

Primary routing may still succeed. Preserve witness unavailability as residue.

### Misclassification upstream

LOADINSTEAD does not rewrite the bit. A later correction produces a descendant bit and a new route receipt.

---

## 15. m0 executable claims

The first implementation may claim only:

1. valid route bits and door declarations are strictly validated;
2. routing is deterministic under a fixed bit and registry;
3. exactly one available owning door yields `ROUTED`;
4. zero yields `UNROUTABLE`;
5. multiple available owning doors yields `AMBIGUOUS`;
6. witness routing is independent from destination routing;
7. every delivery envelope carries `authority: none`;
8. every route reports `admission_status: NOT_ATTEMPTED`;
9. changing source formation, consequence class, door registry, or compile reference changes the receipted route identity;
10. ALEX runtime behavior remains unchanged.

It may **not** claim that eCODE classification is solved, that a destination accepted the bit, or that cross-project delivery has been implemented.

---

## 16. Promotion path

A later slice may add a transport dispatcher only after this pure router is stable.

Recommended sequence:

```text
M0 pure routing
  -> M1 destination proposal ports
  -> M2 transport receipts
  -> M3 destination admission receipts
  -> optional upstream consequence classifier
```

Do not collapse these gates to make the demo feel complete.

---

## 17. Working seal

> **LOADOUT asks what comes through this door with me.**
>
> **LOADINSTEAD asks which door this belongs at.**
>
> **The router may address the door. Only the room may admit the consequence.**
>
> **Left hand in. Right hand out. Keep the receipts between them.**
