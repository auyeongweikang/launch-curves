# az_gsk: collection notes

Group `az_gsk`: Fasenra, Saphnelo, Tezspire (AstraZeneca; Tezspire with Amgen), Nucala and Benlysta (GSK; Benlysta with Human Genome Sciences until 2012).
Collected 2026-11-19 from SEC EDGAR filings (AstraZeneca and GSK 6-Ks, Amgen 8-K Exhibit 99.1, Human Genome Sciences 10-Q/8-K/10-K) and FDA (Drugs@FDA via openFDA, approval letters, labels).
No local Biotech Vault documents were used (the GSK folder holds clinical trial documents only, no results releases).

`az_gsk_sales.csv`: 502 rows. `az_gsk_launches.csv`: 5 rows.

| Drug | Reporting company | Rows | Quarters covered | Blank rows |
|---|---|---|---|---|
| Fasenra | AstraZeneca | 97 | 2017Q4-2022Q3 (20) | 2017Q4 US, 2017Q4 World |
| Saphnelo | AstraZeneca | 100 | 2021Q3-2026Q2 (20) | none |
| Tezspire | AstraZeneca | 83 | 2022Q1-2026Q3 (19) | 2022Q1 World, 2022Q2 World, 2022Q3 World |
| Tezspire | Amgen | 57 | 2022Q1-2026Q3 (19) | none |
| Nucala | GSK | 78 | 2015Q4-2020Q3 (20) | 2015Q4 US |
| Benlysta | GSK | 80 | 2011Q1-2015Q4 (20) | 2011Q1 World, 2011Q4 World |
| Benlysta | Human Genome Sciences | 7 | 2011Q1-2012Q3 (7) | 2012Q3 US |

## Windows

Window = first quarter with any reported sales through quarter 20 counted from the first quarter with US sales, or the latest reported quarter (Q3 2026), whichever is first.

| Drug | First quarter with US sales | Window | Why |
|---|---|---|---|
| Fasenra | 2017Q4 | 2017Q4-2022Q3 (20 quarters) | US approval 14 Nov 2017 and launch straight after (AZ H1 2018 report). No sales anywhere before. |
| Saphnelo | 2021Q3 | 2021Q3-2026Q2 (20) | US approval 30 Jul 2021; US sales $1m in Q3 2021. |
| Tezspire | 2022Q1 | 2022Q1-2026Q3 (19, latest reported) | US approval 17 Dec 2021; Amgen's Q4 2021 release has no Tezspire line and AZ's Q4 2021 collaboration revenue was nil; Amgen US sales $7m in Q1 2022. |
| Nucala | 2015Q4 | 2015Q4-2020Q3 (20) | US approval 4 Nov 2015; GSK: 'launched at the end of 2015'; first printed sales GBP 1m in Q4 2015. |
| Benlysta | 2011Q1 | 2011Q1-2015Q4 (20) | US approval 9 Mar 2011; HGS: first BENLYSTA sales recognised in March 2011. |

## Region coding

- AstraZeneca prints Product Sales in USD millions by World (total), US, Emerging Markets, Europe and Established Rest of World (Established RoW). Recorded as `World`, `US`, `Other:Emerging Markets`, `Other:Europe`, `Other:Established RoW`. No single ex-US line is printed, so no `ExUS` rows for AZ.
- GSK prints Pharmaceuticals turnover in GBP millions. The regional columns changed over time: 2012-2013 `Total, USA/US, Europe, EMAP, Rest of World`; 2014 `Total, USA, Europe, Emerging Markets, Japan`; 2015 onward `Total, US, Europe, International`. Recorded as `World`, `US`, `Other:Europe`, `Other:EMAP`, `Other:Rest of World`, `Other:Emerging Markets`, `Other:Japan`, `Other:International`. GSK's 'International' is not ex-US (Europe is separate), so it is `Other:International`, not `ExUS`.
- In 2014 GSK's printed regions do not add up to Total (there is an unprinted residual region). For Benlysta the residual is GBP 0-1m a quarter (for example Q1 2014: Total 38 vs 34+3+1+0 = 38; Q2 2014: 41 vs 37+3+0+0 = 40).
- Amgen prints Tezspire as US, ROW and TOTAL (USD millions). ROW is always printed as '—' (nil): recorded as `ExUS` = 0. TOTAL is recorded as `World` but is Amgen-recorded sales only.
- Human Genome Sciences printed US net product sales only (USD millions, one decimal): recorded as `US`.
- A printed '-' or '—' is recorded as value 0 with the note "printed as '-' (nil)".
- GSK and AZ print whole millions; quarterly figures are rounded separately, so sums can differ from full-year figures by 1.

## Drug by drug

### Fasenra (AstraZeneca)

