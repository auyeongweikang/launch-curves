"""Launch curves: compares the ABVX model's US sales ramp with the launch library.

Reads   data/launch_years_us.csv and data/curves_us_quarterly.csv (from build_dataset.py)
        and the ABVX workbook (model/ABVX.xlsx)
Writes  data/comparison.csv        each launch year: the library, the ABVX cases, ranks
        data/writeup_tables.md     the write-up's three tables
        data/charts/*.csv          the three charts shown with the write-up
        prints the figures the write-up quotes

Run:    python -I scripts/analyse.py
"""
import csv
import statistics
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'


def local_paths():
    """Optional settings in local_paths.txt next to the README, one "name = path" per line
    (the file is not part of the public copy):
        model         the ABVX workbook to read instead of model/ABVX.xlsx
        chart_copies  a second folder that also gets the three chart files"""
    out, path = {}, ROOT / 'local_paths.txt'
    if path.is_file():
        for line in path.read_text(encoding='utf-8-sig').splitlines():
            name, sep, value = line.partition('=')
            if sep and not line.lstrip().startswith('#') and value.strip():
                out[name.strip().lower()] = Path(value.strip().strip('"'))
    return out


LOCAL = local_paths()
MODEL = LOCAL.get('model', ROOT / 'model' / 'ABVX.xlsx')
CHART_FOLDERS = [DATA / 'charts'] + ([LOCAL['chart_copies']] if 'chart_copies' in LOCAL else [])
MODEL_20, MODEL_40 = 'ABVX 20% case', 'ABVX 40% case'   # the model's lines, as named on the charts
NAMED = ['Entyvio', 'Omvoh', 'Skyrizi']   # launches named on the quarterly chart: the two UC launches and the largest
CASES = {'20%': 'UC 20% to 2039', '40%': 'UC 40% to 2039'}
# Not a normal launch curve: Olumiant's US figures include COVID-19 emergency-use sales from 2021.
LEAVE_OUT = {'Olumiant': 'includes COVID-19 emergency-use sales from 2021Q3'}
# The launches that started in ulcerative colitis, the closest comparisons for the model.
UC_FIRST = ['Entyvio', 'Omvoh']
# A one-off amount a company printed inside a quarter's sales and gave the size of, taken out of
# the comparison and the charts ($M). The printed figure stays as it is in sales_clean.csv.
# Opzelura: Incyte's Q2 2026 release says net sales of $449.7M include a $246.0M one-time benefit
# from reversing Medicaid rebate accruals built up to March 2026, and were $204M without it. The
# accruals had lowered sales in quarters from 2023 on by amounts Incyte did not print, so those
# earlier quarters stay as printed (a little low).
ONE_OFFS = {'Opzelura': {'2026Q2': 246.0}}


def q_index(q):
    return int(q[:4]) * 4 + int(q[5]) - 1


def model_ramp():
    """US revenue in each year from launch, as saved in the workbook (Excel computes it), and for
    the 20% case what that revenue is made of: the share and the size of the market."""
    wb = openpyxl.load_workbook(MODEL, data_only=True, read_only=True)
    ramp, parts = {}, {}
    for case, sheet in CASES.items():
        rows = {r[0]: r for r in wb[sheet].iter_rows(values_only=True) if r and r[0]}
        k = rows['FORECAST ($M)'][1:].index(rows['US launch year'][1])
        ramp[case] = [round(rows['Revenue'][1:][k + y], 1) for y in range(6)]
        if case == '20%':
            parts = {'share': [rows['Obefazimod share'][1:][k + y] for y in range(6)],
                     'market': [rows['US UC drug market'][1:][k + y] for y in range(6)],
                     'market_2025': rows['US UC drug market, 2025 ($m)'][1],
                     'launch': rows['US launch year'][1]}
    return ramp, parts


def percentile(xs, p):
    xs = sorted(xs)
    if len(xs) == 1:
        return xs[0]
    pos = (len(xs) - 1) * p
    lo = int(pos)
    return xs[lo] + (xs[min(lo + 1, len(xs) - 1)] - xs[lo]) * (pos - lo)


