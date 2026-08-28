# UNGATE — decoder-ring archaeology

Use this protocol when a surviving carrier is surrounded by later encoding,
transmission, editorial, interpretive, or institutional layers that may have
changed which readings are reachable without replacing the underlying carrier.

UNGATE is not a license to privilege older readings, strip tradition for sport,
or treat ambiguity as evidence. It is a controlled way to ask what a layer did.

## Constitutional distinctions

```text
nucleus != ring
constraint != hostility
older != truer
unpointed != unconstrained
reopened != attested
possible != intended
closed != true
ungate != interpret
```

A later layer may preserve genuinely old information. Removing it temporarily
for analysis does not demote it historically or theologically.

Core law:

> **UNGATE WITHOUT AMNESIA.**
>
> Remove a gate long enough to learn what it constrained. Preserve the gate,
> its date, producer, purpose, ancestry, and effect. Then put it back and test
> what changes.

## 1. Establish the nucleus

Identify the smallest attributable carrier relevant to the question.

Examples include:

- consonantal text before a later vocalization system;
- manuscript reading before editorial normalization;
- source-language phrase before translation;
- inscription before supplied restoration;
- historical event before later narrative framing;
- raw measurement before model-dependent correction.

Do not assume the oldest surviving carrier is an unmediated origin.

Record:

```text
NUCLEUS
  carrier:
  date_or_range:
  provenance:
  already_present_constraints:
  unresolved_fog:
```

## 2. Build the ring ledger

A `ring` is an attributable layer that changes how the nucleus is read,
segmented, pronounced, grouped, projected, authorized, or made reachable.

Candidate ring types include:

- vocalization;
- punctuation or segmentation;
- cantillation / prosody;
- orthographic normalization;
- translation;
- textual correction or emendation;
- commentary;
- doctrinal or institutional convention;
- genre or propaganda frame;
- catalog or editorial metadata;
- mathematical / computational model;
- visualization or projection;
- modern default-reading convention.

For each ring preserve:

```text
RING
  id:
  layer_type:
  producer_or_tradition:
  date_or_range:
  carrier:
  operation:
  declared_purpose:
  inferred_purpose:
  ancestry:
  dependency_family:
  provenance_visibility:
  invertibility:
  alternatives_preserved:
  alternatives_suppressed:
  hostility_status:
```

Use `hostility_status: unknown` unless evidence warrants more.

## 3. Model reachability

Let `Omega_before` denote readings, projections, or actions that remain lawful
before the tested ring and `Omega_after` those that remain lawful after it.

The useful object is the delta:

```text
DELTA_OMEGA
  newly_required:
  newly_preferred:
  newly_impossible:
  newly_invisible:
  newly_reachable:
```

A constraining ring may produce:

```text
Omega_after subset_of Omega_before
```

but subset relations alone do not establish hostility. A good correction,
measurement model, or pronunciation tradition may intentionally reduce
ambiguity.

## 4. UNGATE exactly one layer

Temporarily suspend one ring while preserving it beside the nucleus.

```text
SURFACE
  -> identify R_n
  -> suspend R_n
  -> reconstruct candidate pre-ring reachability
```

Ask:

> **What becomes reachable again if this one attributable constraint is not
> allowed to decide the reading?**

Do not simultaneously remove multiple layers unless their dependency makes
single-ring removal impossible. If multiple rings are removed, preserve their
order and justify the bundle.

UNGATE output is candidate possibility-space, not historical truth.

## 5. Apply the historical filter

Every reopened reading must then face its own historical cut.

For each candidate ask:

- Was the lexeme, pronunciation, grammar, model, or convention available then?
- Is there a witness showing the candidate was actually used?
- Does genre permit it?
- Does independent contextual evidence support or contradict it?
- Did the ring preserve information older than its written form?

Classify reopened candidates as:

```text
ATTESTED
HISTORICALLY AVAILABLE
FORMALLY POSSIBLE ONLY
ANACHRONISTIC
DISPROVED
UNRESOLVED
```

Never promote `FORMALLY POSSIBLE ONLY` into original meaning.

## 6. SLEEP the surviving readings

If more than one candidate remains materially live, use formation-trace SLEEP.
Hold one to three formulations with explicit discriminators.

