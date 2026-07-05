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

### บทวิเคราะห์เชิงลึก — Deep Dive (6 Lenses × 12 Topics)

> Long-form analysis per expert lens. Each topic is its own placeholder
> `{{analysis_deep_0_<lens>_<topic>}}` — analysts fill in actual reading.
> Schema: `analysis_deep_<section>_<lens_short>_<topic>`.
>
> HTML renders each as a `<p><strong>Heading:</strong> {{token}}</p>` inside a
> `.lens-card` element grouped under a `.lens-deep` block.

#### Carl Jung

- {{analysis_deep_0_jung_persona_shadow}}
- {{analysis_deep_0_jung_individuation_path}}

#### Isabel Briggs Myers

- {{analysis_deep_0_myers_type_stack}}
- {{analysis_deep_0_myers_cognitive_loop}}

#### Helena Blavatsky

- {{analysis_deep_0_blavatsky_root_race}}
- {{analysis_deep_0_blavatsky_monad_reincarnation}}

#### นาตาเลีย ลาดินี

- {{analysis_deep_0_ladini_natal_chart}}
- {{analysis_deep_0_ladini_transit_windows}}

#### The Three Initiates

- {{analysis_deep_0_initiators_mystery_school}}
- {{analysis_deep_0_initiators_initiate_trials}}

#### Su Yu Hong

- {{analysis_deep_0_suyuhong_day_master}}
- {{analysis_deep_0_suyuhong_annual_pillars}}


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

### Octagram — 8 Cosmic Forces Around the Monad

> Eight cosmic forces radiating from the central Monad. Each direction is a lens
> of the universe acting on the persona in this period. Replace each token with
> the analyst's reading.

| Position | Force | Reading |
|----------|-------|---------|
| Center | Monad · Self | `{{octagram_center}}` |
| N | Kybalion · Mentalism | `{{octagram_n}}` |
| NE | LoA · Vibration | `{{octagram_ne}}` |
| E | Matrix · Loop | `{{octagram_e}}` |
| SE | BaZi · Heavenly Stem | `{{octagram_se}}` |
| S | Jung · Shadow | `{{octagram_s}}` |
| SW | Ladini · Saturn | `{{octagram_sw}}` |
| W | Hermetic · Polarity | `{{octagram_w}}` |
| NW | Mystery · Initiation | `{{octagram_nw}}` |

```mermaid
%% Octagram — Monad at center, 8 cosmic forces radiating outward, adjacent forces connect along the octagonal ring.
flowchart TD
  classDef center fill:#1a1a3a,stroke:#ff00d4,color:#ff00d4,stroke-width:4px
  classDef n     fill:#11112a,stroke:#00f0ff,color:#00f0ff
  classDef ne    fill:#11112a,stroke:#39ff14,color:#39ff14
  classDef e     fill:#11112a,stroke:#9d4edd,color:#e6f7ff
  classDef se    fill:#11112a,stroke:#ff00d4,color:#ff00d4
  classDef s     fill:#11112a,stroke:#ff8c00,color:#ffd700
  classDef sw    fill:#11112a,stroke:#9d4edd,color:#e6f7ff
  classDef w     fill:#11112a,stroke:#39ff14,color:#39ff14
  classDef nw    fill:#11112a,stroke:#00f0ff,color:#00f0ff
  MON["Monad &middot; Self<br/>{{octagram_center}}"]:::center
  N["N &middot; Kybalion<br/>Mentalism<br/>{{octagram_n}}"]:::n
  NE["NE &middot; LoA<br/>Vibration<br/>{{octagram_ne}}"]:::ne
  E["E &middot; Matrix<br/>Loop<br/>{{octagram_e}}"]:::e
  SE["SE &middot; BaZi<br/>Heavenly Stem<br/>{{octagram_se}}"]:::se
  S["S &middot; Jung<br/>Shadow<br/>{{octagram_s}}"]:::s
  SW["SW &middot; Ladini<br/>Saturn<br/>{{octagram_sw}}"]:::sw
  W["W &middot; Hermetic<br/>Polarity<br/>{{octagram_w}}"]:::w
  NW["NW &middot; Mystery<br/>Initiation<br/>{{octagram_nw}}"]:::nw
  MON --- N
  MON --- NE
  MON --- E
  MON --- SE
  MON --- S
  MON --- SW
  MON --- W
  MON --- NW
  N --- NE
  NE --- E
  E --- SE
  SE --- S
  S --- SW
  SW --- W
  W --- NW
  NW --- N
```


