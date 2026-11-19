# Immunology launch curves

Quarterly US net sales for 34 immunology drug launches (first approved 2005–2024), taken from
company filings and lined up from each drug's first quarter of US sales. The library is used to
test the US sales ramp in my Abivax (ABVX) model for obefazimod in ulcerative colitis against what
real launches have done.

The write-up, with the charts and the conclusions, is project 2 on my portfolio site:
<https://auyeongweikang.github.io> (type `PRJ 2` in the command bar).

- 2,172 printed figures, each with a link to the document and the table it came from (529 documents).
- 29 launches have a US curve; 28 are compared with the model.
- Data as collected on 19 November 2026, to the third quarter of 2026.

## What is here

| Path | What it is |
|---|---|
| `data/sales_clean.csv` | Every figure in one file: drug, company, quarter, region, value as printed, currency, the US-dollar value, and its source |
| `data/curves_us_quarterly.csv` | US sales by quarter since launch, one column per drug |
| `data/launch_years_us.csv` | US sales in launch years 1–5, with the basis of each drug's figures |
| `data/comparison.csv` | Each year: the library's middle and top quarter, the two ulcerative colitis launches, the ABVX cases and how many launches beat them |
| `data/writeup_tables.md` | The three tables in the write-up |
| `data/charts/` | The three charts in the write-up, as tables |
| `data/checks.md` | Problems the merge found: gaps, launches left out, which company's figure counts |
| `data/verify/` | The random sample that was re-checked against its sources, and the result for each figure |
| `data/drug_list.csv` | The 34 launches |
| `data/raw/<group>_sales.csv` | The figures as collected, one file per group of companies |
| `data/raw/<group>_launches.csv` | FDA approval dates, indications, route and mechanism |
| `data/raw/<group>_notes.md` | How each company reports, gaps, restatements and full-year checks |
| `data/fx/` | Daily exchange rates (Federal Reserve H.10 series, downloaded from FRED) |
| `docs/collection-spec.md` | The rules the figures were collected under |
| `model/ABVX.xlsx` | The ABVX model the library is compared with |
| `scripts/` | `build_dataset.py` merges and checks the raw files; `analyse.py` makes the comparison; `sample_for_check.py` draws the sample for re-checking |

## How to check a figure

Open `data/sales_clean.csv` and find the drug and quarter. `source_url` opens the company's
document, `source_location` says which table, row and column, and `label_as_printed` is the
product line as the company wrote it. `value`, `currency` and `unit` are what is printed there;
`usd_m` is that figure in millions of US dollars (`fx_usd_per_unit` is the rate used).

If you find a wrong figure, please open an issue with the drug, the quarter and what the
document says.

## How the data was collected

- **Who read the filings.** AI research agents (Claude) found the documents, read the figures and
  recorded each one with its source, working to the written rules in `docs/collection-spec.md`.
  The main rule: every figure comes from a document that was opened and read, and a figure that
  cannot be found is left blank, never estimated. Some documents were read from copies I had
  already downloaded (the notes files call this archive the "Biotech Vault"); the link recorded
  is always the document's public address.
- **Full-year check.** For each drug, the four quarters of every complete year were added up and
  compared with the company's printed annual figure. The results are in the notes files.
- **Sample re-check.** A separate set of agents reopened 99 randomly chosen figures (three for
  each drug, about 5% of all figures) and compared value, quarter, region and unit with the
  source. All 99 matched (`data/verify/`).
- **What that does and does not show.** The figures were not each checked by a person. A clean
  sample of 99 makes widespread errors unlikely, but a few wrong figures may remain among the
  rest. Every figure can be checked against its link.

## Choices that shape the results

- **Quarter 1** is the first calendar quarter with US sales; launch years are four quarters from there.
- **Left out of the curves:** Stelara and Simponi (2009 sales never printed), Velsipity (never
  printed separately), Cimzia and Bimzelx (half-year figures only).
- **Left out of the comparison:** Olumiant (its US sales include COVID-19 emergency use from 2021).
- **Company totals:** five small companies print one total, described as all or mostly US, and
  that total is used (`basis` in `launch_years_us.csv`).
- **One one-off taken out:** $246M inside Opzelura's Q2 2026 sales, a reversal of rebate accruals
  that Incyte reported. It is removed in `analyse.py` (`ONE_OFFS`); the printed figure stays in
  `sales_clean.csv`.
- **Not adjusted for inflation,** and all diseases together, not one.

The write-up's Limits section says what the comparison can and cannot support.

## Running it again

```
pip install openpyxl
python -I scripts/build_dataset.py   # merge and check the raw files
python -I scripts/analyse.py         # compare with the ABVX model; writes the tables and charts
```

Both scripts write only inside `data/`. Rules for which company's figure counts when two print
one (Tezspire, Benlysta, Vtama, Entyvio's two currencies) are at the top of `build_dataset.py`.

## Licence

The scripts are under the MIT licence (`LICENSE`). The data, notes, rules and model are under
Creative Commons Attribution 4.0 (`LICENSE-DATA.md`). The sales figures themselves are facts
from the companies' public filings.

Nothing here is investment advice.
