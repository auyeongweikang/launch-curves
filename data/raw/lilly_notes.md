# Lilly group: collection notes

Drugs: Taltz (ixekizumab), Olumiant (baricitinib), Omvoh (mirikizumab), Ebglyss (lebrikizumab).
Reporting company for all four, throughout: Eli Lilly and Company (EDGAR CIK 59478). Calendar fiscal year, USD, millions.
Collected 2026-11-19. Every value was read in the cited Lilly document. The build script re-checked each value against the
converted text of that document (or the workbook cell as displayed by its number format) before writing.

Files: `lilly_sales.csv` (206 rows), `lilly_launches.csv` (4 rows), this file.

## Windows and coverage

| Drug | First quarter with any sales | First US quarter (Q1) | Window end | Quarters | Rows | Regions |
|---|---|---|---|---|---|---|
| Taltz | 2016Q2 | 2016Q2 | 2021Q1 (20th US quarter) | 20 | 57 | US, ExUS, World (gaps below) |
| Olumiant | 2017Q1 (Germany launch) | 2018Q2 | 2023Q1 (20th US quarter) | 25 | 65 | World only 2017Q1-2018Q1; US, ExUS, World from 2018Q2 |
| Omvoh | 2023Q1 (Japan) | 2023Q4 | 2026Q3 (latest reported; 12th US quarter) | 15 | 45 | US, ExUS, World |
| Ebglyss | 2023Q3 (first Lilly-printed Ebglyss revenue) | 2024Q3 | 2026Q3 (latest reported; 9th US quarter) | 13 | 39 | US, ExUS, World |

Lilly's columns map as: "U.S." -> `US`; "Outside U.S." / "Revenue outside the U.S." / workbook "Intl" -> `ExUS`; table total /
workbook "Total" -> `World`. No `Other:` regions are printed for these drugs.

One row is derived (`derived_fy_minus_9m`): Taltz 2017Q4 ExUS. All other rows are `printed`.

## Gaps

- **Taltz 2016Q2 and 2016Q3, US: blank rows (`not found:`).** The releases print worldwide Taltz only (19.3, 32.5). Searched: the
  Q2 and Q3 2016 releases, the Q2 2016 and Q3 2016 10-Qs, the Q2 and Q3 2017 10-Q comparatives, the 2016 10-K and the 2018 10-K.
  None prints a quarterly US split. The 2018 10-K prints only full-year 2016 (US 110.8, outside US 2.3), so 110.8 - 59.5 (Q4 US)
  = 51.3 is the Q2+Q3 US total, which cannot be split by quarter. The release says Taltz launched in the US in April 2016 and began
  launching in Europe in July 2016, so the Q2 2016 worldwide figure is very likely almost all US, but that is not printed.
- **Taltz 2016Q2-2016Q4, ExUS: no rows.** Not printed for any 2016 quarter; full-year 2016 outside US is 2.3 (2018 10-K). No nine-month
  2016 outside-US figure exists, so Q4 2016 cannot be derived. Q4 2016 has US 59.5 and World 61.3 printed.
- **Olumiant 2017Q1-2018Q1, US and ExUS: no rows.** Before the US approval (2018-05-31) Lilly printed only a worldwide Olumiant figure.
  All of it was outside the US (the 2019 10-K prints full-year 2017 US as "—"; first US revenue was June 2018), but the split is not
  printed, so only `World` is recorded. The merge step may treat these as ExUS = World.
- **Omvoh and Ebglyss: no gaps** in their windows.

## Reporting quirks a reader must know

### All drugs

- **Revenue definition.** Lilly's product lines are "revenue" = net product revenue plus collaboration and other revenue attributed
  to the product. For Taltz and Omvoh this is effectively net product sales. For Olumiant and Ebglyss see below.
