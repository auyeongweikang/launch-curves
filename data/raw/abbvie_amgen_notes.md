# abbvie_amgen: collection notes

Group: Skyrizi (risankizumab), Rinvoq (upadacitinib), Otezla (apremilast).
Collected 2026-11-19. All values are USD millions as printed in each company's quarterly
earnings release (8-K Exhibit 99.1). Every quarter in each window was found; no blanks.

## Windows and row counts

| Drug | First quarter with sales | First US quarter (q1) | Window end (q20) | Reporter in window | Rows |
|---|---|---|---|---|---|
| Skyrizi | 2019Q2 | 2019Q2 | 2024Q1 | AbbVie | 60 (20 quarters x US, ExUS, World) |
| Rinvoq | 2019Q3 | 2019Q3 | 2024Q2 | AbbVie | 60 |
| Otezla | 2014Q2 | 2014Q2 | 2019Q1 | Celgene | 60 |

Total: 180 rows, all `method = printed`, all `period_type = quarter`.

- Skyrizi: first approved in Japan (AbbVie release 2019-03-26) and in the US on 2019-04-23, but
  AbbVie's Q1 2019 release has no Skyrizi line, and the Q1 2020 10-Q prints Q1 2019 Skyrizi as
  "—". Q2 2019 is the first quarter with sales anywhere (US 42, international 6).
- Rinvoq: US approval 2019-08-16; first sales Q3 2019 (US only). International is printed as "—"
  in Q3 and Q4 2019 (EU approval announced 2019-12-18); first international figure is Q1 2020 (4).
- Otezla: US approval 2014-03-21, but Celgene's Q1 2014 release has no Otezla line and its Q2 2014
  release says the product launched "in early April". The six-month 2014 figure (4.6) equals Q2,
  so Q2 2014 is quarter 1.

## How the companies report

**AbbVie (Skyrizi, Rinvoq).** The "Key Product Revenues" table of each quarterly release
(Quarter Ended ...) prints net revenues in USD millions, whole numbers, with columns headed
"U.S.", "Int'l." and "Total". Mapped to `US`, `ExUS` and `World`. The hint said "United
States / International"; the printed headers are the abbreviated forms. Calendar-year company.
Skyrizi is part of a collaboration with Boehringer Ingelheim in which AbbVie leads global
development and commercialisation (AbbVie Q3 2019 release); AbbVie prints Skyrizi as its own
net revenues line, so these are product net revenues, not a collaboration or profit-share line.

**Celgene (Otezla).** The "Net Product Sales (In millions)" table, Three-Month Periods block,
row group OTEZLA® with sub-rows "U.S.", "International" and "Worldwide" (mapped to `US`, `ExUS`,
`World`). Footnote markers after OTEZLA® are left out of `label_as_printed`. Precision changes:
Celgene printed one decimal place through the Q4 2016 release and whole millions from the Q1
2017 release on. Values are recorded exactly as printed (for example 4.6, then 199).

**Dashes.** Where the table prints an em dash (—) for a region, the row has `value = 0` and a note
saying so. This affects Rinvoq ExUS 2019Q3 and 2019Q4, and Otezla ExUS 2014Q2, 2014Q3 and 2014Q4.
If the merge step should treat a printed dash differently from zero, these six rows are flagged.

**Duplicate filing.** AbbVie filed two 8-Ks with the same Q1 2022 release on 2022-04-29
(accessions 0001551152-22-000010 and 0001551152-22-000012). The Skyrizi and Rinvoq figures are
identical in both; the rows cite the first accession.

## Otezla ownership change (handover verified from filings)

- 2019-08-25: Celgene and Amgen sign the asset purchase agreement for the worldwide Otezla product
  line ($13.4 billion cash).
