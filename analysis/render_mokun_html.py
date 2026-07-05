"""render_mokun_html.py — Render forecast-mokun.html + forecast-mokun-from-big-template.html.

Pipeline (mirrors MET-491 Win precedent + MET-504 Mokun precedent):

  Stage 1: read templates
    - COMPACT source = template/forecast-template.html          (variant A)
    - BIG     source = deliver/html/forecast-big.html           (variant B; pre-filled HTML)

  Stage 2: read Mokun anchors
    - analysis/_shared/bazi_calc_mokun.py                        (BaZi + PY sequence)
    - TOKEN_TABLE below                                          (Mokun identity strings)
    - 6 fresh specialist MDs (mokun_*.md)                         (per-lens prose source)

  Stage 3: token fill
    - replace every {{key}} with MOKUN_TOKEN_TABLE[key] (one-pass regex).

  Stage 4: zero-{{token}} sanity check
    - assert re.search(r'\\{\\{\\w+\\}\\}', html) is None. Failure ⇒ raise.

  Stage 5: variant B content-swap
    - clone forecast-big.html structure, replace Big-specific names/dates/numbers
      with Mokun equivalents. This is a content-replace pattern (no token schema).

  Stage 6: write outputs
    - deliver/html/forecast-mokun.html                            (variant A — template)
    - deliver/html/forecast-mokun-from-big-template.html          (variant B — big clone)

Usage:
  python3 analysis/render_mokun_html.py
  python3 analysis/render_mokun_html.py --check-only
  python3 analysis/render_mokun_html.py --out-dir /tmp/foo

Content freshness guarantee:
  Every string in this file derives from one of:
    - the 6 fresh Mokun specialist MDs (mokun_*.md)
    - the parent brief (analysis/MET-504-SEQUENCE-BRIEF.md)
    - the BaZi calc (analysis/_shared/bazi_calc_mokun.py)

  NO string is reused from:
    - the cancelled MET-493 mokun-omni-self-forecast.md
    - any Big/Win forecast HTML or MD
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path("/home/big/Documents/ommiself")
TEMPLATE_DIR = ROOT / "template"
DELIVER_DIR = ROOT / "deliver" / "html"
ANALYSIS_DIR = ROOT / "analysis"
SHARED_DIR = ANALYSIS_DIR / "_shared"

TEMPLATE_COMPACT = TEMPLATE_DIR / "forecast-template.html"
TEMPLATE_BIG = DELIVER_DIR / "forecast-big.html"


# ---------------------------------------------------------------------------
# BaZi + Numerology anchors (loaded at import time)
# ---------------------------------------------------------------------------

def _load_bazi() -> dict:
    """Pull Mokun's BaZi anchors from bazi_calc_mokun.py."""
    sys.path.insert(0, str(SHARED_DIR))
    import bazi_calc_mokun as mk  # type: ignore[import-not-found]
    return {
        "name": mk.NAME,
        "dob": "2005-08-02",
        "day_master_th": f"{mk.day_master} ({mk.dm_yin_yang}{mk.dm_element})",
        "year_p": mk.year_p,
        "month_p": mk.month_p,
        "day_p": mk.day_p,
        "hour_p": mk.hour_p,
        "dm_element_th": mk.dm_element,
        "dm_yin_yang_th": mk.dm_yin_yang,
        "eval_age": mk.years,
        "in_period_9": mk.in_period_9,
        "matrix": mk.MATRIX_NUMBERS,
        "echo": mk.ECHO_NUMBERS,
        "echo_cards": mk.ECHO_CARDS,
        "center": mk.MATRIX_CENTER,
        "echo_influence": mk.ECHO_INFLUENCE,
        "py_rows": mk.py_rows,
        "annual_pillars": mk.annual_pillars,
        "luck_pillars": mk.LUCK_PILLARS,
    }


BAZI = _load_bazi()


# ---------------------------------------------------------------------------
# Token table — every key here is filled by raw content from the 6 fresh MDs
# ---------------------------------------------------------------------------

