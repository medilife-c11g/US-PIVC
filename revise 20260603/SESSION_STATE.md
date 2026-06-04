# US-PIVC Revision — Session State (saved 2026-06-04)

**Status:** Revision package for The Ultrasound Journal (#19152) is **BUILT, three-model-audited, and internally consistent.** All files are saved on disk in this folder. Remaining work = final Word formatting + EndNote refs + (optional) Codex 3rd-reviewer pass.

## Where everything is
Authoritative package: `~/Research/US-PIVC/revise 20260603/`. Upload set = `Manuscript_revised_CLEAN.docx` + `Manuscript_revised_MARKEDUP.docx` (my changes in **red**) + `Response_to_Reviewers.md` + Figures 1–6 + SupplementaryFigure 1–2 + Table1 + Table2 + Supplementary_Material_S1–S4. Full change log in `README_REVISION.md`.

## What's done (this session)
- **Avelar 2015** included via its English report (J Infus Nurs); 2013 Portuguese = excluded companion (NCT00930254). Totals: **15 studies / 6 RCTs / 9 cohorts / 78,591**.
- **PRISMA reconciled** from raw screening data (`data/screening_consensus_PI_Masuni.csv`): **19 assessed − 4 excluded = 15**. Figure 2 + Supplementary S3 + manuscript narrative all aligned at n=4.
- **Figure text-overlaps fixed** (Fig 3, Fig 4, Supp Fig 1, Supp Fig 2); all 8 figures overlap-free, 300 dpi.
- **3-model audit** (Claude ✓ + Gemini ✓ done; Codex ✗ auth-expired) → 18 mechanical fixes: CI unified **1.00–1.51**; Desai [15]→[14]; unclosed paren; "[14. 24]"→"[14, 24]"; Discussion figure cross-refs (incl. removing non-existent "Figure 7"×3); two "I2"→"I²"; British→American spellings.
- **Feinsmith → 2023** (DOI-verified: J Vasc Access 2023;24(4):630–8) everywhere — manuscript, Table 1, Table 2, `data/meta_input.csv`, and Figure 1 (RoB) + Supplementary Figure 2 (HR) regenerated.
- **R2.7 chronological reorder DONE:** Table 1 (15 rows), Table 2 (Part A RCTs / Part B cohorts), and 5 Results-narrative passages all most-recent-first.
- **Avelar Table 1 footnote** (382 venipunctures [188/194, total] vs 339 catheters [161/178, infiltration analysis]).
- **Adult-subgroup leave-one-out caveat** added to Conclusion (RR 1.18, 95% CI 0.88–1.58; Saltarelli ~50% weight).
- **Response letter corrected:** R2.6 abstract quote, R2.7 figure numbering, R2.8 figure scheme.
- **Leroux** corrected to "enrolled 223 patients (222 PIVCs analyzed)".

## Last verification (passed)
CLEAN = 0 red runs; MARKEDUP = 89 red runs; 0 sentinels; no residual "Feinsmith 2021" / "Figure 7"; all 15 authors + refs [5],[12]–[26] present; Table 1 year order 2025→2015; Response letter clean.

## Pending (author / next steps)
1. **Word formatting (R2 minor 5):** bold table titles + repeat header rows on each page; bring **Table 2 to one page**; reduce Table 1 font/line-spacing to limit page splits.
2. **EndNote:** add **[31]** Balduzzi S, Rücker G, Schwarzer G. *Evid Based Ment Health.* 2019;22(4):153–160 (meta); **[32]** Viechtbauer W. *J Stat Softw.* 2010;36(3):1–48 (metafor).
3. **Author Contributions** (title page / COI): T/A screening C.C.C. + Y.L.W.; full-text T.A.L. + Y.L.W. + C.C.C.
4. **Export** `Response_to_Reviewers.md` → .docx for upload.
5. **OPTIONAL:** Codex 3rd-reviewer pass (see below); fresh Claude+Gemini re-confirm on the final files.

## Codex re-launch note
Codex failed with **"session token expired."** To re-enable: open a terminal and run **`codex login`** (or the codex-companion login). The audit evidence bundle is persisted at **`_audit_bundle/`** (manuscript_clean.txt, table1/2, supp_s3, response, meta CSVs) — also still at `/tmp/pivc_review/`. Once logged in, ask me to "re-run the Codex integrity audit on `_audit_bundle/`".

## Backups (persistent, survive reboot)
- `_backups/` — pre-edit copies of manuscript (CLEAN/MARKEDUP), Table 1, Table 2, S3 at key checkpoints.
- Updated R scripts in `~/Research/US-PIVC/scripts/`: `04_meta_analysis.R`, `05_prisma_diagram.R`, `07_rob_visualization.R`. Data: `data/meta_input.csv` (Feinsmith 2023; Avelar = study 15). Backup `data/meta_input_pre_avelar_backup.csv`.