- 2017Q4 is blank (World and US rows, `not found:`). AZ's FY and Q4 2017 results (6-K, 2 Feb 2018) have no Fasenra line; Q4 2017 sales sit inside Respiratory 'Others'. The 2017 Form 20-F was filed as images and its XBRL has no Fasenra figure. 2018 reports print 2018 vs 2017 growth only as 'n/m', not a 2017 value. So the first figure is Q1 2018 ($21m, US $19m).
- 2018Q1-2022Q3 complete for all five regions, taken from the 'Product Sales year-on-year analysis' table for each quarter in AZ's results announcements.
- Restatement check: AZ's later reports (quarterly sequential tables, 2018-2021) were compared with the first-reported Fasenra quarters; no restated quarter was noticed.

### Saphnelo (AstraZeneca)

- Complete 2021Q3-2026Q2 for all five regions. No restated quarter was noticed.

### Tezspire (AstraZeneca and Amgen): split reporting

- AstraZeneca results (H1 2022 and FY 2022): "Amgen records sales in the US and AstraZeneca records its share of gross profits in the US as Collaboration Revenue. Total ex-US product sales are recorded as AstraZeneca revenue."
- So the file has two sets of rows: `reporting_company = Amgen` (US product sales; Amgen prints ROW as nil) and `reporting_company = AstraZeneca` (ex-US product sales: Europe, Established RoW, Emerging Markets; AZ prints US as '-'). They are not added together anywhere in the file. Amgen's `World` and AZ's `World` are each company's own recorded sales, not global sales.
- AZ rows 2022Q1-2022Q3 are blank (`not found:`): AZ printed no Tezspire Product Sales until Q4 2022 ($4m; FY 2022 also $4m). AZ's H1 2022 report says Tezspire Total Revenue of $16m in the half 'was comprised entirely of Collaboration Revenue'.
- AZ's Collaboration/Alliance Revenue for Tezspire (its share of US gross profit) is NOT in the sales file. For reference, AZ printed Tezspire collaboration revenue of $16m in H1 2022, $42m in 9M 2022 and $79m in FY 2022; AZ's Q3 2026 report prints Tezspire Total Revenue (product sales plus alliance revenue) of $1,123m for 9M 2026 and $429m for Q3 2026, against Q3 2026 Product Sales of $188m.
- AZ also prints a 'global in-market sales' figure (for example $174m in 2022; $36m US in-market in H1 2022). These are not company net sales and are not recorded.
- Amgen rows 2022Q1-2026Q3 are complete. Restatement check: each Amgen release prints the prior-year quarter's total; all 15 comparatives (2022Q1-2025Q3) match the first-reported figures.

### Nucala (GSK)

- 2015Q4: GSK printed only a total, GBP 1m, in the 'Sales from New Pharmaceutical and Vaccine products' table (Q4 2015 results; FY 2015 also GBP 1m, also in the 2015 Annual Report). The `World` row has the value; the `US` row is blank (`not found:`). EU approval came on 2 Dec 2015, so the GBP 1m may not be all US.
- 2016Q1-2020Q3 complete for Total, US, Europe, International. In Q3 and Q4 2018 GSK printed the line as 'Nucala/Mepolizumab' (label recorded as printed).
- GSK's quarterly releases print growth rates rather than prior-year values, so restated quarters could not be compared directly; none was noticed.

### Benlysta (Human Genome Sciences and GSK): collaboration accounting and ownership change

- Launch to 2 Aug 2012: HGS booked US net product sales; GSK booked sales outside the US plus its share of US gross profit. GSK's figures for this period are therefore NOT product sales in the US: GSK says its turnover 'reflects share of gross profit in the USA and total sales in all other markets'. Rows for 2011Q2-2012Q2 from GSK carry a `COLLABORATION ACCOUNTING` note.
- HGS rows (`reporting_company = Human Genome Sciences`, US, USD): 2011Q1 $0.1m (`derived_other`: six months $7.9m minus Q2 $7.8m, both printed in the Q2 2011 10-Q; the Q1 2011 10-Q gives no amount), 2011Q2 $7.8m, 2011Q3 $18.8m, 2011Q4 $25.7m, 2012Q1 $31.2m, 2012Q2 $38.1m. 2012Q3 blank (`not found:`): HGS was acquired on 3 Aug 2012 and filed no further report.
- GSK 2011: GSK printed Benlysta only in text. Q2 2011 GBP 2m and Q3 2011 GBP 6m are recorded (`World`); Q1 2011 and Q4 2011 are blank (`not found:`). GSK printed 'GSK turnover of GBP 15 million in the year' for 2011 but no Q1 or nine-month figure, so Q4 cannot be derived. GSK's Q3 2011 text also says 'Total sales in the quarter were $19 million' (all markets, USD); that is not recorded as a row.
- 2012Q3 (GSK): mixed period. GSK's Q3 2012 results say HGS 'reported sales of GBP 23 million from that date, including GBP 16 million of Benlysta sales in the US'. GSK's Q3 2012 US Benlysta figure (GBP 19m) combines profit share to 2 Aug and full US sales from 3 Aug.
- From 2012Q4, GSK's US column is full US product sales.
- Currency differs by company: HGS rows are USD, GSK rows are GBP.
- Restatement: GSK's 2015 Annual Report restated FY 2014 Benlysta into the new regions (Total 173, US 156, Europe 12, International 5) against the first-reported FY 2014 split (USA 155, Europe 12, Emerging Markets 3, Japan nil). Quarterly 2014 values in the file are as first reported. No restated quarter was printed.