### บทวิเคราะห์เชิงลึก — Deep Dive (6 Lenses × 13 Topics)

> Long-form analysis per expert lens. Each topic is its own placeholder
> `{{analysis_deep_1_<lens>_<topic>}}` — analysts fill in actual reading.
> Schema: `analysis_deep_<section>_<lens_short>_<topic>`.
>
> HTML renders each as a `<p><strong>Heading:</strong> {{token}}</p>` inside a
> `.lens-card` element grouped under a `.lens-deep` block.

#### Carl Jung

- {{analysis_deep_1_jung_collective_unconscious}}
- {{analysis_deep_1_jung_synchronicity}}

#### Isabel Briggs Myers

- {{analysis_deep_1_myers_function_integration}}
- {{analysis_deep_1_myers_type_development}}

#### Helena Blavatsky

- {{analysis_deep_1_blavatsky_hermetic_principles}}
- {{analysis_deep_1_blavatsky_loa_bridge}}
- {{analysis_deep_1_blavatsky_matrix_loop}}

#### นาตาเลีย ลาดินี

- {{analysis_deep_1_ladini_outer_planet}}
- {{analysis_deep_1_ladini_eclipse_season}}

#### The Three Initiates

- {{analysis_deep_1_initiators_knowledge_awakening}}
- {{analysis_deep_1_initiators_elemental_balance}}

#### Su Yu Hong

- {{analysis_deep_1_suyuhong_stems_branches}}
- {{analysis_deep_1_suyuhong_luck_cycle}}


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

### บทวิเคราะห์เชิงลึก — Deep Dive (6 Lenses × 12 Topics)

> Long-form analysis per expert lens. Each topic is its own placeholder
> `{{analysis_deep_2_<lens>_<topic>}}` — analysts fill in actual reading.
> Schema: `analysis_deep_<section>_<lens_short>_<topic>`.
>
> HTML renders each as a `<p><strong>Heading:</strong> {{token}}</p>` inside a
> `.lens-card` element grouped under a `.lens-deep` block.

#### Carl Jung

- {{analysis_deep_2_jung_center_periphery}}
- {{analysis_deep_2_jung_shadow_corners}}

#### Isabel Briggs Myers

- {{analysis_deep_2_myers_cognitive_mapping}}
- {{analysis_deep_2_myers_type_dynamics}}

#### Helena Blavatsky

- {{analysis_deep_2_blavatsky_hermetic_geometry}}
- {{analysis_deep_2_blavatsky_monad_descent}}

#### นาตาเลีย ลาดินี

- {{analysis_deep_2_ladini_chart_echo}}
- {{analysis_deep_2_ladini_personal_year}}

#### The Three Initiates

- {{analysis_deep_2_initiators_school_grid}}
- {{analysis_deep_2_initiators_initiate_path}}

#### Su Yu Hong

- {{analysis_deep_2_suyuhong_trigram_mapping}}
- {{analysis_deep_2_suyuhong_stems_interaction}}


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

### บทวิเคราะห์เชิงลึก — Deep Dive (6 Lenses × 12 Topics)

> Long-form analysis per expert lens. Each topic is its own placeholder
> `{{analysis_deep_3_<lens>_<topic>}}` — analysts fill in actual reading.
> Schema: `analysis_deep_<section>_<lens_short>_<topic>`.
>
> HTML renders each as a `<p><strong>Heading:</strong> {{token}}</p>` inside a
> `.lens-card` element grouped under a `.lens-deep` block.

#### Carl Jung

- {{analysis_deep_3_jung_talent_archetype}}
- {{analysis_deep_3_jung_karmic_pattern}}

#### Isabel Briggs Myers

- {{analysis_deep_3_myers_natural_strength}}
- {{analysis_deep_3_myers_shadow_gift}}

#### Helena Blavatsky

- {{analysis_deep_3_blavatsky_soul_mission}}
- {{analysis_deep_3_blavatsky_karmic_lesson}}

#### นาตาเลีย ลาดินี

- {{analysis_deep_3_ladini_karmic_debt}}
- {{analysis_deep_3_ladini_soul_contract}}

#### The Three Initiates

- {{analysis_deep_3_initiators_initiate_gift}}
- {{analysis_deep_3_initiators_karmic_mirror}}

#### Su Yu Hong

