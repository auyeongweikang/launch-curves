# takeda_ucb: collection notes

Group: Entyvio (Takeda), Cimzia (UCB), Bimzelx (UCB). Files: `takeda_ucb_sales.csv` (244 rows), `takeda_ucb_launches.csv` (3 rows).
Every value was read from the named public document. Table pages were rendered and checked by eye. Derived values are labelled `derived_*`, and their inputs are given in `notes`.

## Windows covered

| Drug | First sales | First US-sales quarter (Q1) | Window end | Coverage |
|---|---|---|---|---|
| Entyvio | 2014Q2 (US launch June 2014; EU same quarter) | 2014Q2 | 2019Q1 (quarter 20) | 20 of 20 quarters for World and US (JPY); regional splits for every quarter |
| Cimzia | FY2007 (EUR 1m printed for 2007) | 2008Q2 (US approval 2008-04-22, launch April 2008) | 2013Q1 (quarter 20) | Half-year and full-year only (UCB never printed quarters); H1 2008 missing |
| Bimzelx | 2021Q3 (Germany, September 2021) | 2023Q4 (US launch mid-November 2023) | 2026Q2 (latest reported; quarter 20 would be 2028Q3) | Every half-year from H2 2021 to H1 2026 |

## Entyvio (Takeda): how it is reported

- **Fiscal year:** April to March. FY2014 Q1 = April-June 2014 = `2014Q2`. Year rows use the last quarter of the fiscal year: FY2014 is `2015Q1`.
- **Currency and units:** billions of JPY with one decimal, as printed. Takeda also printed a "US major products' sales (in US$)" table (millions of USD) from FY2014 to FY2016. Those values are extra `US` rows with `currency` = USD, so 2014Q2-2017Q1 have two US rows per quarter (JPY and USD). The USD table excludes royalty and service income; the JPY tables of FY2013-FY2014 say they include them. Use one currency at a time. No USD table exists from FY2017 on.
- **Regions:** `Other:Europe and Canada` is printed as "Europe and Canada" up to FY2016 and as "EUCAN" from FY2017. `Other:Emerging Markets` is "Emerging Markets"/"EM". `Other:Japan` appears from FY2018 Q3. Japan approved Entyvio for UC in July 2018 and Takeda launched it there in November 2018 (FY2018 Q3 Tanshin). Before Japan sales began, Takeda's "Overseas total" equals the World total. It is not recorded separately. Takeda prints no single ex-US line, so there are no `ExUS` rows.
- **Quarter figures and where they came from.** These are the important caveats:
  - FY2014 Q1 (2014Q2) is not in any FY2014 Q1 document. The Tanshin only says Entyvio launched in June 2014, and no FY2014 Q1 data book was published. The values come from the prior-year column of the FY2015 Q1 Tanshin (2015-07-30): World 0.4, US 0.4, Europe and Canada 0.0, and USD 4m. Emerging Markets is printed as a dash, so that value is left blank.
  - FY2014 Q2 (2014Q3) is `derived_other`: H1 year-to-date (prior-year column of the FY2015 H1 Data Book) minus FY2014 Q1. The FY2014 H1 data book has no Entyvio sales row. The FY2014 H1 presentation says "¥6.3 b for its first four months" on what appears to be a constant-currency basis. That figure is not used.
  - FY2014 Q3 (2014Q4): World 9.9 is first printed in the FY2014 Q3 supplementary slides (2015-02-05). The regional split comes from the prior-year three-month column of the FY2015 Q3 Tanshin (2016-02-03).
  - FY2014 Q4 (2015Q1) is `derived_fy_minus_9m`: the FY2014 Data Book minus the nine months to December 2014 (FY2015 Q3 Tanshin, prior-year column).
  - FY2015 Q2 and Q4 (2015Q3, 2016Q1) are printed in the quarterly table of the FY2016 H1 Data Book (2016-10-28), not in the FY2015 documents. FY2015 documents printed only year-to-date figures. The FY2015 Q2 quarter equals H1 minus Q1 exactly. For FY2015 Q4, the printed World figure is 26.8, while FY minus 9M gives 26.9 (rounding). The printed value is used.
  - FY2018 Q4 (2019Q1): FY2018 had no Q4 sales data book (the FY2018 Q4 data book covers the pipeline only). World 68.2 is printed in the quarterly table of the FY2019 Q1 Data Book, and also in the FY2019 Q4 Data Book. The regional values (US 45.5, EUCAN 19.7, EM 2.4, Japan 0.6) are `derived_fy_minus_9m`: FY2018 Tanshin p.42 "Product Sales Analysis" minus the Q3 YTD figures in the FY2018 Q3 Data Book. Those regional values sum to 68.2.
