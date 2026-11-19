"""Launch curves: merges the collectors' raw files into one checked dataset.

Reads   data/raw/<group>_sales.csv, <group>_launches.csv, data/drug_list.csv, data/fx/*.csv
Writes  data/sales_clean.csv          every printed figure, with its US-dollar value
        data/curves_us_quarterly.csv  US net sales by quarter since US launch, one column per drug
        data/launch_years_us.csv      US net sales in launch years 1-5, one row per drug
        data/checks.md                problems found, for a person to read

Run:    python -I scripts/build_dataset.py   (from the project folder or anywhere)
Nothing here estimates a figure: a quarter that is missing stays missing, and a
launch year with a missing quarter has no total.
"""
import csv
import statistics
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data' / 'raw'
OUT = ROOT / 'data'
FX = ROOT / 'data' / 'fx'

SALES_COLS = ['drug', 'reporting_company', 'calendar_quarter', 'company_period', 'period_type', 'region',
              'value', 'currency', 'unit', 'method', 'source_title', 'source_date', 'source_url',
              'source_location', 'label_as_printed', 'notes']
LAUNCH_COLS = ['drug', 'generic', 'company_at_launch', 'reporting_companies', 'mechanism', 'route', 'dosing',
               'first_us_indication', 'us_approval_date', 'us_approval_source_url', 'uc_us_approval_date',
               'cd_us_approval_date', 'other_us_indications', 'first_quarter_with_us_sales', 'notes']
UNITS = {'millions': 1.0, 'million': 1.0, 'billions': 1000.0, 'billion': 1000.0,
         'thousands': 0.001, 'thousand': 0.001, 'hundred millions': 100.0, '100 millions': 100.0}
# FRED series: how many US dollars one unit of each currency buys, from the quoted direction.
FX_SERIES = {'EUR': ('DEXUSEU', False), 'GBP': ('DEXUSUK', False), 'JPY': ('DEXJPUS', True), 'CHF': ('DEXSZUS', True)}

def source_for(drug, region, quarter):
    """Which company's printed figure is the drug's sales in this region and quarter, where
    more than one company prints a figure. None means any (there is only one); 'skip' means
    no printed figure is the drug's sales. Taken from the collectors' notes (data/raw/*_notes.md)."""
    if drug == 'Tezspire':
        # Amgen records US product sales; AstraZeneca records ex-US product sales and books its share
        # of US profit as collaboration revenue. Neither company's "World" is global sales.
        return {'US': 'Amgen'}.get(region, 'skip')
    if drug == 'Benlysta' and region in ('US', 'World') and quarter <= '2012Q3':
        # Until GSK bought Human Genome Sciences (3 Aug 2012), HGS booked US sales and GSK's figure
        # was its profit share plus sales elsewhere. 2012Q3 mixes the two, so it has no clean figure.
        return 'Human Genome Sciences' if region == 'US' and quarter <= '2012Q2' else 'skip'
    return None


# Quarters where the sales were split between two reporters (a drug changing hands), so
# both printed figures are added. {drug: {quarter, ...}}
# Vtama 2024Q4: Roivant (Dermavant) to 28 Oct 2024, Organon from then (both say so).
ADD_REPORTERS = {'Vtama': {'2024Q4'}}

# Where a company prints the same quarter in two currencies, the one used. Takeda printed Entyvio's
# US sales in dollars as well as yen until FY2016 (2017Q1); the dollar table is product sales only,
# the yen one adds royalty and service income. The two agree within about 3%.
PREFER_CURRENCY = {'Entyvio': 'USD'}

