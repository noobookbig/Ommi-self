"""Render forecast-template.html in headless Chromium at 1280x800 and report
document.scrollHeight, heightVhRatio, plus per-section bounding boxes.

Sample tokens with realistic values so the rendered DOM is full-size.
"""
import http.server
import json
import re
import socketserver
import sys
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path("/home/big/Documents/ommiself")
TEMPLATE = ROOT / "template" / "forecast-template.html"
OUT_DIR = ROOT / "analysis"
OUT_DIR.mkdir(exist_ok=True)

SAMPLE = {
    "person_name": "Sample Person",
    "dob": "1990-04-12",
    "person_year_start": "2026",
    "person_year_end": "2032",
    "headline_reading": "Year of integration — body, energy, and emotion align around mission.",
    "summary_paragraph": (
        "Cycle transitions from Vissudha (destiny) into Anahata (relationships). "
        "Common energy 12 / 10 / 4 indicates balanced physics with a soft emotional "
        "undercurrent. Career peak window opens mid-cycle and stays open for 18 months."
    ),
    # Section 0 — six lenses
    "lens_jung_persona": "strategic mentor",
    "lens_jung_shadow": "control-freak saver",
    "lens_law_of_attraction_freq": "high-coherence mid-band",
    "lens_kybalion_rhythm": "expansion→contraction 7-yr",
    "lens_kybalion_cause": "every seed in Q1 returns Q4",
    "lens_mbti_type": "ENTJ-A",
    "lens_mbti_lead": "Te-Ni",
    "lens_mbti_grip": "Fi-Si loop under chronic stress",
    "lens_age60_role": "mentor-architect",
    "lens_age60_target": "build a school, not a product",
    "lens_bazi_day_master": "Yang Wood (Jia)",
    "lens_bazi_balance": "needs Water + Earth",
    "lens_bazi_period9_fit": "wood fuels fire — strong fit",
    # Section 1 — Cosmic Synergy
    "synergy_kybalion": "Rhythm: 7-yr expansion pulse",
    "synergy_loa": "Coherence locks at daily 06:30 ritual",
    "synergy_matrix": "Center 22 master number spins loop",
    "synergy_proof": "all three engines climax 2030",
    # Section 2 — Natalia Square 3x3
    "natalia_top_axis_value": "21 / 1 / 6",
    "natalia_top_token": "visionary start",
    "natalia_mid_cycle": "11 / 11 / 22",
    "natalia_mid_token": "master channel",
    "natalia_base_drive": "16 / 5 / 21",
    "natalia_base_mask": "calm operator",
    "natalia_echo_numbers": "11, 22",
    "natalia_echo_influence": "double master amplifier — both grace and pressure",
    "natalia_A": "21", "natalia_B": "1", "natalia_C": "6",
    "natalia_D": "8", "natalia_E": "13", "natalia_F": "21",
    "natalia_G": "5", "natalia_H": "12", "natalia_I": "17",
    "natalia_center": "11",
    # Section 3 — Talent & Karmic
    "talent_primary": "systems-architecture thinking",
    "talent_latent": "symbolic storytelling for mass audience",
    "karmic_pattern": "over-responsibility for siblings' trajectories",
    "karmic_lesson": "delegate before you burnout, not after",
    # Section 4 — Career & Roles
    "career_industry": "ed-tech infrastructure / R&D platform",
    "career_income_pattern": "lumpy milestone payments + retainer tail",
    "career_peak_window": "2029 Q2 – 2030 Q4",
    "role_boss": "decides the why, defers the how",
    "role_boss_token": "vision-bearer",
    "role_sub": "follows the why once signed in",
    "role_sub_token": "loyal executor",
    "role_active": "ships under deadline, cuts scope live",
    "role_active_token": "launcher",
    "role_receptive": "absorbs feedback, integrates quietly",
    "role_receptive_token": "mirror",
    # Section 5 — Relationships & Lines
    "love_pattern": "long fuse, deep burn",
    "love_pull": "people who challenge without judging",
    "love_blind_spot": "assumes others need rescuing",
    "line_father": "duty-first engineer — silent approval",
    "line_mother": "expressive healer — emotional vocabulary",
    # Section 6 — Health Card & Chakras
    "hc_1_phys": "Crown clarity",
    "hc_1_eng": "Mission pull",
    "hc_1_emo": "Calm certainty",
    "hc_2_phys": "Sharp perception",
    "hc_2_eng": "Insight surges",
    "hc_2_emo": "Quiet pride",
    "hc_3_phys": "Voice strength",
    "hc_3_eng": "Steady output",
    "hc_3_emo": "Even temper",
    "hc_4_phys": "Open chest",
    "hc_4_eng": "Warm circulation",
    "hc_4_emo": "Trust earned",
    "hc_5_phys": "Core stability",
    "hc_5_eng": "Sunlit drive",
    "hc_5_emo": "Quiet confidence",
    "hc_6_phys": "Easy flow",
    "hc_6_eng": "Creative tide",
    "hc_6_emo": "Soft joy",
    "hc_7_phys": "Grounded body",
    "hc_7_eng": "Restful current",
    "hc_7_emo": "Patient root",
    "hc_result_phys": "12",
    "hc_result_eng": "10",
    "hc_result_emo": "4",
    "health_watch": "solar plexus over-heats under deadline sprints",
    "health_balance": "90-min forest walk every Sunday",
    # Section 7 — Stages & Year-by-Year
    "stage_1_theme": "compass-build",
    "stage_1_marker": "first shipped notebook",
    "stage_2_theme": "expansion",
    "stage_2_marker": "first overseas engagement",
    "stage_3_theme": "collision",
    "stage_3_marker": "co-founder split",
    "stage_4_theme": "integration",
    "stage_4_marker": "school-shaped pilot launched",
    "stage_5_theme": "delivery",
    "stage_5_marker": "curriculum v3 released",
    "career_year_1": "2026",
    "career_year_1_age": "36",
    "career_year_1_energy": "Personal Year 8 + Bing Fire",
    "career_year_1_situation": "power-shift year — old mandate ends",
    "career_year_1_strategy": "Te — measure twice, sign once",
    "career_year_2": "2027",
    "career_year_2_age": "37",
    "career_year_2_energy": "Personal Year 9 + Ding Fire",
    "career_year_2_situation": "completion + handover",
    "career_year_2_strategy": "Ni — anticipate the next cycle",
    "career_year_3": "2028",
    "career_year_3_age": "38",
    "career_year_3_energy": "Personal Year 1 + Wu Earth",
    "career_year_3_situation": "new chapter seed",
    "career_year_3_strategy": "Se — sense the room",
    "career_year_4": "2029",
    "career_year_4_age": "39",
    "career_year_4_energy": "Personal Year 2 + Ji Earth",
    "career_year_4_situation": "partnerships crystallize",
    "career_year_4_strategy": "Fi — protect the core",
    "career_year_5": "2030",
    "career_year_5_age": "40",
    "career_year_5_energy": "Personal Year 3 + Geng Metal",
    "career_year_5_situation": "public launch, market entry",
    "career_year_5_strategy": "Te — ship under deadline",
    # Section 8 — Protocols
    "protocol_daily": "06:30 walk + 20-min silent writing",
    "protocol_weekly": "Sunday 90-min forest + 1 mentor call",
    "protocol_monthly": "full-day retreat — review three lanes",
    "protocol_crisis": "10-min box-breath + cold face plunge",
    # Section 9 — Synthesis
    "synthesis_interconnectedness": "MBTI Te-Ni matches BaZi Yang Wood, Matrix Center 11 amplifies both — the same person shows up under every lens",
    "synthesis_ultimate_truth": "build the school first; the company is what the school teaches",
    # Legacy aliases (kept for backward compat with older template sections)
    "zone_label": "Common energy",
    "row_1": "Sahasrara",
    "row_2": "Ajna",
    "row_3": "Vissudha",
    "row_4": "Anahata",
    "row_5": "Manipura",
    "row_6": "Svadhi.",
    "row_7": "Muladhara",
    "career_year_1_label": "Reframe — new mandate, slower burn.",
    "career_year_2_label": "Build — first team, first product.",
    "career_year_3_label": "Ship — public launch, market entry.",
    "career_year_4_label": "Scale — second act, partnerships.",
    "career_year_5_label": "Settle — operating cadence, mentors.",
    "template_version": "2.0",
    "generated_at": "2026-07-05",
}


