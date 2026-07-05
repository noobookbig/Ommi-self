"""verify_met_499.py — MET-499 acceptance verification.

Acceptance criteria from issue MET-499:
1. MD §8.2 PY sequence matches canonical formula and HTML §7.2 table exactly
2. MD §8.3 Octagram center shows PY=3 + 乙亥
3. MD line 192, 374, 458 references to "PY=6 at age 60" updated to PY=3
4. Year Pillar 2055 in MD = 乙亥 (matching HTML §7.2 line 970 + Su Yu Hong file line 239)

Canonical PY formula (analysis/_shared/bazi_calc.py line 147):
    d = reduce_to_single(birth_day)      # 2
    m = reduce_to_single(birth_month)    # 10 -> 1
    y = reduce_to_single(birth_year)     # 1995 -> 24 -> 6
    t = reduce_to_single(target_year)
    personal_year = reduce_to_single(d + m + y + t)
Win base = 2 + 1 + 6 = 9
"""
import re
import sys


EXPECTED = {
    2026: (1, "丙午"), 2027: (2, "丁未"), 2028: (3, "戊申"),
    2029: (4, "己酉"), 2030: (5, "庚戌"), 2031: (6, "辛亥"),
    2032: (7, "壬子"), 2033: (8, "癸丑"), 2034: (9, "甲寅"),
    2035: (1, "乙卯"), 2036: (2, "丙辰"),
    2055: (3, "乙亥"),
}


def main():
    with open("analysis/win-omni-self-forecast.md", encoding="utf-8") as fh:
        text = fh.read()

    fails = []

    print("=== Acceptance criterion 1: MD §8.2 PY sequence ===")
    for year, (py, pillar) in EXPECTED.items():
        pat = rf"ปี {year}.*?Personal Year\s*{py}.*?Year Pillar\s*{re.escape(pillar)}"
        if re.search(pat, text, re.DOTALL):
            print(f"  PASS  {year}: PY={py} Pillar={pillar}")
        else:
            print(f"  FAIL  {year}: expected PY={py} Pillar={pillar}")
            fails.append(year)

    print("\n=== Acceptance criterion 2: §8.3 Mermaid Octagram center ===")
    core_pat = r'CORE\["Personal Year 3 · Emperor<br/>乙亥 Yin Wood \+ Pig'
    if re.search(core_pat, text):
        print("  PASS  Mermaid CORE label shows 'Personal Year 3 · Emperor' + '乙亥'")
    else:
        print("  FAIL  Mermaid CORE label does not match expected PY=3 + 乙亥")
        fails.append("§8.3 Mermaid CORE")

    print("\n=== Acceptance criterion 3: line 192/374/458 PY=6 -> PY=3 ===")
    checks_3 = [
        (r"\*\*Bridge to Age 60\*\*.*?Personal Year = 3 \(Emperor\)", "line 192 bridge"),
        (r"Personal Year = 3 Emperor \+ Year Pillar 乙亥 return ณ อายุ 60", "line 374 ช่วงที่ 5"),
        (r"\*\*Emperor Year \+ natal-year return\*\*.*?PY=3 = Emperor", "line 458/459"),
    ]
    for pat, label in checks_3:
        if re.search(pat, text, re.DOTALL):
            print(f"  PASS  {label}")
        else:
            print(f"  FAIL  {label}")
            fails.append(label)

    print("\n=== Acceptance criterion 4: Year Pillar 2055 = 乙亥 ===")
    if re.search(r"ปี 2055.*?Year Pillar\s*乙亥", text):
        print("  PASS  Year 2055 Year Pillar = 乙亥")
    else:
        print("  FAIL  Year 2055 Year Pillar != 乙亥")
        fails.append("pillar 2055")

    print("\n=== Anti-regression: stale PY=6 at age 60 must be gone ===")
    stale = [
        r"PY=6 at age 60",
        r"Personal Year 6 · Year Pillar 乙卯",
        r"Personal Year = 6 \(Lovers\) ณ อายุ 60",
        r"Personal Year = 6 Lovers ณ อายุ 60",
    ]
    for pat in stale:
        if re.search(pat, text):
            print(f"  FAIL  stale pattern present: {pat}")
            fails.append(f"stale: {pat}")
        else:
            print(f"  PASS  no '{pat}'")

    print()
    if fails:
        print(f"=== OVERALL: FAIL ({len(fails)} issues) ===")
        for f in fails:
            print(f"  - {f}")
        sys.exit(1)
    print("=== OVERALL: PASS ===")
    print("MET-499 acceptance criteria 1-4 all satisfied.")


if __name__ == "__main__":
    main()
