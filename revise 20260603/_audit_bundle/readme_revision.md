# The Ultrasound Journal — Revision package (#19152) · 2026-06-03

Decision: **Revisions Required** (R1 Accept; R2 Revisions Required, 10 major + 5 minor). Base = the actual submitted files in `../The Ultrasound Journal [BioMedCentral  Springer Nature]/` (`manuscript with endnote 20260513.docx`). **All changes in the manuscript are shown in RED** in the marked-up file for your re-check.

## Upload set for the journal (3 required files)
1. **`Manuscript_revised_MARKEDUP.docx`** — marked-up; my changes in **red** (British→American spelling applied throughout, not individually reddened).
2. **`Manuscript_revised_CLEAN.docx`** — clean version, changes accepted.
3. **`Response_to_Reviewers.md`** — point-by-point response (export to .docx before upload).

## Figures (✅ regenerated, R 4.5.3, correct submitted numbering)
`Figure1_RiskOfBias.png` (RoB — now 6 RCTs incl. Avelar) · `Figure2_PRISMA.png` (15 incl/4 excl/6 RCTs/78,591) · `Figure3_catheter_failure.png` · `Figure4_dwell_time.png` · `Figure5_infiltration.png` (**k=3, RR 1.30**) · `Figure6_subgroup_by_age.png` (was Fig 7) · `SupplementaryFigure1_extravasation.png` · `SupplementaryFigure2_time_to_event.png` (moved from main per R2.8).

## Tables & Supplements
- `Table1_study_characteristics.docx` — ✅ **Avelar 2015 row added (red)**; now 15 studies.
- `Table2_risk_of_bias.docx` — ✅ **Avelar 2015 added as 6th RCT in Part A (red):** D1 Low · D2 Some concerns · D3 Low · D4 Some concerns · D5 Low · Overall Some concerns.
- `Supplementary_Material_S3.docx` (full-text excluded-studies list) — ✅ **realigned to n = 4 (red)** (see PRISMA reconciliation below): Avelar 2013 reframed as the Portuguese companion of the included 2015 trial (NCT00930254); the two records that were actually title/abstract exclusions (ICU-nurses registration NCT03745209; Kleidon J Vasc Access 2022 abstract) removed from the full-text table, with a red note explaining where they belong; Kleidon BJN 2023 EPIC protocol kept as the single overlapping-report exclusion.
- `Supplementary_Material_S1, S2, S4.docx` — copied from the submission (PRISMA checklist / search strategies / leave-one-out; unaffected by the Avelar addition — catheter-failure pool unchanged).

## PRISMA full-text "Reports excluded" — reconciled to n = 4 (verified against raw screening data)
Re-derived from `data/screening_consensus_PI_Masuni.csv` (1,359 records: 1,287 both-exclude, 57 single-reviewer/disagreement, 15 both-include) and independently re-checked by a 6-agent adversarial workflow (both skeptics: refuted = false, high confidence; ledger confirmed).
- **19 reports** formally advanced to full-text = 15 both-reviewer includes + 4 primary-reviewer-only includes (Kleidon-BJN protocol, Malik, Paladini, Leroux). **19 − 4 excluded = 15 included.** ✓
- **4 full-text exclusions:** (1) Malik — single-arm/no comparator; (2) Avelar **2013** — Portuguese non-English companion of the included 2015 English trial (NCT00930254); (3) oncology-nurses NCT07208175 — unpublished; (4) Kleidon **BJN 2023** — EPIC trial protocol, overlapping report of the included Kleidon 2025.
- **Key correction:** `rayyan-486160498` is the **Avelar 2015 English RCT** (a both-reviewer include wrongly dropped at full-text as "Portuguese"). The records the old S3 over-counted (ICU-nurses 677, Kleidon J Vasc Access 2022 abstract 691, Sengul 703) were single-reviewer **title/abstract** includes adjudicated out at T/A — part of the 1,340, not full-text exclusions.
- **Now aligned across all three artifacts (all say n = 4):** PRISMA flow diagram (`Figure2_PRISMA.png`, regenerated — also fixed a stale infiltration value k=2/RR 0.68 → **k=3/RR 1.30**), Supplementary S3, and the manuscript Methods/Results. The manuscript reason #4 was also corrected (red) so only the BJN 2023 protocol is named as the full-text overlapping-report exclusion; the J Vasc Access 2022 abstract is now described as a title/abstract exclusion (references [11]/[13] retained — no orphaning).

## What was changed (all reflected in the marked-up manuscript)
- **R1.1** neutral framing of the hypothesis sentence.
- **R2.1** abstract "…included **in the qualitative synthesis**"; counts → 15 studies / 6 RCTs / 78,591.
- **R2.4** screening process clarified (T/A = C.C.C. + Y.L.W.; full-text = T.A.L. + Y.L.W. + C.C.C., consensus); reviewer initials standardized to Y.L.W.
- **R2.5** Avelar trial **included** via its English 2015 report [5]; 2013 Portuguese [10] kept excluded as its companion.
- **R2.6** standalone **Study Limitations** section + Scopus/Web-of-Science omission added; abstract limitations line.
- **R2.8** time-to-event forest moved to **Supplementary Figure 2**; section condensed. Infiltration kept as a main figure (now k=3 with Avelar — your decision).
- **R2.10** Supplementary Figure 1 (extravasation) included; callouts fixed.
- **Minors:** American English throughout; `I²` fixed; **R version 4.5.3**; `meta`/`metafor` package refs added ([31] Balduzzi 2019, [32] Viechtbauer 2010); figure-callout errors fixed (dwell→Fig 4; subgroup→Fig 6; Kleidon EPIC → [12]); Refosco year → 2025.
- **Infiltration meta-analysis:** k=2→3 with Avelar; pooled RR **0.68 → 1.30 (0.82–2.05)**, I² 65.9%→48.8%.

