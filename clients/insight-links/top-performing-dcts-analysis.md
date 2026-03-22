# Insight Links — Top-Performing DCT Analysis (COMPLETE DATA)

**Date:** March 22, 2026
**Data Source:** Mailchimp subscriber exports — ALL segments, TFM + Growletter, all three newsletters
**Total Records Analyzed:** 25,187 subscribers

> **Previous version was incomplete.** The prior analysis showed 0 Growletter qualified leads because the GL IW and GL DHW data files were missing. This version includes all data: 6 TFM segments + 41 Growletter segments across CW, IW, and DHW. The honest finding: even with the complete GL data, the picture barely changes. GL produced 12 qualified leads total across 19,925 subscribers.

---

## 1. Total Subscribers by Source x Newsletter

| Newsletter | TFM | Growletter | Total | GL:TFM Ratio |
|---|---:|---:|---:|---:|
| Cardiac Wire | 2,504 | 11,362 | 13,866 | 4.5x |
| Imaging Wire | 1,253 | 2,847 | 4,100 | 2.3x |
| Digital Health Wire | 1,505 | 5,716 | 7,221 | 3.8x |
| **TOTAL** | **5,262** | **19,925** | **25,187** | **3.8x** |

**Growletter delivers 3.8x more total volume than TFM across all newsletters.** The biggest gap is on Cardiac Wire (4.5x). Even on Imaging Wire, where GL has historically struggled, they deliver 2.3x TFM's volume.

---

## 2. Form Completion Rate by Source x Newsletter

"Form complete" = all 4 first-party fields filled: FNAME, LNAME, TITLE, COMPANY.

| Newsletter | TFM Complete | TFM Rate | GL Complete | GL Rate |
|---|---:|---:|---:|---:|
| Cardiac Wire | 629 / 2,504 | **25.1%** | 1,798 / 11,362 | **15.8%** |
| Imaging Wire | 477 / 1,253 | **38.1%** | 832 / 2,847 | **29.2%** |
| Digital Health Wire | 584 / 1,505 | **38.8%** | 1,336 / 5,716 | **23.4%** |

**TFM wins on form completion rate across all 3 newsletters.** TFM leads are 1.5-1.7x more likely to fill out all four fields. However, in absolute numbers, GL still delivers more completed forms on CW (1,798 vs 629) and DHW (1,336 vs 584) due to their volume advantage. On IW, TFM actually approaches parity in completed-form count despite having less than half the volume.

---

## 3. TFM Qualification Results (TFM data only)

> **Methodology note:** The QUALIFIED field is populated by TFM's post-subscribe ICP form, which asks for job title, company, and role. Growletter's signup funnel does not include this form. GL leads never see the qualification questions. Their empty QUALIFIED fields mean "never assessed," not "failed quality." Therefore, **qualification rate is a TFM-internal optimization metric, not a cross-agency comparison.**

| Newsletter | TFM Subs | TFM Qualified | TFM Qual Rate |
|---|---:|---:|---:|
| Cardiac Wire | 2,504 | 259 | **10.3%** |
| Imaging Wire | 1,253 | 255 | **20.4%** |
| Digital Health Wire | 1,505 | 314 | **20.9%** |
| **TOTAL** | **5,262** | **828** | **15.7%** |

IW and DHW qualify at 2x the rate of CW — CW has a systemic quality problem that needs creative-level diagnosis (see Section 5).

### QUALIFIED field distribution (for context)

| Segment | QUALIFIED=true | QUALIFIED=false | QUALIFIED=empty |
|---|---:|---:|---:|
| CW TFM | 259 | 373 | 1,872 |
| IW TFM | 255 | 209 | 789 |
| DHW TFM | 314 | 268 | 923 |

68% of TFM leads have an empty QUALIFIED field (form not completed). Of those who complete the form, roughly 55-60% qualify. The form completion bottleneck is a separate optimization opportunity.

### Why GL data is excluded from this section