- **Sources changed over time.**
  - 2016-2023: quarterly 8-K Exhibit 99.1 earnings releases. Worldwide figures come from the "Select(ed) Revenue Highlights" table;
    US and outside-US from the product paragraph ("U.S. revenue was $X million ... Revenue outside the U.S. was $Y million").
  - For Taltz, the Q2-Q3 2016 releases print worldwide only and the Q4 2016-Q3 2017 releases print worldwide and US only.
    Outside-US for 2017Q1-Q3 was taken from 10-Qs (see Taltz). Pre-US Olumiant (2017Q1-2018Q1) is printed worldwide only.
  - Omvoh and Ebglyss have no revenue row in any 2023-2025 release table, 10-Q or 10-K (Lilly mentions them only in narrative).
    The only Lilly document that prints them by quarter and region is the IR Financial Workbook ("Product Revenue Report", sheet
    "YYYY Revenue", columns US | Intl | Total per quarter), so Omvoh and Ebglyss come almost entirely from workbooks.
  - From Q1 2026 the releases again print worldwide Ebglyss and Omvoh rows. 2026 `World` values come from the releases;
    2026 `US`/`ExUS` from the same-quarter workbooks. The workbook totals equal the release figures (80, 102, 114; 145, 201, 202).
- **Precision change.** Through the Q3 2025 workbook, values are stored in dollars and displayed in millions to one decimal. From the
  Q4 2025 workbook and the 2026 releases, Lilly prints whole millions. The 2025Q4 and 2026 rows are therefore whole numbers, and US +
  ExUS can differ from World by 1 (for example Omvoh 2026Q2: 48 + 53 = 101 vs 102 printed).
- **Workbook dashes.** A workbook cell of 0 displays as a dash. These are recorded as `0` with the note "printed as a dash
  (cell value 0)" (Omvoh US 2023Q1-Q3; Ebglyss US 2023Q3-2024Q2).
- **Workbook links.** The investor.lilly.com workbook URLs (from the vault manifest) return HTTP 403 to scripted requests but open
  in a normal browser. The copies read were the ones already in the Biotech Vault (`Financial Reports`), matched by manifest URL.
- **Workbook source dates.** `source_date` for a workbook is the earnings date it was released with. Two manifest dates differ:
  the Q4 2022 workbook (manifest 2023-02-01; earnings 2023-02-02 used) and the Q3 2026 workbook (manifest 2026-10-27; earnings
  2026-10-29 used).
- **Q1 2018 release is image-based.** The Q1 2018 Exhibit 99.1 (filed 2018-04-24) is scanned page images. Taltz and Olumiant values
  were read from the page images (pages 9 and 12) and matched to the exhibit's embedded text layer.

### Taltz

- 2016Q2 is the first quarter with any revenue (Q1 2016 is printed as "—" in the Q1 2017 release).
- **2017Q1 ExUS (8.8)** is the prior-year comparative in the Q1 2018 10-Q (Note 13 Segment Information). The Q1 2017 release and
  Q1 2017 10-Q do not print it, so this is the first document that does.
- **2017Q2 ExUS (14.3) and 2017Q3 ExUS (20.0)** come from the same-quarter 10-Qs (MD&A product table).
- **2017Q4 ExUS (30.1) is derived:** 2017 10-K full year outside US 73.2 minus Q3 2017 10-Q nine months outside US 43.1. The
  Q1 2018 and Q4 2018 releases describe changes against Q4 2017 that imply 30.0, a rounding difference.
- 2018Q1-2021Q1: US, ExUS and World all from the quarterly releases.

### Olumiant

- **Licence:** Incyte holds the original rights; Lilly has a worldwide licence, records Olumiant as its own net product revenue and
  pays royalties to Incyte (in cost of sales). No change in reporting company.
- **Approved outside the US first.** EU approval and Germany launch Q1 2017; Japan Q3 2017; FDA approval 2018-05-31; US launch
  June 2018. The window starts at 2017Q1 (first sales anywhere).
- **2018Q2 US 1.7** is initial wholesaler stocking (release). US 1.7 + ExUS 42.9 = 44.6 vs World 44.7 printed (rounding).
- **COVID-19 sales (2021Q3-2023Q1).** From the Q3 2021 release, the Olumiant line carries a footnote ("Olumiant(d)", later
  "Olumiant®(c)"): revenue includes baricitinib sold under the FDA Emergency Use Authorization for hospitalized COVID-19 patients.
  US revenue jumps to 194.0 in 2021Q3, then falls. The COVID-19 indication was fully approved 2022-05-10. These quarters are not
  a normal launch curve and should be flagged in any chart.
- **2022Q4 ExUS (162.3)** comes from the Q4 2022 workbook "Intl" column. The Q4 2022 release prints worldwide (205.8) and US (43.5) only.
- 10-Q "Other Immunology" lines (US "—") for 2017-2019 were **not** used for Olumiant because they do not exactly match the
  Olumiant figures (for example 2017Q3 16.3 vs Olumiant 16.2; 2019Q1 82.2 vs 82.1).

