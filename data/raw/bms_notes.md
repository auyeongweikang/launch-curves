# BMS group: Orencia, Zeposia, Sotyktu

Collected 2026-11-19. Reporting company: Bristol Myers Squibb (EDGAR CIK 14272, taken from
https://www.sec.gov/files/company_tickers.json). All values are net product sales/revenues in USD
millions, exactly as printed in BMS quarterly earnings exhibits filed on Form 8-K. No local copies of
BMS SEC filings were found in the Biotech Vault (its BMY folder holds only trial records and Zeposia
regulatory files), so every sales figure comes from EDGAR.

## Coverage

| Drug | Window (quarter 1 = first quarter with US sales) | Quarters | Rows | Missing quarters |
|---|---|---|---|---|
| Orencia | 2006Q1 to 2010Q4 | 20 | 60 (US, ExUS, World) | none |
| Zeposia | 2020Q2 to 2025Q1 | 20 | 60 | none |
| Sotyktu | 2022Q3 to 2026Q3 | 17 | 51 | none; quarters 18 to 20 (2026Q4 to 2027Q2) not yet reported |

The first quarter with US sales was also the first quarter with sales anywhere for all three drugs.
- Orencia: the Q4 2005 release (8-K 2006-01-25) prints no Orencia sales and says Orencia was expected to
  be available in late February or early March 2006; the Q1 2006 release says it launched in February.
- Zeposia: the Q1 2020 release prints no Zeposia revenue row. The Q2 2020 release says the US commercial
  launch was announced in June 2020. Later trend tables print Q1 2020 as a dash.
- Sotyktu: approved 2022-09-09; the Q3 2022 release prints $1 million (US and worldwide).

## How BMS reports these products

1. **2006 to 2010 (Orencia).** Exhibit 99.1 (press release) has a "selected products" table with
   Worldwide Net Sales and U.S. Net Sales for the quarter. The supplemental exhibit (Ex 99.2; Ex 99.3 for
   Q2 2009, where Ex 99.2 is a slide deck) has quarterly trend tables headed Worldwide, Domestic and
   International net sales by product. Orencia is listed from its first quarter (under Immunoscience), so
   the early quarters are not missing. US and World rows come from Ex 99.1; ExUS rows come from the
   International trend table. The Ex 99.2 "Domestic" figures equal the Ex 99.1 U.S. figures in every quarter.
   Up to the Q3 2009 release, a footnote on the Domestic and International tables says total company sales
   are on a legal entity source basis and segment and product sales on a country management reported basis.
   For Orencia, US + International equals Worldwide in every quarter.
2. **2020 to 2022 (Zeposia, Sotyktu launch).** Ex 99.1 prints Worldwide and U.S. revenues (U.S. includes
   Puerto Rico, footnote). Ex 99.2 prints quarterly trend tables for Worldwide, U.S. and International
   revenues, plus "pro forma" versions (Celgene merger), which were not used. ExUS rows come from the
   International table.
3. **From Q1 2023.** The Ex 99.1 "Product Revenues" table prints U.S., Int'l and WW columns for the quarter
   and for the prior-year quarter. Ex 99.2 is now a slide presentation and was not used.
4. **Puerto Rico moves at 2024Q1 (a break in the US series).** Through 2023 Puerto Rico is in U.S. From the
   Q1 2024 release, the footnote reads "Beginning in 2024, Puerto Rico revenues are included in International
   revenues. Prior period amounts have been reclassified to conform to the current presentation." US
   figures for 2024 onward exclude Puerto Rico and are not on the same basis as earlier US figures. From the
   Q4 2025 release on, the Puerto Rico footnote is no longer printed, but the prior-year comparatives in those
   releases match the earlier figures, so the basis looks unchanged. That is not stated by the company.
5. **Rounding.** From 2025 the releases say totals may not sum due to rounding. US + ExUS can differ from
   World by 1 (for example Sotyktu Q1 2026: 35 + 33 vs 69). Record each region as printed and do not
   recompute World.
6. **Hedging.** The 2026 releases add an "Other Revenue" line for revenue hedging. It is separate from the
   product rows used here.
7. No collaboration or alliance accounting applies to these three products. All are BMS product sales.

## Zeros printed as dashes, and ExUS figures taken from later releases

A dash ("—") in a BMS revenue table is recorded as value 0, with a note in the row. Seven rows:
- Orencia ExUS 2006Q1, 2006Q2, 2006Q3: dash in the International trend table of each quarter's own release.
  First International sales: $1 million in 2006Q4.
- Zeposia ExUS 2020Q2 and 2020Q3: the Q2 and Q3 2020 releases have no Zeposia row in the International
  table. The Q4 2020 Ex 99.2 International trend table prints a dash for both quarters, and that is the cited
  source. First International revenue: $2 million in 2020Q4.
- Sotyktu ExUS 2022Q3 and 2022Q4: the 2022 releases have no Sotyktu row in the International table. The
  prior-year Int'l column in the Q3 2023 and Q4 2023 releases prints a dash, and those are the cited
  sources. First Int'l revenue: $1 million in 2023Q1.

These are the only rows whose source is a later release than the quarter itself.

## Restatements (later reports printing a different figure)

- **Orencia:** each 2006 to 2010 quarter was compared with the trend tables of every later release through
  Q1 2011. No differences.
- **Sotyktu:** compared with the prior-year columns of every later release through Q3 2026. No differences.
  The 2024 Puerto Rico reclassification did not change any Sotyktu 2023 figure.
- **Zeposia:** 2020 to 2022 figures match all later trend tables. The 2023 quarters were reclassified in the
  2024 releases because of the Puerto Rico change. World figures are unchanged. The rows keep the
  first-reported value and give the later value in `notes`:

| Quarter | US first reported | US in 2024 release | ExUS first reported | ExUS in 2024 release | Later source |
|---|---|---|---|---|---|
| 2023Q1 | 52 | 51 | 26 | 27 | Q1 2024 release (8-K 2024-04-25) |
| 2023Q2 | 75 | 73 | 25 | 27 | Q2 2024 release (8-K 2024-07-26) |
| 2023Q3 | 96 | 95 | 27 | 28 | Q3 2024 release (8-K 2024-10-31) |
| 2023Q4 | 101 | 100 | 32 | 33 | Q4 2024 release (8-K 2025-02-06) |

The FY2023 comparative in the Q4 2024 release is US 319, Int'l 115, WW 434 (first reported 324 / 110 / 434).

## Full-year checks (sum of my quarters vs printed full year, same region)

The printed full year comes from the Q4 release of that year. Ex 99.1 twelve-month table for US and World,
and for all regions from 2023. For ExUS before 2023, the Year column of the International trend table.

| Drug | Year | Region | Quarters summed | Sum | Printed | Difference |
|---|---|---|---|---|---|---|
| Orencia | 2006 | US | 4 | 88 | 88 | 0 |
| Orencia | 2006 | ExUS | 4 | 1 | 1 | 0 |
| Orencia | 2006 | World | 4 | 89 | 89 | 0 |
| Orencia | 2007 | US | 4 | 216 | 216 | 0 |
| Orencia | 2007 | ExUS | 4 | 15 | 15 | 0 |
| Orencia | 2007 | World | 4 | 231 | 231 | 0 |
| Orencia | 2008 | US | 4 | 363 | 363 | 0 |
| Orencia | 2008 | ExUS | 4 | 78 | 78 | 0 |
| Orencia | 2008 | World | 4 | 441 | 441 | 0 |
| Orencia | 2009 | US | 4 | 467 | 467 | 0 |
| Orencia | 2009 | ExUS | 4 | 135 | 135 | 0 |
| Orencia | 2009 | World | 4 | 602 | 602 | 0 |
| Orencia | 2010 | US | 4 | 547 | 547 | 0 |
| Orencia | 2010 | ExUS | 4 | 186 | 186 | 0 |
| Orencia | 2010 | World | 4 | 733 | 733 | 0 |
| Zeposia | 2020 (partial, Q2 to Q4) | US | 3 | 10 | 10 | 0 |
| Zeposia | 2020 (partial) | ExUS | 3 | 2 | 2 | 0 |
| Zeposia | 2020 (partial) | World | 3 | 12 | 12 | 0 |
| Zeposia | 2021 | US | 4 | 99 | 99 | 0 |
| Zeposia | 2021 | ExUS | 4 | 35 | 35 | 0 |
| Zeposia | 2021 | World | 4 | 134 | 134 | 0 |
| Zeposia | 2022 | US | 4 | 177 | 177 | 0 |
| Zeposia | 2022 | ExUS | 4 | 73 | 73 | 0 |
| Zeposia | 2022 | World | 4 | 250 | 250 | 0 |
| Zeposia | 2023 | US | 4 | 324 | 324 | 0 |
| Zeposia | 2023 | ExUS | 4 | 110 | 110 | 0 |
| Zeposia | 2023 | World | 4 | 434 | 434 | 0 |
| Zeposia | 2024 | US | 4 | 403 | 403 | 0 |
| Zeposia | 2024 | ExUS | 4 | 163 | 163 | 0 |
| Zeposia | 2024 | World | 4 | 566 | 566 | 0 |
| Sotyktu | 2022 (partial, Q3 to Q4) | US | 2 | 8 | 8 | 0 |
| Sotyktu | 2022 (partial) | ExUS | 2 | 0 | not printed in the Q4 2022 release; prior-year column of the Q4 2023 twelve-month table prints a dash | 0 |
| Sotyktu | 2022 (partial) | World | 2 | 8 | 8 | 0 |
| Sotyktu | 2023 | US | 4 | 157 | 157 | 0 |
| Sotyktu | 2023 | ExUS | 4 | 13 | 13 | 0 |
| Sotyktu | 2023 | World | 4 | 170 | 170 | 0 |
| Sotyktu | 2024 | US | 4 | 190 | 190 | 0 |
| Sotyktu | 2024 | ExUS | 4 | 56 | 56 | 0 |
| Sotyktu | 2024 | World | 4 | 246 | 246 | 0 |
| Sotyktu | 2025 | US | 4 | 182 | 182 | 0 |
| Sotyktu | 2025 | ExUS | 4 | 109 | 110 | -1 (rounding; the release says totals may not sum) |
| Sotyktu | 2025 | World | 4 | 291 | 291 | 0 |

Each quarter's US and World values were also checked against the same release's Ex 99.2 trend tables
(2006 to 2022). They agree. In the Q4 2006 Ex 99.2 worldwide table, the Orencia row's columns could not be
lined up reliably in the extracted text, so that one cross-check used the later trend tables instead (they
print 32).

## Launch facts (see bms_launches.csv)

- Orencia: BLA 125118, approved 2005-12-23 for adult RA (IV). The scanned original letter's date stamp is not
  legible, so the date comes from FDA's S-240 letter ("approved on December 23, 2005") and openFDA Drugs@FDA.
  Later approvals: pJIA IV 2008-04-07, SC route for RA 2011-07-29, pJIA SC age 2+ 2017-03-30, PsA 2017-06-30,
  aGVHD prophylaxis 2021-12-15, PsA SC age 2+ 2023-10-30. No UC or CD indication.
- Zeposia: NDA 209899, approved 2020-03-25 for relapsing MS. The letter is addressed to Celgene, which BMS
  acquired on 2019-11-20, before launch. UC approved 2021-05-27. No CD approval among the efficacy supplements
  listed by openFDA.
- Sotyktu: NDA 214958, approved 2022-09-09 for moderate-to-severe plaque psoriasis. Active PsA approved
  2026-03-06. No UC or CD approval.
- No change in the company recording sales for any of the three drugs within the windows.

## Documents relied on

BMS 8-K earnings exhibits on EDGAR (all opened and read):

| Quarter | 8-K filed | Exhibit 99.1 | Supplemental exhibit |
|---|---|---|---|
| 2006Q1 | 2006-04-27 | https://www.sec.gov/Archives/edgar/data/14272/000119312506090371/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312506090371/dex992.htm |
| 2006Q2 | 2006-07-27 | https://www.sec.gov/Archives/edgar/data/14272/000119312506154483/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312506154483/dex992.htm |
| 2006Q3 | 2006-10-26 | https://www.sec.gov/Archives/edgar/data/14272/000119312506215401/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312506215401/dex992.htm |
| 2006Q4 | 2007-01-25 | https://www.sec.gov/Archives/edgar/data/14272/000119312507012503/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312507012503/dex992.htm |
| 2007Q1 | 2007-04-26 | https://www.sec.gov/Archives/edgar/data/14272/000119312507091196/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312507091196/dex992.htm |
| 2007Q2 | 2007-07-26 | https://www.sec.gov/Archives/edgar/data/14272/000119312507162526/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312507162526/dex992.htm |
| 2007Q3 | 2007-10-25 | https://www.sec.gov/Archives/edgar/data/14272/000119312507225360/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312507225360/dex992.htm |
| 2007Q4 | 2008-01-31 | https://www.sec.gov/Archives/edgar/data/14272/000119312508016224/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312508016224/dex992.htm |
| 2008Q1 | 2008-04-24 | https://www.sec.gov/Archives/edgar/data/14272/000119312508088647/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312508088647/dex992.htm |
| 2008Q2 | 2008-07-24 | https://www.sec.gov/Archives/edgar/data/14272/000119312508156827/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312508156827/dex992.htm |
| 2008Q3 | 2008-10-23 | https://www.sec.gov/Archives/edgar/data/14272/000119312508214814/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312508214814/dex992.htm |
| 2008Q4 | 2009-01-27 | https://www.sec.gov/Archives/edgar/data/14272/000119312509011613/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312509011613/dex992.htm |
| 2009Q1 | 2009-04-28 | https://www.sec.gov/Archives/edgar/data/14272/000119312509089307/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312509089307/dex992.htm |
| 2009Q2 | 2009-07-23 | https://www.sec.gov/Archives/edgar/data/14272/000119312509153687/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312509153687/dex993.htm (Ex 99.3) |
| 2009Q3 | 2009-10-22 | https://www.sec.gov/Archives/edgar/data/14272/000119312509211606/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312509211606/dex992.htm |
| 2009Q4 | 2010-01-28 | https://www.sec.gov/Archives/edgar/data/14272/000119312510014925/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312510014925/dex992.htm |
| 2010Q1 | 2010-04-29 | https://www.sec.gov/Archives/edgar/data/14272/000119312510097960/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312510097960/dex992.htm |
| 2010Q2 | 2010-07-22 | https://www.sec.gov/Archives/edgar/data/14272/000119312510163385/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312510163385/dex992.htm |
| 2010Q3 | 2010-10-26 | https://www.sec.gov/Archives/edgar/data/14272/000119312510236161/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312510236161/dex992.htm |
| 2010Q4 | 2011-01-27 | https://www.sec.gov/Archives/edgar/data/14272/000119312511015402/dex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000119312511015402/dex992.htm |
| 2020Q2 | 2020-08-06 | https://www.sec.gov/Archives/edgar/data/14272/000001427220000227/q22020ex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000001427220000227/q22020ex992.htm |
| 2020Q3 | 2020-11-05 | https://www.sec.gov/Archives/edgar/data/14272/000001427220000277/q32020ex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000001427220000277/q32020ex992.htm |
| 2020Q4 | 2021-02-04 | https://www.sec.gov/Archives/edgar/data/14272/000001427221000058/q42020ex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000001427221000058/q42020ex992.htm |
| 2021Q1 | 2021-04-29 | https://www.sec.gov/Archives/edgar/data/14272/000001427221000124/q12021ex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000001427221000124/q12021ex992.htm |
| 2021Q2 | 2021-07-28 | https://www.sec.gov/Archives/edgar/data/14272/000001427221000184/q22021ex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000001427221000184/q22021ex992.htm |
| 2021Q3 | 2021-10-27 | https://www.sec.gov/Archives/edgar/data/14272/000001427221000223/q32021ex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000001427221000223/q32021ex992.htm |
| 2021Q4 | 2022-02-04 | https://www.sec.gov/Archives/edgar/data/14272/000001427222000047/q42021ex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000001427222000047/q42021ex992.htm |
| 2022Q1 | 2022-04-29 | https://www.sec.gov/Archives/edgar/data/14272/000001427222000112/q12022ex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000001427222000112/q12022ex992.htm |
| 2022Q2 | 2022-07-27 | https://www.sec.gov/Archives/edgar/data/14272/000001427222000164/q22022ex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000001427222000164/q22022ex992.htm |
| 2022Q3 | 2022-10-26 | https://www.sec.gov/Archives/edgar/data/14272/000001427222000194/q32022ex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000001427222000194/q32022ex992.htm |
| 2022Q4 | 2023-02-02 | https://www.sec.gov/Archives/edgar/data/14272/000001427223000018/q42022ex991.htm | https://www.sec.gov/Archives/edgar/data/14272/000001427223000018/q42022ex992.htm |
| 2023Q1 | 2023-04-27 | https://www.sec.gov/Archives/edgar/data/14272/000001427223000102/q12023ex991.htm | not used |
| 2023Q2 | 2023-07-27 | https://www.sec.gov/Archives/edgar/data/14272/000001427223000150/q22023ex991-filingversion.htm | not used |
| 2023Q3 | 2023-10-26 | https://www.sec.gov/Archives/edgar/data/14272/000001427223000179/q32023ex991-filing.htm | not used |
| 2023Q4 | 2024-02-02 | https://www.sec.gov/Archives/edgar/data/14272/000001427224000020/q42023ex991-filing.htm | not used |
| 2024Q1 | 2024-04-25 | https://www.sec.gov/Archives/edgar/data/14272/000001427224000094/q12024ex991-filing.htm | not used |
| 2024Q2 | 2024-07-26 | https://www.sec.gov/Archives/edgar/data/14272/000001427224000121/q22024ex991-filing.htm | not used |
| 2024Q3 | 2024-10-31 | https://www.sec.gov/Archives/edgar/data/14272/000001427224000145/q32024ex991-filing.htm | not used |
| 2024Q4 | 2025-02-06 | https://www.sec.gov/Archives/edgar/data/14272/000001427225000037/a2024ex991-filing.htm | not used |
| 2025Q1 | 2025-04-24 | https://www.sec.gov/Archives/edgar/data/14272/000001427225000089/a2025q1ex991-filing.htm | not used |
| 2025Q2 | 2025-07-31 | https://www.sec.gov/Archives/edgar/data/14272/000001427225000129/a2025q2ex991-filing.htm | not used |
| 2025Q3 | 2025-10-30 | https://www.sec.gov/Archives/edgar/data/14272/000001427225000147/a2025q3ex991.htm | not used |
| 2025Q4 | 2026-02-05 | https://www.sec.gov/Archives/edgar/data/14272/000001427226000002/a2025q4ex991.htm | not used |
| 2026Q1 | 2026-04-30 | https://www.sec.gov/Archives/edgar/data/14272/000001427226000008/a2026q1ex991.htm | not used |
| 2026Q2 | 2026-07-30 | https://www.sec.gov/Archives/edgar/data/14272/000001427226000018/a2026q2ex991-filing.htm | not used |
| 2026Q3 | 2026-10-29 | https://www.sec.gov/Archives/edgar/data/14272/000001427226000022/a2026q3ex991-filing.htm | not used |

Also read: the Q4 2005 release (8-K 2006-01-25, no Orencia sales), the Q1 2011 release (8-K 2011-04-28,
restatement check only), the Q1 2020 release (8-K 2020-05-07, no Zeposia revenue), the 8-K of 2022-04-18
(non-GAAP presentation change only, no product revenue changes), and the BMS 8-K of 2019-11-20 on closing the
Celgene acquisition.

FDA documents (accessdata.fda.gov/drugsatfda_docs): Orencia approval letter BL 125118/0 and supplement letters
S-045, S-086, S-122, S-171, S-209, S-211, S-240, S-250, with labels 2007 (S-016) and 2023 (S-250). Zeposia
letters NDA 209899 original, S-001 and S-011/S-012, with the 2024 label. Sotyktu letters NDA 214958 original and
S-002, with the 2026 label. Approval history from the openFDA Drugs@FDA API
(https://api.fda.gov/drug/drugsfda.json?search=application_number:BLA125118, ...:NDA209899, ...:NDA214958).
