# POMIN_v2 Changes — applied 2026-05-05

Source: `POMIN/` (Po-Ming Chen revision dated 2026-05-05)  
Target: `POMIN_v2_2026-05-05/`  
Patch script: `scripts/apply_pomin_v2_patches.py`  
Codex audit: `notes/Codex_POMIN_audit_2026-05-05.md`

## H1–H5 fixes (blocking issues; auto-applied)

| ID | File | Fix | Status |
|---|---|---|---|
| **H1** | `Supplementary Material S3 20260505.docx` | Removed ICU-nurses unpublished row (excluded at adjudication, not full-text); renumbered 1–5; header changed `n=6 → n=5`. Now matches manuscript Methods "Five reports excluded" and `output/screening_consensus.md` | ✅ Auto |
| **H2** | `manuscript 20260505.docx` (title page) | Po-Ming Chen affiliation `4, 5` → `3, 4`. Affiliation #3 (Research Assistant Center, Show Chwan) now used; phantom #5 removed | ✅ Auto |
| **H3** | `manuscript 20260505.docx` (end matter) | Inserted full ICMJE-compliant **Authors' Contributions** section (POMIN had dropped it entirely) including Po-Ming Chen's role; added **Availability of Data and Materials** statement | ✅ Auto |
| **H4** | `manuscript 20260505.docx` (after Table 2) + `Supplementary Material S1 20260505.docx` | Added **Table 3. GRADE Summary of Findings** (5 outcome rows + footnote) inline after Table 2; updated S1 PRISMA checklist row "GRADE not formally assessed" → "Performed; see Manuscript Table 3" | ✅ Auto |
| **H5** | `Cover_Letter 20260505.docx` | CI string `1.00–1.51` → `0.99–1.51 (precise: 0.995–1.508; lower bound rounds to 1.00 at 2 dp but the unrounded interval crosses unity)` (matches authoritative R output: RR 1.225, 95% CI [0.9952, 1.5082], p=0.0556) | ✅ Auto |

## Bonus fixes (also auto-applied)

| ID | File | Fix |
|---|---|---|
| **M1** | `Cover_Letter 20260505.docx` | Added Generative AI Disclosure paragraph before signature (ICMJE 2024 / BMC compliant) |
| **M2** | `manuscript 20260505.docx` (title page) | Email typo `medlife.c11g@gmail.com` → `medilife.c11g@gmail.com` |
| **system hygiene** | `POMIN_v2_2026-05-05/` | Removed all macOS `Icon` / `.DS_Store` files |

## Round 2 — User-confirmed decisions, also auto-applied (2026-05-05)

| ID | Decision | Implementation |
|---|---|---|
| **M3** | Phone ext = 71297 (cover letter was correct) | Title page `ext:71299` → `ext:71297` |
| **M5** | Refosco NOS = 5/9 | NOS table: Selection 3→2, Total 6/9→5/9, key concern "Catheter type confounding" → "Catheter length confounding (64 mm vs 19–32 mm)" |
| **M6** | Jen-Tao Wang = Department of Surgery, Show Chwan (original affiliation; POMIN had broken to EM Chang Bing) | Author line `Jen-Tao Wang1` → `Jen-Tao Wang3`. Affiliation list restructured: #3 Surgery (new), #4 Research Assistant Center (was #3), #5 Nursing CTUST (was #4). Po-Ming Chen `3, 4` → `4, 5` |
| **M7** | RCT-only = RR 1.03 (95% CI 0.66–1.60), p = 0.91 (random-effects DL) | Updated 2 paragraphs (Results + Discussion); explicitly notes "random-effects DerSimonian-Laird, consistent with primary model" |

## Final affiliation list (POMIN_v2)

```
1  Department of Emergency Medicine, Chang Bing Show Chwan Memorial Hospital
2  Department of Gastroenterology, Chang Bing Show Chwan Memorial Hospital
3  Department of Surgery, Show Chwan Memorial Hospital, Changhua, Taiwan
4  Research Assistant Center, Show Chwan Memorial Hospital, Changhua, Taiwan
5  Department of Nursing, Central Taiwan University of Science and Technology, Taichung, Taiwan
```