GL's funnel does not include TFM's post-subscribe ICP questions. Of 19,925 GL subscribers, 93-95% have no QUALIFIED value. The small number with values (e.g., 768 QUALIFIED=false on CW) may have been manually assessed or entered through an alternate pathway — but they were not systematically assessed through the same form. Cross-agency quality comparison requires Jake's manual review, not this automated data.

---

## 4. Top 10 DCTs Overall by Qualified Lead Count

| Rank | DCT | Source | Qualified | Total | Qual Rate |
|---:|---|---|---:|---:|---:|
| 1 | DCT_103_Luiz_Confession [Imaging Wire] | TFM | 199 | 793 | 25.1% |
| 2 | DCT_104_Luiz_Life hack [Digital Health] | TFM | 147 | 620 | 23.7% |
| 3 | DCT_103_Luiz_Confession [Cardiac Wire] | TFM | 95 | 1,265 | 7.5% |
| 4 | DCT_118_Text Call out | TFM | 74 | 401 | 18.5% |
| 5 | DCT_123_If you, BUT | TFM | 53 | 224 | 23.7% |
| 6 | DCT_115_AppleNotesTransformation | TFM | 48 | 204 | 23.5% |
| 7 | DCT_114_ReplaceJournals | TFM | 46 | 174 | 26.4% |
| 8 | DCT_104_Luiz_Life hack [Cardiac Wire] | TFM | 36 | 794 | 4.5% |
| 9 | DCT_102_Luiz_Why read X? [Digital Health] | TFM | 24 | 87 | 27.6% |
| 10 | DCT_104_Luiz_Life hack [Imaging Wire] | TFM | 19 | 66 | 28.8% |

**All top 10 are TFM.** No Growletter DCT produced more than 7 qualified leads. The top GL DCT is `lifehack_jobroles_cw` with 7 qualified out of 9,456 leads on CW (0.07%).

---

## 5. Top 5 DCTs Per Newsletter -- TFM and Growletter

### Cardiac Wire

**TFM -- by qualified leads:**

| DCT | Qualified | Total | Qual Rate |
|---|---:|---:|---:|
| DCT_103_Luiz_Confession [Cardiac Wire] | 57 | 1,001 | 5.7% |
| DCT_118_Text Call out | 50 | 310 | 16.1% |
| DCT_103_Luiz_Confession [Imaging Wire] | 38 | 103 | 36.9% |
| DCT_104_Luiz_Life hack [Digital Health] | 29 | 79 | 36.7% |
| DCT_104_Luiz_Life hack [Cardiac Wire] | 21 | 578 | 3.6% |

**Growletter -- by qualified leads (only 2 DCTs have any):**

| DCT | Qualified | Total | Qual Rate |
|---|---:|---:|---:|
| lifehack_jobroles_cw | 7 | 9,456 | 0.07% |
| 2025resolution_cw | 1 | 307 | 0.33% |

**Growletter -- by volume (since qualification is near-zero):**

| DCT | Total | Form Complete | Form Rate |
|---|---:|---:|---:|
| lifehack_jobroles_cw | 9,456 | 1,515 | 16.0% |
| 8/9 CW DTE | 889 | 47 | 5.3% |
| 2025resolution_cw | 307 | 24 | 7.8% |
| lifehack_dhw | 299 | 74 | 24.7% |
| lifehack_dhw_30k_v3landingpage | 284 | 73 | 25.7% |

### Imaging Wire

**TFM -- by qualified leads:**

| DCT | Qualified | Total | Qual Rate |
|---|---:|---:|---:|
| DCT_103_Luiz_Confession [Imaging Wire] | 120 | 590 | 20.3% |
| DCT_114_ReplaceJournals | 29 | 123 | 23.6% |
| DCT_104_Luiz_Life hack [Digital Health] | 19 | 59 | 32.2% |
| DCT_103_Luiz_Confession [Cardiac Wire] | 14 | 114 | 12.3% |
| DCT_118_Text Call out | 10 | 40 | 25.0% |

