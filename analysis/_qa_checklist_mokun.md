# QA Acceptance Checklist — Mokun Omni-Self Forecast (HTML render)

> **Status:** Parallel prep — issued before MET-497 (CTO render MD → HTML) lands.
> **Target file:** `deliver/html/forecast-mokun.html` (template variant) + `deliver/html/forecast-big.html` (variant pattern; both reference `analysis/mokun-omni-self-forecast.md` as source of truth).
> **Source of truth (raw input):** Mokun — DOB 2 August 2005 · MBTI ENTP-A · University Student จบปี 2028 · อายุ 21 ปี ณ พ.ศ. 2569 (ค.ศ. 2026).
> **Precedent:** `_qa_audit.md` (Win MET-485 structural audit) + `_qa_thai_review.md` (Win MET-484 readability audit) — checklist ของ Mokun ยืมโครงสร้างทั้งสองมา และเพิ่มเช็คที่เรียนรู้จาก Win (เช่น PY off-by-1 bug ของ Win ต้องไม่ปรากฏใน Mokun).
> **Run instructions:** ใช้ checklist นี้เมื่อ QA heartbeat ตามหลัง MET-497 ปิด — ติ๊ก ✅/❌ ในแต่ละ check, เก็บ evidence (grep output, line numbers, screenshots, console logs), แล้วอัปเดตเป็น audit report ที่ `analysis/_qa_audit_mokun.md`.

---

## Canonical Mokun values (expected — embed in HTML)

ค่าทั้งหมดนี้คำนวณจาก raw input (DOB 2 Aug 2005) และอ้างอิงจาก `analysis/mokun-omni-self-forecast.md` ซึ่งเป็นแหล่งเดียวที่ผ่าน self-audit ภายในแล้ว QA ต้อง verify ค่าเหล่านี้ปรากฏใน HTML ที่ render ออกมา — ถ้าค่าใดค่าหนึ่งหายไปหรือผิด = **FAIL**:

| Field | Expected value | Source |
|---|---|---|
| **Name** | Mokun | raw input |
| **DOB** | 2 สิงหาคม 2005 (Thai date canonical) | raw input + MD line 4 |
| **Age @ 2026** | 21 ปี | MD line 5 |
| **Age @ 2065 (Point of Arrival)** | 60 ปี | DOB + 60 years |
| **MBTI** | ENTP-A (not bare ENTP — the `-A` matters) | raw input + MD line 6 |
| **BaZi Day Master** | 戊土 (Yang Earth / ภูเขา / ดินใหญ่) — *not* 甲, *not* 乙, *not* 丙 | MD line 7, 82 |
| **Day Pillar** | 戊午 (stem=4, branch=6) | MD line 84 |
| **Year Pillar (DOB)** | 乙酉 | MD line 86 |
| **Month Pillar (DOB)** | 癸未 | MD line 86 |
| **Hour Pillar (assumed 13:00)** | 戊午 | MD line 86 |
| **Period 9** | 九紫離火運 (2024–2043) · กำลังดำเนินอยู่ | MD line 8 |
| **Matrix anchor A:B:C** | 2 – 8 – 7 (High Priestess · Strength · Chariot) | MD line 9 |
| **3×3 Square layout** | A=2 · B=8 · C=7 · D=1 · E=8 · F=6 · G=9 · H=8 · I=8 | MD line 132–134 |
| **Echo 8 (Triple-Plus)** | ปรากฏ 4/9 ตำแหน่ง (B, E, H, I) | MD line 51, 137 |
| **Personal Year 2026** | 9 (Completion) | MD line 380 — derived from `reduce(2+8+7+2026→1)=9` |
| **Personal Year 2034** | 8 (Power — Anchor Echo return) | MD line 390 — derived from `reduce(17)=8` |
| **Age-60 anchor year** | ค.ศ. 2065 · BaZi 乙巳 | MD line 413 |

