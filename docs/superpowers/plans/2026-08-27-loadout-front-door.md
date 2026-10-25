# LOADOUT Front Door Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Hatch a portable `loadout` skill that routes a task to the smallest sufficient set of currently available capabilities while preserving authority boundaries and leaving irrelevant capabilities asleep.

**Architecture:** Add a compact `skills/loadout/` package alongside ALEX without changing ALEX research semantics. Keep the always-loaded skill surface small; move the plugin-layer taxonomy and evaluation protocol into references. Use repository contract tests and development/holdout routing cases to pressure discovery, non-invocation, missing capability, explicit-tool, and authority behavior.

**Tech Stack:** Markdown Agent Skill package, YAML OpenAI interface metadata, JSON eval catalogs, Python `unittest` contract tests.

**Spec:** `docs/superpowers/specs/2026-08-27-loadout-front-door-design.md`

## Global Constraints

- `task != tool list`
- `mention != mandatory binding`
- `availability != relevance`
- `capability availability != authority`
- `discovery != invocation`
- `read authority != write authority`
- `router choice != evidence`
- `missing capability != missing task`
- Knowledge may load. Capability may bind. Authority does not silently expand.
- The loaded `SKILL.md` must remain under 500 words.
- No ALEX research semantics or runtime kernel files change in this hatch.

---

### Task 1: Freeze the operator contract in RED

**Files:**
- Create: `tests/test_loadout_skill_contract.py`

**Interfaces:**
- Consumes: planned paths under `skills/loadout/` and `evals/`.
- Produces: a repository-level contract that fails before the skill package exists and passes only when the required routing/authority surfaces exist.

- [ ] **Step 1: Write the failing test**

Create a `unittest` module that requires:

```python
SKILL = ROOT / "skills" / "loadout" / "SKILL.md"
FIELD_GUIDE = ROOT / "skills" / "loadout" / "references" / "plugin-layer-map.md"
EVAL_GUIDE = ROOT / "skills" / "loadout" / "references" / "operator-evals.md"
OPENAI = ROOT / "skills" / "loadout" / "agents" / "openai.yaml"
DEV = ROOT / "evals" / "loadout-discovery-cases.json"
HOLDOUT = ROOT / "evals" / "loadout-holdout-cases.json"
```

Assert that the skill description starts with `Use when ` and is under 500 characters, the skill body is under 500 words, the skill links both references, and these laws appear verbatim:

```text
task != tool list
capability availability != authority
discovery != invocation
missing capability != missing task
```

Assert that the OpenAI default prompt names `$loadout`, says `smallest sufficient`, and does not enumerate the plugin avalanche.

Assert both JSON catalogs use schema `loadout.operator-eval/v0`, have disjoint prompt text, unique IDs, a non-empty `must` and `must_not`, and valid `expected_bindings` arrays.

- [ ] **Step 2: Run test to verify it fails**

Run:

```bash
python3 -m unittest tests.test_loadout_skill_contract -v
```

Expected: FAIL because `skills/loadout/SKILL.md` and eval catalogs do not yet exist.

- [ ] **Step 3: Commit RED**

```bash
git add tests/test_loadout_skill_contract.py
git commit -m "test: freeze LOADOUT operator contract"
```

---

### Task 2: Add the compact LOADOUT skill surface

**Files:**
- Create: `skills/loadout/SKILL.md`
- Create: `skills/loadout/agents/openai.yaml`

**Interfaces:**
- Consumes: design laws and reference paths.
- Produces: the portable skill entrypoint and host-facing default prompt.

- [ ] **Step 1: Write minimal skill content**

The skill must contain:

```text
Bring the smallest world that can do the job.
```

and the decision cycle:

```text
CUT -> CLASSIFY -> DISCOVER -> SELECT -> FENCE -> BIND -> WORK -> RECEIPT
```

It must state that candidate lists are candidates, explicit task requirements win, LOADOUT may select none, unavailable capabilities must not be hallucinated, and router choice is not evidence or authority.

- [ ] **Step 2: Add the OpenAI interface**

Use a short description and a default prompt equivalent to:

```text
Use $loadout to choose the smallest sufficient set of currently available capabilities for this task without expanding authority.
```

