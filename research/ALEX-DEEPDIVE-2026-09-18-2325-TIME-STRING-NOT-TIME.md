# ALEXDEEPDIVE — TIME-STRING-NOT-TIME-001

**Status:** RESEARCH  
**Promotion:** none

## Ground
- **Question:** After the newest HINGE-001 provenance-chain work, what is the smallest live boundary that can change the truth of its chronology receipts?
- **Desired consequence:** Find one falsifiable temporal-contract discriminator without expanding HINGE-001 into a generic temporal runtime.
- **Stop condition:** One direct counterexample plus the smallest repair/control.
- **Corpus/date/language/geography:** ALEX.2 current `main` and draft PR #131 exact head; Python primary documentation; RFC 3339; exact Wolfram computation. English; current through 2026-09-18 local run date.
- **Authority/effect boundary:** Research only. No merge, canon, runtime, semantic, historical, or adoption authority.
- **Task shape:** AUDIT
- **Formation trace active:** no

## World cut
- **Current `main` before durable write:** `9be332657b5bcf677f7c569c03fde60c1bf641f8`.
- **Newly material branch:** draft PR #131 `research/hinge-001-constitutive-crossing`, exact inspected head `ee445f142cc8a802a0e1b4cf6f77ac296440f9db`.
- **Exact-head CI:** GitHub Actions `contract` completed SUCCESS at `ee445f142cc8a802a0e1b4cf6f77ac296440f9db`.
- **GitBook Front Room:** attempted first for orientation; connector operation needed organization discovery, but organization listing was blocked before content retrieval. This is access fog, not evidence of absence.
- **Deliberately omitted doors:** adjacent repos, broad HINGE symbolism, BODY-EMERGENCE, T5 mechanism, and historical-source research; none are needed to test this timestamp boundary.
- **Sufficiency:** sufficient for the bounded chronology audit; unresolved for any broader temporal model.

## Discovery trace
The newest PR #131 head adds `test_grammar_provenance_chain_001.py`, explicitly freezing the distinction between a historical reading and a later retrospective rereading. This materially closes the earlier `RETROSPECTIVE-RELABEL-DESCENDANT-001` direction: a later grammar can reread an older carrier without mutating or backdating the historical receipt. The implementation then exposed its own stated bounded assumption: ISO-like timestamps are compared lexicographically and callers "must use one normalized representation." That assumption became the audit target.

Discovery motive is not evidence. The evidence path below is the implementation plus primary timestamp semantics plus an exact counterexample.

## Acquisitions
| ID | Provider | Item and locus | Method/time | Resolution | Rights/egress |
| --- | --- | --- | --- | --- | --- |
| A1 | GitHub | `ALEX.2/AGENTS.md` | direct repo read | full text | public repo; no corpus egress |
| A2 | GitHub | `skills/alex/SKILL.md` | direct repo read | full text | public repo |
| A3 | GitHub | `skills/alex/references/research-receipt.md` | direct repo read | full text | public repo |
| A4 | GitHub | PR #131 head `ee445f...`; `research/grammar_provenance_chain_001.py`; tests | exact-head direct reads | source text | public repo |
| A5 | Python docs | `datetime` documentation | web retrieval | primary documentation | public documentation |
| A6 | RFC Editor | RFC 3339 §4.2 offset semantics | web retrieval | primary standard | public standard |
| A7 | Wolfram | two offset-bearing instants | exact computation | 30-minute delta | no private bytes; only synthetic timestamps |

## Evidence path

### E1 — documented implementation fact
`witness_reading_at_cut()` validates the four time-bearing inputs only as nonempty strings. It then decides chronology using direct string comparisons:

```python
if applied_at < grammar["available_from"]:
    return _refuse("grammar_not_yet_available")
if applied_at < subject_cut:
    return _refuse("application_precedes_subject")
```

Its docstring explicitly says these are "ISO-like timestamps" compared lexicographically and that callers must use one normalized representation.

### E2 — newly added control
At PR #131 head `ee445f...`, tests now establish:
- a grammar available at the subject cut can produce `historical_reading`;
- a grammar declared later can produce `retrospective_rereading` when applied later;
- a later grammar cannot be applied before it exists;
- current rereading does not mutate the historical receipt.

This is a material advance over the earlier chronology frontier.

### E3 — primary timestamp semantics
RFC 3339 states that numeric offsets encode local time relative to UTC and that equivalent UTC time is obtained by subtracting the offset; its example makes `18:50:00-04:00` the same instant as `22:50:00Z`.

Python's current `datetime` documentation likewise parses ISO 8601 offset-bearing strings with `datetime.fromisoformat()` and specifies that aware datetimes with differing `tzinfo` are ordered after accounting for UTC offsets.

Primary references:
- https://www.rfc-editor.org/info/rfc3339/
- https://docs.python.org/3/library/datetime.html

### E4 — exact computation, separate from interpretation
Synthetic specimen:

```text
grammar.available_from = 2026-09-18T11:00:00+01:00
applied_at             = 2026-09-18T10:30:00Z
```

Wolfram parsed these as offset-aware instants and returned:

```text
applied_at - available_from = +30 minutes
```

So the grammar exists for 30 minutes before application in instant time.