### Omvoh

- Approved in Japan (Q1 2023) and the EU (Q2 2023) before the US. FDA issued a complete response letter in April 2023
  (manufacturing) and approved UC on 2023-10-26; Crohn's disease approved 2025-01-15.
- **2023Q1 (Intl 22.0)** was first printed as an Omvoh line in the Q2 2023 workbook. The Q1 2023 workbook showed it inside
  "Other Immunology" (U.S. 0, Intl 22, Total 22) with the footnote "Other – Immunology includes mirikizumab". The figure is
  recorded from the Q2 2023 workbook, the first document that prints it under the Omvoh name.
- US is a dash (0) in 2023Q1-Q3; first US revenue 2023Q4 (0.8).

### Ebglyss

- **Rights and collaboration accounting.** Lebrikizumab was licensed worldwide from Roche/Genentech (Roche receives royalties)
  and came to Lilly with the Dermira acquisition (February 2020). **Almirall holds the licence for Europe and sells Ebglyss there.**
  Lilly records Almirall's royalties and milestones as collaboration and other revenue inside its Ebglyss line. **Almirall's own
  European sales are not in these figures.** Lilly sells Ebglyss in the US, Japan and other markets outside Europe.
- **The ExUS column is mixed.** It combines Lilly's own sales outside the US (for example Japan) with Almirall royalties and milestones.
- **2023Q4 (Intl 67.6)** includes $65 million of milestones for the EU approval and launch (Q4 2023 release). It is not product
  sales; the next quarters fall back to 3-4 million.
- **2023Q3 (Intl 3.5)** is pre-approval. It was first printed as an Ebglyss line in the Q4 2023 workbook (which shows Q1 and Q2 2023
  as dashes). The Q3 2023 workbook had it inside "Other Immunology". It is recorded from the Q4 2023 workbook.
- **Earlier lebrikizumab amounts not collected.** The Q4 2022 workbook's "Other Immunology" line is footnoted "Other – Immunology
  includes Lebrikizumab". It shows 2022 values of Q1 Intl 4.5, Q2 Intl 4.0, Q3 Intl 3.6 and Q4 US 20.0 (full year US 20.0,
  Intl 12.1, total 32.1). These are a combined line, not an Ebglyss line, before any approval, so they were not recorded.
- First US revenue 2024Q3 (0.5), after FDA approval on 2024-09-13.
- One internal workbook inconsistency: in the Q4 2023 workbook, the 2023 full-year Ebglyss cell is 71,151,841 (displays 71.2), but
  the quarter cells sum to 71,115,376 (71.1).

## Full-year checks

Sum of the quarters recorded vs the printed full-year figure, per region where printed. "not printed" = no row for that quarter.

