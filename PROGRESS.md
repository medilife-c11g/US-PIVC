# Progress Tracker — USG-PIVC Post-Insertion Outcomes Meta-Analysis

## Project Info
- **PI**: Chia-Ching Chen, MD (陳家慶)
- **Second reviewer**: Tai-An Lee, MD (LEE TAI AN)
- **Started**: 2026-03-28
- **PROSPERO**: CRD420261354170

---

## Pipeline Progress

| Step | Task | Status | Date | Notes |
|------|------|--------|------|-------|
| 01 | PubMed search | ✅ Done | 2026-03-28 | 530 records retrieved |
| 02 | Cochrane/Embase/CINAHL search strings | ✅ Done | 2026-03-28 | Search strings generated, awaiting manual export |
| 02a | Cochrane CENTRAL manual export | ✅ Done | 2026-03-29 | 68 records |
| 02b | Embase (Ovid) manual export | ✅ Done | 2026-03-29 | 984 records |
| 02c | CINAHL manual export | ✅ Done | 2026-03-29 | 50 records |
| 03 | Deduplication | ✅ Done | 2026-03-29 | 1,632 total → 273 duplicates → 1,359 unique |
| 04 | Title/Abstract screening (Rayyan) | ✅ Done | 2026-04-03 | Rayyan #1961147; Consensus: 17 Include, 0 Maybe, 1,342 Exclude |
| 04a | AI co-reviewer screening + kappa | ✅ Done | 2026-04-03 | Kappa=0.216, 97.1% agreement; 40 disagreements resolved by consensus |
| 04b | Post-consensus removals | ✅ Done | 2026-04-03 | Removed: Avelar (Portuguese), oncology nurses (unpublished), ICU nurses DIVA (unpublished) |
| 05 | Full-text retrieval | 🔄 Partial | 2026-04-04 | 15/17 PDFs downloaded; 2 unavailable (Desai, Nishizawa). Cottrell & Refosco retrieved 2026-04-04. |
| 05a | Full-text screening | ✅ Done | 2026-04-04 | Malik excluded (single-arm). 12 studies confirmed eligible. Dachepally, Paladini & Refosco flagged for catheter confounding. |
| 06 | Data extraction | ✅ Done | 2026-04-04 | 12 studies in `data/meta_input.csv` |
| 07 | Risk of bias assessment | ✅ Done | 2026-04-03 | RoB 2: 3 Some concerns, 1 High risk; NOS: range 5-9/9. See `output/risk_of_bias.md` |
| 08 | Meta-analysis (R) | ✅ Done | 2026-04-03 | `04_meta_analysis.R` completed. Forest plots in `output/`. See results below. |
| 09 | Manuscript drafting | ✅ Done | 2026-04-03 | `output/manuscript_draft.md` — revised per Gemini critique; GRADE added |
| 09a | Tables & Figures PDF | ✅ Done | 2026-04-03 | Table 1-3 PDF + CSV; PRISMA PDF; 6 forest plot PDFs |
| 09b | Supplementary materials | ✅ Done | 2026-04-03 | S1 search strategy, S2 excluded studies, S3 PRISMA checklist |
| 09c | Cover letter + Title page | ✅ Done | 2026-04-03 | Target: The Ultrasound Journal (BMC) |
| 09d | Cottrell + Refosco update | ✅ Done | 2026-04-04 | 12 studies; dwell time I²=91.9% unpoolable; all outputs regenerated |
| 10 | PROSPERO registration | ✅ Done | 2026-03-29 | CRD420261354170 |

---

## Search Results Summary

### PubMed (2026-03-28)
- **Total records**: 530
- **Date range**: 2000–2026
- **Output files**: `data/pubmed_results.csv`, `data/pubmed_results.ris`
- Top years: 2025 (54), 2020 (41), 2022 (36), 2024 (34)

### Cochrane CENTRAL
- Search string: `data/cochrane_search_string.txt`
- Status: Awaiting manual search

### Embase (Ovid)
- Search string: `data/embase_search_string.txt`
- Status: Awaiting manual search

### CINAHL
- Search string: `data/cinahl_search_string.txt`
- Status: Awaiting manual search

---

## Screening Summary (as of 2026-04-03)

