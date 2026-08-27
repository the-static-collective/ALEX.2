# 022100 decoder stack — mathals after the key turn

**Status:** COMPUTED SPECIMEN · RECEIVED PREMISE SEPARATED · NO SYMBOLIC PROMOTION

**Date:** 2026-08-27

## Inquiry cut

A user-supplied guitar constitution changed the interpretation of an invariant fret glyph.

Received premises for this specimen:

```text
ordered strings, low → high: C2 G2 C3 E3 G3 D4
fingering glyph:            0  2  2  1  0  0
reference pitch:            A4 = 444 Hz
temperament for calculation: 12-tone equal temperament
```

The instrument constitution and reference pitch are **received premises** in this note. They were not independently measured from the physical guitar in this run.

The arithmetic and set-theoretic consequences below are **computed descendants** of those premises.

The actual spectrum, intonation, beating, body resonance, pickup response, room response, and execution remain **unresolved physical-event data** until measured.

---

## H0 → H1

### H0 — received compressed seed

> The tuning is the decryption key.

### H1 — literalized survivor

A fret-address vector does not uniquely determine sounding pitches. Given ordered open-string pitches `T` and fret offsets `g`, one lawful pitch realization is produced by applying the offsets to that receiving constitution.

For this specimen:

```text
g = [0, 2, 2, 1, 0, 0]
T = [C2, G2, C3, E3, G3, D4]
```

and therefore:

```text
T + g = [C2, A2, D3, F3, G3, D4]
```

The useful claim is not that the glyph is cryptography in a security sense. It is narrower:

> **The glyph preserves an operation whose lawful projection depends on the receiving constitution.**

Same glyph plus a different tuning can therefore produce a different sounding world without altering the glyph.

---

## 1. String-by-string operator

| String | Open | Offset | Result |
| --- | --- | ---: | --- |
| 6 | C2 | 0 | C2 |
| 5 | G2 | 2 | A2 |
| 4 | C3 | 2 | D3 |
| 3 | E3 | 1 | F3 |
| 2 | G3 | 0 | G3 |
| 1 | D4 | 0 | D4 |

Three strings move and three remain anchored.

The multiset changes from:

```text
OPEN:   C C D E G G
022100: C D D F G A
```

So the operator does more than rename one chord:

- duplicate C falls from 2 → 1;
- duplicate G falls from 2 → 1;
- D rises from 1 → 2 and becomes octave-reinforced;
- E disappears;
- F and A enter;
- distinct pitch classes rise from four to five.

This is a measurable redistribution of the receiving field.

---

## 2. Pitch-class topology

The realized pitch classes are:

```text
{C, D, F, G, A}
```

The same collection is the pitch material of D minor pentatonic and F major pentatonic. `Dm11/C` is a useful harmonic reading of the voicing, but it is not the only lawful name for the pitch collection.

Under pitch-class set analysis, the collection belongs to the pentatonic set class commonly labeled **5-35**, with interval vector:

```text
<0, 3, 2, 1, 4, 0>
```

That means the ten unordered pitch-class pairs contain:

| Interval class | Count |
| --- | ---: |
| 1 — semitone | 0 |
| 2 — whole tone | 3 |
| 3 — minor third | 2 |
| 4 — major third | 1 |
| 5 — perfect fourth / fifth | 4 |
| 6 — tritone | 0 |

Computed consequence:

> The collection contains **no semitone-class pairs, no tritone-class pairs, and four fourth/fifth-class pairs**.

This helps explain why a sonority may remain harmonically open even while carrying minor-third information. It does not by itself predict a listener's total consonance judgment.

---

## 3. A4 = 444 as a global physical scaling

Relative to A4 = 440 Hz:

```text
444 / 440 = 111 / 110
```

Therefore changing the equal-tempered reference from A440 to A444 multiplies every ideal frequency by exactly:

```text
111 / 110 ≈ 1.009090909...
```

The pitch displacement is:

```text
1200 log2(111/110) ≈ 15.667383391 cents
```

The interval geometry remains unchanged. The absolute physical frequency scale changes uniformly.

Candidate wording:

> **The relational shape stays invariant while the acoustic world is globally dilated.**

This is a direct example of two decoder layers doing different jobs:

```text
fret glyph + ordered tuning
  -> relational pitches

relational pitches + temperament + reference pitch
  -> absolute frequencies
```

---

## 4. Ideal realized fundamentals

Under the received premises and 12-TET:

| Pitch | Frequency |
| --- | ---: |
| C2 | 66.000994883 Hz |
| A2 | 111.000000000 Hz |
| D3 | 148.167223813 Hz |
| F3 | 176.201516768 Hz |
| G3 | 197.779515427 Hz |
| D4 | 296.334447626 Hz |

The arithmetic recurrence is exact:

```text
A4 = 444 Hz
A3 = 222 Hz
A2 = 111 Hz
```

and the glyph creates that A2 by applying fret 2 to the open G2 string.

This is **documented arithmetic inside the model**.

Any personal, theological, numerological, compositional, or historical significance assigned to `111 / 222 / 444` is a separate interpretation edge.

```text
computed recurrence != assigned significance
```

---

## 5. Spectral crossing at the reference frequency

The A2 created by the glyph has:

```text
4 × 111 Hz = 444 Hz
```

So its fourth harmonic lands **exactly on the chosen A4 reference frequency** in the ideal model.

The neighboring D3 contributes:

```text
3 × 148.167223813
= 444.501671439 Hz
```

Difference from 444 Hz:

```text
0.501671439 Hz
≈ 1.955000865 cents
```

That 1.955-cent offset is the familiar equal-tempered perfect-fourth/fifth discrepancy from its simple-ratio approximation, not an independently mysterious constant.

