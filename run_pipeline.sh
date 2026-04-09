#!/bin/bash
# ============================================================
# run_pipeline.sh
# USG-PIVC Post-Insertion Outcomes Meta-Analysis Pipeline
# ============================================================
#
# Usage:
#   ./run_pipeline.sh search      # Step 1: Run database searches
#   ./run_pipeline.sh dedup       # Step 2: Deduplicate results
#   ./run_pipeline.sh analyze     # Step 3: Run meta-analysis
#   ./run_pipeline.sh all         # Run all steps
#   ./run_pipeline.sh status      # Check pipeline status
#
# ============================================================

set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

header() {
    echo ""
    echo -e "${BLUE}════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  $1${NC}"
    echo -e "${BLUE}════════════════════════════════════════════════════════${NC}"
}

check_deps() {
    header "Checking Dependencies"
    local missing=0

    # Python
    if command -v python3 &>/dev/null; then
        echo -e "  ${GREEN}✓${NC} Python3: $(python3 --version 2>&1)"
    else
        echo -e "  ${RED}✗${NC} Python3 not found"
        missing=1
    fi

    # BioPython
    if python3 -c "import Bio" 2>/dev/null; then
        echo -e "  ${GREEN}✓${NC} BioPython installed"
    else
        echo -e "  ${YELLOW}!${NC} BioPython missing (run: pip install biopython)"
        missing=1
    fi

    # Pandas
    if python3 -c "import pandas" 2>/dev/null; then
        echo -e "  ${GREEN}✓${NC} Pandas installed"
    else
        echo -e "  ${YELLOW}!${NC} Pandas missing (run: pip install pandas)"
        missing=1
    fi

    # R
    if command -v Rscript &>/dev/null; then
        echo -e "  ${GREEN}✓${NC} R: $(Rscript --version 2>&1 | head -1)"
    else
        echo -e "  ${YELLOW}!${NC} R not found (needed for meta-analysis step)"
    fi

    # R packages
    if Rscript -e 'library(meta)' 2>/dev/null; then
        echo -e "  ${GREEN}✓${NC} R meta package installed"
    else
        echo -e "  ${YELLOW}!${NC} R meta package missing (run: Rscript scripts/install_r_packages.R)"
    fi

    return $missing
}

step_search() {
    header "Step 1: Database Searches"

    echo -e "\n${GREEN}[1/2] Running PubMed search...${NC}"
    python3 scripts/01_search_pubmed.py

    echo -e "\n${GREEN}[2/2] Generating Cochrane/Embase/CINAHL search strings...${NC}"
    python3 scripts/02_search_cochrane.py

    echo ""
    echo -e "${YELLOW}⚡ ACTION REQUIRED:${NC}"
    echo "   1. Open data/cochrane_search_string.txt"
    echo "   2. Run the search manually on Cochrane Library"
    echo "   3. Export results as RIS → data/cochrane_results.ris"
    echo ""
    echo "   4. Open data/embase_search_string.txt"
    echo "   5. Run the search on Embase via institutional access"
    echo "   6. Export results as RIS → data/embase_results.ris"
    echo ""
    echo "   7. Open data/cinahl_search_string.txt"
    echo "   8. Run the search on CINAHL via EBSCOhost"
    echo "   9. Export results as RIS → data/cinahl_results.ris"
    echo ""
    echo "   Then run: ./run_pipeline.sh dedup"
}

step_dedup() {
    header "Step 2: Deduplication"
    python3 scripts/03_deduplicate.py

    echo ""
    echo -e "${YELLOW}⚡ NEXT STEPS:${NC}"
    echo "   1. Upload output/merged_deduplicated.ris to Rayyan (rayyan.ai)"
    echo "   2. Two reviewers screen titles/abstracts independently"
    echo "   3. Resolve conflicts, document exclusion reasons"
    echo "   4. Full-text screening of included studies"
    echo "   5. Extract data into data/extracted_data.csv"
    echo "      (template: templates/data_extraction.csv)"
    echo ""
    echo "   Then run: ./run_pipeline.sh analyze"
}