| Drug | Year | Region | Q1 | Q2 | Q3 | Q4 | Sum | Printed FY | Diff | FY source | Comment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Taltz | 2016 | World | not printed (no sales) | 19.3 | 32.5 | 61.3 | 113.1 | 113.1 | 0.0 | Q4 2016 release; 2017 10-K | |
| Taltz | 2016 | US | not printed | blank | blank | 59.5 | 59.5 | 110.8 | -51.3 | 2018 10-K segment table | Gap = missing Q2+Q3 US |
| Taltz | 2016 | ExUS | not printed | not printed | not printed | not printed | - | 2.3 | n/a | 2018 10-K segment table | No quarterly ExUS printed |
| Taltz | 2017 | World | 96.6 | 138.7 | 151.3 | 172.5 | 559.1 | 559.2 | -0.1 | Q4 2017 release; 2017 10-K | Rounding |
| Taltz | 2017 | US | 87.8 | 124.4 | 131.3 | 142.5 | 486.0 | 486.0 | 0.0 | 2017 10-K | |
| Taltz | 2017 | ExUS | 8.8 | 14.3 | 20.0 | 30.1 (derived) | 73.2 | 73.2 | 0.0 | 2017 10-K | Ties by construction (Q4 derived) |
| Taltz | 2018 | World | 146.5 | 220.1 | 263.9 | 307.0 | 937.5 | 937.5 | 0.0 | Q4 2018 release; 2018 10-K | |
| Taltz | 2018 | US | 111.2 | 173.6 | 210.6 | 243.4 | 738.8 | 738.7 | +0.1 | 2018 10-K | Rounding |
| Taltz | 2018 | ExUS | 35.3 | 46.5 | 53.3 | 63.6 | 198.7 | 198.7 | 0.0 | 2018 10-K | |
| Taltz | 2019 | World | 252.5 | 353.8 | 340.0 | 420.1 | 1366.4 | 1366.4 | 0.0 | 2019 10-K | |
| Taltz | 2019 | US | 180.8 | 268.1 | 250.6 | 317.2 | 1016.7 | 1016.8 | -0.1 | 2019 10-K | Rounding |
| Taltz | 2019 | ExUS | 71.7 | 85.7 | 89.4 | 102.8 | 349.6 | 349.6 | 0.0 | 2019 10-K | |
| Taltz | 2020 | World | 443.5 | 395.2 | 454.5 | 495.3 | 1788.5 | 1788.5 | 0.0 | 2020 10-K | |
| Taltz | 2020 | US | 327.5 | 289.2 | 326.2 | 345.7 | 1288.6 | 1288.5 | +0.1 | 2020 10-K | Rounding |
| Taltz | 2020 | ExUS | 116.0 | 106.0 | 128.3 | 149.7 | 500.0 | 500.0 | 0.0 | 2020 10-K | |
| Olumiant | 2017 | World | 1.9 | 4.8 | 16.2 | 23.0 | 45.9 | 45.9 | 0.0 | Q4 2017 release | 2019 10-K later prints 45.8 |
| Olumiant | 2018 | World | 32.2 | 44.7 | 55.6 | 70.1 | 202.6 | 202.5 | +0.1 | Q4 2018 release; 2019 10-K | Rounding |
| Olumiant | 2018 | US | not printed (pre-approval) | 1.7 | 0.8 | 4.2 | 6.7 | 6.7 | 0.0 | 2019 10-K disaggregation table | |
| Olumiant | 2018 | ExUS | not printed (World 32.2, all ex-US) | 42.9 | 54.8 | 65.9 | 163.6 | 195.9 | -32.3 | 2019 10-K disaggregation table | Gap = Q1 2018 (World only) |
| Olumiant | 2019 | World | 82.1 | 102.4 | 114.6 | 127.8 | 426.9 | 426.9 | 0.0 | 2019 10-K | |
| Olumiant | 2019 | US | 6.4 | 10.7 | 12.1 | 13.0 | 42.2 | 42.2 | 0.0 | 2019 10-K | |
| Olumiant | 2019 | ExUS | 75.7 | 91.7 | 102.5 | 114.9 | 384.8 | 384.7 | +0.1 | 2019 10-K | Rounding |
| Olumiant | 2020 | World | 139.7 | 145.0 | 162.0 | 192.2 | 638.9 | 638.9 | 0.0 | 2020 10-K | |
| Olumiant | 2020 | US | 11.3 | 13.2 | 14.5 | 24.8 | 63.8 | 63.8 | 0.0 | 2020 10-K | |
| Olumiant | 2020 | ExUS | 128.4 | 131.8 | 147.5 | 167.4 | 575.1 | 575.0 | +0.1 | 2020 10-K | Rounding |
| Olumiant | 2021 | World | 193.8 | 208.4 | 406.9 | 306.0 | 1115.1 | 1115.1 | 0.0 | 2021 10-K | |
| Olumiant | 2021 | US | 24.7 | 17.8 | 194.0 | 87.7 | 324.2 | 324.1 | +0.1 | 2021 10-K | Rounding |
| Olumiant | 2021 | ExUS | 169.1 | 190.6 | 212.9 | 218.3 | 790.9 | 791.0 | -0.1 | 2021 10-K | Rounding |
| Olumiant | 2022 | World | 255.6 | 186.2 | 182.9 | 205.8 | 830.5 | 830.5 | 0.0 | 2022 10-K; Q4 2022 workbook | |
| Olumiant | 2022 | US | 71.3 | 10.4 | 22.9 | 43.5 | 148.1 | 148.2 | -0.1 | 2022 10-K | Rounding |
| Olumiant | 2022 | ExUS | 184.3 | 175.8 | 160.0 | 162.3 | 682.4 | 682.3 | +0.1 | 2022 10-K | Rounding |
| Omvoh | 2023 | World | 22.0 | 5.7 | 7.8 | 8.6 | 44.1 | 44.1 | 0.0 | Q4 2023 workbook | |
| Omvoh | 2023 | US | 0 | 0 | 0 | 0.8 | 0.8 | 0.8 | 0.0 | Q4 2023 workbook | |
| Omvoh | 2023 | ExUS | 22.0 | 5.7 | 7.8 | 7.8 | 43.3 | 43.3 | 0.0 | Q4 2023 workbook | |
| Omvoh | 2024 | World | 9.4 | 25.6 | 40.5 | 56.9 | 132.4 | 132.3 | +0.1 | Q4 2024 workbook | Rounding |
| Omvoh | 2024 | US | 3.8 | 15.8 | 24.4 | 23.3 | 67.3 | 67.3 | 0.0 | Q4 2024 workbook | |
| Omvoh | 2024 | ExUS | 5.6 | 9.8 | 16.1 | 33.6 | 65.1 | 65.0 | +0.1 | Q4 2024 workbook | Rounding |
| Omvoh | 2025 | World | 37.2 | 74.8 | 64.9 | 88 | 264.9 | 265 | -0.1 | Q4 2025 workbook (whole millions) | Rounding |
| Omvoh | 2025 | US | 16.1 | 37.6 | 31.8 | 39 | 124.5 | 124 | +0.5 | Q4 2025 workbook (whole millions) | Whole-million rounding |
| Omvoh | 2025 | ExUS | 21.1 | 37.2 | 33.1 | 50 | 141.4 | 141 | +0.4 | Q4 2025 workbook (whole millions) | Whole-million rounding |
| Ebglyss | 2023 | World | 0 (dash, outside window) | 0 (dash, outside window) | 3.5 | 67.6 | 71.1 | 71.2 | -0.1 | Q4 2023 workbook | Workbook FY cell inconsistent (see above) |
| Ebglyss | 2023 | US | 0 (dash, outside window) | 0 (dash, outside window) | 0 | 0 | 0 | 0 (dash) | 0.0 | Q4 2023 workbook | |
| Ebglyss | 2023 | ExUS | 0 (dash, outside window) | 0 (dash, outside window) | 3.5 | 67.6 | 71.1 | 71.2 | -0.1 | Q4 2023 workbook | As World |
| Ebglyss | 2024 | World | 3.1 | 4.3 | 14.9 | 20.4 | 42.7 | 42.8 | -0.1 | Q4 2024 workbook | Rounding |
| Ebglyss | 2024 | US | 0 | 0 | 0.5 | 8.8 | 9.3 | 9.3 | 0.0 | Q4 2024 workbook | |
| Ebglyss | 2024 | ExUS | 3.1 | 4.3 | 14.4 | 11.6 | 33.4 | 33.4 | 0.0 | Q4 2024 workbook | |
| Ebglyss | 2025 | World | 60.2 | 86.8 | 127.1 | 134 | 408.1 | 408 | +0.1 | Q4 2025 workbook (whole millions) | Rounding |
| Ebglyss | 2025 | US | 39.1 | 59.6 | 91.7 | 83 | 273.4 | 274 | -0.6 | Q4 2025 workbook (whole millions) | Whole-million rounding |
| Ebglyss | 2025 | ExUS | 21.1 | 27.2 | 35.3 | 51 | 134.6 | 134 | +0.6 | Q4 2025 workbook (whole millions) | Whole-million rounding |

