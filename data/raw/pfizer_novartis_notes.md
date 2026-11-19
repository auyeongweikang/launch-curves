# pfizer_novartis: collection notes

Collected 2026-11-19. All values are as printed, in USD millions. Every number in
`pfizer_novartis_sales.csv` was parsed from the text of the document named in its row.

## Coverage

| Drug | Window collected | Quarters with a value | Gaps | Rows |
|---|---|---|---|---|
| Xeljanz | 2012Q4 to 2017Q3 (US quarter 1 = 2012Q4, quarter 20 = 2017Q3) | 20 of 20 (US, ExUS, World, plus 3 Pfizer regions) | none | 120 |
| Velsipity | 2023Q4 to 2026Q3 (latest reported quarter) | 0 of 12 | all 12: not broken out | 36 |
| Cibinqo | 2022Q1 to 2026Q3 (quarter 1 = 2022Q1; quarter 19 = latest reported) | 19 of 19 (US, ExUS, World) | none | 75 |
| Cosentyx | 2014Q4 (zero check) and 2015Q1 to 2019Q4 (quarter 1 = 2015Q1, quarter 20 = 2019Q4) | World 20 of 20; US and ExUS 16 of 20 | US and ExUS for 2015Q1 to 2015Q4 | 61 |

Total: 292 rows in `pfizer_novartis_sales.csv`; 4 rows in `pfizer_novartis_launches.csv`.

## Pfizer (Xeljanz, Velsipity, Cibinqo)

**Where the numbers are.** Each quarterly earnings release (8-K Exhibit 99 or 99.1) has a
"Revenues" table by product with Worldwide, United States and Total International columns,
for the quarter and year to date, current and prior year. Until Q4 2023 it also had an
"International revenues by geographic region" table (Developed Europe, Developed Rest of
World, Emerging Markets); these are recorded as `Other:Developed Europe`,
`Other:Developed Rest of World` and `Other:Emerging Markets`. That table was dropped from
Q1 2024, so Cibinqo has regional rows only for 2022Q2 to 2022Q4 and 2023Q2 to 2023Q4.

**International lag (important for anyone lining up quarters).** Pfizer's subsidiaries
outside the US have a fiscal year ending November 30 (stated in the 10-Ks for 2020 to 2025).
The same lag applies in the Xeljanz years: the Q2 2013 10-Q says non-US results are for the
period ended May 26, 2013 (pfe-6302013x10q.htm), and the Q3 2026 10-Q says the non-US quarter
ended August 23, 2026 against September 27, 2026 for the US (pfe-20260927.htm). So `ExUS`
and the regional rows cover a quarter ending about one month earlier than `US`, and `World`
mixes the two. Rows use Pfizer's own quarter label as `calendar_quarter`.

**Dashes.** Where Pfizer prints a dash for a product and period, the row has value 0 and
the note "Printed as a dash; recorded as 0". This affects small early Xeljanz international
figures and Cibinqo Q2 2022 regions.

**Rounding.** Figures are rounded to whole millions, so US + International can differ from
Worldwide by 1 (for example Cibinqo Q2 2022: US 1, International 1, Worldwide 1).

**Xeljanz.** Not printed in Pfizer's own Q4 2012 or Q1 2013 releases (it first appears in
the Q2 2013 table). Q4 2012 (Worldwide 6, US 6, International dash) comes from the prior-year
column of the Q4 2013 release; Q1 2013 (Worldwide 11, US 11, International dash) from the
prior-year column of the Q1 2014 release. From Q1 2014 to Q2 2015 the table has an extra
business column ("GIP"), which does not affect the figures. There is a single "Xeljanz"
line; the releases do not print Xeljanz XR (approved 2016-02-23) separately.

**Cibinqo.** Not printed as its own line in the releases for Q4 2021 to Q1 2023 (it sat in
an "All other" line). Values for those quarters come from later documents that print them on
their own:
- 2022Q1: the 2022 column of Pfizer's "Recasted 2023 Product Revenue Tables" (investor
  relations PDF, 2024-04-23; not on EDGAR). Worldwide 5, US 3, International 2. This is the
  only document found that prints Q1 2022 on its own.
- 2022Q2, 2022Q3, 2022Q4: prior-year columns of the Q2, Q3 and Q4 2023 releases.
- 2023Q1: prior-year column of the Q1 2024 release (the recast PDF prints the same 16 / 8 / 8).
- From 2023Q2: each quarter's own release.
Pfizer's 2023 Form 10-K prints full-year 2021 Cibinqo revenue as a dash, so no 2021 quarter
is recorded even though the UK, Japan (September 2021) and EU (December 2021) approved it
before the US.

