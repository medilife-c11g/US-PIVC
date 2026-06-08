# US-PIVC — Resume Note (updated 2026-06-08)

## Where this project stands
**The Ultrasound Journal (SpringerOpen), Submission #19152 — in revision (R1 Accept; R2 Revisions Required).**
Resubmission is essentially ready. Po-Ming Chen produced a final-corrected version (`Submission #19152/`); I checked it against `Revision 0604/` and built a corrected, consistency-verified package.

### ✅ Ready-to-submit package: `~/Research/US-PIVC/Submission #19152_CORRECTED/`
20 files (Po-Ming's originals left untouched):
- `Manuscript_revised_CLEAN …docx` + `…MARKEDUP_CORRECTED …docx`
- `Table1_study_characteristics`, `Table2_risk_of_bias`, `Table3_GRADE_SoF`
- `Figure1_RiskOfBias` … `Figure6_subgroup_by_age`, `SupplementaryFigure1_extravasation`, `SupplementaryFigure2_time_to_event`
- `Supplementary_Material_S1`–`S4`
- `Response_to_Reviewers.docx` (already correct), `Title_Page.docx`

### Current verified numbers (no regression vs Revision 0604)
15 studies (6 RCT + 9 cohort), 78,591 participants. Catheter failure RR 1.23 (1.00–1.51, p=0.056, I²=0%); infiltration k=3 RR 1.30 (0.82–2.05); cohort subgroup RR 1.29 (1.02–1.63); RCT-only null. Table scheme: **T1=study characteristics, T2=RoB, T3=GRADE** (manuscript ↔ filenames ↔ captions all consistent). Figures: 1 RoB / 2 PRISMA / 3 catheter failure / 4 dwell / 5 infiltration / 6 subgroup; Supp Fig 1 extravasation, 2 time-to-event.

### What I fixed this session
Po-Ming had half-swapped the table numbering (broke it). I reverted the 2 GRADE callouts (Table 1→Table 3), renamed+relabelled the tables to the consistent scheme, produced the CLEAN manuscript, and passed a full-package consistency scan.

## ⏭ Remaining (author-only, before click-submit)
1. Confirm `Title_Page.docx` authors/affiliations are current (Po-Ming changed affiliation superscript to "1Department"; Title Page came from Revision 0604).
2. Confirm 2nd-reviewer initials standardised to **Y.L.W.** (Yu-Ling Wang) in Title Page + Author Contributions.
3. Upload the **CORRECTED** package to The Ultrasound Journal #19152 (do NOT use the broken `Submission #19152/` table set).

## Cross-session note (tools installed this session — already in MEMORY.md)
- **openevidence-mcp** registered (user-scope MCP `openevidence`); activates on Claude restart. Relay token in `~/Projects/openevidence-mcp/.env`; keep an OpenEvidence tab logged in + the relay extension loaded.
- **flowdoc** at `~/Projects/flowdoc` (+ our `prisma-2020-db-only` preset; PR open at htlin222/flowdoc#1).
- Skills installed globally: `audit-oe`, `research-guardian`.
- Separate paper finished this session: SCMJ carbon-emissions proof (4th proof) corrections + corrected Figures 2A/4A (2021 CT 2314→3313) in `~/Downloads/`.