Author line: `Tai-An Lee, MD¹,†, Yu-Ling Wang²,†, Jen-Tao Wang³, Po-Ming Chen⁴,⁵, Chia-Ching Chen¹*`

## Patch scripts (audit trail)

- Round 1 (H1–H5 + M1, M2): `scripts/apply_pomin_v2_patches.py`
- Round 2 (M3, M5, M6, M7): `scripts/apply_pomin_v2_patches_round2.py`

## Verifications you should do in Word before submission

1. Open `manuscript 20260505.docx` and check:
   - Title page: Po-Ming Chen reads "3, 4"; corresponding email reads `medilife.c11g@gmail.com`
   - End matter sequence: Funding → COI → **Authors' Contributions** → **Data Availability** → AI use
   - **Table 3 (GRADE)** appears after Table 2 with 5 outcome rows
2. Open `Cover_Letter 20260505.docx` and check:
   - Bullet 1 has the expanded CI text
   - **Generative AI Disclosure** paragraph sits just before "Sincerely,"
3. Open `Supplementary Material S3 20260505.docx` and check:
   - Header reads `(n = 5)`
   - Excluded studies table rows numbered 1–5 (no ICU-nurses row)
4. Add Word **line numbers** (Layout → Line Numbers → Continuous) before submitting to BMC.

## New deliverable

`figures/Figure7_RoB_Summary.pdf` (and .png) — 3-panel risk-of-bias visualization:
- Panel A: Cochrane RoB 2 traffic-light for 5 RCTs
- Panel B: NOS heatmap for 9 cohorts (star-fraction colour-coded by Cochrane palette)
- Panel C: Combined overall-risk distribution bar (RoB 2 + NOS side-by-side)

Optional addition: cite as "**Figure 7**" inline after Table 2 RoB description in the manuscript Results.

---

## Round 3-6 patches (2026-05-06)

| Round | Issue source | Fix | Verified by |
|---|---|---|---|
| **R3** | Codex Round 2 audit (3 HIGH residuals) | Affiliation superscript split (3 lines); Refosco 5/9 in body; 6 unbracketed citations bracketed; S1 GRADE residual; AI disclosure unified; I² standardization | Codex Round 3 audit |
| **R4** | Codex Round 3 audit (2 cite + 1 fragment) | `prevalence11`→`[11]`; `systematic reviews4-6`→`[4-6]`; `adjusted HRV.`→`adjusted HR.` (POMIN-introduced bug, restored to original) | Codex Round 4 audit |
| **R5** | Codex Round 4 audit (3 cites in Discussion) | `tissue.10`→`[10]`; `vein.10`→`[10]`; `failure.7`→`[7]` | Codex Round 5 audit + manual sweep |
| **R6** | Codex Round 5 audit (refs 13/14 never bracket-cited) | Added "(Desai et al., 2018 [14]; Nishizawa et al., 2020 [13])" at first mention | Codex Round 6 audit |

## Final Codex verdict

🟢 **SUBMISSION READY** — all 15 references properly bracket-cited; no remaining unbracketed inline citations; no stranded text fragments; all numerical values internally consistent; affiliations correctly superscripted; AI disclosure harmonized; Refosco NOS = 5/9 consistent across Table 2 / body text / Figure 7.

## Patch scripts (full audit trail)

- R1 + bonus: `scripts/apply_pomin_v2_patches.py` (H1-H5 + M1, M2)
- R2: `scripts/apply_pomin_v2_patches_round2.py` (M3, M5, M6, M7)
- R3: `scripts/apply_pomin_v2_patches_round3.py` (HIGH residuals: superscript / Refosco / cites / S1 / AI / I²)
- R4-R6: applied inline (small fixes, no separate script)
