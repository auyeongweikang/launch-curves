"""Draws a fixed random sample of the figures the curves use, for an independent re-check.

Writes data/verify/sample_<n>.csv (one file per checker). Each row is a printed figure with its
source, so a checker can open the document and compare. Run: python -I scripts/sample_for_check.py
"""
import csv
import random
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PER_DRUG, CHECKERS, SEED = 3, 3, 20261119

rows = list(csv.DictReader((ROOT / 'data' / 'sales_clean.csv').open(encoding='utf-8')))
by_drug = defaultdict(list)
for r in rows:
    # The figures the curves use: quarterly US rows, or the company total for the small companies.
    if r['value'] and r['period_type'] in ('quarter', 'year') and r['region'] in ('US', 'World'):
        by_drug[r['drug']].append(r)
rng = random.Random(SEED)
sample = []
for drug in sorted(by_drug):
    us = [r for r in by_drug[drug] if r['region'] == 'US'] or by_drug[drug]
    sample += rng.sample(us, min(PER_DRUG, len(us)))
rng.shuffle(sample)
out = ROOT / 'data' / 'verify'
out.mkdir(exist_ok=True)
cols = ['check_id', 'drug', 'reporting_company', 'calendar_quarter', 'company_period', 'period_type', 'region',
        'value', 'currency', 'unit', 'method', 'source_title', 'source_url', 'source_location', 'label_as_printed', 'notes']
for k in range(CHECKERS):
    part = sorted(sample[k::CHECKERS], key=lambda r: (r['reporting_company'], r['calendar_quarter']))
    with (out / f'sample_{k + 1}.csv').open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, cols, extrasaction='ignore')
        w.writeheader()
        for i, r in enumerate(part, 1):
            w.writerow({**r, 'check_id': f'{k + 1}-{i:02d}'})
    print(f'sample_{k + 1}.csv: {len(part)} figures')
