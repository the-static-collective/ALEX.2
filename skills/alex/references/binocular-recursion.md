# BINOCULAR-RECURSION-001

Use this protocol when a bounded inquiry benefits from holding two pressures live at the same time:

- **COMPRESS:** what is the smallest generator or explanation that still preserves the live field?
- **EXPAND:** what follows from NOW under the currently admitted premises and declared relations?

The loop is:

```text
FREEZE → COMPRESS || EXPAND → TENSION → UPDATE → REPEAT
```

`||` means epistemically simultaneous, even if software computes the two traces sequentially. Neither eye may silently close the other.

## Laws

```text
discovery trigger != support
introduced premise != admitted premise
trajectory != focus membership
compression match != truth
terminal stability != truth
ACCEPT != researched claim accepted as true
```

Compression may propose a compact generator. It may not erase a live consequence merely because that consequence complicates the model.

Expansion may follow declared premises and relations to their consequence frontier. It may introduce a proposed premise only if that premise is visibly marked as branch-local; the proposal does not become globally admitted inside the same pass.

Tension is preserved formation data. It may identify missing consequences, surplus generator machinery, unexplained residuals, branch dependence, contradiction, trajectory dependence, or stable match. Tension does not by itself support an external claim.

A field changes only through an attributable update. The binocular operator does not mint authority.

## Executable auditor

The runtime audits an already supplied trace. It does not generate the compression or expansion content.

```bash
python tools/run_binocular_recursion.py tests/fixtures/binocular_recursion/lawful-residual.json
```

Exit `0` means the formation contract was accepted. Exit `1` means the supplied trace was refused or insufficient to test. Exit `2` means the JSON transport could not be executed.
