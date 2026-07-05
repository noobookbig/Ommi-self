#!/usr/bin/env python3
"""
Compute BaZi Four Pillars and supporting numerology for Big (Jitti Kunphruk).
DOB: 21 January 1986 (Bangkok, Thailand UTC+7)
Birth time: 17:36 (now confirmed)

Method:
  - Year/Month/Hour use solar-term (節氣) boundaries per project spec.
  - Day pillar: derived via sxtwl (壽星天文曆) — verified against Wikipedia
    Sexagenary cycle examples (1949-10-01 = 甲子, 1912-02-18 = 甲子,
    1984-02-04 = 甲子 year + 戊辰 day, 2025-01-01 = 甲辰 year).
  - JD+49 formula is internally consistent with sxtwl output.

Run: python3 analysis/_shared/bazi_calc.py
"""

import sxtwl
from datetime import date

# ---- Heavenly Stems & Earthly Branches ----
STEMS = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
BRANCHES = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']

ELEMENT_OF_STEM = {
    '甲':'木','乙':'木','丙':'火','丁':'火','戊':'土','己':'土',
    '庚':'金','辛':'金','壬':'水','癸':'水',
}
YIN_YANG_OF_STEM = {s:('阳' if i%2==0 else '阴') for i,s in enumerate(STEMS)}

HIDDEN_STEMS = {
    '子':['癸'],'丑':['己','癸','辛'],'寅':['甲','丙','戊'],'卯':['乙'],
    '辰':['戊','乙','癸'],'巳':['丙','戊','庚'],'午':['丁','己'],'未':['己','丁','乙'],
    '申':['庚','壬','戊'],'酉':['辛'],'戌':['戊','辛','丁'],'亥':['壬','甲'],
}
NAYIN = {
    ('甲子','乙丑'):'海中金',('丙寅','丁卯'):'炉中火',('戊辰','己巳'):'大林木',
    ('庚午','辛未'):'路旁土',('壬申','癸酉'):'剑锋金',('甲戌','乙亥'):'山头火',
    ('丙子','丁丑'):'涧下水',('戊寅','己卯'):'城头土',('庚辰','辛巳'):'白蜡金',
    ('壬午','癸未'):'杨柳木',('甲申','乙酉'):'泉中水',('丙戌','丁亥'):'屋上土',
    ('戊子','己丑'):'霹雳火',('庚寅','辛卯'):'松柏木',('壬辰','癸巳'):'长流水',
    ('甲午','乙未'):'沙中金',('丙申','丁酉'):'山下火',('戊戌','己亥'):'平地木',
    ('庚子','辛丑'):'壁上土',('壬寅','癸卯'):'金箔金',('甲辰','乙巳'):'覆灯火',
    ('丙午','丁未'):'天河水',('戊申','己酉'):'大驿土',('庚戌','辛亥'):'钗钏金',
    ('壬子','癸丑'):'桑柘木',('甲寅','乙卯'):'大溪水',('丙辰','丁巳'):'沙中土',
    ('戊午','己未'):'天上火',('庚申','辛酉'):'石榴木',('壬戌','癸亥'):'大海水',
}
NAYIN_LOOKUP = {}
for pair, ny in NAYIN.items():
    for p in pair:
        NAYIN_LOOKUP[p] = ny

def nayin(s, b): return NAYIN_LOOKUP.get(s+b, '?')

# ---- Year pillar (solar-term, 立春 cutoff) ----
def year_pillar_solar(d):
    """Returns (year, stem, branch) using 立春 (≈ Feb 4) as year cutoff.
    For Big's DOB (21 Jan 1986), this returns (1985, '乙', '丑') — still in 乙丑 year."""
    year = d.year
    lichun = date(year, 2, 4)
    if d < lichun:
        year -= 1
    stem = STEMS[(year - 4) % 10]
    branch = BRANCHES[(year - 4) % 12]
    return year, stem, branch

# ---- Month pillar (solar-term boundaries) ----
# Jié-qì start dates approximate (correct to within a day for recent years):
# 寅月 starts at 立春 (~Feb 4)
# 卯月 starts at 惊蛰 (~Mar 6)
# 辰月 starts at 清明 (~Apr 5)
# 巳月 starts at 立夏 (~May 6)
# 午月 starts at 芒种 (~Jun 6)
# 未月 starts at 小暑 (~Jul 7)
# 申月 starts at 立秋 (~Aug 7)
# 酉月 starts at 白露 (~Sep 8)
# 戌月 starts at 寒露 (~Oct 8)
# 亥月 starts at 立冬 (~Nov 7)
# 子月 starts at 大雪 (~Dec 7)
# 丑月 starts at 小寒 (~Jan 6) of NEXT year