Taltz 2021, Olumiant 2023 and Omvoh/Ebglyss 2026 are partial years inside the window, so they have no full-year check.
Every full year ties within rounding (0.1, or under 1 where the full year is printed in whole millions), except where whole
quarters are missing (Taltz 2016 US/ExUS, Olumiant 2018 ExUS), and those gaps equal the missing quarters.

## Restatement check

- Prior-year comparatives in the releases (2017-2023), the 10-Qs/10-Ks (2016-2022) and the 2026 releases were compared with the
  first-reported quarter values for all four drugs: **no differences** beyond the rounding below.
- Workbook comparatives: later workbooks reprint earlier quarters with the same values. The Q4 2025 workbook reprints Q1-Q3 2025
  in whole millions (for example Omvoh Q1 2025 16 / 21 / 37 vs 16.1 / 21.1 / 37.2 first reported). This is rounding only;
  first-reported values are kept.
- Olumiant full-year 2017: 45.9 in the Q4 2017 release; the 2019 10-K prints 45.8 (net product revenue, outside US). The quarterly
  rows are as first reported.
- Taltz 2017Q4 ExUS: derived 30.1 vs 30.0 implied by later release commentary (rounding).

## Launch facts (lilly_launches.csv)

Approval dates are from FDA approval letters at accessdata.fda.gov, cross-checked with openFDA drugsfda action dates.

