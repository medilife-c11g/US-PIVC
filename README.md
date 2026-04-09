# USG-PIVC Post-Insertion Outcomes Meta-Analysis Pipeline

## Study Title
**Post-insertion outcomes of ultrasound-guided versus landmark peripheral intravenous catheters: A systematic review and meta-analysis of catheter dwell time, failure rate, and complications**

## Author Team
| Role | Name | Responsibility |
|------|------|---------------|
| First Author / PI | **Chia-Ching Chen, MD** | Study design, search, screening (R1), data extraction, analysis, manuscript |
| Second Reviewer | **Tai-An Lee, MD** | Screening (R2), data extraction verification, RoB assessment |

## Pipeline Overview

```
Step 1: Search     → PubMed, Embase, Cochrane (2000-01 to 2026-03-27)
Step 2: Deduplicate → Remove duplicates across databases
Step 3: Screen     → Export to Rayyan for title/abstract screening
Step 4: Extract    → Data extraction spreadsheet
Step 5: Analyze    → R meta-analysis with heterogeneity checks
Step 6: Report     → Forest plots, funnel plots, GRADE summary
```

## Quick Start

```bash
# 1. Install dependencies
pip install biopython pandas openpyxl --break-system-packages
Rscript scripts/install_r_packages.R

# 2. Run database searches
python scripts/01_search_pubmed.py
python scripts/02_search_cochrane.py
# For Embase: manual export required (see instructions below)

# 3. Deduplicate
python scripts/03_deduplicate.py

# 4. After screening & data extraction, run analysis
Rscript scripts/04_meta_analysis.R
```

## Directory Structure

```
US-PIVC/
├── README.md                  ← You are here
├── scripts/
│   ├── 01_search_pubmed.py    ← Automated PubMed search via Entrez API
│   ├── 02_search_cochrane.py  ← Cochrane CENTRAL search query generator
│   ├── 03_deduplicate.py      ← Cross-database deduplication
│   ├── 04_meta_analysis.R     ← Full meta-analysis with heterogeneity handling
│   └── install_r_packages.R   ← R package installer
├── data/                      ← Raw search results (auto-generated)
├── templates/
│   └── data_extraction.csv    ← Template for data extraction
└── output/                    ← Figures, tables, reports
```

## Embase Manual Search Instructions

Embase requires institutional access. Log in via your hospital library:

1. Go to https://www.embase.com
2. Click "Advanced Search"
3. Paste the search string from `data/embase_search_string.txt`
4. Set date: 2000-01-01 to 2026-03-27
5. Export as RIS → save to `data/embase_results.ris`
