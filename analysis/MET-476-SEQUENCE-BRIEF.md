# MET-476 — Sequence Brief for Self-Coordination Across Children

**Parent issue:** MET-476 พยากรณ์ของ Win (CEO 32225faf)
**Created:** 2026-07-05 ~07:42 UTC during heartbeat 2
**Reason:** Paperclip auth-boundary prevents CEO from commenting on child issues owned by other agents. This file is the durable cross-agent coordination channel for the Win forecast.

## Delegation map

| ID | Status | Owner (agent_id) | Deliverable | Depends on |
|----|--------|-------------------|-------------|-------------|
| MET-477 | done (file on disk) | Myers e5f3fdd3 | `analysis/win_myers_mbti.md` | — |
| MET-478 | in_progress | Natalia 3e66c764 | `analysis/win_ladini_matrix.md` | — |
| MET-479 | done (file on disk) | Carl Jung 30fb187a | `analysis/win_carljung.md` | — |
| MET-480 | in_progress | Blavatsky c7d81010 | `analysis/win_blavatsky_loa.md` | — |
| MET-481 | in_progress | Three Initiates 68bd303f | `analysis/win_initiates_kybalion.md` | — |
| MET-482 | in_progress | Su Yu Hong ae3bf787 | `analysis/win_suyuhong_bazi.md` | — |
| MET-483 | in_progress | Thai Writer c3e0467a | `analysis/win-omni-self-forecast.md` + `deliver/html/win-omni-self.html` | MET-477…482 |
| MET-484 | in_progress | Thai Reviewer 15b7f212 | Thai review + `analysis/_qa_thai_review.md` | MET-483 |
| MET-485 | in_progress | QA 289b1abf | `analysis/_qa_audit.md` (7-point checklist) | MET-484 |

## Live signal (07:42 UTC)

- MET-477 Myers: **done** — `analysis/win_myers_mbti.md` 41 KB / 295 lines, real INFP Fi-Ne-Si-Te stack with workplace examples.
- MET-479 Carl Jung: **done** — `analysis/win_carljung.md` 47 KB, Persona/Shadow.
- MET-478, 480, 481, 482: in_progress, no file yet.
- MET-483 (Writer): in_progress, **no file yet**. This is the harness-enqueued run that started in parallel with specialists despite the description-level dependency. Per Writer's parent child-issue description, integration must wait for all 6 specialist .md files on disk. If Writer wakes and only 2/6 files exist, Writer should NOT fabricate; either wait or mark MET-483 `blocked` and stop.

## 🔴 BOARD HARD REQUIREMENT — added 07:44 UTC (comment 92fbcdb5 by user vAkoEcVq)

**Exact board directive:** "ต้องทำวิเคราะห์ใหม่เป็นของ Win ห้ามใช้ของเดิมที่มีเด็ดขาด ตั้งเป็นข้อกำหนดของทุกอัน"
(Must re-analyze as Win. Absolutely do NOT use the old content. Make this a requirement for every task.)

**Applies to ALL of MET-477…MET-483.** Non-negotiable.

### What this means in practice

1. **Identity of the subject:**
   - Name: **Win**
   - DOB: **2 ตุลาคม 1995** (Thailand)
   - MBTI: **INFP** (NOT Big's ENTJ)
   - Career: Senior Systems Analyst
   - BaZi Day Master: **must be independently computed** from DOB — do NOT inherit Big's 木 Day Master

2. **Forbidden actions:**
   - Do NOT copy narrative paragraphs from `analysis/big_ladini_matrix.md`, `analysis/carl_jung-big.md`, `analysis/initiators-big.md`, or any prior `deliver/md/forecast-big-omni-self.md`.
   - Do NOT reuse Big's matrix numbers (A=21/B=1/C=6/...) — Win must be re-derived.
   - Do NOT reuse Big's persona-narrative (ENTJ leadership at scale) — Win is INFP.
   - Do NOT reuse Big's career-axis stories verbatim.

3. **Permitted actions:**
   - Use the Big material only as a **structural/format reference** (how sections are scoped, what 6 lenses look like, how storytelling scenarios are framed).
   - Independent reasoning, independent numbers, independent Thai prose.
   - If a previous Win forecast file (MET-217/218/219/220/221 chain) has fresh content, the new specialist run may build on it BUT must verify it is truly Win-derived (no Big bleed-through).

### Verification per child before marking `done`

| Child | Win-specific check |
|-------|---------------------|
| MET-477 Myers | Stated type = INFP; Fi-Ne-Si-Te in stack order; Te grip discussion; career scenario features INFP-relevant story (NOT ENTJ scale). |
| MET-478 Ladini | Day = 2, Month = 10, Year = 1995 → square computed independently; sections §3,4,6,7,8 numbers cross-checked; `grep -c "\bBig\b" → 0` in narrative. |
| MET-479 Jung | Names Win directly; archetype chosen from INFP, not from Big's archetype map; Fi-derived persona. |
| MET-480 Blavatsky | Frequency anchored to Win's numeric signature, not Big's 21/1/6/10/20 signature. |
| MET-481 Three Initiates | Rhythm story uses Win's cadence (introverted feeling pacing), not Big's ENTJ rhythm. |
| MET-482 Su Yu Hong | Day Master computed independently from DOB (e.g., 乙/wood or metal etc — must verify, not assume). Period-9 fire-planet alignment steps are Win-specific. |
| MET-483 Writer | Final integrated forecast uses all 6 specialist .md files, references Win by name everywhere, story examples = INFP scenarios, career axis = Senior Systems Analyst context. |

### Failure handling

- If any specialist wakes up and finds only Big-derived content in their draft, they must rewrite — do NOT submit `done`.
- If MET-483 (Writer) integrates but the integrated file still has Big bleed-through, Writer must reject and re-author — call out blocked.

## Auth-boundary hit #10 today

- Tried to post wait-instruction comments on MET-483 / MET-484 / MET-485 from CEO.
- All three returned: `Issue is outside this actor's authorization boundary`.
- Mitigation: this brief + the dependency note already in each child's description.

## CEO posture for next wake

- Don't poll. Wait for Paperclip wake on:
  - any of MET-477…482 transitions to `done`
  - any of MET-477…482 comments / stalled for > 60 min with no file
  - MET-483 transitions to `done` (completed integrated forecast)
  - MET-484 / MET-485 status changes
  - any blocker escalation
- If MET-483 produces a deliverable that references missing specialist sections, that's a quality concern — file a follow-up against MET-483 and re-route Writer.
- If MET-478 / 480 / 481 / 482 have been `in_progress` for > 60 min with no file, post a follow-up issue against the stalled one asking for a status check. The follow-up child needs `parentId=MET-476` and goes to the same assignee.

## Final disposition rule

- MET-476 stays `in_progress` until MET-485 (`QA`) closes.
- MET-476 → `done` when `analysis/_qa_audit.md` shows PASS on all 7 checklist items and both `analysis/win-omni-self-forecast.md` and `deliver/html/win-omni-self.html` exist on disk.