- [ ] **Step 3: Run the contract test**

Run the Task 1 command. Expected: still FAIL because references/eval catalogs are not yet present.

- [ ] **Step 4: Commit the skill surface**

```bash
git add skills/loadout/SKILL.md skills/loadout/agents/openai.yaml
git commit -m "feat: add LOADOUT front door"
```

---

### Task 3: Slice the capability avalanche into functional layers

**Files:**
- Create: `skills/loadout/references/plugin-layer-map.md`
- Create: `skills/loadout/references/operator-evals.md`

**Interfaces:**
- Consumes: named capability examples from the approved design.
- Produces: detailed routing reference loaded only when needed and an evaluation/claim-boundary protocol.

- [ ] **Step 1: Write the plugin layer map**

Document six functional layers:

```text
reasoning organs
process disciplines
research and computation
workspaces and source systems
build/runtime/observability
output/design/communication/expression
```

For each layer, document the routing question, representative current names, overlap rules, and the rule that runtime availability must be discovered rather than assumed.

- [ ] **Step 2: Write the operator-eval protocol**

Define scoring dimensions for task cut, relevance, minimality, availability honesty, explicit-tool fidelity, authority fence, no epistemic laundering, graceful absence, and receipt quality. State that repository tests do not establish model-level invocation reliability.

- [ ] **Step 3: Run the contract test**

Expected: still FAIL only on missing eval catalogs.

- [ ] **Step 4: Commit references**

```bash
git add skills/loadout/references
git commit -m "docs: map LOADOUT capability layers"
```

---

### Task 4: Add routing development cases and unseen holdouts

**Files:**
- Create: `evals/loadout-discovery-cases.json`
- Create: `evals/loadout-holdout-cases.json`

**Interfaces:**
- Consumes: `loadout.operator-eval/v0` case schema.
- Produces: pressure cases usable by future fresh-agent eval runners.

- [ ] **Step 1: Add development cases**

Include at least:

- long “in case” plugin list + GitHub repo task -> bind GitHub plus only the needed development discipline;
- historical scanned-source question -> bind ALEX, not the whole research stack;
- observer-known-at question -> bind 3rdi;
- wild seed not yet making a claim -> bind HATCH/LSD only;
- academic evidence request -> scholarship route;
- explicit “use GitHub and Wolfram” request -> honor both when available;
- unavailable preferred capability -> substitute or proceed and disclose;
- simple rewrite -> bind no special capability;
- writable connector without write authorization -> preserve read-only fence;
- two agreeing tools -> do not promote agreement to independent corroboration automatically.

- [ ] **Step 2: Add holdouts**

Use different prompts covering a mixed design/build task, a current project-state lookup, a deployment request with explicit deployment authority, a generic summary that should stay ordinary, and a named-but-missing plugin.

- [ ] **Step 3: Run the contract test**

Expected: PASS.

- [ ] **Step 4: Run the full repository suite**

```bash
python3 -m unittest discover -s tests -v
```

Expected: all existing ALEX tests and the new LOADOUT contract pass.

- [ ] **Step 5: Commit eval catalogs**

```bash
git add evals/loadout-discovery-cases.json evals/loadout-holdout-cases.json
git commit -m "test: add LOADOUT routing pressure cases"
```

---

### Task 5: Review, verify, and open the hatch PR

**Files:**
- No semantic changes expected; only corrections required by review.

**Interfaces:**
- Consumes: complete branch.
- Produces: reviewable PR with explicit claim boundaries and verification evidence.

- [ ] **Step 1: Inspect the branch diff**

Confirm only the new spec, plan, LOADOUT package, eval catalogs, and LOADOUT contract test changed.

- [ ] **Step 2: Verify package size and contract**

Run:

```bash
wc -w skills/loadout/SKILL.md
python3 -m unittest tests.test_loadout_skill_contract -v
python3 -m unittest discover -s tests -v
```

- [ ] **Step 3: Open PR**

PR body must distinguish:

- what the package and repository tests demonstrate;
- what remains runtime/model-dependent;
- that ALEX semantics are unchanged;
- that the skill is portable and can later move to a dedicated repo unchanged.