- **Taltz** BLA 125521. Plaque psoriasis 2016-03-22 (S-000). PsA 2017-12-01 (S-004). AS 2019-08-23 (S-016). Pediatric plaque
  psoriasis 2020-03-26 (S-020). nr-axSpA 2020-05-29 (S-019). S-009 (2018-05-17) added genital psoriasis data to the label (not a new
  indication).
- **Olumiant** NDA 207924. RA 2 mg 2018-05-31 (S-000; openFDA lists the document date as 2018-06-01). COVID-19 2022-05-10 (S-006).
  Severe alopecia areata 2022-06-13 (S-007). Alopecia areata in patients 12 and older 2026-09-25 (S-009). S-010 (2026-10-09) is a
  boxed-warning label update.
- **Omvoh** BLA 761279. UC 2023-10-26 (S-000). Crohn's disease 2025-01-15 (S-002). S-005 (2025-10-23) added a 200 mg/2 mL presentation
  for UC maintenance (not a new indication).
- **Ebglyss** BLA 761306. Atopic dermatitis (adults and 12+ years, at least 40 kg) 2024-09-13 (S-000, corrected letter). S-006
  (2026-06-09) added a 250 mg every-8-weeks maintenance option (not a new indication).
- No drug changed reporting company inside its window. Licences: Olumiant (Incyte, worldwide licence to Lilly); Ebglyss (Roche
  licence via the Dermira acquisition, February 2020; Almirall in Europe).

## Documents relied on

All EDGAR documents are under https://www.sec.gov/Archives/edgar/data/59478/. Documents marked (vault) were read from the
Biotech Vault copy, with the manifest's public URL used as `source_url`.

### Earnings releases (8-K Exhibit 99.1)