MOKUN_TOKEN_TABLE: Dict[str, str] = {
    # ============== Header / identity ==============
    "person_name": "Mokun",
    "dob": "2 สิงหาคม 2005",
    "person_year_start": "2026",
    "person_year_end": "2065",
    "headline_reading": (
        "ปีของการหลอมภูเขา (2026-2044) — Period 9 ไฟหลอมดินหยาง 戊 · "
        "Echo 10-15-17 (Wheel-Devil-Star) ขับเคลื่อน 3 รอบ · "
        "สู่ PY 3 (Hierophant) ตอนอายุ 60 — วงล้อ 'คิด-เชื่อม-ปลด'"
    ),
    "summary_paragraph": (
        "Day Master 戊 Yang Earth (ภูเขา) เกิด 2 ส.ค. 2005 — Period 9 Fire หลอมดินเป็นเซรามิก 2024-2043 · "
        "Matrix 2-8-7 (High Priestess-Strength-Chariot) บน · Echo 10-15-17 ครอบ 6/9 ตำแหน่ง · "
        "PY 9 เริ่มอายุ 21 (2026) → PY 3 จบอายุ 60 (2065) · "
        "ENTP-A Ne-Ti เป็นฟังก์ชันหลัก แต่ BaZi บอกว่า 'ดินที่แข็งเกินไปต้อง drain ด้วย Water/Metal' — "
        "เส้นทางอาชีพ/การเรียนของ Mokun คือ 'ภูเขาที่เรียนรู้จะเป็นสะพาน' ไม่ใช่ 'ภูเขาที่ยืนนิ่ง'"
    ),

    # ============== Section 0 — Six lenses (header) ==============
    "lens_jung_persona": "Trickster/Explorer",
    "lens_jung_shadow": "Si-Grip + Fe-Loop",
    "lens_law_of_attraction_freq": "Mountain-with-fire-on-top (2-8-7)",
    "lens_kybalion_rhythm": "Seasonal Yang Earth — slow build, long plateau",
    "lens_kybalion_cause": "every seed in summer returns next autumn",
    "lens_mbti_type": "ENTP-A",
    "lens_mbti_lead": "Ne-Ti",
    "lens_mbti_grip": "Si-Grip under chronic stress (thesis deadline 2028)",
    "lens_age60_role": "Bridge-builder / Sage-advisor",
    "lens_age60_target": "build a school-of-bridges, not a single company",
    "lens_bazi_day_master": "戊 (Yang Earth)",
    "lens_bazi_balance": "needs 壬/癸 Water + 庚/辛 Metal (drain + wealth)",
    "lens_bazi_period9_fit": "Fire generates Earth — productive but draining (output relationship)",

    # ============== Section 0 — 6 expert summary rows ==============
    "analysis_0_jung": (
        "Persona=Trickster/Explorer, Shadow=Si-Grip/Fe-Loop — Individuation 4 phases "
        "(21-28 Trickster → 35-42 Hero → 43-55 Sage → 56-60 Hermit); Ego must integrate "
        "The Star (E=17) ก่อนอายุ 39 จึงจะผ่าน Period 9→1 transition"
    ),
    "analysis_0_myers": (
        "ENTP-A stack Ne-Ti-Fe-Si dominant — Si-Grip เป็นจุดบอดที่แท้จริง (ไม่ใช่ Fe-Loop); "
        "TY 2028 = graduation + Si-Grip window; strategy = harvest Ti under Ne ไม่ใช่ดัน Ne อย่างเดียว"
    ),
    "analysis_0_blavatsky": (
        "Dominant vibration 2-8-7 = 'mountain-with-fire-on-top'; dual vibration "
        "low-frequency Earth + high-frequency Star (17); LoA coherence locks ตอน 06:30 walk"
    ),
    "analysis_0_ladini": (
        "Matrix 2-8-7 บน / 10-17-15 กลาง / 17-10-15 ล่าง — Echo 10-15-17 ครอบ 6/9 ตำแหน่ง; "
        "กระจกสามด้าน (Wheel/Devil/Star) ไม่ใช่ห่วงโซ่ — The Star อยู่กลางผังคือผู้มอง"
    ),
    "analysis_0_initiates": (
        "Rhythm (KYB §V) + Mentalism (KYB §I) = main switch; Yang Earth rhythm ขึ้นช้า-อยู่นาน-พังทีเดียว; "
        "Mental Transmutation = Vibration × Mentalism × Polarity เปลี่ยนความถี่ก่อนเปลี่ยน Rhythm"
    ),
    "analysis_0_suyuhong": (
        "Day Master 戊 Yang Earth 太旺 (印比过旺) — 用神 = Water (壬/癸), 喜神 = Metal (庚/辛), "
        "忌神 = Fire/Earth; Period 9 Fire หลอมดินเป็นเซรามิก 2024-2043"
    ),

    # ============== Section 0 — Deep dives (12 tokens) ==============
    "analysis_deep_0_jung_persona_shadow": (
        "Persona = Trickster (เริ่มโครงการใหม่ไม่จบ) + Explorer (เห็นทุกความเป็นไปได้) — "
        "Shadow = Si-Grip (เมื่อ deadline thesis 2028 Ego ถอยเข้าห้องใต้ดินยึดรายละเอียดเก่า) + "
        "Fe-Loop (เมื่อเพื่อนผิดหวัง Ego สับสนอารมณ์คนอื่นกับข้อมูล) — สองเงานี้คือสิ่งที่บอร์ดสั่งเจาะ"
    ),
    "analysis_deep_0_jung_individuation_path": (
        "21-28 Trickster (Youth) → 35-42 Hero (Mid-life transition, 'The Tower Year') → "
        "43-55 Sage (Mature integration) → 56-60 Hermit (Elder) — Path นี้ผูกกับ Period 9→1 transition ที่อายุ 39"
    ),
    "analysis_deep_0_myers_type_stack": (
        "Ne (dominant — gather possibilities) → Ti (auxiliary — internal logic frame) → "
        "Fe (tertiary — read room) → Si (inferior — past-detail trap); lead function ปลดปล่อย, "
        "inferior function = grip point ต้อง integrate ไม่ใช่กดทับ"
    ),
    "analysis_deep_0_myers_cognitive_loop": (
        "Healthy loop: Ne→Ti→output → Si checkpoint รายสัปดาห์ · "
        "Unhealthy: Ne→Fe→loop (เดาอารมณ์คนอื่นจนสูญ Ti) · "
        "Si-Grip: Ti→Si→loop (ยึดรายละเอียดจนหยุด)"
    ),
    "analysis_deep_0_blavatsky_root_race": (
        "Root-race view: Mokun อยู่ใน 5th Root-Race (Aryan) consciousness — Ego+Personality "
        "กำลัง integrate Monad ผ่าน The Star (17); ไฟ Period 9 = collective fire ที่เร่งปลุก Monad"
    ),
    "analysis_deep_0_blavatsky_monad_reincarnation": (
        "Monad ของ Mokun คือ 'สะพาน' (bridge) — Ego ปัจจุบันเป็น Personality ที่ 7 (Hermit-trend); "
        "Soul mission = สอน/เชื่อม ไม่ใช่สร้าง empire; Reincarnation theme = repeat-as-bridge"
    ),
    "analysis_deep_0_ladini_natal_chart": (
        "Natal chart resonance: A=2 Priestess (silent-knower) · B=8 Strength (quiet authority) · "
        "C=7 Chariot (twin ancestral pulls) · Center E=17 Star (mission) · "
        "Echo 10-15-17 covers 6/9 cells = main architecture ไม่ใช่ background noise"
    ),
    "analysis_deep_0_ladini_transit_windows": (
        "Transit windows: 2026 (Saturn in Pisces — anchor personality), 2028-2030 (Saturn opposition — "
        "career test), 2039 (Saturn return ครั้งที่ 2), 2043 (Uranus return — Individuation milestone)"
    ),
    "analysis_deep_0_initiators_mystery_school": (
        "Mystery school: 'Mountain Mystery School' — ใช้ Earth frequency เป็น initiation chamber; "
        "เรียนรู้ผ่าน 'หินที่ละลาย' (เซรามิก) — ไม่ใช่ผ่านไฟโดยตรง; 7 ขั้น = Earth-elements"
    ),
    "analysis_deep_0_initiators_initiate_trials": (
        "Initiate trials: (1) Patience trial — รอ 3 ปี ไม่ได้ผล (2026-2028), (2) Authority trial — "
        "เผชิญ Manager ที่ไม่เข้าใจ (อายุ 25), (3) Founder trial — startup burn (อายุ 32), "
        "(4) Mirror trial — mid-life Ego death (อายุ 44), (5) Integration trial (อายุ 54)"
    ),
    "analysis_deep_0_suyuhong_day_master": (
        "Day Master 戊 Yang Earth (ภูเขา) — 太旺 ตามทุกเกณฑ์ (得月令/得地/得势/得气); "
        "用神 = Water (drain) + Metal (wealth); 忌神 = Fire/Earth (เติมแล้วแตก)"
    ),
    "analysis_deep_0_suyuhong_annual_pillars": (
        "Annual pillars 2026-2065: 丙午→丁未→戊申→己酉→庚戌→...→壬戌; "
        "Yang Earth ปีที่ flow ดี = 壬/癸 (Water control) และ 庚/辛 (Metal wealth); "
        "ปีที่ต้องระวัง = 丙/丁 (Fire seal — 印过旺) และ 戊/己 (Peer — 比劫)"
    ),

    # ============== Section 1 — Cosmic Synergy ==============
    "synergy_kybalion": (
        "Rhythm (KYB §V) + Mentalism (KYB §I) = main switch — Yang Earth rhythm ขึ้นช้า-อยู่นาน; "
        "Mental Transmutation ทำงานที่ความถี่ 06:30 walk + 21:00 review"
    ),
    "synergy_loa": (
        "Manifestation Loop = clarify → align → receive → act → gratitude — "
        "coherence locks ตอม 06:30 walk บนเขา (จริงหรือจำลอง); low-band trap = Si-Grip"
    ),
    "synergy_matrix": (
        "Center E=17 The Star + Echo 10-15-17 = phase-lock loop — "
        "Wheel (rhythm) + Devil (shadow) + Star (mission) หมุนรอบศูนย์เดียวกัน"
    ),
    "synergy_proof": (
        "Three engines climax อายุ 39 (ปี 2044) — Period 9→1 transition + Saturn return ครั้งที่ 2 + "
        "PY 9 (completion); Ego ต้อง integrate ก่อนถึงจุดนี้ มิเช่นนั้นจะพัง"
    ),

    # ============== Section 1 — 6 expert rows + deep dives ==============
    "analysis_1_jung": (
        "Engines: Persona (Ego-syntonic) + Shadow (Ego-dystonic) + Self (transcendent) — "
        "let all run ไม่ปิด Shadow; Si-Grip = Shadow talking loud"
    ),
    "analysis_1_myers": (
        "Ne gathers → Ti organizes → Fe seals → Si grounds; healthy stack ทำงานเป็นทีม, "
        "inferior Si เป็น safety net ไม่ใช่ villain"
    ),
    "analysis_1_blavatsky": (
        "Law satisfied เมื่อ intent (Mentalism) + emotion (Vibration) + action (Polarity) share frequency; "
        "alignment = ความคิด+อารมณ์+การกระทำสั่นที่ความถี่เดียวกัน"
    ),
    "analysis_1_ladini": (
        "3×3 with master centre 17 = phase-lock loop; Star ที่กลางเป็น carrier wave — "
        "honour centre โดยยอมรับว่า Ego เป็นแค่หนึ่งในผู้สังเกตการณ์"
    ),
    "analysis_1_initiates": (
        "Rhythm precedes Vibration precedes Form — inner moves outer; เปลี่ยน Rhythm ก่อน ค่อยเปลี่ยน Vibration ค่อยเปลี่ยน Form"
    ),
    "analysis_1_suyuhong": (
        "2044 (壬戌 Yang Water+EarthDog) = Water controls Earth — Period 9→1 transition, "
        "Day Master ถูกทดสอบ; Pillars บอกว่า Ego ต้อง integrate Water ก่อนถึงปีนั้น"
    ),
    "analysis_deep_1_jung_collective_unconscious": (
        "Collective Unconscious ของ Mokun = 'Mountain archetype' (Senex/Puer tension); "
        "Puer aeternus ในตัวเขาต้อง pair กับ Senex — Trickster+Hermit integration"
    ),
    "analysis_deep_1_jung_synchronicity": (
        "Synchronicity field: เมื่อ Ego อยู่ในจังหวะ The Star (17) — 'meaningful coincidences' จะหนาแน่นขึ้น; "
        "เมื่อ Ego ตกใน Si-Grip — synchronicity จะแห้ง"
    ),
    "analysis_deep_1_myers_function_integration": (
        "Function integration: dominant Ne + auxiliary Ti ใช้ทุกวัน; "
        "tertiary Fe ต้องฝึกตั้งแต่อายุ 21; inferior Si ต้อง acknowledge ไม่ปฏิเสธ"
    ),
    "analysis_deep_1_myers_type_development": (
        "Type development loop: ทุก 7 ปี ENTP-A จะ 'level up' — 21, 28, 35, 42, 49, 56; "
        "ทุกครั้งที่ level up Ego จะ integrate Fe+Si ได้ลึกขึ้น"
    ),
    "analysis_deep_1_blavatsky_hermetic_principles": (
        "7 principles active: Mentalism (Ne-Ti), Correspondence (Matrix-Earth), Vibration (D=10 Wheel), "
        "Polarity (Ne↔Si), Rhythm (Yang Earth), Cause/Effect (Ti), Gender (Androgyne Earth)"
    ),
    "analysis_deep_1_blavatsky_loa_bridge": (
        "LoA bridge: 'inner vibration = outer manifestation' — เปลี่ยน vibration ภายใน → โลกสะท้อนกลับ; "
        "manifestation Loop 5 ขั้น = clarify-align-receive-act-gratitude"
    ),
    "analysis_deep_1_blavatsky_matrix_loop": (
        "Matrix loop awareness: Center 17 + Echo 10-15-17 = locked loop; "
        "ถ้า Ego ไม่ observe loop นี้ จะถูก loop ลาก; ถ้า observe = loop กลายเป็น tool"
    ),
    "analysis_deep_1_ladini_outer_planet": (
        "Outer planet alignment: Uranus จะ trine natal Sun ในปี 2032 (อายุ 27) — "
        "individuation breakthrough; Neptune square natal Moon 2035 (อายุ 30) — emotional test"
    ),
    "analysis_deep_1_ladini_eclipse_season": (
        "Eclipse season impact: ทุก eclipse ในช่วง April-October จะ trigger The Wheel (10) — "
        "Mokun ควร track eclipse calendar เป็น rhythm marker"
    ),
    "analysis_deep_1_initiators_knowledge_awakening": (
        "Hidden knowledge awakening: เมื่อ Ego integrate The Star (17) Ego จะ 'ตื่น' — "
        "เห็น pattern ที่ซ่อนอยู่ในทุก event; นี่คือ 'initiation' ใน Mystery School"
    ),
    "analysis_deep_1_initiators_elemental_balance": (
        "Elemental balance: Earth ต้องการ Water (drain) + Metal (wealth) + Wood (control); "
        "Fire เติมมากเกินไปจาก Period 9 — ต้อง compensate ด้วย Water ritual"
    ),
    "analysis_deep_1_suyuhong_stems_branches": (
        "Heavenly Stems & Earthly Branches: Year 乙酉 (Yin Wood + Metal), Month 癸未 (Yin Water + Earth), "
        "Day 戊午 (Yang Earth + Fire), Hour 戊午 (Yang Earth + Fire) — Earth overload with Fire feeding"
    ),
    "analysis_deep_1_suyuhong_luck_cycle": (
        "Annual luck cycle: ปีที่ flow = 2027 (丁未 Yin Fire), 2032 (壬子 Yang Water), 2037 (丁未); "
        "ปีที่ caution = 2026 (丙午 Yang Fire — Fire overload), 2031 (辛丑 Yin Metal — 印 heavy)"
    ),

    # ============== Section 2 — Matrix 3x3 ==============
    "natalia_top_axis_value": "2 / 8 / 7",
    "natalia_top_token": "High Priestess (2) — Strength (8) — Chariot (7)",
    "natalia_mid_cycle": "10 / 17 / 15",
    "natalia_mid_token": "Wheel (10) — Star (17) — Devil (15)",
    "natalia_base_drive": "17 / 10 / 15",
    "natalia_base_mask": "17-Star drive / 10-Wheel persona / 15-Devil shadow",
    "natalia_echo_numbers": "10, 15, 17",
    "natalia_echo_influence": BAZI["echo_influence"],
    "natalia_A": "2", "natalia_B": "8", "natalia_C": "7",
    "natalia_D": "10", "natalia_E": "17", "natalia_F": "15",
    "natalia_G": "17", "natalia_H": "10", "natalia_I": "15",
    "natalia_A_token": "High Priestess — silent-knower",
    "natalia_B_token": "Strength — quiet authority",
    "natalia_C_token": "Chariot — twin ancestral pulls",
    "natalia_D_token": "Wheel of Fortune — career rhythm",
    "natalia_E_token": "The Star — bridge between heaven and earth",
    "natalia_F_token": "The Devil — self-made chains",
    "natalia_G_token": "The Star — inner drive of hope",
    "natalia_H_token": "Wheel of Fortune — social persona spins",
    "natalia_I_token": "The Devil — forgettable shadow chains",
    "natalia_center": "17",
    "natalia_echo_extended": (
        "Echo 10-15-17 ครอบคลุม 6 จาก 9 ตำแหน่งของผัง 3×3 — ไม่ใช่ background noise แต่เป็น "
        "สถาปัตยกรรมหลักของจิตวิญญาณ Mokun ทั้งสามตัวเลขทำงานร่วมกันเป็น 'กระจกสามด้าน' — "
        "Wheel สะท้อนจังหวะชีวิต, Devil สะท้อนเงาที่ถูกซ่อน, Star สะท้อนแสงที่แท้จริง — "
        "Mokun เกิดมาเพื่อ 'มอง' ทั้งสาม ไม่ใช่ถูกลาก"
    ),

    # ============== Section 2 — 6 expert rows + deep dives ==============
    "analysis_2_jung": (
        "Top=vision (Priestess-Strength-Chariot), base=drive (Star-Wheel-Devil); "
        "Mask = 'quiet spinner' (H=10 Wheel), underlying drive = 'inner hope' (G=17 Star)"
    ),
    "analysis_2_myers": (
        "Ne-Ti top axis, Fe-Si base axis; stack maps onto spatial axes — "
        "dominant functions ด้านบน (vision), inferior function ด้านล่าง (shadow)"
    ),
    "analysis_2_blavatsky": (
        "3×3 = frequency lattice; E=17 Star at centre is carrier wave; "
        "ทั้งผัง resonate ที่ความถี่ของการเป็นสะพาน"
    ),
    "analysis_2_ladini": (
        "Echo 10-15-17 in centre axis = mirror-triplet amplifier; "
        "lesson doubles because echo doubles — เห็นครั้งเดียวไม่พอ Ego ต้องเห็นซ้ำ"
    ),
    "analysis_2_initiates": (
        "Square embodies gender principle; centre = balance point between Masculine (Ne) "
        "and Feminine (Ti) — Androgyne Earth at equilibrium"
    ),
    "analysis_2_suyuhong": (
        "Top Earth (A=2 Priestess-Earth), Mid Earth (E=17 Star-Earth), Base Earth (G=17 Star-Earth) — "
        "ผังทั้งหมด Earth-dominant; ไฟ Period 9 หล่อเลี้ยงจากภายนอก"
    ),
    "analysis_deep_2_jung_center_periphery": (
        "Centre = The Self (E=17 Star) — centre ของจิตรวม; "
        "periphery = Persona+Shadow; Ego oscillates ระหว่าง centre กับ periphery"
    ),
    "analysis_deep_2_jung_shadow_corners": (
        "Shadow corners = F=15 Devil (F, I), H=10 Wheel — shadow ปรากฏที่ corner ของผัง; "
        "เงาที่ Mokun ลืมทำให้สมบูรณ์คือ 'พันธนาการที่สร้างเอง'"
    ),
    "analysis_deep_2_blavatsky_hermetic_geometry": (
        "Hermetic geometry: 3×3 square = base manifestation form; centre = quintessence; "
        "echo = harmonic resonance ที่ทำให้ผัง resonate แรงขึ้น"
    ),
    "analysis_deep_2_blavatsky_monad_descent": (
        "Monad descent: Monad ลงมาเป็น Personality ผ่าน 7 planes; "
        "Mokun อยู่ที่ plane 4 (Emotional) — กำลังขึ้นสู่ plane 5 (Mental)"
    ),
    "analysis_deep_2_initiators_initiate_path": (
        "Initiate path: Earth-initiate (7 steps of Mountain Mystery School) — "
        "(1) recognise stone, (2) carve form, (3) fire-fire-fire, (4) cool slowly, (5) reveal grain, (6) polish, (7) hand on"
    ),
    "analysis_deep_2_initiators_school_grid": (
        "School grid: 3×3 grid คือ 'curriculum' ของ Mountain Mystery School — "
        "ทุก cell คือ 1 lesson; centre = graduation; echo = repeat exam"
    ),
    "analysis_deep_2_ladini_chart_echo": (
        "Chart echo: 10-15-17 echo = triadic echo (3-fold repetition) — "
        "rare pattern; usually chart มี echo เดี่ยวหรือคู่; triadic echo = ชีวิตที่ integrate 3 ธีมพร้อมกัน"
    ),
    "analysis_deep_2_ladini_personal_year": (
        "Personal Year formula: PY(year) = reduce(Day=2) + reduce(Month=8) + reduce(YearSum(year)) "
        "= 10 + reduce(YearSum(year)) → reduce to 1-9; PY 9 ที่อายุ 21, 30, 39, 48, 57"
    ),
    "analysis_deep_2_myers_cognitive_mapping": (
        "Cognitive mapping: dominant (Ne, top) ↔ inferior (Si, bottom), "
        "auxiliary (Ti, mid-left) ↔ tertiary (Fe, mid-right); diagonal = creative tension"
    ),
    "analysis_deep_2_myers_type_dynamics": (
        "Type dynamics: ENTP-A 'Analyst' subtype — assertive variant = Ego มั่นคง, "
        "แต่ก็เสี่ยง Ego over-confident; ต้องมี Ti checkpoint ทุกสัปดาห์"
    ),
    "analysis_deep_2_suyuhong_stems_interaction": (
        "Stems interaction: 戊戊 same-pole (比肩 Peer) ที่ Day+Hour = 'ตัวเองซ้อนตัวเอง'; "
        "Year 乙 (正官 Officer) ดึงออกจาก comfort zone; Month 癸 (伤官 Hurting) ปากกล้า"
    ),
    "analysis_deep_2_suyuhong_trigram_mapping": (
        "Trigram mapping: Earth = 艮 Gen (Mountain) ที่ NE; Mokun = 'Mountain trigram person' — "
        "ยืนหยัด นิ่ง รับน้ำหนัก; complement = 兑 Dui (Lake) ที่ SW (relationship area)"
    ),

    # ============== Section 3 — Talent + Karmic ==============
    "talent_primary": (
        "Symbolic bridge-building — สะพานระหว่าง 'คนที่คิดได้' กับ 'คนที่ทำได้' "
        "(The Star E=17 เป็น carrier ของ talent นี้)"
    ),
    "talent_latent": (
        "Slow-deep craft (เซรามิก Earth) — งานที่ต้องใช้เวลา 'หลอม-เผา-เย็น-ขัด' "
        "เช่น งานเขียน long-form, mentorship, deep research"
    ),
    "karmic_pattern": (
        "Self-made chains (F=15 Devil) — 'ต้องเก่ง ต้องฉลาด ต้องไม่มีใครเห็นว่าฉันอ่อนแอ' "
        "ของ ENTP-A ที่ตก Ne-Ti loop"
    ),
    "karmic_lesson": (
        "Recognise the loose chain (โซ่ใน The Devil นั้นหลวม) — "
        "ปลดปล่อย self-imposed standard แล้วยอมรับ 'ฉันพอดีแล้วในแบบฉัน'"
    ),
    "karmic_extended": (
        "Karmic tail ของ Mokun มาจาก 'ห่วงโซ่แห่งความคาดหวัง' — Ego ในอดีตชาติสร้างความสำเร็จมาก "
        "จนติด; ชาตินี้ Ego ต้องเรียนรู้ 'ความสำเร็จที่ไม่ต้องพิสูจน์ตัวเอง' — "
        "The Star (17) คือ 'ดาวที่เปล่งแสงโดยไม่ต้องขอ'"
    ),

    # ============== Section 3 — 6 expert rows + deep dives ==============
    "analysis_3_jung": (
        "Latent = rejected (Devil self-imposed standard); primary = Hero (Star bridge-builder); "
        "Individuation ต้อง integrate ทั้งสอง shadow และ light"
    ),
    "analysis_3_myers": (
        "Primary = Ne-Ti (possibility + logic); latent = Si (slow craft); "
        "เมื่อ stack tire → tertiary Fe หรือ inferior Si จะ surface; ฝึก Si ทุกสัปดาห์"
    ),
    "analysis_3_blavatsky": (
        "Karmic pattern = low-frequency vibration (Earth-stuck); raise via daily ritual — "
        "LoA coherence lock ตอน 06:30 walk คือ 'vibration lift'"
    ),
    "analysis_3_ladini": (
        "Over-responsibility (Devil shadow) = shadow of master-centre (17 Star); "
        "ทำไม Ego รู้สึกว่า 'ต้องรับผิดชอบทุกอย่าง' — เพราะ The Star สะท้อนกลับมาว่า 'คุณเป็นสะพาน แต่ไม่ใช่ทุกคนต้องข้าม'"
    ),
    "analysis_3_initiates": (
        "Past-cause returns (Cause/Effect KYB §VI); unlock by re-seeding at higher octave — "
        "ทำสิ่งเดิมในระดับที่สูงขึ้น ไม่ใช่ทำสิ่งใหม่"
    ),
    "analysis_3_suyuhong": (
        "Favourable elements = Water (壬/癸) + Metal (庚/辛) = talent; "
        "clashes = Fire (印 过旺) = karmic tail; drain Fire ด้วย Water ritual (เดินริมน้ำ, เขียน stream-of-consciousness)"
    ),
    "analysis_deep_3_jung_talent_archetype": (
        "Talent archetype = The Magician (Star 17 + Trickster Persona) — "
        "คนที่ 'เปลี่ยนแร่เป็นทอง' ด้วยความคิด; archetype นี้ทรงพลังในช่วง mid-life"
    ),
    "analysis_deep_3_jung_karmic_pattern": (
        "Karmic pattern = Devil self-chains; pattern นี้ activate ทุกครั้งที่ Ego รู้สึกว่า 'ไม่พอ' — "
        "ego-ideal สูงเกินไป; ให้ Ego รู้จัก 'พอ' ก่อนทุกครั้ง"
    ),
    "analysis_deep_3_myers_natural_strength": (
        "Natural strength = Ne-Ti combo — 'vision + logic' — "
        "เห็นความเป็นไปได้หลายทาง แล้วเลือกทางที่ logical ที่สุด; "
        "strength นี้คือ competitive advantage ของ Mokun"
    ),
    "analysis_deep_3_myers_shadow_gift": (
        "Shadow gift = Si (slow detail, body memory) — "
        "ตอนที่ Si-Grip ทำงาน Ego จะ 'จำ' ทุกอย่าง — ใช้ gift นี้โดยตั้งใจ journal ทุกสัปดาห์"
    ),
    "analysis_deep_3_blavatsky_soul_mission": (
        "Soul mission = 'bridge-builder' — เชื่อม heaven กับ earth, "
        "เชื่อม possibility กับ execution, เชื่อม Ego กับ Self"
    ),
    "analysis_deep_3_blavatsky_karmic_lesson": (
        "Karmic lesson = 'recognise loose chain' — "
        "ห่วงโซ่ของ Devil นั้นปลดได้ทุกเมื่อ Ego เลือก; การปลดห่วงโซ่ = Individuation"
    ),
"analysis_deep_3_ladini_karmic_debt": (
        "Karmic debt = 'unkept promise from past' — "
        "เคยสัญญาว่าจะ 'สอน' แต่ไม่ได้สอน; ชาตินี้ Ego ต้อง 'สอน' อย่างน้อย 1 คน"
    ),
    "analysis_deep_3_ladini_soul_contract": (
        "Soul contract = 'bridge 7 souls' — "
        "เชื่อม 7 คนเข้าด้วยกันในช่วงชีวิต; เมื่อ Ego เชื่อม 7 คนสำเร็จ สัญญาเสร็จ"
    ),
    "analysis_deep_3_initiators_initiate_gift": (
        "Initiate gift = 'Stone-to-ceramic transmutation' — "
        "เปลี่ยน 'หินดิบ' (raw material) เป็น 'เซรามิก' (refined output) — "
        "gift นี้คือ slow craft ของ Mokun"
    ),
    "analysis_deep_3_initiators_karmic_mirror": (
        "Karmic mirror = 'the first student' — "
        "คนที่ Mokun สอนคนแรกจะเป็น 'mirror' ที่สะท้อน shadow ให้เห็น — "
        "เตรียมตัวให้พร้อมรับ feedback ที่เจ็บ"
    ),
    "analysis_deep_3_suyuhong_bazi_talent": (
        "BaZi talent = Water (壬/癸) + Metal (庚/辛) — "
        "งานที่ involve fluid intelligence (writing, analysis, design, code, water-related fields) "
        "หรืองานที่ involve structure (engineering, finance, law) จะ amplify talent ของ Mokun"
    ),
    "analysis_deep_3_suyuhong_karmic_resolution": (
        "Karmic resolution = 'drain Fire, accumulate Water+Metal' — "
        "lifestyle: เดินริมน้ำทุกสัปดาห์, เขียน stream-of-consciousness, สะสม knowledge assets (books, courses)"
    ),

    # ============== Section 4 — Career & Roles ==============
    "career_industry": (
        "Ed-tech platform · Knowledge-product business · Strategy consulting · "
        "Research lab · UX/Product design (ระบบที่ 'เชื่อม' คนกับความรู้)"
    ),
    "career_income_pattern": (
        "Lumpy retainer + royalty tail (Water/Metal pattern) — "
        "รายได้มาจาก knowledge-product (course, book, IP) ที่ 'หลอม' ทีละชิ้น"
    ),
    "career_peak_window": (
        "2034 Q2 – 2037 Q4 (อายุ 29-32, 壬子-丁未) — "
        "Water+Metal Luck Pillar (己卯→庚寅) เปิด peak window"
    ),
    "role_boss": "Holds the 'why' (Star 17 mission), defers the 'how' (Wheel 10 rhythm)",
    "role_boss_token": "vision-bearer",
    "role_sub": "Follows the 'why' once signed in (Ti internal frame becomes the how)",
    "role_sub_token": "loyal executor",
    "role_active": "Ships under deadline, cuts scope live (Ne-Ti fast iteration)",
    "role_active_token": "launcher",
    "role_receptive": "Absorbs feedback, integrates quietly (Ti + Si checkpoint)",
    "role_receptive_token": "mirror",

    # ============== Section 4 — 6 expert rows + deep dives ==============
    "analysis_4_jung": (
        "Boss=Persona (Trickster), Sub=Shadow (Si-Grip mature); "
        "pick consciously ไม่ใช่ autopilot — รู้ว่าเมื่อไหร Ego เป็น Trickster vs Sage"
    ),
    "analysis_4_myers": (
        "Boss=Ne-Ti (vision+logic), Sub=Fe-Si (only when trust built); "
        "active/receptive = E/I lead; team role = 'Idea Guy' → 'Idea Maker' after graduation 2028"
    ),
    "analysis_4_blavatsky": (
        "Industry fit = vibration match, not credential — "
        "Mokun จะ 'flow' เมื่ออยู่ในงานที่ vibration ตรงกับ Mountain-with-fire-on-top"
    ),
    "analysis_4_ladini": (
        "Four roles = four cardinal cells (A=2 vision, C=7 drive, F=15 shadow, I=15 shadow); "
        "peak = centre (E=17 Star) holds all four — when Ego centres, all roles align"
    ),
    "analysis_4_initiates": (
        "Role-at-work = universe rehearsing larger Self (as above, so below); "
        "งานของ Mokun คือ 'ห้องทดลอง' สำหรับ Soul Mission"
    ),
    "analysis_4_suyuhong": (
        "Ed-tech/Strategy/R&D fits Yang Earth + Water drain; "
        "2032-2037 (己卯 Luck Pillar) = best window; 忌 = corporate sales (印 overload)"
    ),
    "analysis_deep_4_jung_career_persona": (
        "Career persona evolution: 21-28 Trickster → 28-35 Founder → 35-42 Hero → 42-55 Sage → 55-60 Hermit; "
        "แต่ละ persona ต้อง 'ตาย' ก่อน persona ใหม่จะเกิด"
    ),
    "analysis_deep_4_jung_career_growth": (
        "Career growth through Individuation: growth ≠ promotion, growth = depth; "
        "Ego โตเมื่อ integrate Shadow ได้ลึกขึ้น ไม่ใช่เมื่อได้ title สูงขึ้น"
    ),
    "analysis_deep_4_myers_career_stack": (
        "Career stack mapping: Ne (vision) drives career, Ti (logic) builds system, "
        "Fe (people) seals deals, Si (detail) maintains operations"
    ),
    "analysis_deep_4_myers_team_role": (
        "Team role = 'Idea Catalyst' — เริ่มโปรเจกต์ เห็นภาพ แล้วส่งต่อให้คนที่ 'ship' เก่งกว่า; "
        "role นี้ peak หลังอายุ 28 เมื่อ Ego เลิกยึดติดว่า 'ต้องเป็นคนทำเอง'"
    ),
    "analysis_deep_4_blavatsky_vocation_path": (
        "Vocation path = 'Mountain Mystery School teacher' — "
        "อายุ 35+ Mokun จะเริ่ม 'สอน' ไม่ใช่แค่ 'ทำ'; นี่คือ vocation จริงของ Mokun"
    ),
    "analysis_deep_4_blavatsky_money_consciousness": (
        "Money consciousness = 'output value' (Water/Metal — drain + wealth); "
        "Mokun จะรู้สึก wealthy เมื่อ produce output ที่มีคุณค่า ไม่ใช่เมื่อ accumulate เงิน"
    ),
    "analysis_deep_4_ladini_midheaven_transit": (
        "Midheaven transit: Saturn ผ่าน midheaven ในปี 2029-2031 — "
        "career milestone; Mokun จะตัดสินใจครั้งใหญ่เกี่ยวกับ career path"
    ),
    "analysis_deep_4_ladini_career_house": (
        "Career house (10th house) activation: natal 10th house มี The Star (17) influence — "
        "career = 'mission', ไม่ใช่ 'job'"
    ),
    "analysis_deep_4_initiators_initiate_vocation": (
        "Initiate vocation = 'Mountain teacher' — "
        "สอนคนอื่นให้รู้จัก 'ภูเขาในตัวเอง' (own mountain = own Day Master awareness)"
    ),
    "analysis_deep_4_initiators_work_ritual": (
        "Work-life ritual = 'Mountain-time' — 30 นาที silence ก่อนเริ่มงาน + 60 นาที reflection หลังเลิก; "
        "ritual นี้ทำให้ Ego integrate Rhythm (KYB §V)"
    ),
    "analysis_deep_4_suyuhong_career_bazi": (
        "Career BaZi = Yang Earth wants 'big, slow, lasting' — "
        "งานที่ใหญ่ใช้เวลา 5-10 ปี (not 1-2 ปี startup churn); "
        "best fit = research lab, knowledge platform, foundational IP"
    ),
    "analysis_deep_4_suyuhong_wealth_element": (
        "Wealth element = Metal (庚/辛) — "
        "Mokun จะร่ำรวยจาก 'structural assets' (IP, royalties, knowledge products) "
        "ไม่ใช่จาก quick flips หรือ trading"
    ),

    # ============== Section 5 — Relationships & Lines ==============
    "love_pattern": "Long fuse, deep burn (slow build เหมือน Earth)",
    "love_pull": "People who challenge without judging (Anima = Wise Woman / Sophia)",
    "love_blind_spot": "Confuses intensity for depth (Fe-Loop — เดาอารมณ์คนอื่นจนเข้าใจผิด)",
    "line_father": (
        "Duty-quiet engineer (Year Pillar 乙酉 Yin Wood+Metal) — "
        "silent approval; พ่อจะไม่พูดว่า 'เก่ง' แต่จะส่ง resources มาให้"
    ),
    "line_mother": (
        "Expressive healer (Month Pillar 癸未 Yin Water+Earth) — "
        "emotional vocabulary; แม่จะสอน 'ภาษาอารมณ์' ที่ Ti ไม่มี"
    ),
    "relationships_extended": (
        "Anima ของ Mokun = 'The Wise Woman' (Sophia) — ผู้หญิงที่ 'รู้ก่อนพูด' "
        "เหมือน The High Priestess (A=2) ใน Matrix; เมื่อ Mokun project Anima ลงบน partner จริง "
        "เขาจะมอง partner เป็น 'คนที่สอนฉันได้' ซึ่งอาจทำให้ Ego เสียสมดุล — partner ที่ดีคือ "
        "คนที่ reject Anima projection แล้วเป็น 'คนจริง' ของตัวเอง"
    ),

    # ============== Section 5 — 6 expert rows + deep dives ==============
    "analysis_5_jung": (
        "Inner pull = Anima (Wise Woman Sophia); blind spot = inferior Si projected onto partner — "
        "Mokun จะ project 'past-memory' ลงบน partner (อดีต relationship) ทำให้มอง partner ใหม่ผ่านเลนส์เก่า"
    ),
    "analysis_5_myers": (
        "Long-fuse-deep-burn = Ne-Ti intimacy (slow build); "
        "Fe-Loop in relationship = 'เดาว่า partner คิดอะไร' จน Ego สูญเสีย Ti clarity"
    ),
    "analysis_5_blavatsky": (
        "Love = vibration duet (Hermetic Correspondence); re-tune ไม่ใช่ re-pick — "
        "เมื่อ vibration ไม่ตรงกัน ให้ re-tune โดยไม่ต้อง 'หาใหม่'"
    ),
    "analysis_5_ladini": (
        "Paternal line (Year Pillar) = inherited corner (A=2 Priestess); "
        "Maternal line (Month Pillar) = inherited corner (B=8 Strength); "
        "current = centre (E=17 Star) integrating both"
    ),
    "analysis_5_initiates": (
        "Love = correspondence (KYB §II); pull = rhythm seeking octave — "
        "Mokun จะดึงดูดคนที่ vibration เป็น octave ที่สูงกว่า/ต่ำกว่าตัวเอง"
    ),
    "analysis_5_suyuhong": (
        "Spouse palace (日支 午 Fire) needs Water/Metal balance — "
        "partner ที่ดีคือ Water-sign (Pisces/Scorpio) หรือ Earth-sign (Capricorn/Virgo) — "
        "ไม่ใช่ Fire-sign เพราะจะ overload 印"
    ),
    "analysis_deep_5_jung_anima_animus": (
        "Anima integration: 21-28 Ego projects Anima on external (romantic idealisation); "
        "28-35 Ego starts to recognise Anima as internal wisdom; 35+ Anima = integrated guide"
    ),
    "analysis_deep_5_jung_relationship_pattern": (
        "Relationship pattern = 'puer-senex' dynamic — Mokun มีทั้ง Puer (eternal youth, "
        "อยากสำรวจ) และ Senex (mountain wisdom, อยาก rooted); partner ที่ดีคือคนที่ balance สองด้านนี้"
    ),
    "analysis_deep_5_myers_communication_style": (
        "Communication style = 'Ti→Ne broadcast' — "
        "Mokun จะ 'วิเคราะห์' ก่อน 'พูด' แต่ output เป็น Ne (possibility) — "
        "ทำให้ partner รู้สึก 'เห็นได้หลายมุม แต่ไม่รู้ว่าเขาตัดสินใจอะไร'"
    ),
    "analysis_deep_5_myers_love_language": (
        "Love language = 'intellectual mirroring' (Ti-Ne duet) — "
        "Mokun รู้สึก loved เมื่อ partner 'เล่นปัญญา' ด้วย; gift, touch, words of affirmation ไม่สำคัญเท่า"
    ),
    "analysis_deep_5_blavatsky_twin_flame": (
        "Twin flame archetype = 'Sophia-Magus' — "
        "Mokun จะดึงดูดคนที่ 'รู้' (Sophia) เท่ากับ 'ทำ' (Magus); twin flame อยู่ที่ vibration octave เดียวกัน"
    ),
    "analysis_deep_5_blavatsky_generational_wisdom": (
        "Generational wisdom lineage: Year Pillar (paternal) → Month Pillar (maternal) → "
        "Day Pillar (Mokun) → Hour Pillar (children) — ต้องส่งต่อ 'Earth wisdom' ให้ลูก"
    ),
    "analysis_deep_5_ladini_venus_return": (
        "Venus return ที่อายุ 25 (2030) — relationship milestone; "
        "Ego จะตัดสินใจครั้งใหญ่เกี่ยวกับ long-term partner"
    ),
    "analysis_deep_5_ladini_seventh_house": (
        "7th house (partnership) activation: natal 7th house มี Wheel (10) influence — "
        "partnership = 'rhythmic' ไม่ใช่ 'fated'"
    ),
    "analysis_deep_5_initiators_sacred_union": (
        "Sacred union = 'Mountain-Lake' (Earth-Water complement, 艮-兑); "
        "partner ที่ดีคือคนที่ complement Earth ด้วย Water/Earth ไม่ใช่ Fire"
    ),
    "analysis_deep_5_initiators_generational_mission": (
        "Generational mission = 'bridge wisdom across generations' — "
        "Mokun จะเป็นสะพานระหว่าง Gen Z/Millennial กับ silent generation ของครอบครัว"
    ),
    "analysis_deep_5_suyuhong_spouse_palace": (
        "Spouse palace (日支 午 = Fire) — "
        "partner มักจะ Fire-sign ตามธรรมชาติ แต่ Ego ต้องเลือก Water/Earth partner เพื่อ balance"
    ),
    "analysis_deep_5_suyuhong_relationship_luck": (
        "Relationship luck peaks: 2029-2031 (己酉 Year) = 己 Yin Earth mate; "
        "2034-2036 (甲寅 Year) = 寅 Wood → control Earth = tension but transformative; "
        "2043 (癸亥 Year) = deepest partnership window"
    ),

    # ============== Section 6 — Health Card & Chakras ==============
    "hc_1_phys": "Crown clarity — Yang Earth strong, head steady",
    "hc_1_eng": "Mission pull — The Star (17) activates",
    "hc_1_emo": "Quiet certainty — 8-Strength emotional stability",
    "hc_2_phys": "Sharp perception — Ne dominant",
    "hc_2_eng": "Insight surges — Ti moments of clarity",
    "hc_2_emo": "Quiet pride — competence-based self-worth",
    "hc_3_phys": "Voice strength — Strong voice projection",
    "hc_3_eng": "Steady output — Earth consistency",
    "hc_3_emo": "Even temper — High Priestess silence",
    "hc_4_phys": "Open chest — Earth generosity",
    "hc_4_eng": "Warm circulation — Fe tertiary warmth",
    "hc_4_emo": "Trust earned — slow trust building",
    "hc_5_phys": "Core stability — Yang Earth 太旺",
    "hc_5_eng": "Sunlit drive — Period 9 Fire feeding",
    "hc_5_emo": "Quiet confidence — Mountain groundedness",
    "hc_6_phys": "Easy flow — body accepts change",
    "hc_6_eng": "Creative tide — Wheel rhythm",
    "hc_6_emo": "Soft joy — when aligned with mission",
    "hc_7_phys": "Grounded body — Mountain root",
    "hc_7_eng": "Restful current — Earth-rest",
    "hc_7_emo": "Patient root — Senex wisdom emerging",
    "hc_result_phys": "17",
    "hc_result_eng": "8",
    "hc_result_emo": "17",
    "health_watch": (
        "Solar plexus (Manipura) over-heats under deadline sprints — "
        "Si-Grip จะสะสมที่นี่; watch เมื่อ Ego ทำงานหนักเกิน 14 วันติด"
    ),
    "health_balance": (
        "90-min walk ริมน้ำ (Water element) + 30-min journaling — "
        "ritual นี้ drain Fire ที่สะสมในช่วง Period 9"
    ),
    "health_extended": (
        "Mokun เป็น Yang Earth 太旺 ตาม BaZi — ร่างกาย 'แข็งแรง' แต่ 'ท่อตัน' "
        "เมื่อ Ego ไม่ drain Fire/Peer ออก จะเกิด stagnation; "
        "สุขภาพที่ดีของ Mokun = exercise ที่ involve Water (ว่ายน้ำ, เดินริมน้ำ, แช่น้ำ) + "
        "Metal (breath-work ที่เป็นระบบ, cold exposure) — "
        "อย่าเล่น Fire sport (HIIT หนัก) เป็นเวลานาน"
    ),

    # ============== Section 6 — 6 expert rows + deep dives ==============
    "analysis_6_jung": (
        "7 chakras = 7 archetypes (Crown=Sage, Third Eye=Magician, Throat=Trickster, "
        "Heart=Lover, Solar Plexus=Warrior, Sacral=Explorer, Root=Mountain)"
    ),
    "analysis_6_myers": (
        "Phys=Se, eng=Ni, emo=Fi — ENTP-A's 7th/8th function development; "
        "phys/eng/emo totals = 17/8/17 = self-aware + competent + integrated"
    ),
    "analysis_6_blavatsky": (
        "Chakras = fixed vibration; imbalance = dissonance between two adjacent chakras; "
        "Mokun จะมี Crown-Throat harmony แต่ Solar-Sacral dissonance บ่อย"
    ),
    "analysis_6_ladini": (
        "Health card = 3×3 on body; Σ = over-amp or balanced; "
        "Mokun's Σ = 42 (over-amp) = Ego ต้อง drain ผ่าน Water ritual"
    ),
    "analysis_6_initiates": (
        "Body = densest octave (Rhythm KYB §V applied to soma); "
        "solar plexus = where cause enters soma — chronic deadline stress จะ 'ฝัง' ที่นี่"
    ),
    "analysis_6_suyuhong": (
        "Chakra ↔ Five Elements: Crown=Earth, Third Eye=Water, Throat=Metal, "
        "Heart=Wood, Solar=Fire, Sacral=Water, Root=Earth — Mokun's chart = Earth-Water balance"
    ),
    "analysis_deep_6_jung_body_shadow": (
        "Body as Shadow: เมื่อ Ego ignore body signals = body becomes Shadow vessel; "
        "Mokun ต้อง 'ฟัง' body ไม่ใช่แค่ 'ใช้' body"
    ),
    "analysis_deep_6_jung_wholeness_practice": (
        "Wholeness practice = 'Mountain-body meditation' — "
        "20 นาที/day นั่งนิ่ง รู้สึก 'ภูเขาในตัว' — integrate body+mind"
    ),
    "analysis_deep_6_myers_energy_management": (
        "Energy management = 'Pomodoro + Earth-rest' — "
        "25 นาที Ne-Ti focus + 5 นาที Si-rest (walk, water, breath) — cycle 4 ครั้ง = 1 Earth-block"
    ),
    "analysis_deep_6_myers_stress_response": (
        "Stress response = 'Si-Grip early-warning' — "
        "เมื่อ Ego เริ่มหยุดนิ่ง + ยึดรายละเอียดซ้ำ = Si-Grip; ให้ trigger Water ritual ทันที"
    ),
    "analysis_deep_6_blavatsky_etheric_body": (
        "Etheric body = subtle template ของ physical body — "
        "Mokun's etheric body มี Earth-stability แต่ Water-flow ต้องเสริม"
    ),
    "analysis_deep_6_blavatsky_kundalini": (
        "Kundalini rising: เมื่อ Mokun integrate Si (inferior function) kundalini จะ rise จาก Root ขึ้น Crown; "
        "ระวัง 'premature rising' = Si-Grip ก่อน integration เสร็จ"
    ),
    "analysis_deep_6_ladini_sixth_house": (
        "6th house (health, daily routine) activation: natal 6th house มี Wheel (10) influence — "
        "สุขภาพ = 'rhythmic routine' ไม่ใช่ 'one-time cure'"
    ),
    "analysis_deep_6_ladini_healing_transit": (
        "Healing transit: Jupiter trine natal Sun ในปี 2031 — "
        "healing milestone; Mokun จะ 'ปล่อย' chronic condition ที่แบกมานาน"
    ),
    "analysis_deep_6_initiators_chakra_activation": (
        "Chakra activation: Crown→Root (top-down) = 'Senex path'; "
        "Root→Crown (bottom-up) = 'Puer path'; Mokun ทำ top-down (integrating wisdom) จากอายุ 28+"
    ),
    "analysis_deep_6_initiators_energy_field": (
        "Energy field = 'Mountain aura' — "
        "Mokun มี energy field ที่ 'นิ่งและลึก' คนรอบข้างจะรู้สึก grounded เมื่ออยู่ใกล้"
    ),
    "analysis_deep_6_suyuhong_five_elements": (
        "5 Elements balance target: Earth 5 → 4 (drain slightly), Fire 3 → 2 (drain), "
        "Water 1 → 3 (boost), Metal 1 → 2 (boost), Wood 2 → 2 (maintain)"
    ),
    "analysis_deep_6_suyuhong_body_constitution": (
        "Body constitution = 'Earth-strong, Water-weak' (土旺水弱) — "
        "แนะนำอาหาร Water-element (ส้ม, แตงโม, ชาเขียว), Metal-element (หัวหอม, กระเทียม) เสริม"
    ),

    # ============== Section 7 — Stages & Year-by-Year ==============
    "stage_1_theme": "Trickster / Explorer — compass-build",
    "stage_1_marker": "Senior project จบ + ตัดสินใจ career path",
    "stage_2_theme": "Hero / Self individuation — calibration",
    "stage_2_marker": "First authentic creation + first real 'burn'",
    "stage_3_theme": "Sage / Ruler — collision",
    "stage_3_marker": "Founder burnout / mid-life Ego death",
    "stage_4_theme": "Sage mature — integration",
    "stage_4_marker": "School-of-bridges pilot launch",
    "stage_5_theme": "Hermit — delivery",
    "stage_5_marker": "Wisdom-book 'Letter to young ENTP' released",

    # Year-by-year (5-year snapshot, age 21 → 25) — required by template
    "career_year_1": "2026",
    "career_year_1_age": "21",
    "career_year_1_energy": "PY 9 + 丙午 Yang Fire",
    "career_year_1_situation": "Final year + Period 9 Fire peak (overheat warning)",
    "career_year_1_strategy": "Si — anchor to body rhythm + slow detail (ก่อน Si-Grip)",
    "career_year_1_detail": (
        "Mokun อายุ 21 ปี — final year มหาวิทยาลัย · Period 9 Fire เต็มที่ · "
        "PY 9 = completion year ของรอบก่อน · risk = Si-Grip เมื่อ deadline thesis; "
        "strategy = walk ริมน้ำ 06:30 ทุกวัน + journal 30 นาที · ไม่ดัน Ne อย่างเดียว"
    ),
    "career_year_2": "2027",
    "career_year_2_age": "22",
    "career_year_2_energy": "PY 1 + 丁未 Yin Fire",
    "career_year_2_situation": "Graduation year — new chapter seed",
    "career_year_2_strategy": "Ne — explore 3 career paths พร้อมกัน (ไม่ commit เร็ว)",
    "career_year_2_detail": (
        "PY 1 = new beginning · 丁未 Yin Fire = softened Fire (ไม่ overheat เท่าปีก่อน); "
        "Mokun ควร explore 3 career paths เพื่อ integrate Ne · ไม่ commit เร็ว — "
        "Yang Earth ต้อง 'ก่อร่าง' ก่อนสร้างต่อ"
    ),
    "career_year_3": "2028",
    "career_year_3_age": "23",
    "career_year_3_energy": "PY 2 + 戊申 Yang Earth",
    "career_year_3_situation": "First real job — Si-Grip window เปิด",
    "career_year_3_strategy": "Ti — measure twice, sign once (slow craft)",
    "career_year_3_detail": (
        "PY 2 = partnership/crystallisation · 戊申 Yang Earth+Metal = Earth-supporting year; "
        "first job — risk Si-Grip สูงสุด · strategy = Ti 'measure twice' — "
        "อย่า commit project ใหญ่ในปีนี้ · focus = integrate Fe กับทีม"
    ),
    "career_year_4": "2029",
    "career_year_4_age": "24",
    "career_year_4_energy": "PY 3 + 己酉 Yin Earth",
    "career_year_4_situation": "Expression year — first public output",
    "career_year_4_strategy": "Fe — feel the room before answering",
    "career_year_4_detail": (
        "PY 3 = expression · 己酉 Yin Earth + Metal — Ego 'ออกมา' พูด/ทำ/สร้าง; "
        "first public output (blog, talk, product launch) · strategy = Fe (people-first); "
        "warn: 印过旺 trap (over-feeling) — balance ด้วย Ti checkpoint"
    ),
    "career_year_5": "2030",
    "career_year_5_age": "25",
    "career_year_5_energy": "PY 4 + 庚戌 Yang Metal",
    "career_year_5_situation": "Foundation year — Venus return + career milestone",
    "career_year_5_strategy": "Si — anchor to one sensory ritual daily",
    "career_year_5_detail": (
        "PY 4 = foundation · 庚戌 Yang Metal — Metal คือ喜神ของ Mokun! · "
        "ปีนี้ Ego จะ 'รู้สึก grounded' ครั้งแรก · Venus return (relationship milestone); "
        "Saturn enters midheaven transit — career foundation ที่แท้จริง · "
        "strategy = Si (anchor ritual) — don't skip"
    ),

    # ============== Section 7 — 6 expert rows + deep dives ==============
    "analysis_7_jung": (
        "5 stages = 5 individuation cycles; S3 = dark night (อายุ 32 Founder burnout), "
        "S4 = integrate (อายุ 44 mid-life crisis — 'Tower Year')"
    ),
    "analysis_7_myers": (
        "Stages rotate lead function: S1 Ne (explore), S2 Ti (build), S3 Fe (feel), "
        "S4 Si (ground), S5 balanced; year-strategy picks function"
    ),
    "analysis_7_blavatsky": (
        "Coherence ↑ S1-S2, peak S3→S4 (Tower transition = peak intensity), settle S5; "
        "year = dominant vibration; PY 9 ทุก 9 ปี = completion + new cycle"
    ),
    "analysis_7_ladini": (
        "5 stages = 5 master cycles; year-by-year = matrix at full resolution; "
        "PY 9 years (อายุ 21, 30, 39, 48, 57) = Wheel of Fortune peak (10 echo)"
    ),
    "analysis_7_initiates": (
        "5×12=60 convergence — 5 stages × 12 PY slots = 60 year cycle; "
        "crisis mastery = polarity applied to overwhelm — กลับขั้วเมื่อถูก overwhelm"
    ),
    "analysis_7_suyuhong": (
        "Stage-element = luck-pillar flow; year = Personal# + annual stem; "
        "丁巳 Luck Pillar (อายุ 13-22) — Fire feeding Earth; "
        "戊辰 Luck Pillar (อายุ 23-32) — Earth + Earth (caution: 比劫); "
        "己卯 Luck Pillar (อายุ 33-42) — Yin Earth + Wood (control); "
        "庚寅 Luck Pillar (อายุ 43-52) — Metal + Wood (wealth + control — PEAK)"
    ),
    "analysis_deep_7_jung_life_arc": (
        "Life arc: 21-28 Youth (Trickster) → 28-35 Early Adult (Founder) → "
        "35-42 Mid-life transition (Hero) → 42-55 Mature (Sage) → 55-60 Elder (Hermit); "
        "Trickster 'ตาย' ที่ 28 (Founder 'เกิด'); Founder 'ตาย' ที่ 35 (Hero 'เกิด')"
    ),
    "analysis_deep_7_jung_midlife_transition": (
        "Mid-life transition (อายุ 35-42) — Hero individuation crisis; "
        "Ego ต้อง integrate Persona (Trickster) กับ Shadow (Devil) เป็น Self (Star)"
    ),
    "analysis_deep_7_myers_cognitive_aging": (
        "Cognitive aging: ENTP-A's Ne stays sharp ตลอดชีวิต (strength); "
        "Ti deepens หลังอายุ 35; Fe matures หลังอายุ 42; Si integrates หลังอายุ 50"
    ),
    "analysis_deep_7_myers_wisdom_function": (
        "Wisdom function = Fe-Si integration — "
        "หลังอายุ 50 Mokun จะ 'อ่านคน' ได้แม่นยำขึ้น (Fe mature) "
        "และ 'จำบทเรียน' ได้ดีขึ้น (Si integrate) — นี่คือ 'Sage mode'"
    ),
    "analysis_deep_7_blavatsky_reincarnation_cycle": (
        "Reincarnation cycle: Mokun อยู่ที่ Personality ที่ 7 (Hermit-trend); "
        "ครั้งหน้า Ego จะขึ้นเป็น Personality ที่ 8 (Cosmic Teacher); "
        "ปัจจุบัน = integration phase"
    ),
    "analysis_deep_7_blavatsky_year_energy": (
        "Year energy theme: PY 1-3 = build, PY 4-6 = adapt, PY 7-9 = harvest; "
        "อายุ 21-29 = PY 9,1,2,3,4,5,6,7,8 (full 9-cycle); "
        "อายุ 39 = PY 9 again (completion of 1st master cycle)"
    ),
    "analysis_deep_7_ladini_saturn_return": (
        "Saturn return ครั้งที่ 1 (อายุ ~29, ปี 2034) — career milestone; "
        "Saturn return ครั้งที่ 2 (อายุ ~58, ปี 2063) — life review; "
        "Saturn opposition (อายุ ~21, ปี 2026) — first major test"
    ),
    "analysis_deep_7_ladini_progressed_moon": (
        "Progressed Moon: เดือนที่ Ego เกิด (August) — progressed Moon จะผ่านทุก sign ทุก ~2.5 ปี; "
        "track progressed Moon เป็น 'emotional season' indicator"
    ),
    "analysis_deep_7_initiators_year_theme": (
        "Year theme (Mystery School): ทุกปีคือ '1 บทเรียน' — "
        "PY 9 = graduation, PY 1 = enrollment, PY 2-3 = foundation, PY 4-6 = practice, "
        "PY 7-8 = mastery, PY 9 = graduation again"
    ),
    "analysis_deep_7_initiators_annual_ritual": (
        "Annual ritual = 'Mountain-year review' (ธันวาคมของทุกปี) — "
        "ทบทวน 'ปีนี้ภูเขาเรียนรู้อะไร' — Ego จะเห็น pattern ที่ซ่อนอยู่"
    ),
    "analysis_deep_7_suyuhong_decade_luck": (
        "Decade Luck Pillars: 丁巳 13-22 (Fire-feeding Earth — caution 印) → "
        "戊辰 23-32 (Earth-Earth — 比劫 risk, especially year 25 = 庚戌 Metal-wealth ดี) → "
        "己卯 33-42 (Earth-Wood — control, BEST for 30s) → "
        "庚寅 43-52 (Metal-Wood — PEAK for career + wealth) → "
        "辛丑 53-62 (Metal-Earth — late success)"
    ),
    "analysis_deep_7_suyuhong_pillars_reading": (
        "Annual pillars reading: 2026 丙午 (Fire overload), "
        "2032 壬子 (Yang Water — best for soul), "
        "2037 丁未 (Yin Fire balanced), "
        "2044 壬戌 (Yang Water+EarthDog — Period 9→1 transition), "
        "2055 乙卯 (Yin Wood control — late flow)"
    ),

    # ============== Section 8 — Protocols ==============
    "protocol_daily": (
        "06:30 walk ริมน้ำ 30 นาที (Water element) + 21:00 journaling 30 นาที (Metal element) — "
        "ritual นี้ drain Fire ที่ Period 9 เติมทุกวัน"
    ),
    "protocol_weekly": (
        "Sunday 90-min 'Mountain-walk' + 1 mentor call (Water + Earth ritual) — "
        "ทบทวนสัปดาห์ + ถาม mentor เรื่อง Si-Grip warning"
    ),
    "protocol_monthly": (
        "Full-day retreat — review 5 stages + Matrix 3×3 + 10-year Luck Pillar — "
        "ทบทวน Rhythm (KYB §V) ของชีวิต"
    ),
    "protocol_crisis": (
        "10-min box-breath + cold face plunge + write 'one anchor sentence' (The Star 17) — "
        "ถ้า Si-Grip มา: 'I am the mountain, not the avalanche' (re-anchor to Day Master)"
    ),
    "protocol_extended": (
        "Earth-craft ritual = 'ทำของชิ้นหนึ่ง' ที่ใช้เวลา 2-3 ชั่วโมงต่อสัปดาห์ — "
        "เขียน long-form, ปั้น clay, เล่น instrument, code from scratch — "
        "ritual นี้คือ 'Stone-to-ceramic transmutation' ที่ integrate Si (inferior) อย่างสร้างสรรค์"
    ),

    # ============== Section 8 — 6 expert rows + deep dives ==============
    "analysis_8_jung": (
        "Daily = Ego↔Body, Weekly = Ego↔Self, Monthly = Ego↔Collective, "
        "Crisis = Ego↔Shadow (Si-Grip) — 4-axis protocol"
    ),
    "analysis_8_myers": (
        "Walk=Se feed, call=Ni-Fe, retreat=Ni dive, breath=Fi-grip override; "
        "ENTP-A ต้องมี 'Si checkpoint' ทุกสัปดาห์ — Pomodoro + journaling"
    ),
    "analysis_8_blavatsky": (
        "Daily raises vibration, Weekly stabilises, Monthly resets, Crisis = emergency override; "
        "LoA loop: clarify→align→receive→act→gratitude"
    ),
    "analysis_8_ladini": (
        "Daily=cell, Weekly=row, Monthly=centre, Crisis=full-square reset; "
        "Matrix 3×3 protocol maps 1:1 กับ daily-weekly-monthly-crisis rhythm"
    ),
    "analysis_8_initiates": (
        "Practice = conscious Rhythm (KYB §V); without practice rhythm runs Ego — "
        "Earth rhythm ต้อง conscious practice ไม่งั้น unconscious rhythm จะพา Ego ไป Si-Grip"
    ),
    "analysis_8_suyuhong": (
        "Walk=Wood (slight), forest=Wood+Water, retreat=Earth, breath=Metal dispersal; "
        "BaZi daily: 1 glass warm water (06:30) + journal + walk"
    ),
    "analysis_deep_8_jung_shadow_work": (
        "Shadow work protocol: 'Devil dialogue' — เขียนจดหมายถึง 'inner critic' ทุกสัปดาห์ — "
        "Ego จะเห็นว่า 'critic' นั้นคือ 'self-imposed standard' ที่ปลดได้"
    ),
    "analysis_deep_8_jung_individuation_ritual": (
        "Individuation ritual = 'Star meditation' — "
        "นั่ง 20 นาที visualize The Star (E=17) แล้วถามตัวเองว่า 'ฉันเป็นสะพานไปไหน'"
    ),
    "analysis_deep_8_myers_development_plan": (
        "Development plan = 'Function rotation' — "
        "เดือนนี้ฝึก Fe, เดือนหน้าฝึก Si, หมุนเวียน — integrate ทั้ง stack ทุกปี"
    ),
    "analysis_deep_8_myers_team_collaboration": (
        "Team collaboration = 'Ti→Fe bridge' — "
        "Mokun จะ communicate กับทีมด้วย 'Ti frame' (logic) แล้ว 'Fe seal' (empathy); "
        "ห้าม 'Ne broadcast' อย่างเดียว (overwhelm ทีม)"
    ),
    "analysis_deep_8_blavatsky_seven_principles": (
        "7 Principles practice: each day 1 principle — Mon Mentalism, Tue Correspondence, "
        "Wed Vibration, Thu Polarity, Fri Rhythm, Sat Cause/Effect, Sun Gender"
    ),
    "analysis_deep_8_blavatsky_karma_yoga": (
        "Karma Yoga = 'work as worship' — "
        "Mokun จะ integrate ได้ดีที่สุดเมื่อมองงานเป็น 'practice' ไม่ใช่ 'obligation'"
    ),
    "analysis_deep_8_ladini_planetary_remedy": (
        "Planetary remedy: Saturn (career) — wear black/dark blue on Saturdays; "
        "Mercury (communication) — wear green on Wednesdays; Jupiter (wisdom) — Thursday yellow"
    ),
    "analysis_deep_8_ladini_daily_astro": (
        "Daily astro: check Moon sign + void-of-course Moon ก่อนตัดสินใจใหญ่; "
        "track progressed Moon รายเดือน — 'emotional season' indicator"
    ),
    "analysis_deep_8_initiators_pathworking": (
        "Pathworking = 'Mountain visualization' — "
        "20 นาที/day: visualize climbing mountain (representing Individuation path) — "
        "เมื่อถึง 'summit' Ego จะรู้สึก 'Self integration'"
    ),
    "analysis_deep_8_initiators_mantra_practice": (
        "Mantra = 'I am the mountain, I am the bridge' — "
        "พูด 21 ครั้ง/day (อายุปัจจุบัน) · mantras เปลี่ยนตาม phase (อายุ 21-28 'Mountain', "
        "28-35 'Bridge', 35-42 'Star', 42-55 'Sage', 55-60 'Hermit')"
    ),
    "analysis_deep_8_suyuhong_feng_shui": (
        "Feng Shui: โต๊ะทำงานหันหน้า North (Water direction) — "
        "ห้องนอนหัน South-West (Earth direction); สีประจำตัว = blue (Water) + white (Metal)"
    ),
    "analysis_deep_8_suyuhong_bazi_daily": (
        "BaZi daily practice: 06:30 warm water, 12:00 balance meal (Earth+Water+Metal), "
        "18:00 light dinner, 21:00 reflection; avoid 00:00-02:00 late work (Fire hour overload)"
    ),

    # ============== Section 9 — Synthesis ==============
    "synthesis_interconnectedness": (
        "MBTI Ne-Ti ตรงกับ BaZi Yang Earth (戊) ทั้งคู่เป็น 'ผู้สร้างโครงสร้าง'; "
        "Matrix Center 17 (The Star) ขยายทั้งสอง — คนเดียวกันปรากฏในทุกเลนส์ — "
        "ทุกศาสตร์บอกว่า Mokun คือ 'ภูเขาที่เรียนรู้จะเป็นสะพาน'"
    ),
    "synthesis_ultimate_truth": (
        "Build bridges first; the company is what the bridges teach"
    ),
    "synthesis_extended": (
        "ทุกเลนส์ — Jung, MBTI, Matrix, LoA, Kybalion, BaZi — converge ที่ 1 ความจริง: "
        "Mokun เกิดมาเพื่อ 'เชื่อม' (bridge) ไม่ใช่ 'สร้าง empire'; "
        "Persona 'Trickster/Explorer' จะ integrate เป็น 'Sage/Teacher' เมื่ออายุ 35+; "
        "Soul Mission = 'Mountain Mystery School teacher' — สอนคนอื่นให้รู้จัก 'ภูเขาในตัวเอง'; "
        "อายุ 60 Mokun จะยืนอยู่ศูนย์กลางของดาว 8 แฉก (The Star) — ไม่ใช่ 'ผู้นำ' แต่ 'ผู้เชื่อม'"
    ),

    # ============== Section 9 — 6 expert rows + deep dives ==============
    "analysis_9_jung": (
        "School = Self's first expression; company = Persona supporting the school; "
        "Individuation = 'ภูเขากลายเป็นสะพาน' (Ego เชื่อมตัวเองกับโลก)"
    ),
    "analysis_9_myers": (
        "All 4 integrated: Ne sees, Ti builds, Fe protects, Si grounds — "
        "Sage mode (อายุ 50+) = full integration · ENTP-A's final gift = 'Teacher of possibilities'"
    ),
    "analysis_9_blavatsky": (
        "School = highest vibration; company = carrier wave; "
        "Mokun's Monad = 'bridge-builder' — Universal Brotherhood served ผ่าน 'bridges between souls'"
    ),
    "analysis_9_ladini": (
        "E=17 Star = school-key handed; build school first, company is side-effect; "
        "Soul Contract = 'bridge 7 souls' — when 7 souls bridged, contract complete"
    ),
    "analysis_9_initiates": (
        "School = mind's highest octave; company = working octave — same mind; "
        "Universal Service = 'teach the Mountain Mystery School method' to next generation"
    ),
    "analysis_9_suyuhong": (
        "Period 9 Yang Earth = teacher-years (2024-2043); "
        "teach (school) > structure (company) — 用神 wisdom: drain Fire via Water teaching"
    ),
    "analysis_deep_9_jung_the_self": (
        "The Self = E=17 Star at Matrix centre = the 'organising principle' of Mokun's psyche; "
        "Ego ที่ align กับ Self = individuated Mokun — at age 60 this becomes permanent"
    ),
    "analysis_deep_9_jung_meaning_of_life": (
        "Meaning of life (for Mokun) = 'to bridge heaven and earth'; "
        "Mokun's life has meaning เมื่อ Ego ทำหน้าที่ 'สะพาน' ให้คนอื่นเดินทาง"
    ),
    "analysis_deep_9_myers_final_integration": (
        "Final integration: Ne-Ti-Fe-Si all integrated → 'Sage ENTP-A'; "
        "rare archetype — most ENTP-A stay Trickster ตลอดชีวิต; Mokun's potential = Sage"
    ),
    "analysis_deep_9_myers_type_wisdom": (
        "Type wisdom = 'possibility + logic + empathy + memory' — "
        "Sage ENTP-A คือ 'คนที่เห็นความเป็นไปได้ + สร้าง logic + เข้าใจคน + จำบทเรียน' — "
        "ครบเครื่องที่สุดใน 16 types"
    ),
    "analysis_deep_9_blavatsky_universal_brotherhood": (
        "Universal Brotherhood: Mokun serve ผ่าน 'Mountain Mystery School' — "
        "สอนคนให้รู้จัก Day Master ของตัวเอง; ไม่ใช่ religion แต่เป็น 'practical self-knowledge'"
    ),
    "analysis_deep_9_blavatsky_final_aspiration": (
        "Final aspiration = 'Mokun the Bridge' — "
        "ทุกคนที่ Ego เชื่อม (7 souls) จะจำ Mokun ในฐานะ 'คนที่ทำให้โลกเชื่อมถึงกัน'"
    ),
    "analysis_deep_9_ladini_contract_completion": (
        "Soul contract completion: เมื่อ Mokun bridge 7 souls (อายุ ~50-55) contract จะสมบูรณ์; "
        "หลังจากนั้น Mokun มี 'free will' — Ego เลือกเอง"
    ),
    "analysis_deep_9_ladini_chart_mastery": (
        "Chart mastery: Mokun จะ 'อ่าน' chart ของคนอื่นได้แม่นยำ — "
        "talent นี้ peak หลังอายุ 42 (post-Tower); Mountain Mystery School = apply chart-reading ในชีวิตจริง"
    ),
    "analysis_deep_9_initiators_mastery_path": (
        "Mastery path = '7-step Mountain Initiation' complete; "
        "Mokun = Master of Mountain Mystery School ที่อายุ 55-60"
    ),
    "analysis_deep_9_initiators_universal_service": (
        "Universal Service = 'teach 7 generations' — "
        "Mokun's students (direct + indirect) จะส่งต่อ Mountain Mystery School ไปอีก 7 generations"
    ),
    "analysis_deep_9_suyuhong_destiny_unfoldment": (
        "Destiny unfoldment: 戊 Day Master 太旺 → 用神 Water+Metal = "
        "Mokun's destiny คือ 'หลอมดินเป็นเซรามิก' (Earth → Earth+Water+Metal = refined output); "
        "ทุก output ของ Mokun คือ 'ceramic' — durable, beautiful, valuable"
    ),
    "analysis_deep_9_suyuhong_final_blessing": (
        "Final blessing (from Su Yu Hong): 'ภูเขาของ Mokun จะไม่มีวันถล่ม "
        "เพราะ Ego ได้เรียนรู้การ drain Fire และสะสม Water+Metal แล้ว — "
        "ขอให้ Ego จงเป็นสะพาน ไม่ใช่กำแพง'"
    ),

    # ============== Footer ==============
    "template_version": "2.1",
    "generated_at": "2026-07-05",

    # ============== Legacy aliases (kept for backward compat) ==============
    "zone_label": "Common energy",
    "row_1": "Sahasrara (Crown)",
    "row_2": "Ajna (Third Eye)",
    "row_3": "Vishuddha (Throat)",
    "row_4": "Anahata (Heart)",
    "row_5": "Manipura (Solar Plexus)",
    "row_6": "Svadhisthana (Sacral)",
    "row_7": "Muladhara (Root)",
    "career_year_1_label": "Reframe — Si anchor before Si-Grip hits.",
    "career_year_2_label": "Build — explore 3 paths, don't commit early.",
    "career_year_3_label": "Ship — first job, Ti 'measure twice'.",
    "career_year_4_label": "Express — first public output, Fe balance.",
    "career_year_5_label": "Anchor — Venus return + Metal-wealth year.",

    # ============== Octagram (8-direction tokens for cosmic synergy diagram) ==============
    "octagram_center": "E=17 The Star · Self · Mission",
    "octagram_n": "Mentalism · KYB §I · Ne-Ti",
    "octagram_ne": "Vibration · LoA · Mountain-with-fire",
    "octagram_e": "Matrix Loop · Wheel-Star-Devil",
    "octagram_se": "BaZi · Day Master 戊 · Period 9 Fire",
    "octagram_s": "Jung · Shadow · Si-Grip + Fe-Loop",
    "octagram_sw": "Natalia · Saturn Return · Transit",
    "octagram_w": "Polarity · KYB §IV · Ne↔Si · Ti↔Fe",
    "octagram_nw": "Mystery · Mountain Initiation · 7 trials",
}


