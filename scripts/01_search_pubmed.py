#!/usr/bin/env python3
"""
01_search_pubmed.py
PubMed search for USG-PIVC post-insertion outcomes meta-analysis
Search period: 2000/01/01 - 2026/03/27
"""

import os
import sys
import json
import time
from datetime import datetime

try:
    from Bio import Entrez, Medline
except ImportError:
    print("ERROR: biopython not installed. Run:")
    print("  pip install biopython --break-system-packages")
    sys.exit(1)

# ============================================================
# CONFIGURATION
# ============================================================
Entrez.email = "c11g@hotmail.com"
Entrez.api_key = None  # Optional: NCBI API key for faster queries

SEARCH_DATE_MIN = "2000/01/01"
SEARCH_DATE_MAX = "2026/03/27"

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================
# SEARCH STRATEGY
# ============================================================
# Block 1: Ultrasound
BLOCK_US = (
    '"Ultrasonography"[MeSH] OR "ultrasound"[tiab] OR "ultrasonograph*"[tiab] '
    'OR "sonograph*"[tiab] OR "POCUS"[tiab] OR "point-of-care ultrasound"[tiab] '
    'OR "echograph*"[tiab] OR "US-guided"[tiab] OR "USG"[tiab] '
    'OR "ultrasound-guided"[tiab] OR "echo-guided"[tiab]'
)

# Block 2: Peripheral IV
BLOCK_PIV = (
    '"Catheterization, Peripheral"[MeSH] OR "peripheral intravenous"[tiab] '
    'OR "peripheral venous catheter*"[tiab] OR "peripheral IV"[tiab] '
    'OR "PIVC"[tiab] OR "PIV"[tiab] OR "peripheral vascular access"[tiab] '
    'OR "peripheral venous access"[tiab] OR "peripheral cannulat*"[tiab] '
    'OR "intravenous cannulat*"[tiab] OR "venipuncture"[tiab] '
    'OR "venepuncture"[tiab] OR "short peripheral catheter"[tiab] '
    'OR "USGIV"[tiab] OR "USGPIV"[tiab] OR "USG-PIVC"[tiab]'
)

# Block 3: Post-insertion outcomes (KEY differentiator)
BLOCK_OUTCOMES = (
    '"Equipment Failure"[MeSH] OR "Phlebitis"[MeSH] '
    'OR "Catheter-Related Infections"[MeSH] '
    'OR "dwell time"[tiab] OR "catheter survival"[tiab] '
    'OR "catheter failure"[tiab] OR "catheter longevity"[tiab] '
    'OR "catheter durability"[tiab] OR "catheter complication*"[tiab] '
    'OR "post-insertion"[tiab] OR "phlebitis"[tiab] '
    'OR "infiltration"[tiab] OR "extravasation"[tiab] '
    'OR "occlusion"[tiab] OR "dislodgement"[tiab] '
    'OR "dislodgment"[tiab] OR "catheter patency"[tiab] '
    'OR "catheter-related infection"[tiab] '
    'OR "thrombophlebitis"[tiab] '
    'OR "premature removal"[tiab] OR "unplanned removal"[tiab] '
    'OR "catheter-related bloodstream"[tiab] '
    'OR "device failure"[tiab] OR "catheter malfunction"[tiab]'
)

FULL_QUERY = (
    f"({BLOCK_US}) AND ({BLOCK_PIV}) AND ({BLOCK_OUTCOMES}) "
    f"AND (\"{SEARCH_DATE_MIN}\"[Date - Publication] : \"{SEARCH_DATE_MAX}\"[Date - Publication])"
)

# ============================================================
# FUNCTIONS
# ============================================================
def search_pubmed(query):
    """Search PubMed and return list of PMIDs."""
    print(f"[{datetime.now():%H:%M:%S}] Searching PubMed...")
    print(f"  Query length: {len(query)} characters")

    handle = Entrez.esearch(
        db="pubmed",
        term=query,
        retmax=10000,
        usehistory="y"
    )
    results = Entrez.read(handle)
    handle.close()

    count = int(results["Count"])
    id_list = results["IdList"]
    print(f"  Found: {count} results")

    return id_list, results.get("WebEnv"), results.get("QueryKey")


def fetch_records(id_list, webenv=None, query_key=None, batch_size=100):
    """Fetch full records from PubMed in batches."""
    all_records = []
    total = len(id_list)

    print(f"[{datetime.now():%H:%M:%S}] Fetching {total} records...")

    for start in range(0, total, batch_size):
        end = min(start + batch_size, total)
        print(f"  Batch {start+1}-{end} of {total}...")

        if webenv and query_key:
            handle = Entrez.efetch(
                db="pubmed",
                rettype="medline",
                retmode="text",
                retstart=start,
                retmax=batch_size,
                webenv=webenv,
                query_key=query_key
            )
        else:
            batch_ids = id_list[start:end]
            handle = Entrez.efetch(
                db="pubmed",
                id=batch_ids,
                rettype="medline",
                retmode="text"
            )

        records = list(Medline.parse(handle))
        handle.close()
        all_records.extend(records)

        time.sleep(0.4)  # Respect NCBI rate limits

    return all_records


