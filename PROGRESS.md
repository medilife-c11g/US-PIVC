# Progress Tracker — USG-PIVC Post-Insertion Outcomes Meta-Analysis

## 2026-04-28 — Codex audit + 8 fixes applied (M3 / H1-H5 / M1 / M2)

Ran adversarial Codex methods audit (`task-moi59ese-9x65a2`, 3m 3s) on the full manuscript + R script + supplementary materials. 10 ranked risks returned (full output: `notes/Codex_audit_2026-04-28.md`). Top 8 fixed today:

- **M3 (stale numbers)**: title_page n=12→14; CLAUDE.md AI co-reviewer kappa 0.216 → Masuni Wang κ 0.330; manuscript extravasation k=2 / I²=96.7% → k=3 / I²=95.7%
- **H4 (GRADE Table 3)**: regenerated `output/table3_grade_sof.csv` — extravasation classification fixed (2 RCTs + 1 cohort), dwell time row updated to "Not pooled (I²=91.9%)" instead of stale pooled MD; manuscript inline Table 3 row 207 corrected
- **H1 (suppress non-poolable estimates)**: R script `04_meta_analysis.R` — when I²>75%, forest plots now omit pooled diamond; summary CSV reports "Not pooled (exploratory only)" for dwell time + extravasation
- **H3 (RoB completeness)**: added domain-level RoB 2 / NOS for Nishizawa, Cottrell, Refosco, Desai to `output/risk_of_bias.md` (now covers all 14 studies)
- **H2 (AI tool disclosure)**: added ICMJE 2024-compliant Use of AI declaration to manuscript footer
- **H5 (LOO largest-study influence)**: R script + `output/SupTable_LOO_catheter_failure.csv` — Saltarelli (49.8% weight) excluded → RR 1.18, p=0.28 (effect attenuates); Kleidon (paediatric) excluded → RR 1.28, p=0.032 (becomes significant)
- **B2 (design subgroup, bonus)**: cohort-only RR 1.29 (1.02-1.63) p=0.036 vs RCT-only RR 1.03 (NS) — borderline overall signal driven by cohorts; added to Results
- **M1 (equivalence language)**: replaced "perform equivalently" with "no statistically significant difference detected"
- **M2 (REML+HKSJ post hoc)**: relabeled from "pre-specified" to "*post-hoc* sensitivity analysis (not pre-specified in PROSPERO)"

**Remaining 2 Codex findings still open** (require user input):
- B1: PRISMA flow inconsistency (72 union vs 17 actually screened) — needs user to clarify how 72-17=55 were filtered before full-text retrieval
- B2 design heterogeneity GRADE downgrade — narrative paragraph added, formal certainty downgrade still pending

**Files touched today**: `scripts/04_meta_analysis.R`, `output/manuscript_draft.md`, `output/title_page.md`, `output/risk_of_bias.md`, `output/table3_grade_sof.csv`, `CLAUDE.md`. New: `output/SupTable_LOO_catheter_failure.csv`, `notes/Codex_audit_2026-04-28.md`.

---

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
| 04a | Second reviewer (Masuni Wang) screening + kappa | ✅ Done | 2026-04-20 | Kappa=0.330, 95.8% agreement; 57 disagreements resolved by primary reviewer (PI); Rayyan export 2026-04-20_17-45-53; Diane (Lee) & Jen Tao data excluded (did not complete) |
| 04b | Post-consensus removals | ✅ Done | 2026-04-03 | Removed: Avelar (Portuguese), oncology nurses (unpublished), ICU nurses DIVA (unpublished) |
| 05 | Full-text retrieval | ✅ Done | 2026-04-09 | All 14 full texts obtained. Desai 2018 (JAVA 23:3) + Nishizawa 2020 (JAVA 25:2) retrieved 2026-04-09. |
| 05a | Full-text screening | ✅ Done | 2026-04-09 | Malik excluded (single-arm). 14 studies confirmed eligible. Dachepally, Paladini, Refosco & Desai flagged for catheter confounding. |
| 06 | Data extraction | ✅ Done | 2026-04-09 | 14 studies in `data/meta_input.csv`; Desai & Nishizawa fully extracted and added |
| 07 | Risk of bias assessment | ✅ Done | 2026-04-09 | RoB 2: 4 Some concerns (incl. Nishizawa), 1 High risk (Leroux); NOS: Desai 5/9. See `output/risk_of_bias.md` |
| 08 | Meta-analysis (R) | ✅ Done | 2026-04-09 | `04_meta_analysis.R` re-run with 14 studies. Extravasation now k=3 (Bridey/Favot/Nishizawa). Forest plots regenerated. |
| 09 | Manuscript drafting | ✅ Done | 2026-04-09 | `output/manuscript_draft.md` — updated with all 14 studies; Desai & Nishizawa incorporated throughout |
| 09a | Tables & Figures PDF | ✅ Done | 2026-04-09 | Table 1 now 14 studies; Table 2A includes Nishizawa (RoB 2); Table 2B includes Desai (NOS); forest plots updated |
| 09b | Supplementary materials | ✅ Done | 2026-04-18 | S1 search strategy; S2 updated (Desai/Nishizawa moved from "unavailable" → "retrieved & included"); S3 PRISMA checklist |
| 09c | Cover letter + Title page | ✅ Done | 2026-04-18 | Updated: 14 studies / 5 RCTs / 9 cohorts / 78,209 participants; date April 18 |
| 09d | Manuscript peer-review revision (3 rounds) | ✅ Done | 2026-04-18 | See revision log below |
| 09e | REML+HKSJ sensitivity analysis | ✅ Done | 2026-04-18 | Added to `04_meta_analysis.R`; RR 1.225 (1.005–1.493) p=0.047 — consistent with DL |
| 09f | PRISMA PDF regenerated | ✅ Done | 2026-04-18 | n=6 excluded (was n=5); 78,209 participants; Kleidon JVA/BJN both listed |
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

