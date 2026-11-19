# J&J group (Stelara, Simponi, Tremfya): collection notes

Collected 2026-11-19. Reporting company for all three drugs: Johnson & Johnson (CIK 200406, from
https://www.sec.gov/files/company_tickers.json). All values are US dollars, millions, as printed in J&J's quarterly
earnings 8-K sales schedules (Exhibit 99.2O to Q2 2019, Exhibit 99.2 from Q3 2019). J&J prints three lines per
product: US, Intl (recorded as `ExUS`) and WW (recorded as `World`).

## Rows written

- `jnj_sales.csv`: 192 rows (3 regions per quarter). Stelara 2009Q1 to 2014Q3 (69 rows), Simponi 2009Q2 to
  2014Q2 (63 rows), Tremfya 2017Q3 to 2022Q2 (60 rows).
- Blank (not found) quarters: Stelara 2009Q1, 2009Q2, 2009Q3, 2009Q4; Simponi
  2009Q2, 2009Q3, 2009Q4; Tremfya none.
- `jnj_launches.csv`: 3 rows.

## What a reader must know

1. **Stelara and Simponi 2009 are missing, and so is the US launch quarter.** J&J did not print a STELARA or SIMPONI
   line in any 2009 or 2010 quarterly report; both sat inside "Other" pharmaceutical sales. The Q4 2010 report
   (2011-01-25) gives only a footnote: "Includes December YTD 2010 sales of $393MM for STELARA and $226MM for SIMPONI."
   The 2010 quarters in the data are the prior-year comparatives printed in the 2011 quarterly reports, the first time
   J&J printed those quarters. Nothing printed covers 2009. Checked: Q1, Q2 and Q3 2009 earnings 8-Ks on EDGAR
   (accessions 0000200406-09-000063, -09-000086, -09-000116: press release and sales schedules), the Q4 2009 earnings
   8-K Exhibit 99.2O (filed 2010-01-26; product list Aciphex to Velcade plus Other, Prezista and Invega under "major new
   products"), the FY2009 annual report (10-K Exhibit 13, filed 2010-03-01; Stelara and Simponi named only as 2009
   approvals; "Other Pharmaceutical sales were $7.6 billion"), the FY2010 annual report (10-K Exhibit 13), the Q2 and Q3
   2009 10-Qs and the 2010 10-Qs (product names only, no figures), and a web search (no company document with 2009
   figures). `first_quarter_with_us_sales` is therefore left blank for both drugs; see the launches file for the
   candidate quarters (Stelara 2009Q3 or 2009Q4; Simponi 2009Q2 or later). Because of that uncertainty the Stelara
   rows run to 2014Q3 and the Simponi rows to 2014Q2, one quarter past the earliest-launch reading of quarter 20.
2. **Tremfya 2017Q3 is derived, not printed.** J&J printed no TREMFYA line in its Q3 2017 to Q3 2018 reports. The Q4
   2018 report (2019-01-22) first printed it, with a "Pharmaceutical Supplemental Schedule" giving full-year 2017
   (US 62, Intl 1, WW 63) and 2018 Q1 to Q4, and prior-year Q4 2017 comparatives (US 46, Intl 1, WW 47). 2017Q3 =
   full year minus Q4 = US 16, ExUS 0, World 16 (`method` = `derived_other`). This holds only because there were no
   sales before the 2017-07-13 FDA approval, which fell in J&J fiscal Q3 2017. Inputs are rounded to $1MM, so the
   derived ExUS 0 means "about zero". As corroboration only, the Q3 2017 report prints an unlabelled OTHER IMMUNOLOGY
   line with US 16 (prior year nil), and the OTHER IMMUNOLOGY US figures in the Q4 2017 to Q3 2018 reports (46, 66,
   102, 143) equal the later TREMFYA US figures. 2017Q4 comes from the Q4 2018 comparatives and 2018Q1 to Q3 from the
   supplemental schedule; the Q1 to Q3 2019 comparatives match.
3. **Simponi's ExUS line is not end-market sales.** Under the distribution agreements, Schering-Plough (later part of
   Merck) distributed SIMPONI and REMICADE outside the US, Japan, Taiwan, Indonesia and China/Hong Kong. J&J's
   2011-04-15 release says its 2010 SIMPONI sales of $226 million included sales to distribution partner Merck. Under
   the 2011-04-15 settlement, J&J began recording sales in Canada, Central and South America, the Middle East, Africa
   and Asia Pacific from 2011-07-01; Merck kept Europe, Russia and Turkey (Merck's own sales there are not in J&J's
   numbers; contribution income split 50/50 from 2011-07-01 to 2024-10-01). Mitsubishi Tanabe holds licensed
   distribution rights in Japan, Indonesia and Taiwan. The printed ExUS figure is volatile around the change (2011:
   Q1 42, Q2 6, Q3 70, Q4 57). Do not read Simponi `ExUS` or `World` as global end-user sales.
