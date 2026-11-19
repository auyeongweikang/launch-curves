# sanofi_roche: collection notes

Group: Dupixent (dupilumab) and Kevzara (sarilumab), reported by Sanofi in EUR; Actemra/RoActemra (tocilizumab), reported by Roche in CHF.
Collected 2026-11-19. Every value in `sanofi_roche_sales.csv` was read from the document named in its row.

## Overview

| Drug | Window (calendar quarters) | Quarter 1 (first US sales) | Rows | Blank values |
|---|---|---|---|---|
| Dupixent | 2017Q2 to 2022Q1 | 2017Q2 | 91 | none |
| Kevzara | 2017Q2 to 2022Q1 | 2017Q2 | 91 | none |
| Actemra | 2009Q1 to 2014Q4 | 2010Q1 | 116 (114 quarter rows, 2 FY 2009 rows) | 2009Q1 and 2009Q2 (World, US): not found; 2009Q3 and 2009Q4 US: printed as "-" |

Total: 298 sales rows, 3 launch rows.

## Dupixent and Kevzara (Sanofi)

**Source.** Sanofi's quarterly results press releases, filed on EDGAR as 6-K Exhibit 99.1 (Q1 2019: Exhibit 99.4). Every quarter comes from that quarter's own release (first reported), Appendix 1 table "net sales by GBU, franchise, geographic region and product", row "Dupixent" or "Kevzara". The figures are EUR millions as printed. `source_date` is the release date printed on the release, which is the filing date or up to three days before it.