**Critical reminder:** Win's HTML (MET-485) had a bug where PY sequence was off-by-1 vs canonical formula. For Mokun, **MD §8.2 sequence is correct** (verified against `analysis/_shared/bazi_calc.py:147` formula `reduce(d+m+y+t)`). QA must re-confirm this in the *rendered HTML*, not trust the source MD — because the HTML may be re-rendered by MET-497 and may re-introduce the bug.

---

## Check 1 — Structural parity (10 sections)

วัตถุประสงค์: ยืนยันว่า HTML ที่ render ออกมามี **ครบ 10 sections** ตามลำดับ spec ของ MET-493 directive (เทียบ MD lines 17, 81, 105, 163/191, 215, 281, 314, 364, 492, 572).

### 1.1 · MD section map (ground truth)

| Spec # | Heading | MD line |
|---|---|---|
| 1 | บทสรุป 6 มุมมองเชิงลึก (Carl Jung · Blavatsky · Kybalion · MBTI · Age 60 · BaZi) | 17 |
| 2 | จุดเชื่อมโยมแห่งปรัชญาและวัฏจักร (The Cosmic Synergy) | 101 |
| 3 | โปรแกรมชีวิตและแกนหลัก (Natalia Square 3×3) | 125 |
| 4 | พรสวรรค์ ศักยภาพ และอดีตชาติ | 191 |
| 5 | การเงิน ความสำเร็จ และบทบาทเชิงลึก | 215 |
| 6 | สายสัมพันธ์ ความรัก และครอบครัว | 281 |
| 7 | สุขภาพ จุดอ่อน และจักระ | 314 |
| 8 | ไทม์ไลน์ 5 ช่วงวัย และพยากรณ์อาชีพรายปี | 364 |
| 9 | คำแนะนำและแนวทางปฏิบัติ (Actionable Protocols) | 492 |
| 10 | บทสรุปแห่งสัจธรรม (The Ultimate Synthesis) | 572 |

### 1.2 · Pass criteria (HTML)

- [ ] HTML contains exactly **N top-level `<section>` blocks** (or `.card` analog) — 10 ถ้าใช้ section ตรงตัว, หรือ 11 ถ้า §7 ถูก split เป็น §7.1 (5 Stages) + §7.2 (Year-by-Year) ตามแบบ Win HTML
- [ ] ลำดับ sections ตรงกับ MD ตามตารางข้างบน (renumber เป็น 0-index ได้ แต่ลำดับ semantic ต้องตรง)
- [ ] ทุก section heading ปรากฏใน DOM (visible text, ไม่ใช่ hidden / `aria-hidden`)
- [ ] ไม่มี section ที่ MD มีแต่ HTML ขาด (เช่น ถ้า MD มี §3.1 + §3.2 + §3.3 ทั้งหมด ต้องมีครบใน HTML)

### 1.3 · How to verify

```bash
# 1) count top-level section blocks
grep -c '<section' deliver/html/forecast-mokun.html
# expected: ≥10 (or ≥11 if §7 split)

# 2) verify each section heading is present as Thai text
for h in "ส่วนที่ 1" "ส่วนที่ 2" "ส่วนที่ 3" "ส่วนที่ 4" "ส่วนที่ 5" \
         "ส่วนที่ 6" "ส่วนที่ 7" "ส่วนที่ 8" "ส่วนที่ 9" "ส่วนที่ 10"; do
  grep -F "$h" deliver/html/forecast-mokun.html >/dev/null && echo "✓ $h" || echo "✗ MISSING: $h"
done

# 3) visual cross-check via Playwright (mirror qa_render.py pattern):
#    navigate to file:// URL, dump section list, compare 1:1 with MD line numbers
```

### 1.4 · Evidence to capture

- Output of `grep -c '<section'`
- Output of heading presence loop
- Playwright DOM dump of section headings + IDs
- Screenshot of the table of contents / nav (if any) at the top of the page

**Verdict:** ☐ PASS — 10 or 11 sections present in correct order, Thai headings visible
☐ FAIL — section count mismatch OR missing heading OR wrong order

---