## ⚠ Author finalization (please complete in your EndNote master before upload)
All substantive content edits are done and marked red. The remaining items are Word formatting + your reference library:
1. **Chronological reorder (R2.7)** — reorder studies **most-recent-first** in Table 1 and Table 2, and in the Results narrative. The Avelar rows are already inserted (red, as the oldest study they sit last either way). This is left to you because it reshuffles your EndNote-linked rows; pooled estimates are display-order-invariant.
2. **Table formatting (m5)** — bold table titles + repeat the header row on each page; reduce Table 1 font/line-spacing to limit splitting; bring **Table 2 to a single page**.
3. **References** — add to your EndNote library: **[31]** Balduzzi S, Rücker G, Schwarzer G. *Evid Based Ment Health.* 2019;22(4):153–160; **[32]** Viechtbauer W. *J Stat Softw.* 2010;36(3):1–48. (Bracketed numbers in the manuscript mirror the submitted EndNote numbering.)
4. **Author Contributions** (title page / `coi_disclosure` file) — align with the corrected roles: T/A screening C.C.C. + Y.L.W.; full-text screening T.A.L. + Y.L.W. + C.C.C.
5. Export the response letter to **.docx** for upload.

## Three-model cross-review (2026-06-04) — fixes applied
Codex (auth-expired this run), Claude, and Gemini audited the package; verified findings fixed in both manuscript files (red in markup):
- **Catheter-failure CI reconciled to 1.00–1.51** in Abstract + Conclusion (were "0.99"); exact lower bound = 0.99516 → rounds to 1.00 (matches csv/Results/Figure 3); the Results sentence now cites the true precise value (0.995) when explaining the CI crosses unity.
- **Citation/typo fixes:** Desai mis-cited [15]→[14]; unclosed "(" after Saltarelli [26] closed; "[14. 24]"→"[14, 24]".
- **Figure cross-reference fixes (Discussion used stale numbers):** catheter-failure "(Figure 2)"→"(Figure 3)"; dwell "(Figure 3)"→"(Figure 4)"; subgroup "(Figure 7)" ×3 → "(Figure 6)"; Fig 6 legend "same as Figure 2"→"Figure 3"; Fig 4 legend "Refosco 2024"→"2025".
- **Formatting:** two plain "I2" → "I²" (Results, Discussion); residual British spellings → American (randomisation, recognised, favoured, specialised ×2, generalisable, unfavourable).

**Round-2 fixes applied per author decisions (2026-06-04):**
- **Feinsmith year unified to 2023** (DOI-verified: *J Vasc Access* 2023;24(4):630–8) — manuscript body ×4 + Supp Fig 2 legend, Table 1, Table 2, `data/meta_input.csv`, and the RoB (Figure 1) + HR (Supplementary Figure 2) figure labels regenerated.
- **Chronological reorder (R2.7) — Tables done:** Table 1 (15 study rows) and Table 2 (Part A RCTs; Part B Newcastle–Ottawa cohorts) reordered most-recent-first (year desc, author asc); forests already chronological. The **Results-narrative ordering remains yours to finalize in Word.**
- **Response letter corrected:** R2.6 abstract quote (dropped the non-existent "(5 RCTs, 9 cohorts)"); R2.7 figure numbering ("Figures 2–4" → 3–5) + tables-now-reordered; R2.8 figure scheme rewritten to the actual RoB=Fig 1 / PRISMA=Fig 2 / … / subgroup=Fig 6 layout.

- **Leroux enrollment corrected** (source-verified): now "enrolled 223 adult ED patients (222 PIVCs analyzed)" — 117 control PIVCs randomized, 116 analyzed (one unsuccessful insertion); 106 USG + 116 control = 222 PIVCs (consistent with Table 1 and the 78,591 total).

**Round-3 fixes applied (2026-06-04):**
- **Avelar denominator footnote** added to Table 1 (red): clarifies 382 venipunctures (188/194, shown in the table and the participant total) vs 339 catheters analyzed (161/178, the infiltration denominators).
- **Adult-subgroup leave-one-out caveat** added to the Conclusion (red): notes the adult signal is dominated by a single conference abstract (Saltarelli, ~50% weight) and that the leave-one-out analysis renders the pooled estimate non-significant (RR 1.18, 95% CI 0.88–1.58).
- **Results narrative reordered most-recent-first (R2.7 complete):** five passages reordered to match the tables — RCT characteristics, confounded-cohort list, RoB "some concerns" RCT list, NOS 6/9 & 5/9 lists, and the extravasation studies (which had been oldest-first). The catheter-failure and infiltration lists were already chronological. Reordered passages are red in the markup file.

Package is now internally complete: tables, figures, Results narrative, manuscript counts, and the response letter all reconciled and most-recent-first.

## Reproducibility / backups
Forests + RoB + PRISMA regenerated in R 4.5.3 from `data/meta_input.csv` (Avelar = study 15). Backups: `scripts/*_pre_revise_backup.R`, `data/meta_input_pre_avelar_backup.csv`. Pooled estimates order-invariant (display only) except infiltration (Avelar added).