# ---------------------------------------------------------------------------
# Fill + verify + write
# ---------------------------------------------------------------------------

def _fill(html: str, table: Dict[str, str]) -> str:
    """Replace every {{token}} with table[token]."""
    keys_in_html = set(re.findall(r"\{\{(\w+)\}\}", html))

    def repl(match: "re.Match[str]") -> str:
        key = match.group(1)
        if key in table:
            return table[key]
        raise ValueError(f"missing token in table: {key!r}")

    out = re.sub(r"\{\{(\w+)\}\}", repl, html)
    residual = re.findall(r"\{\{\w+\}\}", out)
    if residual:
        # Defense-in-depth — repl above should have raised already.
        raise ValueError(f"unfilled tokens remain: {residual[:5]}")
    return out


def _first_unfilled(html: str) -> str | None:
    m = re.search(r"\{\{(\w+)\}\}", html)
    return m.group(0) if m else None


def render_compact(out_path: Path) -> dict:
    if not TEMPLATE_COMPACT.exists():
        raise FileNotFoundError(f"missing template: {TEMPLATE_COMPACT}")
    raw = TEMPLATE_COMPACT.read_text(encoding="utf-8")
    filled = _fill(raw, MOKUN_TOKEN_TABLE)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(filled, encoding="utf-8")
    return {"path": str(out_path), "tokens_used": len(MOKUN_TOKEN_TABLE)}


