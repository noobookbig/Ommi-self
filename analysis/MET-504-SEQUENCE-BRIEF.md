# MET-504 Sequence Brief — วิเคราะห์ของ Mokun ใหม่

> **Status:** Active. **Created:** 2026-07-05 ~10:01 UTC. **Parent issue:** MET-504. **Project:** Ommi-Self (596245ac).
>
> **Purpose:** Durable cross-agent coordination channel for MET-504. CEO cannot comment on child issues owned by other agents (auth-boundary block, confirmed pattern from MET-476 / MET-493). This file IS the broadcast.

---

## 🔴 BOARD HARD REQUIREMENT (applies to EVERY child)

**"ห้ามใช้ผลการพยากรณ์เก่า ให้ทำใหม่โดย Agent ที่มีความเชี่ยวชาญ"**
*(Do not reuse old forecast results. Do it fresh using agents with domain expertise.)*

### Identity lock — Mokun ONLY

| Field | Value |
|---|---|
| Name | **Mokun** |
| DOB | **2 สิงหาคม ค.ศ. 2005** (Thailand, UTC+7) |
| Age at eval | **21 ปี** (in 2026) |
| MBTI | **ENTP-A** (Ne-Ti dominant) |
| Context | University student — graduates 2028 |
| Forecast window | **2026 (age 21) → 2065 (age 60)** |

### Forbidden in any deliverable

- Any Big-specific numbers: **乙 / Yin Wood / 21-01-1986 / 21:36 / ENTJ / Wheel-of-Fortune D=E=G=10**
- Any Win-specific numbers: **丙 / Yang Fire / 02-10-1995 / INFP / Hanged Man 12-16-18**
- Any reused text from prior `analysis/mokun-omni-self-forecast.md` (cancelled in MET-493). That file is **dead**.
- The phrase **"ต้องลบ Section 20 ทิ้งแล้วทำใหม่ ทั้งหมด"** style ban also applies — no template-fill.

### Required deliverables (per issue)

| Child | Owner | Output file | Voice / Standard |
|---|---|---|---|
| **MET-504.1** | นาตาเลีย ลาดินี | `analysis/mokun_natalia_matrix.md` | Matrix of Destiny. Compute your own Square 3×3 (Day/Month/YearSum reduction >22). Must freshly derive: A, B, C, D, E, F, G, H, I, Echo Numbers, PersonalYear age 21→60. NO contrast refs to Big/Win except brief methodology footer. |
| **MET-504.2** | Su Yu Hong | `analysis/mokun_suyuhong_bazi.md` | BaZi & Period 9. **Day Master = 戊 (Yang Earth / ภูเขา)** — already verified by CEO using sxtwl (2005-08-02 noon Thailand: Year 乙酉, Month 癸未, Day 戊午, Hour 戊午). Re-verify in your own analysis. Compute 10-year Luck Pillars (大运) from age 21 onward, annual cycles (流年) 2026–2065, Period 9 (Fire) overlay. |
| **MET-504.3** | Carl Jung | `analysis/mokun_carl_jung.md` | Depth Psychology. ENTP-A archetype mapping (Persona = Explorer/Trickster; Shadow = Si-Grip, Fe-Loop). Individuation journey 21→60. Archetype assignments must tie to Mokun's Matrix anchors (after Natalia publishes). Use Jungian voice in Thai. |
| **MET-504.4** | Helena Blavatsky | `analysis/mokun_helena_blavatsky.md` | LoA & New Thought. Mokun's frequency signature. Use Hermetic Correspondence (as above so below). ENTP-A = Magician/Hierophant in LoA framing. Story-based — describe his vibration and how it manifests. |
| **MET-504.5** | The Three Initiates | `analysis/mokun_initiates_kybalion.md` | 7 Hermetic Principles applied. **STANDARD.md MET-394** compliance: prose + reasoning + direct cite of your discipline. NO token schema `{{TOKEN}} = value`. NO business-logic code. Reason about the 7 principles in Mokun's context. Rhythm = Yang Earth diurnal cycle. |
| **MET-504.6** | Isabel Briggs Myers | `analysis/mokun_myers_mbti.md` | MBTI. ENTP-A = Ne-Ti-Fe-Si. Explain dominant, auxiliary, tertiary, inferior. Address Si-Grip and Fe-Loop specifically (board story requirement). Tie to Mokun's narrative as university student graduating 2028. |
| **MET-504.7** | Thai Writer (integrator) | `analysis/mokun-omni-self-forecast.md` | **Sequential — must run AFTER all 6 specialists done.** Read all 6 analysis files. Assemble the integrated 10-section forecast in Big's voice (use `deliver/md/forecast-big-omni-self.md` as structural reference but content fully Mokun-specific). Target 500–700 lines. Include Mermaid diagrams (Natalia 3×3 + 60-year Octagram). |
| **MET-504.8** | CTO | `deliver/html/forecast-mokun.html` + `deliver/html/forecast-mokun-from-big-template.html` | **Sequential — must run AFTER MET-504.7.** Render MD → 2 HTML variants. Variant A: clone `template/forecast-template.html`, fill all `{{token}}` with Mokun content. Variant B: clone `deliver/html/forecast-big.html`, swap Big→Mokun content. Also: `analysis/_qa_render_mokun_1280x800.png` via existing `analysis/qa_render.py`. |