- Q2 2016, filed 2016-07-26: https://www.sec.gov/Archives/edgar/data/59478/000005947816000393/q216lillysalesandearningsp.htm
- Q3 2016, filed 2016-10-25: https://www.sec.gov/Archives/edgar/data/59478/000005947816000436/q316lillysalesandearningsp.htm
- Q4 2016, filed 2017-01-31: https://www.sec.gov/Archives/edgar/data/59478/000005947817000023/q416lillysalesandearningsp.htm
- Q1 2017, filed 2017-04-25: https://www.sec.gov/Archives/edgar/data/59478/000005947817000127/q117lillysalesandearningsp.htm
- Q2 2017, filed 2017-07-25: https://www.sec.gov/Archives/edgar/data/59478/000005947817000180/q217lillysalesandearningsp.htm
- Q3 2017, filed 2017-10-24: https://www.sec.gov/Archives/edgar/data/59478/000005947817000201/q317lillysalesandearningsp.htm
- Q4 2017, filed 2018-01-31: https://www.sec.gov/Archives/edgar/data/59478/000005947818000028/q417lillysalesandearningsp.htm
- Q1 2018, filed 2018-04-24 (scanned images): https://www.sec.gov/Archives/edgar/data/59478/000005947818000133/q118lillysalesandearning.htm
- Q2 2018, filed 2018-07-24: https://www.sec.gov/Archives/edgar/data/59478/000005947818000186/q218lillysalesandearningsp.htm
- Q3 2018, filed 2018-11-06: https://www.sec.gov/Archives/edgar/data/59478/000005947818000253/q318lillysalesandearningsp.htm
- Q4 2018, filed 2019-02-06: https://www.sec.gov/Archives/edgar/data/59478/000005947819000044/q418lillysalesandearningsp.htm
- Q1 2019, filed 2019-04-30: https://www.sec.gov/Archives/edgar/data/59478/000005947819000171/q119lillysalesandearningsp.htm
- Q2 2019, filed 2019-07-30: https://www.sec.gov/Archives/edgar/data/59478/000005947819000228/q219lillysalesandearningsp.htm
- Q3 2019, filed 2019-10-23: https://www.sec.gov/Archives/edgar/data/59478/000005947819000269/q319lillysalesandearni.htm
- Q4 2019, filed 2020-01-30: https://www.sec.gov/Archives/edgar/data/59478/000005947820000012/q419lillysalesandearni.htm
- Q1 2020, filed 2020-04-23: https://www.sec.gov/Archives/edgar/data/59478/000005947820000100/q120lillysalesandearningsp.htm
- Q2 2020, filed 2020-07-30: https://www.sec.gov/Archives/edgar/data/59478/000005947820000128/q220lillysalesandearni.htm
- Q3 2020, filed 2020-10-27: https://www.sec.gov/Archives/edgar/data/59478/000005947820000152/q320lillysalesandearni.htm
- Q4 2020, filed 2021-01-29: https://www.sec.gov/Archives/edgar/data/59478/000005947821000010/q420lillysalesandearningsp.htm
- Q1 2021, filed 2021-04-27: https://www.sec.gov/Archives/edgar/data/59478/000005947821000117/q121lillysalesandearningsp.htm
- Q2 2021, filed 2021-08-03: https://www.sec.gov/Archives/edgar/data/59478/000005947821000168/q221lillysalesandearningsp.htm
- Q3 2021, filed 2021-10-26: https://www.sec.gov/Archives/edgar/data/59478/000005947821000213/q321lillysalesandearningsp.htm
- Q4 2021, filed 2022-02-03: https://www.sec.gov/Archives/edgar/data/59478/000005947822000016/q421lillysalesandearningsp.htm
- Q1 2022, filed 2022-04-28: https://www.sec.gov/Archives/edgar/data/59478/000005947822000130/q122lillysalesandearningsp.htm
- Q2 2022, filed 2022-08-04: https://www.sec.gov/Archives/edgar/data/59478/000005947822000194/q222lillysalesandearningsp.htm
- Q3 2022, filed 2022-11-01: https://www.sec.gov/Archives/edgar/data/59478/000005947822000248/q322lillysalesandearningsp.htm
- Q4 2022, filed 2023-02-02 (vault): https://www.sec.gov/Archives/edgar/data/59478/000005947823000025/q422lillysalesandearningsp.htm
- Q1 2023, filed 2023-04-27 (vault): https://www.sec.gov/Archives/edgar/data/59478/000005947823000160/q123lillysalesandearningsp.htm
- Q1 2026, filed 2026-04-30 (vault): https://www.sec.gov/Archives/edgar/data/59478/000005947826000043/q126lillysalesandearningsp.htm
- Q2 2026, filed 2026-08-05 (vault): https://www.sec.gov/Archives/edgar/data/59478/000005947826000077/q226lillysalesandearningsp.htm
- Q3 2026, filed 2026-10-29 (vault): https://www.sec.gov/Archives/edgar/data/59478/000005947826000104/q326lillysalesandearningsp.htm
- Q4 2023, filed 2024-02-06 (vault; source of the $65 million Ebglyss milestone statement):
  https://www.sec.gov/Archives/edgar/data/59478/000005947824000032/q423lillysalesandearningsp.htm
- The other 2023-2025 releases (vault) were read to confirm that Omvoh and Ebglyss have no revenue row there.

### 10-Q and 10-K filings

- 10-Q Q2 2016 (2016-07-28): https://www.sec.gov/Archives/edgar/data/59478/000005947816000399/lly-6302016x10q.htm (searched for the Taltz US split)
- 10-Q Q3 2016 (2016-10-28): https://www.sec.gov/Archives/edgar/data/59478/000005947816000440/lly-9302016x10q.htm (searched)
- 10-K 2016 (2017-02-21): https://www.sec.gov/Archives/edgar/data/59478/000005947817000098/lly-20161231x10xk.htm (searched)
- 10-Q Q2 2017 (2017-07-28): https://www.sec.gov/Archives/edgar/data/59478/000005947817000183/lly-6302017x10q.htm (Taltz 2017Q2 ExUS)
- 10-Q Q3 2017 (2017-10-27): https://www.sec.gov/Archives/edgar/data/59478/000005947817000204/lly-9302017x10q.htm (Taltz 2017Q3 ExUS; nine months)
- 10-K 2017 (2018-02-20): https://www.sec.gov/Archives/edgar/data/59478/000005947818000089/lly-20171231x10xk.htm (Taltz FY2017; derivation)
- 10-Q Q1 2018 (2018-04-27): https://www.sec.gov/Archives/edgar/data/59478/000005947818000136/lly-3312018x10q.htm (Taltz 2017Q1 ExUS comparative)
- 10-K 2018 (2019-02-19): https://www.sec.gov/Archives/edgar/data/59478/000005947819000082/lly-20181231x10xk.htm (FY checks; Taltz FY2016 split)
- 10-K 2019 (2020-02-19): https://www.sec.gov/Archives/edgar/data/59478/000005947820000057/lly-20191231x10xk.htm (FY checks)
- 10-K 2020 (2021-02-17): https://www.sec.gov/Archives/edgar/data/59478/000005947821000083/lly-20201231.htm (FY checks)
- 10-K 2021 (2022-02-23): https://www.sec.gov/Archives/edgar/data/59478/000005947822000068/lly-20211231.htm (FY checks)
- 10-K 2022 (2023-02-22, vault): https://www.sec.gov/Archives/edgar/data/59478/000005947823000082/lly-20221231.htm (FY checks)
- 10-K 2023 (2024-02-21, vault): https://www.sec.gov/Archives/edgar/data/59478/000005947824000065/lly-20231231.htm (Ebglyss/Almirall, Omvoh approvals)
- The other 2017-2022 10-Qs were used for the comparative (restatement) check.

