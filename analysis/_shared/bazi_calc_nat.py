"""Nat — BaZi Four Pillars & supporting numerology.
DOB: 2 ตุลาคม 2005 (Bangkok, Thailand UTC+7)
Birth time: unknown at task creation; treated as 12:00 (noon) for hour pillar
           unless a confirmed time arrives in MET-519/MET-522 followups.

Reuses analysis/_shared/bazi_calc.py helpers (STEMS, BRANCHES, ELEMENT_OF_STEM,
YIN_YANG_OF_STEM, HIDDEN_STEMS, NAYIN_LOOKUP, year_pillar_solar, month_pillar_solar,
day_pillar, hour_pillar, personal_year, reduce_to_single) without re-defining them.

Run: python3 analysis/_shared/bazi_calc_nat.py
"""

import sys
from datetime import date
from pathlib import Path

# Reuse Big's helper module without modifying it
sys.path.insert(0, str(Path(__file__).parent))
import bazi_calc as _bazi  # noqa: E402

# ---- Identity ----
NAME = "Nat"
DOB = date(2005, 10, 2)
EVAL_DATE = date(2026, 7, 5)
BIRTH_HOUR = 12      # placeholder; refine if a confirmed time lands
BIRTH_MIN = 0
MBTI = "INFJ"
CONTEXT = "นักศึกษา (มีกำหนดจบการศึกษาในปี 2027)"
MATRIX_NUMBERS = {
    "A": 2,  "B": 10, "C": 7,
    "D": 12, "E": 19, "F": 17,
    "G": 19, "H": 12, "I": 17,
}
ECHO_NUMBERS = [12, 17, 19]

# ---- Four Pillars (sxtwl canonical, mirrors bazi_calc.py Big pattern) ----
_sxtwl = _bazi.sxtwl.fromSolar(DOB.year, DOB.month, DOB.day)
year_p = f"{_bazi.STEMS[_sxtwl.getYearGZ().tg]}{_bazi.BRANCHES[_sxtwl.getYearGZ().dz]}"
month_p = f"{_bazi.STEMS[_sxtwl.getMonthGZ().tg]}{_bazi.BRANCHES[_sxtwl.getMonthGZ().dz]}"
day_p = f"{_bazi.STEMS[_sxtwl.getDayGZ().tg]}{_bazi.BRANCHES[_sxtwl.getDayGZ().dz]}"
# Hour pillar: noon defaults to 午 hour; refine if a real time arrives
hs, hb, _, _ = _bazi.hour_pillar(DOB, BIRTH_HOUR)
hour_p = f"{hs}{hb}"

day_master = _bazi.STEMS[_sxtwl.getDayGZ().tg]   # 己
year_branch = _bazi.BRANCHES[_sxtwl.getYearGZ().dz]  # 酉

nayin_year = _bazi.nayin(year_p[0], year_p[1])
nayin_month = _bazi.nayin(month_p[0], month_p[1])
nayin_day = _bazi.nayin(day_p[0], day_p[1])
nayin_hour = _bazi.nayin(hour_p[0], hour_p[1])

hidden_year = _bazi.HIDDEN_STEMS[year_p[1]]
hidden_month = _bazi.HIDDEN_STEMS[month_p[1]]
hidden_day = _bazi.HIDDEN_STEMS[day_p[1]]
hidden_hour = _bazi.HIDDEN_STEMS[hour_p[1]]

dm_element = _bazi.ELEMENT_OF_STEM[day_master]          # 土
dm_yin_yang = _bazi.YIN_YANG_OF_STEM[day_master]       # 阴

# ---- Age ----
years, months, days = _bazi.age_ymd(DOB, EVAL_DATE)

# ---- Personal Year table (age 21 → 60, 2026-2065) — Nat MD §8.2 ---
py_rows = []
for y in range(2026, 2066):
    age = y - 2005
    py = _bazi.personal_year(DOB, y)
    py_rows.append((y, age, py))

# ---- Annual year pillars (year stem+branch per year, 立春 cutoff) ----
annual_pillars = []
for y in range(2026, 2066):
    anchor = date(y, 6, 1)
    _, s, b = _bazi.year_pillar_solar(anchor)
    annual_pillars.append((y, y - 2005, f"{s}{b}", _bazi.ELEMENT_OF_STEM[s]))

