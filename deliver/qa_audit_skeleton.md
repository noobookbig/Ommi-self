# QA Audit Skeleton — forecast-big-omni-self (MET-471)

> Status: **BLOCKED** — master deliverable not yet assembled by CTO (MET-462 in_progress).
> จะเติม PASS/FAIL ในแต่ละ check หลังจาก CTO render `deliver/md/forecast-big-omni-self.md` + `deliver/html/forecast-big-omni-self.html`

## Canonical inputs (source of truth)

- `/home/big/Documents/ommiself/analysis/_shared/big_inputs.md`
- Subject: Big (Jitti Kunphruk), DOB 21 ม.ค. 2529 (21.01.1986)
- Day Master: **乙 (Yin Wood)**
- Age 2026-07-05: **40y 5m 14d**
- Matrix A=21, B=1, C=6, D=E=G=10, F=20, H=4, I=9
- Period 9 (2024–2043)
- Personal Year sequence: 7→8→9→1→2→...→9 (years 2026–2046)

## 10 audit checks

| # | Check | Result |
|---|---|---|
| 1 | Token completeness (no `{token}` ค้าง ยกเว้น {template_version}, {generated_at}) | ⏳ pending |
| 2 | Numeric consistency: Day Master = 乙, age = 40, Matrix A=21..I=9 ปรากฏครบ consistent | ⏳ pending |
| 3 | 6-lens coverage ครบ 10 sections (60 analysis_<n>_<lens> + 121 analysis_deep_<n>_<lens>_<topic>) | ⏳ pending |
| 4 | Mermaid 4 diagrams render: Cosmic Synergy loop, Natalia 3×3, 5-stage timeline, Octagram | ⏳ pending |
| 5 | Year-by-year 21 rows 2026–2046, age 40–60 | ⏳ pending |
| 6 | Period 9 context (lens 6 / §2 / §7) | ⏳ pending |
| 7 | Personal Year sequence 7→8→9→1→2→...→9 | ⏳ pending |
| 8 | Storytelling scenarios ≥ 2–3 (§4.2, §7.2, §8 Crisis) | ⏳ pending |
| 9 | HTML renders without JS errors + SVG diagrams visible | ⏳ pending |
| 10 | Originality — no copy-paste จาก `forecast-big-1986-01-21-and-career-2024-2060.md` (legacy) | ⏳ pending |

## Lenses expected in deliverable

- `analysis_0_jung` (Carl Jung)
- `analysis_0_myers` (Isabel Briggs Myers / MBTI)
- `analysis_0_blavatsky` (Helena Blavatsky / Theosophy)
- `analysis_0_ladini` (Natalia Ladini / Matrix of Destiny)
- `analysis_0_initiates` (The Three Initiates / Kybalion)
- `analysis_0_suyuhong` (Su Yu Hong / BaZi)

## Unblock owner

CTO agent `9ffd8c63` (MET-462 active run `a846f49b-821d-470b-b50d-863ed5fa05d3`) — ต้อง assemble master file ที่ `deliver/md/forecast-big-omni-self.md` + `deliver/html/forecast-big-omni-self.html`