step_analyze() {
    header "Step 3: Meta-Analysis"

    if [ ! -f "data/extracted_data.csv" ]; then
        echo -e "${YELLOW}⚠️  data/extracted_data.csv not found.${NC}"
        echo "   A template with example data will be created."
        echo ""
    fi

    Rscript scripts/04_meta_analysis.R

    echo ""
    echo -e "${GREEN}📊 Output files:${NC}"
    ls -la output/*.pdf output/*.csv 2>/dev/null || echo "  (no output files yet)"
}

step_status() {
    header "Pipeline Status"

    echo -e "\n  ${BLUE}Search Results:${NC}"
    for f in data/pubmed_results.ris data/cochrane_results.ris data/embase_results.ris data/cinahl_results.ris; do
        if [ -f "$f" ]; then
            lines=$(wc -l < "$f" 2>/dev/null)
            echo -e "    ${GREEN}✓${NC} $(basename $f) ($lines lines)"
        else
            echo -e "    ${RED}✗${NC} $(basename $f) — not found"
        fi
    done

    echo -e "\n  ${BLUE}Deduplication:${NC}"
    if [ -f "output/merged_deduplicated.ris" ]; then
        echo -e "    ${GREEN}✓${NC} Deduplicated file ready"
    else
        echo -e "    ${RED}✗${NC} Not yet deduplicated"
    fi

    if [ -f "output/prisma_numbers.json" ]; then
        echo -e "    ${GREEN}✓${NC} PRISMA numbers generated"
        python3 -c "
import json
with open('output/prisma_numbers.json') as f:
    d = json.load(f)
    print(f\"      Total identified: {d['identification']['total_identified']}\")
    print(f\"      After dedup: {d['deduplication']['records_after_dedup']}\")
" 2>/dev/null
    fi

    echo -e "\n  ${BLUE}Data Extraction:${NC}"
    if [ -f "data/extracted_data.csv" ]; then
        rows=$(tail -n +2 data/extracted_data.csv | grep -c -v "^$" 2>/dev/null || echo 0)
        echo -e "    ${GREEN}✓${NC} extracted_data.csv ($rows studies)"
    else
        echo -e "    ${RED}✗${NC} Not yet extracted"
    fi

    echo -e "\n  ${BLUE}Analysis Output:${NC}"
    n_pdf=$(ls output/*.pdf 2>/dev/null | wc -l)
    if [ "$n_pdf" -gt 0 ]; then
        echo -e "    ${GREEN}✓${NC} $n_pdf forest/funnel plots generated"
        ls output/*.pdf 2>/dev/null | while read f; do
            echo "      - $(basename $f)"
        done
    else
        echo -e "    ${RED}✗${NC} No analysis output yet"
    fi

    if [ -f "output/meta_analysis_summary.csv" ]; then
        echo -e "    ${GREEN}✓${NC} Summary table generated"
    fi
}

# ============================================================
# MAIN
# ============================================================
case "${1:-help}" in
    search)
        check_deps || true
        step_search
        ;;
    dedup)
        step_dedup
        ;;
    analyze)
        step_analyze
        ;;
    all)
        check_deps || true
        step_search
        echo -e "\n${YELLOW}Pausing... Complete manual searches before continuing.${NC}"
        echo "Run './run_pipeline.sh dedup' after adding all RIS files."
        ;;
    status)
        step_status
        ;;
    *)
        echo "USG-PIVC Post-Insertion Meta-Analysis Pipeline"
        echo ""
        echo "Usage: $0 {search|dedup|analyze|all|status}"
        echo ""
        echo "  search   — Run PubMed search + generate manual search strings"
        echo "  dedup    — Deduplicate results from all databases"
        echo "  analyze  — Run R meta-analysis (requires extracted_data.csv)"
        echo "  all      — Run search + dedup (manual steps needed in between)"
        echo "  status   — Check current pipeline status"
        ;;
esac
