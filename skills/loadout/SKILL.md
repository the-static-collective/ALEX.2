---
name: loadout
description: Use when a task may benefit from multiple skills, plugins, connectors, tools, research engines, workspaces, or development disciplines; when a long candidate list risks overloading context; when the operator must discover what is actually available now; or when read, write, publish, send, deploy, and execution authority must remain distinct while choosing what to use.
---

# LOADOUT

> **Bring the smallest world that can do the job.**

LOADOUT is the session front door. Start from the task, discover relevant capabilities currently exposed by the host, bind only the smallest sufficient set, preserve authority, then get out of the way.

## Constitutional line

> **Knowledge may load. Capability may bind. Authority does not silently expand.**

```text
task != tool list
mention != mandatory binding
availability != relevance
capability availability != authority
discovery != invocation
read authority != write authority
missing capability != missing task
router choice != evidence
```

## Route

`CUT -> CLASSIFY -> DISCOVER -> SELECT -> FENCE -> BIND -> WORK -> RECEIPT`

1. **CUT** — Freeze the actual task, constraints, and useful stopping condition.
2. **CLASSIFY** — Ask which functional layers are needed: reasoning, process, research, workspace, runtime, expression.
3. **DISCOVER** — Check the current host for relevant capabilities. Do not infer installation from a mention, memory, or old session.
4. **SELECT** — **Explicit task requirements win. Candidate lists are candidates**, not commands. Choose the smallest sufficient set and **leave everything else asleep**. **LOADOUT may select none.**
5. **FENCE** — Keep inspect/read, mutate/write, publish/send, and deploy/execute authority separate. Capability never enlarges permission.
6. **BIND / WORK** — Hand off to the chosen organ, discipline, connector, or tool. LOADOUT should disappear unless routing changes.
7. **RECEIPT** — When material, state what was selected, omitted, unavailable, substituted, or authority-limited.

If a preferred capability is missing, use the nearest lawful substitute or proceed without it; disclose the limitation when it matters. Agreement across tools is not independent corroboration without lineage. Routing does not manufacture evidence, permission, or admission.

Read [plugin-layer-map.md](references/plugin-layer-map.md) when choosing among overlapping capabilities. Read [operator-evals.md](references/operator-evals.md) when testing or changing LOADOUT.

## Stay asleep

Do not over-route ordinary rewriting, summarization, simple chronology, or other tasks where built-in capability is sufficient.

## Scope

LOADOUT is not a persistent plugin registry, universal ontology, truth engine, or permission mint. It uses the capabilities the present host actually exposes.