## Full-year checks

Sum of the four quarterly values in the file compared with the full-year figure printed in the Q4/full-year release. Differences of 1 are rounding (each quarter and the year are rounded separately).

### AstraZeneca (USD m)

| Company | Drug | Year | Region | Sum of 4 quarters | Printed full year | Difference |
|---|---|---|---|---|---|---|
| AstraZeneca | Fasenra | 2018 | World | 297 | 297 | 0 |
| AstraZeneca | Fasenra | 2018 | US | 218 | 218 | 0 |
| AstraZeneca | Fasenra | 2018 | Other:Emerging Markets | 1 | 1 | 0 |
| AstraZeneca | Fasenra | 2018 | Other:Europe | 32 | 32 | 0 |
| AstraZeneca | Fasenra | 2018 | Other:Established RoW | 46 | 46 | 0 |
| AstraZeneca | Fasenra | 2019 | World | 704 | 704 | 0 |
| AstraZeneca | Fasenra | 2019 | US | 482 | 482 | 0 |
| AstraZeneca | Fasenra | 2019 | Other:Emerging Markets | 5 | 5 | 0 |
| AstraZeneca | Fasenra | 2019 | Other:Europe | 118 | 118 | 0 |
| AstraZeneca | Fasenra | 2019 | Other:Established RoW | 99 | 99 | 0 |
| AstraZeneca | Fasenra | 2020 | World | 949 | 949 | 0 |
| AstraZeneca | Fasenra | 2020 | US | 603 | 603 | 0 |
| AstraZeneca | Fasenra | 2020 | Other:Emerging Markets | 12 | 12 | 0 |
| AstraZeneca | Fasenra | 2020 | Other:Europe | 203 | 203 | 0 |
| AstraZeneca | Fasenra | 2020 | Other:Established RoW | 131 | 131 | 0 |
| AstraZeneca | Fasenra | 2021 | World | 1259 | 1258 | 1 |
| AstraZeneca | Fasenra | 2021 | US | 790 | 790 | 0 |
| AstraZeneca | Fasenra | 2021 | Other:Emerging Markets | 20 | 20 | 0 |
| AstraZeneca | Fasenra | 2021 | Other:Europe | 286 | 286 | 0 |
| AstraZeneca | Fasenra | 2021 | Other:Established RoW | 163 | 162 | 1 |
| AstraZeneca | Saphnelo | 2022 | World | 116 | 116 | 0 |
| AstraZeneca | Saphnelo | 2022 | US | 112 | 111 | 1 |
| AstraZeneca | Saphnelo | 2022 | Other:Emerging Markets | 0 | 0 | 0 |
| AstraZeneca | Saphnelo | 2022 | Other:Europe | 1 | 2 | -1 |
| AstraZeneca | Saphnelo | 2022 | Other:Established RoW | 3 | 3 | 0 |
| AstraZeneca | Saphnelo | 2023 | World | 280 | 280 | 0 |
| AstraZeneca | Saphnelo | 2023 | US | 261 | 260 | 1 |
| AstraZeneca | Saphnelo | 2023 | Other:Emerging Markets | 2 | 2 | 0 |
| AstraZeneca | Saphnelo | 2023 | Other:Europe | 7 | 8 | -1 |
| AstraZeneca | Saphnelo | 2023 | Other:Established RoW | 10 | 10 | 0 |
| AstraZeneca | Saphnelo | 2024 | World | 474 | 474 | 0 |
| AstraZeneca | Saphnelo | 2024 | US | 425 | 425 | 0 |
| AstraZeneca | Saphnelo | 2024 | Other:Emerging Markets | 7 | 7 | 0 |
| AstraZeneca | Saphnelo | 2024 | Other:Europe | 26 | 26 | 0 |
| AstraZeneca | Saphnelo | 2024 | Other:Established RoW | 16 | 16 | 0 |
| AstraZeneca | Saphnelo | 2025 | World | 686 | 686 | 0 |
| AstraZeneca | Saphnelo | 2025 | US | 596 | 596 | 0 |
| AstraZeneca | Saphnelo | 2025 | Other:Emerging Markets | 17 | 16 | 1 |
| AstraZeneca | Saphnelo | 2025 | Other:Europe | 49 | 49 | 0 |
| AstraZeneca | Saphnelo | 2025 | Other:Established RoW | 24 | 25 | -1 |
| AstraZeneca | Tezspire | 2022 | World | n/a (quarters blank) | 4 | n/a |
| AstraZeneca | Tezspire | 2022 | US | n/a (quarters blank) | 0 | n/a |
| AstraZeneca | Tezspire | 2022 | Other:Emerging Markets | n/a (quarters blank) | 0 | n/a |
| AstraZeneca | Tezspire | 2022 | Other:Europe | n/a (quarters blank) | 2 | n/a |
| AstraZeneca | Tezspire | 2022 | Other:Established RoW | n/a (quarters blank) | 2 | n/a |
| AstraZeneca | Tezspire | 2023 | World | 86 | 86 | 0 |
| AstraZeneca | Tezspire | 2023 | US | 0 | 0 | 0 |
| AstraZeneca | Tezspire | 2023 | Other:Emerging Markets | 1 | 1 | 0 |
| AstraZeneca | Tezspire | 2023 | Other:Europe | 49 | 48 | 1 |
| AstraZeneca | Tezspire | 2023 | Other:Established RoW | 36 | 37 | -1 |
| AstraZeneca | Tezspire | 2024 | World | 248 | 248 | 0 |
| AstraZeneca | Tezspire | 2024 | US | 0 | 0 | 0 |
| AstraZeneca | Tezspire | 2024 | Other:Emerging Markets | 12 | 11 | 1 |
| AstraZeneca | Tezspire | 2024 | Other:Europe | 156 | 156 | 0 |
| AstraZeneca | Tezspire | 2024 | Other:Established RoW | 80 | 81 | -1 |
| AstraZeneca | Tezspire | 2025 | World | 459 | 458 | 1 |
| AstraZeneca | Tezspire | 2025 | US | 0 | 0 | 0 |
| AstraZeneca | Tezspire | 2025 | Other:Emerging Markets | 40 | 40 | 0 |
| AstraZeneca | Tezspire | 2025 | Other:Europe | 298 | 297 | 1 |
| AstraZeneca | Tezspire | 2025 | Other:Established RoW | 121 | 121 | 0 |

