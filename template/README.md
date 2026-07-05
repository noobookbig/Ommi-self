# Template

Canonical Template package for the Ommi-self forecasting workflow.

This directory contains **structure only** — no numerology, no interpretation, no business
logic. Meaning is filled in by downstream agents (MET-447-B/C/D).

> Updated in **MET-458** — the skeleton now spans the full **10 sections** of Project
> Omni-Self Forecast. Section 0 (summary) is preserved as the umbrella; Sections 1–10
> mirror the canonical Output Structure (MET-457).
>
> Updated in **MET-461-A** — added **บทวิเคราะห์เชิงลึก — Deep Dive** block under each
> section's existing 6-lens analysis. 121 new `analysis_deep_<sec>_<lens>_<topic>`
> placeholders (10 sections × 6 lenses × ~2 topics each). HTML renders these as
> `.lens-card` elements inside a `.lens-deep` block. **Placeholders only** — the
> analyst fills in actual analysis per user.
>
> Updated in **MET-461-B** — §1 Cosmic Synergy gained an **Octagram** diagram
> (Monad center + 8 cosmic forces around an octagonal ring). 9 new `{{octagram_*}}`
> placeholders.
>
> Updated in **MET-457-A** — each section now ends with a **บทวิเคราะห์ (Analysis —
> 6 Lenses)** block: the same data re-read through six expert traditions
> (Carl Jung / Isabel Briggs Myers / Helena Blavatsky / Natalia Ladini / The Three
> Initiates / Su Yu Hong). 60 new `analysis_<n>_<expert>` tokens total.

## Files