**Growletter -- by qualified leads (only 2 DCTs have any):**

| DCT | Qualified | Total | Qual Rate |
|---|---:|---:|---:|
| TIW US+Can 2.4.2023 Ad DTE | 2 | 516 | 0.39% |
| lifehack_jobroles_cw | 1 | 1,690 | 0.06% |

**Growletter -- by volume:**

| DCT | Total | Form Complete | Form Rate |
|---|---:|---:|---:|
| lifehack_jobroles_cw | 1,690 | 639 | 37.8% |
| TIW US+Can 2.4.2023 Ad DTE | 516 | 33 | 6.4% |
| lifehack_dhw | 199 | 45 | 22.6% |
| lifehack_dhw_30k_v3landingpage | 135 | 33 | 24.4% |
| og_lifehacktext | 102 | 28 | 27.5% |

### Digital Health Wire

**TFM -- by qualified leads:**

| DCT | Qualified | Total | Qual Rate |
|---|---:|---:|---:|
| DCT_104_Luiz_Life hack [Digital Health] | 99 | 482 | 20.5% |
| DCT_103_Luiz_Confession [Imaging Wire] | 41 | 107 | 38.3% |
| DCT_115_AppleNotesTransformation | 36 | 167 | 21.6% |
| DCT_123_If you, BUT | 35 | 184 | 19.0% |
| DCT_103_Luiz_Confession [Cardiac Wire] | 24 | 150 | 16.0% |

**Growletter -- by qualified leads (only 1 DCT has any):**

| DCT | Qualified | Total | Qual Rate |
|---|---:|---:|---:|
| lifehack_jobroles_cw | 1 | 2,657 | 0.04% |

**Growletter -- by volume:**

| DCT | Total | Form Complete | Form Rate |
|---|---:|---:|---:|
| lifehack_jobroles_cw | 2,657 | 1,030 | 38.8% |
| lifehack_dhw_30k_v3landingpage | 1,019 | 70 | 6.9% |
| lifehack_dhw | 882 | 119 | 13.5% |
| dhw_video_textoverlay_lifehack-newaudience-dhw | 625 | 28 | 4.5% |
| 6/13 DHW Video Ad USA DTE | 328 | 33 | 10.1% |

---

## 6. Qualification Rate Per DCT (min 20 total leads)

### Top 20 by Qualification Rate

| DCT | Segment | Qual Rate | Qualified | Total |
|---|---|---:|---:|---:|
| DCT_123_If you, BUT | TFM / CW | **45.5%** | 10 | 22 |
| DCT_103_Luiz_Confession [Imaging Wire] | TFM / DHW | **38.3%** | 41 | 107 |
| DCT_115_AppleNotesTransformation | TFM / CW | **38.1%** | 8 | 21 |
| DCT_103_Luiz_Confession [Imaging Wire] | TFM / CW | **36.9%** | 38 | 103 |
| DCT_104_Luiz_Life hack [Digital Health] | TFM / CW | **36.7%** | 29 | 79 |
| DCT_114_ReplaceJournals | TFM / CW | **36.4%** | 8 | 22 |
| DCT_104_Luiz_Life hack [Digital Health] | TFM / IW | **32.2%** | 19 | 59 |
| DCT_114_ReplaceJournals | TFM / DHW | **31.0%** | 9 | 29 |
| DCT_118_Text Call out | TFM / DHW | **27.5%** | 14 | 51 |
| DCT_122_Make Better Decisions | TFM / DHW | **26.7%** | 8 | 30 |
| DCT_118_Text Call out | TFM / IW | **25.0%** | 10 | 40 |
| DCT_102_Luiz_Why read X? [Digital Health] | TFM / DHW | **24.1%** | 14 | 58 |
| DCT_114_ReplaceJournals | TFM / IW | **23.6%** | 29 | 123 |
| DCT_115_AppleNotesTransformation | TFM / DHW | **21.6%** | 36 | 167 |
| DCT_104_Luiz_Life hack [Digital Health] | TFM / DHW | **20.5%** | 99 | 482 |
| DCT_103_Luiz_Confession [Imaging Wire] | TFM / IW | **20.3%** | 120 | 590 |
| DCT_123_If you, BUT | TFM / DHW | **19.0%** | 35 | 184 |
| DCT_104_Luiz_Life hack [Imaging Wire] | TFM / IW | **18.6%** | 8 | 43 |
| DCT_112_EndangerPatient | TFM / CW | **16.7%** | 8 | 48 |
| DCT_118_Text Call out | TFM / CW | **16.1%** | 50 | 310 |