### Lilly Financial Workbooks (investor.lilly.com, Product Revenue Report; read from the vault copies)

- Q4 2022 (2023-02-02): https://investor.lilly.com/static-files/696830df-f284-47fe-b21b-8ba13f4a08eb
- Q1 2023 (2023-04-27): https://investor.lilly.com/static-files/87db090f-ba8c-41bb-93c9-0a4871bc622b
- Q2 2023 (2023-08-08): https://investor.lilly.com/static-files/4ac75ee3-b80c-425d-bc40-bbad3eaf64d3
- Q3 2023 (2023-11-02): https://investor.lilly.com/static-files/d8d2a198-e565-41f4-81c2-b9d6a52fdd0c
- Q4 2023 (2024-02-06): https://investor.lilly.com/static-files/42061b11-00c6-434c-b274-af8fb2c64d72
- Q1 2024 (2024-04-30): https://investor.lilly.com/static-files/591188d0-51cb-439b-baa1-518621f390f0
- Q2 2024 (2024-08-08): https://investor.lilly.com/static-files/51b37229-8ae5-480e-805c-a00181dcc541
- Q3 2024 (2024-10-30): https://investor.lilly.com/static-files/73d7cec3-32e7-4727-b82a-574215da0482
- Q4 2024 (2025-02-06): https://investor.lilly.com/static-files/67b79228-97f9-4e7e-93a5-4a580b4bf004
- Q1 2025 (2025-05-01): https://investor.lilly.com/static-files/abc14558-0a5f-4240-9c03-b28fc540b1bf
- Q2 2025 (2025-08-07): https://investor.lilly.com/static-files/d83fb7fe-6a2f-457d-8a2d-8ee150588e75
- Q3 2025 (2025-10-30): https://investor.lilly.com/static-files/530c1a43-10cb-44dc-ae4c-f0eb92a55e62
- Q4 2025 (2026-02-04): https://investor.lilly.com/static-files/17760a45-91e4-4e3c-832c-1301f68fcac0
- Q1 2026 (2026-04-30): https://investor.lilly.com/static-files/9d2cb001-7b42-4117-9268-8c3c27ea5a96
- Q2 2026 (2026-08-05): https://investor.lilly.com/static-files/62390bb9-70f5-4e25-ad8d-3dc2282e2e43
- Q3 2026 (2026-10-29): https://investor.lilly.com/static-files/ba77e8ef-6b14-4fe8-a48e-2978074b1e76

### FDA (https://www.accessdata.fda.gov/drugsatfda_docs/)

- Approval letters (appletter/): 2016/125521Orig1s000ltr.pdf (Taltz); Taltz supplements S-004, S-009, S-016, S-019, S-020;
  2018/207924Orig1s000ltr.pdf (Olumiant); Olumiant S-006, S-007, S-009, S-010; 2023/761279Orig1s000ltr.pdf (Omvoh);
  Omvoh S-002, S-003, S-005; 2024/761306Orig1s000correctedltr.pdf (Ebglyss); Ebglyss S-006.
- Labels (label/): Taltz s000, s009, s032; Olumiant s000, s009; Omvoh s000, s002; Ebglyss s000 (corrected), s006 (mechanism,
  route and dosing).
- openFDA drugsfda API (api.fda.gov/drug/drugsfda.json) for application numbers and action dates.
