# smallcaps: collection notes

Group `smallcaps` (Vyvgart, Opzelura, Lupkynis, Zoryve, Vtama, Nemluvio). Collected 2026-11-19 under `docs/collection-spec.md`. Every value in `smallcaps_sales.csv` was read from the document named in its row. No figure is estimated, derived or filled from memory; every row has `method` = `printed` (or blank for the one gap).

## Windows and gaps

| Drug | First quarter with US sales (Q1) | Quarter 20 | Latest reported | Window collected | Quarters | Found | Missing |
|---|---|---|---|---|---|---|---|
| Vyvgart | 2022Q1 | 2026Q4 | 2026Q3 | 2022Q1 to 2026Q3 | 19 | 19 | none |
| Opzelura | 2021Q4 | 2026Q3 | 2026Q3 | 2021Q4 to 2026Q3 | 20 | 20 | none |
| Lupkynis | 2021Q1 | 2025Q4 | not needed (quarter 20 already reported) | 2021Q1 to 2025Q4 | 20 | 20 | none |
| Zoryve | 2022Q3 | 2027Q2 | 2026Q3 | 2022Q3 to 2026Q3 | 17 | 17 | none |
| Vtama | 2022Q2 | 2027Q1 | 2026Q3 | 2022Q2 to 2026Q3 | 18 | 18 | none |
| Nemluvio | 2024Q3 | 2029Q2 | 2026Q3 | 2024Q3 to 2026Q3 | 9 | 8 | 2024Q3 |

- In every case the first quarter with any sales anywhere was also the first quarter with US sales.
- **Nemluvio 2024Q3 is missing.** Galderma never printed a Q3 2024 Nemluvio figure; the Q3 2024 trading update only says first sales were recorded after the mid-August US launch. The FY2024 release gives 23 (USD millions, all US) for 2024 and the FY2025 release gives Q4 2024 as 21. The 2024 year row (23) is in the sales file; Q3 2024 is left blank, not derived from two rounded numbers.
- Lupkynis reached quarter 20 at 2025Q4, so 2026 quarters were not collected (the Q1 2026 release was opened only to check the Q1 2025 comparative).
- Vyvgart quarter 20 (2026Q4) is not yet reported; Zoryve, Vtama and Nemluvio are still inside their first 20 quarters.

## How regions are recorded

- An unlabelled company total (for example argenx "Product net sales", Aurinia "Net product sales") is recorded as `World`. Where the company says the sales were all in the US, the row note starts with "All US:". The same number is never copied into a `US` row; the merge step can decide.
- `US`, `ExUS` and `Other:` rows appear only where the company printed that line: argenx half-year and full-year regional tables, Incyte text bullets for some quarters, and Organon's U.S. / Int'l / Total columns.
- Units differ by row: argenx thousands to 2025 and millions from 2026; Incyte, Aurinia, Arcutis and Roivant thousands; Incyte regional text figures, Organon and Galderma millions. Check `unit` before adding rows.

## Company reporting quirks

### Vyvgart (argenx)
- argenx files 6-Ks (foreign private issuer, IFRS). The only product line is "Product net sales", which combines VYVGART (IV) and VYVGART Hytrulo (SC, US approval 2023-06-20) across all countries. The releases from Q3 2023 say the figure includes both products. There is no split by product or by quarter and region.
- Regional splits are printed only for six-month periods (interim report segment note) and full years (20-F). They are recorded as `period_type` `half` (calendar_quarter = 2022Q2, 2023Q2, 2024Q2, 2025Q2, 2026Q2) and `year` (calendar_quarter = 2022Q4 to 2025Q4) rows. The February full-year releases have no regional table, so the 20-F is the first report of full-year splits.
- Region labels change over time: Other* (2022) became EMEA, then Rest of the World; H1 2024 was printed as North America, later restated as United States 754,542 and Rest of the World 67,066; FY2022 Europe 5,678 plus Other 1,619 was later shown as EMEA 7,297; H1 2025 Netherlands 1,588 was later folded into Rest of the World. All first-reported values are kept, and the restatements are in row notes.
- Units switch from USD thousands to USD millions with the 2026 releases.
- Zai Lab (Greater China partner) payments are collaboration revenue or other income, not product net sales. China product sales appear in the regional tables.
- Every prior-year comparative checked in later releases matched the first-reported quarter.

