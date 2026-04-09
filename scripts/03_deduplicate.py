#!/usr/bin/env python3
"""
03_deduplicate.py
Merge and deduplicate search results from multiple databases.
Uses DOI, PMID, and title fuzzy matching to identify duplicates.
"""

import os
import re
import csv
import json
from datetime import datetime
from collections import defaultdict

try:
    import pandas as pd
except ImportError:
    print("ERROR: pandas not installed. Run: pip install pandas --break-system-packages")
    exit(1)

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================
# RIS PARSER
# ============================================================
def parse_ris(filepath):
    """Parse a RIS file into a list of record dicts."""
    records = []
    current = {}
    current_tag = None

    if not os.path.exists(filepath):
        print(f"  ⚠️  File not found: {filepath}")
        return []

    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.rstrip("\n")

            # New tag
            match = re.match(r"^([A-Z][A-Z0-9])  - (.*)$", line)
            if match:
                tag, value = match.groups()
                current_tag = tag

                if tag == "TY":
                    current = {"TY": value, "_authors": [], "_keywords": []}
                elif tag == "ER":
                    if current:
                        records.append(current)
                    current = {}
                    current_tag = None
                elif tag == "AU":
                    current["_authors"].append(value)
                elif tag == "KW":
                    current["_keywords"].append(value)
                else:
                    current[tag] = value
            elif current_tag and line.startswith("      "):
                # Continuation line
                if current_tag in current:
                    current[current_tag] += " " + line.strip()

    return records


def normalize_title(title):
    """Normalize title for fuzzy matching."""
    if not title:
        return ""
    t = title.lower().strip()
    t = re.sub(r"[^a-z0-9\s]", "", t)  # Remove punctuation
    t = re.sub(r"\s+", " ", t)          # Normalize whitespace
    return t


def normalize_doi(doi):
    """Extract and normalize DOI."""
    if not doi:
        return ""
    doi = doi.strip().lower()
    # Extract DOI pattern
    match = re.search(r"10\.\d{4,}/\S+", doi)
    if match:
        return match.group(0).rstrip(".")
    return ""


def jaccard_similarity(s1, s2):
    """Compute Jaccard similarity between two strings (word-level)."""
    if not s1 or not s2:
        return 0.0
    words1 = set(s1.split())
    words2 = set(s2.split())
    if not words1 or not words2:
        return 0.0
    intersection = words1 & words2
    union = words1 | words2
    return len(intersection) / len(union)


# ============================================================
# DEDUPLICATION ENGINE
# ============================================================
def deduplicate(all_records):
    """
    Deduplicate records using three strategies:
    1. Exact DOI match
    2. Exact PMID match
    3. Title similarity (Jaccard >= 0.85)
    """
    unique = []
    seen_dois = {}       # doi -> index in unique
    seen_pmids = {}      # pmid -> index in unique
    seen_titles = {}     # normalized_title -> index in unique
    duplicate_log = []

    for rec in all_records:
        doi = normalize_doi(rec.get("DO", ""))
        pmid = rec.get("AN", "").strip()
        title_norm = normalize_title(rec.get("TI", ""))
        source_db = rec.get("DB", "Unknown")
        is_dup = False
        dup_reason = ""
        dup_match_idx = -1

        # Strategy 1: DOI match
        if doi and doi in seen_dois:
            is_dup = True
            dup_reason = f"DOI match: {doi}"
            dup_match_idx = seen_dois[doi]

        # Strategy 2: PMID match
        if not is_dup and pmid and pmid in seen_pmids:
            is_dup = True
            dup_reason = f"PMID match: {pmid}"
            dup_match_idx = seen_pmids[pmid]

        # Strategy 3: Title fuzzy match
        if not is_dup and title_norm:
            for existing_title, idx in seen_titles.items():
                sim = jaccard_similarity(title_norm, existing_title)
                if sim >= 0.85:
                    is_dup = True
                    dup_reason = f"Title similarity ({sim:.2f}): '{rec.get('TI', '')[:60]}...'"
                    dup_match_idx = idx
                    break

        if is_dup:
            # Log duplicate but add source DB to original record
            orig = unique[dup_match_idx]
            if "DB_all" not in orig:
                orig["DB_all"] = orig.get("DB", "")
            orig["DB_all"] += f"; {source_db}"

            duplicate_log.append({
                "duplicate_title": rec.get("TI", ""),
                "duplicate_db": source_db,
                "original_title": orig.get("TI", ""),
                "original_db": orig.get("DB", ""),
                "reason": dup_reason,
            })
        else:
            # New unique record
            idx = len(unique)
            unique.append(rec)

            if doi:
                seen_dois[doi] = idx
            if pmid:
                seen_pmids[pmid] = idx
            if title_norm:
                seen_titles[title_norm] = idx

    return unique, duplicate_log