- **Basis changes:** FY2018 data books are on Takeda's new "net basis". The change and the 2018-09-11 partial correction affected Japanese products only, not Entyvio's figures. The Shire acquisition (January 2019) did not change Entyvio reporting. Takeda reported Entyvio throughout the window.
- **Restatements:** No later comparative that differs from the first-reported value was found. The FY2015 Q1 values are reprinted unchanged in the FY2016 quarterly tables. The FY2014 Q3 world figure is reprinted as 9.9.

## Cimzia (UCB): how it is reported

- **Half-year and full-year only.** UCB's Q1 and Q3 interim statements for 2008-2009 (15 May 2008, 31 Oct 2008, 30 Apr 2009, 22 Oct 2009) print no Cimzia sales, so there are no quarter rows. Half-year rows use the half's last quarter (H1 = `YYYYQ2`, H2 = `YYYYQ4`). Year rows use `YYYYQ4`. The H2 rows are `derived_other` (full year minus H1) and give a six-month series. They are not printed by UCB.
- **No US-only figure.** UCB's regional tables show `Other:North America` (U.S. and Canada, per the definition printed in the 2013 half-year report), Europe and Rest of World. For 2008-2013 they never show a U.S. line. North America is the closest available proxy for US sales, but it is not US.
- **Region changes:** From 2010, Russia and Turkey moved from Europe to Rest of World. The 2013 reports split Rest of World into Japan, Emerging markets (BRICMT: Brazil, Russia, India, China, Mexico, Turkey) and Rest of World. Under that split, H1 2012 is restated as Japan 0, EM 1, RoW 5 (first reported as RoW 6), and FY2012 as Japan 0, EM 1, RoW 12 (first reported 13). The first-reported values are kept.
- **First sales:** The 2008 Annual Report prints Cimzia 2007 net sales of EUR 1m (North America 0). UCB states the first launches were Switzerland (January 2008) and the U.S. (April 2008). The 2007 figure is recorded as printed.
- **Window end:** Quarter 20 is 2013Q1, which falls inside H1 2013. H1 2013 is recorded and includes 2013Q2.
- **Group-level items:** "Unallocated" amounts (and later "designated hedges reclassified to net sales") are kept at group level. Product rows exclude them.

## Bimzelx (UCB): how it is reported

- **Half-year and full-year only** (2021-2026). UCB's investor "UCB financials" page lists only half-year and full-year reports. No Q1, Q3 or nine-month product sales were found, so Q3 2026 is not available and the series ends with H1 2026. H2 rows are `derived_other` (FY minus H1).
- **Regions:** `US`, `Other:Europe`, `Other:Japan` and `Other:International markets`. In H1 2022, "international markets" still included Japan (BIMZELX Japan EUR 1m). From FY2022, Japan is shown separately, and the 2023 half-year report restated H1 2022 as Japan 1, international markets 0. The H2 2022 Japan and international-markets rows are derived using those restated H1 values (see the row notes).
- **US:** Not approved in the US until 2023-10-17. A printed U.S. line of 0 appears for H1 2022 and, as a comparative, for H1 2023. FY2021 and FY2022 have no U.S. line. First U.S. sales: FY2023 EUR 9m ("launched in the U.S. mid-November"), so H2 2023 = 9.
- **Net sales basis:** Product net sales are "before hedging". Designated hedges reclassified to net sales are a separate group-level line.
- **H1 2026 caveat:** UCB says the H1 2025 base was depressed by a channel-mix true-up that was booked in H2 2025, and that H1 2026 benefited from a favourable prior-period gross-to-net accrual adjustment. This is a group-level statement and is not quantified for Bimzelx.
- **Unrounded figures:** The 2026 half-year results Excel file (`2026-07/2026_HY_Results_excel.xlsx`) gives unrounded euros, for example BIMZELX H1 2026 EUR 1,528,272,260. The CSV keeps the printed millions.

## Gaps