```text
SUSPEND {
  H1
  H2
  H3
}
```

The purpose is bounded plurality, not permanent ambiguity.

## 7. Hostile triangulation

When materially independent encoders describe an overlapping nucleus, compare
them after accounting for each encoder's genre, incentives, and dependency.

```text
WORLD_OR_EVENT
  -> encoder A
  -> encoder B
  -> encoder C
```

Examples may include rival royal inscriptions, administrative records,
archaeological residue, later narrative traditions, or independent measurement
families.

Ask:

> **What remains difficult to remove after mutually different or hostile
> encoding systems are peeled according to their own constitutions?**

Agreement is not automatically independent corroboration. Preserve known shared
ancestry. Hostility or rivalry can improve independence pressure but does not
make testimony automatically true.

## 8. REGATE

Reapply the documented ring to the reconstructed pre-ring state.

```text
REGATE(UNGATE(surface, R), R)
```

Ask whether the recorded operation regenerates the descendant surface or
reading-state.

Return:

```text
EXACT REGATE
ATTRIBUTABLE REGATE
DIVERGENT REGATE
INSUFFICIENT RING RECEIPT
```

`EXACT REGATE` does not prove that the reconstructed pre-ring state is the only
historical ancestor. It only proves that the declared ring can reproduce the
tested descendant under the recorded conditions.

## 9. Hostility test

`constraint != hostility`.

A ring becomes a candidate **hostile encoding ring** only when evidence supports
one or more stronger properties such as:

- suppressing or destroying recoverable alternatives;
- concealing that the layer is later or external to the nucleus;
- impersonating the nucleus or original voice;
- preventing lawful inversion or audit;
- self-authenticating its own output;
- silently expanding interpretive or institutional authority;
- using the ring's downstream effects as proof that the ring was always native;
- deliberately binding, trapping, erasing, or redirecting an object or target.

Distinguish:

```text
PROTECTIVE RING
INTERPRETIVE RING
NORMALIZING RING
PERFORMATIVE RING
ADVERSARIAL / HOSTILE RING
UNKNOWN
```

Intent and structural effect are separate fields. A benevolent preservation
system can later become structurally oppressive if its provenance disappears
and its chosen output becomes indistinguishable from the nucleus.

## 10. Output contract

Preserve at minimum:

```text
H0
NUCLEUS
RING LEDGER
OMEGA BEFORE
OMEGA AFTER
DELTA OMEGA
UNGATED CANDIDATES
HISTORICAL FILTER
SLEEP STATES, if any
HOSTILE TRIANGULATION, if used
REGATE RESULT
WHAT THE RING ACTUALLY CHANGED
WHAT REMAINS UNRESOLVED
NEXT DISCRIMINATOR
```

Keep discovery trace and evidence path distinct when formation history matters.
Use PEEL / SLEEP / LEEP around UNGATE when the research path itself is worth
preserving.

## Adversarial refusals

### OLDER-IS-TRUER

Given a later ring and an older reachable candidate, infer that the older
candidate is therefore the true or intended meaning.

**Required result:** refuse. Older is a temporal relation, not an evidentiary
promotion rule.

### AMBIGUITY-INFLATION

Remove a constraining ring, discover ten formally possible readings, and treat
all ten as historically live.

**Required result:** apply the historical filter. Formal possibility is not
attestation.

### HOSTILITY-BY-CONSTRAINT

A ring reduces ambiguity, therefore call it hostile.

**Required result:** refuse unless stronger evidence establishes adversarial
intent or structurally hostile effects.

### CLOSED-IS-TRUE

A decoder yields a complete, coherent, internally closed interpretation.

**Required result:** refuse truth promotion. Closure means the decoder accounts
for its own ports; it does not prove faithful reconstruction of formation
history.

### RING-ERASURE

UNGATE a layer and then write the result as though the layer never existed.

**Required result:** restore the ring ledger and REGATE. UNGATE preserves the
history of constraint.

## Seal

> **PEEL asks how the surface became this.**
>
> **UNGATE asks what each layer made reachable or unreachable.**
>
> **REGATE tests whether the attributed layer can make the descendant again.**
>
> **Do not free the word from meaning. Free it from meanings that have become
> invisible as gates, then test what the historical world can actually bear.**