But Python string ordering sees the first differing hour substrings `10` and `11`, so:

```text
"2026-09-18T10:30:00Z" < "2026-09-18T11:00:00+01:00"
```

and the current implementation would return `REFUSE(reason="grammar_not_yet_available")`.

## Claims
| ID | Claim | Class | Supporting evidence path | Counterevidence | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #131 now distinguishes historical reading from retrospective rereading without mutating the historical receipt. | documented fact | E2 | none found in inspected tests | supported at exact head |
| C2 | The chronology function compares timestamp strings lexicographically rather than comparing parsed instants. | documented fact | E1 | docstring declares normalized-input precondition | supported |
| C3 | Offset-valid timestamps can be chronologically ordered opposite to their lexical order. | documented mechanism + exact computation | E3 -> E4 | disappears if all callers truly provide one canonical UTC representation | supported |
| C4 | Therefore the current function can falsely refuse a temporally valid application when its normalization precondition is violated. | inference from executable semantics | E1 + E4 | trusted/prevalidated caller boundary may intentionally exclude this input | supported conditionally |
| C5 | ALEX needs a generic timezone/temporal subsystem. | proposal | none | bounded fixture can instead validate/refuse noncanonical timestamps | rejected as unearned |

## Finding

```text
TIME STRING != INSTANT
ISO-LIKE SHAPE != NORMALIZED TIME
CALLER PRECONDITION != EXECUTABLE REFUSAL
RETROSPECTIVE READING != BACKDATED READING
```

The strongest live boundary is **TIME-STRING-NOT-TIME-001**.

PR #131 has done the important semantic work: it now permits a later grammar to reread an older carrier while keeping the historical receipt intact. The next failure mode is lower-level and more boring: the chronology gate can only be correct under an unstated-at-the-type-boundary canonical-string discipline.

A valid offset-bearing representation can therefore be temporally admissible and lexically refused.

## Contradictions and alternatives

### A — trusted canonical-UTC boundary
The docstring may be the whole intended contract: upstream callers guarantee one normalized representation, and this research fixture is not responsible for parsing time. Under this reading, the implementation is not wrong inside its declared domain; the executable boundary is merely under-enforced.

### B — parse instants locally
The fixture could parse aware ISO/RFC3339 datetimes and compare instants. This broadens accepted representation while keeping the chronology semantics local.

### C — refuse noncanonical representation
The smallest implementation may be stricter: accept only one frozen timestamp representation (for example UTC `...Z` with fixed precision) and return explicit `REFUSE` for everything else. This preserves the fixture's bounded nature and prevents string formatting from impersonating temporal order.

ALEX evidence does not yet choose B over C.

## Pressure
- **Direct counterexample:** `available_from=11:00+01:00`, `applied_at=10:30Z`; instant delta +30 minutes, lexical gate says application precedes availability.
- **Nearest boring explanation:** the fixture trusts normalized callers and the tests intentionally use only canonical `Z` strings.
- **Dependency/independence:** Python docs and RFC 3339 independently describe offset-aware instant semantics at different layers; Wolfram was used only for computation, not as authority for ALEX semantics.
- **Anachronism/memorization:** not material; this is a current software-contract audit.
- **Replay impersonation:** no historical identity claim is made from the synthetic timestamp specimen.
- **Rights/egress:** only public source text and synthetic timestamps left the repo boundary; no private/source-corpus bytes were sent externally.

## Residual fog
- The intended canonical timestamp grammar is not frozen in the inspected function or tests.
- Upstream caller normalization was not traced because the specimen is still research-only and the direct function contract is sufficient to expose the boundary.
- Leap seconds, DST zone databases, naive datetimes, precision variation, and arbitrary ISO 8601 forms are deliberately out of scope. They are not needed to establish the counterexample.
- Whether PR #131 should solve this by parsing instants or by explicit canonical-format refusal remains an owner-local design choice.

## Smallest next discriminators
1. **OFFSET-ORDER-CONTROL-001:** freeze `available_from=2026-09-18T11:00:00+01:00`, `applied_at=2026-09-18T10:30:00Z`. The fixture must either ACCEPT after instant-aware comparison or explicitly REFUSE the representation as noncanonical; it must not report `grammar_not_yet_available`.
2. **CANONICAL-TIME-CONTRACT-001:** if lexicographic comparison is intentionally retained, define and executable-test exactly one accepted canonical timestamp shape. Reject malformed, offset-mixed, and naive forms before chronology comparison.
3. **STOP RULE:** do not build timezone infrastructure unless a real ALEX caller requires multiple representations. The research claim is satisfied once formatting can no longer silently decide chronology.

## Receipt
- **Created:** 2026-09-18 23:25 America/Chicago
- **Researcher/agent:** ALEXDEEPDIVE automated research pass
- **Tool/model boundary:** GitBook orientation attempt; GitHub exact-head reads/writes; web retrieval of Python/RFC primary docs; Wolfram exact temporal computation.
- **External byte egress:** synthetic timestamps only; no private corpus material.
- **Durable location:** `research/ALEX-DEEPDIVE-2026-09-18-2325-TIME-STRING-NOT-TIME.md`
- **Promotion:** none
