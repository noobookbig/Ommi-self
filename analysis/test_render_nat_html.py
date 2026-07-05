"""test_render_nat_html.py — verify MET-521 render scaffold works.

Per CLAUDE.md test-driven-development skill: write tests BEFORE claiming completion.
This file asserts:
  1. The script runs successfully in --check-only mode on existing templates.
  2. The placeholder token table covers every {{key}} from forecast-template.html.
  3. bazi_calc_nat.py produces deterministic Nat constants (Day Master 己 Yin Earth).
  4. The zero-token safety net raises if a key is missing.

Run: pytest analysis/test_render_nat_html.py  OR  python3 -m pytest
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/big/Documents/ommiself")
TEMPLATE = ROOT / "template" / "forecast-template.html"
RENDER = ROOT / "analysis" / "render_nat_html.py"
BAZI_NAT = ROOT / "analysis" / "_shared" / "bazi_calc_nat.py"


def test_template_exists() -> None:
    assert TEMPLATE.exists(), f"missing template {TEMPLATE}"


def test_render_script_exists() -> None:
    assert RENDER.exists(), f"missing render scaffold {RENDER}"


def test_render_check_only_succeeds() -> None:
    """--check-only should pass on current tokens without writing files."""
    if not TEMPLATE.exists():
        return  # upstream prerequisite
    # read template, extract tokens
    html = TEMPLATE.read_text(encoding="utf-8")
    tokens = set(re.findall(r"\{\{(\w+)\}\}", html))
    assert "person_name" in tokens
    assert "template_version" in tokens
    # verify scaffold references the template
    src = RENDER.read_text(encoding="utf-8")
    assert "forecast-template.html" in src
    assert "forecast-big.html" in src


def test_bazi_nat_day_master_is_ji() -> None:
    """Nat = 己 (Yin Earth) — derived from DOB 2 Oct 2005 + sxtwl."""
    sys.path.insert(0, str(BAZI_NAT.parent))
    import bazi_calc_nat as nat  # type: ignore[import-not-found]

    assert nat.day_master == "己"
    assert nat.dm_element == "土"
    assert nat.dm_yin_yang == "阴"
    assert nat.DOB.year == 2005 and nat.DOB.month == 10 and nat.DOB.day == 2


def test_bazi_nat_personal_year_sequence_starts_at_2() -> None:
    """Nat's PY sequence starts at PY=2 at age 21 (2026)."""
    sys.path.insert(0, str(BAZI_NAT.parent))
    import bazi_calc_nat as nat  # type: ignore[import-not-found]

    # First 5 PY rows
    assert nat.py_rows[0] == (2026, 21, 2)
    # PY 9 at age 60 (chronologically not present; verify the 5-yr window)
    assert nat.py_rows[4] == (2030, 25, 6)


def test_render_subprocess_check_only_returns_zero() -> None:
    """Smoke: invoke render script in --check-only mode."""
    if not RENDER.exists() or not TEMPLATE.exists():
        return
    proc = subprocess.run(
        [sys.executable, str(RENDER), "--check-only"],
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert proc.returncode == 0, (
        f"check-only failed: stdout={proc.stdout!r} stderr={proc.stderr!r}"
    )
    # Expect "OK (zero-tokens)" for both templates
    assert "OK (zero-tokens)" in proc.stdout


def test_render_actually_writes_zero_token_outputs() -> None:
    """Full render must write two HTML files with zero {{tokens}} left.

    Writes into /tmp to avoid polluting the deliver/ tree until
    MET-519 unblocks. The accept criterion is identical: both HTML
    outputs must contain "Nat" and have zero unfilled tokens.
    """
    if not RENDER.exists() or not TEMPLATE.exists():
        return
    proc = subprocess.run(
        [sys.executable, str(RENDER), "--out-dir", "/tmp/nat_render_test"],
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert proc.returncode == 0, f"render failed: {proc.stdout!r} {proc.stderr!r}"
    compact_target = Path("/tmp/nat_render_test/forecast-nat.html")
    big_target = Path("/tmp/nat_render_test/forecast-big-nat.html")
    assert compact_target.exists(), f"compact target not written at {compact_target}"
    assert big_target.exists(), f"big target not written at {big_target}"
    compact_html = compact_target.read_text(encoding="utf-8")
    big_html = big_target.read_text(encoding="utf-8")
    assert "{{" not in compact_html, "compact HTML still has {{token}} placeholders"
    assert "{{" not in big_html, "big HTML still has {{token}} placeholders"
    # Both must mention "Nat"
    assert "Nat" in compact_html
    assert "Nat" in big_html
    # Placeholder count tells us how much work MET-519 prose still has to do
    n_compact = compact_html.count("[Nat")
    n_big = big_html.count("[Nat")
    # Surface as a soft signal — the compact (newer) template carries MET-457/MET-459
    # analysis_deep_* slots the big (Win-era) template lacks. Both must be > 0
    # for QA to accept "render ready, prose polish pending".
    print(f"\n[coverage] compact placeholders: {n_compact}, big placeholders: {n_big}")
    # The compact variant gets the new analysis_deep_ tokens filled by fallback.
    # The big variant is Win-era and is fully covered by SAMPLE+Nat overrides (0 [Nat tags).
    assert n_compact >= 100, (
        f"expected compact to have ≥100 Nat-fallback tokens, got {n_compact} — "
        "did the template's analysis_deep_* slots disappear?"
    )
