# Forecast Template — {{person_name}} ({{dob}})

> Canonical template. **Structure only** — meaning is filled in by downstream agents.
> Replace every `{{token}}` (and remove the token text) before rendering. Tokens are
> placeholders, never final content.
>
> Template covers the 10 sections of the **Project Omni-Self Forecast** output structure
> defined by MET-447 / MET-457. Sections are numbered 0–9 to match the spec; downstream
> agents must keep this numbering when filling in the body copy.

---

## Section 0 — บทสรุป 6 มุมมองเชิงลึกที่อ่านชะตาของคุณ

> Six-lens executive summary. Each lens is one short paragraph (~50 words) — the persona's
> full reading is captured by the downstream copywriter in `{{summary_paragraph}}`.

- Person: `{{person_name}}`
- DOB: `{{dob}}`
- Person-year window: `{{person_year_start}}` → `{{person_year_end}}`
- Headline reading: `{{headline_reading}}`

### Lens 1 — มุมมองจิตวิทยาเชิงลึก (Carl Jung)
`{{lens_jung_persona}}` (Persona) · `{{lens_jung_shadow}}` (Shadow)

### Lens 2 — มุมมองกฎแห่งการดึงดูด (Helena Blavatsky)
`{{lens_law_of_attraction_freq}}`

### Lens 3 — มุมมองกฎธรรมชาติ (The Kybalion)
`{{lens_kybalion_rhythm}}` · `{{lens_kybalion_cause}}`

### Lens 4 — มุมมองบุคลิกภาพ (MBTI)
`{{lens_mbti_type}}` · cognitive lead `{{lens_mbti_lead}}` · grip `{{lens_mbti_grip}}`

### Lens 5 — มุมมองจุดบรรจบแห่งวัย (Age 60 Forecast)
`{{lens_age60_role}}` · `{{lens_age60_target}}`

### Lens 6 — มุมมองดวงจีน (BaZi & Period 9)
Day Master `{{lens_bazi_day_master}}` · balance `{{lens_bazi_balance}}` · Period-9 fit `{{lens_bazi_period9_fit}}`

### บทวิเคราะห์ (Analysis — 6 Lenses)
> The six lenses above each produce one sentence of data; this block produces
> six sentences of analysis — one per lens — showing what each tradition
> *concludes* from the same numbers. Each entry is ~30 words.

- **Carl Jung:** `{{analysis_0_jung}}`
- **Isabel Briggs Myers:** `{{analysis_0_myers}}`
- **Helena Blavatsky:** `{{analysis_0_blavatsky}}`
- **นาตาเลีย ลาดินี:** `{{analysis_0_ladini}}`
- **The Three Initiates:** `{{analysis_0_initiates}}`
- **Su Yu Hong:** `{{analysis_0_suyuhong}}`

---

## Section 1 — จุดเชื่อมโยงแห่งปรัชญาและวัฏจักร (The Cosmic Synergy)

> Three engines (Kybalion rhythm → Law of Attraction vibration → Matrix-of-Destiny loop)
> locked into one cycle. Proof line summarizes whether the three engines point the same way.

- **Engine A — Kybalion rhythm:** `{{synergy_kybalion}}`
- **Engine B — Law of Attraction vibration:** `{{synergy_loa}}`
- **Engine C — Matrix of Destiny loop:** `{{synergy_matrix}}`
- **Proof line:** `{{synergy_proof}}`

### บทวิเคราะห์ (Analysis — 6 Lenses)
> Same data, read through six expert perspectives. Each lens is a short
> interpretation (~30 words) that names what the lens *catches* that the others miss.

