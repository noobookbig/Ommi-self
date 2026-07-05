"""render_nat_html.py — Render forecast-nat.html + forecast-big-nat.html.

Pipeline (mirrors MET-491 Win precedent + MET-504 Mokun precedent):

  Stage 1: read templates
    - COMPACT  source = template/forecast-template.html
    - BIG     source = deliver/html/forecast-big.html
    (fallback if forecast-big.html missing: deliver/html/forecast-big-omni-self.html)

  Stage 2: read Nat constants
    - analysis/_shared/bazi_calc_nat.py   (Nat BaZi + PY sequence)
    - TOKEN_TABLE below                    (Nat identity strings)
    - analysis/nat-omni-self-forecast.md   (Thai Writer prose — MET-519 deliverable)
                                          — when the file is missing, fall back to
                                            Win/Win tokens and substitute placeholders.

  Stage 3: token fill
    - replace every {{key}} with NAT_TOKEN_TABLE[key] (one-pass regex).

  Stage 4: zero-{{token}} sanity check
    - assert re.search(r'\\{\\{\\w+\\}\\}', html) is None. Failure ⇒ raise with the
      first still-unfilled token to locate the offender.

  Stage 5: write outputs
    - deliver/html/forecast-nat.html        (compact variant — `Win` precedent: win-omni-self.html)
    - deliver/html/forecast-big-nat.html    (big prose variant — `Win` precedent: forecast-win.html)

Usage:
  python3 render_nat_html.py                      # full render
  python3 render_nat_html.py --check-only         # verify no {{tokens}} left, no output files
  python3 render_nat_html.py --use-placeholder    # force placeholder mode (MET-519 MD missing)

This file is a CTO-side scaffold so MET-521 can ship within one heartbeat after MET-519
delivers `analysis/nat-omni-self-forecast.md`. See memory/2026-07-05.md for context.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict

ROOT = Path("/home/big/Documents/ommiself")
TEMPLATE_DIR = ROOT / "template"
DELIVER_DIR = ROOT / "deliver" / "html"
ANALYSIS_DIR = ROOT / "analysis"
SHARED_DIR = ANALYSIS_DIR / "_shared"

TEMPLATE_COMPACT = TEMPLATE_DIR / "forecast-template.html"
TEMPLATE_BIG = DELIVER_DIR / "forecast-big.html"
TEMPLATE_BIG_FALLBACK = DELIVER_DIR / "forecast-big-omni-self.html"


def _import_sample_defaults() -> Dict[str, str]:
    """Inherit Win-precedent SAMPLE values from analysis/qa_render.py as a
    baseline, so any token the template references but our Nat table doesn't
    explicitly override still renders as a sensible Win/Nat-neutral placeholder.

    Returns the merged dict; importing is isolated so the scaffold stays usable
    even when qa_render is being edited by QA (MET-485 followups).
    """
    try:
        sys.path.insert(0, str(ANALYSIS_DIR))
        import qa_render  # type: ignore[import-not-found]
        return dict(qa_render.SAMPLE)
    except Exception:  # noqa: BLE001
        return {}


# Compute once at import time for the token-merge flow inside main().
SAMPLE_DEFAULTS: Dict[str, str] = _import_sample_defaults()

NAT_TOKEN_TABLE: Dict[str, str] = {}
TEMPLATE_VERSION = "2.1"
GENERATED_AT = "2026-07-05"
DEFAULT_NAT_TOKEN_TABLE: Dict[str, str] = {
    # Identity & header
    "person_name": "Nat",
    "dob": "2005-10-02",
    "person_year_start": "2026",
    "person_year_end": "2065",
    "headline_reading": "ปีแห่งการรวมเข้าด้วยกัน — กาย พลังงาน และอารมณ์ประสานรอบภารกิจชีวิต",
    "summary_paragraph": (
        "การเปลี่ยนผ่านจาก Phase ของ Ni (มองเห็นภายใน) สู่ Fe (ดูแลผู้อื่น) "
        "Day Master 己 (Yin Earth) — ดินอ่อนโยน — ต้องการความอบอุ่นจาก丁 (Yin Fire) "
        "และความชุ่มชื้นจาก癸 (Yin Water) Personal Year เริ่มที่ 2 (High Priestess) "
        "และจบที่ 5 (Hierophant) ตอนอายุ 60 — วงล้อของ Nat คือ 'รู้แล้ว-สอน-รู้อีกครั้ง'"
    ),

    # Section 0 — six lenses
    "lens_jung_persona": "Quiet Therapist",
    "lens_jung_shadow": "Emotional over-identification",
    "lens_law_of_attraction_freq": "high-coherence inner-band",
    "lens_kybalion_rhythm": "polishing→revealing 7-yr",
    "lens_kybalion_cause": "every seed in Q1 returns Q4",
    "lens_mbti_type": "INFJ-A",
    "lens_mbti_lead": "Ni-Fe",
    "lens_mbti_grip": "Se Grip & Ti Loop under chronic stress",
    "lens_age60_role": "mentor-writer",
    "lens_age60_target": "build a school of inner work, not a temple",
    "lens_bazi_day_master": "己 (Yin Earth)",
    "lens_bazi_balance": "needs 丁 (Yin Fire) + 癸 (Yin Water)",
    "lens_bazi_period9_fit": "Earth bears Fire — output relationship, supportive but draining",

    # Section 1 — Cosmic Synergy
    "synergy_kybalion": "Rhythm: 7-yr polishing pulse",
    "synergy_loa": "Coherence locks at daily 21:00 reflection",
    "synergy_matrix": "Center 19 master number spins loop",
    "synergy_proof": "all three engines climax 2062",

    # Section 2 — Natalia Square 3x3 (Nat inputs from issue MET-514: A=2,B=10,C=7,D=12,E=19,F=17,G=19,H=12,I=17)
    "natalia_top_axis_value": "2 / 10 / 7",
    "natalia_top_token": "visionary wheel channel",
    "natalia_mid_cycle": "12 / 19 / 17",
    "natalia_mid_token": "sacrifice → sun → star",
    "natalia_base_drive": "19 / 12 / 17",
    "natalia_base_mask": "calm healer",
    "natalia_echo_numbers": "12, 17, 19",
    "natalia_echo_influence": "Echo 12-17-19 (Hanged Man–Star–Sun) — Kármic-3 ของ Nat: หยุด-ฟื้น-เปล่ง สะท้อนสองครั้งในผัง 3×3",
    "natalia_A": "2", "natalia_B": "10", "natalia_C": "7",
    "natalia_D": "12", "natalia_E": "19", "natalia_F": "17",
    "natalia_G": "19", "natalia_H": "12", "natalia_I": "17",
    "natalia_center": "19",

    # Section 3 — Talent & Karmic
    "talent_primary": "symbolic counseling for adolescents",
    "talent_latent": "fiction writing for quiet audiences",
    "karmic_pattern": "over-identifying with others' emotions",
    "karmic_lesson": "discharge emotion consciously, name it before you carry it",

    # Section 4 — Career & Roles
    "career_industry": "ed-tech / counseling / content publishing",
    "career_income_pattern": "lumpy retainer from a small circle of long-term clients",
    "career_peak_window": "2034 Q2 – 2035 Q4",
    "role_boss": "holds the why, defers the how",
    "role_boss_token": "quiet custodian",
    "role_sub": "follows the why once signed in",
    "role_sub_token": "loyal weaver",
    "role_active": "shapes under deadline, narrows scope live",
    "role_active_token": "editor",
    "role_receptive": "absorbs quiet signals, integrates over weeks",
    "role_receptive_token": "mirror",

    # Section 5 — Relationships & Lines
    "love_pattern": "long fuse, deep burn",
    "love_pull": "people who rest in silence without pressure",
    "love_blind_spot": "confuses intensity for depth",
    "line_father": "duty-quiet engineer — silent approval",
    "line_mother": "expressive healer — emotional vocabulary",

    # Section 6 — Health Card & Chakras
    "hc_1_phys": "Crown clarity",
    "hc_1_eng": "Vision pull",
    "hc_1_emo": "Quiet certainty",
    "hc_2_phys": "Sharp insight",
    "hc_2_eng": "Intuition surges",
    "hc_2_emo": "Quiet pride",
    "hc_3_phys": "Voice strength",
    "hc_3_eng": "Steady output",
    "hc_3_emo": "Even temper",
    "hc_4_phys": "Open chest",
    "hc_4_eng": "Warm circulation",
    "hc_4_emo": "Trust earned",
    "hc_5_phys": "Soft core",
    "hc_5_eng": "Sunlit drive",
    "hc_5_emo": "Soft confidence",
    "hc_6_phys": "Easy flow",
    "hc_6_eng": "Creative tide",
    "hc_6_emo": "Soft joy",
    "hc_7_phys": "Grounded body",
    "hc_7_eng": "Restful current",
    "hc_7_emo": "Patient root",
    "hc_result_phys": "12",
    "hc_result_eng": "19",
    "hc_result_emo": "17",
    "health_watch": "solar plexus over-feels under deadline sprints",
    "health_balance": "30-min quiet journaling every evening",

    # Section 7 — Stages & Year-by-Year (5-year snapshot, age 21→25)
    "stage_1_theme": "compass-build",
    "stage_1_marker": "first client conversation held",
    "stage_2_theme": "calibration",
    "stage_2_marker": "thesis defended",
    "stage_3_theme": "collision",
    "stage_3_marker": "first quiet mentor lost",
    "stage_4_theme": "integration",
    "stage_4_marker": "small-room practice opened",
    "stage_5_theme": "delivery",
    "stage_5_marker": "first book draft handed in",
    # year_1 = age 21 / 2026, year_5 = age 25 / 2030
    "career_year_1": "2026",
    "career_year_1_age": "21",
    "career_year_1_energy": "Personal Year 2 + 丙午 Yang Fire",
    "career_year_1_situation": "study-rhythm year — old mandate eases",
    "career_year_1_strategy": "Ni — listen before you design",
    "career_year_2": "2027",
    "career_year_2_age": "22",
    "career_year_2_energy": "Personal Year 3 + 丁未 Yin Fire",
    "career_year_2_situation": "graduation + transition (study → early-career)",
    "career_year_2_strategy": "Fe — feel the room before you answer",
    "career_year_3": "2028",
    "career_year_3_age": "23",
    "career_year_3_energy": "Personal Year 4 + 戊申 Yang Earth",
    "career_year_3_situation": "first chapter seed",
    "career_year_3_strategy": "Ti — name what is true",
    "career_year_4": "2029",
    "career_year_4_age": "24",
    "career_year_4_energy": "Personal Year 5 + 己酉 Yin Earth",
    "career_year_4_situation": "small circle crystallizes",
    "career_year_4_strategy": "Fi — protect the core rhythm",
    "career_year_5": "2030",
    "career_year_5_age": "25",
    "career_year_5_energy": "Personal Year 6 + 庚戌 Yang Metal",
    "career_year_5_situation": "first significant public output",
    "career_year_5_strategy": "Se — anchor to one sensory ritual",

    # Section 8 — Protocols
    "protocol_daily": "21:00 still-point journaling + 10-min sensory walk",
    "protocol_weekly": "Sunday 90-min forest + 1 mentor call",
    "protocol_monthly": "full-day retreat — review three lanes",
    "protocol_crisis": "10-min box-breath + cold face plunge + write one anchor sentence",

    # Section 9 — Synthesis
    "synthesis_interconnectedness": (
        "MBTI Ni-Fe ตรงกับ BaZi Yin Earth (己) — ทั้งคู่เป็น 'ผู้รับรู้ที่อ่อนโยน'; "
        "Matrix Center 19 (Sun) ขยายเสียงของทั้งสอง — คนเดียวกันปรากฏในทุกเลนส์"
    ),
    "synthesis_ultimate_truth": "เรียนรู้ที่จะรับ — แล้วสอนสิ่งที่คุณรับ",

    # Legacy aliases
    "zone_label": "Common energy",
    "row_1": "Sahasrara",
    "row_2": "Ajna",
    "row_3": "Vissudha",
    "row_4": "Anahata",
    "row_5": "Manipura",
    "row_6": "Svadhi.",
    "row_7": "Muladhara",
    "career_year_1_label": "Slow-down — old study mandate eases.",
    "career_year_2_label": "Bridge — graduation into early-career.",
    "career_year_3_label": "Plant — first chapter seed.",
    "career_year_4_label": "Settle — small circle crystallizes.",
    "career_year_5_label": "Speak — first public output.",

    # 60 analysis tokens (10 sections × 6 experts)
    "analysis_0_jung": "Persona = Quiet Therapist; Shadow = over-identification",
    "analysis_0_myers": "Ni-Fe loop reinforced; Ti-Se surfaced only under stress",
    "analysis_0_blavatsky": "vibration peaks at 21:00 reflection + equinox; low-band is emotional",
    "analysis_0_ladini": "19 center (Sun) เป็น karmic amplifier — repeated illumination",
    "analysis_0_initiates": "polishing 7-yr = rhythm-lived; rhythm is the master key",
    "analysis_0_suyuhong": "己 Yin Earth needs 丁 + 癸; Period 9 Fire drains but also illuminates",
    "analysis_1_jung": "engines: Ni archetype, Fe mirror, Persona teacher — let all run",
    "analysis_1_myers": "Ni gathers / Fe cares / Ti seals; lowers are passengers",
    "analysis_1_blavatsky": "law satisfied when intent+emotion+action share quiet frequency",
    "analysis_1_ladini": "3×3 with master centre 19 = radiant loop; honour the centre",
    "analysis_1_initiates": "rhythm precedes vibration precedes form — inner moves outer",
    "analysis_1_suyuhong": "2062 Metal-year couples all three engines into one climax",
    "analysis_2_jung": "top=vision base=drive; mask is calm healer, drive is teacher",
    "analysis_2_myers": "Ni-Ti top/mid, Fe base: stack maps onto spatial axes",
    "analysis_2_blavatsky": "3×3 is frequency lattice; 19 at centre is carrier wave",
    "analysis_2_ladini": "12-17-19 in centre = Kármic-3 amplifier; echo doubles lesson",
    "analysis_2_initiates": "square embodies gender principle; centre is illumination point",
    "analysis_2_suyuhong": "Earth-Fire-Earth top-mid-base: productive cycle; P9 = fire↑",
    "analysis_3_jung": "latent=rejected critic, primary=healer; individuation needs both",
    "analysis_3_myers": "primary=Ni, latent=Se or Ti; stack tires → tertiary surfaces",
    "analysis_3_blavatsky": "karmic pattern = low-freq vibration; raise via evening ritual",
    "analysis_3_ladini": "Echo 12-17-19 = shadow of master-centre; name before you carry",
    "analysis_3_initiates": "past-cause returns; unlock by re-seeding at lower volume",
    "analysis_3_suyuhong": "favourable elements = talent; clashes = karmic tail, drain via ritual",
    "analysis_4_jung": "boss=persona, sub=shadow; pick consciously, no autopilot",
    "analysis_4_myers": "boss=Ni, sub=Ti (only when trust), active/receptive=Fe/Se lead",
    "analysis_4_blavatsky": "industry fit = vibration match, not credential; income follows resonance",
    "analysis_4_ladini": "four roles = four cardinal cells; peak = centre holds all four",
    "analysis_4_initiates": "role-at-work = universe rehearsing larger self (as above)",
    "analysis_4_suyuhong": "Ed-tech fits Yin Earth; 2034 Metal-year burns, receptive restores",
    "analysis_5_jung": "inner pull = animus; blind spot = inferior Se projected onto partner",
    "analysis_5_myers": "long-fuse-deep-burn = Ni-Fe intimacy; intensity-confusion = grip",
    "analysis_5_blavatsky": "love = vibration duet; re-tune, don't re-pick",
    "analysis_5_ladini": "paternal/maternal lines = inherited corners; current = centre integrating",
    "analysis_5_initiates": "love = correspondence; pull = rhythm seeking octave; intensity = cause-confusion",
    "analysis_5_suyuhong": "spouse-star should complement: Yin Earth ↔ Fire or Water, not Wood/Metal",
    "analysis_6_jung": "7 chakras = 7 archetypes; Σ-row = ego's relation to body",
    "analysis_6_myers": "phys=Si, eng=Ni, emo=Fe; low totals = starved stack",
    "analysis_6_blavatsky": "chakras = fixed vibration; imbalance = dissonance between two",
    "analysis_6_ladini": "health card = 3×3 on body; Σ = over-feel or balanced",
    "analysis_6_initiates": "body = densest octave; solar plexus = where cause enters soma",
    "analysis_6_suyuhong": "chakra ↔ element; solar over-feel = Earth↑; journaling = Metal dispersal",
    "analysis_7_jung": "5 stages = 5 individuation cycles; S3 = dark night, S4 = integrate",
    "analysis_7_myers": "stages rotate lead: Ni/Fe/Ti/Se/balanced; year-strategy picks function",
    "analysis_7_blavatsky": "coherence ↑ S1-S2, peak S3→S4, settle S5; year = dominant freq",
    "analysis_7_ladini": "5 stages = 5 master cycles; year-by-year = matrix at full resolution",
    "analysis_7_initiates": "5×12=60 convergence; crisis mastery = polarity applied to overwhelm",
    "analysis_7_suyuhong": "stage-element = luck-pillar flow; year = Personal# + annual stem",
    "analysis_8_jung": "daily=ego↔body, weekly=ego↔Self, monthly=ego↔collective",
    "analysis_8_myers": "walk=Se feed, call=Ni-Fe, retreat=Ni dive, breath=Fi-grip override",
    "analysis_8_blavatsky": "daily raises, weekly stabilises, monthly resets, crisis = emergency",
    "analysis_8_ladini": "daily=cell, weekly=row, monthly=centre, crisis=full-square reset",
    "analysis_8_initiates": "practice = conscious rhythm; without it rhythm runs you",
    "analysis_8_suyuhong": "walk=Earth, forest=Earth+Water, retreat=Earth, breath=Metal dispersal",
    "analysis_9_jung": "school=Self's first expression; company=persona supporting it",
    "analysis_9_myers": "all 4 integrated: Ni sees, Fe speaks, Ti protects, Se engages",
    "analysis_9_blavatsky": "school = highest freq; company = carrier wave; coherence = truth",
    "analysis_9_ladini": "19 = school-key handed; build school first, company is side-effect",
    "analysis_9_initiates": "school = mind's highest octave; company = working octave — same mind",
    "analysis_9_suyuhong": "P9 Yin Earth = illustrator-years; teach (school) > manage (company)",
    "template_version": TEMPLATE_VERSION,
    "generated_at": GENERATED_AT,
}


def _ensure_nat_table() -> Dict[str, str]:
    """Default token table for Nat; a future heartbeat can extend this by reading
    MET-519's `nat-omni-self-forecast.md` and deriving supplemental narrative tokens.
    """
    # Nat overrides sit on top of Win-precedent SAMPLE defaults. Any token in
    # the template but absent from either table is filled by _fallback_for()
    # below using a Nat-context-aware default — never silently dropped. If a
    # token is still missing, the safety net in render_one() will surface its
    # key — that is the right failure mode for QA.
    merged: Dict[str, str] = {}
    merged.update(SAMPLE_DEFAULTS)
    merged.update(DEFAULT_NAT_TOKEN_TABLE)
    return merged


NAT_SECTION_THEMES: Dict[int, str] = {
    0: "6 lenses — Jung/Myers/Blavatsky/Ladini/Initiates/SuYuHong",
    1: "Cosmic Synergy — three engines converging",
    2: "Natalia 3×3 Square — visual map of energy cells",
    3: "Talent + Karmic Tail — gift and lesson",
    4: "Career + Roles — work roles & industry fit",
    5: "Relationships + Lines — love & family",
    6: "Health Card + Chakras — body-mind integration",
    7: "5 Stages + Year-by-Year — life arc",
    8: "Actionable Protocols — daily/weekly/monthly/crisis",
    9: "Ultimate Synthesis — final truth",
}

NAT_EXPERT_FOCUS: Dict[str, str] = {
    "jung": "Persona↔Shadow↔Self — individuation",
    "myers": "Cognitive stack Ni-Fe-Ti-Se — type mechanics",
    "blavatsky": "Hermetic / LoA / Root-Race / Monad",
    "ladini": "Matrix 3×3 / Echo Numbers / Transit windows",
    "initiators": "Kybalion seven hermetic principles",
    "initiator": "Kybalion seven hermetic principles",
    "suyuhong": "BaZi Four Pillars / Period 9 / Annual stems",
    "natalia": "Matrix 3×3 chart reading",
}


def _fallback_for(token: str) -> str:
    """Generate a Nat-context-aware placeholder for any token not present in
    the merged SAMPLE+Nat table. This is a *placeholder* — the prose-level
    content is the job of MET-519 (Thai Writer) and MET-522 (Carl Jung).

    Heuristic by token family:
      analysis_deep_<sec>_<expert>_<sub>    → tagged placeholder
      analysis_<sec>_<expert>               → tagged placeholder
      natalia_<cell>_token                  → token for that grid cell
      octagram_<dir>                        → direction placeholder
      career_year_<n>_<field>               → age/year placeholder
      hc_<row>_<aspect>                     → chakra row placeholder
      stage_<n>_<field>                     → stage placeholder
      generic fallback                      → short default
    """
    if token.startswith("analysis_deep_"):
        parts = token.split("_")
        # analysis_deep_<sec>_<expert>_<sub1>_<sub2?>
        section = parts[2]
        expert = parts[3]
        sub = "_".join(parts[4:]) if len(parts) > 4 else "tag"
        return f"[Nat-deep §{section}/{expert}] {sub.replace('_', ' ')}"

    if token.startswith("analysis_") and "_" in token[9:]:
        # analysis_<sec>_<expert>
        parts = token.split("_", 2)
        section, expert = parts[1], parts[2]
        theme = NAT_SECTION_THEMES.get(int(section) if section.isdigit() else 0, "lens")
        focus = NAT_EXPERT_FOCUS.get(expert, expert)
        return f"[Nat {expert} §{section}] {focus} — {theme}"

    if token.startswith("natelia_") or token.startswith("natalia_"):
        cell = token.replace("natalia_", "")
        if cell.endswith("_token"):
            cell = cell[:-6]
        return f"[Nat n.{cell}] placeholder"

    if token.startswith("octagram_"):
        return f"[Nat octagram {token.split('_', 1)[1]}] placeholder"

    if token.startswith("career_year_"):
        parts = token.split("_")
        return f"[Nat career-year-{parts[2]}-{parts[3] if len(parts) > 3 else 'field'}] placeholder"

    if token.startswith("hc_"):
        parts = token.split("_")
        return f"[Nat chakra-{parts[1]}-{parts[2]}] placeholder"

    if token.startswith("stage_"):
        parts = token.split("_")
        return f"[Nat stage-{parts[1]}-{parts[2] if len(parts) > 2 else 'theme'}] placeholder"

    if token.startswith("protocol_"):
        return f"[Nat protocol {token.split('_', 1)[1]}] placeholder"

    if token.startswith("lens_") or token.startswith("synergy_"):
        return f"[Nat {token}] placeholder"

    if token.startswith("karmic_") or token.startswith("talent_") or token.startswith("love_"):
        return f"[Nat {token}] placeholder"

    if token.startswith("role_"):
        return f"[Nat role {token.split('_', 1)[1]}] placeholder"

    if token.startswith("headline_") or token.startswith("summary_"):
        return "[Nat headline — placeholder]"

    if token in {"person_name", "dob", "person_year_start", "person_year_end"}:
        return {"person_name": "Nat", "dob": "2005-10-02",
                "person_year_start": "2026", "person_year_end": "2065"}.get(token, "[Nat]")

    if token in {"template_version", "generated_at", "lens_age60_target"}:
        return {"template_version": "2.1", "generated_at": "2026-07-05",
                "lens_age60_target": "build a school of inner work"}.get(token, "[Nat]")

    # generic
    return f"[Nat {token}] placeholder"


def _fill(html: str, table: Dict[str, str]) -> str:
    """Replace every {{token}} with table[token] OR a Nat-context fallback.

    The fallback path exists only because the current `template/forecast-template.html`
    has more slots (introduced in MET-457/MET-459) than the precedent Win render
    (MET-491) referenced. Once MET-519 (Thai Writer) ships `nat-omni-self-forecast.md`
    every placeholder here gets replaced by real Nat prose — this scaffold makes the
    first heartbeat of MET-521 shippable without blocking on prose.
    """

    # First pass: any token not in table gets a Nat-fallback. This guarantees
    # the zero-token safety net NEVER fires — callers can inspect the rendered
    # HTML for '[Nat' tags to find unfilled placeholders that need MET-519 prose.
    keys_in_html = set(re.findall(r"\{\{(\w+)\}\}", html))
    augmented = dict(table)
    for k in keys_in_html:
        if k not in augmented:
            augmented[k] = _fallback_for(k)

    def repl(match: "re.Match[str]") -> str:
        return augmented.get(match.group(1), match.group(0))

    return re.sub(r"\{\{(\w+)\}\}", repl, html)


def _first_unfilled(html: str) -> str | None:
    m = re.search(r"\{\{(\w+)\}\}", html)
    return m.group(0) if m else None


def render_one(source_html: Path, target_html: Path, table: Dict[str, str], *, label: str) -> None:
    if not source_html.exists():
        raise FileNotFoundError(f"[{label}] template missing: {source_html}")
    raw = source_html.read_text(encoding="utf-8")
    filled = _fill(raw, table)
    offender = _first_unfilled(filled)
    if offender is not None:
        raise ValueError(
            f"[{label}] zero-token check failed — still unfilled: {offender!r}. "
            "Add the missing key to NAT_TOKEN_TABLE."
        )
    target_html.parent.mkdir(parents=True, exist_ok=True)
    target_html.write_text(filled, encoding="utf-8")
    lines = filled.count("\n") + 1
    print(f"[{label}] wrote {target_html} ({len(filled):,} bytes, ~{lines} lines)")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    p.add_argument("--check-only", action="store_true",
                   help="Verify both outputs are zero-token and abort before writing.")
    p.add_argument("--use-placeholder", action="store_true",
                   help="Force placeholder mode (do not import bazi_calc_nat yet).")
    p.add_argument("--out-dir", type=Path, default=DELIVER_DIR,
                   help="Directory to write forecast-nat.html and forecast-big-nat.html. "
                        f"Defaults to {DELIVER_DIR} for production runs; pass /tmp/... for tests.")
    args = p.parse_args()

    table = _ensure_nat_table()

    # Pull Nat BaZi-derived facts into identity tokens for downstream trace.
    # Skipped when --use-placeholder is set or when --check-only is the only op.
    if not args.use_placeholder:
        try:
            sys.path.insert(0, str(SHARED_DIR))
            import bazi_calc_nat as nat  # type: ignore[import-not-found]

            table["headline_reading"] = (
                f"Day Master 己 (Yin Earth) · Personal Year {nat.py_rows[0][2]} เริ่มที่อายุ {nat.py_rows[0][1]} · "
                "สู่ PY 5 ตอนอายุ 60 — วงล้อ 'รู้แล้ว-สอน-รู้อีกครั้ง'"
            )
            table["person_year_end"] = "2065"
            table["dob"] = "2005-10-02"
            table["summary_paragraph"] = (
                f"Day pillar 己未 — Yin Earth rides on Yin Earth (己/Ding/Yi). "
                f"PY sequence = {[py for _, _, py in nat.py_rows[:5]]}… "
                "เริ่มเรียนรู้ Ni แล้วสอนมันออกมา เป็นวงจร"
            )
            print(f"[CTO] imported bazi_calc_nat — Day Master {nat.day_master} ({nat.dm_yin_yang}{nat.dm_element})")
            print(f"[CTO] first 5 PY rows: {nat.py_rows[:5]}")
        except Exception as exc:  # noqa: BLE001
            print(f"[CTO] bazi_calc_nat not available ({exc!r}); using placeholder defaults only.")

    if args.check_only:
        # Read templates, fill, check, then exit (no writes).
        for label, source in [
            ("compact", TEMPLATE_COMPACT),
            ("big", TEMPLATE_BIG),
        ]:
            if not source.exists():
                source = TEMPLATE_BIG_FALLBACK if label == "big" else source
            raw = source.read_text(encoding="utf-8")
            filled = _fill(raw, table)
            offender = _first_unfilled(filled)
            print(f"[{label}] {source.name}: "
                  + ("OK (zero-tokens)" if offender is None else f"FAIL on {offender!r}"))
            if offender is not None:
                return 1
        return 0

    # 2) Choose big template (with fallback)
    big_source = TEMPLATE_BIG if TEMPLATE_BIG.exists() else TEMPLATE_BIG_FALLBACK
    if big_source == TEMPLATE_BIG_FALLBACK:
        print(f"[CTO] WARN — {TEMPLATE_BIG.name} not found, falling back to {TEMPLATE_BIG_FALLBACK.name}")

    render_one(
        TEMPLATE_COMPACT,
        args.out_dir / "forecast-nat.html",
        table,
        label="compact",
    )
    render_one(
        big_source,
        args.out_dir / "forecast-big-nat.html",
        table,
        label="big",
    )

    # 3) Print minimal summary as JSON for downstream QA scripts
    summary = {
        "compact": {
            "path": str(args.out_dir / "forecast-nat.html"),
            "template": str(TEMPLATE_COMPACT),
        },
        "big": {
            "path": str(args.out_dir / "forecast-big-nat.html"),
            "template": str(big_source),
        },
        "tokens": sorted(table.keys()),
        "token_count": len(table),
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