Notes: Fasenra 2017 and 2022 are not full years in the window or not printed. Tezspire (AZ) 2022: quarters 2022Q1-Q3 are blank because no product sales were printed; the only printed quarter, Q4 2022 ($4m: Europe 2, Established RoW 2), equals the FY 2022 figure ($4m). Saphnelo 2021 and 2026 are partial years.

### Amgen, Tezspire (USD m)

| Company | Drug | Year | Region | Sum of 4 quarters | Printed full year | Difference |
|---|---|---|---|---|---|---|
| Amgen | Tezspire | 2022 | US | 170 | 170 | 0 |
| Amgen | Tezspire | 2022 | ExUS | 0 | 0 | 0 |
| Amgen | Tezspire | 2022 | World | 170 | 170 | 0 |
| Amgen | Tezspire | 2023 | US | 567 | 567 | 0 |
| Amgen | Tezspire | 2023 | ExUS | 0 | 0 | 0 |
| Amgen | Tezspire | 2023 | World | 567 | 567 | 0 |
| Amgen | Tezspire | 2024 | US | 972 | 972 | 0 |
| Amgen | Tezspire | 2024 | ExUS | 0 | 0 | 0 |
| Amgen | Tezspire | 2024 | World | 972 | 972 | 0 |
| Amgen | Tezspire | 2025 | US | 1478 | 1478 | 0 |
| Amgen | Tezspire | 2025 | ExUS | 0 | 0 | 0 |
| Amgen | Tezspire | 2025 | World | 1478 | 1478 | 0 |

### GSK (GBP m)

