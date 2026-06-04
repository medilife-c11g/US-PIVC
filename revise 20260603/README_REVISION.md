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

## Round-4 — Codex third-reviewer audit (2026-06-04, on refreshed `_audit_bundle/`)
Codex re-ran successfully. Many findings were extraction artifacts (verified false): Table 2 RoB rows ARE complete; Avelar/Desai Table 1 rows are NOT column-shifted. **Verified-real fixes applied:**
- British spellings normalized in the **tables** (Table 1 "Paediatric" ×9 → Pediatric, "centre" → center; Table 2 "Randomisation" → Randomization) and manuscript "visualising" → "visualizing".
- Avelar's Table 1 Study cell → **"Avelar AF [5]"** (was "Avelar et al." — now matches the "Author [ref]" format of every other row).
- `data/meta_input.csv` Refosco year 2024 → **2025** (manuscript/tables/ref were already 2025).
- Response letter: replaced placeholder "[updated participant total]" → **78,591**; corrected example ref numbers "[16]/[17]" → **[22]/[23]**.
- Results cohort-highlights sentence reordered most-recent-first (Feinsmith 2023 → Cottrell 2021 → Shokoohi 2019).
- Removed a citation I had introduced that was **wrong**: the clause calling reference [11] a "J Vasc Access 2022 conference abstract" — reference [11] is actually *Kleidon TM et al., a systematic review/meta-analysis, J Paediatr Child Health 2022;58(6):953–61*. Clause softened to "a further overlapping EPIC conference abstract …" with no (mismatched) citation.

## ⚠ Open items needing YOUR EndNote master / a judgment call (NOT changed)
1. **Reference [11] is now uncited** after the fix above. In your EndNote master, decide whether to (a) cite the Kleidon J Paediatr Child Health 2022 SR/MA [11] where appropriate (e.g., among the prior systematic reviews), or (b) remove it; and if you want to cite the Kleidon *J Vasc Access* EPIC conference abstract, add it as a new reference (it is not currently in the list).
2. **Unbracketed / possibly-mis-numbered citations** (EndNote-layer): "…high exclusion prevalence**11** rather than…" and "…three prior USG-PIVC systematic reviews **4-6**…" are not bracketed like the rest, and given [5] = Avelar (a primary RCT) the "[4-6] = systematic reviews" mapping looks wrong. Verify these citation numbers/brackets against your EndNote library.
3. ✅ **RESOLVED (your call: delete).** The extravasation pooled RR 2.75 was removed; the Results now state "these three studies were not pooled (I² = 95.7%) and no summary estimate is reported," consistent with the I²>75% rule.
4. ✅ **RESOLVED (your call: convert).** Study Limitations is now a true numbered list (1.–10.), replacing the "First… Finally…" prose. Content unchanged.
5. ✅ **RESOLVED (your call: reorder).** Both Discussion confounded-cohort lists ("Studies with Major Confounding" paragraph + the Discussion sentence) reordered most-recent-first (Refosco 2025 → Dachepally 2023 → Desai 2018 → Paladini 2018). R2.7 now fully satisfied throughout Results + Discussion.