**Velsipity.** Never printed as a separate line. Checked: every earnings release Q4 2023 to
Q3 2026 (quarter and year-to-date tables), the 10-Q/10-K "Significant Product Revenues"
tables 2023 Q3 to 2026 Q3, the Recasted 2023 and Recasted 2025 and 2024 Product Revenue
Tables, and the Q2 and Q3 2026 Historical Product Revenues workbooks; a web search found no
Pfizer document with a Velsipity figure. Its sales sit inside an "All other" line; Pfizer
does not say which (the 2025 Form 10-K lists Velsipity in the Specialty Care inflammation and
immunology portfolio). All 36 Velsipity rows are blank with `not found: not broken out`;
nothing was derived from other lines. For context only: the Q4 2023 release reports a USD 1.4
billion impairment of etrasimod "based on a change in development plans for additional
indications and overall revenue expectations".

**Restatement checks.** Every Xeljanz quarter Q2 2013 to Q3 2017 was compared with the
prior-year column of the following year's release (including the Q1 to Q3 2018 releases),
for all six regions: no differences. Every Cibinqo quarter Q2 2023 to Q3 2025 was compared
with the following year's release: no differences. The Recasted 2023 tables and the
Recasted 2025 and 2024 tables (2026-04-20) print the same Cibinqo figures as the releases.

**Ownership.** Velsipity (etrasimod) came with Arena Pharmaceuticals, acquired by Pfizer on
2022-03-11 (Pfizer Q1 2022 10-Q), 19 months before FDA approval, so Pfizer is the only
company that has recorded sales. Xeljanz and Cibinqo were Pfizer products from the start.

## Novartis (Cosentyx)

**Where the numbers are.** Quarterly 6-K, Exhibit 99.2 ("Interim Financial Report"):
- An Immunology and Dermatology franchise table: Cosentyx total (worldwide) for the quarter
  and year to date, current and prior year.
- From Q1 2016, the "Net sales of the top 20 ... products" table: US, Rest of world and
  Total for the current period only (no prior-year US or rest-of-world values).
Calendar-year company, USD millions. Rest of world is recorded as `ExUS`.

