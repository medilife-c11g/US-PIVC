#!/usr/bin/env python3
"""AI co-reviewer: independent title/abstract screening for USG-PIVC meta-analysis.

Reads articles.csv from Rayyan export, applies inclusion/exclusion criteria,
compares with Reviewer 1 (Chen) decisions, and computes Cohen's kappa.
"""

import csv
import re
import json
from pathlib import Path
from collections import Counter

OUTPUT_DIR = Path("output")

# ============================================================================
# INCLUSION CRITERIA (all 5 must be met)
# ============================================================================
# 1. Compares USG-guided vs landmark/palpation PIVC insertion
# 2. Reports >=1 post-insertion outcome: dwell time, catheter failure, phlebitis,
#    infiltration, occlusion, dislodgement, infection
# 3. Study design: RCT or comparative cohort (not single-arm, not SR/MA)
# 4. Human participants (adult or paediatric)
# 5. English/Chinese language, year 2000-2026

# EXCLUSION patterns:
# - PICC, midline, CVC, arterial line
# - Single-arm USG study (no landmark control)
# - Comparing two USG catheter types (no landmark group)
# - Systematic review / meta-analysis (tag for reference check)
# - AI/device development, QI project, position paper, editorial
# - Insertion-only outcomes without post-insertion follow-up
# - Before-after study without concurrent comparison

def classify_article(title, abstract, keywords=""):
    """Classify a single article. Returns (decision, reason)."""
    title_lower = (title or "").lower()
    abstract_lower = (abstract or "").lower()
    kw_lower = (keywords or "").lower()
    combined = title_lower + " " + abstract_lower + " " + kw_lower

    # === QUICK EXCLUDES ===

    # Non-PIVC devices
    picc_terms = [r'\bpicc\b', r'\bperipherally inserted central', r'\bmidline catheter',
                  r'\bcentral venous catheter', r'\bcvc\b', r'\barterial line',
                  r'\barterial catheter', r'\bcentral line', r'\bhickman',
                  r'\bport-a-cath', r'\btunneled catheter']
    for term in picc_terms:
        if re.search(term, combined):
            # Check if PIVC is also mentioned as the main focus
            if not re.search(r'\bperipheral intravenous\b|\bperipheral iv\b|\bpivc\b|\bpiv\b|\bperipheral venous catheter', combined):
                return "EXCLUDE", "Non-PIVC device (PICC/CVC/midline/arterial)"

    # Systematic review / meta-analysis
    if re.search(r'\bsystematic review\b|\bmeta-analysis\b|\bmeta analysis\b|\bscoping review\b', title_lower):
        return "EXCLUDE", "Systematic review/meta-analysis"

    # Case report, editorial, letter, guideline, position paper
    if re.search(r'\bcase report\b|\beditorial\b|\bletter to\b|\bposition paper\b|\bguideline\b|\bconsensus statement\b', title_lower):
        return "EXCLUDE", "Non-eligible publication type"

    # Protocol only
    if re.search(r'\bprotocol\b', title_lower) and not re.search(r'\bresult', combined):
        return "EXCLUDE", "Protocol without results"

    # Animal / veterinary / phantom / simulation without clinical
    if re.search(r'\bphantom\b|\bsimulat\b|\bcadaver\b|\bmannequin\b|\bin vitro\b', title_lower):
        if not re.search(r'\bclinical\b|\bpatient\b', combined):
            return "EXCLUDE", "Simulation/phantom study"

    # AI / machine learning development only
    if re.search(r'\bdeep learning\b|\bmachine learning\b|\bartificial intelligence\b|\bneural network\b', title_lower):
        if not re.search(r'\bclinical outcome\b|\bdwell\b|\bfailure\b|\bcomplication\b', combined):
            return "EXCLUDE", "AI/ML development study"

    # === CHECK FOR USG + PIVC ===
    has_usg = bool(re.search(
        r'\bultrasound.guid\b|\bultrasound-guid\b|\bUS-guid\b|\bUSG\b'
        r'|\bsonograph\b|\bechograph\b|\bPOCUS\b'
        r'|\bultrasound.assist\b|\bultrasound-assist\b'
        r'|\bvascular ultrasound\b|\bvascular US\b'
        r'|\breal.time ultrasound\b',
        combined, re.IGNORECASE
    ))

    has_pivc = bool(re.search(
        r'\bperipheral intravenous\b|\bperipheral venous catheter\b'
        r'|\bperipheral iv\b|\bpivc\b|\bpiv\b'
        r'|\bperipheral cannul\b|\bintravenous cannul\b'
        r'|\bvenipuncture\b|\bvenepuncture\b'
        r'|\bperipheral vascular access\b|\bperipheral venous access\b'
        r'|\bshort peripheral\b|\bUSGIV\b|\bUSGPIV\b',
        combined, re.IGNORECASE
    ))

    if not has_usg:
        return "EXCLUDE", "No ultrasound guidance mentioned"
    if not has_pivc:
        return "EXCLUDE", "Not about PIVC"

    # === CHECK FOR COMPARISON GROUP ===
    has_comparison = bool(re.search(
        r'\bversus\b|\bvs\.?\b|\bcompare[d]?\b|\bcomparison\b'
        r'|\brandom\b|\brandomiz\b|\bRCT\b'
        r'|\bcontrol group\b|\bconventional\b|\btraditional\b'
        r'|\blandmark\b|\bpalpation\b|\bblind\b.*\binsertion\b'
        r'|\bstandard\b.*\btechnique\b|\bstandard\b.*\bmethod\b'
        r'|\bwithout ultrasound\b|\bnon.ultrasound\b',
        combined, re.IGNORECASE
    ))

    if not has_comparison:
        return "EXCLUDE", "Single-arm study (no landmark comparator)"

    # === CHECK FOR POST-INSERTION OUTCOMES ===
    has_post_insertion = bool(re.search(
        r'\bdwell time\b|\bcatheter survival\b|\bcatheter longevity\b'
        r'|\bcatheter failure\b|\bcatheter malfunction\b'
        r'|\bpost.insertion\b|\bpost insertion\b'
        r'|\bphlebitis\b|\binfiltration\b|\bextravasation\b'
        r'|\bocclusion\b|\bblockage\b|\bdislodgement\b|\bdislodgment\b'
        r'|\bthrombophlebitis\b|\bcatheter.related infection\b'
        r'|\bpremature removal\b|\bunplanned removal\b'
        r'|\bcatheter patency\b|\bdevice failure\b'
        r'|\bcatheter complication\b|\bIV complication\b'
        r'|\bsurvival\b.*\bcatheter\b|\bcatheter\b.*\bsurvival\b'
        r'|\bfunctional\b.*\bduration\b|\bduration\b.*\bcatheter\b'
        r'|\btime to\b.*\bremoval\b|\btime to\b.*\bfailure\b'
        r'|\bKaplan.Meier\b|\bhazard ratio\b',
        combined, re.IGNORECASE
    ))

    has_insertion_only = bool(re.search(
        r'\bfirst.attempt success\b|\bfirst attempt success\b'
        r'|\binsertion time\b|\baccess time\b|\bcannulation time\b'
        r'|\bsuccess rate\b.*\binsertion\b',
        combined, re.IGNORECASE
    ))

    if has_post_insertion:
        # Check study design
        is_sr_ma = bool(re.search(r'\bsystematic review\b|\bmeta.analysis\b', combined))
        if is_sr_ma:
            return "EXCLUDE", "Systematic review/meta-analysis (check references)"

        is_comparative = bool(re.search(
            r'\brandomiz\b|\bRCT\b|\bcohort\b|\bretrospective\b|\bprospective\b'
            r'|\bcompar\b|\bobservational\b|\bcross.sectional\b',
            combined, re.IGNORECASE
        ))

        if is_comparative:
            return "INCLUDE", "USG vs landmark PIVC with post-insertion outcomes"
        else:
            return "MAYBE", "USG vs landmark PIVC with post-insertion data but unclear study design"

    elif has_insertion_only and not has_post_insertion:
        return "EXCLUDE", "Insertion-only outcomes (no post-insertion follow-up)"

    # Has USG + PIVC + comparison but unclear outcomes
    return "MAYBE", "USG vs landmark PIVC comparison but unclear if post-insertion outcomes reported"


