# ALEXDEEPDIVE — RIGHTS-REF-NOT-RIGHTS-001

Status: RESEARCH  
Promotion: none  
Shape: AUDIT

## Ground

- Question: What is the strongest newly exposed research boundary in ALEX.2 since the previous ALEXDEEPDIVE packet?
- Desired consequence: identify one smallest hostile discriminator without promoting research into runtime authority.
- Stop condition: one materially evidenced boundary, its boring explanation, counter-reading, residual fog, and 1–3 smallest next moves.
- Corpus/date/language/geography: current ALEX.2 repository state through inspected head `3df266f0369b0d2e015add3618496180422a84db`; English; repository-local semantics.
- Authority and effect boundary: research only. No canon/runtime promotion. This packet itself changes no runtime behavior.
- Formation trace active: no.

## Orientation

GitBook Front Room was reached first. Its orientation remains deliberately narrow: the room is a stable landmark, destination bodies may change, and bounded traversal should follow a relevant door rather than loading the world. That orientation did not supply evidence for the finding below; current ALEX.2 code and design do.

## World cut

### Included

- `ALEX.2/AGENTS.md`
- `skills/alex/SKILL.md`
- `skills/alex/references/research-receipt.md`
- repository delta from prior packet commit `14f02bd92b0d65dab302c0b02ef0ba4f1bb8b19f` to `3df266f0369b0d2e015add3618496180422a84db`
- `alex_runtime/commons.py`
- `tests/test_commons.py`
- `docs/superpowers/specs/2026-09-17-alex-commons-library-card-dialogic-trace-design.md`

### Deliberately omitted

- adjacent repositories: not needed; the boundary is fully local to the newly landed Commons intake contract.
- broad web scholarship: not needed to establish an internal mismatch between declared rights semantics and the current evaluator boundary.
- Wolfram: no mathematical/statistical/temporal/geometric/scientific calculation bears on this discriminator.

### Material delta

Since the prior packet, `main` advanced six commits to `3df266f...`. The dominant new surface is **ALEX Commons + DIALOGIC TRACE v0**, including Commons rights records, deposit intake, pseudonym continuity, hostile specimens, and tests.

## Finding

The strongest live boundary is:

```text
RIGHTS STATEMENT REF != RIGHTS STATEMENT
DIGEST SHAPE != RESOLVED RIGHTS
DEPOSIT PUBLICATION FIELD != PROVEN PUBLICATION PERMISSION
```

`evaluate_commons_deposit()` currently verifies that `rights_statement_ref` has the syntactic form `sha256:<64 hex>` and independently verifies that the deposit's `publication_permission` is one of `YES | NO | UNRESOLVED`. It does **not** resolve the referenced rights statement, prove that the digest names the intended rights receipt, or require the deposit-level publication field to agree with the referenced statement.

That means a deposit can be locally accepted with, for example:

```text
rights statement: publish = NO
rights_statement_ref: syntactically valid digest
commons deposit: publication_permission = YES
```

provided the evaluator is called on the deposit alone. The current tests instantiate `BASE_RIGHTS.publish = NO` and `BASE_DEPOSIT.publication_permission = NO`, but they do not bind the two records or freeze a contradictory pair.

## Claims

| ID | Claim | Class | Supporting evidence path | Counterevidence | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | Commons v0 newly landed after the previous packet. | observed | Git compare `14f02bd... -> 3df266f...` | none observed | established for this run |
| C2 | Rights declarations are designed as separate hold/process/quote/publish/identity/reply permissions. | documented design | Commons design §9 | none | established |
| C3 | Deposit evaluation validates the rights ref only as digest-shaped text and publication permission only as an enum value. | observed | `alex_runtime/commons.py::evaluate_commons_deposit` | none | established |
| C4 | The current deposit evaluator does not resolve or compare the referenced rights statement. | observed | same function; no rights object/store argument or lookup path | possible intended composition at a later intake stage | established for this function; system-level intent unresolved |
| C5 | A contradictory rights/deposit pair can therefore each be structurally accepted when evaluated independently. | inference from executable contract | `evaluate_rights_statement` + `evaluate_commons_deposit` signatures and checks | no end-to-end contradictory specimen was executed in this research pass | strongly supported, executable discriminator still owed |
| C6 | This is necessarily a bug. | proposal | none | design may intentionally keep structural validation separate from referential resolution | **not admitted** |