## Check 2 — Token resolution (no leftover `{{TOKEN}}` placeholders)

วัตถุประสงค์: ยืนยันว่า HTML ไม่มี `{{ ... }}` placeholder ที่ render ไม่สำเร็จ เหลือค้างอยู่ — ละเมิด STANDARD.md (MET-394) ข้อ 3 และลายเซ็น Win MET-481 ที่เคยมีปัญหา

### 2.1 · Pass criteria

- [ ] `grep -c "{{" deliver/html/forecast-mokun.html` returns **0** in production body
- [ ] ค่าที่ต้อง resolve ให้เป็น Thai text ทั้งหมด เช่น `{{ name }}` → "Mokun", `{{ day_master }}` → "戊土"
- [ ] ไม่มี HTML comment ที่หลงเหลือ token tags เช่น `<!-- TODO: replace {{x}} -->`
- [ ] ถ้ามี `{template_version}` หรือ `{generated_at}` ใน metadata block (เช่นใน Win HTML) ต้องเป็น **dated** ไม่ใช่ placeholder — ยอมรับได้

### 2.2 · Allowed exceptions

- Mermaid diagram `{{...}}` ในส่วน inline labels ต้องเรียกใช้เป็นปกติ (Mermaid syntax ใช้ `{}` ใน edge labels / notes) — ตรวจให้ละเอียดเพื่อแยกระหว่าง "Mermaid syntax ที่ valid" กับ "leftover template placeholder"
- ถ้ามี JSON-LD `<script type="application/ld+json">` ที่มี `{` brace ใน schema — ไม่นับเป็น violation

### 2.3 · How to verify

```bash
# 1) raw count
grep -c '{{' deliver/html/forecast-mokun.html

# 2) inspect any matches (if count > 0) and classify:
grep -n '{{' deliver/html/forecast-mokun.html

# 3) compare with original token map (if any was shared in source MD):
#    source MD should NOT contain {{ ... }} in body
grep -n '{{' analysis/mokun-omni-self-forecast.md
```

### 2.4 · Evidence to capture

- Raw `grep -c` output
- Line-by-line `grep -n` output (ถ้ามี matches)
- Decision: แต่ละ match เป็น "Mermaid syntax" / "JSON-LD schema" / "LEGIT VIOLATION"

**Verdict:** ☐ PASS — count = 0 in body (Mermaid + JSON-LD ยอมรับได้)
☐ FAIL — match ใด ๆ ใน body ของ HTML ที่ไม่ใช่ Mermaid/JSON-LD

---

## Check 3 — Mermaid render (3×3 + Octagram + Stages)

วัตถุประสงค์: ยืนยันว่า Mermaid diagrams ทั้งหมด render เป็น SVG สำเร็จ ไม่มี parse error โดยเฉพาะ 2 ตัวที่ critical สำหรับ Mokun (จาก MET-493 directive):

- **3×3 Natalia Square** ใน §3 (MD lines 155–187)
- **Octagram อายุ 60** ใน §8 (MD lines 417–488)

Win's HTML มี bug ที่ Octagram ถูกย้ายจาก §8 ไปอยู่ใน §1 ทำเป็น HTML table แทน — **Mokun ต้องไม่ repeat bug นี้**

### 3.1 · Pass criteria

- [ ] HTML มีอย่างน้อย **2 Mermaid blocks** ที่ render สำเร็จ (3×3 Square + Octagram) — โดย **Mermaid Octagram ต้องอยู่ใน §8 (ไทม์ไลน์/พยากรณ์/Year-by-Year) ไม่ใช่ใน §1 หรือ §2**
- [ ] ทุก Mermaid block ที่ render ออกมาเป็น `<svg>` element ไม่ใช่ข้อความ error เช่น "Syntax error in graph"
- [ ] 3×3 Square SVG มี **9 cells** ที่ระบุค่าครบ: A=2, B=8, C=7, D=1, E=8, F=6, G=9, H=8, I=8
- [ ] Octagram SVG มี **center node + 8 directional nodes** (N, NE, E, SE, S, SW, W, NW)
- [ ] ไม่มี console error จาก `mermaid.run()` ตอน page load