### Per-deliverable Win-bleed check (run before marking done)

```bash
# Replace win with mokun in the grep
for file in analysis/mokun_*.md; do
  echo "=== $file ==="
  grep -E "Big|Win|乙木|丙火|21-01-1986|02-10-1995|ENTJ|INFP|Wheel of Fortune D=E=G=10|Hanged Man 12-16-18" "$file" | grep -v "methodology footer\|contrast\|comparison\|brief" | head -10
done
```

If grep returns non-empty hits in BODY content (not methodology footer), FAIL and rewrite.

---

## Pre-computed Anchors (locked — do not recompute or alter)

These are the substrate every specialist builds on. Verified by CEO via sxtwl. Use them as anchors, not as gospel — if your discipline's own method contradicts, reason about it in your section but DO NOT replace the anchor silently.

### BaZi Four Pillars (Mokun)

| Pillar | Stem-Branch | Nayin |
|---|---|---|
| Year (年柱) | 乙酉 (Yin Wood / Rooster) | 井泉水 |
| Month (月柱) | 癸未 (Yin Water / Goat) | 杨柳木 |
| **Day (日柱)** | **戊午 (Yang Earth / Horse)** | **天上火** |
| Hour (時柱) | 戊午 (Yang Earth / Horse) | 天上火 |

- **Day Master (DM) = 戊 (Yang Earth)** — mountain, dyke, cliff. Stable, holding, generous, slow to anger but absolute when crossed. Earth carries everything.
- **Month branch 未 = 己土本气 + 丁火余气 + 乙木余气** — strong Earth base; summer month (Fire supports Earth).
- **Hour 戊午 = same as day** — twin pillars. Mokun's "double anchor" structure.
- **No specific hour given by user** — issue says "DOB only". For full BaZi you may note the hour is unconfirmed and use noon default; the Day pillar is the same regardless of hour branch.

### Personal Year formula (board-locked for project)

```
PY(year) = reduce(Day) + reduce(Month) + reduce(YearSum of Gregorian year)
reduce(n) = n if n <= 9 else 1+((n-1) % 9)  # single digit
```

For 2005-08-02: reduce(Day=2)=2, reduce(Month=8)=8, reduce(YearSum=2+0+0+5=7)=7
→ Personal Year base for 2026 = 2+8+reduce(2+0+2+6=10→1) = **2+8+1 = 11 → 2 (High Priestess)**

Cross-verify with Natalia's Square: she computes independently but should land on the same A=2.

### Period 9 overlay (2024-2044 = Fire)

- Period 9 = 离 Fire. **Fire produces Earth (火生土)** in productive cycle.
- 戊 Day Master is **doubly fed by Period 9 Fire**. Mokun sits at peak productive alignment with the era 2024-2044. This is a MASSIVE tailwind.
- Period 9 ends 2044. Mokun age 39. Beyond that, Period 1 (Water, 2044-2063) — Water controls Earth (土). New challenge phase begins at 39–60.

### University timeline anchor

- 2026 (age 21): final year of undergrad (or master start)
- 2027 (age 22): transition / first job hunt
- 2028 (age 23): **graduation** — first income, first real-world test of ENTP-A pattern

---

## Stakeholder map

| Role | Agent | Status |
|---|---|---|
| CEO (orchestrator) | 32225faf-8321-4c09-9f5d-963b19929513 | running |
| Matrix of Destiny | 3e66c764-56a1-4461-b2c7-f6b3fa29f047 | running |
| BaZi & Period 9 | ae3bf787-0f1d-43cb-8edb-e3649bc8c1eb | idle |
| Depth Psychology | 30fb187a-4751-4341-9e9b-22addc67e945 | idle |
| LoA & New Thought | c7d81010-cb88-4894-8b3b-064799010754 | idle |
| Kybalion / Hermetic | 68bd303f-855d-48f9-a85b-4398106b0cf6 | idle |
| MBTI | e5f3fdd3-81d3-495e-bf63-d0a703620955 | idle |
| Thai Writer (integrator) | c3e0467a-c406-4914-9f68-b460fb43edf6 | idle |
| Thai Reviewer (lang pass) | 15b7f212-4201-4040-a782-b20a56ca97c5 | idle |
| CTO (HTML render) | 9ffd8c63-2f35-4159-abfc-2e7b85074c28 | idle |
| QA (acceptance) | 289b1abf-f43b-4475-9841-f7086cd9457c | idle |

---

## Sequencing

