# USG-PIVC Screening Progress — Title/Abstract Phase
## Last updated: 2026-03-29

## Project Info
- **PROSPERO**: CRD420261354170 (registered 2026-03-28)
- **Rayyan Review ID**: 1961147
- **Total records**: 1,359 (after deduplication)
- **Databases**: PubMed (530) + Embase (984) + Cochrane (68) + CINAHL (50) = 1,632 → 1,359 unique

---

## Screening Decisions Log

### INCLUDED (confirmed符合全部5項 Inclusion Criteria)

| # | Rayyan ID | First Author | Title (short) | Year | Design | Population | Key Post-Insertion Outcomes | Notes |
|---|-----------|-------------|---------------|------|--------|------------|---------------------------|-------|
| 1 | 486160691 | Kleidon TM | EPIC RCT - J Vascular Access version | 2022 | RCT | Paediatric | PIVC failure, dwell time, post-insertion complications | Same trial as #2 and #3 |
| 2 | 486160195 | Kleidon TM | EPIC RCT - JAMA Pediatrics full report | 2023 | RCT | Paediatric | PIVC failure, dwell time, post-insertion complications | Primary report; use this for data extraction |
| 3 | 486160240 | Kleidon TM | EPIC RCT - Protocol paper (BJN) | 2023 | Protocol | Paediatric | Protocol only, no results | Same trial as #1 and #2 |
| 4 | 486160424 | Bridey C | USG vs landmark PIVC by ICU nurses (BMJ Open) | 2018 | RCT | Adult ICU | Catheter lifespan (3 vs 3 days), extravasation | Null result |
| 5 | 486160202 | Refosco M | USG deep veins vs blind superficial veins in children 0-18y | 2024 | Retrospective cohort | Paediatric | Dwell time (5.3 vs 2.5 days), complications (25% vs 70%), dislodgement | Confounding: USG=long catheter, blind=short |
| 6 | 486160255 | Dachepally R | USG long PIV vs traditional standard PIV in paediatric ICU | 2022 | Retrospective cohort | Paediatric ICU | IV survival (219 vs 108 hrs), failure HR 2.20, vascular access escalation OR 0.39 | Confounding: USG=long catheter |
| 7 | - | Feinsmith SE | USG vs landmark PIV after simulation training | 2022 | Retrospective cohort | Adult | Time to failure, Kaplan-Meier survival (USG better, p<0.001) | Large sample: 43,470 PIVCs |
| 8 | - | (unknown) | Contrast extravasation: USGPIV vs landmark | 2017 | Retrospective cohort | Adult ED | Contrast extravasation (4.1% vs 0.21%, RR 19.4) | Result unfavorable to USG |
| 9 | - | (unknown) | Utility and survivorship of PIVCs in ED | ~2015 | Prospective cohort | Adult ED | 72-hr survivorship (73% vs 79%), premature removal RR 1.26 | n=1,174; null result |
| ~~10~~ | - | ~~(unknown)~~ | ~~Oncology nurses USG vs traditional IV~~ | ~~2025~~ | ~~RCT~~ | ~~Adult oncology~~ | ~~Dwell time, catheter failure, phlebitis, etc.~~ | **REMOVED: Not published** |

### MAYBE (需要 full-text 確認)

| # | Rayyan ID | First Author | Title (short) | Reason for Maybe |
|---|-----------|-------------|---------------|-----------------|
| 1 | - | (Spanish RCT) | Comparison of traditional and USG techniques in ED DIVA patients | Protocol; unclear if post-insertion outcomes reported; Jan 2025 start |
| 2 | - | (São Paulo RCT) | Assertiveness and PIVC dwell times with USG in children | Language concern: may be Portuguese only. RCT with dwell time data |
| 3 | - | (São Paulo RCT) | Peripheral IV puncture guided by vascular ultrasound | Same trial as Maybe #2 |
| 4 | - | (Turkish study) | Effectiveness of using USG in PIVC application | Small sample (n=30), zero complications, quasi-experimental crossover |
| 5 | - | (VAS-ED) | Introducing VAS model in ED | Service model comparison, need to confirm if USG vs landmark extractable |

### EXCLUDED — Common Patterns

| Exclusion Reason | Count (approx) | Examples |
|-----------------|----------------|---------|
| Single-arm USG study (no landmark control) | Many | Dargin 2009, Gregg 2010, Godfrey 2024, Gilardi 2022 |
| Different catheter types compared (not insertion technique) | Several | LPC vs SPC, EDC vs standard USIV, midline vs PIVC |
| Systematic review / meta-analysis | Several | Shcherbatiuk (Neonatology), others |
| Position paper / guideline / editorial | Several | NEVAT position paper |
| AI/technology development study | Several | Takahashi (AI prediction), Bahl (AI failure prediction) |
| Insertion-only outcomes (no post-insertion follow-up) | Several | 3-arm French RCT (USG vs IR vs traditional) |
| PICC / CVC / arterial catheter study | Several | Park (PICC duration) |
| QI project / implementation study | Several | Campos (VAS initiative), DART3 |
| Before-after study (not concurrent comparison) | Several | Kanno 2020 (algorithm pretest-posttest) |
| Risk factor / prediction study | Several | Abe (DIVA risk factors), EA-DIVA validation |
| Transillumination comparator (not landmark) | 1 | Retrospective pediatric USG vs transillumination |

---

## Screening Rules Summary

### Include ALL 5 criteria must be met:
1. Compares USG-guided vs landmark/palpation PIVC insertion
2. Reports ≥1 post-insertion outcome: dwell time, catheter failure, phlebitis, infiltration, occlusion, dislodgement, infection
3. Study design: RCT or comparative cohort
4. Human participants (adult or paediatric)
5. English language, year 2000-2026

### Quick Exclude patterns:
- Title says "systematic review" or "meta-analysis" → Exclude (but tag reference-check)
- Single-arm USG study → Exclude
- PICC, midline, CVC, arterial line as main subject → Exclude
- Comparing two USG catheter types (no landmark group) → Exclude
- AI/device development, QI project, position paper → Exclude
- Insertion-only outcomes without post-insertion follow-up → Exclude

### When uncertain → Maybe (resolve at full-text stage)

---

## Next Steps
- Continue title/abstract screening (both reviewers independently)
- Pilot calibration: compare first 50 decisions between Chen and Lee
- After screening complete: resolve conflicts → full-text screening → data extraction
