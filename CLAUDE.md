# CLAUDE.md — Project Context for Claude Code

## Project
Systematic review and meta-analysis: "Post-insertion outcomes of ultrasound-guided versus landmark peripheral intravenous catheters"

## Authors
- PI: Chia-Ching Chen, MD (陳家慶) — Emergency Medicine, Changhua Show Chwan Memorial Hospital, Taiwan
- Second reviewer: Tai-An Lee, MD (LEE TAI AN)

## Key Parameters
- Search dates: 2000-01-01 to 2026-03-27
- Databases: PubMed, Embase, Cochrane CENTRAL, CINAHL
- PICO: USG-PIVC vs Landmark → post-insertion outcomes (dwell time, catheter failure, phlebitis, infiltration, occlusion, dislodgement, infection)
- Language: English and Chinese
- Study designs: RCTs and comparative cohort studies
- PROSPERO: CRD420261354170 (registered 2026-03-29)

## Pipeline Steps
1. `scripts/01_search_pubmed.py` — PubMed via Entrez API (email: c11g@hotmail.com)
2. `scripts/02_search_cochrane.py` — Generates search strings for Cochrane/Embase/CINAHL
3. `scripts/03_deduplicate.py` — Three-layer dedup (DOI → PMID → title Jaccard ≥0.85)
4. Manual: Rayyan screening by two independent reviewers
5. Manual: Data extraction into `data/extracted_data.csv`
6. `scripts/04_meta_analysis.R` — Random-effects MA with heterogeneity guard (I²>75% = no pooling)

## Rules
- NEVER delete files. Only create or edit.
- Always use zsh on macOS.
- R analysis uses packages: meta, metafor, dmetar.
- Python uses: biopython, pandas.

## Current Status (updated 2026-04-03)
- Search: ✅ Complete — 1,632 records across 4 databases, 1,359 after dedup
  - PubMed: 530 | Embase: 984 | Cochrane: 68 | CINAHL: 50
- Screening: ✅ Complete — Rayyan Review #1961147
  - Consensus: 17 Include, 0 Maybe, 1,342 Exclude
  - Masuni Wang (second reviewer) kappa=0.330, 95.8% agreement; 57 disagreements resolved (PI took precedence on remaining post-discussion conflicts)
  - Removed post-consensus: Avelar (Portuguese), oncology nurses (unpublished), ICU nurses DIVA (unpublished)
- Full-text retrieval: ✅ Complete — all PDFs found (Desai + Nishizawa added 2026-04-09)
  - ⚠️ Malik A excluded at full-text stage (single-arm, no landmark comparator)
- Detailed screening log: `output/screening_progress.md`, `output/screening_consensus.md`
- Full-text screening: ✅ Done — Malik excluded. 14 studies eligible (Cottrell & Refosco added 2026-04-04; Desai & Nishizawa added 2026-04-09).
- Data extraction: ✅ Done — `data/extracted_data.csv` + `data/meta_input.csv`
- Risk of bias: ✅ Done — `output/risk_of_bias.md`
- Meta-analysis: ✅ Done — Catheter failure RR 1.23 (1.00-1.51) NS; Dwell time k=3 I²=91.9% NOT POOLABLE
- Manuscript: ✅ Done — revised per Gemini critique (GRADE SoF, extravasation safety section, AI tool disclosure, CI precision)
- Tables/Figures: ✅ All PDF + CSV generated (Table 1-3, PRISMA flowchart, 6 forest plots)
- Supplementary: ✅ S1 search strategies, S2 excluded studies, S3 PRISMA checklist
- Cover letter + Title page: ✅ Target journal: The Ultrasound Journal (BMC)
- Next: Final review by Lee → Submit to Ultrasound Journal

## Target Journals
1. Journal of Vascular Access
2. Journal of Clinical Ultrasound
3. Journal of Infusion Nursing


## Sync Protocol
When ending a session or reaching conversation limit:
1. Update PROGRESS.md with latest status
2. Update screening_progress.md if screening decisions changed  
3. Generate sync_for_claude_app.md with current summary
4. Remind user to upload these files when starting new Claude App conversation