def records_to_ris(records, filename):
    """Convert MEDLINE records to RIS format for Rayyan import."""
    ris_lines = []
    for rec in records:
        ris_lines.append("TY  - JOUR")
        ris_lines.append(f"TI  - {rec.get('TI', '')}")

        for author in rec.get("AU", []):
            ris_lines.append(f"AU  - {author}")

        ris_lines.append(f"JO  - {rec.get('JT', '')}")
        ris_lines.append(f"AB  - {rec.get('AB', '')}")
        ris_lines.append(f"DP  - {rec.get('DP', '')}")
        ris_lines.append(f"VI  - {rec.get('VI', '')}")
        ris_lines.append(f"IP  - {rec.get('IP', '')}")
        ris_lines.append(f"PG  - {rec.get('PG', '')}")
        ris_lines.append(f"AN  - {rec.get('PMID', '')}")
        ris_lines.append(f"DO  - {rec.get('LID', '').replace(' [doi]', '')}")

        for kw in rec.get("MH", []):
            ris_lines.append(f"KW  - {kw}")

        ris_lines.append("DB  - PubMed")
        ris_lines.append("ER  - ")
        ris_lines.append("")

    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(ris_lines))

    return filepath


def records_to_csv(records, filename):
    """Export records as CSV for quick review."""
    try:
        import pandas as pd
    except ImportError:
        print("  Warning: pandas not available, skipping CSV export")
        return None

    data = []
    for rec in records:
        data.append({
            "PMID": rec.get("PMID", ""),
            "Title": rec.get("TI", ""),
            "Authors": "; ".join(rec.get("AU", [])),
            "Journal": rec.get("JT", ""),
            "Year": rec.get("DP", "")[:4] if rec.get("DP") else "",
            "Abstract": rec.get("AB", ""),
            "DOI": rec.get("LID", "").replace(" [doi]", ""),
            "Publication_Type": "; ".join(rec.get("PT", [])),
            "MeSH": "; ".join(rec.get("MH", [])),
        })

    df = pd.DataFrame(data)
    filepath = os.path.join(OUTPUT_DIR, filename)
    df.to_csv(filepath, index=False, encoding="utf-8-sig")

    return filepath, df


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("USG-PIVC Post-Insertion Outcomes — PubMed Search")
    print(f"Date range: {SEARCH_DATE_MIN} to {SEARCH_DATE_MAX}")
    print("=" * 60)

    # Email configured
    # Entrez.email = "c11g@hotmail.com"

    # Run search
    pmids, webenv, query_key = search_pubmed(FULL_QUERY)

    if not pmids:
        print("No results found. Check your search strategy.")
        sys.exit(0)

    # Fetch full records
    records = fetch_records(pmids, webenv, query_key)
    print(f"  Retrieved: {len(records)} full records")

    # Save query for reproducibility
    query_log = {
        "database": "PubMed",
        "search_date": datetime.now().isoformat(),
        "date_range": f"{SEARCH_DATE_MIN} to {SEARCH_DATE_MAX}",
        "query": FULL_QUERY,
        "results_count": len(records),
        "pmids": pmids
    }
    with open(os.path.join(OUTPUT_DIR, "pubmed_search_log.json"), "w") as f:
        json.dump(query_log, f, indent=2, ensure_ascii=False)

    # Export RIS (for Rayyan)
    ris_path = records_to_ris(records, "pubmed_results.ris")
    print(f"  RIS saved: {ris_path}")

    # Export CSV (for quick review)
    result = records_to_csv(records, "pubmed_results.csv")
    if result:
        csv_path, df = result
        print(f"  CSV saved: {csv_path}")

        # Quick summary
        print(f"\n{'='*60}")
        print("SUMMARY")
        print(f"{'='*60}")
        print(f"  Total records: {len(df)}")
        if "Year" in df.columns:
            year_counts = df["Year"].value_counts().sort_index()
            print(f"  Year range: {year_counts.index.min()} - {year_counts.index.max()}")
            print(f"\n  Records by year (top 10):")
            for yr, cnt in year_counts.tail(10).items():
                print(f"    {yr}: {cnt}")

    print(f"\n✅ PubMed search complete!")
    print(f"   Next: Run 02_search_cochrane.py for Cochrane CENTRAL")
