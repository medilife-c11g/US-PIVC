# Claude Code Sync Instructions
# Run the following commands in Claude Code to update your pipeline

# 1. Copy screening_progress.md to the pipeline
cp ~/Downloads/screening_progress.md ~/Research/US-PIVC/output/screening_progress.md

# 2. Ask Claude Code to update PROGRESS.md with:
#    - PROSPERO: CRD420261354170 (registered 2026-03-28) ✅
#    - PubMed: 530 ✅
#    - Cochrane: 68 ✅ 
#    - Embase: 984 ✅
#    - CINAHL: 50 ✅
#    - Deduplication: 1,632 → 1,359 unique ✅
#    - Rayyan: Review ID 1961147, blind mode ON, 2 reviewers active ✅
#    - Title/abstract screening: IN PROGRESS
#    - Included so far: ~10 studies
#    - Maybe: ~5 studies
#    - Screening rules documented in screening_progress.md

# 3. Tell Claude Code:
# "Please read ~/Research/US-PIVC/output/screening_progress.md 
#  and update PROGRESS.md accordingly. 
#  Also update CLAUDE.md with the current screening status."