### Bottom 20 by Qualification Rate (all Growletter except two TFM entries)

| DCT | Segment | Qual Rate | Qualified | Total |
|---|---|---:|---:|---:|
| lifehack_jobroles_cw | GL / IW | 0.06% | 1 | 1,690 |
| lifehack_jobroles_cw | GL / DHW | 0.04% | 1 | 2,657 |
| 8/9 CW DTE | GL / CW | 0.00% | 0 | 889 |
| lifehack_dhw_30k_v3landingpage | GL / CW | 0.00% | 0 | 284 |
| lifehack_dhw | GL / CW | 0.00% | 0 | 299 |
| dhw_video_textoverlay_lifehack-newaudience-dhw | GL / CW | 0.00% | 0 | 71 |
| DCT_105_Luiz_UGC doctor [Cardiac Wire] | TFM / IW | 0.00% | 0 | 20 |
| 2025resolution_cw | GL / IW | 0.00% | 0 | 39 |
| lifehack_dhw_30k_v3landingpage | GL / IW | 0.00% | 0 | 135 |
| lifehack_static_patientscan_tiw | GL / IW | 0.00% | 0 | 46 |
| lifehack_dhw | GL / IW | 0.00% | 0 | 199 |
| og_lifehacktext | GL / IW | 0.00% | 0 | 102 |
| DCT_105_Luiz_UGC doctor [Cardiac Wire] | TFM / DHW | 0.00% | 0 | 24 |
| lifehack_dhw_30k_v3landingpage | GL / DHW | 0.00% | 0 | 1,019 |
| 6/13 DHW Video Ad USA DTE | GL / DHW | 0.00% | 0 | 328 |
| lifehack_dhw | GL / DHW | 0.00% | 0 | 882 |
| 2025resolution_cw | GL / DHW | 0.00% | 0 | 73 |
| dhw_video_textoverlay_lifehack-newaudience-dhw | GL / DHW | 0.00% | 0 | 625 |
| og_lifehacktext | GL / DHW | 0.00% | 0 | 43 |
| lifehack_static_patientscan_tiw | GL / DHW | 0.00% | 0 | 23 |

**Every single top-20 entry is TFM. Every single bottom-20 entry is Growletter (plus two underperforming TFM creatives: DCT_105 UGC doctor).**

---

## 7. Job Title Analysis -- Top Qualified Titles by Source x Newsletter

### Cardiac Wire -- Qualified Titles

**TFM (259 qualified):**

| Title | Count |
|---|---:|
| Cardiologist | 12 |
| Physician | 10 |
| MD | 9 |
| CEO | 8 |
| Resident | 6 |
| Nurse practitioner | 5 |
| Fellow | 5 |
| Radiologist | 4 |
| Ceo | 4 |
| RN | 4 |
| PA | 3 |
| President | 3 |
| Consultant | 3 |
| Np | 3 |

**Growletter (8 qualified -- complete list):**

| Title | Count |
|---|---:|
| Cardiologist | 2 |
| MD radiologist | 1 |
| md | 1 |
| APRN | 1 |
| PA-C | 1 |
| NP | 1 |
| Fellow | 1 |

### Imaging Wire -- Qualified Titles

**TFM (255 qualified):**

