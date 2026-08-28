# LOADOUT Plugin Layer Map

> **A named capability is a door, not a destiny. Bind by role, not by brand.**

This is a cold reference for LOADOUT. Do not load the whole catalog merely because a task mentions several names. First decide what role the task needs, then discover availability in the current host.

## Availability discipline

**Discover availability at runtime. Do not assume** a skill, plugin, connector, or app exists because it was available in another session, appears in memory, was mentioned by the user, or is documented somewhere. A named capability may be installed, unavailable, renamed, duplicated, permission-limited, or better served by a native tool.

Explicit user instructions are different from an “in case” list: if the user specifically requires a named capability, honor that requirement when it is available and relevant. If it is unavailable, say so and choose the nearest lawful route rather than pretending it ran.

A capability can serve more than one layer. Classify it by the role it is performing **in this task**.

## 1. Reasoning organs

**Routing question:** Does the problem need a special way of seeing, separating, pressuring, or traversing information?

Representative organs:

- **ALEX** — source witnesses, evidence paths, deliberate hypothesis pressure, historical/source provenance, formation trace.
- **3rdi** — observer-local cuts, known-at vs occurred-at, availability, parallax, decoder changes, hindsight control.
- **HATCH / LSD** — expand a seed's nearby possibility-space without promoting the seed into evidence or truth.
- **Free Graph** — bounded relational traversal, typed relation proposals, ancestry, tests, and no-promotion graph work.
- **Novelist** — narrative formation when the task is primarily narrative rather than evidentiary.

Do not bind several reasoning organs just because they sound compatible. Use one unless the task genuinely crosses their jurisdictions or a handoff is useful.

## 2. Process disciplines

**Routing question:** Does the work itself need an execution, testing, review, improvement, or completion discipline?

Representative disciplines:

- **Superpowers** — software planning, TDD, systematic debugging, implementation, review, verification, branch completion.
- **Riqor** — controlled self-improvement, baselines, bounded interventions, holdouts, regressions, rollback.
- **PR Completion** — finishing/reviewing pull-request work when that workflow is specifically needed.
- **Develoop** — development workflow when its current host capability is available and materially distinct.

A process discipline governs *how* work is done. It is not evidence that the result is correct.

## 3. Research and computation

**Routing question:** Does the task require external scholarship, formal computation, domain retrieval, or independent research machinery?

Representative capabilities:

- **Wolfram** — formal computation and curated computational knowledge.
- **Scholar Gateway**, **Sider Scholar**, **Consensus** — scholarly literature search and synthesis, with their own source scopes.
- **BigGeo AI**, **GeoAI Skills** — spatial/geographic reasoning or real-world geodata workflows.

Prefer the smallest route that can answer the question. Multiple research engines are useful when source coverage, methodological independence, or explicit comparison matters—not merely to make the answer look more corroborated.

## 4. Workspaces and source systems

**Routing question:** Where does the user's or project's current authoritative state actually live?

Representative systems:

- **GitHub**, **GitLab** — repositories, issues, pull requests/merge requests, code and project state.
- **GitBook** — published/project documentation.
- **Google Drive**, **Dropbox** — connected files and documents.
- **Notion** — workspace knowledge, plans, pages, databases.
- **Linear** — issue/project planning state.

Use the owning workspace before reconstructing its current state from memory or public web results. Reading a workspace does not grant mutation authority.

## 5. Build, runtime, and observability

**Routing question:** What system must execute, host, deploy, instrument, message, or expose the software?

Representative systems:

- **Supabase** — database, auth, storage, realtime, edge/runtime services.
- **Vercel**, **Cloudflare** — deployment, hosting, domains, edge/runtime infrastructure.
- **PostHog** — product analytics, experiments, logs, observability.
- **Twilio Developer Kit** — communications/runtime integration where exposed.
- **NaCl**, **pstack** — specialized runtime/security/development capabilities when currently available.

Separate `can deploy` from `authorized to deploy`, and `can send` from `authorized to send`. Runtime access never manufactures project authority.

## 6. Output, design, communication, and expression

**Routing question:** What form should the finished result take, and does it need to be designed, transformed, communicated, or published?

Representative capabilities:

- **Canva**, **Figma**, **Visualize** — visual/design output.
- **Spreadsheets** — structured tabular artifacts and analysis.
- **Socializioz** — social publishing workflow where authorized.
- **HumanWriting**, **Plain Language** — writing/transformation disciplines when available.
- **Creator Workspace** — creator-oriented output workflow when currently exposed.

Do not wake the expression layer before the content or project state is ready unless design itself is the task.

## Overlap rules

Use these tie-breakers:

1. **Owning state beats remembered state.** If the question is about a repo, calendar, document, deployment, issue tracker, or analytics property, inspect its owner when available.
2. **Specialized reasoning only when it changes the cut.** ALEX, 3rdi, HATCH, and Free Graph should not become decorative prefixes.
3. **Native/simple beats orchestration.** A built-in calculator, straightforward rewrite, or ordinary summary may need no special binding.
4. **Explicit user requirement beats optimization.** “Use GitHub and Wolfram” means try both; “here are all my tools in case” does not.
5. **Independence must be earned.** Two tools agreeing is not independent corroboration without lineage/source analysis.
6. **Missing capability is recoverable.** Substitute lawfully, continue without it, or expose the capability gap. Never hallucinate a successful invocation.

## Authority fence

For any selected capability, keep these coordinates distinct:

```yaml
read: allowed | ask | unavailable
write: allowed | ask | unavailable
publish_or_send: allowed | ask | unavailable
deploy_or_execute: allowed | ask | unavailable
```

The strongest available tool does not enlarge the fence. LOADOUT carries attributable authority; it does not mint it.
