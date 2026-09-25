# MENU-PROVENANCE-001

**Status:** bounded executable research specimen  
**Authority:** none  
**Promotion:** none  
**Formation:** ALEX.2 #118 downstream of Dogram #132 / #133

## Question

When a collapsed state exposes an aggregate menu of possible futures, what must survive so the union cannot be misread as a possibility owned by every collapsed representative?

## Frozen control

```text
left  -> {green}
right -> {hold}
```

The lawful aggregate is:

```text
MAY  = {green, hold}
MUST = {}
```

but the representative-local families remain:

```text
left  -> {green}
right -> {hold}
```

and the contributor relation is:

```text
green <- {left}
hold  <- {right}
```

Therefore:

```text
AGGREGATE POSSIBILITY != REPRESENTATIVE POSSIBILITY
MAY != MUST
SUMMARY != UNIVERSALIZATION
```

A shared-successor control adds `advance` to both representatives and receipts it in `MUST` with both contributors.

## Executable surface

`alex_runtime.menu_provenance.summarize_menu()` returns only:

- deterministic representative-local successor families;
- aggregate `may` union;
- common `must` intersection;
- successor-to-contributor relation;
- `authority: none`.

It refuses an empty representative family.

## Boundary

```text
POSSIBLE != OCCURRED
MAY != AUTHORIZED
MUST-IN-THIS-FAMILY != INEVITABLE HISTORICAL FUTURE
CONTRIBUTOR != CAUSE
SUMMARY != EVIDENCE
```

No modal logic engine, evidence semantics, causal semantics, runtime ontology, or authority path is introduced.

## Verification target

Focused tests freeze:

1. disjoint representative menus with a larger aggregate union;
2. one truly common possibility entering `must`;
3. empty-family refusal.