| Title | Count |
|---|---:|
| Radiologist | 24 |
| MD | 9 |
| CEO | 5 |
| MRI Technologist | 4 |
| Radiographer | 4 |
| Ceo | 3 |
| Sonographer | 3 |
| Owner | 3 |
| Cardiologist | 3 |
| Consultant | 3 |
| Student | 3 |

**Growletter (3 qualified -- complete list):**

| Title | Count |
|---|---:|
| Mammo tech | 1 |
| Ct tech | 1 |
| md | 1 |

### Digital Health Wire -- Qualified Titles

**TFM (314 qualified):**

| Title | Count |
|---|---:|
| CEO | 22 |
| Ceo | 9 |
| Director | 7 |
| Founder | 7 |
| Radiologist | 6 |
| COO | 6 |
| Physician | 5 |
| MD | 5 |
| Owner | 4 |
| Consultant | 4 |
| President | 3 |
| Cardiologist | 3 |
| Executive Director | 3 |
| Fellow | 3 |
| RN | 3 |

**Growletter (1 qualified -- complete list):**

| Title | Count |
|---|---:|
| md | 1 |

---

## 8. Seniority Distribution by Source

> **Note:** Title/seniority distribution is a fair comparison because it comes from Mailchimp merge fields (TITLE), not from TFM's qualification form. However, GL leads fill title fields at much lower rates (79-70% empty vs 61-75% for TFM), so GL's distribution is based on a smaller assessed sample. The "GL Qual" and "GL Q%" columns below use TFM's QUALIFIED field which GL leads were NOT systematically assessed through — these columns are shown for completeness but should not be interpreted as GL's true quality rate.

Title tiers: Executive/Director, Senior Clinical (MD/DO/Specialist), Mid-level Clinical (NP/PA/Supervisor), Entry-level Clinical (RN/Tech), Non-clinical, Other/Unclassified, Unknown/Empty.

### Cardiac Wire

| Tier | TFM Count | TFM % | TFM Qual | TFM Q% | GL Count | GL % | GL Qual | GL Q% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Executive/Director | 145 | 5.8% | 48 | 33.1% | 248 | 2.2% | 0 | 0.0% |
| Senior Clinical | 131 | 5.2% | 77 | 58.8% | 186 | 1.6% | 5 | 2.7% |
| Mid-level Clinical | 30 | 1.2% | 19 | 63.3% | 201 | 1.8% | 3 | 1.5% |
| Entry-level Clinical (RN/Tech) | 74 | 3.0% | 35 | 47.3% | 1,068 | 9.4% | 0 | 0.0% |
| Non-clinical | 111 | 4.4% | 25 | 22.5% | 216 | 1.9% | 0 | 0.0% |
| Other/Unclassified | 148 | 5.9% | 54 | 36.5% | 443 | 3.9% | 0 | 0.0% |
| Unknown/Empty | 1,865 | 74.5% | 1 | 0.1% | 9,000 | 79.2% | 0 | 0.0% |

### Imaging Wire

| Tier | TFM Count | TFM % | TFM Qual | TFM Q% | GL Count | GL % | GL Qual | GL Q% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Executive/Director | 105 | 8.4% | 44 | 41.9% | 122 | 4.3% | 0 | 0.0% |
| Senior Clinical | 100 | 8.0% | 67 | 67.0% | 87 | 3.1% | 1 | 1.1% |
| Mid-level Clinical | 14 | 1.1% | 6 | 42.9% | 78 | 2.7% | 0 | 0.0% |
| Entry-level Clinical (RN/Tech) | 95 | 7.6% | 65 | 68.4% | 487 | 17.1% | 2 | 0.4% |
| Non-clinical | 76 | 6.1% | 31 | 40.8% | 104 | 3.7% | 0 | 0.0% |
| Other/Unclassified | 97 | 7.7% | 41 | 42.3% | 237 | 8.3% | 0 | 0.0% |
| Unknown/Empty | 766 | 61.1% | 1 | 0.1% | 1,732 | 60.8% | 0 | 0.0% |