# Smaller companies that print one sales total per quarter, which their filings describe as all
# or mostly US. Their curves use that total, so they can only overstate US sales. The text is
# the basis shown with the figures (from data/raw/smallcaps_notes.md).
COMPANY_TOTAL = {
    'Lupkynis': 'company total: US only until 2022Q2, then also includes supply sales to Otsuka (split not printed)',
    'Zoryve': 'company total: US only until 2023Q1; Canada from June 2023, under 10% of sales (Arcutis 10-K)',
    'Vtama': 'company total: US only under Roivant; Organon total from 28 Oct 2024 (ex-US $1-4M a quarter)',
    'Opzelura': 'company total: US only until 2023Q1; Europe from 2023Q2 (about 15% of sales where printed)',
    'Nemluvio': 'company total: US launch Aug 2024; Galderma says the vast majority of 2025 sales were US',
}

issues = []


def say(kind, drug, text):
    issues.append((kind, drug, text))


def q_index(q):
    y, n = int(q[:4]), int(q[5])
    return y * 4 + n - 1


def q_label(i):
    return f'{i // 4}Q{i % 4 + 1}'


def fx_quarterly():
    """Average daily rate per calendar quarter, as US dollars per unit of currency."""
    rates = {'USD': defaultdict(lambda: 1.0)}
    for cur, (series, invert) in FX_SERIES.items():
        sums = defaultdict(list)
        with (FX / f'{series}.csv').open(encoding='utf-8') as f:
            for row in csv.DictReader(f):
                d, v = row.get('observation_date') or row.get('DATE'), row.get(series)
                if not v or v == '.':
                    continue
                dt = date.fromisoformat(d)
                sums[f'{dt.year}Q{(dt.month - 1) // 3 + 1}'].append(float(v))
        rates[cur] = {q: (1 / statistics.mean(v) if invert else statistics.mean(v)) for q, v in sums.items()}
    return rates


def read_csv(path, cols):
    with path.open(encoding='utf-8-sig', newline='') as f:
        r = csv.DictReader(f)
        missing = [c for c in cols if c not in (r.fieldnames or [])]
        if missing:
            say('format', path.name, f'missing columns: {", ".join(missing)}')
        return [{k: (v or '').strip() for k, v in row.items() if k} for row in r]