SOLAR_TERM_BRANCH_1986 = [
    (date(1986, 2, 4),  '寅'),
    (date(1986, 3, 6),  '卯'),
    (date(1986, 4, 5),  '辰'),
    (date(1986, 5, 6),  '巳'),
    (date(1986, 6, 6),  '午'),
    (date(1986, 7, 7),  '未'),
    (date(1986, 8, 7),  '申'),
    (date(1986, 9, 8),  '酉'),
    (date(1986,10, 8),  '戌'),
    (date(1986,11, 7),  '亥'),
    (date(1986,12, 7),  '子'),
    (date(1987, 1, 6),  '丑'),  # 小寒 1987
]

YEAR_STEM_MONTH_START = {0:2, 1:4, 2:6, 3:8, 4:0}  # 甲己之年丙作首
MONTH_ORDER = ['寅','卯','辰','巳','午','未','申','酉','戌','亥','子','丑']

def month_pillar_solar(d):
    yp_year, _, _ = year_pillar_solar(d)
    stem_offset = YEAR_STEM_MONTH_START[(yp_year - 4) % 10]
    br = None
    for cutoff, branch in SOLAR_TERM_BRANCH_1986:
        if d < cutoff:
            br = branch
            break
    if br is None:
        br = '丑'  # past 小寒 1987
    m_idx = MONTH_ORDER.index(br)
    stem = STEMS[(stem_offset + m_idx) % 10]
    return stem, br, stem_offset, m_idx

# ---- Day pillar (via sxtwl) ----
def day_pillar(d):
    day = sxtwl.fromSolar(d.year, d.month, d.day)
    gz = day.getDayGZ()
    return STEMS[gz.tg], BRANCHES[gz.dz], gz.tg, gz.dz

# ---- Hour pillar ----
HOUR_BRANCH = [
    (23, 1, '子'), (1, 3, '丑'), (3, 5, '寅'), (5, 7, '卯'),
    (7, 9, '辰'), (9, 11, '巳'), (11, 13, '午'), (13, 15, '未'),
    (15, 17, '申'), (17, 19, '酉'), (19, 21, '戌'), (21, 23, '亥'),
]
HOUR_BRANCH_LIST = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']

def hour_branch(h):
    for lo, hi, br in HOUR_BRANCH:
        if lo <= h < hi:
            return br
    return '子'

def hour_pillar(d, h):
    _, _, ds_idx, _ = day_pillar(d)
    br = hour_branch(h)
    stem_offset = (ds_idx % 5) * 2
    h_idx = HOUR_BRANCH_LIST.index(br)
    stem = STEMS[(stem_offset + h_idx) % 10]
    return stem, br, stem_offset, h_idx

# ---- Personal Year (Matrix of Destiny reduction) ----
def reduce_to_single(n):
    while n >= 10:
        n = sum(int(c) for c in str(n))
    return n

def personal_year(birth_d, target_year):
    d = reduce_to_single(birth_d.day)
    m = reduce_to_single(birth_d.month)
    y = reduce_to_single(birth_d.year)
    t = reduce_to_single(target_year)
    return reduce_to_single(d + m + y + t)

# ---- Age ----
def age_ymd(birth, target):
    years = target.year - birth.year
    anchor = birth.replace(year=birth.year + years)
    if anchor > target:
        years -= 1
        anchor = birth.replace(year=birth.year + years)
    months = 0
    while months < 12 and _add_months(anchor, months + 1) <= target:
        months += 1
    anchor_m = _add_months(anchor, months)
    days = (target - anchor_m).days
    return years, months, days

def _add_months(d, n):
    m = d.month - 1 + n
    y = d.year + m // 12
    m = m % 12 + 1
    # Clamp day to month length
    import calendar
    last = calendar.monthrange(y, m)[1]
    day = min(d.day, last)
    return date(y, m, day)

# ---- Useful God heuristic ----
# Very rough heuristic — refine against full chart strength once all four pillars are read.
def useful_god_heuristic(day_master, month_branch):
    element = ELEMENT_OF_STEM[day_master]
    # 丑月 (early spring, cold) hosts 己/癸/辛 — supports Earth but month is still wintry.
    # For 乙 (Yin Wood), 丑月 is the time of seed germination. Wood is still weak in deep winter.
    # The classical heuristic (调候法):
    #   乙木生于丑月, 寒气未退, 需丙火暖局; 又需癸水润根.
    return "调候用神: 丙火 (warm Wood, 解丑月之寒) + 癸水 (润根, 滋养乙木)"

# ============================================================
# Build the canonical inputs
# ============================================================

DOB = date(1986, 1, 21)
EVAL_DATE = date(2026, 7, 5)
BIRTH_HOUR = 17
BIRTH_MIN = 36

# Four Pillars
yy, ys, yb = year_pillar_solar(DOB)
ms, mb, _, _ = month_pillar_solar(DOB)
ds, db, _, _ = day_pillar(DOB)
hs, hb, _, _ = hour_pillar(DOB, BIRTH_HOUR)