- {{analysis_deep_3_suyuhong_bazi_talent}}
- {{analysis_deep_3_suyuhong_karmic_resolution}}


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

### บทวิเคราะห์เชิงลึก — Deep Dive (6 Lenses × 12 Topics)

> Long-form analysis per expert lens. Each topic is its own placeholder
> `{{analysis_deep_4_<lens>_<topic>}}` — analysts fill in actual reading.
> Schema: `analysis_deep_<section>_<lens_short>_<topic>`.
>
> HTML renders each as a `<p><strong>Heading:</strong> {{token}}</p>` inside a
> `.lens-card` element grouped under a `.lens-deep` block.

#### Carl Jung

- {{analysis_deep_4_jung_career_persona}}
- {{analysis_deep_4_jung_career_growth}}

#### Isabel Briggs Myers

- {{analysis_deep_4_myers_career_stack}}
- {{analysis_deep_4_myers_team_role}}

#### Helena Blavatsky

- {{analysis_deep_4_blavatsky_vocation_path}}
- {{analysis_deep_4_blavatsky_money_consciousness}}

#### นาตาเลีย ลาดินี

- {{analysis_deep_4_ladini_midheaven_transit}}
- {{analysis_deep_4_ladini_career_house}}

#### The Three Initiates

- {{analysis_deep_4_initiators_initiate_vocation}}
- {{analysis_deep_4_initiators_work_ritual}}

#### Su Yu Hong

- {{analysis_deep_4_suyuhong_career_bazi}}
- {{analysis_deep_4_suyuhong_wealth_element}}


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

### บทวิเคราะห์เชิงลึก — Deep Dive (6 Lenses × 12 Topics)

> Long-form analysis per expert lens. Each topic is its own placeholder
> `{{analysis_deep_5_<lens>_<topic>}}` — analysts fill in actual reading.
> Schema: `analysis_deep_<section>_<lens_short>_<topic>`.
>
> HTML renders each as a `<p><strong>Heading:</strong> {{token}}</p>` inside a
> `.lens-card` element grouped under a `.lens-deep` block.

#### Carl Jung

- {{analysis_deep_5_jung_anima_animus}}
- {{analysis_deep_5_jung_relationship_pattern}}

#### Isabel Briggs Myers

- {{analysis_deep_5_myers_communication_style}}
- {{analysis_deep_5_myers_love_language}}

#### Helena Blavatsky

- {{analysis_deep_5_blavatsky_twin_flame}}
- {{analysis_deep_5_blavatsky_generational_wisdom}}

#### นาตาเลีย ลาดินี

- {{analysis_deep_5_ladini_venus_return}}
- {{analysis_deep_5_ladini_seventh_house}}

#### The Three Initiates

- {{analysis_deep_5_initiators_sacred_union}}
- {{analysis_deep_5_initiators_generational_mission}}

#### Su Yu Hong

- {{analysis_deep_5_suyuhong_spouse_palace}}
- {{analysis_deep_5_suyuhong_relationship_luck}}


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

### บทวิเคราะห์เชิงลึก — Deep Dive (6 Lenses × 12 Topics)

> Long-form analysis per expert lens. Each topic is its own placeholder
> `{{analysis_deep_6_<lens>_<topic>}}` — analysts fill in actual reading.
> Schema: `analysis_deep_<section>_<lens_short>_<topic>`.
>
> HTML renders each as a `<p><strong>Heading:</strong> {{token}}</p>` inside a
> `.lens-card` element grouped under a `.lens-deep` block.

#### Carl Jung

- {{analysis_deep_6_jung_body_shadow}}
- {{analysis_deep_6_jung_wholeness_practice}}

#### Isabel Briggs Myers

- {{analysis_deep_6_myers_energy_management}}
- {{analysis_deep_6_myers_stress_response}}

#### Helena Blavatsky

- {{analysis_deep_6_blavatsky_etheric_body}}
- {{analysis_deep_6_blavatsky_kundalini}}

#### นาตาเลีย ลาดินี

- {{analysis_deep_6_ladini_sixth_house}}
- {{analysis_deep_6_ladini_healing_transit}}

#### The Three Initiates

- {{analysis_deep_6_initiators_chakra_activation}}
- {{analysis_deep_6_initiators_energy_field}}

#### Su Yu Hong

- {{analysis_deep_6_suyuhong_five_elements}}
- {{analysis_deep_6_suyuhong_body_constitution}}


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

