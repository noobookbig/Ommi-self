"""qa_render_mokun.py — headless render of forecast-mokun.html at 1280×800.

Mirrors analysis/qa_render.py (Win precedent) but renders the Mokun variant.

Outputs:
  - analysis/_qa_render_mokun_1280x800.png  (full-page screenshot)
  - analysis/_qa_render_mokun_full.png       (full-page tall screenshot)
  - analysis/_qa_report_mokun.json           (render metrics)
"""
from __future__ import annotations

import http.server
import json
import re
import socketserver
import sys
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path("/home/big/Documents/ommiself")
HTML_PATH = ROOT / "deliver" / "html" / "forecast-mokun.html"
OUT_DIR = ROOT / "analysis"
SERVE_DIR = HTML_PATH.parent
SERVE_FILE = "_qa_render_mokun.html"


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
    if not HTML_PATH.exists():
        print(f"missing HTML: {HTML_PATH}", file=sys.stderr)
        return 2

    OUT_DIR.mkdir(exist_ok=True)
    SERVE_DIR.mkdir(parents=True, exist_ok=True)
    raw = HTML_PATH.read_text(encoding="utf-8")
    served = SERVE_DIR / SERVE_FILE
    served.write_text(raw, encoding="utf-8")

    server, port = _start_server(SERVE_DIR)
    url = f"http://127.0.0.1:{port}/{SERVE_FILE}"
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(viewport={"width": 1280, "height": 800})
            page = context.new_page()
            page.goto(url)
            page.wait_for_load_state("networkidle")

            # Mermaid may need a moment
            try:
                page.wait_for_function(
                    "() => !!document.querySelector('.mermaid svg') || !!document.querySelector('.mermaid[data-mermaid]')",
                    timeout=10_000,
                )
            except Exception as exc:  # noqa: BLE001
                print(f"warn: mermaid wait: {exc}", file=sys.stderr)
            page.wait_for_timeout(800)

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
                  mermaidSvgs: [...document.querySelectorAll('.mermaid svg')].map(svg => ({
                    w: svg.getBoundingClientRect().width,
                    h: svg.getBoundingClientRect().height
                  })),
                  overflowingCards: [...document.querySelectorAll('section.card, main.page > h1, main.page > .footer')].filter(el => el.scrollHeight > el.clientHeight + 1).length,
                  placeholderCount: (document.body.innerHTML.match(/\\{\\{/g) || []).length,
                  titleText: document.title,
                })"""
            )

            png_path = OUT_DIR / "_qa_render_mokun_1280x800.png"
            png_full_path = OUT_DIR / "_qa_render_mokun_full.png"
            page.screenshot(path=str(png_path), full_page=False)
            page.screenshot(path=str(png_full_path), full_page=True)

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
        "mermaidSvgs": metrics["mermaidSvgs"],
        "overflowingCards": metrics["overflowingCards"],
        "placeholderCount": metrics["placeholderCount"],
        "titleText": metrics["titleText"],
        "sections": metrics["sections"],
        "screenshot_1280x800": str(OUT_DIR / "_qa_render_mokun_1280x800.png"),
        "screenshot_full": str(OUT_DIR / "_qa_render_mokun_full.png"),
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    (OUT_DIR / "_qa_report_mokun.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return 0 if report["passes_110vh"] else 1


if __name__ == "__main__":
    sys.exit(main())