### Digital Health Wire

| Tier | TFM Count | TFM % | TFM Qual | TFM Q% | GL Count | GL % | GL Qual | GL Q% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Executive/Director | 202 | 13.4% | 132 | 65.3% | 216 | 3.8% | 0 | 0.0% |
| Senior Clinical | 65 | 4.3% | 44 | 67.7% | 100 | 1.7% | 1 | 1.0% |
| Mid-level Clinical | 14 | 0.9% | 8 | 57.1% | 111 | 1.9% | 0 | 0.0% |
| Entry-level Clinical (RN/Tech) | 63 | 4.2% | 35 | 55.6% | 770 | 13.5% | 0 | 0.0% |
| Non-clinical | 106 | 7.0% | 35 | 33.0% | 190 | 3.3% | 0 | 0.0% |
| Other/Unclassified | 134 | 8.9% | 58 | 43.3% | 343 | 6.0% | 0 | 0.0% |
| Unknown/Empty | 921 | 61.2% | 2 | 0.2% | 3,986 | 69.7% | 0 | 0.0% |

### Key seniority findings

**TFM concentrations by newsletter:**
- **CW:** 5.8% Executive/Director + 5.2% Senior Clinical = 11.0% high-value roles
- **IW:** 8.4% Executive/Director + 8.0% Senior Clinical = 16.4% high-value roles
- **DHW:** 13.4% Executive/Director + 4.3% Senior Clinical = 17.7% high-value roles (strongest exec concentration)

**Growletter concentrations by newsletter:**
- **CW:** 2.2% Executive/Director + 1.6% Senior Clinical = 3.8% high-value roles, BUT 9.4% Entry-level Clinical (mostly RNs)
- **IW:** 4.3% Executive/Director + 3.1% Senior Clinical = 7.3% high-value roles, BUT 17.1% Entry-level Clinical
- **DHW:** 3.8% Executive/Director + 1.7% Senior Clinical = 5.5% high-value roles, BUT 13.5% Entry-level Clinical

**The GL pattern across all newsletters:** Heavy RN/tech concentration, low exec/specialist concentration. The GL Entry-level Clinical rate (9.4-17.1%) is 3-4x the TFM rate (3.0-7.6%).

---

## 9. Non-Qualified Patterns

### What non-qualified leads look like by source

**TFM non-qualified top titles (across all newsletters):**
- Owner, Retired, CEO, RN, President, None, Physician, Resident, MD
- Dominant pattern: a mix of legitimate professionals who didn't qualify plus retired/non-applicable
- TFM non-qualified leads are 77-83% title-empty (never filled out the form)

**Growletter non-qualified top titles (across all newsletters):**
- **RN is the #1 title by a wide margin in every single newsletter segment**
  - CW: 454x RN, 97x Rn, 85x Registered Nurse (~636 combined for case variants)
  - IW: 170x RN, 34x Rn, 28x Registered Nurse (~232 combined)
  - DHW: 295x RN, 71x Rn, 64x Registered Nurse (~430 combined)
- After nurses: Owner, Nurse (generic), NP, Paramedic, LPN, Retired, Cardiac Sonographer
- GL non-qualified leads are 61-79% title-empty

**The RN concentration in Growletter data is overwhelming.** Combining all case variants of "RN" and "Registered Nurse" across all GL newsletter segments, there are approximately 1,300+ nurse leads. These are not the audience Insight Links sells to their B2B advertisers.

### Seniority breakdown of non-qualified leads (all newsletters combined)

| Source | Executive/Dir | Senior Clinical | Mid-level | Entry-level (RN/Tech) | Non-clinical | Unknown |
|---|---:|---:|---:|---:|---:|---:|
| TFM (all NLs) | 228 (5.1%) | 108 (2.4%) | 25 (0.6%) | 97 (2.2%) | 201 (4.5%) | 3,548 (79.9%) |
| GL (all NLs) | 586 (3.0%) | 366 (1.9%) | 387 (2.0%) | 2,323 (11.7%) | 500 (2.5%) | 14,718 (74.4%) |

