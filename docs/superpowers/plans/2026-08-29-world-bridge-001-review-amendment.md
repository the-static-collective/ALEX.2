# WORLD-BRIDGE-001 — Owner Review Amendment

**Date:** 2026-08-29

## Finding

The first GREEN evaluator required evidence for documented bridge types, but it allowed `source_ref` or `target_ref` itself to satisfy that requirement.

That allowed this malformed reasoning shape:

```text
NODE A exists
NODE B exists
therefore A↔B bridge is documented
```

The endpoints are evidence for their own occurrences. They are not, by themselves, evidence for the edge between them.

## RED

Added hostile tests:

- source endpoint used as bridge evidence → must REFUSE
- target endpoint used as bridge evidence → must REFUSE

Actions run `33261761080` failed exactly on those two tests because the first implementation returned `ACCEPT`.

## Correction

For documented bridge types, every `evidence_ref` must be distinct from both endpoints.

New refusal:

```text
bridge_evidence_must_be_distinct
```

## Verification

Corrected implementation head `f37562a972179905a578b87d31471a90c6ec845a` passed `crucible-contract` run `33261845180`.

The durable law is:

> **TWO NODES DO NOT PROVE THE EDGE BETWEEN THEM.**