| Lens | Reading |
|------|---------|
| **Carl Jung** (Analytical Psychology) | `{{analysis_1_jung}}` |
| **Isabel Briggs Myers** (MBTI) | `{{analysis_1_myers}}` |
| **Helena Blavatsky** (Law of Attraction / Theosophy) | `{{analysis_1_blavatsky}}` |
| **นาตาเลีย ลาดินี** (Matrix of Destiny) | `{{analysis_1_ladini}}` |
| **The Three Initiates** (The Kybalion) | `{{analysis_1_initiates}}` |
| **Su Yu Hong** (BaZi & Period 9) | `{{analysis_1_suyuhong}}` |

```mermaid
%% Three-engine loop — Kybalion drives vibration, vibration drives Matrix loop, Matrix feeds back into rhythm.
flowchart LR
    classDef engine fill:#f5f5f5,stroke:#222,color:#222
    K["Kybalion<br/>Rhythm<br/>{{synergy_kybalion}}"]:::engine
    L["Law of Attraction<br/>Vibration<br/>{{synergy_loa}}"]:::engine
    M["Matrix of Destiny<br/>Loop<br/>{{synergy_matrix}}"]:::engine
    K --> L --> M --> K
```

---

## Section 2 — โปรแกรมชีวิตและแกนหลัก (Natalia Square 3×3)

> 3×3 grid with central hub. Each cell carries the canonical Natalia-square slot letter (A–I)
> and the computed value placeholder. Echo Numbers row surfaces any repeating numerals.

### 2.1 แกนบน (ความคิด / เริ่มต้น)
Day/month/year decoding → `{{natalia_top_axis_value}}` · lead token `{{natalia_top_token}}`

### 2.2 แกนกลาง (การงาน / วิถีชีวิต)
`{{natalia_mid_cycle}}` · maturity marker `{{natalia_mid_token}}`

### 2.3 แกนล่าง (ฐานราก / บุคลิก)
`{{natalia_base_drive}}` · persona surface `{{natalia_base_mask}}`

### 2.4 Echo Numbers
`{{natalia_echo_numbers}}` · influence `{{natalia_echo_influence}}`

### บทวิเคราะห์ (Analysis — 6 Lenses)

- **Carl Jung:** `{{analysis_2_jung}}`
- **Isabel Briggs Myers:** `{{analysis_2_myers}}`
- **Helena Blavatsky:** `{{analysis_2_blavatsky}}`
- **นาตาเลีย ลาดินี:** `{{analysis_2_ladini}}`
- **The Three Initiates:** `{{analysis_2_initiates}}`
- **Su Yu Hong:** `{{analysis_2_suyuhong}}`

```mermaid
%% Natalia Square 3x3 — slots A..I around a center hub + Echo strip.
flowchart LR
    classDef corner fill:#e6f8ff,stroke:#4169e1,color:#1a1a2e
    classDef edge   fill:#f0f8ff,stroke:#20b2aa,color:#1a1a2e
    classDef center fill:#fff,stroke:#8a2be2,color:#1a1a2e,stroke-width:3px
    classDef echo   fill:#fff5e6,stroke:#ff8c00,color:#1a1a2e

    A["A<br/>{{natalia_A}}"]:::corner
    B["B<br/>{{natalia_B}}"]:::edge
    C["C<br/>{{natalia_C}}"]:::corner
    D["D<br/>{{natalia_D}}"]:::edge
    C2["center<br/>{{natalia_center}}"]:::center
    E["E<br/>{{natalia_E}}"]:::edge
    F["F<br/>{{natalia_F}}"]:::corner
    G["G<br/>{{natalia_G}}"]:::edge
    H["H<br/>{{natalia_H}}"]:::corner
    I["I<br/>{{natalia_I}}"]:::corner
    ECHO["Echo: {{natalia_echo_numbers}}"]:::echo

    A --- B --- C
    A --- D --- C2 --- E --- C
    C --- F --- C
    D --- G --- E
    F --- H --- I
    I --- G --- F
    C2 --- ECHO
```

---

## Section 3 — พรสวรรค์ ศักยภาพ และอดีตชาติ