def main():
    drugs = {r['drug']: r for r in read_csv(OUT / 'drug_list.csv', ['group', 'drug', 'generic'])}
    fx = fx_quarterly()
    sales, launches = [], {}
    for path in sorted(RAW.glob('*_sales.csv')):
        for row in read_csv(path, SALES_COLS):
            row['_file'] = path.name
            sales.append(row)
    for path in sorted(RAW.glob('*_launches.csv')):
        for row in read_csv(path, LAUNCH_COLS):
            if row['drug'] in launches:
                say('duplicate', row['drug'], f'launch facts given twice ({path.name})')
            launches[row['drug']] = row

    # ---- every printed figure, checked and put into US dollars ----
    clean = []
    for row in sales:
        d = row['drug']
        if d not in drugs:
            say('format', d, f'"{d}" is not in drug_list.csv ({row["_file"]})')
            continue
        q, cur, unit = row['calendar_quarter'], row['currency'].upper(), row['unit'].lower()
        if len(q) != 6 or q[4] != 'Q' or not q[:4].isdigit() or q[5] not in '1234':
            say('format', d, f'calendar_quarter "{q}" is not YYYYQn')
            continue
        if not row['value']:
            row['usd_m'] = ''
            clean.append(row)
            continue
        try:
            v = float(row['value'].replace(',', ''))
        except ValueError:
            say('format', d, f'{q} {row["region"]}: value "{row["value"]}" is not a number')
            continue
        if unit not in UNITS:
            say('format', d, f'{q}: unknown unit "{row["unit"]}"')
            continue
        if cur not in fx:
            say('format', d, f'{q}: unknown currency "{cur}"')
            continue
        # A half year is converted at the average of its two quarters, a year at its four.
        span = {'quarter': 1, 'half': 2, 'year': 4}.get(row['period_type'], 1)
        qs = [q_label(q_index(q) - k) for k in range(span)]
        try:
            rate = statistics.mean(fx[cur][x] for x in qs) if cur != 'USD' else 1.0
        except KeyError:
            say('fx', d, f'{q}: no exchange rate for {cur}')
            continue
        if v < 0:
            say('value', d, f'{q} {row["region"]}: negative figure {v} (returns or reversals?)')
        row['usd_m'] = round(v * UNITS[unit] * rate, 3)
        row['fx_usd_per_unit'] = round(rate, 6)
        clean.append(row)

    # ---- one US figure per drug and quarter ----
    us = defaultdict(dict)      # drug -> quarter index -> usd_m
    world = defaultdict(dict)
    by_key = defaultdict(list)
    for row in clean:
        if row['period_type'] == 'quarter' and row['usd_m'] != '':
            by_key[(row['drug'], row['calendar_quarter'], row['region'])].append(row)
    for (d, q, region), rows in list(by_key.items()):
        rule = source_for(d, region, q)
        if rule == 'skip':
            del by_key[(d, q, region)]
            continue
        if rule:
            rows = by_key[(d, q, region)] = [r for r in rows if r['reporting_company'] == rule]
            if not rows:
                del by_key[(d, q, region)]
                continue
        if len(rows) > 1 and d in PREFER_CURRENCY and any(r['currency'] == PREFER_CURRENCY[d] for r in rows):
            rows = [r for r in rows if r['currency'] == PREFER_CURRENCY[d]]
        if len(rows) > 1:
            companies = sorted({r['reporting_company'] for r in rows})
            if q in ADD_REPORTERS.get(d, ()):
                v = sum(r['usd_m'] for r in rows)
            elif len({r['usd_m'] for r in rows}) == 1:
                v = rows[0]['usd_m']
            else:
                say('conflict', d, f'{q} {region}: {len(rows)} different figures from {", ".join(companies)}; none used')
                continue
        else:
            v = rows[0]['usd_m']
        if region == 'US':
            us[d][q_index(q)] = v
        elif region == 'World':
            world[d][q_index(q)] = v
    for (d, q, region), rows in by_key.items():   # US + ExUS = World, when World is not printed
        i = q_index(q)
        if region == 'US' and i not in world[d] and (d, q, 'ExUS') in by_key and len(by_key[(d, q, 'ExUS')]) == 1:
            world[d][i] = round(us[d].get(i, 0) + by_key[(d, q, 'ExUS')][0]['usd_m'], 3)
    for d in us:
        for i, v in us[d].items():
            if i in world[d] and v > world[d][i] * 1.001:
                say('value', d, f'{q_label(i)}: US {v} is above World {world[d][i]}')

    # Printed full-year US figures, for launch years that are calendar years (a first quarter launch).
    us_year = defaultdict(dict)
    for row in clean:
        if row['period_type'] == 'year' and row['region'] == 'US' and row['usd_m'] != '':
            us_year[row['drug']][int(row['calendar_quarter'][:4])] = row['usd_m']

    # ---- line each drug up from its first quarter of US sales ----
    curves, years, start, basis = {}, {}, {}, {}
    for d in drugs:
        series_region = 'World' if d in COMPANY_TOTAL else 'US'
        series = world.get(d) if d in COMPANY_TOTAL else us.get(d)
        basis[d] = COMPANY_TOTAL.get(d, 'US net sales as printed')
        if not series and d in us_year:
            # No quarterly US figures, but printed US years. If those years start with the
            # launch quarter (a first-quarter launch), they are the launch years themselves.
            given = launches.get(d, {}).get('first_quarter_with_us_sales', '')
            y0 = min(us_year[d])
            if given == f'{y0}Q1':
                start[d], curves[d] = q_index(given), [None] * 20
                years[d] = [round(us_year[d][y0 + y], 1) if y0 + y in us_year[d] else None for y in range(5)]
                basis[d] = 'US net sales, printed only for full years (launch in a first quarter, so launch years are calendar years)'
                say('check', d, f'no quarterly US figures; launch years taken from printed US full years from {y0}')
                continue
        if not series:
            say('gap', d, 'no US quarterly figures, so it has no launch curve')
            continue
        us[d] = series
        first = min(i for i, v in us[d].items() if v > 0)
        given = launches.get(d, {}).get('first_quarter_with_us_sales', '')
        # US quarters listed but not found before the first figure. If the collector established
        # the launch quarter from the filings (for example from worldwide sales), the curve starts
        # there with those quarters left blank; otherwise the launch quarter is unknown, lining the
        # drug up would mean guessing, and it stays in sales_clean only.
        blank_before = sorted(q_index(r['calendar_quarter']) for r in clean
                              if r['drug'] == d and r['region'] == series_region and r['usd_m'] == ''
                              and r['period_type'] == 'quarter' and q_index(r['calendar_quarter']) < first)
        if blank_before and not given:
            say('excluded', d, f'US figures for {", ".join(q_label(i) for i in blank_before)} were not printed, '
                               f'so the launch quarter is not known; left out of the curves')
            continue
        if given and q_index(given) < first:
            say('check', d, f'launch facts put the first US quarter at {given}; US figures start at '
                            f'{q_label(first)}, so the quarters between are blank')
            first = q_index(given)
        elif given and given != q_label(first):
            say('check', d, f'first US quarter in the figures is {q_label(first)}, launch facts say {given}')
        start[d] = first
        last = max(us[d])
        curve = [us[d].get(first + k) for k in range(20)]
        for k in range(20):
            if first + k <= last and curve[k] is None:
                say('gap', d, f'quarter {k + 1} ({q_label(first + k)}) has no US figure')
        curves[d] = curve
        years[d] = [round(sum(curve[4 * y:4 * y + 4]), 1) if all(v is not None for v in curve[4 * y:4 * y + 4]) else None
                    for y in range(5)]

    # ---- write ----
    with (OUT / 'sales_clean.csv').open('w', encoding='utf-8', newline='') as f:
        cols = SALES_COLS + ['usd_m', 'fx_usd_per_unit']
        w = csv.DictWriter(f, cols, extrasaction='ignore')
        w.writeheader()
        for row in sorted(clean, key=lambda r: (r['drug'], r['calendar_quarter'], r['region'], r['reporting_company'])):
            w.writerow(row)
    order = sorted(curves, key=lambda d: start[d])
    with (OUT / 'curves_us_quarterly.csv').open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['Quarter'] + order)
        for k in range(20):
            w.writerow([k + 1] + ['' if curves[d][k] is None else round(curves[d][k], 1) for d in order])
    with (OUT / 'launch_years_us.csv').open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['drug', 'group', 'first_us_quarter', 'first_us_indication', 'route', 'uc_us_approval_date',
                    'year1', 'year2', 'year3', 'year4', 'year5', 'basis'])
        for d in order:
            L = launches.get(d, {})
            w.writerow([d, drugs[d]['group'], q_label(start[d]), L.get('first_us_indication', ''), L.get('route', ''),
                        L.get('uc_us_approval_date', '')] + ['' if v is None else v for v in years[d]] + [basis[d]])
    with (OUT / 'checks.md').open('w', encoding='utf-8') as f:
        f.write(f'# Checks ({date.today().isoformat()})\n\n')
        f.write(f'{len(clean)} figures from {len({r["_file"] for r in clean})} files; '
                f'{len(curves)} of {len(drugs)} drugs have a US launch curve.\n\n')
        for kind in ('format', 'duplicate', 'conflict', 'excluded', 'value', 'fx', 'check', 'gap'):
            rows = [(d, t) for k, d, t in issues if k == kind]
            if rows:
                f.write(f'## {kind} ({len(rows)})\n\n' + ''.join(f'- {d}: {t}\n' for d, t in rows) + '\n')
    print(f'{len(clean)} figures, {len(curves)} curves, {len(issues)} issues (see data/checks.md)')


if __name__ == '__main__':
    main()