- 2019-11-20: Bristol-Myers Squibb completes the acquisition of Celgene (Celgene 8-K, Item 2.01:
  https://www.sec.gov/Archives/edgar/data/816284/000110465919065939/tm1923405d1_8k.htm).
- 2019-11-21: Celgene completes the sale of Otezla to Amgen (Celgene 8-K filed 2019-11-22:
  https://www.sec.gov/Archives/edgar/data/816284/000110465919066707/tm19236191_8k.htm; Amgen 8-K
  filed 2019-11-21: https://www.sec.gov/Archives/edgar/data/318154/000119312519297010/d817874d8k.htm).

**The handover falls outside the Otezla window.** Counting Q2 2014 as quarter 1, quarter 20 is
Q1 2019, so every window quarter is a Celgene figure and no handover rows are in the sales file.
For anyone extending the series, this is what each company printed around the handover (not
in the CSV):

- Celgene's last report was Q3 2019 (release 2019-10-31): Otezla U.S. 445, International 102,
  Worldwide 547.
  https://www.sec.gov/Archives/edgar/data/816284/000110465919058070/tm1921268d1_ex99-1.htm
- Amgen's Q4 2019 release (2020-01-30), Product Sales Detail table: Otezla US 139, ROW 39,
  TOTAL 178, covering 2019-11-21 to 2019-12-31 only ("Otezla was acquired on Nov. 21, 2019, and
  generated $178 million in sales for the period"). Amgen's FY2019 Otezla line is the same 178.
  https://www.sec.gov/Archives/edgar/data/318154/000031815420000012/amgn-20191231xq4ex991.htm
- Gap: Otezla sales for 2019-10-01 to 2019-11-20 were not found in any public document.
  Celgene published no Q4 2019 report. BMS's Q4 2019 supplemental information (8-K Exhibit 99.2,
  2020-02-06) states that "All historically reported Celgene revenues have been recast to exclude
  Otezla" and lists Celgene product revenues for 2019-10-01 to 2019-11-19 without Otezla.
  https://www.sec.gov/Archives/edgar/data/14272/000001427220000075/q42019ex992.htm
  So calendar Q4 2019 has only Amgen's partial-quarter figure. A full Q4 2019 cannot be built.

## Full-year checks (sum of the four quarters vs the printed full-year figure)

Full-year figures come from the twelve-month table in each Q4 release. For AbbVie they were
also checked against the annual product table in the 10-K (same values in every 10-K that prints
that year). Partial first years (Skyrizi 2019: 3 quarters; Rinvoq 2019: 2 quarters; Otezla
2014: 3 quarters) are compared because the company had no sales in the missing quarters.

| Drug | Year | Quarters | US sum / printed / diff | ExUS sum / printed / diff | World sum / printed / diff |
|---|---|---|---|---|---|
| Skyrizi | 2019 | 3 | 311 / 311 / 0 | 44 / 44 / 0 | 355 / 355 / 0 |
| Skyrizi | 2020 | 4 | 1,385 / 1,385 / 0 | 205 / 205 / 0 | 1,590 / 1,590 / 0 |
| Skyrizi | 2021 | 4 | 2,486 / 2,486 / 0 | 453 / 453 / 0 | 2,939 / 2,939 / 0 |
| Skyrizi | 2022 | 4 | 4,484 / 4,484 / 0 | 681 / 681 / 0 | 5,165 / 5,165 / 0 |
| Skyrizi | 2023 | 4 | 6,753 / 6,753 / 0 | 1,010 / 1,010 / 0 | 7,763 / 7,763 / 0 |
| Rinvoq | 2019 | 2 | 47 / 47 / 0 | 0 / — / 0 | 47 / 47 / 0 |
| Rinvoq | 2020 | 4 | 653 / 653 / 0 | 78 / 78 / 0 | 731 / 731 / 0 |
| Rinvoq | 2021 | 4 | 1,271 / 1,271 / 0 | 380 / 380 / 0 | 1,651 / 1,651 / 0 |
| Rinvoq | 2022 | 4 | 1,794 / 1,794 / 0 | 728 / 728 / 0 | 2,522 / 2,522 / 0 |
| Rinvoq | 2023 | 4 | 2,824 / 2,824 / 0 | 1,145 / 1,145 / 0 | 3,969 / 3,969 / 0 |
| Otezla | 2014 | 3 | 69.8 / 69.8 / 0 | 0 / — / 0 | 69.8 / 69.8 / 0 |
| Otezla | 2015 | 4 | 440.0 / 440.0 / 0 | 31.7 / 31.7 / 0 | 471.7 / 471.7 / 0 |
| Otezla | 2016 | 4 | 904.4 / 904.4 / 0 | 112.8 / 112.8 / 0 | 1,017.2 / 1,017.2 / 0 |
| Otezla | 2017 | 4 | 1,058 / 1,058 / 0 | 221 / 221 / 0 | 1,279 / 1,279 / 0 |
| Otezla | 2018 | 4 | 1,275 / 1,275 / 0 | 333 / 333 / 0 | 1,608 / 1,608 / 0 |

Every full year inside the windows reconciles exactly. The Otezla FY2016 figure is printed as
904 / 113 / 1,017 in the Q4 2017 release's prior-year column (whole-million rounding).

## Restatement checks (first-reported value vs later comparatives)

- **AbbVie.** Q1-Q3 quarters were compared with the prior-year columns of the 10-Q one year later
  (2020-08-04 through 2025-08-04 10-Qs). All 30 comparisons match exactly. AbbVie's quarterly
  releases print only percentage changes, not prior-year values, and no document prints a Q4
  quarter as a comparative; the annual totals in later 10-Ks match, so no Q4 change is implied.
- **Celgene.** Each quarter was compared with the prior-year column of the release one year later.
  2014Q2-2015Q4 and 2017Q1-2018Q3 match exactly. The 2016 quarters were reprinted in whole
  millions in the 2017 releases; most differences are rounding, but three are larger and look
  like small restatements:
  - 2016Q2 International: 25.1 first reported, 24 in the Q2 2017 release.
  - 2016Q2 Worldwide: 241.9 first reported, 241 in the Q2 2017 release.
  - 2016Q3 International: 30.1 first reported, 31 in the Q3 2017 release.
  The later values and sources are in the `notes` column of each 2016 row. 2018Q4 and 2019Q1 were
  never reprinted as comparatives because Celgene stopped reporting after Q3 2019.

## Launch facts

Approval dates in `abbvie_amgen_launches.csv` are FDA approval-letter dates from Drugs@FDA
(accessdata.fda.gov), found through the openFDA drugsfda API and confirmed by reading each
letter. Where the company press release is dated a day later (Skyrizi Crohn's disease:
letter 2022-06-16, AbbVie release 2022-06-17; Rinvoq GCA: letter 2025-04-28, AbbVie release
2025-04-29) the letter date is used. Efficacy supplements that only changed label sections
(Skyrizi formulation and device supplements, genital/scalp data; Otezla scalp and genital
psoriasis data; Rinvoq UC fatigue data) are not counted as new indications. Otezla has no UC or
Crohn's disease approval.

## Documents relied on

- AbbVie quarterly earnings releases, 8-K Exhibit 99.1, Q2 2019 to Q2 2024 (21 releases), read from
  the local copies in Biotech Vault `Source Documents\ABBV - AbbVie\SEC Filings`; `source_url` is
  the original EDGAR URL from that folder's manifest.csv (CIK 1551152). Also the Q1 2019 release
  (no Skyrizi line), the Q3 2024 to Q4 2024 releases, and the Q3 2026 release (both products still
  reported).
- AbbVie 10-Q and 10-K filings 2019-11 to 2026-02 (local copies) for restatement and annual checks.
- Celgene quarterly earnings releases, 8-K Exhibit 99.1, Q1 2014 to Q3 2019 (23 releases),
  downloaded from EDGAR (CIK 816284, found by EDGAR company search "celgene": CELGENE CORP /DE/).
- Celgene 8-Ks of 2019-11-20 and 2019-11-22; Amgen 8-K of 2019-11-21 (CIK 318154); Amgen Q4 2019
  and Q3 2026 earnings releases; BMS Q4 2019 earnings release and supplemental information
  (CIK 14272).
- FDA approval letters and labels for BLA 761105, BLA 761262, NDA 211675, NDA 218347, NDA 205437,
  NDA 206088 and NDA 210745 (accessdata.fda.gov).
- AbbVie press releases (local copies) for the Skyrizi Japan approval (2019-03-26) and the
  Rinvoq EU approval (2019-12-18).