**Items 1–2 above — RESOLVED 2026-06-04 (PubMed-verified, no fabrication):**
- **Conclusion insertion-advantage sentence** now cites **[6, 27]** (van Loon 2018 + Stolz 2015 — adult USG-PIVC SR/MAs already in the list; "adult evidence only" per author).
- **"[4-6]" fixed → "[4, 6, 27]"** in both the Intro and the Limitations (Egan + van Loon + Stolz = three genuine SR/MAs; removes the wrongly-swept-in Avelar [5] RCT, adds the omitted Stolz [27]) — now consistent with the Discussion, which already used [4, 6, 27].
- **Reference [11]** (Kleidon 2022 J Paediatr Child Health pediatric SR/MA) is now cited once, accurately, in the Intro: "…though findings in general pediatric populations have been less consistent [11]" (it found *no* significant pediatric first-attempt difference). No longer orphaned.
- **"prevalence11" (κ-paradox) fixed → "[33]"** = a new, correct methods reference **Byrt T, Bishop J, Carlin JB. Bias, prevalence and kappa. J Clin Epidemiol. 1993;46(5):423-9** (DOI 10.1016/0895-4356(93)90018-v; the PABAK source) — added to the reference list as [33]. Replaces the erroneous Kleidon-SR citation.
- **Conclusion sentence third ref added:** now **[6, 27, 34]** — added **[34] Tran QK, Fairchild M, Yardi I, Mirda D, Markin K, Pourmand A. Efficacy of Ultrasound-Guided Peripheral Intravenous Cannulation versus Standard of Care: A Systematic Review and Meta-analysis. Ultrasound Med Biol. 2021;47(11):3068-78** (adult ED, first-attempt OR 2.1; DOI 10.1016/j.ultrasmedbio.2021.07.002).
- ⏭ In your EndNote master: add **[33] Byrt 1993** and **[34] Tran 2021** (both PubMed-verified above); EndNote will finalize numbering. Egan/van Loon/Stolz are already in your library ([4]/[6]/[27]).

## Round-5 — three-way scientific-soundness audit (2026-06-04)
Codex + Claude completed (both verdict: **"sound with revisions"** — statistically reproducible, honest about fragility, correct epistemic stance); **Gemini hit its free-tier quota** (not run). All pooled estimates independently re-verified as correct. Resolutions applied per author decisions:
- **GRADE formally applied & included (decision A):** new **`Table3_GRADE_SoF.docx`** (Summary of Findings, current values: catheter failure Low; dwell/infiltration/extravasation/time-to-event Very low) added to the upload set; a GRADE-methods sentence added to Methods (cites [30] + Table 3); Limitations now references "(Table 3)"; **Supplementary S1 PRISMA checklist items 15 & 22 corrected** (were "GRADE not applied" → now "GRADE applied; see Table 3"). Resolves the text-vs-checklist contradiction both reviewers flagged as #1.
- **RCT-only p corrected:** "p = 0.88" → **"p = 0.91"** (re-verified in R: k=2, RR 1.03 [0.66,1.60]).
- **Design-stratification — strengthened annotation (not restructured):** the primary catheter-failure Results now states the borderline signal "arose predominantly from the cohort studies; the RCT-only estimate was null (RR 1.03)" at the point of the result. (Rationale: the k=4 mixed pool was the pre-specified PROSPERO primary; keeping it but flagging the cohort-driven/RCT-null divergence addresses the reviewers without an underpowered k=2 RCT-only headline.)
- **Circularity caveat added (Conclusion):** the "no consistent benefit / catheter selection is the primary determinant" interpretation is now explicitly stated as "conditional on our classification of four catheter-specification-confounded studies and their exclusion from the primary pooled analyses."

**Round-5 follow-ups — RESOLVED 2026-06-04:**
- **"warranted.15" miscitation fixed** → "narrower than warranted **[35]**." Added **[35] IntHout J, Ioannidis JPA, Borm GF. The HKSJ method… considerably outperforms the standard DerSimonian-Laird method. BMC Med Res Methodol. 2014;14:25** (DOI 10.1186/1471-2288-14-25) — the correct small-k methods reference (was wrongly citing [15] Nishizawa, an RCT).
- **REML/HKSJ asymmetry fixed:** infiltration sensitivity now run and reported — **RR 1.33 (95% CI 0.62–2.85; p = 0.25)**, consistent with the DL estimate (RR 1.30 [0.82–2.05]); added to the infiltration Results and to `04_meta_analysis.R` (code now matches the methods text).
- ⏭ EndNote: also add **[35] IntHout 2014** (PubMed-verified). Reference list now [1]–[35] (new this revision: [31] Balduzzi, [32] Viechtbauer, [33] Byrt, [34] Tran, [35] IntHout).
- **Gemini (gemini-2.5-flash) third reviewer — completed, but its lone CRITICAL finding is a VERIFIED FALSE POSITIVE.** Flash claimed the REML+HKSJ p=0.047 was unreproducible because "the code uses `hakn=FALSE` throughout `metagen()` calls." In fact the script uses `metabin(..., method.tau="REML", hakn=TRUE)` (lines 114, 206), and the catheter-failure HKSJ result reproduces exactly: **RR 1.225 [1.005, 1.493], p = 0.0470**. Flash also hallucinated a nonexistent "Adhikari 2020" study and an incorrect PROSPERO ID. Its non-hallucinated points (Scopus/WoS omission; κ=0.330 + PI adjudication; RCTs-with-cohorts pooling; adult-subgroup caution; confounding-causal-vs-observational) duplicate Codex/Claude and are already addressed/acknowledged. **Net: no new valid actionable finding; the robust verdict from the two reliable reviewers (Codex + Claude) stands at "sound with revisions," with all substantive items now resolved.**