| Company | Drug | Year | Region | Sum of 4 quarters | Printed full year | Difference |
|---|---|---|---|---|---|---|
| GSK | Benlysta | 2012 | World | 70 | 70 | 0 |
| GSK | Benlysta | 2012 | US | 65 | 65 | 0 |
| GSK | Benlysta | 2012 | Other:Europe | 4 | 4 | 0 |
| GSK | Benlysta | 2012 | Other:EMAP | 0 | 0 | 0 |
| GSK | Benlysta | 2012 | Other:Rest of World | 1 | 1 | 0 |
| GSK | Benlysta | 2013 | World | 146 | 146 | 0 |
| GSK | Benlysta | 2013 | US | 134 | 134 | 0 |
| GSK | Benlysta | 2013 | Other:Europe | 8 | 8 | 0 |
| GSK | Benlysta | 2013 | Other:EMAP | 1 | 1 | 0 |
| GSK | Benlysta | 2013 | Other:Rest of World | 3 | 3 | 0 |
| GSK | Benlysta | 2014 | World | 173 | 173 | 0 |
| GSK | Benlysta | 2014 | US | 155 | 155 | 0 |
| GSK | Benlysta | 2014 | Other:Europe | 12 | 12 | 0 |
| GSK | Benlysta | 2014 | Other:Emerging Markets | 3 | 3 | 0 |
| GSK | Benlysta | 2014 | Other:Japan | 0 | 0 | 0 |
| GSK | Benlysta | 2015 | World | 230 | 230 | 0 |
| GSK | Benlysta | 2015 | US | 209 | 209 | 0 |
| GSK | Benlysta | 2015 | Other:Europe | 15 | 15 | 0 |
| GSK | Benlysta | 2015 | Other:International | 6 | 6 | 0 |
| GSK | Nucala | 2016 | World | 102 | 102 | 0 |
| GSK | Nucala | 2016 | US | 71 | 71 | 0 |
| GSK | Nucala | 2016 | Other:Europe | 23 | 23 | 0 |
| GSK | Nucala | 2016 | Other:International | 8 | 8 | 0 |
| GSK | Nucala | 2017 | World | 344 | 344 | 0 |
| GSK | Nucala | 2017 | US | 236 | 236 | 0 |
| GSK | Nucala | 2017 | Other:Europe | 70 | 70 | 0 |
| GSK | Nucala | 2017 | Other:International | 38 | 38 | 0 |
| GSK | Nucala | 2018 | World | 563 | 563 | 0 |
| GSK | Nucala | 2018 | US | 341 | 341 | 0 |
| GSK | Nucala | 2018 | Other:Europe | 152 | 152 | 0 |
| GSK | Nucala | 2018 | Other:International | 70 | 70 | 0 |
| GSK | Nucala | 2019 | World | 768 | 768 | 0 |
| GSK | Nucala | 2019 | US | 453 | 453 | 0 |
| GSK | Nucala | 2019 | Other:Europe | 206 | 206 | 0 |
| GSK | Nucala | 2019 | Other:International | 109 | 109 | 0 |

Other years: Benlysta 2011 (GSK) - only Q2 (GBP 2m) and Q3 (GBP 6m) printed, FY 2011 GBP 15m, so no check is possible. Nucala 2015 - Q4 GBP 1m equals FY 2015 GBP 1m (World). Nucala 2020 is a partial year.

### Human Genome Sciences, Benlysta US (USD m)

| Year | Sum of 4 quarters | Printed full year | Difference |
|---|---|---|---|
| 2011 | 52.4 (0.1 derived + 7.8 + 18.8 + 25.7) | 52.3 (Q4 2011 earnings release and 2011 Form 10-K) | 0.1 (rounding; Q1 is derived from rounded figures) |

2012 is not a full year for HGS (acquired 3 Aug 2012). The six-month 2012 figure printed in the Q2 2012 10-Q ($69.3m) equals Q1 + Q2 (31.2 + 38.1).

## Other things a reader must know

- Values are company net sales as printed (AZ 'Product Sales', GSK 'turnover', Amgen 'Product Sales', HGS 'net product sales'). No conversion between currencies.
- AstraZeneca table numbers (for example 'Table 22') are given in `source_location`; older AZ reports have unnumbered tables, named by title.
- Source URLs point to the EDGAR document that holds the figure (6-K for AZ and GSK; 8-K Exhibit 99.1 for Amgen; 10-Q or 8-K Exhibit 99 for HGS).

## Documents relied on

Sales figures (every document listed was opened; one URL per filing):

