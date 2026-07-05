"""Mokun — BaZi Four Pillars & supporting numerology.

DOB: 2 สิงหาคม ค.ศ. 2005 (Thailand, UTC+7)
Birth time: not specified — use noon (12:00) default per parent brief.

Reuses analysis/_shared/bazi_calc.py helpers (STEMS, BRANCHES, ELEMENT_OF_STEM,
YIN_YANG_OF_STEM, HIDDEN_STEMS, NAYIN_LOOKUP, year_pillar_solar, month_pillar_solar,
day_pillar, hour_pillar, personal_year, reduce_to_single).

Day Master (CEO-verified via sxtwl + cross-checked by Su Yu Hong in MET-507):
    戊 (Yang Earth / ภูเขา / Mountain).

Run: python3 analysis/_shared/bazi_calc_mokun.py
"""

import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import bazi_calc as _bazi  # noqa: E402

NAME = "Mokun"
DOB = date(2005, 8, 2)
EVAL_DATE = date(2026, 7, 5)
BIRTH_HOUR = 12  # noon default per parent brief
BIRTH_MIN = 0
MBTI = "ENTP-A"
CONTEXT = "นักศึกษามหาวิทยาลัย (กำหนดจบการศึกษาปี 2028)"

MATRIX_NUMBERS = {
    "A": 2,  "B": 8,  "C": 7,
    "D": 10, "E": 17, "F": 15,
    "G": 17, "H": 10, "I": 15,
}
ECHO_NUMBERS = [10, 15, 17]
ECHO_CARDS = {10: "Wheel of Fortune", 15: "The Devil", 17: "The Star"}
MATRIX_CENTER = MATRIX_NUMBERS["E"]

_sxtwl = _bazi.sxtwl.fromSolar(DOB.year, DOB.month, DOB.day)
year_p = f"{_bazi.STEMS[_sxtwl.getYearGZ().tg]}{_bazi.BRANCHES[_sxtwl.getYearGZ().dz]}"
month_p = f"{_bazi.STEMS[_sxtwl.getMonthGZ().tg]}{_bazi.BRANCHES[_sxtwl.getMonthGZ().dz]}"
day_p = f"{_bazi.STEMS[_sxtwl.getDayGZ().tg]}{_bazi.BRANCHES[_sxtwl.getDayGZ().dz]}"
hs, hb, _, _ = _bazi.hour_pillar(DOB, BIRTH_HOUR)
hour_p = f"{hs}{hb}"

day_master = _bazi.STEMS[_sxtwl.getDayGZ().tg]
year_branch = _bazi.BRANCHES[_sxtwl.getYearGZ().dz]

nayin_year = _bazi.nayin(year_p[0], year_p[1])
nayin_month = _bazi.nayin(month_p[0], month_p[1])
nayin_day = _bazi.nayin(day_p[0], day_p[1])
nayin_hour = _bazi.nayin(hour_p[0], hour_p[1])

hidden_year = _bazi.HIDDEN_STEMS[year_p[1]]
hidden_month = _bazi.HIDDEN_STEMS[month_p[1]]
hidden_day = _bazi.HIDDEN_STEMS[day_p[1]]
hidden_hour = _bazi.HIDDEN_STEMS[hour_p[1]]

dm_element = _bazi.ELEMENT_OF_STEM[day_master]
dm_yin_yang = _bazi.YIN_YANG_OF_STEM[day_master]

years, months, days = _bazi.age_ymd(DOB, EVAL_DATE)

# Personal Year table (age 21 → 60, 2026-2065)
py_rows = []
for y in range(2026, 2066):
    age = y - 2005
    py = _bazi.personal_year(DOB, y)
    py_rows.append((y, age, py))

annual_pillars = []
for y in range(2026, 2066):
    anchor = date(y, 6, 1)
    _, s, b = _bazi.year_pillar_solar(anchor)
    annual_pillars.append((y, y - 2005, f"{s}{b}", _bazi.ELEMENT_OF_STEM[s]))

PERIOD_9_START = 2024
PERIOD_9_END = 2043
RELATIONSHIP = {
    '木': 'Wood feeds Fire (productive cycle) — Wood periods amplify output',
    '火': 'Fire is in its element — peak alignment',
    '土': 'Fire generates Earth — drain relationship (output, not fuel)',
    '金': 'Fire melts Metal — controlling relationship',
    '水': 'Water douses Fire — controlling relationship',
}
in_period_9 = PERIOD_9_START <= 2026 <= PERIOD_9_END

