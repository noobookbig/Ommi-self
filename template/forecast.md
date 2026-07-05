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
%% Eight-spoke layout — 8 numbered slots around a central zone.
%% Subgraphs label each spoke's position; the diagram preserves the
%% 8-spoke + center + outer-ring structure of the reference PDF.
flowchart LR
    classDef slot1 fill:#8a2be2,stroke:#fff,color:#fff,stroke-width:2px
    classDef slot2 fill:#4169e1,stroke:#fff,color:#fff,stroke-width:2px
    classDef slot3 fill:#20b2aa,stroke:#fff,color:#fff,stroke-width:2px
    classDef slot4 fill:#9acd32,stroke:#fff,color:#000,stroke-width:2px
    classDef slot5 fill:#ffd700,stroke:#fff,color:#000,stroke-width:2px
    classDef slot6 fill:#ff8c00,stroke:#fff,color:#000,stroke-width:2px
    classDef slot7 fill:#dc143c,stroke:#fff,color:#fff,stroke-width:2px
    classDef center fill:#fff,stroke:#222,color:#222,stroke-width:2px

    subgraph HUB["HUB"]
        direction TB
        C["11<br/>center"]:::center
    end
    subgraph TOP["top"]
        direction TB
        S1["1<br/>Slot 1<br/>20y"]:::slot1
    end
    subgraph TOPR["top-right"]
        direction TB
        S2["13<br/>Slot 2<br/>30y"]:::slot2
    end
    subgraph RIGHT["right"]
        direction TB
        S3["12<br/>Slot 3<br/>25y"]:::slot3
    end
    subgraph BOTR["bottom-right"]
        direction TB
        S4["5<br/>Slot 4<br/>50y"]:::slot4
    end
    subgraph BOT["bottom"]
        direction TB
        S5["21<br/>Slot 5<br/>60y"]:::slot5
    end
    subgraph BOTL["bottom-left"]
        direction TB
        S6["17<br/>Slot 6<br/>45y"]:::slot6
    end
    subgraph LEFT["left"]
        direction TB
        S7["6<br/>Slot 7<br/>40y"]:::slot7
    end
    subgraph TOPL["top-left"]
        direction TB
        S8["16<br/>Slot 8<br/>70y"]:::slot1
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

## Section 1 — Eight Spoke Layout (mermaid)

> 8 numbered slots around a central zone. See diagram above. Each spoke carries a numeric
> token (placeholder) and a person-year marker. Real values come from the personal-calculation
> tool (MET-447-B).

```mermaid
%% Three-axis zone — placeholder table shape.
flowchart LR
    classDef zone fill:#f5f5f5,stroke:#222,color:#222
    Z["{{zone_label}}<br/>Zone value: 12 / 10 / 4"]:::zone
    P["Axis A"]:::zone
    E["Axis B"]:::zone
    M["Axis C"]:::zone
    Z --> P
    Z --> E
    Z --> M
```

## Section 2 — Three-Axis Matrix (mermaid)

> Three-axis placeholder rows. Replace with computed values.

```mermaid
%% Matrix rows — slot label + three-axis triple.
flowchart TB
    classDef row fill:#fafafa,stroke:#bbb,color:#222
    R1["Slot 1 — 21 / 1 / 22"]:::row
    R2["Slot 2 — 8 / 13 / 21"]:::row
    R3["Slot 3 — 5 / 12 / 17"]:::row
    R4["Slot 4 — 16 / 5 / 21"]:::row
    R5["Slot 5 — 11 / 11 / 22"]:::row
    R6["Slot 6 — 17 / 21 / 11"]:::row
    R7["Slot 7 — 6 / 10 / 16"]:::row
    R1 --> R2 --> R3 --> R4 --> R5 --> R6 --> R7
```

## Section 3 — Career-year list

- `{{career_year_1}}` — `{{career_year_1_label}}`
- `{{career_year_2}}` — `{{career_year_2_label}}`
- `{{career_year_3}}` — `{{career_year_3_label}}`
- `{{career_year_4}}` — `{{career_year_4_label}}`
- `{{career_year_5}}` — `{{career_year_5_label}}`

## Section 4 — Health Card

| Slot | Axis A | Axis B | Axis C |
|------|--------|--------|--------|
| Slot 1 | `{{hc_1_phys}}` | `{{hc_1_eng}}` | `{{hc_1_emo}}` |
| Slot 2 | `{{hc_2_phys}}` | `{{hc_2_eng}}` | `{{hc_2_emo}}` |
| Slot 3 | `{{hc_3_phys}}` | `{{hc_3_eng}}` | `{{hc_3_emo}}` |
| Slot 4 | `{{hc_4_phys}}` | `{{hc_4_eng}}` | `{{hc_4_emo}}` |
| Slot 5 | `{{hc_5_phys}}` | `{{hc_5_eng}}` | `{{hc_5_emo}}` |
| Slot 6 | `{{hc_6_phys}}` | `{{hc_6_eng}}` | `{{hc_6_emo}}` |
| Slot 7 | `{{hc_7_phys}}` | `{{hc_7_eng}}` | `{{hc_7_emo}}` |
| Zone value | `{{hc_result_phys}}` | `{{hc_result_eng}}` | `{{hc_result_emo}}` |

---

*Template version: `{{template_version}}` · Generated: `{{generated_at}}`*