# SYZYGY-PRESSURE-001 — Relation Closure Under Hostile Cuts

**Status:** candidate research method / no kernel promotion

## Purpose

ALEX receives an already-declared syzygy candidate and pressure-tests whether the claimed relation survives its stated ambient, decoder, parser, and controls.

ALEX does **not** discover arithmetic truth by aesthetic resemblance and does not inherit semantic authority from Dogram receipts.

## Input contract

A candidate should minimally declare:

```yaml
ambient: A
generators: G
decoder: D
relation: R
residual: epsilon
source_surface: source
controls: []
```

Dogram may calculate `epsilon = R(G)`. ALEX asks what that closure does and does not support.

## Pressure sequence

### Gate 1 — generator identity

Are the named generators actually present in the source surface, or were they introduced by normalization, segmentation, concatenation, unit choice, date formatting, base conversion, or another decoder?

```text
SOURCE VALUE != DECODED VALUE
DECODED VALUE != SOURCE INVARIANT
```

### Gate 2 — ambient declaration

Does the relation depend on a specific ring, field, module, coordinate system, base, scale, or topology?

A relation that holds in one ambient world must not silently migrate into another.

Example control:

For

\[
M=\begin{pmatrix}
1&1&0\\
1&0&1\\
0&1&1
\end{pmatrix},
\]

over `F_2` there is a nontrivial kernel vector `(1,1,1)`, while over `F_3` the kernel is trivial.

Therefore:

```text
SAME SURFACE MATRIX != SAME SYZYGY SPACE
```

### Gate 3 — decoder dependence

Re-run the candidate under nearby lawful decoders.

Examples:

```text
date components vs concatenated integer
raw delta vs GCD-reduced delta
integer factorization vs Gaussian-integer factorization
ordered-pair space vs unordered-pair space
```

Classify:

```text
SOURCE_INVARIANT
DECODER_STABLE
DECODER_LOCAL
DECODER_FRAGILE
```

These labels describe the tested relation only.

### Gate 4 — residual

Record the exact residual:

\[
\epsilon=R(G).
\]

Do not round a nonzero residual into closure without an explicitly justified tolerance model.

```text
ZERO RESIDUAL != CAUSATION
SMALL RESIDUAL != EXACT RELATION
```

### Gate 5 — hostile siblings

Construct nearby controls that preserve the superficial visual/numerical attraction while breaking one structural condition.

Examples for a date tuple:

```text
same digits, different parser
same month, neighboring day/year
same raw delta, different GCD carrier
same equality shape, shuffled generator roles
```

A candidate that survives only the chosen specimen remains local.

### Gate 6 — phenomenal bridge

If the candidate is connected to a historical, physical, symbolic, or theological occurrence, require an independent bridge from the mathematical relation to the phenomenon.

```text
MATHEMATICAL CLOSURE != HISTORICAL LINKAGE
MATHEMATICAL CLOSURE != PHYSICAL MECHANISM
MATHEMATICAL CLOSURE != SYMBOLIC INTENTION
```

Absence of such a bridge does not invalidate the arithmetic. It limits the promoted claim.

## Relation to receipts

For a formation map

\[
\Delta x=Nf,
\]

endpoint-invisible history lies in

\[
\ker N.
\]

If a receipt map `R_c` is added, remaining hidden history is

\[
\ker N\cap\ker R_c.
\]

Candidate architectural reading:

> A receipt can distinguish histories that were syzygous under a weaker projection.

ALEX should preserve this as an analogy grounded in exact linear algebra, not promote it into a universal definition of receipt.

## Higher-syzygy pressure

When a verified relation is reified as a next-level carrier, require the new level to preserve provenance to the lower-level relation.

```text
RELATION -> REIFIED CARRIER
```

must retain:

```text
source generators
ambient
original decoder
original residual
formation receipt
```

and must not imply:

```text
REIFIED RELATION -> AUTHORITY
REIFIED RELATION -> SOURCE IDENTITY
REIFIED RELATION -> PHENOMENAL CAUSE
```

## Example: SYZYGY-001 date specimen

Literal tuple:

\[
(8,27,26)\to(8,28,28).
\]

Exact observations include:

\[
28=\binom82,
\qquad
8+28+28=64,
\qquad
27=26+1.
\]

The component transition has raw delta `(0,1,2)`, while GCD peeling makes both changing coordinates primitive forward unit steps.

Hostile control:

\[
82726\to82828
\]

produces reduced displacement `51`, so the paired unit-step structure is parser-local.

Disposition:

```text
exact arithmetic                       ESTABLISHED
component-parser closure               ESTABLISHED / DECODER-LOCAL
syzygy decoder architectural utility   CANDIDATE METHOD
historical/cosmic encoding             UNSUPPORTED absent independent bridge
```

## Output record

```yaml
candidate_id:
closure_status:
ambient_status:
decoder_status:
residual:
hostile_controls:
source_bridge_status:
promotable_claim:
refused_claims:
open_questions:
```

## Seal

\[
\boxed{\textbf{A RELATION MAY CLOSE EXACTLY AND STILL SUPPORT ONLY A LOCAL CLAIM.}}
\]

ALEX owns the pressure, not the arithmetic and not the final authority.