def parse_reviewer1_decision(notes):
    """Extract Reviewer 1 decision from Rayyan notes field."""
    if not notes:
        return "UNKNOWN"
    match = re.search(r'"家慶"=>"(\w+)"', notes)
    if match:
        decision = match.group(1)
        if decision == "Included":
            return "INCLUDE"
        elif decision == "Excluded":
            return "EXCLUDE"
        elif decision == "Maybe":
            return "MAYBE"
    return "UNKNOWN"


def compute_kappa(decisions1, decisions2):
    """Compute Cohen's kappa for two lists of binary decisions (INCLUDE vs EXCLUDE)."""
    # Convert to binary: INCLUDE/MAYBE = positive, EXCLUDE = negative
    def to_binary(d):
        return 1 if d in ("INCLUDE", "MAYBE") else 0

    n = len(decisions1)
    if n == 0:
        return 0.0

    b1 = [to_binary(d) for d in decisions1]
    b2 = [to_binary(d) for d in decisions2]

    # Contingency table
    a = sum(1 for i in range(n) if b1[i] == 1 and b2[i] == 1)  # both positive
    b = sum(1 for i in range(n) if b1[i] == 1 and b2[i] == 0)  # R1 pos, R2 neg
    c = sum(1 for i in range(n) if b1[i] == 0 and b2[i] == 1)  # R1 neg, R2 pos
    d = sum(1 for i in range(n) if b1[i] == 0 and b2[i] == 0)  # both negative

    po = (a + d) / n  # observed agreement
    p1_pos = (a + b) / n
    p2_pos = (a + c) / n
    p1_neg = (c + d) / n
    p2_neg = (b + d) / n
    pe = p1_pos * p2_pos + p1_neg * p2_neg  # expected agreement

    if pe == 1.0:
        return 1.0
    kappa = (po - pe) / (1 - pe)
    return kappa, po, pe, {"a": a, "b": b, "c": c, "d": d}


