# LOADOUT Front Door — Smallest-Sufficient Session Router v0

**Date:** 2026-08-27  
**Status:** approved architecture; implementation target  
**Owning repo:** `the-static-collective/ALEX.2` (portable package may later move unchanged)

> **Bring the smallest world that can do the job.**

LOADOUT is the single front door for a session that may have many skills, plugins, connectors, development disciplines, research engines, and project runtimes available. The human should not need to remember which named capability to mention. LOADOUT discovers what is available, chooses the smallest sufficient set for the actual task, preserves authority boundaries, and leaves everything else asleep.

This extends the existing ALEX × LOADOUT boundary without merging their jurisdictions:

> **LOADOUT compiles the means. ALEX accounts for meaning. Neither admits consequence.**

## 1. Problem

A long `@tool @tool @tool` list creates an ambiguous routing surface. Names in the list may be:

- reasoning organs or methods;
- process disciplines;
- research/computation capabilities;
- connected workspaces and source systems;
- build/runtime services;
- presentation, communication, or writing capabilities;
- unavailable, renamed, duplicated, or session-specific entries.

Treating that list as “load everything” wastes context and can cause bad routing. Treating every name as equivalent collapses instruction, capability, evidence, and authority.

## 2. Constitutional laws

```text
task != tool list
mention != mandatory binding
availability != relevance
relevance != necessity
capability availability != authority
discovery != invocation
read authority != write authority
write authority != publish/deploy/send authority
router choice != evidence
plugin output != owning-world admission
missing capability != missing task
```

And the existing LOADOUT law remains:

> **Knowledge may load. Capability may bind. Authority does not silently expand.**

## 3. One front door

When LOADOUT is invoked, start from the user's task rather than the candidate list.

```text
TASK
  -> CUT        freeze the actual problem and stopping condition
  -> CLASSIFY   identify what kinds of help are needed
  -> DISCOVER   determine which relevant capabilities actually exist now
  -> SELECT     choose the smallest sufficient set
  -> FENCE      preserve read/write/publish/deploy/send authority boundaries
  -> BIND       wake only selected capabilities
  -> WORK       hand off to the selected organ/tool/discipline
  -> RECEIPT    say what was used, omitted, unavailable, and why when material
```

LOADOUT is allowed to select **none**. Ordinary tasks should stay ordinary.

## 4. Capability layers

The layer map is functional, not ontological. A named product can serve more than one layer; classify it by the role needed in this task.

### A. Reasoning organs

Static methods that change how the problem is examined.

Examples: `ALEX`, `3rdi`, `HATCH/LSD`, `Free Graph`.

- ALEX: source witness, evidence, pressure, formation trace.
- 3rdi: observer-local cuts, parallax, decoder/availability/hindsight discipline.
- HATCH/LSD: non-promotional divergence and possibility-space expansion.
- Free Graph: bounded relational traversal and typed relation proposals.

### B. Process disciplines

Methods governing how work is executed or verified rather than what is believed.

Examples: `Superpowers`, `Riqor`, `PR Completion`.

### C. Research and computation

External engines that can answer, calculate, search scholarship, or perform domain analysis.

Examples: `Wolfram`, `Scholar Gateway`, `Sider Scholar`, `Consensus`, `BigGeo AI`, `GeoAI Skills`.

### D. Workspaces and source systems

Places where project/user material lives and where current state may be read or changed.

Examples: `GitHub`, `GitLab`, `GitBook`, `Google Drive`, `Dropbox`, `Notion`, `Linear`.

### E. Build, runtime, and observability

Systems that host, execute, deploy, instrument, or operate software.

Examples: `Supabase`, `Vercel`, `Cloudflare`, `PostHog`, `Twilio Developer Kit`, `NaCl`, `pstack`.

### F. Output, design, communication, and expression

Capabilities that transform or publish the result.

Examples: `Canva`, `Figma`, `Visualize`, `Spreadsheets`, `Socializioz`, `HumanWriting`, `Plain Language`, `Creator Workspace`.

## 5. Selection rules

1. **Explicit task requirement wins.** If the user says “check GitHub,” GitHub is not optional if available.
2. **Candidate lists are candidates, not commands.** A long list supplied “in case” does not wake all entries.
3. **Smallest sufficient set.** Prefer one capable route over several overlapping routes unless independence, comparison, or redundancy is materially useful.
4. **Use native/current capability discovery.** Never claim a named plugin is installed or callable without current evidence when that matters.
5. **Graceful absence.** If a preferred capability is missing, choose the nearest lawful substitute or proceed without it; state the limitation when material.
6. **No authority laundering.** A connector being writable does not imply authorization to write. A gate result does not itself perform the side effect.
7. **No epistemic laundering.** Tool choice, recurrence across tools, or multiple outputs do not become independent evidence without lineage analysis.
8. **Route then disappear.** LOADOUT should not continue narrating itself unless routing, authority, or capability availability becomes material again.

## 6. Default routing heuristics

- Strange/open seed with no claim yet -> HATCH/LSD.
- Historical/source/provenance or deliberate hypothesis pressure -> ALEX.
- Observer/known-at/availability/decoder/hindsight question -> 3rdi.
- Typed relation neighborhood, ancestry, or bounded traversal -> Free Graph.
- Code change or debugging -> appropriate development discipline plus project source/runtime tools.
- Academic evidence question -> scholarship route, with ALEX only if source-witness provenance is material.
- Calculation/formal computation -> Wolfram or native calculator route.
- Project state question -> owning workspace first.
- Publication/design/output task -> expression layer only after content/state is ready.

These are defaults, not exclusive ownership claims.

## 7. Authority fence

LOADOUT must track at least:

```yaml
read: allowed | ask | unavailable
write: allowed | ask | unavailable
publish_or_send: allowed | ask | unavailable
deploy_or_execute: allowed | ask | unavailable
```

A stronger capability does not enlarge the fence. Explicit user authorization and owning-system policy remain controlling.

## 8. Portable skill package

Create `skills/loadout/` with:

- compact trigger-first `SKILL.md`;
- `agents/openai.yaml`;
- `references/plugin-layer-map.md` for the detailed functional taxonomy and routing heuristics;
- `references/operator-evals.md` for evaluation protocol and claim boundaries.

Add development and holdout routing cases plus repository contract tests. No production runtime is required for v0; the skill is a decision instrument that uses whatever capabilities the current host actually exposes.

## 9. Acceptance

The v0 hatch is acceptable when:

- the loaded skill surface is under 500 words and does not enumerate the whole avalanche;
- discovery description contains triggers only;
- the skill makes “smallest sufficient / everything else asleep” explicit;
- capability availability and authority are visibly distinct;
- explicit user-requested tools are honored when available;
- candidate-list overload cases select a small set rather than all candidates;
- missing-capability cases degrade without hallucinating availability;
- negative cases demonstrate that LOADOUT may select no special capability;
- holdout prompts are disjoint from development prompts;
- existing ALEX tests remain green;
- no ALEX research semantics are changed.

## 10. Claim boundary

Repository tests can prove package structure, routing-contract coverage, and semantic non-collapse in the written skill. They do **not** prove universal automatic invocation, cross-model behavior, or that every external capability will remain installed. Those require fresh-agent/runtime evaluation in the actual host.