**GL has 2,323 entry-level clinical non-qualified leads (11.7% of all non-qualified), vs TFM's 97 (2.2%).** This is the clearest structural difference in audience composition.

---

## 10. The Honest TFM vs Growletter Story

### Where Growletter definitively wins

1. **Volume -- and it is not close.** GL delivers 3.8x more total subscribers. On Cardiac Wire it is 4.5x. Even on the "problem" newsletter (Imaging Wire), GL delivers 2.3x TFM's volume. If Jake only cared about raw subscriber count, GL would be the obvious choice.

2. **Absolute form completions on CW and DHW.** Despite lower form-completion rates, GL's volume advantage means they still deliver more completed forms on CW (1,798 vs 629) and DHW (1,336 vs 584). That is real first-party data at scale.

3. **Cost efficiency (implied).** GL delivers more bodies per dollar. Their raw CPL advantage, documented elsewhere, holds up in total subscriber delivery.

### Where TFM's data shows strength (TFM-internal metrics)

1. **828 qualified leads through TFM's ICP form.** TFM's post-subscribe form identified 828 qualified professionals (15.7% of TFM subs). This is TFM's own measurement system — GL's funnel does not include this form, so GL's 12 qualified leads reflect "never assessed," not a quality comparison.

2. **High-value title concentration (among leads who filled title fields).** TFM delivers 11-18% Executive/Director + Senior Clinical roles depending on newsletter. GL delivers 3.8-7.3%. This comparison uses the TITLE merge field (not the QUALIFIED form), but GL leads fill title fields at lower rates, so GL's distribution is based on a smaller sample.