### 3.1 พรสวรรค์หลักและศักยภาพแฝง
- Primary gift: `{{talent_primary}}`
- Latent gift: `{{talent_latent}}`

### 3.2 ชีวิตในอดีตและหางกรรม (Karmic Tail)
- Recurring pattern: `{{karmic_pattern}}`
- Lesson to unlock: `{{karmic_lesson}}`

### บทวิเคราะห์ (Analysis — 6 Lenses)

- **Carl Jung:** `{{analysis_3_jung}}`
- **Isabel Briggs Myers:** `{{analysis_3_myers}}`
- **Helena Blavatsky:** `{{analysis_3_blavatsky}}`
- **นาตาเลีย ลาดินี:** `{{analysis_3_ladini}}`
- **The Three Initiates:** `{{analysis_3_initiates}}`
- **Su Yu Hong:** `{{analysis_3_suyuhong}}`

---

## Section 4 — การเงิน ความสำเร็จ และบทบาทเชิงลึก

### 4.1 อาชีพและการเงิน
> Analyze industry fit from natal code only — do NOT reference current occupation.

- Best-fit industry: `{{career_industry}}`
- Income pattern: `{{career_income_pattern}}`
- Peak window: `{{career_peak_window}}`

### 4.2 บทบาทเชิงลึกในที่ทำงาน

| Role | Behaviour | Token |
|------|-----------|-------|
| Boss (ผู้นำ) | `{{role_boss}}` | `{{role_boss_token}}` |
| Subordinate (ผู้ตาม/ทีมเวิร์ค) | `{{role_sub}}` | `{{role_sub_token}}` |
| Active hand (มือขวา — รุก) | `{{role_active}}` | `{{role_active_token}}` |
| Receptive hand (มือซ้าย — รับ) | `{{role_receptive}}` | `{{role_receptive_token}}` |

### บทวิเคราะห์ (Analysis — 6 Lenses)

- **Carl Jung:** `{{analysis_4_jung}}`
- **Isabel Briggs Myers:** `{{analysis_4_myers}}`
- **Helena Blavatsky:** `{{analysis_4_blavatsky}}`
- **นาตาเลีย ลาดินี:** `{{analysis_4_ladini}}`
- **The Three Initiates:** `{{analysis_4_initiates}}`
- **Su Yu Hong:** `{{analysis_4_suyuhong}}`

---

## Section 5 — สายสัมพันธ์ ความรัก และครอบครัว

### 5.1 ความรักและวงใน
- Relationship pattern: `{{love_pattern}}`
- Inner-circle pull: `{{love_pull}}`
- Emotional blind spot: `{{love_blind_spot}}`

### 5.2 มรดกสายตระกูล (Generation Lines)
- Paternal line: `{{line_father}}`
- Maternal line: `{{line_mother}}`

### บทวิเคราะห์ (Analysis — 6 Lenses)

- **Carl Jung:** `{{analysis_5_jung}}`
- **Isabel Briggs Myers:** `{{analysis_5_myers}}`
- **Helena Blavatsky:** `{{analysis_5_blavatsky}}`
- **นาตาเลีย ลาดินี:** `{{analysis_5_ladini}}`
- **The Three Initiates:** `{{analysis_5_initiates}}`
- **Su Yu Hong:** `{{analysis_5_suyuhong}}`

---

## Section 6 — สุขภาพและจุดอ่อน (Health Card & Chakras)

> Seven chakras × three zones (physical / energy / emotional). Central zone value summarizes the row.