### 3.2 · How to verify

```bash
# 1) count mermaid blocks declared
grep -c 'class="mermaid"\|data-mermaid=\|pre class="mermaid"' deliver/html/forecast-mokun.html

# 2) Playwright headless render test (mirror qa_render_win_octagram.py pattern):
cat > /tmp/qa_render_mokun.py <<'PY'
from playwright.sync_api import sync_playwright
import json
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 800})
    errors = []
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.on("console", lambda m: errors.append(f"console.{m.type}: {m.text}") if m.type == "error" else None)
    page.goto("file:///home/big/Documents/ommiself/deliver/html/forecast-mokun.html")
    page.wait_for_load_state("networkidle")
    # wait for mermaid to finish
    page.wait_for_timeout(2000)
    result = {
        "errors": errors,
        "svgCount": page.locator("svg").count(),
        "mermaidSvgs": page.locator(".mermaid svg").count(),
        "sectionCount": page.locator("section").count(),
        "scrollHeight": page.evaluate("document.body.scrollHeight"),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    browser.close()
PY
python3 /tmp/qa_render_mokun.py
```

Expected JSON output:
```json
{
  "errors": [],
  "svgCount": ≥2,
  "mermaidSvgs": 2 (or more),
  "sectionCount": 10 (or 11),
  "scrollHeight": > 800
}
```

### 3.3 · Visual evidence

- [ ] Screenshot ของ 3×3 Square at 1280×800
- [ ] Screenshot ของ Octagram at 1280×800 (หลัง scroll ไปที่ §8)
- [ ] Full-page screenshot — save as `analysis/_qa_render_mokun_1280x800.png` และ `analysis/_qa_render_mokun_full.png`
- [ ] Full-page screenshot ของ Octagram ที่ `analysis/_qa_render_mokun_octagram_1280x800.png`

### 3.4 · Red flags to watch

- 🟥 Red flag #1: Octagram Mermaid ปรากฏใน §1 (Cosmic Synergy) — fail
- 🟥 Red flag #2: 3×3 Square ไม่มี Mermaid block แต่เป็น HTML table — fail (mirror Win issue)
- 🟥 Red flag #3: 3×3 cell values ไม่ตรงกับ {2, 8, 7, 1, 8, 6, 9, 8, 8} — fail
- 🟥 Red flag #4: Mermaid block มี `<pre>` text แต่ไม่มี `<svg>` ข้างใน → render fail → fail

**Verdict:** ☐ PASS — ทั้ง 3×3 และ Octagram render เป็น SVG, Octagram อยู่ใน §8 ไม่ใช่ §1
☐ FAIL — render error, missing diagram, wrong position, or wrong values

---

## Check 4 — Content fidelity (Mokun-specific data integrity)

วัตถุประสงค์: ยืนยันว่า HTML มีค่าของ Mokun ครบถ้วน ไม่มี placeholder, ไม่หลงเหลือค่าจาก template/skeleton ที่ยังไม่ได้ substitute

### 4.1 · Required Mokun-specific strings

ทุก string ด้านล่างต้องปรากฏใน HTML **อย่างน้อย 1 ครั้ง**:

| # | String | Why |
|---|---|---|
| 1 | `Mokun` (literal) | subject name |
| 2 | `2 สิงหาคม 2005` หรือ `2 ส.ค. 2005` หรือ `2 สิงหาคม 2005` | DOB canonical |
| 3 | `ENTP-A` หรือ `ENTP · A` หรือ `ENTP` + assertive marker | MBTI — note: `-A` is critical |
| 4 | `戊土` (literal Han characters) หรือ `Yang Earth` หรือ `ภูเขา` | Day Master |
| 5 | `2-8-7` หรือ `2 – 8 – 7` หรือ `2 8 7` (Matrix anchor trio) | Matrix anchor |
| 6 | `Echo 8` หรือ `8 × 4` หรือ `Triple-Plus Echo` | Echo characterization |
| 7 | `Age 60` หรือ `อายุ 60` หรือ `Point of Arrival` | Age 60 anchor |
| 8 | `Period 9` หรือ `九紫離火運` หรือ `2024–2043` | Period 9 context |