3. **ICP accuracy on Imaging Wire (Jake's manual assessment).** Jake manually reviewed both agencies' IW leads and found TFM delivered 12 radiologists vs GL's 0. This is the only cross-agency quality comparison validated by the client directly. IW is 65% of Insight Links revenue.

4. **DHW executive delivery.** TFM's DHW pool is 13.4% Executive/Director among those who filled title fields — the exact audience Jake says his DHW advertisers want. TFM produced 31 qualified CEOs on DHW alone through the ICP form.

### What we can't determine from this data

1. **GL's actual lead quality.** GL's funnel does not include TFM's post-subscribe ICP questions. GL leads never see the form. Their 93-95% empty QUALIFIED fields mean "never assessed," not "failed." We cannot determine GL's true qualification rate from this data — only Jake's manual review can compare quality across agencies.

2. **Whether GL's titled leads would qualify.** GL has 248 Executive/Director leads on CW, 122 on IW, 216 on DHW — but these leads were never assessed through TFM's form. They may or may not meet Jake's ICP criteria. We don't know.

3. **The silent majority.** 61-79% of leads across BOTH sources never fill in their title. The seniority analysis covers only the 20-39% who do. The actual audience composition of the majority is unknown for both agencies.

### What IS clear regardless of measurement system

1. **TFM's CW qualification rate is notably lower than IW/DHW.** 10.3% on CW vs 20.4% on IW vs 20.9% on DHW. This is a TFM-internal finding showing Cardiac Wire is the hardest newsletter to qualify leads for.

2. **GL wins on volume.** 3.8x more subscribers overall. GL's raw CPL advantage is real.

3. **Both agencies serve different audience profiles.** Among leads who DO fill title fields, GL skews Entry-level Clinical (RN/Tech at 9.4-17.1%) while TFM skews Senior Clinical and Executive. Whether this matters depends on what Jake's advertisers value.

### The bottom line for the bake-off

**The question Jake needs to answer is: does he value 828 qualified leads or 19,925 total subscribers?**

At $100-150/qualified lead to his advertisers, TFM's 828 qualified leads represent $82,800-$124,200 in potential advertiser revenue. GL's 12 qualified leads represent $1,200-$1,800.

At the same time, GL's 19,925 subscribers are real email addresses that receive the newsletter. They may open, click, and generate advertising impressions even if they never become qualified leads for direct advertiser campaigns. The value of those subscribers depends entirely on how Insight Links monetizes them.

If the business model is "sell qualified leads to advertisers at $100-150 each" -- TFM wins by 69x.
If the business model is "grow the subscriber base for CPM-based newsletter advertising" -- GL wins by 3.8x.

Jake has said repeatedly that qualified leads are what matters. The data supports TFM on that metric overwhelmingly.

---

## Appendix: TFM DCT Performance Summary (All Newsletters Combined)

| DCT | Total Leads | Qualified | Qual Rate | Best Newsletter |
|---|---:|---:|---:|---|
| DCT_103_Luiz_Confession [IW] | 793 | 199 | 25.1% | IW (120q), DHW (41q), CW (38q) |
| DCT_104_Luiz_Life hack [DH] | 620 | 147 | 23.7% | DHW (99q), CW (29q), IW (19q) |
| DCT_103_Luiz_Confession [CW] | 1,265 | 95 | 7.5% | CW (57q), DHW (24q), IW (14q) |
| DCT_118_Text Call out | 401 | 74 | 18.5% | CW (50q), DHW (14q), IW (10q) |
| DCT_123_If you, BUT | 224 | 53 | 23.7% | DHW (35q), CW (10q), IW (8q) |
| DCT_115_AppleNotesTransformation | 204 | 48 | 23.5% | DHW (36q), CW (8q), IW (4q) |
| DCT_114_ReplaceJournals | 174 | 46 | 26.4% | IW (29q), DHW (9q), CW (8q) |
| DCT_104_Luiz_Life hack [CW] | 794 | 36 | 4.5% | CW (21q), IW (8q), DHW (7q) |
| DCT_102_Luiz_Why read X? [DH] | 87 | 24 | 27.6% | DHW (14q), CW (6q), IW (5q) |
| DCT_104_Luiz_Life hack [IW] | 66 | 19 | 28.8% | IW (8q), DHW (6q), CW (5q) |
| DCT_112_EndangerPatient | 60 | 10 | 16.7% | CW (8q), DHW (2q) |
| DCT_122_Make Better Decisions | 36 | 10 | 27.8% | DHW (8q), CW (2q) |
| DCT_101_Luiz_Reasons Why [CW] | 237 | 9 | 3.8% | Low qual across all |

### Notes on TFM creative performance

- **Highest qualification rate at scale:** DCT_104_Life hack [Imaging Wire] (28.8%) and DCT_102_Why read X? [Digital Health] (27.6%), but both have limited volume
- **Best combination of volume + quality:** DCT_103_Confession [Imaging Wire] -- 793 leads, 199 qualified (25.1%). This is the workhorse. (Note: prior versions showed 800 total; 793 reflects the deduplicated dashboard count as of March 22.)
- **Rising star:** DCT_118_Text Call out -- 401 leads, 74 qualified (18.5%). Especially strong on CW where it is the best quality-adjusted performer (50 qualified at 16.1% rate vs DCT_103 CW's 57 qualified at 5.7% rate).
- **Highest efficiency:** DCT_123_If you, BUT -- 224 leads, 53 qualified (23.7%). Newest format, proving out well.
- **CW-specific problem:** The two highest-volume CW creatives (DCT_103 Confession CW at 5.7% and DCT_104 Life hack CW at 3.6%) have the lowest qualification rates. CW volume is being driven by creatives that attract the wrong audience. DCT_118 Text Call out at 16.1% CW qual rate is the fix -- shift more budget there.
- **DCT_105_UGC doctor is a confirmed non-performer:** 0 qualified leads across IW and DHW placements, and only 1/85 on CW.

---

*Analysis generated March 22, 2026 from 25,187 Mailchimp subscriber records across 47 JSON export files (6 TFM + 41 Growletter). All qualification data reflects the Mailchimp QUALIFIED merge field as recorded in the exports.*