**2015 has worldwide figures only.** Q1 2015's own report gives no figure (it says only that
initial sales were booked in the US and Japan); Q1 2015 (22) is the prior-year column of the
Q1 2016 report. Q2 2015 (30) is printed only in the text of the Q2 2015 report ("Cosentyx
(USD 30 million), launched in February 2015"); the I&D table that quarter folds Cosentyx into
"Other". Q3 2015 (88) and Q4 2015 (121) are table rows. No US / rest-of-world split exists
for any 2015 quarter in the 2015 or 2016 interim reports or the 2015 Form 20-F, so the eight
2015 US and ExUS rows are blank.

**Pre-US quarter.** Japan approved Cosentyx in December 2014 and the EU in January 2015,
slightly before the US (2015-01-21). Novartis prints Q4 2014 Cosentyx sales as 0 (prior-year
column of the Q4 2015 report), so there is no ex-US sales quarter before the US launch
quarter. A single 2014Q4 World row with value 0 records this check.

**Restatement checks.** Each quarter 2016Q1 to 2019Q4 (worldwide) was compared with the
prior-year column of the following year's report (through the Q4 2020 report): no
differences. Some prior-year columns are labelled "restated" for franchise regrouping; the
Cosentyx figures did not change.

## Full-year checks

Sum of the four recorded quarters against the full-year figure printed in the Q4 release
(Pfizer: Twelve Months tables; Novartis: Full year top-20 table, or the I&D table for 2015).
Differences are rounding.

**Xeljanz** (Pfizer Q4 releases of 2014-01-28, 2015-01-27, 2016-02-02, 2017-01-31)

| Year | Region | Sum of quarters | Printed full year | Difference |
|---|---|---|---|---|
| 2013 | World | 114 | 114 | 0 |
| 2013 | US | 112 | 112 | 0 |
| 2013 | ExUS | 2 | 2 | 0 |
| 2013 | Developed Europe / Developed RoW / Emerging Markets | 0 / 1 / 1 | dash / 1 / 1 | 0 / 0 / 0 |
| 2014 | World | 309 | 308 | +1 |
| 2014 | US | 289 | 289 | 0 |
| 2014 | ExUS | 20 | 20 | 0 |
| 2014 | Developed Europe / Developed RoW / Emerging Markets | 6 / 8 / 6 | 6 / 7 / 6 | 0 / +1 / 0 |
| 2015 | World | 523 | 523 | 0 |
| 2015 | US | 471 | 470 | +1 |
| 2015 | ExUS | 53 | 53 | 0 |
| 2015 | Developed Europe / Developed RoW / Emerging Markets | 12 / 19 / 22 | 12 / 20 / 22 | 0 / -1 / 0 |
| 2016 | World | 927 | 927 | 0 |
| 2016 | US | 805 | 805 | 0 |
| 2016 | ExUS | 122 | 122 | 0 |
| 2016 | Developed Europe / Developed RoW / Emerging Markets | 20 / 59 / 43 | 19 / 60 / 43 | +1 / -1 / 0 |

2012 is a part year inside the window (Q4 only): Q4 2012 = 6 and full-year 2012 printed in
the Q4 2013 release = 6 (US 6, International dash). 2017 is part of the window (Q1 to Q3)
and was not checked.

**Cibinqo** (Q4 releases of 2024-01-30, 2025-02-04, 2026-02-03)

| Year | Region | Sum of quarters | Printed full year | Difference |
|---|---|---|---|---|
| 2022 | World | 27 | 27 | 0 |
| 2022 | US | 13 | 11 | +2 |
| 2022 | ExUS | 16 | 16 | 0 |
| 2023 | World | 128 | 128 | 0 |
| 2023 | US | 46 | 46 | 0 |
| 2023 | ExUS | 81 | 81 | 0 |
| 2024 | World | 216 | 215 | +1 |
| 2024 | US | 90 | 90 | 0 |
| 2024 | ExUS | 126 | 126 | 0 |
| 2025 | World | 284 | 284 | 0 |
| 2025 | US | 115 | 115 | 0 |
| 2025 | ExUS | 169 | 169 | 0 |

The 2022 US difference of +2 comes from rounding very small quarters drawn from different
documents (Q1 3 from the recast PDF, Q2 1, Q3 3, Q4 6; Pfizer also prints six-month 2022 US
as 3 and nine-month as 6). The 2022 full year is the prior-year column of the Q4 2023
release. Regional rows exist for only three quarters of 2022 and 2023, so no regional
full-year check is possible. 2026 is a part year (Q1 to Q3).

**Cosentyx** (Novartis Q4 interim reports of 2016-01-27, 2017-01-25, 2018-01-24, 2019-01-30, 2020-01-29)

| Year | Region | Sum of quarters | Printed full year | Difference |
|---|---|---|---|---|
| 2015 | World | 261 | 261 | 0 |
| 2016 | World / US / ExUS | 1128 / 765 / 363 | 1128 / 765 / 363 | 0 / 0 / 0 |
| 2017 | World / US / ExUS | 2071 / 1275 / 796 | 2071 / 1275 / 796 | 0 / 0 / 0 |
| 2018 | World / US / ExUS | 2837 / 1674 / 1163 | 2837 / 1674 / 1163 | 0 / 0 / 0 |
| 2019 | World / US / ExUS | 3551 / 2220 / 1331 | 3551 / 2220 / 1331 | 0 / 0 / 0 |

## Documents relied on

Pfizer (EDGAR CIK 78003; read from the copies in the Biotech Vault `PFE - Pfizer` folder, with
each row's `source_url` taken from that folder's manifest; two were re-fetched from EDGAR and
matched):
- Earnings releases (8-K Exhibit 99 / 99.1), Q4 2012 to Q3 2018 and Q4 2021 to Q3 2026.
- Forms 10-Q and 10-K 2022 to 2026 (product revenue tables, fiscal year-end wording, Arena
  acquisition date).
- Recasted 2023 Product Revenue Tables (2024-04-23) and Recasted 2025 and 2024 Product
  Revenue Tables (2026-04-20), investors.pfizer.com (s206.q4cdn.com); the 2023 PDF was
  re-fetched from its public URL and is identical to the local copy.
- Q2 and Q3 2026 Historical Product Revenues workbooks (checked for Velsipity only).

Novartis (EDGAR CIK 1114448, found in company_tickers.json): 6-K Exhibits 99.1 and 99.2 for
Q3 2014 to Q4 2020 (accessions 0001370368-...), and the 2015 Form 20-F.

FDA: Drugs@FDA pages for NDA 203214, NDA 208246, NDA 216956, NDA 213871, BLA 125504 and
BLA 761349; approval letters and current labels as cited in `pfizer_novartis_launches.csv`.