### Full-text retrieval: ALL 14 INCLUDED STUDIES RETRIEVED ✅
- Desai K 2018 (JAVA 23:3) — retrieved via interlibrary loan 2026-04-09
- Nishizawa T 2020 (JAVA 25:2) — retrieved via interlibrary loan 2026-04-09

### Full-text screening: Malik A excluded (single-arm, no comparator)
- **14 studies confirmed eligible** (updated 2026-04-09)
- Confounded (excluded from primary pooling): Dachepally, Paladini, Refosco, Desai

### Meta-Analysis Results (updated 2026-04-18)

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
- Extravasation (k=3, I²=95.7%): Favot RR 19.4 unfavorable to USG; Bridey 34% vs 18% trending unfavorable; **Nishizawa 13.6% vs 28.5% (NS, opposite direction, small n)**
- Infiltration: Saltarelli OR 1.31 null; Varghese 2.2% vs 11.1% favoring USG
- Confounded studies (Dachepally, Paladini, Refosco, **Desai**): strongly favor USG but catheter length confounds results
  - **Desai 2018**: KM 143 vs 89h (p<0.001); complications 34% vs 32% (NS); CONFOUNDED — 55% DIVA hx in USG vs 7.2% TPIV; longer catheters used
  - **Nishizawa 2020**: 5th RCT (nurse-performed ICU, DIVA); primary = first-attempt success (70% vs 40%, p<0.05); extravasation secondary NS

**Outputs:**
- `output/forest_catheter_failure.pdf`
- `output/forest_dwell_time.pdf`
- `output/forest_HR_failure.pdf`
- `output/forest_failure_by_age.pdf`
- `output/risk_of_bias.md`
- `output/meta_analysis_summary.csv`
- `data/extracted_data.csv`
- `data/meta_input.csv`

### Manuscript Revision Log (2026-04-18)

Three rounds of AI-assisted peer review (via ChatGPT simulation) completed. Status: **Minor Revision → submission-ready**.

| Round | Key Change | Status |
|-------|-----------|--------|
| R1 | Cover letter updated (14/5/9/78,209); PRISMA n=5→n=6; AI reviewer reframed; S2 Desai/Nishizawa status corrected; REML+HKSJ added; language softened (adult subgroup, extravasation) | ✅ |
| R2 | Study characteristics counts fixed (7 adult/7 paed; ED=8/ICU=3); extravasation Table 3 RR removed → "not pooled"; HKSJ borderline statement added; PRISMA flow cleaned | ✅ |
| R3 | AI screening paragraph further tightened (human decision emphasis); Results compressed (individual studies → 3 paragraphs); PRISMA ambiguous bracket removed; Table 3 extravasation finalised | ✅ |

### Next Actions (Updated 2026-04-21)
1. ~~Retrieve unavailable full-texts~~ — DONE
2. ~~Unify participant totals~~ — DONE (78,209 throughout)
3. ~~REML+HKSJ sensitivity analysis~~ — DONE
4. ~~Second reviewer screening (Masuni Wang = Yu-Ling Wang)~~ — DONE (kappa=0.330, 95.8%)
5. ~~Author information updated~~ — DONE (4 authors: Tai-An Lee†, Yu-Ling Wang†, Jen-Tao Wang, Chia-Ching Chen*)
6. ~~AI screening references removed~~ — DONE (manuscript, screening_consensus, sync_for_claude_app all updated)
7. ~~Forest plots → TIFF 300 dpi~~ — DONE (`output/tiff/` 6 files)
8. **PENDING**: 四位作者填入 ORCID
9. **PENDING**: 所有作者簽核確認
10. **PENDING**: Submit to The Ultrasound Journal (BMC)

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
