# ALEX-MOTIF-021 — Source custody evidence and research packet

A saved **bounded ALEX-style local full-file exact-phrase search** over five public pinned source document copies. The adapter under `tools/motif021-search.mjs` verifies each original Git blob SHA-1 before scanning every line, retains exact file/line references and an explicit observation footprint with truncation. It writes no external sources.

**Search scope:** MOTIF-019/020 design, current public ALEX research method, planZ README and GRAFT README at exact source commits. These snapshots are for public-source method research, **not evidence that real witnesses are independent or that any private source may be exported**.

See `research-packet.json` for the actual persisted machine-readable packet and `source-manifest.json` for source custody. `research-packet.json` is a bounded reproducible discovery receipt, not a conclusion about source ancestry. The sources are full pinned public Markdown file copies, but coverage is **PARTIAL** because unmaterialized repository paths, later changes, private repositories, and underlying human evidence were not searched.

Run with Node 20+: `node tools/motif021-search.mjs`, and `node --test test/motif021-search.test.mjs`.

**Proposed handoff:** planZ receives an exact copied packet in its own draft branch, computes a reviewable classical plan, and GRAFT composes a bounded executable public-source packet analyzer. Source-owner custody and external effects stay separate.