### Opzelura (Incyte)
- Source line: Revenue Details table, "Net product revenues" block (renamed "Net sales" from 2026), row Opzelura. It is a worldwide figure. Before the European Commission vitiligo approval in April 2023, Opzelura was approved only in the US, so 2021Q4 to 2023Q1 are noted "All US".
- Incyte gives regional figures only in release text, rounded to $ millions and not every quarter: Europe 6 (2024Q1) and 11 (2024Q2); US 119 and ex-US 20 (2024Q3); ex-US 24 (2024Q4; ex-US 61 for full-year 2024); US 95 and ex-US 23 (2025Q1); US 132 and ex-US 32 (2025Q2). No split is printed for 2023Q2 to 2023Q4 or from 2025Q3 onward. Ex-US check for 2024: 6 + 11 + 20 + 24 = 61 against the printed full-year ex-US 61, though Q1 and Q2 are labelled Europe, not ex-US.
- **2026Q2 (449,736) is inflated by a one-time, non-cash benefit of $246 million**: reversal of Medicaid rebate accruals built up through March 31, 2026, after Incyte's agreement with CMS on the Medicaid line-extension dispute. The release says Opzelura net sales were $204 million without it. The Q3 2026 table repeats the point in footnote 3 on the nine-month figure (847,631, including $246.0 million). Earlier quarters from 2023 were reduced by those accruals (Incyte 10-Q Q3 2023 describes the line-extension accrual), so a launch curve should flag 2026Q2 rather than treat it as demand.
- All comparatives matched as first reported.

### Lupkynis (Aurinia)
- Label "Product revenue, net" to Q3 2024, then "Net product sales" from Q4 2024 (same line).
- Aurinia sells LUPKYNIS in the US to two specialty pharmacies and a specialty distributor. From the August 2022 commercial supply agreement it also sells LUPKYNIS inventory (including semi-finished product) to Otsuka, its partner for Europe and Japan, and these supply sales are in the same product sales line. The split is not printed, so from 2022Q3 the line is "mostly US", not "all US". The Q2 2024 release names such sales.
- Otsuka royalties, milestones and manufacturing services are in "License, collaboration and royalty revenue" and are not recorded. The 10-K FY2024 geographic table is for total revenue (US 210,095 / 157,958 / 102,460 for 2024 / 2023 / 2022; Japan 25,038 / 17,555 / 31,481), so it was not used as a US product sales figure.
- The Q1 2024 release was furnished as Exhibit 99.1 to an 8-K listing items 2.03 and 9.01. Preliminary revenue 8-Ks (January 2023, January 2024) were not used.

### Zoryve (Arcutis)
- One line, "Product revenue, net", covers every ZORYVE form (cream 0.3% from August 2022, foam 0.3% from January 2024, cream 0.15% from July 2024, cream 0.05% from October 2025) and Canada (from June 2023). Arcutis 10-K FY2025: product revenue outside the US was less than 10% of product revenue in 2023, 2024 and 2025. 2022Q3 to 2023Q1 are noted "All US". "Other revenue" (licence income) is excluded.
- Full-year product revenue by form (10-K FY2025): 2025 cream 0.3% 120,995, foam 181,892, cream 0.15% 68,274, cream 0.05% 911; 2024 cream 0.3% 85,082, foam 71,539, cream 0.15% 9,921; 2023 cream 0.3% 29,186. These are not in the sales file (not quarterly; no separate drug names).
- The Q1 2026 release was furnished under an 8-K listing item 9.01 only. Preliminary revenue 8-Ks (October 2023, January 2025) were not used.