**Start of the window.** The Q1 2017 release (6-K filed 2017-05-01, https://www.sec.gov/Archives/edgar/data/1121404/000119312517150279/d380206dex991.htm) has no Dupixent or Kevzara line in Appendix 1. In the Q2 2017 release the H1 2017 table prints the same figures as Q2 (Dupixent 26, Kevzara 1). Q2 2017 is therefore both the first quarter with reported sales and quarter 1 for both drugs. Quarter 20 is Q1 2022.

**Region layout changes in 2020.**
- **2017 to 2019.** The columns are Total GBUs, Europe, United States, Rest of the World, Emerging Markets and Total Franchises.
  - Rest of the World excludes Emerging Markets, which have their own column.
  - Emerging Markets are defined in Sanofi's footnote as the world excluding the U.S., Canada, Western & Eastern Europe (except Eurasia), Japan, South Korea, Australia, New Zealand and Puerto Rico.
  - Rows recorded: `World` = Total Franchises, `US`, `Other:Europe`, `Other:Rest of the World`, `Other:Emerging Markets`. Total Franchises equals the sum of the four regions in every quarter.
- **Total GBUs is not recorded.** It excludes Emerging Markets (a separate GBU at the time), so it is lower whenever EM sales are non-zero. The cases are:
  - Dupixent: 2018Q2 175 vs 176, 2018Q3 223 vs 225, 2018Q4 278 vs 280, 2019Q1 326 vs 329, 2019Q2 490 vs 496, 2019Q3 561 vs 570, 2019Q4 668 vs 679.
  - Kevzara: 2019Q2 51 vs 52, 2019Q4 53 vs 54.
  - Each World row's notes give the Total GBUs value.
- **From Q1 2020.** The columns are Total Sales, United States, Europe and Rest of the world, which now includes the former Emerging Markets. Rows recorded: `World`, `US`, `Other:Europe`, `Other:Rest of the world`.
- **Breaks in the series.** `Other:Rest of the World` (2017 to 2019) and `Other:Rest of the world` (2020 on) cover different areas and are labelled differently on purpose. `World`, `US` and `Other:Europe` are continuous.

**These are product net sales, not alliance revenue.** Sanofi's text calls both drugs "(collaboration with Regeneron)", but the Appendix 1 figures are Sanofi's net sales of the products. Regeneron's Q1 2022 release (footnote b) says: "Sanofi records global net product sales of Dupixent and Kevzara. The Company records its share of profits/losses in connection with global sales of Dupixent and Kevzara."

**What Regeneron prints (USD; kept out of the data).** Regeneron's own revenue line is "Sanofi collaboration revenue". It holds Regeneron's share of collaboration profits plus reimbursements, and covers more than these two drugs. Regeneron also prints Sanofi-recorded sales in USD as information:

| Regeneron 8-K Exhibit 99.1 | Table | Dupixent | Kevzara |
|---|---|---|---|
| Q4 2017 ([link](https://www.sec.gov/Archives/edgar/data/872589/000153217618000010/exhibit991q42017.htm)) | "Global net product sales recorded by Sanofi" | Q4 2017 $139m; FY 2017 $256m | Q4 2017 $9m; FY 2017 $13m |
| Q4 2019 ([link](https://www.sec.gov/Archives/edgar/data/872589/000153217620000005/exhibit991q42019.htm)) | "Net product sales recorded by Sanofi", US / ROW / Total | Q4 2019 $605.2m / $146.3m / $751.5m; FY 2019 $1,871.2m / $444.4m / $2,315.6m | Q4 2019 $37.6m / $22.1m / $59.7m |
| Q1 2022 ([link](https://www.sec.gov/Archives/edgar/data/872589/000180422022000013/exhibit991q12022.htm)) | US / ROW / Total | $1,325.6m / $484.8m / $1,810.4m | $57.0m / $49.4m / $106.4m |

The "Total Sanofi collaboration revenue" line in the same releases is Q4 2017 $199.5m (FY 2017 $877.2m), Q4 2019 $427.1m (FY 2019 $1,426.8m) and Q1 2022 $630.9m. Regeneron's US-dollar figures are translations of Sanofi's sales and must not be mixed with the EUR series.

**Ownership.**
- **Kevzara.** Sanofi's Q4 2019 release says Sanofi and Regeneron announced in December 2019 an intent to restructure the Kevzara arrangement, with Sanofi expected to gain sole global rights. I did not open a document confirming completion. Either way, Sanofi records Kevzara's global net sales throughout the window, so the recording company does not change.
- **Dupixent.** No change in recording company in the window. Drugs@FDA lists Regeneron Pharmaceuticals as the BLA 761055 holder.

**Restatements.** I took each quarter from its own release. I did not compare every later comparative column for restatements. The full-year tables in the Q4 releases equal the sum of the first-reported quarters in every region (see below).

## Actemra/RoActemra (Roche)

**Sources.** Roche is not an SEC filer, and its pre-2015 results documents are no longer on roche.com (old URLs return 403/404). The quarterly figures come from copies of Roche's own PDFs held by the Internet Archive's Wayback Machine. `source_url` is the archived copy of the original roche.com file. The documents used are the tables appendices to the sales and results releases (`mr…ane.pdf`), the investor updates (`inv-update-….pdf`) and the Finance Reports 2009 and 2014. The FY 2011 tables are also on EDGAR. Roche's FY 2011 results were filed under Illumina's CIK as form DFAN14A on 2012-02-02: https://www.sec.gov/Archives/edgar/data/1110803/000095010312000524/dp28491_dfan14a-q4.htm

**Start of the window: the first period Roche reports.**
- **Before 2009.** The Finance Report 2008 mentions the Actemra/RoActemra launch but prints no sales.
- **First half of 2009.** None of these print a figure:
  - the HY 2009 tables appendix (mr2q09ane): no Actemra row;
  - the Half-Year Report 2009 (hy09e): text only, no figure;
  - the 9M 2009 and FY 2009 appendices: no Actemra row in their Top 20 tables.
- **First figure: FY 2009.** The first Roche figure is in the Finance Report 2009, page 10, in text: "Global sales rose 289% to 146 million Swiss francs" and "Sales in Japan amounted to 98 million Swiss francs". These are recorded as two `period_type=year` rows (calendar_quarter 2009Q4, World 146, Other:Japan 98).
- **Quarterly figures from Q3 2009.** They first appear as comparatives in the 9M 2010 appendix. The window therefore starts at 2009Q1. Q1 and Q2 2009 are blank ("not found"), because only the full year covers them.
- **Chugai's Japanese sales from 2005 to 2008 were not collected.**
- **First US quarter.** US approval was 2010-01-08 and first US sales are in Q1 2010 (CHF 5m), so Q1 2010 is quarter 1 and Q4 2014 is quarter 20. The US column prints "-" for Q3 and Q4 2009; those rows are left blank with a note rather than set to 0.

**Regions.**
- **2009 to 2012.** United States, Western Europe, Japan and International. International = Asia-Pacific, CEMAI (Central and Eastern Europe, Middle East, Africa, Central Asia, Indian Subcontinent), Latin America, Canada and Others.
- **From 2013.** Roche changed the layout to United States, Europe, Japan and International. International = Asia-Pacific, EEMEA (Eastern Europe, Middle East and Africa), Latin America, Canada and Others.
- **Recorded as.** `World` (Total), `US`, `Other:Western Europe` (to 2012Q4) or `Other:Europe` (from 2013Q1), `Other:Japan` and `Other:International`.
- **Break in the series.** "Europe" and "International" from 2013 are not comparable with "Western Europe" and "International" before 2013. In the FY 2013 investor update, Q4 2012 is restated as Europe 78 and International 36, against Western Europe 73 and International 41 as first reported. World, US and Japan are unchanged. The two restated values are in the notes of the Q4 2012 rows.
- **Japan.** Japan is Chugai's sales, consolidated in the Roche Group. The Finance Report 2009 shows Chugai non-controlling interests.

**Which document each quarter comes from.** Roche publishes Q1 and 9M sales releases and HY and FY results. Each tables appendix prints the last five quarters, so most quarters are printed for the quarter itself.
- **From the quarter's own document (first reported):**
  - Q3 2010: 9M 2010 appendix.
  - Q4 2010: FY 2010 appendix.
  - Q1 2011: Q1 2011 appendix.
  - Q2 2011: HY 2011 appendix.
  - Q4 2011: FY 2011 appendix.
  - Q3 2012: 9M 2012 investor update.
  - Q4 2012: FY 2012 appendix.
  - Q4 2013: FY 2013 investor update.
  - Q1 2014: Q1 2014 appendix.
  - Q2 2014: HY 2014 appendix.
  - Q3 2014: 9M 2014 appendix.
- **From the earliest later Roche document I could open**, because the quarter's own appendix is not archived or (for Q1 2010) has no Actemra row:
  - Q3 2009, Q4 2009, Q1 2010 and Q2 2010: 9M 2010 appendix (the Q1 2010 appendix has no Actemra row; the HY 2010 appendix was not found).
  - Q3 2011: FY 2011 appendix.
  - Q1 2012 and Q2 2012: 9M 2012 investor update.
  - Q1, Q2 and Q3 2013: FY 2013 investor update.
- **Comparing later printings.** Wherever a quarter is printed again in a later document I opened, the value is the same, apart from the 2013 regional restatement of Q4 2012. Each row's notes list the later documents compared.
- **Q4 2014: `derived_fy_minus_9m`.** No Q4 2014 table was found: there is no Wayback copy of the FY 2014 appendix (mrar14ane) or the Q1 2015 appendix, and the FY 2014 investor update copy has no tables. Q4 2014 = FY 2014 (Finance Report 2014, page 16, "Actemra/RoActemra regional sales") minus 9M 2014 (9M 2014 appendix, table 4):

  | Region | FY 2014 | 9M 2014 | Q4 2014 |
  |---|---|---|---|
  | World | 1,224 | 897 | 327 |
  | US | 406 | 292 | 114 |
  | Europe | 433 | 320 | 113 |
  | Japan | 214 | 156 | 58 |
  | International | 171 | 129 | 42 |

**Other cross-checks (all tie):**
- 9M 2010 YTD table: 262 / US 32 / Western Europe 97 / Japan 112 / International 21. This equals Q1 to Q3 2010 in every region.
- HY 2010 report: H1 2010 = 155 = 66 + 89.
- HY 2011 appendix YTD: 277 / 61 / 94 / 84 / 38. This equals Q1 + Q2 2011.
- 9M 2012 update YTD: 601 / 171 / 192 / 144 / 94. This equals Q1 to Q3 2012.
- HY 2013 report: H1 2013 = 496 = 238 + 258, and H1 2012 = 385 = 184 + 201.
- Q1 2014 YTD = Q1 2014.
- HY 2014 YTD: 568 / 180 / 207 / 100 / 81. This equals Q1 + Q2 2014.
- 9M 2014 YTD: 897 / 292 / 320 / 156 / 129. This equals Q1 to Q3 2014.

## Full-year checks (sum of the four quarters against the printed full-year figure)

### Sanofi (EUR m; printed totals from the full-year table in each Q4 release)

| Drug | Year | World | US | Europe | RoW | EM |
|---|---|---|---|---|---|---|
| Dupixent | 2017 (Q2 to Q4 only) | 219 / 219 / 0 | 216 / 216 / 0 | 2 / 2 / 0 | 1 / 1 / 0 | 0 / 0 / 0 |
| Dupixent | 2018 | 788 / 788 / 0 | 660 / 660 / 0 | 75 / 75 / 0 | 48 / 48 / 0 | 5 / 5 / 0 |
| Dupixent | 2019 | 2,074 / 2,074 / 0 | 1,669 / 1,669 / 0 | 200 / 200 / 0 | 176 / 176 / 0 | 29 / 29 / 0 |
| Dupixent | 2020 | 3,534 / 3,534 / 0 | 2,808 / 2,808 / 0 | 386 / 386 / 0 | 340 / 340 / 0 | n/a |
| Dupixent | 2021 | 5,249 / 5,249 / 0 | 3,971 / 3,971 / 0 | 649 / 649 / 0 | 629 / 629 / 0 | n/a |
| Kevzara | 2017 (Q2 to Q4 only) | 11 / 11 / 0 | 10 / 10 / 0 | 1 / 1 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| Kevzara | 2018 | 83 / 83 / 0 | 64 / 64 / 0 | 14 / 14 / 0 | 5 / 5 / 0 | 0 / 0 / 0 |
| Kevzara | 2019 | 185 / 185 / 0 | 115 / 115 / 0 | 43 / 43 / 0 | 25 / 25 / 0 | 2 / 2 / 0 |
| Kevzara | 2020 | 236 / 236 / 0 | 123 / 123 / 0 | 75 / 75 / 0 | 38 / 38 / 0 | n/a |
| Kevzara | 2021 | 287 / 287 / 0 | 135 / 135 / 0 | 102 / 102 / 0 | 50 / 50 / 0 | n/a |

Each cell reads sum of quarters / printed total / difference.
- **2017.** The printed total is the "2017 (€ million)" table in the Q4 2017 release. Q1 2017 had no sales line, so three quarters make up the year.
- **2020 and 2021.** RoW is "Rest of the world" in the new layout.
- **2022.** Only Q1 2022 is in the window, so there is no full-year check.

### Roche, Actemra/RoActemra (CHF m)

| Year | World | US | (W.) Europe | Japan | International | Printed total from |
|---|---|---|---|---|---|---|
| 2009 | 93 / 146 / -53 | not printed / n/a | n/a | 57 / 98 / -41 | n/a | Finance Report 2009 text (World and Japan only) |
| 2010 | 397 / 397 / 0 | 58 / 58 / 0 | 136 / 136 / 0 | 167 / 167 / 0 | 36 / 36 / 0 | FY 2010 appendix, table 4 |
| 2011 | 618 / 618 / 0 | 141 / 141 / 0 | 198 / 198 / 0 | 195 / 195 / 0 | 84 / 84 / 0 | FY 2011 appendix, table 7 |
| 2012 | 842 / 842 / 0 | 241 / 241 / 0 | 265 / 265 / 0 | 201 / 201 / 0 | 135 / 135 / 0 | FY 2012 appendix, table 6 |
| 2013 | 1,037 / 1,037 / 0 | 314 / 314 / 0 | 360 / 360 / 0 | 197 / 197 / 0 | 166 / 166 / 0 | FY 2013 investor update, table 4 |
| 2014 | 1,224 / 1,224 / 0 | 406 / 406 / 0 | 433 / 433 / 0 | 214 / 214 / 0 | 171 / 171 / 0 | Finance Report 2014, page 16 |

- **2009.** The sum covers Q3 and Q4 only, because Q1 and Q2 2009 are not printed. The difference is the unreported first half; it is not a discrepancy.
- **2014.** The check is circular because Q4 2014 is derived from the full year. Q1 to Q3 2014 were checked against the printed 9M 2014 YTD instead, with zero difference in every region.
- **2012 against 2013 regions.** 2012 uses the Western Europe layout and 2013 the Europe layout.

## Gaps

- **Actemra 2009Q1 and 2009Q2 (World, US): not found.** Documents tried:
  - Q1 2009 appendix: only a 404 page is archived.
  - HY 2009 appendix: no Actemra row.
  - Half-Year Report 2009: text only.
  - 9M 2009 and FY 2009 appendices: no Actemra row.
  - Finance Report 2008: no figure.
- **Actemra 2009Q3 and 2009Q4 US: blank.** Printed as "-" before the US approval.
- **Actemra appendices not found in the Wayback Machine:**
  - 2010: HY (mr2q10ane).
  - 2011: 9M (mr3q11ane).
  - 2012: Q1, HY and 9M appendices.
  - 2013: Q1, HY, 9M and FY appendices.
  - 2014: FY (mrar14ane).
  - 2015: Q1 (mr1q15ane) and FY (mrar15ane).
  The quarters these would have covered were taken from later Roche documents (see above) or, for Q4 2014, derived.
- **Dupixent and Kevzara: no gaps.**

## Documents relied on

Sanofi (EDGAR, CIK 1121404), results press releases. Each is 6-K Exhibit 99.1 except Q1 2019 (Exhibit 99.4). The accession folder and file are listed here; each full URL is in the `source_url` column.
- **Q1 2017** (start check only): 000119312517150279/d380206dex991.htm
- **2017:** Q2 000119312517242074/d431208dex991.htm; Q3 000119312517330595/d487336dex991.htm; Q4 000119312518034550/d528561dex991.htm
- **2018:** Q1 000119312518138290/d573546dex991.htm; Q2 000119312518232871/d451116dex991.htm; Q3 000119312518313798/d647789dex991.htm; Q4 000119312519030709/d713074dex991.htm
- **2019:** Q1 000119312519124231/d729228dex994.htm; Q2 000119312519205456/d756141dex991.htm; Q3 000119312519280117/d825523dex991.htm; Q4 000119312520026621/d860609dex991.htm
- **2020:** Q1 000119312520121046/d889738dex991.htm; Q2 000112140420000017/pressreleaseq22020engl.htm; Q3 000112140420000020/pressreleaseq32020engl.htm; Q4 000112140421000002/pressreleaseq42020english.htm
- **2021:** Q1 000112140421000006/pressreleaseq12021english.htm; Q2 000112140421000011/pressreleaseq22021english.htm; Q3 000112140421000017/pressreleaseq32021english.htm; Q4 000112140422000002/pressreleaseq42021english.htm
- **2022:** Q1 000112140422000009/pressreleaseq12022english.htm

Regeneron (EDGAR, CIK 872589), for these notes only: the Q4 2017, Q4 2019 and Q1 2022 8-K Exhibit 99.1 releases linked above.

Roche. All are Wayback Machine copies of roche.com files unless noted.
- **2009:** Finance Report 2009, http://web.archive.org/web/20110919164039/http://www.roche.com:80/ILINK/Download/annual_reports.htm/fb09e.pdf
- **2010:**
  - 9M 2010 appendix, http://web.archive.org/web/20101105202100/http://www.roche.com:80/mr3q10ane.pdf
  - FY 2010 appendix, http://web.archive.org/web/20220118110419/https://www.roche.com/dam/jcr:a7cff6be-f233-4983-a9be-47af962ca3a4/en/mrar10ane.pdf
- **2011:**
  - Q1 2011 appendix, http://web.archive.org/web/20110919170146/http://www.roche.com:80/mr1q11ane.pdf
  - HY 2011 appendix, http://web.archive.org/web/20111226102611/http://www.roche.com:80/mr2q11ane.pdf
  - FY 2011 appendix, http://web.archive.org/web/20121114204043/http://www.roche.com:80/mrar11ane.pdf (also on EDGAR, link above)
- **2012:**
  - 9M 2012 investor update, http://web.archive.org/web/20121030125211/http://www.roche.com:80/inv-update-2012-10-16-e.pdf
  - FY 2012 appendix, http://web.archive.org/web/20140422202644/http://www.roche.com:80/mrar12ane.pdf
- **2013:** FY 2013 investor update, http://web.archive.org/web/20160328000646/http://www.roche.com:80/inv-update-2014-01-30-e.pdf
- **2014:**
  - Q1 2014 appendix, http://web.archive.org/web/20140501214747/http://www.roche.com:80/mr1q14ane.pdf
  - HY 2014 appendix, http://web.archive.org/web/20141212200621/http://www.roche.com:80/mr2q14ane.pdf
  - 9M 2014 appendix, http://web.archive.org/web/20141212211729/http://www.roche.com:80/mr3q14ane.pdf
  - Finance Report 2014, http://web.archive.org/web/20160410131107/http://www.roche.com/fb14e.pdf. Source date set to the FY 2014 results date, 2015-01-28.
- **Cross-checks only:**
  - Half-Year Report 2010, https://assets.cwp.roche.com/f/126832/f796568dac/hy10e.pdf
  - Half-Year Report 2013, https://assets.cwp.roche.com/f/126832/141c31a4e1/hy13e.pdf
  - Half-Year Report 2009, http://web.archive.org/web/20110919105030/http://www.roche.com:80/ILINK/Download/annual_reports.htm/hy09e.pdf
  - Finance Report 2008, http://web.archive.org/web/20110919164034/http://www.roche.com:80/ILINK/Download/annual_reports.htm/fb08e.pdf
  - 2009 appendices mr2q09ane, mr3q09ane and mrar09ane
  - Q1 2010 appendix mr1q10ane

FDA (launch facts):
- Drugs@FDA overview pages for BLA 761055 (Dupixent), 761037 (Kevzara), 125276 and 125472 (Actemra).
- The approval letters named in `sanofi_roche_launches.csv`.
- The original labels, for mechanism and dosing.