### Final Include List (17 studies, ≈14-15 unique after dedup)
| # | First Author | Year | Design | Population | Key Outcomes | Full-text |
|---|-------------|------|--------|------------|-------------|-----------|
| 1 | Kleidon TM | 2025 | RCT | Paediatric | PIVC failure, dwell time (JAMA Pediatrics — primary report) | ✅ |
| 2 | Refosco M | 2024 | Retro cohort | Paediatric | Dwell time, complications | ❌ |
| 3 | Malik A | 2023 | Retro cohort | Adult ED | Dwell time, USIV survival (n=388) | ✅ ⚠️ may be single-arm |
| 4 | Dachepally R | 2023 | Retro cohort | Paediatric ICU | IV survival, failure HR 2.20 | ✅ |
| 5 | Feinsmith SE | 2021 | Retro cohort | Adult | Time to failure (n=43,470) | ✅ |
| 6 | Cottrell JT | — | — | Paediatric | USG dwell time in children | ❌ |
| 7 | Favot M | 2019 | Retro cohort | Adult ED | Contrast extravasation (unfavorable to USG) | ✅ |
| 8 | Shokoohi H | 2019 | Prospective | Adult ED | 72-hr survivorship (null) | ✅ |
| 9 | Bridey C | 2018 | RCT | Adult ICU | Catheter lifespan, extravasation (null result) | ✅ |
| 10 | Paladini A | 2018 | Retro cohort | Paediatric ED | USG long peripheral in children | ✅ |
| 11 | Kleidon TM | 2022 | RCT | Paediatric | EPIC (J Vasc Access version) — duplicate of #1 | ✅ |
| 12 | Varghese S | 2025 | RCT | Paediatric ED | USG vs landmark RCT | ✅ |
| 13 | Desai K | — | — | Paediatric ED | Longevity & complications | ❌ |
| 14 | Saltarelli NA | 2015 | Retro cohort | Adult ED | Infiltration rates (null result, abstract only) | ✅ |
| 15 | Nishizawa T | — | RCT | Adult ICU | Nurse-performed USG RCT | ❌ |
| 16 | Leroux S | 2023 | RCT | Adult ED | Catheter-to-vein ratio & post-insertion failure | ✅ |
| 17 | Turkish study | — | Quasi-exp | — | Effectiveness USG in PIVC application (n=30) | ❌ |

### Removed from Include
- Avelar AF [486160522] — Portuguese language
- Oncology nurses [486160685] — Not published
- ICU nurses DIVA [486160677] — Not published
- Kleidon protocol (BJN) — Protocol only, same trial as #1

### Full-text retrieval: 11/17 downloaded, 4 unavailable
- ❌ Refosco M, Cottrell JT, Desai K, Nishizawa T

### Full-text screening: Malik A excluded (single-arm, no comparator)
- 10 studies confirmed eligible for data extraction
- Dachepally & Paladini flagged: catheter length/type confounding

### Meta-Analysis Results (2026-04-03)

**Primary: Catheter Failure (k=4, I²=0%)**
- RR = 1.23 (95% CI 1.00–1.51), p = 0.056 — NOT significant
- Studies: Kleidon, Shokoohi, Leroux, Saltarelli

**Primary: Dwell Time (k=3, I²=91.9%) — CANNOT POOL**
- Cottrell +36.7h favors USG (p<0.001) vs Kleidon/Leroux null
- Studies: Kleidon, Leroux, Cottrell
- Narrative synthesis: benefit may be setting/operator dependent

**HR-based Failure (k=2, I²=68%)**
- Pooled HR = 1.02 (0.75–1.38), p = 0.91 — conflicting directions (Feinsmith favors USG, Shokoohi null)

**Narrative synthesis (insufficient studies to pool):**
- Extravasation: Favot RR 19.4 unfavorable to USG; Bridey 34% vs 18% trending
- Infiltration: Saltarelli OR 1.31 null; Varghese 2.2% vs 11.1% favoring USG
- Confounded studies (Dachepally, Paladini, Refosco): strongly favor USG but catheter length confounds results

**Outputs:**
- `output/forest_catheter_failure.pdf`
- `output/forest_dwell_time.pdf`
- `output/forest_HR_failure.pdf`
- `output/forest_failure_by_age.pdf`
- `output/risk_of_bias.md`
- `output/meta_analysis_summary.csv`
- `data/extracted_data.csv`
- `data/meta_input.csv`

### Next Actions
1. Retrieve 4 unavailable full-texts (if possible) and re-run analysis
2. Co-author review (Lee)
3. Convert forest plots to journal-required format (TIFF 300 dpi)
4. Cover letter for target journal

### Completed Outputs
- `output/manuscript_draft.md` — Full manuscript with tables and PRISMA diagram
- `output/supplementary_S1_search_strategy.md` — Complete search strategies (4 databases)
- `output/supplementary_S2_excluded_studies.md` — Excluded studies with reasons
- `output/supplementary_S3_PRISMA_checklist.md` — PRISMA 2020 checklist (29 items)
- `output/risk_of_bias.md` — Detailed RoB 2 + NOS assessment
- `output/forest_catheter_failure.pdf` — Figure 2
- `output/forest_dwell_time.pdf` — Figure 3
- `output/forest_infiltration.pdf` — Figure 4
- `output/forest_failure_by_age.pdf` — Figure 5
- `output/forest_HR_failure.pdf` — HR-based analysis
- `output/forest_extravasation.pdf` — Extravasation (narrative)
- `output/meta_analysis_summary.csv` — Pooled results summary
- `data/extracted_data.csv` — Full data extraction
- `data/meta_input.csv` — Meta-analysis input data
