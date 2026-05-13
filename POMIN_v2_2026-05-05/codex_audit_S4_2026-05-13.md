# Codex Audit Report — Supplementary Material S4
**Date:** 2026-05-13
**Auditor:** Codex (codex-companion, fresh run)
**Files audited:**
- `/Users/chencc/Research/US-PIVC/POMIN_v2_2026-05-05/Supplementary Material S4 20260505.docx`
- `/Users/chencc/Research/US-PIVC/POMIN_v2_2026-05-05/manuscript 20260505.docx`
**Reference CSV:** `/Users/chencc/Research/US-PIVC/output/SupTable_LOO_catheter_failure.csv`

---

## BLOCKER — None

All 4 LOO rows in S4 docx match the CSV exactly:

| Study excluded | Weight in full model | Pooled RR [95% CI] | p-value | I² |
|---|---|---|---|---|
| Kleidon (2025) | 14.9% | 1.28 [1.02, 1.60] | 0.0316 | 0.0% |
| Shokoohi (2019) | 28.1% | 1.19 [0.93, 1.52] | 0.159 | 0.0% |
| Leroux (2023) | 7.2% | 1.23 [0.99, 1.52] | 0.0626 | 0.0% |
| Saltarelli (2015) | 49.8% | 1.18 [0.88, 1.58] | 0.277 | 0.0% |

**Saltarelli statement (numerically consistent, not verbatim — acceptable):**
- S4: "Saltarelli (2015) carried 49.8% of the full-model weight; removing it attenuated the pooled estimate to RR 1.18 (95% CI 0.88–1.58, p = 0.28)..."
- Manuscript: "removing Saltarelli et al. (2015), the largest contributor at 49.8% random-effects weight, attenuated the estimate to RR 1.18 (95% CI 0.88–1.58; p = 0.28)..."
- Verdict: ✓ consistent

**Full-model estimate (substantively consistent, display precision differs — see MEDIUM):**
- S4: "RR 1.225 (95% CI 0.995–1.508; p = 0.056; I² = 0.0%)"
- Manuscript: "RR was 1.23 (95% CI 0.995–1.508; p = 0.056; I² = 0%)"
- Verdict: ✓ consistent (1.225 rounds to 1.23; CI/p identical)

**Study names consistent:**
- S4: Kleidon 2025, Shokoohi 2019, Leroux 2023, Saltarelli 2015
- Manuscript: Kleidon et al. (2025), Leroux et al. (2023), Shokoohi et al. (2019), Saltarelli et al. (2015)
- Verdict: ✓ consistent

---

## HIGH — None

**Footnotes:** Standard and accurate.
- "CI, confidence interval; I², between-study heterogeneity statistic; LOO, leave-one-out; RR, risk ratio."
- "Model: DerSimonian–Laird random-effects on log(RR); single-study removal."
- "p-values are two-sided Wald-type tests on the pooled log-RR."

**Referenced files exist:**
- `/Users/chencc/Research/US-PIVC/scripts/04_meta_analysis.R` — ✓ confirmed present
- `/Users/chencc/Research/US-PIVC/output/SupTable_LOO_catheter_failure.csv` — ✓ confirmed present

---

## MEDIUM

**M1 — RR display precision not harmonized across S4 and manuscript (cosmetic only)**
- S4 uses "RR 1.225" (3 decimal places)
- Manuscript uses "RR 1.23" (2 decimal places)
- Both representations are arithmetically consistent; the CI and p-value are identical.
- Recommendation: Consider rounding S4 full-model display to "RR 1.23" for consistency. No scientific impact.

**M2 — p-value display: CSV raw value 0.277 rounded to "p = 0.28" in S4 narrative**
- S4 table cell: "0.277"; S4 narrative: "p = 0.28"; manuscript: "p = 0.28"
- Verdict: ✓ consistent with manuscript; standard rounding.

---

## LOW

**L1 — En-dash inconsistency is in the MANUSCRIPT, not S4**
- S4 correctly uses en-dash throughout: "DerSimonian–Laird", "0.995–1.508"
- Manuscript uses hyphen in multiple places: "DerSimonian-Laird"
- This is a pre-existing manuscript issue, not an S4 issue. Not in scope of this audit (manuscript cleared R7).

**L2 — No typos, awkward phrasing, or formatting glitches found in S4.**

---

## Verdict

✓ S4 consistent with manuscript — GREEN-LIGHT

All BLOCKER checks pass. The only actionable item is MEDIUM M1 (cosmetic precision harmonization of RR 1.225 → 1.23), which has zero scientific impact and may be left as-is at PI's discretion.
