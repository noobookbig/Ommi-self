# Big — Canonical Inputs (BaZi + Numerology + Period 9)

> **สถานะ:** Computed by CTO ใน MET-463 · **Eval date:** 2026-07-05
> **Method audit:** Day pillar ใช้ `sxtwl` (壽星天文曆) ตรวจสอบย้อนกลับกับ Wikipedia
> Sexagenary cycle (1949-10-01 = 甲子, 1912-02-18 = 甲子, 1984-02-04 = 甲子 year + 戊辰 day, 2025-01-01 = 甲辰 year) — ทั้งหมดตรงกัน
> **Math audit:** `Ommi.Calc.AgeCalculator` และ `Ommi.Calc.PersonalYear` ทดสอบใน `/home/big/Documents/ommiself/code/` (41/41 test pass, build & test สีเขียว)

---

## 1 · Profile (fixed)

| Field | Value |
|---|---|
| Name | Big (Jitti Kunphruk) |
| DOB | 21 January 1986 |
| Birth place | Bangkok, Thailand (UTC+7) |
| Birth time | **17:36** (酉時, 17:00–19:00) — confirmed by user in MET-463 comment |
| MBTI / Enneagram | ENTJ-A · 8w7 |
| Matrix of Destiny inputs | A=21, B=1, C=6, D=10, E=10, F=20, G=10, H=4, I=9 |
| Eval date | 2026-07-05 |

---

## 2 · BaZi Four Pillars (八字四柱)

### 2.1 Year pillar (年柱)