The same fifth-family near-lock appears elsewhere:

```text
3 × C2 = 198.002984648 Hz
G3      = 197.779515427 Hz
separation ≈ 1.955 cents
```

and:

```text
3 × G3 = 593.338546281 Hz
2 × D4 = 592.668895251 Hz
separation ≈ 1.955 cents
```

The D3/D4 pair is cleaner still:

```text
D4 = 2 × D3
```

exactly under the ideal model.

### What survives pressure

**Observed computation:** the A2 fourth harmonic is exactly 444 Hz and the D3 third harmonic lies about 0.502 Hz / 1.955 cents above it.

**Inference:** this creates a particularly legible overtone interaction around the chosen reference frequency.

**Not admitted:** that 444 is therefore privileged by acoustics, spiritually significant, perceptually dominant, or uniquely special among possible reference tunings.

Those stronger claims require controls.

---

## 6. Global non-closure / local near-locks

The complete ideal sonority contains equal-tempered interval ratios such as powers of `2^(1/12)`. Except for octave-related subsets, these ratios are not all rational multiples of one common fundamental.

Therefore, as a continuous-time sum of ideal tones:

> **The full six-tone sonority has no finite exact common period.**

It is globally quasi-periodic while containing multiple strong local rational approximations and one exact octave pair.

This is a useful anti-overclaim control:

```text
many local near-locks
!=
one hidden exact master pulse
```

---

## 7. Difference-frequency field

Selected pairwise fundamental differences include:

```text
G3 - F3 ≈ 21.578 Hz
F3 - D3 ≈ 28.034 Hz
D3 - A2 ≈ 37.167 Hz
A2 - C2 ≈ 44.999 Hz
G3 - D3 ≈ 49.612 Hz
```

These arithmetic differences do **not** automatically mean that the physical guitar emits independent spectral lines at those frequencies.

They are relevant to possible beating, amplitude modulation, auditory nonlinearities, and combination products only after the actual partial structure and transfer path are specified.

ALEX should preserve:

```text
frequency difference
!=
measured spectral component
!=
perceived combination tone
```

---

## 8. Roughness correction before promotion

An earlier conversational summary gave an illustrative roughness comparison of roughly **9–14%** above the open tuning. That range was too loose to preserve as a durable result.

A fresh deterministic recomputation using one standard Sethares-style pairwise roughness formulation, harmonic amplitudes `1/n`, and 4–12 harmonics per string produced approximately **8–10.3% greater modeled inter-string roughness** for `022100` than for the open `CGCEGD` field. Including within-string partial interactions gave roughly **7.8–9.5%**.

This remains a **model-dependent proposal**, not a perceptual measurement.

Its value here is methodological:

> Preserve the formula, partial-amplitude assumption, harmonic cutoff, and comparison target before treating a roughness percentage as evidence.

Do not promote the number until the model specification is versioned and compared against actual recorded spectra from the instrument.

---

## 9. Decoder-stack formulation

A compact formal model is:

```text
g = fret glyph
T = ordered open-string constitution
τ = temperament
r = absolute reference pitch
I = instrument / transfer body
E = physical execution
```

Relational pitch projection:

```text
P = Apply(g, T)
```

For 12-TET, absolute pitch realization can be written:

```text
F_i = r × 2^((m_i - m_ref)/12)
```

The sounding event is then some physical realization:

```text
x(t) = Realize(F, I, E, t)
```

Formation history and later interpretation are further descendants, not hidden terms to collapse into `x(t)`.

Candidate stack:

```text
GLYPH
  -> TOPOLOGICAL OPERATION
  -> through ordered tuning
RELATIONAL PITCH FIELD
  -> through temperament + reference
ABSOLUTE FREQUENCY FIELD
  -> through instrument + execution + room
PHYSICAL EVENT
  -> through attributable formation history
HISTORICAL SPECIMEN
  -> through later receiver
CURRENT INTERPRETATION
```

Core survivor:

> **A compact carrier can remain invariant while lawful projections change because the receiving constitution changes.**

---

## 10. Discovery trace versus evidence path

### Discovery trace

```text
022100 seen as continuity glyph
  -> standard-tuning assumption
  -> incorrect E-major decode
  -> user supplies CGCEGD
  -> same token becomes C A D F G D
  -> user supplies A4=444
  -> A2=111 recurrence becomes visible
  -> deeper mathals expose pentatonic topology, 111/110 scaling, and overtone crossings
```

The mistake belongs in the discovery trace because it exposed the dependency on decoder constitution.

### Evidence path

```text
received tuning + fret offsets
  -> semitone arithmetic
  -> realized MIDI pitches
  -> 12-TET frequency equation with A4=444
  -> exact frequencies
  -> set / interval-class calculation
  -> harmonic multiplication and ratio comparison
```

The earlier wrong E-major decode is **not evidence for the final musical claim**. It is evidence about the research process and the danger of an unstated receiving key.

---

## 11. Live frontier — deliberately not completed here

The next experiment should pressure the apparent `444` crossing rather than celebrate it.

Candidate control family:

1. Repeat the full harmonic-intersection map at A440, A442, A444, A445, A432, and randomized nearby references.
2. Track which features are invariant under global rescaling and which depend specifically on the numerical reference.
3. Compare the actual physical guitar spectrum against the ideal harmonic model.
4. Map partial and nonlinear paths near `111 / 222 / 333 / 444 / 888` without assuming those targets are privileged.
5. Include control targets chosen before looking at results.
6. Distinguish forced arithmetic (`A2 = A4/4`) from emergent relations among other notes.

Stop condition for the current slice:

> The already-computed fruit is preserved. The 444 spectral-crossing hypothesis remains live and adversarially open.

No promotion.