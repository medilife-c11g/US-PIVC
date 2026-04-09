#!/usr/bin/env python3
"""
02_search_cochrane.py
Generate search strings for Cochrane CENTRAL and Embase.
These databases require manual search via web interface.
This script generates the exact search strings and saves instructions.
"""

import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================
# COCHRANE CENTRAL SEARCH STRING
# ============================================================
COCHRANE_SEARCH = """
=== COCHRANE CENTRAL SEARCH STRATEGY ===
Database: Cochrane Central Register of Controlled Trials (CENTRAL)
URL: https://www.cochranelibrary.com/advanced-search
Date: 2000-01 to 2026-03

INSTRUCTIONS:
1. Go to https://www.cochranelibrary.com/advanced-search
2. Select "Trials" tab
3. Enter each search line in "Search Manager"
4. Combine with AND
5. Limit publication date: Jan 2000 to Mar 2026
6. Export results as RIS → save to data/cochrane_results.ris

--- SEARCH LINES ---

#1 MeSH descriptor: [Ultrasonography] explode all trees
    OR (ultrasound OR ultrasonograph* OR sonograph* OR POCUS
    OR "point-of-care ultrasound" OR "US-guided" OR "USG"
    OR "ultrasound-guided"):ti,ab,kw

#2 MeSH descriptor: [Catheterization, Peripheral] explode all trees
    OR ("peripheral intravenous" OR "peripheral venous catheter*"
    OR "peripheral IV" OR PIVC OR PIV
    OR "peripheral vascular access" OR "peripheral venous access"
    OR "peripheral cannulat*" OR "intravenous cannulat*"
    OR venipuncture OR venepuncture
    OR "short peripheral catheter"
    OR USGIV OR USGPIV):ti,ab,kw

#3 MeSH descriptor: [Equipment Failure] explode all trees
    OR MeSH descriptor: [Phlebitis] explode all trees
    OR MeSH descriptor: [Catheter-Related Infections] explode all trees
    OR ("dwell time" OR "catheter survival" OR "catheter failure"
    OR "catheter longevity" OR "catheter durability"
    OR "catheter complication*" OR "post-insertion"
    OR phlebitis OR infiltration OR extravasation
    OR occlusion OR dislodgement OR dislodgment
    OR "catheter patency" OR thrombophlebitis
    OR "premature removal" OR "unplanned removal"
    OR "device failure" OR "catheter malfunction"):ti,ab,kw

#4 #1 AND #2 AND #3

#5 #4 with Publication Year from 2000 to 2026
"""

# ============================================================
# EMBASE (OVID) SEARCH STRING
# ============================================================
EMBASE_SEARCH = """
=== EMBASE (OVID) SEARCH STRATEGY ===
Database: Embase via Ovid
URL: Access via your hospital library (e.g., 秀傳圖書館 or 國家衛生研究院)
Date limit: 2000-2026

INSTRUCTIONS:
1. Log in to Ovid Embase via institutional access
2. Select "Advanced Search"
3. Enter each line, run search
4. Combine sets with AND
5. Apply date limit: 2000 to 2026
6. Remove animal-only studies
7. Export as RIS → save to data/embase_results.ris

--- SEARCH LINES ---

1   exp echography/ OR ultrasound.tw. OR ultrasonograph*.tw.
    OR sonograph*.tw. OR POCUS.tw. OR "point-of-care ultrasound".tw.
    OR "US-guided".tw. OR USG.tw. OR "ultrasound-guided".tw.

2   exp peripheral catheterization/ OR "peripheral intravenous".tw.
    OR "peripheral venous catheter*".tw. OR PIVC.tw. OR PIV.tw.
    OR "peripheral vascular access".tw. OR "peripheral venous access".tw.
    OR "peripheral cannulat*".tw. OR "intravenous cannulat*".tw.
    OR venipuncture.tw. OR venepuncture.tw.
    OR "short peripheral catheter".tw.
    OR USGIV.tw. OR USGPIV.tw.

3   exp device failure/ OR exp phlebitis/ OR exp catheter infection/
    OR "dwell time".tw. OR "catheter survival".tw.
    OR "catheter failure".tw. OR "catheter complication*".tw.
    OR phlebitis.tw. OR infiltration.tw. OR extravasation.tw.
    OR occlusion.tw. OR dislodg*.tw. OR "catheter patency".tw.
    OR thrombophlebitis.tw.
    OR (premature adj2 removal).tw.
    OR (unplanned adj2 removal).tw.
    OR "device failure".tw. OR "catheter malfunction".tw.

4   1 AND 2 AND 3

5   limit 4 to yr="2000-2026"

6   5 NOT (exp animal/ NOT exp human/)
"""

# ============================================================
# CINAHL (BONUS - 4th database)
# ============================================================
CINAHL_SEARCH = """
=== CINAHL (EBSCOhost) SEARCH STRATEGY ===
Database: CINAHL Complete via EBSCOhost
URL: Access via hospital library
Date limit: 2000-2026
Note: CINAHL is particularly important for nursing-focused studies.

INSTRUCTIONS:
1. Log in to EBSCOhost CINAHL
2. Select "Advanced Search"
3. Enter each search block
4. Combine with AND
5. Apply limiters: Publication Date 2000-2026; English or Chinese
6. Export as RIS → save to data/cinahl_results.ris

--- SEARCH LINES ---

S1  (MH "Ultrasonography+") OR TI ultrasound OR AB ultrasound
    OR TI ultrasonograph* OR AB POCUS
    OR TI "point-of-care ultrasound" OR TI "ultrasound-guided"
    OR AB "US-guided"

S2  (MH "Catheter Insertion, Peripheral") OR (MH "Peripheral Vascular Devices")
    OR TI "peripheral intravenous" OR AB "peripheral venous catheter*"
    OR TI PIVC OR AB "peripheral cannulat*"
    OR TI "intravenous cannulat*" OR AB venipuncture

S3  (MH "Phlebitis") OR (MH "Equipment Failure")
    OR (MH "Catheter-Related Infections")
    OR TI "dwell time" OR AB "catheter failure"
    OR TI phlebitis OR AB infiltration
    OR TI extravasation OR AB occlusion
    OR TI dislodg* OR AB "catheter complication*"
    OR TI "catheter survival" OR AB "premature removal"
    OR TI "unplanned removal" OR AB thrombophlebitis

S4  S1 AND S2 AND S3

S5  S4 (Limiters: Published Date 2000-2026)
"""

# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Generating search strings for manual database searches")
    print("=" * 60)

    # Save Cochrane search
    cochrane_path = os.path.join(OUTPUT_DIR, "cochrane_search_string.txt")
    with open(cochrane_path, "w", encoding="utf-8") as f:
        f.write(COCHRANE_SEARCH)
    print(f"✅ Cochrane CENTRAL search → {cochrane_path}")

    # Save Embase search
    embase_path = os.path.join(OUTPUT_DIR, "embase_search_string.txt")
    with open(embase_path, "w", encoding="utf-8") as f:
        f.write(EMBASE_SEARCH)
    print(f"✅ Embase (Ovid) search    → {embase_path}")

    # Save CINAHL search
    cinahl_path = os.path.join(OUTPUT_DIR, "cinahl_search_string.txt")
    with open(cinahl_path, "w", encoding="utf-8") as f:
        f.write(CINAHL_SEARCH)
    print(f"✅ CINAHL search           → {cinahl_path}")

    print(f"\n📋 Next steps:")
    print(f"   1. Use search strings to query each database manually")
    print(f"   2. Export results as RIS files to data/ folder")
    print(f"   3. Run 03_deduplicate.py to merge and deduplicate")