- **Entyvio:** FY2014 Q1 Emerging Markets is blank (a dash is printed). No other gaps in 2014Q2-2019Q1. Regional quarters for FY2014 Q2, FY2014 Q4 and FY2018 Q4 are derived, not printed.
- **Cimzia:** H1 2008 (World and North America) was not found. The 1 Aug 2008 results release names the launches but prints no figure. The 2008 half-year financial report and the 2009 half-year report (which would carry the H1 2008 comparative) could not be located: guessed ucb.com URLs returned 404, and the Wayback Machine was offline during this task. As a result, H2 2008 cannot be derived either. The H1 2009 regional split comes from the 2010 half-year report's comparative column. There is no US-only line for any period.
- **Bimzelx:** No quarterly figures exist in UCB's publications. Q3 2026 has not been published.

## Full-year checks

### Entyvio: sum of four fiscal quarters vs printed fiscal-year total (Takeda fiscal years, all inside the window)

| Fiscal year | Region | Currency | Quarters | Sum of quarters | Printed FY | Difference |
|---|---|---|---|---|---|---|
| FY2014 | World | JPY bn | 4 | 27.8 | 27.8 | 0.0 |
| FY2014 | US | JPY bn | 4 | 20.1 | 20.1 | 0.0 |
| FY2014 | US | USD m | 4 | 179 | 179 | 0 |
| FY2014 | Europe and Canada | JPY bn | 4 | 7.7 | 7.7 | 0.0 |
| FY2014 | Emerging Markets | JPY bn | 3 (Q1 dash) | 0.0 | 0.0 | 0.0 |
| FY2015 | World | JPY bn | 4 | 86.2 | 86.2 | 0.0 |
| FY2015 | US | JPY bn | 4 | 63.0 | 63.1 | -0.1 |
| FY2015 | US | USD m | 4 | 524 | 524 | 0 |
| FY2015 | Europe and Canada | JPY bn | 4 | 21.8 | 21.9 | -0.1 |
| FY2015 | Emerging Markets | JPY bn | 4 | 1.3 | 1.3 | 0.0 |
| FY2016 | World | JPY bn | 4 | 143.1 | 143.2 | -0.1 |
| FY2016 | US | JPY bn | 4 | 99.7 | 99.6 | +0.1 |
| FY2016 | US | USD m | 4 | 913 | 913 | 0 |
| FY2016 | Europe and Canada | JPY bn | 4 | 39.5 | 39.5 | 0.0 |
| FY2016 | Emerging Markets | JPY bn | 4 | 4.2 | 4.0 | +0.2 |
| FY2017 | World | JPY bn | 4 | 201.4 | 201.4 | 0.0 |
| FY2017 | US | JPY bn | 4 | 133.7 | 133.6 | +0.1 |
| FY2017 | EUCAN | JPY bn | 4 | 60.2 | 60.2 | 0.0 |
| FY2017 | EM | JPY bn | 4 | 7.5 | 7.5 | 0.0 |
| FY2018 | World | JPY bn | 4 | 269.2 | 269.2 | 0.0 |
| FY2018 | US / EUCAN / EM / Japan | JPY bn | 4 (Q4 derived) | 182.4 / 75.9 / 9.8 / 1.1 | same | 0.0 by construction |

Differences of 0.1-0.2 are rounding in Takeda's one-decimal tables. FY2014 Q4 and FY2018 Q4 regional quarters are FY minus 9M, so those regional checks are zero by construction. The FY2014 USD and FY2014 regional checks are likewise partly constructed (Q2 and Q4 derived).

### Cimzia and Bimzelx: no quarterly check possible

UCB prints only H1 and the full year, and the H2 rows are FY minus H1, so a four-quarter check cannot be made. Instead, the printed regions were summed against the printed World total for each period:

- **Cimzia:** FY2008 8+2 = 10 (0). H1 2009 23+2 = 25 vs 24 (+1, rounding). FY2009 75 (0). H1 2010 83 (0). FY2010 198 (0). H1 2011 143 (0). FY2011 312 (0). H1 2012 209 (0). FY2012 467 (0). H1 2013 272 (0). FY2007: only North America 0 is printed, against World 1.
- **Bimzelx:** FY2021 4 (0). H1 2022 10 (0). FY2022 35 (0). H1 2023 53 vs 52 (+1). FY2023 149 vs 148 (+1). H1 2024 214 vs 215 (-1). FY2024 607 (0). H1 2025 799 (0). FY2025 2228 vs 2227 (+1). H1 2026 1529 vs 1528 (+1). All differences are rounding.
- Every H1 and FY Cimzia and Bimzelx value was also checked against the prior-year comparative column of the following report. They match, apart from the regional reclassifications listed above.

## Launch facts (see launches CSV)