- Amgen, 2022-04-27: Amgen Q1 2022 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815422000019/amgenq12022earningsrelease.htm
- Amgen, 2022-08-04: Amgen Q2 2022 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815422000039/amgn-2022630earningsrelease.htm
- Amgen, 2022-11-03: Amgen Q3 2022 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815422000053/amgn-2022930earningsrelease.htm
- Amgen, 2023-01-30: Amgen Q4 2022 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815423000011/amgn-20221231earningsrelea.htm
- Amgen, 2023-04-27: Amgen Q1 2023 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815423000026/amgn-2023331earningsrelease.htm
- Amgen, 2023-08-03: Amgen Q2 2023 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815423000049/amgn-2023630earningsrelease.htm
- Amgen, 2023-10-31: Amgen Q3 2023 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815423000061/amgn-2023930earningsrelease.htm
- Amgen, 2024-02-06: Amgen Q4 2023 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815424000004/amgn-20231231earningsrelea.htm
- Amgen, 2024-05-02: Amgen Q1 2024 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815424000018/amgn-20240331earningsrelea.htm
- Amgen, 2024-08-06: Amgen Q2 2024 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815424000033/amgn-20240630earningsrelea.htm
- Amgen, 2024-10-30: Amgen Q3 2024 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815424000042/amgn-20240930earningsrelea.htm
- Amgen, 2025-02-04: Amgen Q4 2024 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815425000005/amgn-20241231earningsrelea.htm
- Amgen, 2025-05-01: Amgen Q1 2025 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815425000018/amgn-20250331earningsrelea.htm
- Amgen, 2025-08-05: Amgen Q2 2025 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815425000054/amgn-20250630earningsrelea.htm
- Amgen, 2025-11-04: Amgen Q3 2025 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815425000070/amgn-20250930earningsrelea.htm
- Amgen, 2026-02-03: Amgen Q4 2025 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815426000003/amgn-20251231earningsrelea.htm
- Amgen, 2026-04-30: Amgen Q1 2026 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815426000054/amgn-20260331earningsrelea.htm
- Amgen, 2026-08-04: Amgen Q2 2026 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815426000124/amgn-20260630earningsrelea.htm
- Amgen, 2026-11-03: Amgen Q3 2026 earnings release (8-K Exhibit 99.1) - https://www.sec.gov/Archives/edgar/data/318154/000031815426000153/amgn-20260930earningsrelea.htm
- AstraZeneca, 2018-02-02: AstraZeneca FY and Q4 2017 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495418001029/azn.htm
- AstraZeneca, 2018-05-18: AstraZeneca Q1 2018 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495418005620/a4988o.htm
- AstraZeneca, 2018-07-26: AstraZeneca H1 and Q2 2018 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000110465918047274/a18-14307_16k.htm
- AstraZeneca, 2018-11-08: AstraZeneca 9M and Q3 2018 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495418012172/a7037g.htm
- AstraZeneca, 2019-02-14: AstraZeneca FY and Q4 2018 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495419001546/a9540p.htm
- AstraZeneca, 2019-04-26: AstraZeneca Q1 2019 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495419004837/a1704x.htm
- AstraZeneca, 2019-07-25: AstraZeneca H1 and Q2 2019 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000110465919041809/a19-12893_16k.htm
- AstraZeneca, 2019-10-24: AstraZeneca 9M and Q3 2019 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495419011972/a9391q1.htm
- AstraZeneca, 2020-02-14: AstraZeneca FY and Q4 2019 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495420001577/a9843cnew.htm
- AstraZeneca, 2020-04-29: AstraZeneca Q1 2020 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495420004573/a2404l.htm
- AstraZeneca, 2020-07-30: AstraZeneca H1 and Q2 2020 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495420008163/a5880uv2.htm
- AstraZeneca, 2020-11-05: AstraZeneca 9M and Q3 2020 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495420011868/a3158e.htm
- AstraZeneca, 2021-02-11: AstraZeneca FY and Q4 2020 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495421001465/a6964o.htm
- AstraZeneca, 2021-04-30: AstraZeneca Q1 2021 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495421004839/a1438x.htm
- AstraZeneca, 2021-07-30: AstraZeneca H1 and Q2 2021 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000110465921097781/tmb-20210630x6k.htm
- AstraZeneca, 2021-11-12: AstraZeneca 9M and Q3 2021 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495421012039/a1635s.htm
- AstraZeneca, 2022-02-10: AstraZeneca FY and Q4 2021 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495422001372/a2250b.htm
- AstraZeneca, 2022-04-29: AstraZeneca Q1 2022 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495422005571/a7847j.htm
- AstraZeneca, 2022-07-29: AstraZeneca H1 and Q2 2022 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000110465922083922/azn-20220331x6k.htm
- AstraZeneca, 2022-11-10: AstraZeneca 9M and Q3 2022 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495422014930/a9087f.htm
- AstraZeneca, 2023-02-09: AstraZeneca FY and Q4 2022 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495423001503/a3767p.htm
- AstraZeneca, 2023-04-27: AstraZeneca Q1 2023 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495423005296/a6110x.htm
- AstraZeneca, 2023-07-28: AstraZeneca H1 and Q2 2023 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000110465923085104/azn-20230630x6k.htm
- AstraZeneca, 2023-11-09: AstraZeneca 9M and Q3 2023 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495423013969/a8671s.htm
- AstraZeneca, 2024-02-08: AstraZeneca FY and Q4 2023 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495424001467/a4081c.htm
- AstraZeneca, 2024-04-25: AstraZeneca Q1 2024 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495424004975/a9413l.htm
- AstraZeneca, 2024-07-25: AstraZeneca H1 and Q2 2024 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000110465924082531/azn-20240630x6k.htm
- AstraZeneca, 2024-11-12: AstraZeneca 9M and Q3 2024 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495424014089/a7967l.htm
- AstraZeneca, 2025-02-06: AstraZeneca FY and Q4 2024 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495425001189/a1107w.htm
- AstraZeneca, 2025-04-29: AstraZeneca Q1 2025 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495425004737/a5242g.htm
- AstraZeneca, 2025-07-29: AstraZeneca H1 and Q2 2025 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000110465925071432/azn-20250630x6k.htm
- AstraZeneca, 2025-11-06: AstraZeneca 9M and Q3 2025 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495425012630/a4030g.htm
- AstraZeneca, 2026-02-10: AstraZeneca FY and Q4 2025 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495426001073/a3234s.htm
- AstraZeneca, 2026-04-29: AstraZeneca Q1 2026 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495426004047/a2999c.htm
- AstraZeneca, 2026-07-27: AstraZeneca H1 and Q2 2026 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000110465926086846/azn-20260630x6k.htm
- AstraZeneca, 2026-10-30: AstraZeneca 9M and Q3 2026 results announcement (6-K) - https://www.sec.gov/Archives/edgar/data/901832/000165495426009256/a0835b.htm
- GSK, 2011-04-27: GSK Q1 2011 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000095012311039933/u11011e6vk.htm
- GSK, 2011-07-26: GSK Q2 2011 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119312511197252/d6k.htm
- GSK, 2011-10-26: GSK Q3 2011 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119312511281704/d247608d6k.htm
- GSK, 2012-02-07: GSK Q4 2011 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119312512043398/d286391d6k.htm
- GSK, 2012-04-25: GSK Q1 2012 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119163812000550/gsk201204256k.htm
- GSK, 2012-07-25: GSK Q2 2012 and half-year results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119163812000958/gsk201207256k.htm
- GSK, 2012-10-31: GSK Q3 2012 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119163812001390/gsk201210316k.htm
- GSK, 2013-02-06: GSK Q4 2012 and full-year results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119163813000135/gsk201302066k2.htm
- GSK, 2013-04-24: GSK Q1 2013 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119163813000509/gsk201304246k.htm
- GSK, 2013-07-24: GSK Q2 2013 and half-year results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119163813000943/gsk201307246k.htm
- GSK, 2013-10-23: GSK Q3 2013 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119163813001342/gsk201310236k.htm
- GSK, 2014-02-05: GSK Q4 2013 and full-year results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119163814000145/gsk201402056k.htm
- GSK, 2014-04-30: GSK Q1 2014 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119163814000647/gsk201404306k.htm
- GSK, 2014-07-23: GSK Q2 2014 and half-year results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119163814001050/gsk201407236k.htm
- GSK, 2014-10-22: GSK Q3 2014 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119163814001364/gsk201410226k.htm
- GSK, 2015-02-04: GSK Q4 2014 and full-year results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119163815000135/gsk201502046k.htm
- GSK, 2015-05-06: GSK Q1 2015 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119163815000622/gsk201505066k.htm
- GSK, 2015-07-29: GSK Q2 2015 and half-year results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119163815000956/gsk201507296k.htm
- GSK, 2015-10-28: GSK Q3 2015 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119163815001276/gsk201510286k.htm
- GSK, 2016-02-03: GSK Q4 2015 and full-year results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119163816001631/gsk201602036k.htm
- GSK, 2016-04-27: GSK Q1 2016 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000119163816001998/gsk201604276k.htm
- GSK, 2016-07-27: GSK Q2 2016 and half-year results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000165495416000982/a160727solxq2201627july_f000.htm
- GSK, 2016-10-26: GSK Q3 2016 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000165495416003093/q3201626oct_sefinal2000.htm
- GSK, 2017-02-08: GSK Q4 2016 and full-year results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000165495417000843/a3451w.htm
- GSK, 2017-04-26: GSK Q1 2017 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000165495417003652/a4004d.htm
- GSK, 2017-07-26: GSK Q2 2017 and half-year results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000165495417006671/a1411m.htm
- GSK, 2017-10-25: GSK Q3 2017 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000165495417009667/a3qresults.htm
- GSK, 2018-02-07: GSK Q4 2017 and full-year results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000165495418001174/a2006e.htm
- GSK, 2018-04-25: GSK Q1 2018 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000165495418004348/a25-042018v4.htm
- GSK, 2018-07-25: GSK Q2 2018 and half-year results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000165495418008015/a7337v.htm
- GSK, 2018-10-31: GSK Q3 2018 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000165495418011770/a8811f.htm
- GSK, 2019-02-06: GSK Q4 2018 and full-year results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000165495419001110/a2711pfr.htm
- GSK, 2019-05-01: GSK Q1 2019 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000165495419005118/a7578x.htm
- GSK, 2019-07-24: GSK Q2 2019 and half-year results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000165495419008468/a5920g.htm
- GSK, 2019-10-30: GSK Q3 2019 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000165495419012095/a6482r.htm
- GSK, 2020-02-05: GSK Q4 2019 and full-year results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000165495420001122/a0670c.htm
- GSK, 2020-04-29: GSK Q1 2020 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000165495420004610/a3184l.htm
- GSK, 2020-07-29: GSK Q2 2020 and half-year results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000165495420008105/a4934u.htm
- GSK, 2020-10-28: GSK Q3 2020 results (6-K) - https://www.sec.gov/Archives/edgar/data/1131399/000165495420011516/a4952d.htm
- Human Genome Sciences, 2011-04-29: Human Genome Sciences Q1 2011 Form 10-Q (no amount; cited in the derived Q1 2011 row) - https://www.sec.gov/Archives/edgar/data/901219/000095012311042007/c15446e10vq.htm
- Human Genome Sciences, 2011-07-28: Human Genome Sciences Q2 2011 Form 10-Q - https://www.sec.gov/Archives/edgar/data/901219/000119312511199223/d10q.htm
- Human Genome Sciences, 2011-10-28: Human Genome Sciences Q3 2011 Form 10-Q - https://www.sec.gov/Archives/edgar/data/901219/000119312511285088/d219381d10q.htm
- Human Genome Sciences, 2012-02-27: Human Genome Sciences Q4 and full-year 2011 earnings release (8-K Exhibit 99) - https://www.sec.gov/Archives/edgar/data/901219/000119312512081721/d307118dex99.htm
- Human Genome Sciences, 2012-04-26: Human Genome Sciences Q1 2012 Form 10-Q - https://www.sec.gov/Archives/edgar/data/901219/000119312512182654/d311838d10q.htm
- Human Genome Sciences, 2012-07-26: Human Genome Sciences Q2 2012 Form 10-Q - https://www.sec.gov/Archives/edgar/data/901219/000119312512316881/d353751d10q.htm