4. **Simponi label changes.** `SIMPONI` from 2011Q1 to 2013Q4 (and as the label on the 2010 comparatives);
   `SIMPONI/SIMPONI ARIA` from the Q1 2014 report; `SIMPONI / SIMPONI ARIA` (spaces only) from the Q1 2015 report.
   SIMPONI ARIA (IV) was FDA-approved 2013-07-18, but the Q3 and Q4 2013 reports still print `SIMPONI`. The later
   combined-label comparatives for 2013 (Q1 2014 report: Q1 2013 = 94/143/237; FY2014 report: 2013 = 932) equal the
   earlier SIMPONI figures, so no restatement was made; the documents do not say whether the Q3 to Q4 2013 SIMPONI line
   already contained SIMPONI ARIA sales.
5. **Fiscal calendar.** J&J's fiscal year ends on the Sunday nearest 31 December and its quarters are 13-week periods
   (for example fiscal Q3 2009 ended 2009-09-27, fiscal Q3 2017 ended 2017-10-01). Fiscal quarters are recorded as the
   matching calendar quarter. Fiscal 2009 and fiscal 2020 had 53 weeks (per the 10-Ks), so one quarter in each of those
   years has an extra week; the 10-Ks do not say which quarter in the passages read.
6. **US + Intl does not always equal WW.** J&J rounds each line separately. Quarters where the printed lines differ by
   1: Tremfya 2020Q4 (276 + 105 vs 382), 2021Q1 (274 + 143 vs 418), 2021Q2 (325 + 155 vs 479), 2022Q2 (382 + 214 vs
   597). These are flagged in the `World` row notes.
7. **2011 presentation.** In the 2011 reports both products appear under "MAJOR NEW PHARMACEUTICAL PRODUCTS (Included in
   Other)"; from Q1 2012 they appear under Pharmaceutical segment, IMMUNOLOGY. In the Q3 2011 report the nine-month
   product table is headed "THIRD QUARTER" by mistake (its values are nine-month totals); the quarter table was used.

## Restatements

Each quarter from 2011Q1 on (Stelara, Simponi) and from 2018Q4 on (Tremfya) was compared with the prior-year
comparative printed in the following year's report for the same quarter (through the Q3 2015 report and the Q2 2023
report). Number of differences found: 0. The 2018Q1 to 2018Q3 Tremfya figures from the Q4 2018
supplemental schedule also match the 2019 comparatives. The 2010 quarters are themselves comparatives (first printed in
2011), so they have no earlier figure to compare with.

## Full-year checks

Sum of the four quarters in the file versus the printed twelve-month figure (Q4 earnings release, TWELVE MONTHS
table). 2010 uses the prior-year column of the Q4 2011 release; it also matches the FY2010 footnote in the Q4 2010
release (WW 393 Stelara, 226 Simponi). Partial years (Stelara and Simponi 2009 and 2014; Tremfya 2017 and 2022) are
not checked; Tremfya 2017Q3 + 2017Q4 equals full-year 2017 by construction.

