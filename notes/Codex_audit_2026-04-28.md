Read-only audit completed. Ranked substantive risks:

1. **BLOCKER: Screening/PRISMA process is internally inconsistent**
Evidence: Manuscript says any record included by either reviewer proceeded to full text, with 57 disagreements resolved by PI ([output/manuscript_draft.md](/Users/chencc/Research/US-PIVC/output/manuscript_draft.md:48)). But screening consensus says union rule yielded 72 records to full text, while only 17 were actually full-text screened ([output/screening_consensus.md](/Users/chencc/Research/US-PIVC/output/screening_consensus.md:88), [output/screening_consensus.md](/Users/chencc/Research/US-PIVC/output/screening_consensus.md:89)).
Fix: Reconcile the screening flow. Either remove the “union rule” claim or explain how 72 union-included records were reduced to 17 before full-text retrieval. Prefer adjudication by consensus or third reviewer, not “PI took precedence.”

2. **BLOCKER: Mixed RCT/cohort pooling is not quantitatively defended**
Evidence: Primary catheter failure pools 2 RCTs and 2 cohorts ([output/manuscript_draft.md](/Users/chencc/Research/US-PIVC/output/manuscript_draft.md:102), [output/manuscript_draft.md](/Users/chencc/Research/US-PIVC/output/manuscript_draft.md:204)). Methods claim pre-specified subgroup by study design ([output/manuscript_draft.md](/Users/chencc/Research/US-PIVC/output/manuscript_draft.md:68)), but the script only implements RCT-only sensitivity and age subgroup, not design subgroup/meta-regression ([scripts/04_meta_analysis.R](/Users/chencc/Research/US-PIVC/scripts/04_meta_analysis.R:258), [scripts/04_meta_analysis.R](/Users/chencc/Research/US-PIVC/scripts/04_meta_analysis.R:282)).
Fix: Add design-stratified results for catheter failure at minimum: RCT-only, cohort-only, and subgroup interaction if feasible. If underpowered, state that design heterogeneity could not be reliably quantified and downgrade certainty.

3. **HIGH: “No pooling if I² >75%” is contradicted by outputs**
Evidence: Methods say outcomes with I² >75% were not pooled ([output/manuscript_draft.md](/Users/chencc/Research/US-PIVC/output/manuscript_draft.md:66)). But the script still computes and plots random-effects pooled dwell time and extravasation estimates ([scripts/04_meta_analysis.R](/Users/chencc/Research/US-PIVC/scripts/04_meta_analysis.R:134), [scripts/04_meta_analysis.R](/Users/chencc/Research/US-PIVC/scripts/04_meta_analysis.R:211)), and the summary CSV reports pooled estimates while marking them “No” for poolable ([output/meta_analysis_summary.csv](/Users/chencc/Research/US-PIVC/output/meta_analysis_summary.csv:3), [output/meta_analysis_summary.csv](/Users/chencc/Research/US-PIVC/output/meta_analysis_summary.csv:5)).
Fix: For non-poolable outcomes, suppress pooled diamonds/summary estimates or clearly label them “exploratory only, not used for inference.” State whether the I² >75% rule was in PROSPERO/SAP; if not, call it post hoc.

4. **HIGH: AI/tool disclosure is missing despite project evidence of AI use**
Evidence: Project notes say manuscript revised per Gemini critique and AI disclosure added ([CLAUDE.md](/Users/chencc/Research/US-PIVC/CLAUDE.md:46)); progress log documents AI-assisted peer review via ChatGPT ([PROGRESS.md](/Users/chencc/Research/US-PIVC/PROGRESS.md:132)). The manuscript only lists funding and conflicts, with no AI declaration ([output/manuscript_draft.md](/Users/chencc/Research/US-PIVC/output/manuscript_draft.md:368), [output/manuscript_draft.md](/Users/chencc/Research/US-PIVC/output/manuscript_draft.md:370)).
Fix: Add an ICMJE/Springer-compatible declaration specifying which AI tools were used, for what tasks, and that authors verified all content and take responsibility.

5. **HIGH: Risk-of-bias documentation is stale/incomplete**
Evidence: Standalone RoB file only details 4 RCTs and 6 cohorts; it omits Nishizawa, Cottrell, Refosco, and Desai from detailed assessments ([output/risk_of_bias.md](/Users/chencc/Research/US-PIVC/output/risk_of_bias.md:6), [output/risk_of_bias.md](/Users/chencc/Research/US-PIVC/output/risk_of_bias.md:50), [output/risk_of_bias.md](/Users/chencc/Research/US-PIVC/output/risk_of_bias.md:102)). Manuscript/table CSV include those later additions ([output/table2a_rob2_rcts.csv](/Users/chencc/Research/US-PIVC/output/table2a_rob2_rcts.csv:6), [output/table2b_nos_cohorts.csv](/Users/chencc/Research/US-PIVC/output/table2b_nos_cohorts.csv:8)).
Fix: Update `risk_of_bias.md` with full domain-level assessments for all 14 studies. Make manuscript, CSV, PDF, and supplement match.