| File | Purpose |
|---|---|
| `forecast.md` | Markdown source template — **10-section skeleton** (§0 umbrella summary + §1..§9, mapping 1:1 to MET-457's ส่วนที่ 1..10). Replace `{{tokens}}` with real per-person values. |
| `forecast-template.html` | Single-page HTML wrapper. Inline `<style>`, inline mermaid init, vendored mermaid runtime. Mirrors the 10-section layout as a single renderable page. |
| `vendor/mermaid.min.js` | Mermaid v10.9.1 runtime, bundled locally so the wrapper is **offline-clean** (no CDN dependency at render time). Google Fonts still loads over the network for `Kanit` + `Inter`; if needed, swap to system fonts by deleting the `<link>` lines in the wrapper. |

## 10-section skeleton (Project Omni-Self Forecast)

| § (template) | Section title | Anchor | Primary discipline | Maps to MET-457 ส่วนที่ |
|---|---|---|---|---|
| Header | ข้อมูลผู้รับคำพยากรณ์ | Identity metadata | inputs | (input) |
| §0 | บทสรุป 6 มุมมองเชิงลึก (The 6 Lenses) | Jung / LOA / Kybalion / MBTI / Age 60 / BaZi | 6 disciplines | ส่วนที่ 1 |
| §1 | จุดเชื่อมโยงแห่งปรัชญาและวัฏจักร (The Cosmic Synergy) | Kybalion ↔ LOA ↔ Matrix loop | convergence | ส่วนที่ 2 |
| §2 | โปรแกรมชีวิตและแกนหลัก (Natalia Square 3×3) | Top / Middle / Bottom axis + Echo | Matrix of Destiny | ส่วนที่ 3 |
| §3 | พรสวรรค์ ศักยภาพ และอดีตชาติ (Talent + Karmic Tail) | Core gift + Karmic tail | Identity & past | ส่วนที่ 4 |
| §4 | การเงิน ความสำเร็จ และบทบาทเชิงลึก (Career + Roles) | Industry + Boss/Sub/Active/Receptive | career | ส่วนที่ 5 |
| §5 | สายสัมพันธ์ ความรัก และครอบครัว (Relationships + Lineage) | Inner circle + Paternal/Maternal | relationships | ส่วนที่ 6 |
| §6 | สุขภาพและจุดอ่อน (Health Card & Chakras) | 7-chakra table (Crown→Root) | health | ส่วนที่ 7 |
| §7 | ไทม์ไลน์ 5 ช่วงวัย + พยากรณ์รายปี (Timeline + Year-by-Year) | 5 stages + year-by-year → 60 | timeline | ส่วนที่ 8 |
| §8 | คำแนะนำและแนวทางปฏิบัติ (Actionable Protocols) | Daily / Weekly / Monthly + Crisis 5-step | protocols | ส่วนที่ 9 |
| §9 | บทสรุปแห่งสัจธรรม (The Ultimate Synthesis) | Interconnectedness + Ultimate Truth | final synthesis | ส่วนที่ 10 |

> The template uses §0..§9 internally so the umbrella summary (§0 = the 6-lens reading)
> precedes the spec's ส่วนที่ 1. The mapping above is 1:1 with the parent MET-457
> Output Structure.

## Token catalog (complete, 10-section)

> Every token below is a placeholder. The list is intentionally exhaustive so any
> downstream agent can locate the right one by section. `*_short` variants are 1-line
> labels intended for cards/charts; the un-suffixed tokens carry full sentences.

### Header tokens

- Identity: `{{person_name}}`, `{{dob}}`, `{{personality_type}}`, `{{day_master}}`, `{{matrix_core}}`
- Window & headline: `{{person_year_start}}`, `{{person_year_end}}`, `{{headline_reading}}`

### §0 — 6 Lenses (umbrella summary)

- 6-lens reading sentences: `{{lens_jung_persona}}`, `{{lens_jung_shadow}}` — combined as `{{lens_jung}}`
- `{{lens_law_of_attraction_freq}}` (combined as `{{lens_law_of_attraction}}`)
- `{{lens_kybalion_rhythm}}`, `{{lens_kybalion_cause}}` (combined as `{{lens_kybalion}}`)
- `{{lens_mbti_type}}`, `{{lens_mbti_lead}}`, `{{lens_mbti_grip}}` (combined as `{{lens_mbti}}`)
- `{{lens_age60_role}}`, `{{lens_age60_target}}` (combined as `{{lens_age_60}}`)
- `{{lens_bazi_day_master}}`, `{{lens_bazi_balance}}`, `{{lens_bazi_period9_fit}}` (combined as `{{lens_bazi}}`)
- Aggregate body: `{{summary_paragraph}}` (≤ 300 คำ — used in §0 of .html and as overall glue paragraph)

### §1 — Cosmic Synergy

- `{{synergy_kybalion}}`, `{{synergy_loa}}`, `{{synergy_matrix}}`, `{{synergy_proof}}`

### §2 — Natalia Square 3×3

- 3×3 cells (9): `{{natalia_A}}` … `{{natalia_I}}`
- Center: `{{natalia_center}}`
- Axes: `{{natalia_top_axis_value}}`, `{{natalia_top_token}}`, `{{natalia_mid_cycle}}`, `{{natalia_mid_token}}`, `{{natalia_base_drive}}`, `{{natalia_base_mask}}`
- Echo: `{{natalia_echo_numbers}}`, `{{natalia_echo_influence}}`

### §3 — Talent & Karma

- Talent: `{{talent_primary}}`, `{{talent_latent}}`
- Karmic: `{{karmic_pattern}}`, `{{karmic_lesson}}`

### §4 — Career & Roles (no current-job reference)

- `{{career_industry}}`, `{{career_income_pattern}}`, `{{career_peak_window}}`
- Roles: `{{role_boss}}`, `{{role_sub}}`, `{{role_active}}`, `{{role_receptive}}` (+ `{{role_*_token}}` chart labels)

### §5 — Relationships + Lineage

- Love: `{{love_pattern}}`, `{{love_pull}}`, `{{love_blind_spot}}`
- Lineage: `{{line_father}}`, `{{line_mother}}`

### §6 — Health Card & Chakras

- 7-chakra × 3-axis: `{{hc_1_phys}}` … `{{hc_7_emo}}`
- Zone value: `{{hc_result_phys}}`, `{{hc_result_eng}}`, `{{hc_result_emo}}`
- Watch & balance: `{{health_watch}}`, `{{health_balance}}`

### §7 — Timeline + Year-by-Year Forecast (อายุปัจจุบัน → 60)

- 5 Stages of Evolution: `{{stage_1_theme}}` … `{{stage_5_theme}}` (+ `{{stage_*_marker}}`)
- Year rows: `{{career_year_N}}`, `{{career_year_N_age}}`, `{{career_year_N_energy}}`, `{{career_year_N_situation}}`, `{{career_year_N_strategy}}` (for `N = 1..5` scaffold — agent expands to age 60 per person)

### §8 — Actionable Protocols

- Cadence: `{{protocol_daily}}`, `{{protocol_weekly}}`, `{{protocol_monthly}}`
- Crisis: `{{protocol_crisis}}`

### §9 — Ultimate Synthesis

- `{{synthesis_interconnectedness}}`, `{{synthesis_ultimate_truth}}`

### Meta

- `{{template_version}}`, `{{generated_at}}`

### บทวิเคราะห์ — 6 Lenses (per-section, 60 tokens)

> Added in **MET-457-A** in response to reviewer feedback ("ขาดบทวิเคราะห์ที่
> มองผ่านมุมต่างๆ"). Every section §0..§9 carries an **analysis block** at the
> bottom — a tight 3×2 grid showing the same data read through six expert lenses.
> Each entry is a short interpretation (~10–15 words) that names what *that*
> tradition catches that the others miss.
>
> Token schema: `analysis_<section>_<expert_short>`, where:
> - `<section>` = `0..9` (matches the section number)
> - `<expert_short>` = one of:
>   - `jung` — **Carl Jung** (Analytical Psychology)
>   - `myers` — **Isabel Briggs Myers** (MBTI)
>   - `blavatsky` — **Helena Blavatsky** (Law of Attraction / Theosophy)
>   - `ladini` — **นาตาเลีย ลาดินี** (Natalia Ladini, Matrix of Destiny)
>   - `initiates` — **The Three Initiates** (The Kybalion)
>   - `suyuhong` — **Su Yu Hong** (BaZi & Period 9)
>
> In the HTML, the analysis block uses class `.analysis` with 3-col grid + ellipsis;
> in the .md, each section ends with a `### บทวิเคราะห์ (Analysis — 6 Lenses)` table.

| Section | Tokens (6 each) |
|---|---|
| §0 Summary | `analysis_0_jung`, `analysis_0_myers`, `analysis_0_blavatsky`, `analysis_0_ladini`, `analysis_0_initiates`, `analysis_0_suyuhong` |
| §1 Cosmic Synergy | `analysis_1_jung`, `analysis_1_myers`, `analysis_1_blavatsky`, `analysis_1_ladini`, `analysis_1_initiates`, `analysis_1_suyuhong` |
| §2 Natalia Square 3×3 | `analysis_2_jung`, `analysis_2_myers`, `analysis_2_blavatsky`, `analysis_2_ladini`, `analysis_2_initiates`, `analysis_2_suyuhong` |
| §3 Talent & Karma | `analysis_3_jung`, `analysis_3_myers`, `analysis_3_blavatsky`, `analysis_3_ladini`, `analysis_3_initiates`, `analysis_3_suyuhong` |
| §4 Career & Roles | `analysis_4_jung`, `analysis_4_myers`, `analysis_4_blavatsky`, `analysis_4_ladini`, `analysis_4_initiates`, `analysis_4_suyuhong` |
| §5 Relationships + Lineage | `analysis_5_jung`, `analysis_5_myers`, `analysis_5_blavatsky`, `analysis_5_ladini`, `analysis_5_initiates`, `analysis_5_suyuhong` |
| §6 Health & Chakras | `analysis_6_jung`, `analysis_6_myers`, `analysis_6_blavatsky`, `analysis_6_ladini`, `analysis_6_initiates`, `analysis_6_suyuhong` |
| §7 Timeline + Year-by-Year | `analysis_7_jung`, `analysis_7_myers`, `analysis_7_blavatsky`, `analysis_7_ladini`, `analysis_7_initiates`, `analysis_7_suyuhong` |
| §8 Protocols | `analysis_8_jung`, `analysis_8_myers`, `analysis_8_blavatsky`, `analysis_8_ladini`, `analysis_8_initiates`, `analysis_8_suyuhong` |
| §9 Ultimate Synthesis | `analysis_9_jung`, `analysis_9_myers`, `analysis_9_blavatsky`, `analysis_9_ladini`, `analysis_9_initiates`, `analysis_9_suyuhong` |

**Total: 60 analysis tokens** (10 sections × 6 experts). Each entry is rendered as
`<expert-name>: <short reading>` in a 3-column compact row.

### บทวิเคราะห์เชิงลึก — Deep Dive (per-section, 121 tokens)

> Long-form analysis per expert lens, per section. Each topic is its own placeholder —
> analysts fill in the actual reading per user. **This is the canonical analysis surface**;
> the compact `analysis_<n>_<lens>` tokens above are short summaries.
>
> Token schema: `analysis_deep_<section>_<lens_short>_<topic>`
> - `<section>` = `0..9` (matches section number)
> - `<lens_short>` = `jung` | `myers` | `blavatsky` | `ladini` | `initiators` | `suyuhong`
> - `<topic>` = per-section, per-lens topic slug (e.g. `persona_shadow`, `initiate_path`)
>
> HTML renders each topic as `<p><strong>Heading:</strong> {{token}}</p>` inside a `.lens-card`
> element with neon border + glow, grouped under a `.lens-deep` block per section.

| Section | Topics per section | Total tokens |
|---|---|---|
| §0 Summary | 2 each | 12 |
| §1 Cosmic Synergy | 2-3 each | 13 |
| §2 Natalia Square | 2 each | 12 |
| §3 Talent & Karmic | 2 each | 12 |
| §4 Career & Roles | 2 each | 12 |
| §5 Relationships | 2 each | 12 |
| §6 Health & Chakras | 2 each | 12 |
| §7 Life Stages | 2 each | 12 |
| §8 Protocols | 2 each | 12 |
| §9 Ultimate Synthesis | 2 each | 12 |

**Total: 121 deep-analysis tokens.**

### Octagram (cosmic forces, 9 tokens)

§1 Cosmic Synergy carries an octagram — Monad at center, 8 cosmic forces around the
octagonal ring. Mermaid TD-layout.

- Center: `{{octagram_center}}`
- 8 directions: `{{octagram_n}}`, `{{octagram_ne}}`, `{{octagram_e}}`, `{{octagram_se}}`,
  `{{octagram_s}}`, `{{octagram_sw}}`, `{{octagram_w}}`, `{{octagram_nw}}`


## How to author a new forecast

1. Copy `forecast.md` to your forecast folder (typically `analysis/<person-slug>.md`).
2. Open the copy and replace every `{{token}}` from the catalog above.
3. Update the mermaid block(s) in the .md with the computed slot values (10 sections,
   plus inline diagrams per section).
4. Open `forecast-template.html`, replace the same tokens in the HTML body, and update
   each inline mermaid source in the `.mermaid` div to match the .md.
5. Open the .html in a browser to render. Mermaid init runs on `DOMContentLoaded`.

## Theme palette

Hex values are documented in the comment block at the top of `forecast-template.html`:

| Token | Hex | Role |
|---|---|---|
| `--bg` | `#32dbfc` | page gradient start (cyan, top-left of JPG ref) |
| `--bg-soft` | `#e6f8ff` | card surface |
| `--fg` | `#1a1a2e` | body text |
| `--accent-1` | `#8a2be2` | §0 (umbrella/6 Lenses) + brand accents (deep purple) |
| `--accent-2` | `#4169e1` | §1 (Cosmic Synergy) — royal blue |
| `--accent-3` | `#20b2aa` | §2 (Natalia Square) — teal |
| `--accent-4` | `#9acd32` | §3 (Talent & Karma) — lime |
| `--accent-5` | `#ffd700` | §4 (Career & Roles) — gold |
| `--accent-6` | `#ff8c00` | §5 (Relationships) — orange |
| `--accent-7` | `#dc143c` | §6 (Health & Chakras) — crimson |
| `--accent-8` | `#f63375` | §7 (Timeline & Year-by-Year) — magenta |
| `--accent-9` | `#1a1a2e` | §8 (Protocols) — deep ink |
| (slate reuse) | `#4a4a6a` | §9 (Ultimate Synthesis) — slate (currently rendered in ink for visual closure) |
| `--accent-magenta` | `#f63375` | magenta highlight (corner accent from JPG) |

Palette was sampled from
`paperclip-storage/issues/MET-447/2026/07/05/...-1783225172954.jpg` (Cloudly SaaS landing
template) and extended to 10 sections by adding `--accent-8`/`--accent-9`/`--accent-10`.

## Single-page layout

`forecast-template.html` uses a CSS grid (`1fr 1fr`) with `gap: 3px 6px` on a max-width
`1280px` page, sized so the deliverable renders as a single page without scroll chrome on
a desktop browser at 1280px width (per the original MET-447 acceptance criterion).
Sections §0 (umbrella), §7 (timeline + year-by-year) use the full row (`.card.full`);
the rest are paired cards (one text-heavy + one diagram).

## Acceptance criteria mapping

## Acceptance criteria mapping

| Criterion | Where |
|---|---|
| All 10 sections of Project Omni-Self Forecast | `forecast.md` §0..§9 (1:1 with MET-457's ส่วนที่ 1..10) and matching `<h2>Section N` blocks in HTML |
| Inline `<style>` only | `<style>` block inside `<head>`, no external `.css` link |
| Google font via `<link>` only | `fonts.googleapis.com` link in `<head>` (Kanit headings, Inter body) |
| Per-section accents from palette | `--accent-1..7` documented as CSS custom properties + used as card border-left colors |
| No frameworks; only mermaid + minimal DOMContentLoaded init | one `<script src="vendor/mermaid.min.js">` + one inline `DOMContentLoaded` listener |
| No business logic in template | only `{{tokens}}` placeholders; the .md and .html carry structure, not meaning |

## Versioning

`{{template_version}}` is a placeholder. Bump it when the section list, palette, or layout
changes in a backward-incompatible way.

| Version | Date | Change |
|---|---|---|
| (MET-447) | initial | 5-section skeleton (Section 0..4) |
| (MET-458) | expansion | 10-section skeleton (§0..§9, mapping 1:1 to MET-457 ส่วนที่ 1..10); added 6-lens tokens, Natalia 3×3 cells, 7-chakra table, 5 stages, year-by-year rows, crisis 5-step |
| (MET-457-A) | analysis | added **บทวิเคราะห์ (6 Lenses)** block at the bottom of every section — 10 sections × 6 expert lenses (Carl Jung / Isabel Briggs Myers / Helena Blavatsky / Natalia Ladini / The Three Initiates / Su Yu Hong) = 60 new `analysis_<n>_<expert>` tokens. CSS tightened to keep one-page 1280×800 fit (heightVhRatio 1.03). |
| (MET-461) | neon + deep dive + octagram | Reworked **forecast-template.html** to futuristic-neon dark theme with Kanit font, inline `<style>`, scrollable layout, no horizontal overflow at 1280px. Added **บทวิเคราะห์เชิงลึก — Deep Dive** block per section (121 new `analysis_deep_<s>_<lens>_<topic>` placeholders, no static text — analyst fills them per user). Added **Octagram** mermaid to §1 Cosmic Synergy (9 `{{octagram_*}}` placeholders). |