- **Entyvio:** BLA 125476 was approved 2014-05-20 for both UC and CD (approval letter and 2014 label: integrin receptor antagonist; 300 mg IV at weeks 0, 2 and 6, then every 8 weeks). The S-057 letter (2023-09-28) aligns the labeling with subcutaneous ENTYVIO and ENTYVIO Pen for UC. Drugs@FDA lists S-060/S-061 on 2024-04-18, but those letters were not opened, so no date for subcutaneous use in CD is claimed.
- **Cimzia:** BLA 125160 was approved 2008-04-22 for CD. Later US indications: RA 2009-05-13 (Drugs@FDA SUPPL-80; no letter posted; UCB press release 2009-05-14), PsA 2013-09-27, AS 2013-10-17, plaque psoriasis 2018-05-24, nr-axSpA 2019-03-28 and pJIA 2024-09-13, each from its FDA letter. Cimzia has no UC approval.
- **Bimzelx:** BLA 761151 was approved 2023-10-17 for plaque psoriasis, after a complete response letter on 2022-05-12. PsA, nr-axSpA and AS were approved 2024-09-20, and HS 2024-11-19.

## Source dates

- **Takeda:** The release date of each results package (confirmed from Takeda's archive pages and the document dates).
- **UCB annual reports 2008-2012:** The date of the statutory auditor's report printed in the report. The PDF itself may have been posted a few weeks later.
- **UCB half-year reports:** The date printed in the report on which the board approved it for issue (or the date of the auditor's review). The 2010 results press release is dated 2 August 2010.
- **UCB FY2021-FY2024 management reports:** No date is printed in these documents, so the PDF creation date from the file metadata is used. Publication was on, or the morning after, that date.
- **UCB 2025 Integrated Annual Report:** Its stated publication date, 2026-02-26.

## Documents relied on

Takeda (all on `assets-dam.takeda.com/.../investors/quarterly-announcements/`; full URLs in the CSV):
- FY2014: Q1 Tanshin `qr2014_q1_f_en.pdf`, H1 presentation `qr2014_q2_p01_en.pdf` (context only), Q3 Tanshin `qr2014_q3_f_en.pdf`, Q3 supplementary materials `qr2014_q3_p03_en.pdf`, Data Book `qr2014_full_d_en.pdf`.
- FY2015: Q1 Tanshin `financial-statements-download-entire-file.pdf`, H1 Data Book `data-book-download-file.pdf`, Q3 Tanshin `qr2015_q3_f_en.pdf`, Data Book `data-book.pdf`.
- FY2016: Q1 Data Book `download-data-book.pdf`, H1 Data Book `databook.pdf`, Q3 Data Book `qr2016_q3_d_en.pdf`, Data Book `qr2016_q4_d1_en.pdf`.
- FY2017: Q1 `qr2017_q1_d_en.pdf`, Q2 `qr2017_q2_d_en.pdf`, Q3 `qr2017_q3_d_en.pdf`, Q4 `qr2017_q4_d01_en.pdf` (Data Books).
- FY2018: Q1 `qr2018_q1_d_en_3.pdf`, Q2 `qr2018_q2_d_en.pdf`, Q3 `qr2018_q3_d-en.pdf` (Data Books), FY Tanshin `qr2018_q4_f_en.pdf`.
- FY2019: Q1 Data Book (revised) `qr2019_q1_d_en_revised.pdf`. The FY2019 Q4 Data Book `qr2019_q4_d_en.pdf` was used as a cross-check.
- Some FY2016-FY2018 data books were read from the local Biotech Vault copies (read only). Their original takeda.com URLs are used as sources.

UCB (Cimzia): 2008, 2009, 2010, 2011, 2012 and 2013 Annual Reports; 2010, 2011, 2012 and 2013 half-year reports (`ucb.com/_up/ucb_com_ir/documents/`); press releases 080515, 080801, 081031, 090303, 090430, 090731, 091022 and HY2010 results (`ucb.com/sites/default/files/press_files/`); Cimzia RA approval release 090514.

UCB (Bimzelx): FY2021 Business Performance Review; 2022, 2023, 2024, 2025 and 2026 half-year financial reports; 2022, 2023 and 2024 full-year management reports; 2025 Integrated Annual Report; 2026 HY results Excel file (cross-check only).

FDA (accessdata.fda.gov): Drugs@FDA histories for BLA 125476, 125160 and 761151; letters 125476 s000 and s057; 125160 s000, s174, s213, s215, s237, s275, s283 and s305; 761151 s000, s005-s007 and s010; labels 125476s000, 125160s315 and 761151s010.
