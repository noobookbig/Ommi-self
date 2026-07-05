# Template

Canonical Template package for the Ommi-self forecasting workflow.

This directory contains **structure only** — no numerology, no interpretation, no business
logic. Meaning is filled in by downstream agents (MET-447-B/C/D).

## Files

| File | Purpose |
|---|---|
| `forecast.md` | Markdown source template. Author your forecast here, replacing `{{tokens}}` with real per-person values. |
| `forecast-template.html` | Single-page HTML wrapper. Inline `<style>`, inline mermaid init, vendored mermaid runtime. |
| `vendor/mermaid.min.js` | Mermaid v10.9.1 runtime, bundled locally so the wrapper is **offline-clean** (no CDN dependency at render time). Google Fonts still loads over the network for `Kanit` + `Inter`; if needed, swap to system fonts by deleting the `<link>` lines in the wrapper. |

## How to author a new forecast

1. Copy `forecast.md` to your forecast folder (typically `analysis/<person-slug>.md`).
2. Open the copy and replace every `{{token}}`:
   - identity tokens: `{{person_name}}`, `{{dob}}`, `{{person_year_start}}`, `{{person_year_end}}`, `{{headline_reading}}`, `{{summary_paragraph}}`
   - career-year tokens: `{{career_year_1}}` … `{{career_year_5}}` + matching `{{career_year_N_label}}`
   - health-card tokens: `{{hc_1_phys}}`, `{{hc_1_eng}}`, `{{hc_1_emo}}` … `{{hc_result_emo}}`
   - meta tokens: `{{template_version}}`, `{{generated_at}}`
3. Update the mermaid block(s) in the .md with the computed slot values (eight-spoke radial + matrix table).
4. Open `forecast-template.html`, replace the same tokens in the HTML body, and update the inline mermaid source in the `.mermaid` divs to match the .md.
5. Open the .html in a browser to render. Mermaid init runs on `DOMContentLoaded`.

## Theme palette

Hex values are documented in the comment block at the top of `forecast-template.html`:

| Token | Hex | Role |
|---|---|---|
| `--bg` | `#32dbfc` | page gradient start (cyan, top-left of JPG ref) |
| `--bg-soft` | `#e6f8ff` | card surface |
| `--fg` | `#1a1a2e` | body text |
| `--accent-1` | `#8a2be2` | accent 1 — slot 1 + slot 8 (deep purple) |
| `--accent-2` | `#4169e1` | accent 2 — slot 2 (royal blue) |
| `--accent-3` | `#20b2aa` | accent 3 — slot 3 (teal) |
| `--accent-4` | `#9acd32` | accent 4 — slot 4 (lime) |
| `--accent-5` | `#ffd700` | accent 5 — slot 5 (gold) |
| `--accent-6` | `#ff8c00` | accent 6 — slot 6 (orange) |
| `--accent-7` | `#dc143c` | accent 7 — slot 7 (crimson) |
| `--accent-magenta` | `#f63375` | magenta highlight (corner accent from JPG) |

Palette was sampled from
`paperclip-storage/issues/MET-447/2026/07/05/...-1783225172954.jpg` (Cloudly SaaS landing
template) and additionally drawn from the eight-slot color wheel that the reference PDF uses.

## Single-page layout

`forecast-template.html` uses a CSS grid (`1fr 1fr`) with `gap: 18px 22px` on a max-width
`1280px` page. The page is sized to fit ≤ 110vh on a desktop browser at 1280px width so
the deliverable renders as a single page without scroll chrome (per acceptance criterion).

## Acceptance criteria mapping

| Criterion | Where |
|---|---|
| Section-0 summary, eight-spoke layout, matrix, career-year list, health card | `forecast.md` §0–§4 and matching `<section class="card">` blocks in the HTML wrapper |
| 1-page render on 1280px desktop | `.page` grid + `@media (min-width: 1024px)` rules |
| Inline `<style>` only | `<style>` block inside `<head>`, no external `.css` link |
| Google font via `<link>` only | `fonts.googleapis.com` link in `<head>` (Kanit headings, Inter body) |
| Eight-spoke layout matches PDF structure | 8 numbered slots (`S1`–`S8`) around central node `C`, joined hub-and-spoke + outer ring |
| Palette documented as CSS custom properties | comment block at top of HTML + `:root` in `<style>` |
| No frameworks; only mermaid runtime + minimal DOMContentLoaded init | one `<script src="vendor/mermaid.min.js">` + one inline `DOMContentLoaded` listener |
| No business logic in template | only `{{tokens}}` placeholders; the .md and .html carry structure, not meaning |

## Versioning

`{{template_version}}` is a placeholder. Bump it when the section list, palette, or layout
changes in a backward-incompatible way.