# Short names for the first US indication and the route, for the write-up's tables (from the launches files).
FIRST = {'Skyrizi': 'Psoriasis', 'Rinvoq': 'Rheumatoid arthritis', 'Otezla': 'Psoriatic arthritis', 'Fasenra': 'Severe asthma',
         'Saphnelo': 'Lupus', 'Tezspire': 'Severe asthma', 'Nucala': 'Severe asthma', 'Benlysta': 'Lupus',
         'Orencia': 'Rheumatoid arthritis', 'Zeposia': 'Multiple sclerosis', 'Sotyktu': 'Psoriasis', 'Tremfya': 'Psoriasis',
         'Taltz': 'Psoriasis', 'Olumiant': 'Rheumatoid arthritis', 'Omvoh': 'Ulcerative colitis', 'Ebglyss': 'Atopic dermatitis',
         'Xeljanz': 'Rheumatoid arthritis', 'Cibinqo': 'Atopic dermatitis', 'Cosentyx': 'Psoriasis', 'Dupixent': 'Atopic dermatitis',
         'Kevzara': 'Rheumatoid arthritis', 'Actemra': 'Rheumatoid arthritis', 'Vyvgart': 'Myasthenia gravis',
         'Opzelura': 'Atopic dermatitis', 'Lupkynis': 'Lupus nephritis', 'Zoryve': 'Psoriasis', 'Vtama': 'Psoriasis',
         'Nemluvio': 'Prurigo nodularis', 'Entyvio': "Ulcerative colitis and Crohn's"}
ROUTE = {'Rinvoq': 'pill', 'Otezla': 'pill', 'Zeposia': 'pill', 'Sotyktu': 'pill', 'Olumiant': 'pill', 'Xeljanz': 'pill',
         'Cibinqo': 'pill', 'Lupkynis': 'pill', 'Opzelura': 'cream', 'Zoryve': 'cream', 'Vtama': 'cream',
         'Saphnelo': 'infusion', 'Benlysta': 'infusion', 'Orencia': 'infusion', 'Actemra': 'infusion', 'Vyvgart': 'infusion',
         'Entyvio': 'infusion'}


def money(v):
    return '' if v is None else f'{v:,.0f}'


def write_tables(rows, years, out, parts, full):
    """Markdown tables for the write-up, so its figures come from the data, not from typing."""
    def line(label, cells):
        return f'| {label} | ' + ' | '.join(cells) + ' |'

    head = ['| | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |', '|---|---:|---:|---:|---:|---:|']
    # 1. The library against the model.
    lines = ['Table 1: the library against the model', ''] + head
    lines.append(line('Launches with a figure', [str(r['launches']) for r in out]))
    lines.append(line('Median launch', [money(r['median']) for r in out]))
    lines.append(line(f'Median of the {len(full)} launches with all five years', [money(r['cohort_median']) for r in out]))
    lines.append(line('Top quarter starts at', [money(r['p75']) for r in out]))
    lines.append(line('Largest', [f"{money(r['max'])} ({r['max_drug']})" for r in out]))
    for d in UC_FIRST:
        lines.append(line(d, [money(years[d][y]) for y in range(5)]))
    for case in ('20%', '40%'):
        lines.append(line(f'ABVX model, {case} case', [money(r[f'abvx_{case}']) for r in out]))
        lines.append(line(f'Launches above the {case} case', [str(r[f'abvx_{case}_beaten_by']) for r in out]))
    # 2. What the 20% case is made of.
    lines += ['', 'Table 2: what the 20% case is made of', ''] + head
    lines.append(line('Share of US UC sales', [f"{r['share_20']:.1f}%" for r in out]))
    lines.append(line('US UC market', [money(r['market']) for r in out]))
    lines.append(line('Sales (share of that market)', [money(r['abvx_20%']) for r in out]))
    lines.append(line(f"Same share of the 2025 market (${parts['market_2025']:,.0f}M)", [money(r['flat_20']) for r in out]))
    lines.append(line('Launches above that', [str(r['flat_20_beaten_by']) for r in out]))
    # 3. Every launch.
    lines += ['', 'Table 3: every launch', '',
              '| Drug | Launched (US) | First disease | Form | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |',
              '|---|---|---|---|---:|---:|---:|---:|---:|']
    for r in sorted(rows, key=lambda r: r['first_us_quarter']):
        d = r['drug']
        v = years[d] if d in years else [float(r[f'year{y}']) if r[f'year{y}'] else None for y in range(1, 6)]
        mark = ('*' if r['basis'].startswith('company total') else '') + ('†' if d in LEAVE_OUT else '') + ('‡' if d in ONE_OFFS else '')
        lines.append(f"| {d}{mark} | {r['first_us_quarter'][:4]} Q{r['first_us_quarter'][5]} | {FIRST.get(d, '')} | "
                     f"{ROUTE.get(d, 'injection')} | " + ' | '.join(money(x) for x in v) + ' |')
    (DATA / 'writeup_tables.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')