### บทวิเคราะห์เชิงลึก — Deep Dive (6 Lenses × 12 Topics)

> Long-form analysis per expert lens. Each topic is its own placeholder
> `{{analysis_deep_7_<lens>_<topic>}}` — analysts fill in actual reading.
> Schema: `analysis_deep_<section>_<lens_short>_<topic>`.
>
> HTML renders each as a `<p><strong>Heading:</strong> {{token}}</p>` inside a
> `.lens-card` element grouped under a `.lens-deep` block.

#### Carl Jung

- {{analysis_deep_7_jung_life_arc}}
- {{analysis_deep_7_jung_midlife_transition}}

#### Isabel Briggs Myers

- {{analysis_deep_7_myers_cognitive_aging}}
- {{analysis_deep_7_myers_wisdom_function}}

#### Helena Blavatsky

- {{analysis_deep_7_blavatsky_reincarnation_cycle}}
- {{analysis_deep_7_blavatsky_year_energy}}

#### นาตาเลีย ลาดินี

- {{analysis_deep_7_ladini_saturn_return}}
- {{analysis_deep_7_ladini_progressed_moon}}

#### The Three Initiates

- {{analysis_deep_7_initiators_year_theme}}
- {{analysis_deep_7_initiators_annual_ritual}}

#### Su Yu Hong

- {{analysis_deep_7_suyuhong_decade_luck}}
- {{analysis_deep_7_suyuhong_pillars_reading}}


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

### บทวิเคราะห์เชิงลึก — Deep Dive (6 Lenses × 12 Topics)

> Long-form analysis per expert lens. Each topic is its own placeholder
> `{{analysis_deep_8_<lens>_<topic>}}` — analysts fill in actual reading.
> Schema: `analysis_deep_<section>_<lens_short>_<topic>`.
>
> HTML renders each as a `<p><strong>Heading:</strong> {{token}}</p>` inside a
> `.lens-card` element grouped under a `.lens-deep` block.

#### Carl Jung

- {{analysis_deep_8_jung_shadow_work}}
- {{analysis_deep_8_jung_individuation_ritual}}

#### Isabel Briggs Myers

- {{analysis_deep_8_myers_development_plan}}
- {{analysis_deep_8_myers_team_collaboration}}

#### Helena Blavatsky

- {{analysis_deep_8_blavatsky_seven_principles}}
- {{analysis_deep_8_blavatsky_karma_yoga}}

#### นาตาเลีย ลาดินี

- {{analysis_deep_8_ladini_planetary_remedy}}
- {{analysis_deep_8_ladini_daily_astro}}

#### The Three Initiates

- {{analysis_deep_8_initiators_pathworking}}
- {{analysis_deep_8_initiators_mantra_practice}}

#### Su Yu Hong

- {{analysis_deep_8_suyuhong_feng_shui}}
- {{analysis_deep_8_suyuhong_bazi_daily}}


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

### บทวิเคราะห์เชิงลึก — Deep Dive (6 Lenses × 12 Topics)

> Long-form analysis per expert lens. Each topic is its own placeholder
> `{{analysis_deep_9_<lens>_<topic>}}` — analysts fill in actual reading.
> Schema: `analysis_deep_<section>_<lens_short>_<topic>`.
>
> HTML renders each as a `<p><strong>Heading:</strong> {{token}}</p>` inside a
> `.lens-card` element grouped under a `.lens-deep` block.

#### Carl Jung

- {{analysis_deep_9_jung_the_self}}
- {{analysis_deep_9_jung_meaning_of_life}}

#### Isabel Briggs Myers

- {{analysis_deep_9_myers_final_integration}}
- {{analysis_deep_9_myers_type_wisdom}}

#### Helena Blavatsky

- {{analysis_deep_9_blavatsky_universal_brotherhood}}
- {{analysis_deep_9_blavatsky_final_aspiration}}

#### นาตาเลีย ลาดินี

- {{analysis_deep_9_ladini_contract_completion}}
- {{analysis_deep_9_ladini_chart_mastery}}

#### The Three Initiates

- {{analysis_deep_9_initiators_mastery_path}}
- {{analysis_deep_9_initiators_universal_service}}

#### Su Yu Hong

- {{analysis_deep_9_suyuhong_destiny_unfoldment}}
- {{analysis_deep_9_suyuhong_final_blessing}}


---

*Template version: `{{template_version}}` · Generated: `{{generated_at}}` · Sections 0–9 (Project Omni-Self)*