# ============================================================
# EXPORT
# ============================================================
def export_merged_ris(records, filepath):
    """Export deduplicated records as RIS for Rayyan import."""
    lines = []
    for rec in records:
        lines.append("TY  - JOUR")
        lines.append(f"TI  - {rec.get('TI', '')}")
        for au in rec.get("_authors", []):
            lines.append(f"AU  - {au}")
        lines.append(f"JO  - {rec.get('JO', rec.get('T2', ''))}")
        lines.append(f"AB  - {rec.get('AB', '')}")
        lines.append(f"DP  - {rec.get('DP', rec.get('PY', ''))}")
        lines.append(f"DO  - {rec.get('DO', '')}")
        lines.append(f"AN  - {rec.get('AN', '')}")
        lines.append(f"DB  - {rec.get('DB_all', rec.get('DB', ''))}")
        for kw in rec.get("_keywords", []):
            lines.append(f"KW  - {kw}")
        lines.append("ER  - ")
        lines.append("")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def export_screening_csv(records, filepath):
    """Export CSV for manual screening."""
    rows = []
    for i, rec in enumerate(records, 1):
        rows.append({
            "ID": i,
            "PMID": rec.get("AN", ""),
            "DOI": rec.get("DO", ""),
            "Title": rec.get("TI", ""),
            "Authors": "; ".join(rec.get("_authors", [])),
            "Year": rec.get("DP", rec.get("PY", ""))[:4],
            "Journal": rec.get("JO", rec.get("T2", "")),
            "Abstract": rec.get("AB", ""),
            "Source_DB": rec.get("DB_all", rec.get("DB", "")),
            "Screen_Decision": "",       # Include / Exclude / Maybe
            "Exclusion_Reason": "",      # No post-insertion outcome / No comparison / etc.
            "Full_Text_Decision": "",
            "Notes": "",
        })

    df = pd.DataFrame(rows)
    df.to_csv(filepath, index=False, encoding="utf-8-sig")
    return df


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Cross-Database Deduplication")
    print("=" * 60)

    # Collect all RIS files
    ris_files = {
        "PubMed": os.path.join(DATA_DIR, "pubmed_results.ris"),
        "Cochrane": os.path.join(DATA_DIR, "cochrane_results.ris"),
        "Embase": os.path.join(DATA_DIR, "embase_results.ris"),
        "CINAHL": os.path.join(DATA_DIR, "cinahl_results.ris"),
    }

    all_records = []
    db_counts = {}

    for db_name, filepath in ris_files.items():
        records = parse_ris(filepath)
        for rec in records:
            rec["DB"] = db_name
        db_counts[db_name] = len(records)
        all_records.extend(records)
        if records:
            print(f"  {db_name}: {len(records)} records loaded")
        else:
            print(f"  {db_name}: no file found or empty (skipped)")

    if not all_records:
        print("\n❌ No records found! Place RIS files in data/ folder first.")
        print("   Expected files: pubmed_results.ris, cochrane_results.ris, etc.")
        exit(0)

    total_raw = len(all_records)
    print(f"\n  Total raw records: {total_raw}")

    # Deduplicate
    print(f"\n[{datetime.now():%H:%M:%S}] Running deduplication...")
    unique_records, dup_log = deduplicate(all_records)

    n_dups = total_raw - len(unique_records)
    print(f"  Duplicates removed: {n_dups}")
    print(f"  Unique records: {len(unique_records)}")

    # Save duplicate log
    if dup_log:
        dup_df = pd.DataFrame(dup_log)
        dup_path = os.path.join(OUTPUT_DIR, "duplicate_log.csv")
        dup_df.to_csv(dup_path, index=False, encoding="utf-8-sig")
        print(f"  Duplicate log: {dup_path}")

    # Export merged RIS for Rayyan
    merged_ris_path = os.path.join(OUTPUT_DIR, "merged_deduplicated.ris")
    export_merged_ris(unique_records, merged_ris_path)
    print(f"  Merged RIS (for Rayyan): {merged_ris_path}")

    # Export screening CSV
    screening_csv_path = os.path.join(OUTPUT_DIR, "screening_sheet.csv")
    df = export_screening_csv(unique_records, screening_csv_path)
    print(f"  Screening sheet: {screening_csv_path}")

    # PRISMA numbers
    prisma = {
        "identification": {
            "databases": db_counts,
            "total_identified": total_raw,
        },
        "deduplication": {
            "duplicates_removed": n_dups,
            "records_after_dedup": len(unique_records),
        },
        "generated_at": datetime.now().isoformat(),
    }

    prisma_path = os.path.join(OUTPUT_DIR, "prisma_numbers.json")
    with open(prisma_path, "w") as f:
        json.dump(prisma, f, indent=2)
    print(f"  PRISMA numbers: {prisma_path}")

    # Summary
    print(f"\n{'='*60}")
    print("PRISMA FLOW — Identification Stage")
    print(f"{'='*60}")
    for db, cnt in db_counts.items():
        if cnt > 0:
            print(f"  {db:15s}: {cnt:5d} records")
    print(f"  {'─'*30}")
    print(f"  {'Total':15s}: {total_raw:5d}")
    print(f"  {'Duplicates':15s}: {n_dups:5d}")
    print(f"  {'After dedup':15s}: {len(unique_records):5d}")
    print(f"\n✅ Deduplication complete!")
    print(f"   Next: Upload merged_deduplicated.ris to Rayyan for screening")
    print(f"   Or use screening_sheet.csv for manual screening")