def num(v):
    """A figure for a chart file: blank when missing, no trailing .0."""
    return '' if v is None else f'{v:.1f}'.rstrip('0').rstrip('.')


def write_chart(name, options, head, body):
    """One chart file for the site: "# key: value" lines that say how it is drawn, then the
    table. Written to data/charts (and to the chart_copies folder, if local_paths.txt names one)."""
    lines = [f'# {k}: {v}' for k, v in options.items()]
    for folder in CHART_FOLDERS:
        folder.mkdir(exist_ok=True)
        with (folder / name).open('w', encoding='utf-8', newline='') as f:
            f.write(''.join(line + '\n' for line in lines))
            w = csv.writer(f)
            w.writerow(head)
            w.writerows(body)


def write_charts(years, ramp, full, start):
    """The three charts: every launch by quarter, each year ranked, and the shape of the climb."""
    # 1. Every launch by quarter. The model has yearly figures only, so each of its quarters is
    #    a quarter of that year's figure (a step, not an estimate of the path inside the year).
    with (DATA / 'curves_us_quarterly.csv').open(encoding='utf-8') as f:
        rows = list(csv.reader(f))
    for d, items in ONE_OFFS.items():          # the same one-offs come out of the quarterly lines
        col = rows[0].index(d)
        for q, amount in items.items():
            cell = rows[1 + q_index(q) - start[d]]
            cell[col] = num(float(cell[col]) - amount)
    keep = [k for k, d in enumerate(rows[0]) if k and d not in LEAVE_OUT and any(r[k] for r in rows[1:])]
    order = sorted(keep, key=lambda k: (rows[0][k] in NAMED, k))   # named launches last, so they draw on top
    head = ['Quarter'] + [rows[0][k] for k in order] + [MODEL_40, MODEL_20]
    body = [[r[0]] + [r[k] for k in order] + [num(ramp[c][(int(r[0]) - 1) // 4] / 4) for c in ('40%', '20%')]
            for r in rows[1:]]
    write_chart('Launch curves by quarter.csv',
                {'unit': '$M', 'scale': 'log', 'floor': 1, 'accent': f'{MODEL_20}; {MODEL_40}',
                 'dashed': MODEL_40, 'highlight': '; '.join(NAMED)}, head, body)
    # 2. Each launch year ranked, with the model's two cases among the launches.
    drugs = sorted(years, key=lambda d: -max(v for v in years[d] if v is not None))
    head = ['Year'] + drugs + [MODEL_20, MODEL_40]
    body = [[y + 1] + [num(years[d][y]) for d in drugs] + [num(ramp['20%'][y]), num(ramp['40%'][y])] for y in range(5)]
    write_chart('Launch curves ranked.csv',
                {'form': 'ranked', 'unit': '$M', 'accent': f'{MODEL_20}; {MODEL_40}', 'highlight': '; '.join(UC_FIRST)},
                head, body)
    # 3. The shape of the climb: each year as a percentage of the launch's own year 5, for the
    #    launches with all five years.
    cohort = [d for d in drugs if d in full]
    middle = [statistics.median(years[d][y] / years[d][4] for d in cohort) * 100 for y in range(5)]
    head = ['Year'] + cohort + ['Middle launch', MODEL_20]
    body = [[y + 1] + [num(years[d][y] / years[d][4] * 100) for d in cohort]
            + [num(middle[y]), num(ramp['20%'][y] / ramp['20%'][4] * 100)] for y in range(5)]
    write_chart('Launch curves shape.csv',
                {'unit': '%', 'accent': MODEL_20, 'highlight': 'Middle launch'}, head, body)
    print(f'Charts: {len(order)} launches by quarter ({len(order) - len(NAMED)} grey), {len(drugs)} ranked, '
          f'{len(cohort)} with all five years;', 'middle launch as % of its year 5:', [round(m) for m in middle],
          '| model', [round(ramp["20%"][y] / ramp["20%"][4] * 100) for y in range(5)])


def main():
    rows = list(csv.DictReader((DATA / 'launch_years_us.csv').open(encoding='utf-8')))
    start = {r['drug']: q_index(r['first_us_quarter']) for r in rows}
    years = {r['drug']: [float(r[f'year{y}']) if r[f'year{y}'] else None for y in range(1, 6)]
             for r in rows if r['drug'] not in LEAVE_OUT}
    for d, items in ONE_OFFS.items():
        for q, amount in items.items():
            y = (q_index(q) - start[d]) // 4
            print(f'One-off taken out: {d} {q} (launch year {y + 1}) {amount}; year {y + 1} {years[d][y]} -> {round(years[d][y] - amount, 1)}')
            years[d][y] = round(years[d][y] - amount, 1)
    ramp, parts = model_ramp()
    full = [d for d in years if all(v is not None for v in years[d])]
    out = []
    for y in range(5):
        vals = {d: v[y] for d, v in years.items() if v[y] is not None}
        xs = list(vals.values())
        flat = round(parts['share'][y] * parts['market_2025'], 1)   # the same share, had the market stayed at its 2025 size
        row = {'year': y + 1, 'launches': len(xs),
               'p25': round(percentile(xs, 0.25), 1), 'median': round(statistics.median(xs), 1),
               'p75': round(percentile(xs, 0.75), 1), 'max': max(xs), 'max_drug': max(vals, key=vals.get),
               'cohort_median': round(statistics.median(years[d][y] for d in full), 1)}
        for d in UC_FIRST:
            row[d] = vals.get(d)
        for case, r in ramp.items():
            row[f'abvx_{case}'] = r[y]
            row[f'abvx_{case}_beaten_by'] = sum(1 for v in xs if v > r[y])
            row[f'abvx_{case}_above'] = sorted(d for d, v in vals.items() if v > r[y])
        row.update({'share_20': round(parts['share'][y] * 100, 1), 'market': round(parts['market'][y], 1), 'flat_20': flat,
                    'flat_20_beaten_by': sum(1 for v in xs if v > flat)})
        out.append(row)
    with (DATA / 'comparison.csv').open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, list(out[0].keys()))
        w.writeheader()
        w.writerows(out)
    write_charts(years, ramp, full, start)
    write_tables(rows, years, out, parts, full)

    # ---- the figures the notes quote ----
    print(f'Launches: {len(rows)} with a US curve, {len(years)} in the comparison (left out: {", ".join(LEAVE_OUT)}); '
          f'{len(full)} with all five years')
    for r in out:
        print(f"Year {r['year']}: n={r['launches']}, median {r['median']}, {len(full)}-launch median {r['cohort_median']}, "
              f"p75 {r['p75']}, max {r['max']} ({r['max_drug']}) | ABVX 20% {r['abvx_20%']} beaten by {r['abvx_20%_beaten_by']} "
              f"{r['abvx_20%_above']} | ABVX 40% {r['abvx_40%']} beaten by {r['abvx_40%_beaten_by']} {r['abvx_40%_above']}")
    print('No year 1 figure:', sorted(d for d in years if years[d][0] is None and any(v is not None for v in years[d][1:])))
    print(f"Model, 20% case, from {parts['launch']}: share {[round(s * 100, 1) for s in parts['share']]}, "
          f"market {[round(m) for m in parts['market']]}, sales {ramp['20%']} (year 6 is the first at the full share)")
    print(f"Same share of the 2025 market ({parts['market_2025']}):", [r['flat_20'] for r in out],
          'launches above:', [r['flat_20_beaten_by'] for r in out])
    print('The UC launches as a share of the 20% case:')
    for d in UC_FIRST:
        print(f'  {d}:', years[d], [None if v is None else round(v / ramp['20%'][y] * 100) for y, v in enumerate(years[d])])
    # Launches from 2017 on, priced closer to today; and the drugs with a US ulcerative colitis approval.
    recent = {d for d in years if int(next(r for r in rows if r['drug'] == d)['first_us_quarter'][:4]) >= 2017}
    print('Launches from 2017:', len(recent))
    for y in range(5):
        xs = [years[d][y] for d in recent if years[d][y] is not None]
        print(f'  year {y + 1}: n={len(xs)} median {round(statistics.median(xs), 1)} p75 {round(percentile(xs, 0.75), 1)}'
              f' | ABVX 20% beaten by {sum(1 for v in xs if v > ramp["20%"][y])}')
    uc = {r['drug']: r['uc_us_approval_date'] for r in rows if r['uc_us_approval_date'] and r['drug'] in years}
    print('Drugs with a US UC approval:', {d: (uc[d], next(r for r in rows if r['drug'] == d)['first_us_quarter']) for d in sorted(uc, key=uc.get)})
    growth = {d: round(v[4] / v[0], 1) for d, v in years.items() if v[0] and v[4]}
    print(f'Year 5 / year 1, {len(growth)} launches:', dict(sorted(growth.items(), key=lambda t: t[1])),
          'median', statistics.median(growth.values()), '| ABVX model', round(ramp['20%'][4] / ramp['20%'][0], 1))


if __name__ == '__main__':
    main()
