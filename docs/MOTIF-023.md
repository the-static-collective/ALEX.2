# ALEX-023 — Open question field / live public source collections

A bounded, new-question **public GitHub source discovery** adapter owned by ALEX. It can select among five predeclared and currently public repository collections: MOTIF, ALEX.2, planZ, GRAFT and the-daily-slice. The source collection can be explicitly selected from that public allowlist or routed by question terms. Private repositories, including MEMENTO, are **not on the allowlist**.

Unlike ALEX-021/022's five frozen documents, it fetches a verified PUBLIC repository's **current default branch head**, resolves its immutable commit tree, checks tree completeness, selects at most two small eligible Markdown files per repo, fetches each by immutable Git blob SHA, independently recomputes the Git blob hash and returns source/commit/path/line-located search leads. It records incomplete coverage. A fetch failure or unsupported question holds; missing matches do not prove absence. Read-only API operations use a fixed https://api.github.com host.

It is not a universal ALEX crawler, not a private connector, not verified independent human evidence, not permission to redistribute private records, and not source authority. The CI includes mock transport tests for remote privacy and integrity failures plus a **real GitHub API** fetch that must produce an actual source-scope packet before passing.

```sh
node --test test/motif023-live.test.mjs
GITHUB_TOKEN=... node tools/motif023-live.mjs "Which original Maxhinal Fiber and Pressure chambers preserve source custody?"
```

GitHub Actions can supply an ephemeral read-only token; no token is embedded in the research receipt. A user may also run it anonymously subject to public GitHub API limits.