## Round-6 — figure-title/data fixes + Author Contributions (2026-06-04)
- **Embedded figure-number titles corrected:** `Figure1_RiskOfBias.png` said "**Figure 7.** …" → now "**Figure 1.** …"; `Figure2_PRISMA.png` said "**Figure 1.** PRISMA…" → now "**Figure 2.** PRISMA…". (Forest plots Figures 3–6 + Supp 1–2 use `smlab`, not an embedded number, so were already correct.)
- **RoB figure data synced to Table 2:** the NOS panel had stale "**Refosco 2024, 5/9 (Selection 2)**" → corrected to "**Refosco 2025, 6/9 (Selection 3)**" to match Table 2 and the manuscript narrative. ✅ RESOLVED 2026-06-04: full NOS re-scored from the Refosco PDF = Selection 3 / Comparability 1 / Outcome 2 = **6/9**, confirming Table 2 + Figure 1 + narrative. The April `risk_of_bias.md` 5/9 was the outlier (would make Refosco inconsistent with the identically catheter-confounded Dachepally 6/9 and Paladini 6/9). No change needed.
- **Figure scheme now fully consistent** across file names, embedded titles, in-text callouts, and legends: 1 = Risk of bias; 2 = PRISMA; 3 = catheter failure; 4 = dwell time; 5 = infiltration; 6 = catheter failure by age subgroup; Supp 1 = extravasation; Supp 2 = time-to-event.
- **Author Contributions updated** (in `output/title_page.md` and a new `Title_Page.docx` in this folder) to match the corrected screening process: title/abstract screening = C.C.C. + Y.L.W.; full-text eligibility = T.A.L. + Y.L.W., adjudicated by C.C.C. Also fixed the title page's stale figure/table/supplement descriptions ("[14 studies]" → 15; "Figure 1: PRISMA" → correct scheme; 3 → 4 supplements + 2 supp figures).
- **Upload set is now 19 files** (added `Title_Page.docx`).
- **Figure 1A traffic-light labels fixed:** robvis was rendering the RCT study labels rotated 90° in a narrow strip and truncating them ("…idon 20", "…idey 20"). Replaced robvis `rob_traffic_light()` with a custom ggplot traffic-light in `07_rob_visualization.R` — study names now render as full **horizontal** left labels; RoB-2 judgments unchanged (match Table 2); domain key added as a subtitle.
- **Figure 1 both panels reordered most-recent-first (R2.7), matching Table 2:** Part A (RCTs) = Kleidon 2025 → Varghese 2025 → Leroux 2023 → Nishizawa 2020 → Bridey 2018 → Avelar 2015; Part B (cohorts) = Refosco 2025 → Dachepally 2023 → Feinsmith 2023 → Cottrell 2021 → Favot 2019 → Shokoohi 2019 → Desai 2018 → Paladini 2018 → Saltarelli 2015.

## Reproducibility / backups
Forests + RoB + PRISMA regenerated in R 4.5.3 from `data/meta_input.csv` (Avelar = study 15). Backups: `scripts/*_pre_revise_backup.R`, `data/meta_input_pre_avelar_backup.csv`. Pooled estimates order-invariant (display only) except infiltration (Avelar added).