def main():
    articles_path = OUTPUT_DIR / "articles.csv"

    # Read articles
    articles = []
    with open(articles_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            articles.append(row)

    print(f"Total articles to screen: {len(articles)}")

    # Screen each article
    results = []
    for art in articles:
        title = art.get("title", "")
        abstract = art.get("abstract", "")
        keywords = art.get("keywords", "")
        notes = art.get("notes", "")

        ai_decision, ai_reason = classify_article(title, abstract, keywords)
        r1_decision = parse_reviewer1_decision(notes)

        results.append({
            "key": art.get("key", ""),
            "title": title[:150],
            "year": art.get("year", ""),
            "authors": art.get("authors", "")[:80],
            "reviewer1_decision": r1_decision,
            "ai_decision": ai_decision,
            "ai_reason": ai_reason,
            "agreement": "AGREE" if (
                (r1_decision in ("INCLUDE", "MAYBE") and ai_decision in ("INCLUDE", "MAYBE")) or
                (r1_decision == "EXCLUDE" and ai_decision == "EXCLUDE")
            ) else "DISAGREE" if r1_decision != "UNKNOWN" else "R1_UNKNOWN",
        })

    # Summary
    r1_decisions = [r["reviewer1_decision"] for r in results]
    ai_decisions = [r["ai_decision"] for r in results]

    print(f"\n{'='*60}")
    print("SCREENING SUMMARY")
    print(f"{'='*60}")

    print(f"\nReviewer 1 (Chen):")
    for k, v in Counter(r1_decisions).most_common():
        print(f"  {k}: {v}")

    print(f"\nAI Reviewer:")
    for k, v in Counter(ai_decisions).most_common():
        print(f"  {k}: {v}")

    # Filter to only articles where R1 has a decision
    paired = [r for r in results if r["reviewer1_decision"] != "UNKNOWN"]
    print(f"\nPaired decisions: {len(paired)}")

    agreements = [r for r in paired if r["agreement"] == "AGREE"]
    disagreements = [r for r in paired if r["agreement"] == "DISAGREE"]
    print(f"Agreements: {len(agreements)}")
    print(f"Disagreements: {len(disagreements)}")

    # Cohen's kappa
    if paired:
        r1_list = [r["reviewer1_decision"] for r in paired]
        ai_list = [r["ai_decision"] for r in paired]
        kappa_result = compute_kappa(r1_list, ai_list)
        if isinstance(kappa_result, tuple):
            kappa, po, pe, table = kappa_result
            print(f"\nCohen's Kappa: {kappa:.3f}")
            print(f"Observed agreement: {po:.3f} ({po*100:.1f}%)")
            print(f"Expected agreement: {pe:.3f}")
            print(f"Contingency table: {table}")
            print(f"Kappa interpretation: ", end="")
            if kappa >= 0.81:
                print("Almost perfect")
            elif kappa >= 0.61:
                print("Substantial")
            elif kappa >= 0.41:
                print("Moderate")
            elif kappa >= 0.21:
                print("Fair")
            else:
                print("Slight/Poor")

    # Print disagreements
    if disagreements:
        print(f"\n{'='*60}")
        print(f"DISAGREEMENTS ({len(disagreements)} articles)")
        print(f"{'='*60}")
        for r in disagreements:
            print(f"\n  Key: {r['key']}")
            print(f"  Title: {r['title']}")
            print(f"  Year: {r['year']}")
            print(f"  R1 (Chen): {r['reviewer1_decision']}")
            print(f"  AI: {r['ai_decision']} — {r['ai_reason']}")

    # Print AI includes
    ai_includes = [r for r in results if r["ai_decision"] in ("INCLUDE", "MAYBE")]
    print(f"\n{'='*60}")
    print(f"AI INCLUDE/MAYBE ({len(ai_includes)} articles)")
    print(f"{'='*60}")
    for r in ai_includes:
        print(f"  [{r['ai_decision']}] {r['key']} | {r['year']} | {r['title'][:100]}")
        print(f"    R1: {r['reviewer1_decision']} | Reason: {r['ai_reason']}")

    # Save results
    output_path = OUTPUT_DIR / "ai_screening_results.csv"
    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print(f"\nResults saved to {output_path}")

    # Save disagreements
    disagree_path = OUTPUT_DIR / "screening_disagreements.csv"
    with open(disagree_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=disagreements[0].keys() if disagreements else [])
        if disagreements:
            writer.writeheader()
            writer.writerows(disagreements)
    print(f"Disagreements saved to {disagree_path}")


if __name__ == "__main__":
    main()