# 10-year Luck Pillars (大运) — derived from Su Yu Hong's MET-507 reasoning.
# Mokun is Yin-male (per parent-brief gender assumption) → backward 逆行
# from month pillar 癸未. Backward steps: 未→午→巳→辰→卯→寅→丑→子→亥
LUCK_PILLARS = [
    {"age_start": 3,  "age_end": 12, "pillar": "丙午", "stem": "丙", "branch": "午", "element": "Fire"},
    {"age_start": 13, "age_end": 22, "pillar": "丁巳", "stem": "丁", "branch": "巳", "element": "Fire"},
    {"age_start": 23, "age_end": 32, "pillar": "戊辰", "stem": "戊", "branch": "辰", "element": "Earth"},
    {"age_start": 33, "age_end": 42, "pillar": "己卯", "stem": "己", "branch": "卯", "element": "Earth/Wood-mix"},
    {"age_start": 43, "age_end": 52, "pillar": "庚寅", "stem": "庚", "branch": "寅", "element": "Metal/Wood"},
    {"age_start": 53, "age_end": 62, "pillar": "辛丑", "stem": "辛", "branch": "丑", "element": "Metal/Earth"},
]

MATRIX_ROWS = [
    {"name": "Top (Vision)", "values": [MATRIX_NUMBERS["A"], MATRIX_NUMBERS["B"], MATRIX_NUMBERS["C"]],
     "tokens": ["The High Priestess (2) — silent-knower", "Strength (8) — quiet authority",
                "The Chariot (7) — twin ancestral pulls"]},
    {"name": "Mid (Heart)", "values": [MATRIX_NUMBERS["D"], MATRIX_NUMBERS["E"], MATRIX_NUMBERS["F"]],
     "tokens": ["Wheel of Fortune (10) — career rhythm",
                "The Star (17) — bridge between heaven and earth",
                "The Devil (15) — self-made chains"]},
    {"name": "Base (Drive)", "values": [MATRIX_NUMBERS["G"], MATRIX_NUMBERS["H"], MATRIX_NUMBERS["I"]],
     "tokens": ["The Star (17) — inner drive of hope",
                "Wheel of Fortune (10) — social persona spins",
                "The Devil (15) — shadow: forgettable chains"]},
]

ECHO_INFLUENCE = (
    "Echo 10-15-17 (Wheel · Devil · Star) — กระจกสามด้านของ Mokun: "
    "Wheel สะท้อนจังหวะชีวิต · Devil สะท้อนเงาที่ถูกซ่อน · Star สะท้อนแสงที่แท้จริง "
    "ครอบคลุม 6 จาก 9 ตำแหน่งในผัง — สถาปัตยกรรมหลักของจิตวิญญาณ ไม่ใช่ห่วงโซ่"
)


if __name__ == '__main__':
    print(f'=== BaZi Four Pillars for {NAME} ===')
    print(f'DOB: {DOB} {BIRTH_HOUR:02d}:{BIRTH_MIN:02d} (Thailand UTC+7, hour assumed noon)')
    print(f'Eval: {EVAL_DATE}')
    print()
    print(f'Year   pillar: {year_p}  (Nayin {nayin_year}; hidden: {hidden_year})')
    print(f'Month  pillar: {month_p}  (Nayin {nayin_month}; hidden: {hidden_month})')
    print(f'Day    pillar: {day_p}  (Nayin {nayin_day}; hidden: {hidden_day})')
    print(f'Hour   pillar: {hour_p}  (Nayin {nayin_hour}; hidden: {hidden_hour})')
    print()
    print(f'Day Master: {day_master} ({dm_yin_yang}{dm_element}) — mountain / cliff / holding earth')
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
    print(f'In Period 9 (Fire 2024-2043): {in_period_9}')
    print(f'Day Master ({dm_element}) vs Fire: {RELATIONSHIP.get(dm_element, "?")}')
    print()
    print('Matrix 3x3:')
    for row in MATRIX_ROWS:
        print(f"  {row['name']}: {row['values']}")
    print(f"Center: {MATRIX_CENTER} ({ECHO_CARDS[MATRIX_CENTER]})")
    print(f"Echo Numbers: {ECHO_NUMBERS}")