| Drug, year | Region | Q1 + Q2 + Q3 + Q4 | Sum | Printed full year | Difference | Printed in |
|---|---|---|---|---|---|---|
| Stelara 2010 | US | 56 + 49 + 62 + 73 | 240 | 240 | 0 | Q4 2011 report, TWELVE MONTHS table, prior-year column |
| Stelara 2010 | ExUS | 31 + 37 + 38 + 47 | 153 | 153 | 0 | Q4 2011 report, TWELVE MONTHS table, prior-year column |
| Stelara 2010 | World | 87 + 86 + 100 + 120 | 393 | 393 | 0 | Q4 2011 report, TWELVE MONTHS table, prior-year column |
| Stelara 2011 | US | 105 + 100 + 112 + 126 | 443 | 443 | 0 | Q4 2011 report, TWELVE MONTHS table |
| Stelara 2011 | ExUS | 61 + 76 + 77 + 81 | 295 | 295 | 0 | Q4 2011 report, TWELVE MONTHS table |
| Stelara 2011 | World | 166 + 176 + 189 + 207 | 738 | 738 | 0 | Q4 2011 report, TWELVE MONTHS table |
| Stelara 2012 | US | 129 + 152 + 188 + 158 | 627 | 627 | 0 | Q4 2012 report, TWELVE MONTHS table |
| Stelara 2012 | ExUS | 92 + 96 + 99 + 111 | 398 | 398 | 0 | Q4 2012 report, TWELVE MONTHS table |
| Stelara 2012 | World | 221 + 248 + 287 + 269 | 1025 | 1025 | 0 | Q4 2012 report, TWELVE MONTHS table |
| Stelara 2013 | US | 226 + 233 + 233 + 265 | 957 | 957 | 0 | Q4 2013 report, TWELVE MONTHS table |
| Stelara 2013 | ExUS | 120 + 138 + 137 + 152 | 547 | 547 | 0 | Q4 2013 report, TWELVE MONTHS table |
| Stelara 2013 | World | 346 + 371 + 370 + 417 | 1504 | 1504 | 0 | Q4 2013 report, TWELVE MONTHS table |
| Simponi 2010 | US | 39 + 47 + 51 + 56 | 193 | 193 | 0 | Q4 2011 report, TWELVE MONTHS table, prior-year column |
| Simponi 2010 | ExUS | 3 + 12 + 9 + 9 | 33 | 33 | 0 | Q4 2011 report, TWELVE MONTHS table, prior-year column |
| Simponi 2010 | World | 42 + 59 + 60 + 65 | 226 | 226 | 0 | Q4 2011 report, TWELVE MONTHS table, prior-year column |
| Simponi 2011 | US | 53 + 61 + 59 + 62 | 235 | 235 | 0 | Q4 2011 report, TWELVE MONTHS table |
| Simponi 2011 | ExUS | 42 + 6 + 70 + 57 | 175 | 175 | 0 | Q4 2011 report, TWELVE MONTHS table |
| Simponi 2011 | World | 95 + 67 + 129 + 119 | 410 | 410 | 0 | Q4 2011 report, TWELVE MONTHS table |
| Simponi 2012 | US | 64 + 63 + 93 + 72 | 292 | 292 | 0 | Q4 2012 report, TWELVE MONTHS table |
| Simponi 2012 | ExUS | 52 + 62 + 92 + 109 | 315 | 315 | 0 | Q4 2012 report, TWELVE MONTHS table |
| Simponi 2012 | World | 116 + 125 + 185 + 181 | 607 | 607 | 0 | Q4 2012 report, TWELVE MONTHS table |
| Simponi 2013 | US | 94 + 87 + 111 + 112 | 404 | 404 | 0 | Q4 2013 report, TWELVE MONTHS table |
| Simponi 2013 | ExUS | 143 + 88 + 155 + 142 | 528 | 528 | 0 | Q4 2013 report, TWELVE MONTHS table |
| Simponi 2013 | World | 237 + 175 + 266 + 254 | 932 | 932 | 0 | Q4 2013 report, TWELVE MONTHS table |
| Tremfya 2018 | US | 66 + 102 + 143 + 142 | 453 | 453 | 0 | Q4 2018 report, TWELVE MONTHS table |
| Tremfya 2018 | ExUS | 6 + 24 + 28 + 33 | 91 | 91 | 0 | Q4 2018 report, TWELVE MONTHS table |
| Tremfya 2018 | World | 72 + 126 + 171 + 175 | 544 | 544 | 0 | Q4 2018 report, TWELVE MONTHS table |
| Tremfya 2019 | US | 168 + 176 + 221 + 199 | 764 | 764 | 0 | Q4 2019 report, TWELVE MONTHS table |
| Tremfya 2019 | ExUS | 49 + 59 + 69 + 71 | 248 | 248 | 0 | Q4 2019 report, TWELVE MONTHS table |
| Tremfya 2019 | World | 217 + 235 + 290 + 270 | 1012 | 1012 | 0 | Q4 2019 report, TWELVE MONTHS table |
| Tremfya 2020 | US | 187 + 241 + 222 + 276 | 926 | 926 | 0 | Q4 2020 report, TWELVE MONTHS table |
| Tremfya 2020 | ExUS | 109 + 101 + 105 + 105 | 420 | 421 | -1 | Q4 2020 report, TWELVE MONTHS table |
| Tremfya 2020 | World | 296 + 342 + 327 + 382 | 1347 | 1347 | 0 | Q4 2020 report, TWELVE MONTHS table |
| Tremfya 2021 | US | 274 + 325 + 376 + 528 | 1503 | 1503 | 0 | Q4 2021 report, TWELVE MONTHS table |
| Tremfya 2021 | ExUS | 143 + 155 + 161 + 165 | 624 | 624 | 0 | Q4 2021 report, TWELVE MONTHS table |
| Tremfya 2021 | World | 418 + 479 + 537 + 693 | 2127 | 2127 | 0 | Q4 2021 report, TWELVE MONTHS table |