6. **HIGH: GRADE table has stale and incorrect rows**
Evidence: Manuscript says extravasation is 3 studies but misclassifies it as 1 RCT + 2 cohorts ([output/manuscript_draft.md](/Users/chencc/Research/US-PIVC/output/manuscript_draft.md:207)); actually Bridey and Nishizawa are RCTs and Favot is cohort ([data/meta_input.csv](/Users/chencc/Research/US-PIVC/data/meta_input.csv:3), [data/meta_input.csv](/Users/chencc/Research/US-PIVC/data/meta_input.csv:7), [data/meta_input.csv](/Users/chencc/Research/US-PIVC/data/meta_input.csv:14)). The CSV/PDF GRADE output is older: extravasation k=2 and I²=96.7%, dwell time k=2 with pooled MD ([output/table3_grade_sof.csv](/Users/chencc/Research/US-PIVC/output/table3_grade_sof.csv:3), [output/table3_grade_sof.csv](/Users/chencc/Research/US-PIVC/output/table3_grade_sof.csv:5)).
Fix: Regenerate Table 3 from current data. Consider separating RCT and observational certainty or explicitly explaining how mixed-design GRADE certainty was derived.

7. **HIGH: Largest-study/influence analysis is insufficient**
Evidence: Included population is dominated by Feinsmith n=43,470 and Favot n=29,508 ([data/meta_input.csv](/Users/chencc/Research/US-PIVC/data/meta_input.csv:4), [data/meta_input.csv](/Users/chencc/Research/US-PIVC/data/meta_input.csv:7)). Primary catheter failure is dominated by Saltarelli numerically, n=2,688 of 3,404 ([data/meta_input.csv](/Users/chencc/Research/US-PIVC/data/meta_input.csv:11)); manuscript only reports removal of Kleidon, not the largest/most influential study ([output/manuscript_draft.md](/Users/chencc/Research/US-PIVC/output/manuscript_draft.md:104)).
Fix: Add leave-one-out table for catheter failure, plus “remove largest study/highest weight” analyses for catheter failure, HR failure, and extravasation. Report whether conclusions survive removal of Saltarelli, Feinsmith, and Favot.

8. **MEDIUM: Borderline RR language is improved but still overstates certainty**
Evidence: Manuscript correctly notes precise CI crosses unity and HKSJ is secondary ([output/manuscript_draft.md](/Users/chencc/Research/US-PIVC/output/manuscript_draft.md:102)). But Discussion says USG and landmark “perform equivalently” ([output/manuscript_draft.md](/Users/chencc/Research/US-PIVC/output/manuscript_draft.md:144)), and conclusion says the review “demonstrates” no improvement ([output/manuscript_draft.md](/Users/chencc/Research/US-PIVC/output/manuscript_draft.md:174)).
Fix: Replace equivalence language with “no statistically significant difference was detected” and “evidence does not support a post-insertion benefit.” Do not imply equivalence without an equivalence margin.

9. **MEDIUM: HKSJ/REML is labelled pre-specified without local evidence**
Evidence: Manuscript calls REML/HKSJ pre-specified in abstract/methods/results ([output/manuscript_draft.md](/Users/chencc/Research/US-PIVC/output/manuscript_draft.md:16), [output/manuscript_draft.md](/Users/chencc/Research/US-PIVC/output/manuscript_draft.md:102)). Progress log says it was added on April 18 after the April 9 meta-analysis run ([PROGRESS.md](/Users/chencc/Research/US-PIVC/PROGRESS.md:34)).
Fix: Verify PROSPERO/SAP. If absent, call it “post hoc sensitivity analysis” or “additional sensitivity analysis,” and keep DL as primary.

10. **MEDIUM: Stale numbers still leak through submission materials**
Evidence: Title page says Table 1 has 12 studies ([output/title_page.md](/Users/chencc/Research/US-PIVC/output/title_page.md:39)); current manuscript/data say 14 ([output/manuscript_draft.md](/Users/chencc/Research/US-PIVC/output/manuscript_draft.md:18), [data/meta_input.csv](/Users/chencc/Research/US-PIVC/data/meta_input.csv:15)). CLAUDE still mentions an AI co-reviewer kappa 0.216 ([CLAUDE.md](/Users/chencc/Research/US-PIVC/CLAUDE.md:37)), conflicting with current kappa 0.330.
Fix: Run a final consistency sweep across title page, CSV tables, PDFs, supplements, and project docs before submission. Search specifically for `12`, `11`, `96.7`, `0.216`, `AI co-reviewer`, and old k values.

Publication bias is mostly defensible as written: max k per pooled outcome is 4, so Egger/Begg is not appropriate despite 14 total studies. I would tighten the wording to say “fewer than 10 studies contributed to any outcome-specific meta-analysis,” which the manuscript already nearly does ([output/manuscript_draft.md](/Users/chencc/Research/US-PIVC/output/manuscript_draft.md:164)).

Codex session ID: 019dd269-6697-7993-9c3f-6fc62c3dd2c7
Resume in Codex: codex resume 019dd269-6697-7993-9c3f-6fc62c3dd2c7
