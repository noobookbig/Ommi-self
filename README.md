# Ommi-self

> **Multidimensional Forecasting System** — integrating Jungian psychology (MBTI / Carl
> Jung), The Kybalion, Matrix of Destiny, and Sumerian cosmology into a single
> "life navigation map" for individuals navigating the Period-9 transition (2024–2043).

This repository is the canonical home for the Ommi-self forecasting project. It contains
the canonical Template package, the deterministic utility-math library used to feed the
forecasting agents, the agent-authored analysis outputs, and the human-readable
deliverables that ship to the end user.

## Folder map

| Folder | Purpose | Owner |
|---|---|---|
| [`template/`](./template/) | Canonical forecast Template — `forecast.md` source, `forecast-template.html` single-page wrapper (Kanit + Inter, vendored Mermaid v10.9.1, inline CSS), `vendor/mermaid.min.js` for offline rendering, `README.md` usage doc. **Structure only — no numerology / tarot / chakra / octagram interpretation lives here.** | CTO (template owner) |
| [`code/`](./code/) | Deterministic utility math in C# (.NET 8 class library `Ommi.Calc` + xUnit `Ommi.Calc.Tests`). Pure arithmetic only — age from DOB (years + months + days, not just year integer), day-of-year, personal-year reduction, matrix reduction, day-of-period arithmetic. **No interpretive logic per project policy.** | CTO (code owner) |
| [`analysis/`](./analysis/) | Per-person forecast analyses written by domain agents (Carl Jung, Isabel Briggs Myers, Helena Blavatsky, Three Initiates, นาตาเลีย ลาดินี, Su Yu Hong). Long-form Markdown, always grounded in numbers produced by `Ommi.Calc`. May include hypothetical scenarios (career, organisation, world events) to make the reading actionable. | Domain agents |
| [`deliver/`](./deliver/) | Final user-facing deliverables — one `.md`, one `.html` (single-page, inline styles, embedded Mermaid), and one `.pdf` per forecast. The Thai Writer consolidates everything into one easy-to-read page, then Thai Reviewer + QA verify before ship. | Thai Writer (consolidation) → Thai Reviewer + QA (verification) |

## Policy references

- **MET-394 · STANDARD.md** — *No code-based numerology/tarot/chakra/octagram
  interpretation.* Code contains pure utility math only; all meaning comes from
  agents. The `code/` module is therefore deliberately boring arithmetic; the
  interesting work happens in `analysis/` and `deliver/`.
- **MET-447** — the parent issue that spawned this repository. Defines the
  canonical Template (MET-447-A), the folder skeleton + utility math
  (MET-447-B), the git remote + initial push (MET-447-C, this README), and the
  QA + Thai-Reviewer verification gate (MET-447-D).

## Contributor flow

```
                ┌──────────────────────────────────────┐
                │  CTO (builds template + utility math)│
                └────────────┬─────────────────────────┘
                             │  canonical Template + .NET utility
                             ▼
   ┌─────────────────────────────────────────────────────────┐
   │ Domain agents (Carl Jung, MBTI, Kybalion,               │
   │ Matrix of Destiny, Sumerian) — write analysis/*.md      │
   │ grounded in numbers from Ommi.Calc                       │
   └────────────────────┬────────────────────────────────────┘
                        │  per-person analysis .md
                        ▼
   ┌─────────────────────────────────────────────────────────┐
   │ Thai Writer — consolidates analyses + template into     │
   │ a single readable deliver/forecast.{md,html,pdf} page   │
   └────────────────────┬────────────────────────────────────┘
                        │  consolidated deliverable
                        ▼
   ┌─────────────────────────────────────────────────────────┐
   │ Thai Reviewer + QA — final verification before ship     │
   └─────────────────────────────────────────────────────────┘
```

Strict ordering: build → analyze → consolidate → review. No agent skips a stage,
and no stage emits work into the next stage's folder.

## Tooling

- **C# / .NET 8** — utility math, xUnit tests. Build with `dotnet build` in
  `code/`; run tests with `dotnet test`.
- **Mermaid v10.9.1** — octagram and matrix diagrams. The runtime is vendored
  at `template/vendor/mermaid.min.js` so the HTML wrapper renders offline.
- **Google Fonts (Kanit + Inter)** — loaded via `<link>` only in
  `forecast-template.html`. To render fully offline, delete those two `<link>`
  lines and the wrapper falls back to system sans-serif.

## Build artifacts

The `.gitignore` excludes `bin/`, `obj/`, `node_modules/`, `*.user`,
`*.suo`, `.vs/`, `.vscode/`, `.idea/`, `.DS_Store`, `Thumbs.db`, and `*.log`.

## How to read this repo

1. Start with [`template/README.md`](./template/README.md) to understand the
   canonical Template structure and palette.
2. Read [`code/README.md`](./code/README.md) for the utility-math contract and
   the "no interpretation" rule.
3. Open any forecast in `analysis/` and the matching `deliver/` to see the
   end-to-end flow.

## License

Internal project — not yet licensed for redistribution.