The only difference is Tremfya 2020 ExUS (420 vs 421), a rounding difference of 1.

## Launch facts

From FDA documents on Drugs@FDA (accessdata.fda.gov): approval letters for BLA 125261 (Stelara SC), 761044 (Stelara
IV), 125289 (Simponi), 125433 (Simponi Aria) and 761061 (Tremfya); the 2009 Stelara and Simponi labels, the 2013
Simponi UC and Simponi Aria labels, the 2016 and 2019 Stelara labels, and the 2017, 2024 and 2025 Tremfya labels; and the
Drugs@FDA overview pages for action dates. The Tremfya original approval letter's first pages are scanned images, so its
date comes from the Drugs@FDA overview (the 2025 pediatric letter also cites 2017-07-13). Distribution facts for Simponi
come from the FY2009 annual report and the 2011-04-15 8-K (Exhibits 99.1 and 99.2,
https://www.sec.gov/Archives/edgar/data/200406/000020040611000051/pressrelease1.htm and pressrelease2.htm).

## Documents relied on for sales figures

Local copies under `Biotech Vault\Source Documents\JNJ - Johnson & Johnson\SEC Filings` (read only; original URLs
from its manifest.csv). Every `source_url` in the sales file is one of these:

- 2011-04-19, Johnson & Johnson Q1 2011 earnings release, sales schedules (8-K Exhibit 99.2O): https://www.sec.gov/Archives/edgar/data/200406/000020040611000052/exhibit99202011.htm
- 2011-07-19, Johnson & Johnson Q2 2011 earnings release, sales schedules (8-K Exhibit 99.2O): https://www.sec.gov/Archives/edgar/data/200406/000020040611000091/ninetyninetwoo.htm
- 2011-10-18, Johnson & Johnson Q3 2011 earnings release, sales schedules (8-K Exhibit 99.2O): https://www.sec.gov/Archives/edgar/data/200406/000020040611000111/exhibit992o3rdqtr2011.htm
- 2012-01-24, Johnson & Johnson Q4 2011 earnings release, sales schedules (8-K Exhibit 99.2O): https://www.sec.gov/Archives/edgar/data/200406/000144530512000096/a4q20118-kexhibit992o.htm
- 2012-04-17, Johnson & Johnson Q1 2012 earnings release, sales schedules (8-K Exhibit 99.2O): https://www.sec.gov/Archives/edgar/data/200406/000020040612000061/a1q20128-kexhibit992o.htm
- 2012-07-17, Johnson & Johnson Q2 2012 earnings release, sales schedules (8-K Exhibit 99.2O): https://www.sec.gov/Archives/edgar/data/200406/000020040612000112/a2q20128kexhibit992o.htm
- 2012-10-16, Johnson & Johnson Q3 2012 earnings release, sales schedules (8-K Exhibit 99.2O): https://www.sec.gov/Archives/edgar/data/200406/000020040612000134/a3q20128kexhibit992o.htm
- 2013-01-22, Johnson & Johnson Q4 2012 earnings release, sales schedules (8-K Exhibit 99.2O): https://www.sec.gov/Archives/edgar/data/200406/000020040613000011/a4q20128kexhibit992o.htm
- 2013-04-16, Johnson & Johnson Q1 2013 earnings release, sales schedules (8-K Exhibit 99.2O): https://www.sec.gov/Archives/edgar/data/200406/000020040613000050/a1q20138kexhibit992o.htm
- 2013-07-16, Johnson & Johnson Q2 2013 earnings release, sales schedules (8-K Exhibit 99.2O): https://www.sec.gov/Archives/edgar/data/200406/000020040613000086/a2013q28kexhibit992o.htm
- 2013-10-15, Johnson & Johnson Q3 2013 earnings release, sales schedules (8-K Exhibit 99.2O): https://www.sec.gov/Archives/edgar/data/200406/000020040613000103/a2013q38kexhibit992o.htm
- 2014-01-21, Johnson & Johnson Q4 2013 earnings release, sales schedules (8-K Exhibit 99.2O): https://www.sec.gov/Archives/edgar/data/200406/000020040614000010/a4q20138kexhibit992o.htm
- 2014-04-15, Johnson & Johnson Q1 2014 earnings release, sales schedules (8-K Exhibit 99.2O): https://www.sec.gov/Archives/edgar/data/200406/000020040614000042/a1q20148kexhibit992o.htm
- 2014-07-15, Johnson & Johnson Q2 2014 earnings release, sales schedules (8-K Exhibit 99.2O): https://www.sec.gov/Archives/edgar/data/200406/000020040614000084/a2014q28kexhibit992o.htm
- 2014-10-14, Johnson & Johnson Q3 2014 earnings release, sales schedules (8-K Exhibit 99.2O): https://www.sec.gov/Archives/edgar/data/200406/000020040614000095/a2014q38kexhibit992o.htm
- 2019-01-22, Johnson & Johnson Q4 2018 earnings release, sales schedules (8-K Exhibit 99.2O): https://www.sec.gov/Archives/edgar/data/200406/000020040619000004/a2018q4exhibit992o.htm
- 2019-04-16, Johnson & Johnson Q1 2019 earnings release, sales schedules (8-K Exhibit 99.2O): https://www.sec.gov/Archives/edgar/data/200406/000020040619000025/a2019q1exhibit992o.htm
- 2019-07-16, Johnson & Johnson Q2 2019 earnings release, sales schedules (8-K Exhibit 99.2O): https://www.sec.gov/Archives/edgar/data/200406/000020040619000049/a2019q2exhibit992o.htm
- 2019-10-15, Johnson & Johnson Q3 2019 earnings release, sales schedules (8-K Exhibit 99.2): https://www.sec.gov/Archives/edgar/data/200406/000020040619000061/a2019q3exhibit992.htm
- 2020-01-22, Johnson & Johnson Q4 2019 earnings release, sales schedules (8-K Exhibit 99.2): https://www.sec.gov/Archives/edgar/data/200406/000020040620000004/a2019q4exhibit992.htm
- 2020-04-14, Johnson & Johnson Q1 2020 earnings release, sales schedules (8-K Exhibit 99.2): https://www.sec.gov/Archives/edgar/data/200406/000020040620000026/a2020q1exhibit992.htm
- 2020-07-16, Johnson & Johnson Q2 2020 earnings release, sales schedules (8-K Exhibit 99.2): https://www.sec.gov/Archives/edgar/data/200406/000020040620000047/a2020q2exhibit992.htm
- 2020-10-13, Johnson & Johnson Q3 2020 earnings release, sales schedules (8-K Exhibit 99.2): https://www.sec.gov/Archives/edgar/data/200406/000020040620000054/a2020q3exhibit992.htm
- 2021-01-26, Johnson & Johnson Q4 2020 earnings release, sales schedules (8-K Exhibit 99.2): https://www.sec.gov/Archives/edgar/data/200406/000020040621000006/a2020q4exhibit992.htm
- 2021-04-20, Johnson & Johnson Q1 2021 earnings release, sales schedules (8-K Exhibit 99.2): https://www.sec.gov/Archives/edgar/data/200406/000020040621000024/a2021q1exhibit992final.htm
- 2021-07-21, Johnson & Johnson Q2 2021 earnings release, sales schedules (8-K Exhibit 99.2): https://www.sec.gov/Archives/edgar/data/200406/000020040621000053/a2021q2exhibit992final.htm
- 2021-10-19, Johnson & Johnson Q3 2021 earnings release, sales schedules (8-K Exhibit 99.2): https://www.sec.gov/Archives/edgar/data/200406/000020040621000067/a2021q3exhibit992.htm
- 2022-01-25, Johnson & Johnson Q4 2021 earnings release, sales schedules (8-K Exhibit 99.2): https://www.sec.gov/Archives/edgar/data/200406/000020040622000012/a2021q4exhibit992.htm
- 2022-04-19, Johnson & Johnson Q1 2022 earnings release, sales schedules (8-K Exhibit 99.2): https://www.sec.gov/Archives/edgar/data/200406/000020040622000038/a2022q1exhibit992.htm
- 2022-07-19, Johnson & Johnson Q2 2022 earnings release, sales schedules (8-K Exhibit 99.2): https://www.sec.gov/Archives/edgar/data/200406/000020040622000063/a2022q2exhibit992.htm

Also opened (no product figures, used for "not found" and context): 2009 Q1 to Q3 earnings 8-K exhibits
(https://www.sec.gov/Archives/edgar/data/200406/000020040609000063/firstqtrt99202009.htm,
https://www.sec.gov/Archives/edgar/data/200406/000020040609000086/financials.htm,
https://www.sec.gov/Archives/edgar/data/200406/000020040609000116/exhibi99203q2009.htm and the press-release exhibits),
Q4 2009 earnings 8-K Exhibit 99.2O (https://www.sec.gov/Archives/edgar/data/200406/000020040610000006/exhibi99204q2010.htm), 2010 Q1 to Q3 exhibits
(https://www.sec.gov/Archives/edgar/data/200406/000020040610000047/firstq20108k9920.htm, https://www.sec.gov/Archives/edgar/data/200406/000020040610000068/exhibit992o.htm,
https://www.sec.gov/Archives/edgar/data/200406/000020040610000097/thirdqtr99202010.htm), Q4 2010 exhibit (https://www.sec.gov/Archives/edgar/data/200406/000020040611000017/exhibit99152o4thqtr2010.htm),
Q3 2017 to Q3 2018 exhibits (https://www.sec.gov/Archives/edgar/data/200406/000020040617000050/a8k2017q3exhibit992o.htm and the next four), FY2009 and FY2010
annual reports (https://www.sec.gov/Archives/edgar/data/200406/000095012310019392/y80744exv13.htm,
https://www.sec.gov/Archives/edgar/data/200406/000095012311018128/y86310kexv13.htm), FY2013 annual report
(https://www.sec.gov/Archives/edgar/data/200406/000020040614000033/ex13-form10xk20131229.htm), 2009 Q2 and Q3 10-Qs.