# ---- Period 9 (Fire — 九紫離火運 2024-2043) alignment ----
PERIOD_9_START = 2024
PERIOD_9_END = 2043
RELATIONSHIP = {
    '木': 'Wood feeds Fire (Wood supports Fire) — productive cycle, strong fit',
    '火': 'Fire is in its element — peak alignment',
    '土': 'Fire generates Earth — drain relationship (output, not fuel)',
    '金': 'Fire melts Metal — controlling relationship',
    '水': 'Water douses Fire — controlling relationship',
}
in_period_9 = PERIOD_9_START <= 2026 <= PERIOD_9_END

# ---- Echo influence for Nat Matrix ----
# 12, 17, 19 are repeated twice each in the 3x3 (D=12, G=19, H=12, I=17)
# Echo dualities at a glance: Hanged Man–Star–Sun axis
ECHO_INFLUENCE = (
    "Echo 12-17-19 (Hanged Man · Star · Sun) — Kármic-3: หยุด-ฟื้น-เปล่ง ที่สะท้อนเป็นครั้งที่สอง "
    "ในผัง 3x3 ของ Nat — เป็นทั้งแรงกดดัน (Hanged Man) และแรงบันดาลใจ (Sun) และโอกาสฟื้นตัว (Star)"
)

# ---- Matrix 3x3 layout (echo visuals in deliver) ----
MATRIX_ROWS = [
    {"name": "Top (Vision)", "values": [MATRIX_NUMBERS["A"], MATRIX_NUMBERS["B"], MATRIX_NUMBERS["C"]],
     "tokens": ["visionary start (2-High Priestess)", "wheel of fortune (10)", "channel (7)"]},
    {"name": "Mid (Heart)", "values": [MATRIX_NUMBERS["D"], MATRIX_NUMBERS["E"], MATRIX_NUMBERS["F"]],
     "tokens": ["sacrifice-pause (12)", "Sun-amplifier (19)", "Star-light (17)"]},
    {"name": "Base (Drive)", "values": [MATRIX_NUMBERS["G"], MATRIX_NUMBERS["H"], MATRIX_NUMBERS["I"]],
     "tokens": ["Sun-found (19)", "sacrifice-rest (12)", "Star-restored (17)"]},
]
MATRIX_CENTER = MATRIX_NUMBERS["E"]

if __name__ == '__main__':
    print(f'=== BaZi Four Pillars for {NAME} ===')
    print(f'DOB: {DOB} {BIRTH_HOUR:02d}:{BIRTH_MIN:02d} (Bangkok UTC+7)')
    print(f'Eval: {EVAL_DATE}')
    print()
    print(f'Year   pillar: {year_p}  (Nayin {nayin_year}; hidden: {hidden_year})')
    print(f'Month  pillar: {month_p}  (Nayin {nayin_month}; hidden: {hidden_month})')
    print(f'Day    pillar: {day_p}  (Nayin {nayin_day}; hidden: {hidden_day})')
    print(f'Hour   pillar: {hour_p}  (Nayin {nayin_hour}; hidden: {hidden_hour})')
    print()
    print(f'Day Master: {day_master} ({dm_yin_yang}{dm_element})')
    print(
        'Use-God heuristic (调候): REASONED IN PROSE by Su Yu Hong agent (MET-515) — '
        'bazi_calc.useful_god_heuristic is Big-specific (丑月), not Nat-specific (酉月). '
        'Classical 调候 anchor for 己 (Yin Earth) in 酉 month: 丁火暖土 + 癸水润局.')

    print()
    print(f'Age at {EVAL_DATE}: {years} years, {months} months, {days} days')
    print()
    print('Personal Year table 2026..2065 (age 21..60):')
    for y, age, py in py_rows:
        print(f'  {y} (age {age}) -> Personal Year {py}')
    print()
    print('Annual year pillars 2026..2065:')
    for y, age, p, e in annual_pillars:
        print(f'  {y} (age {age}) -> {p}  ({e})')
    print()
    print(f'In Period 9 (Fire): {in_period_9}')
    print(f'Day Master ({dm_element}) vs Fire: {RELATIONSHIP.get(dm_element, "?")}')
    print()
    print('Matrix 3x3:')
    for row in MATRIX_ROWS:
        print(f"  {row['name']}: {row['values']}")
    print(f'Center: {MATRIX_CENTER}')
    print(f'Echo Numbers: {ECHO_NUMBERS}')