def render_big_clone(out_path: Path) -> dict:
    """Variant B — content-swap from forecast-big.html (Big's structure) → Mokun.

    Strategy: regex-replace Big-specific names/dates/numbers with Mokun equivalents.
    This is NOT a token-fill (Big's HTML has no {{token}} schema) — it's a content
    rewrite that keeps Big's CSS/layout/structure but replaces every Big-specific
    string with a Mokun-specific string.
    """
    if not TEMPLATE_BIG.exists():
        raise FileNotFoundError(f"missing big template: {TEMPLATE_BIG}")
    raw = TEMPLATE_BIG.read_text(encoding="utf-8")

    # Big → Mokun content swap.
    swaps: List[Tuple[str, str]] = [
        # Names
        (r"\bBig\b", "Mokun"),
        (r"\bJitti\b", "Mokun"),
        (r"\bKunphruk\b", "Mokun"),
        (r"\bJitti Kunphruk\b", "Mokun"),
        # DOB
        (r"21\s*มกราคม\s*2529", "2 สิงหาคม 2548"),
        (r"21\s*มกราคม\s*1986", "2 สิงหาคม 2005"),
        (r"21/01/1986", "02/08/2005"),
        (r"21-01-1986", "02-08-2005"),
        (r"\b2529\b", "2548"),
        (r"\b1986\b", "2005"),
        # MBTI / Type
        (r"\bENTJ(?:-A)?\b", "ENTP-A"),
        # BaZi — Day Master
        (r"\b乙\s*\(Yin Wood\)", "戊 (Yang Earth)"),
        (r"\b乙\s*\(Yin\s*Wood\s*/\s*กล้าไม้\)", "戊 (Yang Earth / ภูเขา)"),
        (r"\b乙\s*木\b", "戊 土"),
        (r"\bYin\s*Wood\b", "Yang Earth"),
        (r"\b乙木\b", "戊土"),
        # BaZi other stems (Big's chart-specific)
        (r"\b甲子\b", "乙酉"),
        (r"\b乙丑\b", "癸未"),
        (r"\b戊辰\b", "戊午"),
        # Matrix numbers (Big uses Wheel-of-Fortune D=E=G=10)
        (r"\bD\s*=\s*E\s*=\s*G\s*=\s*10\b", "Echo 10-15-17"),
        (r"\bD\s*=\s*E\s*=\s*G\s*=\s*10", "Echo 10-15-17 (Wheel-Devil-Star)"),
        (r"\b21\s*/\s*1\s*/\s*6\b", "2 / 8 / 7"),
        (r"\b21\s*-\s*1\s*-\s*6\b", "2-8-7"),
        # Age / window
        (r"\b40\s*ปี\b", "40 ปี"),
        (r"\b2024\s*[-–]\s*2046\b", "2026-2065"),
        (r"\b2024\s*[-–]\s*2044\b", "2026-2065"),
        (r"\b2026\s*[-–]\s*2046\b", "2026-2065"),
        # Personal Year base
        (r"\bPersonal\s*Year\s*8\b", "Personal Year 9"),
    ]
    out = raw
    for pattern, repl in swaps:
        out = re.sub(pattern, repl, out)

    # Sanity: no Big/Win-bleed should remain in body (allow methodology footer only)
    forbidden = ["Jitti", "Kunphruk", "ENTJ", "21/01/1986", "21-01-1986",
                 "21 มกราคม 2529", "21 มกราคม 1986", "Yin Wood",
                 "D=E=G=10", "ENTJ-A"]
    # methodology footer exception
    methodology_zone = out.rsplit("methodology", 1)
    if len(methodology_zone) > 1:
        body, foot = methodology_zone[0], methodology_zone[1]
    else:
        body, foot = out, ""
    leaks = []
    for f in forbidden:
        if f in body:
            leaks.append(f)
    if leaks:
        raise ValueError(
            f"variant B still contains Big-specific strings in body: {leaks}. "
            "Add more swaps before shipping."
        )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(out, encoding="utf-8")
    return {"path": str(out_path), "swaps_applied": len(swaps), "leaks": leaks}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    p.add_argument("--check-only", action="store_true",
                   help="Verify zero-token check + Big/Win-bleed check, then exit.")
    p.add_argument("--out-dir", type=Path, default=DELIVER_DIR,
                   help=f"Directory for outputs (default: {DELIVER_DIR}).")
    args = p.parse_args()

    summary = {"tokens_provided": len(MOKUN_TOKEN_TABLE)}

    if args.check_only:
        raw = TEMPLATE_COMPACT.read_text(encoding="utf-8")
        first = _first_unfilled(_fill(raw, MOKUN_TOKEN_TABLE))
        print(f"[compact] {TEMPLATE_COMPACT.name}: {'OK' if first is None else f'FAIL on {first}'}")
        if first:
            return 1
        # Big clone check-only
        try:
            _ = render_big_clone(args.out_dir / "forecast-mokun-from-big-template.html.tmp")
            print("[big] swap-clean (no Big-bleed in body)")
            (args.out_dir / "forecast-mokun-from-big-template.html.tmp").unlink(missing_ok=True)
        except ValueError as e:
            print(f"[big] FAIL: {e}")
            return 1
        return 0

    summary["compact"] = render_compact(args.out_dir / "forecast-mokun.html")
    summary["big"] = render_big_clone(args.out_dir / "forecast-mokun-from-big-template.html")
    summary["person_name"] = BAZI["name"]
    summary["day_master"] = BAZI["day_master_th"]
    summary["echo"] = BAZI["echo"]
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())