def render(html_text: str) -> str:
    return re.sub(r"\{\{(\w+)\}\}", lambda m: SAMPLE.get(m.group(1), m.group(0)), html_text)


class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *_args, **_kwargs):  # noqa: ANN001
        return


def _start_server(directory: Path) -> tuple[socketserver.TCPServer, int]:
    handler = lambda *a, **kw: _Quiet(*a, directory=str(directory), **kw)
    server = socketserver.TCPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, server.server_address[1]


def main() -> int:
    if not TEMPLATE.exists():
        print(f"missing template: {TEMPLATE}", file=sys.stderr)
        return 2

    template_dir = TEMPLATE.parent
    html = TEMPLATE.read_text(encoding="utf-8")
    html = render(html)
    served = template_dir / "_qa_render.html"
    served.write_text(html, encoding="utf-8")

    server, port = _start_server(template_dir)
    url = f"http://127.0.0.1:{port}/_qa_render.html"
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(viewport={"width": 1280, "height": 800})
            page = context.new_page()
            page.goto(url)
            page.wait_for_load_state("networkidle")
            try:
                page.wait_for_function(
                    "() => !!document.querySelector('.mermaid[data-mermaid=\"matrix\"] svg')",
                    timeout=10_000,
                )
            except Exception as exc:  # noqa: BLE001
                print(f"warn: mermaid render wait failed: {exc}", file=sys.stderr)
            page.wait_for_timeout(500)

            metrics = page.evaluate(
                """() => ({
                  docHeight: document.documentElement.scrollHeight,
                  bodyHeight: document.body.scrollHeight,
                  innerHeight: window.innerHeight,
                  innerWidth: window.innerWidth,
                  sections: [...document.querySelectorAll('section.card, main.page > h1, main.page > .footer')].map(el => ({
                    tag: el.tagName,
                    cls: el.className,
                    top: el.getBoundingClientRect().top + window.scrollY,
                    height: el.getBoundingClientRect().height
                  })),
                  spokeSvg: (() => {
                    const svg = document.querySelector('.eight-spoke-svg svg, .octagram-svg svg');
                    return svg ? { w: svg.getBoundingClientRect().width, h: svg.getBoundingClientRect().height } : null;
                  })(),
                  mermaidSvgs: [...document.querySelectorAll('.mermaid svg')].map(svg => ({
                    w: svg.getBoundingClientRect().width,
                    h: svg.getBoundingClientRect().height
                  })),
                  overflowCount: [...document.querySelectorAll('section.card, main.page > h1, main.page > .footer')].filter(el => el.scrollHeight > el.clientHeight + 1).length
                })"""
            )

            png_path = OUT_DIR / "_qa_render_1280x800.png"
            page.screenshot(path=str(png_path), full_page=True)

            browser.close()
    finally:
        server.shutdown()
        served.unlink(missing_ok=True)

    height_vh_ratio = metrics["docHeight"] / metrics["innerHeight"]
    report = {
        "viewport": {"width": metrics["innerWidth"], "height": metrics["innerHeight"]},
        "scrollHeight": metrics["docHeight"],
        "bodyHeight": metrics["bodyHeight"],
        "heightVhRatio": round(height_vh_ratio, 3),
        "passes_110vh": metrics["docHeight"] <= metrics["innerHeight"] * 1.10,
        "spokeSvg": metrics["spokeSvg"],
        "mermaidSvgs": metrics["mermaidSvgs"],
        "overflowingCards": metrics["overflowCount"],
        "sections": metrics["sections"],
        "screenshot": str(png_path),
    }
    print(json.dumps(report, indent=2))

    (OUT_DIR / "_qa_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    return 0 if report["passes_110vh"] else 1


if __name__ == "__main__":
    sys.exit(main())