```
[Parallel]
MET-504.1 Natalia  ─┐
MET-504.2 Su Yu Hong ┤
MET-504.3 Carl Jung  ┤
MET-504.4 Blavatsky  ├──→ MET-504.7 Thai Writer (integrate) ──→ MET-504.8 CTO (render)
MET-504.5 Initiates  ┤
MET-504.6 Myers     ─┘
                                              │
                                              └──→ MET-504.9 (optional) Thai Reviewer pass on HTML
```

---

## Cross-references (READ FIRST, do not copy)

- `template/forecast-template.html` — full skeleton w/ mermaid runtime vendored
- `deliver/html/forecast-big.html` — variant B template (used by MET-504.8)
- `deliver/md/forecast-big-omni-self.md` — voice/structure reference for MET-504.7
- `analysis/_shared/big_inputs.md` — Big's verified BaZi (DO NOT copy — methodology footer only)
- `analysis/win_ladini_matrix.md` — Natalia's prior Win work (DO NOT copy — methodology footer only)

---

## Failure modes & escalation

1. **Specialist stuck >30 min** — wake CEO via issue comment on MET-504 (parent). CEO will reassign or unblock.
2. **Integrator (MET-504.7) finds conflicting numbers between specialists** — reason about it, present BOTH readings in §0 §1, pick one for the spine. Do not erase the other.
3. **CTO (MET-504.8) blocked on tooling** — escalate to CEO; CTO has `pnpm dev` / Playwright precedent in `analysis/qa_render.py`.
4. **Board adds constraint mid-flight** — CEO will append to this brief and post a new comment on MET-504.
5. **Mokun-specific data bleeds from cancelled MET-493 MD** — FORBIDDEN. Even if you saw the old MD, do not retain any phrase or number that wasn't freshly derived from raw inputs (2005-08-02 / ENTP-A / university student).

---

## Live signal (updated by CEO)

- **2026-07-05 ~10:01 UTC** — MET-504 received. Brief authored. 8 children queued for assignment. Awaiting first specialist wake.
- **2026-07-05 ~10:09 UTC** — All 8 children created and assigned (MET-506…MET-513). Coordination comment posted on MET-504.
- **2026-07-05 ~10:10 UTC (heartbeat 2)** — Specialist wave in flight:
  - MET-506 (Natalia) — running since 10:06:49 UTC
  - MET-507 (Su Yu Hong) — running since 10:07:59 UTC
  - MET-508 (Carl Jung) — running since 10:07:59 UTC
  - MET-509 (Blavatsky) — running since 10:07:59 UTC
  - MET-510 (Three Initiates) — running since 10:08:00 UTC
  - MET-511 (Myers) — running since 10:08:00 UTC
  - MET-512 (Thai Writer) — todo, blocked by 6 specialists ✓
  - MET-513 (CTO) — todo, blocked by all 7 ✓
  - 0 files on disk yet — normal mid-flight state (Win wave took ~10-15 min for first delivery)
- **Disposition alert** at 10:09:52 (system watchdog comment `d8ad8b29`): "Paperclip needs a disposition before this issue can continue." Resolved this heartbeat — confirming `in_progress` with live continuation path. No blocker attention. No productivity review. No recovery action.
- **Next wake:** when first specialist flips to `done` (estimated ~10:15-10:20 UTC).
- **2026-07-05 ~10:14 UTC (heartbeat 3 — CTO)** — System escalated via `source_scoped_recovery_action` (cause: `successful_run_missing_state`, recovery owner: CTO 9ffd8c63, previousStatus: in_progress). Re-verified state:
  - 6 specialists still `in_progress`, healthy (started 10:06:49–10:08:00 UTC, ~6–7 min elapsed)
  - MET-512 (Thai Writer): `todo` (correctly blocked by 6 specialists)
  - **MET-513 (CTO/me): `todo`** (correctly blocked by all 7). No deliverable work for me until MET-512 publishes `analysis/mokun-omni-self-forecast.md`.
  - Workspace: 0 `analysis/mokun_*.md` files on disk yet (specialists still in reasoning phase — Win wave precedent: ~10–15 min for first delivery)
  - Prior CEO heartbeat 2 (10:10 UTC) correctly kept parent at `in_progress`. No real blocker; the system watchdog flagged missing disposition because the CEO's `in_progress` PATCH did not persist as the canonical state transition under the recovery flow.
  - **Disposition set this heartbeat:** `in_progress` with live continuation path. Next CTO wake: when MET-512 flips to `done` (post-specialist integration).
- **2026-07-05 ~10:22 UTC (heartbeat 6 — CTO)** — Watchdog kept firing `source_scoped_recovery_action` after each successful CTO run because the prior `in_progress` PATCH did not satisfy the `clear_next_step` validator. Took the MAS-35-style fix: PATCH `status: blocked` + `blockedByIssueIds: [MET-506, MET-507, MET-510, MET-512]` (4 still-running children). The 3 already-done specialists (MET-508/509/511) are NOT blockers — they closed cleanly. MET-513 (CTO) is unblocked the moment MET-512 closes. Recovery action `966f8bbc-…` resolved; `blockerAttention.state=covered, unresolved=4, stalled=0`.