Other documents opened:

- AstraZeneca FY and Q4 2017 results (checked for Fasenra; none printed): https://www.sec.gov/Archives/edgar/data/901832/000165495418001029/azn.htm
- AstraZeneca Fasenra US approval press release (6-K, 14 Nov 2017): https://www.sec.gov/Archives/edgar/data/901832/000165495417010682/a5116w.htm
- AstraZeneca Saphnelo US approval press release (6-K, 2 Aug 2021): https://www.sec.gov/Archives/edgar/data/901832/000165495421008378/a2087h.htm
- AstraZeneca Tezspire US approval press release (6-K, 20 Dec 2021): https://www.sec.gov/Archives/edgar/data/901832/000165495421013320/a1228w.htm
- GSK Nucala US approval press release (6-K, 4 Nov 2015): https://www.sec.gov/Archives/edgar/data/1131399/000119163815001329/gsk201511046k.htm
- GSK 2015 Annual Report (Form 20-F exhibit; Nucala 2015 total, Benlysta FY 2014 restated split): https://www.sec.gov/Archives/edgar/data/1131399/000119312516510261/d32974dex152.htm
- HGS/GSK Benlysta FDA approval press release (HGS 8-K, 9 Mar 2011): https://www.sec.gov/Archives/edgar/data/901219/000095012311023782/c13929exv99.htm
- HGS Q1 2011 Form 10-Q (filed 2011-04-29; first Benlysta sales, no amount): https://www.sec.gov/Archives/edgar/data/901219/000095012311042007/c15446e10vq.htm
- HGS Q2 2011 earnings release (8-K Exhibit 99, 2011-07-21): https://www.sec.gov/Archives/edgar/data/901219/000095012311067183/c20107exv99.htm
- HGS Q3 2011 earnings release (8-K Exhibit 99, 2011-10-25): https://www.sec.gov/Archives/edgar/data/901219/000095012311091756/c23638exv99.htm
- HGS 2011 Form 10-K (FY 2011 Benlysta $52.3m): https://www.sec.gov/Archives/edgar/data/901219/000119312512085140/d258554d10k.htm
- HGS Q1 2012 earnings release (8-K Exhibit 99.1): https://www.sec.gov/Archives/edgar/data/901219/000119312512178832/d339062dex991.htm
- GSK Q1 2011 results (6-K; no Benlysta figure): https://www.sec.gov/Archives/edgar/data/1131399/000095012311039933/u11011e6vk.htm
- GSK FY 2011 results (6-K; Benlysta FY 2011 GBP 15m): https://www.sec.gov/Archives/edgar/data/1131399/000119312512043398/d286391d6k.htm
- Amgen Q4 2021 earnings release (no Tezspire line): https://www.sec.gov/Archives/edgar/data/318154/000031815422000005/amgenq42021earningsrelease.htm
- FDA approval letter, Saphnelo BLA 761123: https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2021/761123Orig1s000ltr.pdf
- FDA approval letter, Tezspire BLA 761224: https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2021/761224Orig1s000ltr.pdf
- Drugs@FDA records via openFDA (approval and supplement dates): https://api.fda.gov/drug/drugsfda.json?search=application_number:BLA761070 (also BLA761123, BLA761224, BLA761451, BLA125526, BLA761122, BLA125370, BLA761043)
- Current FDA labels via openFDA (indications, dosing): https://api.fda.gov/drug/label.json?search=openfda.brand_name:%22FASENRA%22 (and SAPHNELO, TEZSPIRE, NUCALA, BENLYSTA)