### Vtama (Roivant/Dermavant, then Organon)
- Roivant's fiscal year ends March 31 (FY2022 = April 2022 to March 2023). `company_period` keeps Roivant's label; `calendar_quarter` is the calendar quarter.
- 2022Q2 (141): the 10-Q for the June 2022 quarter said product revenue had not been significant and printed no figure. The 141 is from the prior-year column of the June 2023 quarter release.
- 2022Q3 and 2022Q4 come from the 10-Q MD&A line "VTAMA revenues, net". The Q3 release gave only "$5.0 million" in text.
- From the September 2024 quarter Dermavant is a discontinued operation, so 2024Q3 and 2024Q4 come from the 10-Q discontinued-operations note. 2024Q4 (2,296) covers only about October 1 to 28, 2024.
- **Ownership change**: Organon's acquisition of Dermavant closed on 2024-10-28. Organon reports Vtama from that date in Table 2 "Sales by top products" (U.S. / Int'l / Total, $ millions). 2024Q4 therefore has rows from both reporters: Roivant 2,296 (thousands, Oct 1 to 28) and Organon 12 (millions, Oct 28 to Dec 31). Organon's Q4 2024 figures (U.S. 10 + Int'l 1 = 11, against a Total of 12) do not foot; Organon says totals may not foot due to rounding.
- Organon has an Int'l Vtama line from Q4 2024, recorded as `ExUS`. Roivant's figures are all US.
- Organon issued no earnings release for Q2 or Q3 2026. Its 8-Ks of 2026-07-31 and 2026-10-30 furnish supplemental measures in lieu of a quarterly earnings release, so those quarters come from the 10-Q "Product and Geographic Information" table. Six months 2026: 57 / 3 / 60; nine months 2026: 95 / 7 / 102 (U.S. / Int'l / Total). The quarters match.
- All Roivant and Organon comparatives matched as first reported.

### Nemluvio (Galderma)
- Galderma is listed in Switzerland and does not file with the SEC. All figures are from news releases on investors.galderma.com, read as HTML pages (the site blocks scripted downloads, so the PDF versions were not used). Galderma reports in USD millions, rounded.
- Galderma started printing quarterly Nemluvio figures (row "of which Nemluvio" under Therapeutic Dermatology in the appendix net sales tables) only from Q4 2025. Earlier quarters were first printed as prior-year comparatives one year later. First-reported cumulative figures were: FY2024 23 (all US); Q1 2025 none; H1 2025 131; nine months 2025 263 ("predominantly from the U.S."). The comparatives give Q1 39, Q2 93, Q3 132, Q4 188 = 452 for 2025, matching the FY2025 total. Q1 + Q2 2025 = 132 against the first-reported H1 131, and nine months = 264 against 263: rounding.
- Later figures: H1 2026 433 (185 + 248), nine months 2026 735 (+ 302). Galderma says the vast majority of 2025 sales were in the US, roughly evenly split between prurigo nodularis and atopic dermatitis; no US figure is printed after 2024.

## Full-year checks (sum of recorded quarters against printed total, World unless stated)

| Drug | Reporter | Period | Region | Quarters summed | Sum | Printed | Difference | Unit | Printed total from |
|---|---|---|---|---|---|---|---|---|---|
| Vyvgart | argenx | FY2022 | World | 2022Q1-2022Q4 (4 qtrs) | 400,721 | 400,720 | +1 | thousands | FY2022 release (6-K 2023-03-02) and 20-F |
| Vyvgart | argenx | FY2023 | World | 2023Q1-2023Q4 (4 qtrs) | 1,190,783 | 1,190,783 | +0 | thousands | FY2023 release (6-K 2024-02-29) and 20-F |
| Vyvgart | argenx | FY2024 | World | 2024Q1-2024Q4 (4 qtrs) | 2,185,883 | 2,185,883 | +0 | thousands | FY2024 release (6-K 2025-02-27) and 20-F |
| Vyvgart | argenx | FY2025 | World | 2025Q1-2025Q4 (4 qtrs) | 4,151,316 | 4,151,316 | +0 | thousands | FY2025 release (6-K 2026-02-26) and 20-F |
| Vyvgart | argenx | H1 2022 | World | 2022Q1-2022Q2 (2 qtrs) | 95,996 | 95,996 | +0 | thousands | H1 2022 interim report total |
| Vyvgart | argenx | H1 2023 | World | 2023Q1-2023Q2 (2 qtrs) | 487,335 | 487,335 | +0 | thousands | H1 2023 interim report total |
| Vyvgart | argenx | H1 2024 | World | 2024Q1-2024Q2 (2 qtrs) | 875,918 | 875,918 | +0 | thousands | H1 2024 interim report total |
| Vyvgart | argenx | H1 2025 | World | 2025Q1-2025Q2 (2 qtrs) | 1,738,644 | 1,738,644 | +0 | thousands | H1 2025 interim report total |
| Vyvgart | argenx | H1 2026 | World | 2026Q1-2026Q2 (2 qtrs) | 2,814 | 2,813 | +1 | millions | H1 2026 interim report total |
| Opzelura | Incyte | FY2021 | World | 2021Q4-2021Q4 (1 qtrs) | 4,668 | 4,668 | +0 | thousands | Q4 2021 release, year column (launched Oct 2021) |
| Opzelura | Incyte | FY2022 | World | 2022Q1-2022Q4 (4 qtrs) | 128,735 | 128,735 | +0 | thousands | Q4 2022 release, year column |
| Opzelura | Incyte | FY2023 | World | 2023Q1-2023Q4 (4 qtrs) | 337,864 | 337,864 | +0 | thousands | Q4 2023 release, year column |
| Opzelura | Incyte | FY2024 | World | 2024Q1-2024Q4 (4 qtrs) | 508,293 | 508,293 | +0 | thousands | Q4 2024 release, year column |
| Opzelura | Incyte | FY2025 | World | 2025Q1-2025Q4 (4 qtrs) | 678,455 | 678,455 | +0 | thousands | Q4 2025 release, year column |
| Lupkynis | Aurinia | FY2021 | World | 2021Q1-2021Q4 (4 qtrs) | 45,488 | 45,488 | +0 | thousands | Q4 2021 release, year column |
| Lupkynis | Aurinia | FY2022 | World | 2022Q1-2022Q4 (4 qtrs) | 103,468 | 103,468 | +0 | thousands | Q4 2022 release, year column |
| Lupkynis | Aurinia | FY2023 | World | 2023Q1-2023Q4 (4 qtrs) | 158,533 | 158,533 | +0 | thousands | Q4 2023 release, year column |
| Lupkynis | Aurinia | FY2024 | World | 2024Q1-2024Q4 (4 qtrs) | 216,186 | 216,186 | +0 | thousands | Q4 2024 release, year column |
| Lupkynis | Aurinia | FY2025 | World | 2025Q1-2025Q4 (4 qtrs) | 271,345 | 271,345 | +0 | thousands | Q4 2025 release, year column |
| Zoryve | Arcutis | FY2022 | World | 2022Q3-2022Q4 (2 qtrs) | 3,686 | 3,686 | +0 | thousands | Q4 2022 release, year column (sales from Q3 2022) |
| Zoryve | Arcutis | FY2023 | World | 2023Q1-2023Q4 (4 qtrs) | 29,186 | 29,186 | +0 | thousands | Q4 2023 release, year column |
| Zoryve | Arcutis | FY2024 | World | 2024Q1-2024Q4 (4 qtrs) | 166,542 | 166,542 | +0 | thousands | Q4 2024 release, year column |
| Zoryve | Arcutis | FY2025 | World | 2025Q1-2025Q4 (4 qtrs) | 372,072 | 372,072 | +0 | thousands | Q4 2025 release, year column |
| Vtama | Roivant (Dermavant) | FY ended 2023-03-31 | World | 2022Q2-2023Q1 (4 qtrs) | 28,011 | 28,011 | +0 | thousands | Roivant FY2022 Q4 release, year column |
| Vtama | Roivant (Dermavant) | FY ended 2024-03-31 | World | 2023Q2-2024Q1 (4 qtrs) | 75,057 | 75,057 | +0 | thousands | Roivant FY2023 Q4 release, year column |
| Vtama | Roivant (Dermavant) | Nine months ended 2024-12-31 (to 2024-10-28) | World | 2024Q2-2024Q4 (3 qtrs) | 41,599 | 41,599 | +0 | thousands | Roivant 10-Q Dec 2024, discontinued operations note, nine-month column |
| Vtama | Organon | FY2024 (from 2024-10-28) | US | 2024Q4-2024Q4 (1 qtrs) | 10 | 10 | +0 | millions | Organon Q4 2024 release, year columns |
| Vtama | Organon | FY2024 (from 2024-10-28) | ExUS | 2024Q4-2024Q4 (1 qtrs) | 1 | 1 | +0 | millions | Organon Q4 2024 release, year columns |
| Vtama | Organon | FY2024 (from 2024-10-28) | World | 2024Q4-2024Q4 (1 qtrs) | 12 | 12 | +0 | millions | Organon Q4 2024 release, year columns |
| Vtama | Organon | FY2025 | US | 2025Q1-2025Q4 (4 qtrs) | 111 | 111 | +0 | millions | Organon Q4 2025 release, year columns |
| Vtama | Organon | FY2025 | ExUS | 2025Q1-2025Q4 (4 qtrs) | 17 | 17 | +0 | millions | Organon Q4 2025 release, year columns |
| Vtama | Organon | FY2025 | World | 2025Q1-2025Q4 (4 qtrs) | 128 | 128 | +0 | millions | Organon Q4 2025 release, year columns |
| Nemluvio | Galderma | FY2024 | World | 2024Q3-2024Q4 (2 qtrs) (missing: 2024Q3) | 21 | 23 | -2 | millions | Galderma FY2024 release text |
| Nemluvio | Galderma | FY2025 | World | 2025Q1-2025Q4 (4 qtrs) | 452 | 452 | +0 | millions | Galderma FY2025 release |

Comments on non-zero differences:
- Vyvgart FY2022 World: 400,721 against 400,720 (+1). Rounding in argenx's published quarters.
- Vyvgart H1 2026 World: 2,814 against 2,813 (+1). Rounding (2026 figures are in millions).
- Nemluvio FY2024 World: 21 against 23 (-2). Q3 2024 is missing (not printed); 23 - 21 implies about 2, which is not recorded.
- argenx regional (US, Japan, and so on) full-year figures cannot be checked against quarters, because no quarterly regional figures are printed.
- Vtama has no printed calendar-year total: Roivant reports on an April-March year and Organon only from 2024-10-28.

## Launch facts

- Approval dates come from Drugs@FDA (openFDA drugsfda records, with submission status dates) and were checked against the FDA approval letters on accessdata.fda.gov. Mechanism, route and dosing come from the current FDA labels. Letter URLs are in `smallcaps_launches.csv`.
- None of the six drugs has an ulcerative colitis or Crohn's disease indication, so those columns are blank.
- Only Vtama changed reporting company (Roivant/Dermavant to Organon, closed 2024-10-28).

## Documents relied on

Sales figures (one line per document, by company and date):

- 2022-11-08 | Arcutis | Arcutis Q3 2022 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1787306/000178730622000070/pressreleaseex991q32022.htm
- 2023-02-28 | Arcutis | Arcutis Q4 2022 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1787306/000178730623000022/pressreleaseex991q42022.htm
- 2023-05-09 | Arcutis | Arcutis Q1 2023 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1787306/000178730623000042/pressreleaseex991q12023.htm
- 2023-08-08 | Arcutis | Arcutis Q2 2023 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1787306/000178730623000076/pressreleaseex991q22023.htm
- 2023-11-03 | Arcutis | Arcutis Q3 2023 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1787306/000178730623000122/pressreleaseex991q32023.htm
- 2024-02-27 | Arcutis | Arcutis Q4 2023 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1787306/000178730624000029/pressreleaseex991q42023.htm
- 2024-05-14 | Arcutis | Arcutis Q1 2024 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1787306/000178730624000078/pressreleaseex991q12024.htm
- 2024-08-14 | Arcutis | Arcutis Q2 2024 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1787306/000178730624000122/pressreleaseex991q22024.htm
- 2024-11-06 | Arcutis | Arcutis Q3 2024 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1787306/000178730624000151/pressreleaseex991q32024.htm
- 2025-02-25 | Arcutis | Arcutis Q4 2024 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1787306/000178730625000028/pressreleaseex991q42024.htm
- 2025-05-06 | Arcutis | Arcutis Q1 2025 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1787306/000178730625000091/pressreleaseex991q12025.htm
- 2025-08-06 | Arcutis | Arcutis Q2 2025 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1787306/000178730625000122/pressreleaseex991q22025.htm
- 2025-10-28 | Arcutis | Arcutis Q3 2025 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1787306/000178730625000142/pressreleaseex991q32025.htm
- 2026-02-25 | Arcutis | Arcutis Q4 2025 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1787306/000178730626000017/pressreleaseex991q42025.htm
- 2026-05-06 | Arcutis | Arcutis Q1 2026 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1787306/000178730626000039/pressreleaseex991q12026.htm
- 2026-08-05 | Arcutis | Arcutis Q2 2026 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1787306/000178730626000049/pressreleaseex991q22026.htm
- 2026-11-04 | Arcutis | Arcutis Q3 2026 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1787306/000178730626000056/pressreleaseex991q32026.htm
- 2021-05-06 | Aurinia | Aurinia Q1 2021 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000162828021009298/exhibit991_q12021pressrele.htm
- 2021-08-05 | Aurinia | Aurinia Q2 2021 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000162828021015854/exhibit991_q22021pressrele.htm
- 2021-11-03 | Aurinia | Aurinia Q3 2021 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000162828021021239/exhibit991_q32021pressrele.htm
- 2022-02-28 | Aurinia | Aurinia Q4 2021 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000162828022004080/exhibit991_q42021pressrele.htm
- 2022-05-10 | Aurinia | Aurinia Q1 2022 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000162828022013437/exhibit991_q12022pressrele.htm
- 2022-08-04 | Aurinia | Aurinia Q2 2022 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000162828022020811/exhibit991_q22022pressrele.htm
- 2022-11-03 | Aurinia | Aurinia Q3 2022 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000162828022027930/exhibit991_q32022pressrele.htm
- 2023-02-28 | Aurinia | Aurinia Q4 2022 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000162828023005333/exhibit991_q42022pressrele.htm
- 2023-05-04 | Aurinia | Aurinia Q1 2023 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000160062023000010/exhibit991_q12023pressrele.htm
- 2023-08-03 | Aurinia | Aurinia Q2 2023 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000160062023000028/exhibit991_q22023pressrele.htm
- 2023-11-02 | Aurinia | Aurinia Q3 2023 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000160062023000043/exhibit991_q32023pressrele.htm
- 2024-02-15 | Aurinia | Aurinia Q4 2023 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000160062024000010/exhibit991_q42023pressrele.htm
- 2024-05-02 | Aurinia | Aurinia Q1 2024 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000160062024000049/exhibit991_q12024pressrele.htm
- 2024-08-01 | Aurinia | Aurinia Q2 2024 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000160062024000089/exhibit991_q22024pressrele.htm
- 2024-11-07 | Aurinia | Aurinia Q3 2024 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000160062024000106/exhibit991_q32024earningsr.htm
- 2025-02-27 | Aurinia | Aurinia Q4 2024 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000160062025000009/exhibit991_q42024pressrele.htm
- 2025-05-12 | Aurinia | Aurinia Q1 2025 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000160062025000047/exhibit991_q12025earningsr.htm
- 2025-07-31 | Aurinia | Aurinia Q2 2025 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000160062025000090/exhibit991_q22025earningsr.htm
- 2025-11-04 | Aurinia | Aurinia Q3 2025 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000160062025000108/exhibit991_q32025earningsr.htm
- 2026-02-26 | Aurinia | Aurinia Q4 2025 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1600620/000160062026000015/exhibit991_q42025earningsr.htm
- 2024-10-24 | Galderma | Galderma Q3 2024 trading update press release (nine months 2024) | https://investors.galderma.com/news-releases/news-release-details/galderma-delivers-record-net-sales-3259-b-usd-first-nine-months
- 2025-03-06 | Galderma | Galderma FY 2024 results press release | https://investors.galderma.com/news-releases/news-release-details/galderma-delivers-2024-record-net-sales-4410-billion-usd-93-year
- 2026-03-05 | Galderma | Galderma FY 2025 results press release | https://investors.galderma.com/news-releases/news-release-details/galderma-delivers-record-2025-results-net-sales-5207-billion-usd
- 2026-04-23 | Galderma | Galderma Q1 2026 trading update press release | https://investors.galderma.com/news-releases/news-release-details/galderma-reports-strong-start-year-delivering-first-quarter-2026
- 2026-07-23 | Galderma | Galderma H1 2026 results press release | https://investors.galderma.com/news-releases/news-release-details/galderma-reports-record-first-half-2026-net-sales-3134-billion
- 2026-10-22 | Galderma | Galderma Q3 2026 trading update press release (nine months 2026) | https://investors.galderma.com/news-releases/news-release-details/galderma-delivers-net-sales-4765-b-usd-first-nine-months-251
- 2022-02-08 | Incyte | Incyte Q4 2021 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000155837022000883/incy-20220208xex99d1.htm
- 2022-05-03 | Incyte | Incyte Q1 2022 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000155837022006719/incy-20220503xex99d1.htm
- 2022-08-02 | Incyte | Incyte Q2 2022 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000155837022011546/incy-20220802xex99d1.htm
- 2022-11-01 | Incyte | Incyte Q3 2022 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000087916922000007/incy-q32022xexx991.htm
- 2023-02-07 | Incyte | Incyte Q4 2022 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000087916923000005/incy-q42022xexx991.htm
- 2023-05-02 | Incyte | Incyte Q1 2023 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000087916923000014/incy-q12023xexx991.htm
- 2023-08-01 | Incyte | Incyte Q2 2023 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000087916923000022/incy-q22023xexx991.htm
- 2023-10-31 | Incyte | Incyte Q3 2023 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000087916923000038/incy-q32023xexx991.htm
- 2024-02-13 | Incyte | Incyte Q4 2023 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000087916924000042/incy-q42023xexx991.htm
- 2024-04-30 | Incyte | Incyte Q1 2024 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000087916924000074/incy-q12024xexx991.htm
- 2024-07-30 | Incyte | Incyte Q2 2024 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000087916924000146/incy-q22024xexx991.htm
- 2024-10-29 | Incyte | Incyte Q3 2024 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000087916924000169/incy-q32024xexx991.htm
- 2025-02-10 | Incyte | Incyte Q4 2024 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000162828025004514/incy-q42024xexx991.htm
- 2025-04-29 | Incyte | Incyte Q1 2025 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000087916925000053/incy-q12025xexx991.htm
- 2025-07-29 | Incyte | Incyte Q2 2025 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000087916925000100/incy-q22025xexx991.htm
- 2025-10-28 | Incyte | Incyte Q3 2025 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000087916925000115/incy-q32025xexx991.htm
- 2026-02-10 | Incyte | Incyte Q4 2025 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000087916926000006/incy-q42025xexx991.htm
- 2026-04-28 | Incyte | Incyte Q1 2026 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000087916926000023/incy-q12026xexx991.htm
- 2026-07-28 | Incyte | Incyte Q2 2026 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000087916926000053/incy-q22026xexx991.htm
- 2026-10-29 | Incyte | Incyte Q3 2026 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/879169/000087916926000063/incy-q32026xexx991.htm
- 2025-02-13 | Organon | Organon Q4 2024 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1821825/000110465925012546/tm256470d1_ex99-1.htm
- 2025-05-01 | Organon | Organon Q1 2025 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1821825/000110465925043023/tm2513730d1_ex99-1.htm
- 2025-08-05 | Organon | Organon Q2 2025 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1821825/000110465925073929/tm2522571d1_ex99-1.htm
- 2025-11-10 | Organon | Organon Q3 2025 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1821825/000110465925108821/tm2530711d1_ex99-1.htm
- 2026-02-12 | Organon | Organon Q4 2025 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1821825/000110465926013888/tm266144d1_ex99-1.htm
- 2026-04-30 | Organon | Organon Q1 2026 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1821825/000110465926052165/tm2613165d1_ex99-1.htm
- 2026-07-31 | Organon | Organon 10-Q for the quarter ended June 30, 2026 | https://www.sec.gov/Archives/edgar/data/1821825/000162828026051230/ogn-20260630.htm
- 2026-10-30 | Organon | Organon 10-Q for the quarter ended September 30, 2026 | https://www.sec.gov/Archives/edgar/data/1821825/000182182526000004/ogn-20260930.htm
- 2022-11-14 | Roivant (Dermavant) | Roivant 10-Q for the quarter ended September 30, 2022 | https://www.sec.gov/Archives/edgar/data/1635088/000114036122041175/brhc10044005_10q.htm
- 2023-02-13 | Roivant (Dermavant) | Roivant 10-Q for the quarter ended December 31, 2022 | https://www.sec.gov/Archives/edgar/data/1635088/000114036123006180/brhc10047697_10q.htm
- 2023-06-28 | Roivant (Dermavant) | Roivant FY2022 Q4 and full-year earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1635088/000114036123031794/brhc20054989_ex99-1.htm
- 2023-08-14 | Roivant (Dermavant) | Roivant FY2023 Q1 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1635088/000114036123039405/brhc20057388_ex99-1.htm
- 2023-11-13 | Roivant (Dermavant) | Roivant FY2023 Q2 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1635088/000114036123052718/ef20014462_99-1.htm
- 2024-02-13 | Roivant (Dermavant) | Roivant FY2023 Q3 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1635088/000114036124007259/ef20021494_ex99-1.htm
- 2024-05-30 | Roivant (Dermavant) | Roivant FY2023 Q4 and full-year earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1635088/000114036124027986/ef20030255_ex99-1.htm
- 2024-08-08 | Roivant (Dermavant) | Roivant FY2024 Q1 earnings release (8-K Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1635088/000114036124036281/ef20033756_ex99-1.htm
- 2024-11-12 | Roivant (Dermavant) | Roivant 10-Q for the quarter ended September 30, 2024 | https://www.sec.gov/Archives/edgar/data/1635088/000114036124046019/ef20034554_10q.htm
- 2025-02-10 | Roivant (Dermavant) | Roivant 10-Q for the quarter ended December 31, 2024 | https://www.sec.gov/Archives/edgar/data/1635088/000114036125003661/ef20039028_10q.htm
- 2022-05-05 | argenx | argenx Q1 2022 results press release (Form 6-K, Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1697862/000110465922056161/tm2214548d1_ex99-1.htm
- 2022-07-28 | argenx | argenx H1/Q2 2022 results press release (Form 6-K, Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1697862/000155837022011211/argx-20220630xex99d1.htm
- 2022-07-28 | argenx | argenx H1 2022 interim financial report (Form 6-K, Exhibit 99.2) | https://www.sec.gov/Archives/edgar/data/1697862/000155837022011211/argx-20220630xex99d2.htm
- 2022-10-27 | argenx | argenx Q3 2022 results press release (Form 6-K, Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1697862/000110465922111775/tm2228911d1_ex99-1.htm
- 2023-03-02 | argenx | argenx FY/Q4 2022 results press release (Form 6-K, Exhibit 99.2) | https://www.sec.gov/Archives/edgar/data/1697862/000110465923027703/tm238287d1_ex99-2.htm
- 2023-03-16 | argenx | argenx 2022 annual report on Form 20-F | https://www.sec.gov/Archives/edgar/data/1697862/000155837023004027/argx-20221231x20f.htm
- 2023-05-05 | argenx | argenx Q1 2023 results press release (Form 6-K, Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1697862/000110465923056316/tm2314617d1_ex99-1.htm
- 2023-07-27 | argenx | argenx H1/Q2 2023 results press release (Form 6-K, Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1697862/000155837023012337/argx-20230630xex99d1.htm
- 2023-07-27 | argenx | argenx H1 2023 interim financial report (Form 6-K, Exhibit 99.2) | https://www.sec.gov/Archives/edgar/data/1697862/000155837023012337/argx-20230630xex99d2.htm
- 2023-10-31 | argenx | argenx Q3 2023 results press release (Form 6-K, Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1697862/000110465923112777/tm2329468d1_ex99-1.htm
- 2024-02-29 | argenx | argenx FY/Q4 2023 results press release (Form 6-K, Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1697862/000110465924029353/tm247489d1_ex99-1.htm
- 2024-03-21 | argenx | argenx 2023 annual report on Form 20-F | https://www.sec.gov/Archives/edgar/data/1697862/000155837024003665/argx-20231231x20f.htm
- 2024-05-09 | argenx | argenx Q1 2024 results press release (Form 6-K, Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1697862/000110465924059094/tm2413809d1_ex99-1.htm
- 2024-07-25 | argenx | argenx H1/Q2 2024 results press release (Form 6-K, Exhibit 99.1) | https://www.sec.gov/Archives/edgar/data/1697862/000155837024010095/argx-20240630xex99d1.htm
- 2024-07-25 | argenx | argenx H1 2024 interim financial report (Form 6-K, Exhibit 99.2) | https://www.sec.gov/Archives/edgar/data/1697862/000155837024010095/argx-20240630xex99d2.htm
- 2024-10-31 | argenx | argenx Q3 2024 earnings press release (Form 6-K exhibit) | https://www.sec.gov/Archives/edgar/data/1697862/000169786224000012/a02earningspressreleaseq32.htm
- 2025-02-27 | argenx | argenx Q4/FY 2024 earnings press release (Form 6-K exhibit) | https://www.sec.gov/Archives/edgar/data/1697862/000169786225000006/a09earningspressreleaseq42.htm
- 2025-03-20 | argenx | argenx 2024 annual report on Form 20-F | https://www.sec.gov/Archives/edgar/data/1697862/000169786225000024/argx-20241231.htm
- 2025-05-08 | argenx | argenx Q1 2025 earnings press release (Form 6-K exhibit) | https://www.sec.gov/Archives/edgar/data/1697862/000169786225000028/a02earningspressreleaseq1.htm
- 2025-07-31 | argenx | argenx H1/Q2 2025 earnings press release (Form 6-K exhibit) | https://www.sec.gov/Archives/edgar/data/1697862/000169786225000042/a04earningspressreleasehy.htm
- 2025-07-31 | argenx | argenx H1 2025 interim financial report (Form 6-K exhibit) | https://www.sec.gov/Archives/edgar/data/1697862/000169786225000042/argx-20250630_d2.htm
- 2025-10-30 | argenx | argenx Q3 2025 earnings press release (Form 6-K exhibit) | https://www.sec.gov/Archives/edgar/data/1697862/000169786225000059/a02earningspressreleaseq3.htm
- 2026-02-26 | argenx | argenx Q4/FY 2025 earnings press release (Form 6-K exhibit) | https://www.sec.gov/Archives/edgar/data/1697862/000169786226000010/a09earningspressreleaseq4.htm
- 2026-03-19 | argenx | argenx 2025 annual report on Form 20-F | https://www.sec.gov/Archives/edgar/data/1697862/000169786226000032/argx-20251231.htm
- 2026-05-07 | argenx | argenx Q1 2026 earnings press release (Form 6-K exhibit) | https://www.sec.gov/Archives/edgar/data/1697862/000162828026031739/a02earningspressreleaseq1.htm
- 2026-07-23 | argenx | argenx H1/Q2 2026 earnings press release (Form 6-K exhibit) | https://www.sec.gov/Archives/edgar/data/1697862/000169786226000033/a04earningspressreleasehy.htm
- 2026-07-23 | argenx | argenx H1 2026 interim financial report (Form 6-K exhibit) | https://www.sec.gov/Archives/edgar/data/1697862/000169786226000033/argx-20260630_d2.htm
- 2026-10-22 | argenx | argenx Q3 2026 earnings press release (Form 6-K exhibit) | https://www.sec.gov/Archives/edgar/data/1697862/000169786226000034/a02earningspressreleaseq3.htm

Other documents used for notes and checks:

- 2026-02-25 | Arcutis | Arcutis 10-K for 2025 (launch timing, ex-US share under 10%, revenue by form) | https://www.sec.gov/Archives/edgar/data/1787306/000178730626000018/arqt-20251231.htm
- 2025-02-27 | Aurinia | Aurinia 10-K for 2024 (customers, Otsuka supply agreement, revenue by geography) | https://www.sec.gov/Archives/edgar/data/1600620/000160062025000011/auph-20241231.htm
- 2025-04-24 | Galderma | Galderma Q1 2025 trading update (no Nemluvio figure) | https://investors.galderma.com/news-releases/news-release-details/galderma-delivers-record-first-quarter-net-sales-1129-billion
- 2025-07-24 | Galderma | Galderma H1 2025 results (Nemluvio H1 2025 = 131) | https://investors.galderma.com/news-releases/news-release-details/galderma-delivers-record-first-half-2025-net-sales-2448-billion
- 2025-10-23 | Galderma | Galderma Q3 2025 trading update (Nemluvio nine months 2025 = 263) | https://investors.galderma.com/news-releases/news-release-details/galderma-delivers-record-net-sales-3737-billion-usd-first-nine
- 2023-10-31 | Incyte | Incyte 10-Q for the quarter ended September 30, 2023 (EC approval April 2023; Medicaid line-extension accrual) | https://www.sec.gov/Archives/edgar/data/879169/000087916923000041/incy-20230930.htm
- 2026-10-29 | Incyte | Incyte 10-Q for the quarter ended September 30, 2026 (no geographic split of Opzelura) | https://www.sec.gov/Archives/edgar/data/879169/000087916926000066/incy-20260930.htm
- 2026-07-31 | Organon | Organon 8-K of 2026-07-31 (supplemental measures in lieu of an earnings release) | https://www.sec.gov/Archives/edgar/data/1821825/000110465926089008/
- 2026-10-30 | Organon | Organon 8-K of 2026-10-30 (supplemental measures in lieu of an earnings release) | https://www.sec.gov/Archives/edgar/data/1821825/000110465926120423/
- 2022-08-15 | Roivant (Dermavant) | Roivant 10-Q for the quarter ended June 30, 2022 (VTAMA revenue not significant) | https://www.sec.gov/Archives/edgar/data/1635088/000119312522220561/d383218d10q.htm
- 2024-11-12 | Roivant (Dermavant) | Roivant FY2024 Q2 earnings release (Organon deal) | https://www.sec.gov/Archives/edgar/data/1635088/000114036124046015/ef20038392_ex99-1.htm
- 2022-03-03 | argenx | argenx FY2021 results press release (6-K): no product net sales line | https://www.sec.gov/Archives/edgar/data/1697862/000110465922029609/tm228207d1_ex99-1.htm
- Aurinia Q1 2026 earnings release (8-K Exhibit 99.1): opened only to check the Q1 2025 comparative (59,971 matched).
- FDA: openFDA drugsfda records for BLA 761195, BLA 761304, NDA 215309, NDA 213716, NDA 215985, NDA 217242, NDA 215272, BLA 761390, BLA 761391; the approval letters listed in the launches file; current FDA labels for each product.
- SEC company_tickers.json and data.sec.gov submissions JSON for CIKs: argenx 1697862, Incyte 879169, Aurinia 1600620, Arcutis 1787306, Roivant 1635088, Organon 1821825.
