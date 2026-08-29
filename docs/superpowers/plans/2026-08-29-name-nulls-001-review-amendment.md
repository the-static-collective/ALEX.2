# NAME-NULLS-001 — Owner Review Amendment

**Date:** 2026-08-29

## Finding

The first GREEN battery validator enforced a complete six-control family but tolerated opaque extra fields. That allowed a control packet to carry a predeclared favored result while still receiving structural `ACCEPT`.

Examples:

```text
expected_answer: favored hypothesis survives
expected_outcome: still hits
survival_expected: true
```

A null that carries the answer it is supposed to test is not hostile.

## RED

Added tests for battery-level `expected_answer`, control-level `expected_outcome`, and control-level `survival_expected`.

Actions run `33261891997` ran 207 tests and failed exactly those three review tests because the first implementation returned `ACCEPT`.

## Correction

The evaluator now refuses explicit result-bearing fields at battery and control level with:

```text
favored_answer_not_allowed
```

The control may still state `next_discriminator`: what observation would discriminate. It may not state which observation is expected or desired.

## Law

> **A TEST THAT ALREADY KNOWS ITS ANSWER IS NOT A HOSTILE TEST.**