## Contradictions and alternatives

### Reading A — missing referential-integrity gate

If `publication_permission` on a deposit is intended to testify to the permission granted by its `rights_statement_ref`, accepting disagreement allows a permission field to outrun the source it claims to summarize. That would violate the design's central requirement that publication rights remain explicit and unresolved by default when unclear.

### Reading B — deliberately separate structural validators

The boring explanation is credible: these functions may only validate record shape at arrival. `rights_statement_ref` may be a future content-addressed link whose resolution belongs to a later store/composition layer. Under this reading, neither standalone evaluator is wrong; what is missing is an end-to-end composition gate, not stricter local parsing.

### Reading C — deposit permission is independent testimony

A contributor might intentionally make a deposit-level publication declaration separate from a prior rights statement. But if so, the semantics need an explicit precedence/version/descendant rule. A bare contradiction cannot safely decide whether the newer field supersedes, narrows, broadens, or merely conflicts with the referenced rights record.

## Pressure

- Direct counterexample: no current hostile specimen was found that binds a `publish=NO` rights statement to a `publication_permission=YES` deposit and demands refusal/hold.
- Nearest boring explanation: standalone structural validators are intentionally non-resolving; composition is simply not implemented yet.
- Dependency/independence: the deposit's rights field and rights ref are currently syntactically co-present but semantically unjoined by the inspected evaluator.
- Rights/egress boundary: this is precisely where conservatism matters. Until a resolved rights path proves publication permission, a syntactically valid digest must not itself grant egress.
- Authority: none. The finding does not alter Commons policy or implementation.

## Discovery trace vs evidence path

Discovery trace: recent commit scan exposed the new Commons surface; inspection of `commons.py` made the duplicate publication-rights representation salient.

Evidence path: design §9 -> rights evaluator -> deposit evaluator -> current tests. The fact that the recent commit drew attention to Commons is not evidence for the claim.

## Residual fog

- No persistent Commons store/resolver was found or inspected that might already bind `rights_statement_ref` to an evaluated rights receipt after structural intake.
- It is unresolved whether deposit-level `publication_permission` is intended as a cached projection, independent testimony, or a later override.
- No precedence law for contradictory rights descendants was established in this pass.

## Smallest next discriminators

1. **RIGHTS-REF-CONSISTENCY-001** — freeze one evaluated rights statement with `publish=NO`, bind its actual digest/ref into a deposit claiming `publication_permission=YES`, and require an explicit non-public outcome (`REFUSE` or `HELD`) at the first composition layer that resolves references.
2. Add the positive control: the same resolved rights receipt with matching `publication_permission=NO` survives composition unchanged.
3. If rights statements are versionable, define the smaller precedence law before adding machinery: later rights record may narrow/broaden only through explicit ancestry; unresolved contradiction never silently grants publication.

## Receipt

- Created: 2026-09-17 23:22 America/Chicago
- Researcher/agent: ALEXDEEPDIVE
- Tool/model boundary: GitBook orientation; GitHub repository inspection and durable write. No external model byte egress. No Wolfram computation used.
- External byte egress: none from local/source corpora; repository text was read through connected GitHub/GitBook services.
- Durable location: `research/ALEX-DEEPDIVE-2026-09-17-2322-RIGHTS-REF-NOT-RIGHTS.md`
- Promotion: none

## Compact result

**Finding:** Commons v0 currently preserves a rights-statement digest reference and a deposit-level publication permission, but the inspected deposit evaluator does not prove they agree.

**Counter-reading:** this may be correct structural validation with referential composition intentionally deferred.

**Next discriminator:** `RIGHTS-REF-CONSISTENCY-001` at the first layer that can resolve the referenced rights receipt.
