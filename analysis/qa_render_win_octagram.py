"""Render deliver/html/win-omni-self.html in headless Chromium and verify:
- 0 console errors, 0 page errors
- All 4 mermaid blocks render to SVG (synergy, natalia, stages, octagram60)
- §7.2 contains the octagram60 mermaid block
"""
import http.server
import json
import socketserver
import sys
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path("/home/big/Documents/ommiself")
HTML_FILE = ROOT / "deliver" / "html" / "win-omni-self.html"
HTML_DIR = HTML_FILE.parent
OUT_DIR = ROOT / "analysis"


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
    if not HTML_FILE.exists():
        print(f"missing html: {HTML_FILE}", file=sys.stderr)
        return 2

    server, port = _start_server(HTML_DIR)
    url = f"http://127.0.0.1:{port}/{HTML_FILE.name}"
    console_errors: list[str] = []
    page_errors: list[str] = []

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(viewport={"width": 1280, "height": 800})
            page = context.new_page()
            page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
            page.on("pageerror", lambda exc: page_errors.append(str(exc)))
            page.goto(url)
            page.wait_for_load_state("networkidle")

            try:
                page.wait_for_function(
                    "() => !!document.querySelector('.mermaid[data-mermaid=\"octagram60\"] svg')",
                    timeout=10_000,
                )
            except Exception as exc:  # noqa: BLE001
                print(f"warn: octagram60 render wait failed: {exc}", file=sys.stderr)

            page.wait_for_timeout(500)

            metrics = page.evaluate(
                """() => ({
                  docHeight: document.documentElement.scrollHeight,
                  bodyHeight: document.body.scrollHeight,
                  innerHeight: window.innerHeight,
                  innerWidth: window.innerWidth,
                  sections: [...document.querySelectorAll('section.card')].map(el => ({
                    id: el.id,
                    cls: el.className,
                    top: el.getBoundingClientRect().top + window.scrollY,
                    height: el.getBoundingClientRect().height
                  })),
                  mermaidBlocks: [...document.querySelectorAll('.mermaid[data-mermaid]')].map(el => ({
                    id: el.getAttribute('data-mermaid'),
                    renderedSvg: !!el.querySelector('svg'),
                    svgWidth: el.querySelector('svg') ? el.querySelector('svg').getBoundingClientRect().width : 0,
                    svgHeight: el.querySelector('svg') ? el.querySelector('svg').getBoundingClientRect().height : 0
                  })),
                  octagram60InS72: (() => {
                    const s72 = document.getElementById('s72');
                    if (!s72) return null;
                    const oct = s72.querySelector('.mermaid[data-mermaid=\"octagram60\"] svg');
                    return oct ? { w: oct.getBoundingClientRect().width, h: oct.getBoundingClientRect().height } : null;
                  })(),
                  coreText: (() => {
                    const core = document.querySelector('.mermaid[data-mermaid=\"octagram60\"] svg');
                    if (!core) return null;
                    const text = core.textContent || '';
                    return {
                      hasPY3: /Personal Year 3/.test(text),
                      hasYiHai: /乙亥/.test(text),
                      hasPig: /Pig/.test(text),
                      hasReturnOrigin: /Return-to-Origin/.test(text),
                      hasYiMao: /乙卯/.test(text),
                      hasRabbit: /Rabbit/.test(text),
                      hasPY6: /Personal Year 6/.test(text),
                    };
                  })()
                })"""
            )

            png_path = OUT_DIR / "_qa_render_win_octagram_1280x800.png"
            page.screenshot(path=str(png_path), full_page=True)

            browser.close()
    finally:
        server.shutdown()

    report = {
        "viewport": {"width": metrics["innerWidth"], "height": metrics["innerHeight"]},
        "scrollHeight": metrics["docHeight"],
        "bodyHeight": metrics["bodyHeight"],
        "heightVhRatio": round(metrics["docHeight"] / metrics["innerHeight"], 3),
        "consoleErrors": console_errors,
        "pageErrors": page_errors,
        "mermaidBlocks": metrics["mermaidBlocks"],
        "octagram60InS72": metrics["octagram60InS72"],
        "coreText": metrics["coreText"],
        "sections": metrics["sections"],
        "screenshot": str(png_path),
    }
    print(json.dumps(report, indent=2))

    (OUT_DIR / "_qa_report_win_octagram.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    all_mermaid_rendered = all(b["renderedSvg"] for b in metrics["mermaidBlocks"])
    octagram60_in_s72 = metrics["octagram60InS72"] is not None
    no_console_errors = len(console_errors) == 0 and len(page_errors) == 0
    core_correct = (metrics["coreText"] is not None
                    and metrics["coreText"]["hasPY3"]
                    and metrics["coreText"]["hasYiHai"]
                    and metrics["coreText"]["hasReturnOrigin"]
                    and not metrics["coreText"]["hasYiMao"]
                    and not metrics["coreText"]["hasPY6"])

    ok = all_mermaid_rendered and octagram60_in_s72 and no_console_errors and core_correct
    print(f"\nVERDICT: {'PASS' if ok else 'FAIL'}")
    print(f"  all_mermaid_rendered = {all_mermaid_rendered}")
    print(f"  octagram60_in_s72    = {octagram60_in_s72}")
    print(f"  no_console_errors    = {no_console_errors}")
    print(f"  core_correct         = {core_correct}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())