| # | Chakra | Physical (Axis A) | Energy (Axis B) | Emotional (Axis C) |
|---|--------|-------------------|-----------------|--------------------|
| 1 | Crown (Sahasrara) | `{{hc_1_phys}}` | `{{hc_1_eng}}` | `{{hc_1_emo}}` |
| 2 | Third Eye (Ajna) | `{{hc_2_phys}}` | `{{hc_2_eng}}` | `{{hc_2_emo}}` |
| 3 | Throat (Vishuddha) | `{{hc_3_phys}}` | `{{hc_3_eng}}` | `{{hc_3_emo}}` |
| 4 | Heart (Anahata) | `{{hc_4_phys}}` | `{{hc_4_eng}}` | `{{hc_4_emo}}` |
| 5 | Solar Plexus (Manipura) | `{{hc_5_phys}}` | `{{hc_5_eng}}` | `{{hc_5_emo}}` |
| 6 | Sacral (Svadhisthana) | `{{hc_6_phys}}` | `{{hc_6_eng}}` | `{{hc_6_emo}}` |
| 7 | Root (Muladhara) | `{{hc_7_phys}}` | `{{hc_7_eng}}` | `{{hc_7_emo}}` |
| **Σ** | **Zone value** | **`{{hc_result_phys}}`** | **`{{hc_result_eng}}`** | **`{{hc_result_emo}}`** |

### ข้อควรระวังและวิธีปรับสมดุล
- Watch: `{{health_watch}}`
- Balance ritual: `{{health_balance}}`

### บทวิเคราะห์ (Analysis — 6 Lenses)

- **Carl Jung:** `{{analysis_6_jung}}`
- **Isabel Briggs Myers:** `{{analysis_6_myers}}`
- **Helena Blavatsky:** `{{analysis_6_blavatsky}}`
- **นาตาเลีย ลาดินี:** `{{analysis_6_ladini}}`
- **The Three Initiates:** `{{analysis_6_initiates}}`
- **Su Yu Hong:** `{{analysis_6_suyuhong}}`

---

## Section 7 — ไทม์ไลน์ 5 ช่วงวัย และพยากรณ์อาชีพรายปี

### 7.1 5 Stages of Evolution (ก่อนจุดบรรจบอายุ 60)

| # | Stage | Age band | Theme | Marker |
|---|-------|----------|-------|--------|
| 1 | ปฐมบทและการสร้างเข็มทิศ | วัยเยาว์ – ต้น 20 | `{{stage_1_theme}}` | `{{stage_1_marker}}` |
| 2 | การสำรวจและขยายอาณาเขต | กลาง 20 – ต้น 30 | `{{stage_2_theme}}` | `{{stage_2_marker}}` |
| 3 | การปะทะและจุดวิกฤต | กลาง 30 – ต้น 40 | `{{stage_3_theme}}` | `{{stage_3_marker}}` |
| 4 | การบูรณาการและปรับขั้วพลังงาน | กลาง 40 – ต้น 50 | `{{stage_4_theme}}` | `{{stage_4_marker}}` |
| 5 | การตกผลึกและส่งมอบ | กลาง 50 – 59 | `{{stage_5_theme}}` | `{{stage_5_marker}}` |

### 7.2 Year-by-Year Career Forecast (อายุปัจจุบัน → 60)

> Computed from Personal Year (Matrix) × BaZi annual stem element. Each row gives one
> year of strategic guidance.

| Year (CE) | Age | Lead energy (Personal Year + BaZi stem) | Career situation | Strategy (Cognitive Fn) |
|-----------|-----|------------------------------------------|------------------|--------------------------|
| `{{career_year_1}}` | `{{career_year_1_age}}` | `{{career_year_1_energy}}` | `{{career_year_1_situation}}` | `{{career_year_1_strategy}}` |
| `{{career_year_2}}` | `{{career_year_2_age}}` | `{{career_year_2_energy}}` | `{{career_year_2_situation}}` | `{{career_year_2_strategy}}` |
| `{{career_year_3}}` | `{{career_year_3_age}}` | `{{career_year_3_energy}}` | `{{career_year_3_situation}}` | `{{career_year_3_strategy}}` |
| `{{career_year_4}}` | `{{career_year_4_age}}` | `{{career_year_4_energy}}` | `{{career_year_4_situation}}` | `{{career_year_4_strategy}}` |
| `{{career_year_5}}` | `{{career_year_5_age}}` | `{{career_year_5_energy}}` | `{{career_year_5_situation}}` | `{{career_year_5_strategy}}` |