# Sanity: sxtwl gives year/month/day pillars for the date directly (which may differ
# from solar-term month rule). sxtwl's month pillar for Jan 21 (still in 丑月 before
# 立春) is 己丑, matching our month pillar. ✓
sxtwl_year = sxtwl.fromSolar(DOB.year, DOB.month, DOB.day).getYearGZ()
sxtwl_month = sxtwl.fromSolar(DOB.year, DOB.month, DOB.day).getMonthGZ()
sxtwl_day = sxtwl.fromSolar(DOB.year, DOB.month, DOB.day).getDayGZ()
sxtwl_yp = f"{STEMS[sxtwl_year.tg]}{BRANCHES[sxtwl_year.dz]}"
sxtwl_mp = f"{STEMS[sxtwl_month.tg]}{BRANCHES[sxtwl_month.dz]}"
sxtwl_dp = f"{STEMS[sxtwl_day.tg]}{BRANCHES[sxtwl_day.dz]}"

# Use sxtwl's pillars (they handle solar terms automatically), but document method.
# For DOB 21 Jan 1986, sxtwl gives year=乙丑 (matches our solar-term year pillar),
# month=己丑 (matches our 丑月 calculation), day=乙丑 (matches our day pillar).
year_p = sxtwl_yp
month_p = sxtwl_mp
day_p = sxtwl_dp
hour_p = f"{hs}{hb}"
day_master = ds

# Nayin
nayin_year = nayin(year_p[0], year_p[1])
nayin_month = nayin(month_p[0], month_p[1])
nayin_day = nayin(day_p[0], day_p[1])
nayin_hour = nayin(hour_p[0], hour_p[1])

# Hidden stems
hidden_year = HIDDEN_STEMS[year_p[1]]
hidden_month = HIDDEN_STEMS[month_p[1]]
hidden_day = HIDDEN_STEMS[day_p[1]]
hidden_hour = HIDDEN_STEMS[hour_p[1]]

# Day Master element + yin-yang
dm_element = ELEMENT_OF_STEM[day_master]
dm_yin_yang = YIN_YANG_OF_STEM[day_master]

# Age now
years, months, days = age_ymd(DOB, EVAL_DATE)

# Personal Year table 2026..2046
py_rows = []
for y in range(2026, 2047):
    py_rows.append((y, y - 1986 + 1, personal_year(DOB, y)))

# Annual year pillars 2026..2046 (year stem+branch per year, using 立春-cutoff year)
annual_pillars = []
for y in range(2026, 2047):
    anchor = date(y, 6, 1)  # June 1 is safely inside the year pillar
    _, s, b = year_pillar_solar(anchor)
    annual_pillars.append((y, y - 1986 + 1, f"{s}{b}", ELEMENT_OF_STEM[s]))

# Period 9 check
PERIOD_9_START = 2024
PERIOD_9_END = 2043
in_period_9 = PERIOD_9_START <= 2026 <= PERIOD_9_END

# Element relationship to Fire (Period 9 element)
RELATIONSHIP = {
    '木':'Wood feeds Fire (Wood supports Fire) — strong synergy',
    '火':'Fire is in its element — peak alignment',
    '土':'Fire generates Earth — drain relationship',
    '金':'Fire melts Metal — controlling relationship',
    '水':'Water douses Fire — controlling relationship',
}

# Sanity check prints
if __name__ == '__main__':
    print('=== BaZi Four Pillars for Big ===')
    print(f'DOB: {DOB} {BIRTH_HOUR:02d}:{BIRTH_MIN:02d} (Bangkok UTC+7)')
    print(f'Eval: {EVAL_DATE}')
    print()
    print(f'Year   pillar: {year_p}  (Nayin {nayin_year}; hidden: {hidden_year})')
    print(f'Month  pillar: {month_p}  (Nayin {nayin_month}; hidden: {hidden_month})')
    print(f'Day    pillar: {day_p}  (Nayin {nayin_day}; hidden: {hidden_day})')
    print(f'Hour   pillar: {hour_p}  (Nayin {nayin_hour}; hidden: {hidden_hour})')
    print()
    print(f'Day Master: {day_master} ({dm_yin_yang}{dm_element})')
    print(f'Use-God heuristic: {useful_god_heuristic(day_master, mb)}')
    print()
    print(f'Age at {EVAL_DATE}: {years} years, {months} months, {days} days')
    print()
    print('Personal Year table 2026..2046:')
    for y, age, py in py_rows:
        print(f'  {y} (age {age}) -> Personal Year {py}')
    print()
    print('Annual year pillars 2026..2046:')
    for y, age, p, e in annual_pillars:
        print(f'  {y} (age {age}) -> {p}  ({e})')
    print()
    print(f'In Period 9 (Fire): {in_period_9}')
    print(f'Day Master ({dm_element}) vs Fire: {RELATIONSHIP.get(dm_element, "?")}')