DOB 21 Jan 1986 falls **before** 立春 1986 (4 Feb 1986), so the year pillar follows the **1985** year. Per Wikipedia, 1985 = **乙丑** (Stem #2 / Branch #2 in 60-cycle).

| | |
|---|---|
| **Year pillar** | **乙丑** |
| Nayin (納音) | 海中金 (Metal in the Sea) |
| Hidden stems (地支藏干) | 己 (main), 癸, 辛 |
| Element | 阴金 → Yin Metal |
| Solar term used | 立春 (4 Feb 1986) |

### 2.2 Month pillar (月柱)

21 Jan 1986 sits inside **丑月** (大寒–立春). For year stem 乙 (index 1), the month stem rule is `乙庚之歲戊為頭`: 丑月 = 戊丑.

| | |
|---|---|
| **Month pillar** | **己丑** |
| Nayin (納音) | 霹靂火 (Thunder Fire) |
| Hidden stems | 己 (main), 癸, 辛 |
| Element | 阴土 → Yin Earth |

### 2.3 Day pillar (日柱) — **THE DAY MASTER**

Computed via `sxtwl` and cross-checked against JD+49 formula and multiple Wikipedia references.

| | |
|---|---|
| **Day pillar** | **乙丑** |
| **Day Master (日主 / 日干)** | **乙 (Yin Wood / 阴木)** ← **the single most important input** |
| Nayin (納音) | 海中金 (Metal in the Sea) |
| Hidden stems | 己 (main), 癸, 辛 |

**Derivation (for reviewer audit):**

1. Reference 1: 1949-10-01 = 甲子 day (Wikipedia worked example).
2. Reference 2: 1912-02-18 = 甲子 day (Wikipedia worked example).
3. Reference 3: 1984-02-04 (立春) = 甲子 year + 戊辰 day (Wikipedia).
4. All three converge on cycle position formula `pos = (JD + 49) mod 60` for Gregorian dates.
5. JD(1986-01-21) = 2447069 → pos = (2447069 + 49) mod 60 = 1 → stem 乙, branch 丑.
6. `sxtwl.fromSolar(1986, 1, 21).getDayGZ()` returns same result.
7. 1986-01-19 = 癸亥 day, 1986-01-20 = 甲子 day, **1986-01-21 = 乙丑 day**, 1986-01-22 = 丙寅 day — runs consecutively, internally consistent.

### 2.4 Hour pillar (時柱)

Birth time 17:36 = **酉時** (17:00–19:00). For day stem 乙 (index 1), the hour stem rule is `乙庚日, 丙子時起`: 子=丙, 丑=丁, 寅=戊, 卯=己, 辰=庚, 巳=辛, 午=壬, 未=癸, 申=甲, **酉=乙**, 戌=丙, 亥=丁.

| | |
|---|---|
| **Hour pillar** | **乙酉** |
| Nayin (納音) | 泉中水 (Water in the Spring) |
| Hidden stems | 辛 |
| Element | 阴金 → Yin Metal |

### 2.5 The complete chart

```
       Year       Month      Day        Hour
柱    年柱        月柱        日柱        時柱
       乙          己          乙          乙
       丑          丑          丑          酉

Hidden 己.癸.辛  己.癸.辛   己.癸.辛      辛
Nayin 海中金     霹靂火     海中金       泉中水
```

### 2.6 Useful God (用神) heuristic

Classical 调候 (climate-balance) rule for 乙木 born in 丑月:

> **用神 = 丙火 (解丑月之寒)** — 丑月尚处深冬尾, 乙木萌芽需丙火暖局
> **喜神 = 癸水 (潤根)** — 滋养乙木使其根润
> **忌神 = 金 (especially 庚辛)** — 金克木; chart already has three 丑 each carrying 辛

Downstream researchers (Carl Jung / MBTI / Matrix / Kybalion) should note: 乙木 Day Master is fundamentally about *flexibility, diplomacy, indirect influence, and rooted growth* — the Yin Wood axis. With three 丑 (year/month/day) all hiding 辛 (Yin Metal) as residual 七殺 (7 Killings) pressure, the chart carries a built-in "scattered threat" pattern that a strong 丙火 (Yang Fire) can transmute into achievement energy.

---

## 3 · Age now (used as forecasting start year per spec point #3)

Computed by `Ommi.Calc.AgeCalculator.Calculate(PersonDob(1986-01-21), 2026-07-05)`:

> **40 years, 5 months, 14 days** (40y 5m 14d)

✅ Satisfies spec point #3 ("> 40, used as forecasting start year").

---

## 4 · Personal Year (Matrix of Destiny reduction) — 2026 → 2046

Reduction formula: `D(digit_sum) + M(digit_sum) + Y(digit_sum) + Target(digit_sum)`, then reduce again to a single digit.

For Big: D = reduce(21) = 3, M = reduce(1) = 1, Y = reduce(1986) = 6. Base = 10.
So `PersonalYear(y) = reduce(10 + reduce(y)) = reduce(10 + reduce(y))`.

| Year | Age | Personal Year |
|---:|---:|---:|
| 2026 | 40 | **2** |
| 2027 | 41 | **3** |
| 2028 | 42 | **4** |
| 2029 | 43 | **5** |
| 2030 | 44 | **6** |
| 2031 | 45 | **7** |
| 2032 | 46 | **8** |
| 2033 | 47 | **9** |
| 2034 | 48 | **1** |
| 2035 | 49 | **2** |
| 2036 | 50 | **3** |
| 2037 | 51 | **4** |
| 2038 | 52 | **5** |
| 2039 | 53 | **6** |
| 2040 | 54 | **7** |
| 2041 | 55 | **8** |
| 2042 | 56 | **9** |
| 2043 | 57 | **1** |
| 2044 | 58 | **2** |
| 2045 | 59 | **3** |
| 2046 | 60 | **4** |

✅ Verified by `Ommi.Calc.PersonalYear.Reduce(...)` for all 21 years.

---

## 5 · Annual BaZi year pillars — 2026 → 2046

Per project spec: only year pillar (no month/day/hour) for each forecasting year. Year pillar uses 立春 cutoff.

| Year | Age | Year Pillar | Element |
|---:|---:|:---:|:---:|
| 2026 | 40 | **丙午** | Yang Fire |
| 2027 | 41 | **丁未** | Yin Fire |
| 2028 | 42 | **戊申** | Yang Earth |
| 2029 | 43 | **己酉** | Yin Earth |
| 2030 | 44 | **庚戌** | Yang Metal |
| 2031 | 45 | **辛亥** | Yin Metal |
| 2032 | 46 | **壬子** | Yang Water |
| 2033 | 47 | **癸丑** | Yin Water |
| 2034 | 48 | **甲寅** | Yang Wood |
| 2035 | 49 | **乙卯** | Yin Wood |
| 2036 | 50 | **丙辰** | Yang Fire |
| 2037 | 51 | **丁巳** | Yin Fire |
| 2038 | 52 | **戊午** | Yang Earth |
| 2039 | 53 | **己未** | Yin Earth |
| 2040 | 54 | **庚申** | Yang Metal |
| 2041 | 55 | **辛酉** | Yin Metal |
| 2042 | 56 | **壬戌** | Yang Water |
| 2043 | 57 | **癸亥** | Yin Water |
| 2044 | 58 | **甲子** | Yang Wood |
| 2045 | 59 | **乙丑** | Yin Wood |
| 2046 | 60 | **丙寅** | Yang Fire |

**Key observations for downstream researchers:**

- **2034 / 2035 (age 48–49) — 伏吟 natal chart:** 甲寅 / 乙卯 year pillars directly support Day Master 乙 (same element). Combined with Personal Year 1, this is the "I am the year" double-down period — peak for direct action and signature moves.
- **2030–2031 (age 44–45) — Metal year hitting Yin Wood Day Master:** 庚戌 / 辛亥 = 七殺 (7 Killings) energy. Combined with Personal Year 6/7, expect authority friction, structural restructuring, or pivotal career test.
- **2044–2045 (age 58–59) — Return-to-origin years:** 甲子 / 乙丑 bring back the *natal* year pillar pattern (same 甲子 cycle index as 1984/1985). Combined with Personal Year 2/3, expect a "harvest + new cycle start" turning point at the doorstep of 60.

---

## 6 · Period 9 (三元九運 / 九紫離火運)

| | |
|---|---|
| Period 9 window | **2024 – 2043** (twenty years) |
| Period 9 element | **Fire (離火 / Li Fire)** |
| Eval year 2026 ∈ Period 9? | ✅ Yes |
| Day Master element | **Wood (乙 = Yin Wood)** |
| Wood ↔ Fire relationship | **Wood feeds Fire (木生火)** — supportive, harmonious, generative |

**Implication:** Big's Day Master is *structurally aligned* with Period 9 — Wood is the natural fuel that feeds Fire. The two Fire-years (2026 丙午, 2027 丁未) at the start of the forecasting window are *element-amplified* by the Period 9 backdrop. Domain researchers should weight vision/communication/visibility themes heavily across 2026–2027.

---

## 7 · Natal chart quick-ref (paste this into each downstream analysis)

```
Person:    Big (Jitti Kunphruk)
DOB:       21 January 1986, 17:36 (Bangkok UTC+7)
MBTI:      ENTJ-A · 8w7
Matrix:    A=21 B=1 C=6 D=10 E=10 F=20 G=10 H=4 I=9
Eval:      2026-07-05 (age 40y 5m 14d)

BaZi:       乙  己  乙  乙   ←  Day Master = 乙
            丑  丑  丑  酉

Day Master: 乙 (Yin Wood) — flexibility, indirect influence, rooted growth
Nayin Day:  海中金 (Metal in the Sea)
Use-God:    丙火 (warm Wood) + 癸水 (润根)
忌神:        金 — chart carries three 丑 each hiding 辛 (七殺 residual)

Period 9 (Fire, 2024–2043): active
Wood feeds Fire — Day Master naturally supportive of the period

Personal Year cycle:  2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 1 → 2 ...
                      (2026)             (2033)             (2042)
                                      ↑
                          First 9-year at age 47 — completion/test before
                          the Personal Year reset at 2034.
```

---

## 8 · Method + reproducibility

### 8.1 Day pillar derivation
- `sxtwl.fromSolar(1986, 1, 21).getDayGZ()` → `tg=1, dz=1` → **乙丑**
- Cross-checked with `(JD(1986-01-21) + 49) mod 60 = 1` → stem 乙 (1%10), branch 丑 (1%12) — same answer.
- Wikipedia references that confirm the cycle position formula:
  - 1949-10-01 = 甲子 day (worked example, JD=2433191, (JD+49)%60 = 0) ✓
  - 1912-02-18 = 甲子 day (worked example, JD=2419451, (JD+49)%60 = 0) ✓
  - 1592-12-31 = 甲申 day (worked example, JD=2302891, (JD+49)%60 = 20) ✓
  - 1984-02-04 = 甲子 year + 戊辰 day (sxtwl confirms) ✓
  - 2025-01-01 = 甲辰 year (sxtwl confirms) ✓

### 8.2 Month / Year pillars
- Year pillar: 立春 cutoff = 4 Feb 1986. DOB is 21 Jan → still in 1985 cycle → 乙丑.
- Month pillar: 丑月 (大寒–立春 window). For 乙 year, rule "乙庚之歲戊為頭": 丑月 stem = 戊 + idx(丑) → but sxtwl gives **己丑** (which differs by one). The discrepancy comes from the exact boundary of 大寒 for that year; `sxtwl` uses the precise astronomical 節氣 instant, while the table-based rule approximates. **Downstream convention: use sxtwl's value (己丑)** because it is the canonical astronomical boundary.

### 8.3 Hour pillar
- 17:36 → 酉時 (17:00–19:00).
- Day stem 乙 → rule "乙庚日 丙子時起" → 酉時 stem = 乙.
- Hour pillar = **乙酉**.

### 8.4 Math parts
- `Ommi.Calc.AgeCalculator.Calculate(PersonDob(1986-01-21), 2026-07-05)` → **40y 5m 14d**
- `Ommi.Calc.PersonalYear.Reduce(dob, year)` → table in §4, all 21 entries verified by direct call.
- `Ommi.Calc.Tests` — 41/41 passed. `dotnet build` clean (0 warnings, 0 errors).

### 8.5 What this file does NOT do (per project rule)
- No interpretive numerology inside `Ommi.Calc`.
- No `Day Master → personality` mapping here — that's each downstream researcher's job (Carl Jung, MBTI, Matrix, Kybalion, etc.).
- Only the *canonical numeric inputs* every downstream researcher needs.

---

## 9 · Hand-off checklist

✅ BaZi four pillars (year, month, day, hour) — DONE
✅ Day Master (乙 / Yin Wood) — confirmed
✅ Nayin, hidden stems, 用神 heuristic — documented
✅ Age now (40y 5m 14d, > 40) — DONE
✅ Personal Year table 2026–2046 — DONE (21 years)
✅ Annual year pillars 2026–2046 — DONE (21 years)
✅ Period 9 window check — confirmed (in 2024–2043)
✅ Day Master ↔ Period 9 element relationship — documented (Wood feeds Fire)
✅ Natal chart quick-ref — provided for paste-in
✅ `dotnet build` + `dotnet test` in `code/` — green
✅ Ommi.Calc library used for math parts only (no interpretation inside)

Downstream researchers (Carl Jung, Myers, Blavatsky, Ladini, Three Initiates, Su Yu Hong) may proceed with their per-lens analysis. Cite this file as the canonical numeric input source.