### 4.2 · Optional but expected (presence adds confidence)

- [ ] `Wanderer` ใน §1.1 (Carl Jung Hero's Journey stage per MD line 23)
- [ ] `Strength` (Arcane XV) สำหรับ Matrix B=8 และ Echo
- [ ] `Sage-Strategist` ใน §8/§10 (Mokun-specific archetype per MD line 268, 413)
- [ ] `Si Grip` ใน §9.4 Crisis protocol (per MD line 521)
- [ ] `Su Yu Hong` (Su 雨虹) หรือ `苏雨虹` ใน §1.6 source citation

### 4.3 · Pass criteria

- [ ] **8 of 8 required strings** present in HTML body
- [ ] Zero typos in Day Master canonical form (ไม่เขียน "戊土" ผิดเป็น "戊士" / "戊士" / "成功" ฯลฯ)
- [ ] Number formatting consistent: "8 × 4" / "8x4" / "8 (4 ครั้ง)" ทั้งหมดยอมรับได้ ตราบเท่าที่ semantic ตรง

### 4.4 · How to verify

```bash
for s in "Mokun" "2 สิงหาคม 2005" "ENTP-A" "戊土" "2-8-7" "Echo 8" "Age 60" "Period 9" \
         "Wanderer" "Strength" "Sage-Strategist" "Si Grip" "苏雨虹"; do
  count=$(grep -F "$s" deliver/html/forecast-mokun.html | wc -l)
  echo "[$count] $s"
done

# Expected: every required string ≥ 1, every optional string ≥ 0
```

### 4.5 · Evidence

- [ ] Loop output above (presence counts)
- [ ] Manual spot-check: scan HTML body for `Mokun` occurrences — should be ≥ 5 (heading + intro + timeline + archetype references)

**Verdict:** ☐ PASS — all 8 required strings present, no typos in Day Master
☐ FAIL — missing any required string OR typo in canonical form

---

## Check 5 — No leftover Big / Win content

วัตถุประสงค์: ป้องกัน template leakage — ยืนยันว่า HTML ของ Mokun ไม่มีข้อมูลของ Big (DOB 14/9/1986) หรือ Win (DOB 19/9/1999) ปะปน

### 5.1 · Red-flag strings

| String | What it leaks |
|---|---|
| `Big` (in body) | subject name from prior template |
| `Win` (in body) | subject name from prior template |
| `14/9/1986` หรือ `14 ก.ย. 2529` หรือ `21/01/1986` หรือ `21 ม.ค. 2529` | Big's DOB |
| `19/9/1999` หรือ `2 ตุลาคม 1995` หรือ `2 ต.ค. 2538` | Win's DOB |
| `INTJ` หรือ `INTP` หรือ `INFP` หรือ `INFJ` | other personas' MBTI types — *not* ENTP |
| `乙 (Yin Wood)` (as Day Master) | Big's Day Master — contrast with Mokun's 戊 |
| `丙 (Yang Fire)` (as Day Master) | Win's Day Master — contrast with Mokun's 戊 |
| `21-1-6` หรือ `21 – 1 – 6` (Matrix anchor) | Big's matrix anchor trio |
| `2-10-6` หรือ `2 – 10 – 6` (Matrix anchor) | Win's matrix anchor trio |
| `CFR-21` หรือ `Senior Systems Analyst` หรือ `Te Grip` | Win's profession / framework |
| `INTP-A` | contrast with ENTP-A |

### 5.2 · Pass criteria (strict)

- [ ] **`grep -c "Big" deliver/html/forecast-mokun.html`** ≤ 2 (allow "Big" in citation/source list e.g. "Page forecast-big" or "rendered alongside forecast-big.html" — but **0 in body**)
- [ ] **`grep -c "Win" deliver/html/forecast-mokun.html`** ≤ 2 (same exception — only filename references, not body prose)
- [ ] **`grep -c "14/9/1986\|14 ก.ย. 2529\|21/01/1986\|21 ม.ค. 2529" deliver/html/forecast-mokun.html`** = 0
- [ ] **`grep -c "19/9/1999\|2 ตุลาคม 1995\|2 ต.ค. 2538" deliver/html/forecast-mokun.html`** = 0
- [ ] **`grep -c "INTJ\|INTP\|INFP\|INFJ\|ESTJ\|ESFP" deliver/html/forecast-mokun.html`** = 0 (only ENTP allowed; per MBTI section, MBTI types cited as compatibility are OK if the prose explicitly names them — but **the subject profile's MBTI must not contain other types**)
- [ ] **`grep -c "乙土\|丙土\|甲土\|丁土\|己土" deliver/html/forecast-mokun.html`** = 0 (Mokun's Day Master = 戊 only; any other Wu Earth variant would be a parsing error)
- [ ] **`grep -c "乙 (Yin Wood)\|丙 (Yang Fire)"` in body context** = 0 except in comparison/citation passages

### 5.3 · How to verify

```bash
cd /home/big/Documents/ommiself

echo "=== Subject name leakage ==="
grep -n "Big\|Win" deliver/html/forecast-mokun.html | head -20

echo "=== DOB leakage ==="
grep -n "14/9/1986\|14 ก.ย. 2529\|21/01/1986\|21 ม.ค. 2529\|19/9/1999\|2 ตุลาคม 1995" deliver/html/forecast-mokun.html
# expected: no output

echo "=== Wrong-Day-Master leakage ==="
grep -n "乙土\|丙土\|甲土\|丁土\|己土" deliver/html/forecast-mokun.html
# expected: no output

echo "=== Wrong-MBTI leakage ==="
grep -E "Mokun (is |has |is a )(INTJ|INTP|INFP|INFJ|ESTJ|ESFP)" deliver/html/forecast-mokun.html
# expected: no output
```

### 5.4 · Allowed exceptions

- ✅ `<a href="forecast-big.html">` หรือ filename references — ยอมรับได้ (UI navigation)
- ✅ Mermaid node labels ที่ระบุสำหรับ archetype อื่น — ไม่ควรมี (Mokun spec ไม่มี archetypal cross-reference ไปยัง Big/Win)
- ❌ Body prose "Mokun เหมือน Win ที่..." — ไม่อนุญาต (template leakage)

### 5.5 · Evidence

- [ ] Loop output ทั้ง 6 grep commands
- [ ] Decision: classification ของแต่ละ match (allowed filename vs violation)

**Verdict:** ☐ PASS — zero Big/Win DOB/MBTI/Day Master leakage in body
☐ FAIL — any DOB/MBTI/Matrix/Day Master leakage

---

## Check 6 — Thai readability (borrow from `_qa_thai_review.md`)

วัตถุประสงค์: สืบทอดมาตรฐานจาก Win MET-484 (Thai reviewer audit) — ยืนยันว่า HTML ของ Mokun ไม่มี AI-tell ที่รู้จัก overuse, ใช้ register สม่ำเสมอ

### 6.1 · AI-tell overuse check

| Pattern | Threshold |
|---|---|
| `อย่างมาก` | ≤ 2 occurrences ในทั้ง HTML |
| `ที่สุด` (ที่ใช้เป็น emphasis — ไม่ใช่ "ครั้งสุดท้าย") | ≤ 3 occurrences ในทั้ง HTML |
| `อย่างสมบูรณ์` | ≤ 1 occurrence |
| `อย่างจริงจัง` | ≤ 1 occurrence |
| `อย่างแท้จริง` | ≤ 2 occurrences (allowed if Jung framework citation) |
| spacing: `บ่อยๆ`, `เงียบๆ`, `จริงๆ` (no space) | **0 occurrences** — must be `บ่อย ๆ`, `เงียบ ๆ`, `จริง ๆ` |

### 6.2 · Pass criteria

- [ ] All threshold counts met
- [ ] No leftover `{{ ... }}` placeholders (cross-check Check 2)
- [ ] Glossary consistency: same Thai terms for same concepts across all sections (e.g. "Day Master" / "ดิถีธาตุ" ใช้สลับกันได้ แต่ต้องสลับในทิศทางเดียวกันทั้ง HTML)
- [ ] No Moji-bake / encoding corruption (e.g. `à¸à¸¥à¸à¸²à¸¡`) — meta charset must be UTF-8

### 6.3 · Allowed exceptions

- "ที่สุด" in literary/lit contexts: "ครั้งสุดท้าย", "ลึกที่สุด" (จำเป็น)
- "อย่างแท้จริง" ใน Jung individuation passages (framework term)
- "ที่สุด" / "มาก" ใน Mermaid labels — ขึ้นกับ render pipeline

### 6.4 · How to verify

```bash
echo "=== AI-tell frequency ==="
for pat in "อย่างมาก" "อย่างสมบูรณ์" "อย่างจริงจัง" "อย่างแท้จริง"; do
  c=$(grep -c "$pat" deliver/html/forecast-mokun.html)
  echo "[$c] $pat"
done

# count ที่สุด with non-final-year semantic:
grep -n "ที่สุด" deliver/html/forecast-mokun.html | \
  grep -v "ครั้งสุดท้าย\|ความยากที่สุด\|ลึกที่สุด\|สำคัญที่สุด" | wc -l

# spacing violation:
echo "=== No-space Thai reduplication ==="
grep -E "บ่อยๆ|เงียบๆ|จริงๆ|ดีๆ|มากๆ|น้อยๆ" deliver/html/forecast-mokun.html
# expected: no output

echo "=== Charset ==="
grep -i "charset" deliver/html/forecast-mokun.html | head -3
# expected: UTF-8
```

### 6.5 · Evidence

- [ ] AI-tell frequency table output
- [ ] Spacing violation grep output (empty if pass)
- [ ] Manual review by Thai-language speaker for 1 randomly chosen section (e.g. §1.1 or §5.3)

**Verdict:** ☐ PASS — all thresholds met, spacing clean, charset UTF-8
☐ FAIL — any threshold breach OR spacing violation OR encoding issue

---

## Check 7 — Render quality (headless screenshot, console errors)

วัตถุประสงค์: ยืนยันว่า HTML ทำงานใน headless browser ได้ ไม่มี console error, ทุก section แสดงผลใน viewport

### 7.1 · Pass criteria

- [ ] Page load ใน Chromium headless ที่ viewport 1280×800 สำเร็จ (HTTP 200 หรือ file:// OK)
- [ ] **0 console errors**
- [ ] **0 page errors**
- [ ] Section count visible at first viewport (≥ 1, ideally with hero/intro section)
- [ ] Full-page `scrollHeight` ≥ 2400 px (5+ viewports — long-form report expected)
- [ ] Mermaid SVG count ≥ 2 (3×3 + Octagram)
- [ ] No broken image elements (`<img>` without `alt` is OK; `<img>` with broken `src` = fail)
- [ ] No external network requests to non-whitelisted domains (เฉพาะ local file OK; ถ้ามี CDN fonts/Mermaid ที่ allow-listed ก็ OK)

### 7.2 · How to verify

```bash
# Mirror qa_render.py pattern (Win precedent)
python3 /tmp/qa_render_mokun.py > /tmp/qa_render_mokun_result.json

# Expected JSON keys: errors, svgCount, mermaidSvgs, sectionCount, scrollHeight
# Compare against expected thresholds above.

# Validate results:
python3 -c "
import json
r = json.load(open('/tmp/qa_render_mokun_result.json'))
assert len(r['errors']) == 0, f'Console/page errors: {r[\"errors\"]}'
assert r['mermaidSvgs'] >= 2, f'Mermaid SVGs: {r[\"mermaidSvgs\"]}'
assert r['sectionCount'] >= 10, f'Sections: {r[\"sectionCount\"]}'
assert r['scrollHeight'] >= 2400, f'Scroll height too small: {r[\"scrollHeight\"]}'
print('All render checks PASS')
"
```

### 7.3 · Visual artifacts to capture

- [ ] `analysis/_qa_render_mokun_1280x800.png` — first viewport (above-the-fold)
- [ ] `analysis/_qa_render_mokun_full.png` — entire page (1280 wide × full height)
- [ ] `analysis/_qa_render_mokun_octagram_1280x800.png` — viewport at §8 where Octagram renders
- [ ] `analysis/_qa_report_mokun.json` — JSON dump of Playwright metrics (mirror `_qa_report_win.json` pattern)

### 7.4 · Red flags

- 🟥 External `<script src="http://...">` ที่ load จาก CDN ที่ไม่ได้ allow-list — fail (privacy issue)
- 🟥 Console errors mentioning `mermaid`, `syntax`, `undefined`, `404` — fail
- 🟥 `<img>` with `src=` that 404s — fail
- 🟥 Scroll height < 2400 px (suspicious that sections are missing) — investigate

**Verdict:** ☐ PASS — 0 errors, ≥ 2 mermaid SVGs, ≥ 10 sections, ≥ 2400px scroll height
☐ FAIL — any of: console errors, missing sections, broken resources, Mermaid errors

---

## Composite verdict

QA reviewer ต้องรายงาน result ของทั้ง 7 checks ใน `analysis/_qa_audit_mokun.md` (mirror `_qa_audit.md` Win precedent) แล้วตัดสินว่า:

- ☐ **Composite PASS** — ทุก 7 checks ผ่าน — MET-497 (CTO render) ถือว่า render สำเร็จ, child issue สำหรับครั้งนี้ปิดได้
- ☐ **Composite FAIL** — มี ≥ 1 check fail — ต้องสร้าง child issues ตาม FAIL table ด้านล่าง

---

## FAIL-to-issue mapping (เมื่อ composite FAIL)

| Check | Symptom | Required child issue | Owner |
|---|---|---|---|
| 1 | Section count mismatch / missing heading | Child: "Mokun forecast HTML §X missing in render" → reassign to CTO/MET-497 owner | CTO agent (MET-497) |
| 2 | `{{ ... }}` leftover | Child: "Mokun forecast HTML has unresolved template tokens" | CTO (re-render) |
| 3a | Mermaid 3×3 doesn't render | Child: "Mokun 3×3 Natalia Square: Mermaid syntax error" | CTO |
| 3b | Octagram missing from §8 (per Win precedent) | Child: "Mokun Octagram misplaced or rendered as HTML table" | CTO |
| 4 | Missing Mokun-specific string | Child: "Mokun <string> not present in HTML — placeholder not substituted" | CTO |
| 5 | Big/Win content leakage | Child: "Mokun HTML has Big/Win content leakage — clean template substitution" | CTO |
| 6 | AI-tell overuse | Child: "Mokun HTML Thai polish: <pattern> overuse" → reassign to Thai Reviewer | Thai Reviewer agent |
| 7 | Console errors / broken render | Child: "Mokun HTML render failure: <error>" | CTO |

---

## Coordination hand-off

- **Trigger:** MET-502 (this issue) transitions to `done` เมื่อ checklist นี้ committed + child issues รอการ run (เมื่อ MET-497 ปิด).
- **Next step:** MET-497 (CTO render) ปิด → create child issue "QA: run Mokun acceptance checklist (link: analysis/_qa_checklist_mokun.md)" → assign to QA (this agent `289b1abf`).
- **QA action in next heartbeat:** copy this checklist เป็น `analysis/_qa_audit_mokun.md`, run all 7 checks, populate `Verdict` rows, file composite PASS/FAIL, แล้ว transition MET-502-related child issue ตาม FAIL table.

— จบ checklist —
