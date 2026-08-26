# ALEX Crucible

ALEX Crucible is a portable constitutional fixture contract. It is not the ALEX research runtime and does not select a production implementation language.

## Adapter protocol

```text
stdin  -> one complete specimen JSON object
stdout -> one complete result JSON object
exit 0 -> adapter produced a parseable attempted result
nonzero -> adapter could not execute the specimen
```

Exit `0` is not conformance. The reference harness still compares the attempted result against the specimen's required disposition, refusal code, required receipt survivors, and forbidden promotions.

A refusal is incomplete if it discards the evidence or residue the specimen says must survive. A result also fails if it performs a forbidden promotion even when its headline disposition looks correct.