```mermaid
%% 5-stage evolution bar — left-to-right timeline before the age-60 convergence.
flowchart LR
    classDef stage fill:#e6f8ff,stroke:#4169e1,color:#1a1a2e
    classDef hub   fill:#fff,stroke:#8a2be2,color:#1a1a2e,stroke-width:3px
    S1["Stage 1<br/>{{stage_1_theme}}"]:::stage
    S2["Stage 2<br/>{{stage_2_theme}}"]:::stage
    S3["Stage 3<br/>{{stage_3_theme}}"]:::stage
    S4["Stage 4<br/>{{stage_4_theme}}"]:::stage
    S5["Stage 5<br/>{{stage_5_theme}}"]:::stage
    H["Age 60<br/>Convergence"]:::hub
    S1 --> S2 --> S3 --> S4 --> S5 --> H
```

### บทวิเคราะห์ (Analysis — 6 Lenses)

- **Carl Jung:** `{{analysis_7_jung}}`
- **Isabel Briggs Myers:** `{{analysis_7_myers}}`
- **Helena Blavatsky:** `{{analysis_7_blavatsky}}`
- **นาตาเลีย ลาดินี:** `{{analysis_7_ladini}}`
- **The Three Initiates:** `{{analysis_7_initiates}}`
- **Su Yu Hong:** `{{analysis_7_suyuhong}}`

---

## Section 8 — คำแนะนำและแนวทางปฏิบัติ (Actionable Protocols)

- **รายวัน (Daily):** `{{protocol_daily}}`
- **รายสัปดาห์ (Weekly):** `{{protocol_weekly}}`
- **รายเดือน (Monthly):** `{{protocol_monthly}}`
- **กลยุทธ์รับมือวิกฤต (Crisis Mastery):** `{{protocol_crisis}}`

### บทวิเคราะห์ (Analysis — 6 Lenses)
> Each lens names what the protocol *means* in its own frame — not what to do,
> but *why* it works according to that tradition.

- **Carl Jung:** `{{analysis_8_jung}}`
- **Isabel Briggs Myers:** `{{analysis_8_myers}}`
- **Helena Blavatsky:** `{{analysis_8_blavatsky}}`
- **นาตาเลีย ลาดินี:** `{{analysis_8_ladini}}`
- **The Three Initiates:** `{{analysis_8_initiates}}`
- **Su Yu Hong:** `{{analysis_8_suyuhong}}`

---

## Section 9 — บทสรุปแห่งสัจธรรม (The Ultimate Synthesis)

> Melts every lens into a single map. Two closing paragraphs: how everything connects, and
> the personal truth to carry forward.

- **ความเกี่ยวข้องกันของสรรพสิ่ง (Interconnectedness):** `{{synthesis_interconnectedness}}`
- **สัจธรรมประจำตัว (Your Ultimate Truth):** `{{synthesis_ultimate_truth}}`

### บทวิเคราะห์ (Analysis — 6 Lenses)
> The closing read. Each lens seals the synthesis from its own angle, so the
> reader sees the same ultimate truth refracted through six traditions.

- **Carl Jung:** `{{analysis_9_jung}}`
- **Isabel Briggs Myers:** `{{analysis_9_myers}}`
- **Helena Blavatsky:** `{{analysis_9_blavatsky}}`
- **นาตาเลีย ลาดินี:** `{{analysis_9_ladini}}`
- **The Three Initiates:** `{{analysis_9_initiates}}`
- **Su Yu Hong:** `{{analysis_9_suyuhong}}`

---

*Template version: `{{template_version}}` · Generated: `{{generated_at}}` · Sections 0–9 (Project Omni-Self)*