# Forecast Template — {{person_name}} ({{dob}})

> Canonical template. Structure only — meaning is filled in by downstream agents.
> Replace every `{{token}}` (and remove the token text) before rendering. Tokens are placeholders,
> never final content.

---

## Section 0 — Summary (≤ 300 words)

> Free-form 300-word summary. English or Thai; downstream copywriter decides.

- Person: `{{person_name}}`
- DOB: `{{dob}}`
- Person-year window: `{{person_year_start}}` → `{{person_year_end}}`
- Headline reading: `{{headline_reading}}`

```mermaid
%% Octagram — 8 chakra spokes around a central zone.
%% Subgraphs label each spoke's position; the diagram preserves the
%% 8-spoke + center + outer-ring structure of the reference PDF.
flowchart LR
    classDef ch1 fill:#8a2be2,stroke:#fff,color:#fff,stroke-width:2px
    classDef ch2 fill:#4169e1,stroke:#fff,color:#fff,stroke-width:2px
    classDef ch3 fill:#20b2aa,stroke:#fff,color:#fff,stroke-width:2px
    classDef ch4 fill:#9acd32,stroke:#fff,color:#000,stroke-width:2px
    classDef ch5 fill:#ffd700,stroke:#fff,color:#000,stroke-width:2px
    classDef ch6 fill:#ff8c00,stroke:#fff,color:#000,stroke-width:2px
    classDef ch7 fill:#dc143c,stroke:#fff,color:#fff,stroke-width:2px
    classDef center fill:#fff,stroke:#222,color:#222,stroke-width:2px

    subgraph HUB["HUB"]
        direction TB
        C["11<br/>center"]:::center
    end
    subgraph TOP["top"]
        direction TB
        S1["1<br/>Sahasrara<br/>20y"]:::ch1
    end
    subgraph TOPR["top-right"]
        direction TB
        S2["13<br/>Ajna<br/>30y"]:::ch2
    end
    subgraph RIGHT["right"]
        direction TB
        S3["12<br/>Vissudha<br/>25y"]:::ch3
    end
    subgraph BOTR["bottom-right"]
        direction TB
        S4["5<br/>Anahata<br/>50y"]:::ch4
    end
    subgraph BOT["bottom"]
        direction TB
        S5["21<br/>Manipura<br/>60y"]:::ch5
    end
    subgraph BOTL["bottom-left"]
        direction TB
        S6["17<br/>Svadhisthana<br/>45y"]:::ch6
    end
    subgraph LEFT["left"]
        direction TB
        S7["6<br/>Muladhara<br/>40y"]:::ch7
    end
    subgraph TOPL["top-left"]
        direction TB
        S8["16<br/>Common<br/>70y"]:::ch1
    end

    C --- S1
    C --- S2
    C --- S3
    C --- S4
    C --- S5
    C --- S6
    C --- S7
    C --- S8
    S1 --- S2
    S2 --- S3
    S3 --- S4
    S4 --- S5
    S5 --- S6
    S6 --- S7
    S7 --- S8
    S8 --- S1
```

## Section 1 — Octagram (mermaid)

> 8 chakra spokes around a central zone. See diagram above. Each spoke carries a numeric
> token (placeholder) and a person-year marker. Real values come from the personal-calculation
> tool (MET-447-B).

```mermaid
%% Matrix of Destiny — placeholder table shape.
flowchart LR
    classDef zone fill:#f5f5f5,stroke:#222,color:#222
    Z["{{zone_label}}<br/>Common energy: 12 / 10 / 4"]:::zone
    P["Physics"]:::zone
    E["Energy"]:::zone
    M["Emotions"]:::zone
    Z --> P
    Z --> E
    Z --> M
```

## Section 2 — Matrix (mermaid)

> Matrix of Destiny table — placeholder rows. Replace with computed values.

```mermaid
%% Matrix rows — chakra name + physics/energy/emotions triple.
flowchart TB
    classDef row fill:#fafafa,stroke:#bbb,color:#222
    R1["Sahasrara — Mission — 21 / 1 / 22"]:::row
    R2["Ajna — Destiny — 8 / 13 / 21"]:::row
    R3["Vissudha — Destiny — 5 / 12 / 17"]:::row
    R4["Anahata — Relationships — 16 / 5 / 21"]:::row
    R5["Manipura — Status — 11 / 11 / 22"]:::row
    R6["Svadhisthana — Joy — 17 / 21 / 11"]:::row
    R7["Muladhara — Body — 6 / 10 / 16"]:::row
    R1 --> R2 --> R3 --> R4 --> R5 --> R6 --> R7
```

## Section 3 — Career-year list

- `{{career_year_1}}` — `{{career_year_1_label}}`
- `{{career_year_2}}` — `{{career_year_2_label}}`
- `{{career_year_3}}` — `{{career_year_3_label}}`
- `{{career_year_4}}` — `{{career_year_4_label}}`
- `{{career_year_5}}` — `{{career_year_5_label}}`

## Section 4 — Health card

| Chakra | Physics | Energy | Emotions |
|--------|---------|--------|----------|
| Sahasrara (Mission) | `{{hc_1_phys}}` | `{{hc_1_eng}}` | `{{hc_1_emo}}` |
| Ajna (Destiny) | `{{hc_2_phys}}` | `{{hc_2_eng}}` | `{{hc_2_emo}}` |
| Vissudha (Destiny) | `{{hc_3_phys}}` | `{{hc_3_eng}}` | `{{hc_3_emo}}` |
| Anahata (Relationships) | `{{hc_4_phys}}` | `{{hc_4_eng}}` | `{{hc_4_emo}}` |
| Manipura (Status) | `{{hc_5_phys}}` | `{{hc_5_eng}}` | `{{hc_5_emo}}` |
| Svadhisthana (Joy) | `{{hc_6_phys}}` | `{{hc_6_eng}}` | `{{hc_6_emo}}` |
| Muladhara (Body) | `{{hc_7_phys}}` | `{{hc_7_eng}}` | `{{hc_7_emo}}` |
| Common energy zone | `{{hc_result_phys}}` | `{{hc_result_eng}}` | `{{hc_result_emo}}` |

---

*Template version: `{{template_version}}` · Generated: `{{generated_at}}`*