# Pocket-door candidates for the kitchen–utility door: evidence comparison (DRAFT, research only)

**Status:** research for the designer. **No product is selected.** Nothing here is manufacturer confirmation for this project. OQ-05, OQ-06 and OQ-07 remain **OPEN**. Draft 0.2.3 is **not issued** and the proposed drawing was **not changed**.

Sources were read on 24 Oct 2026; see `POCKET_DOOR_SOURCE_REGISTER.csv`. Calculator outputs are in `evidence/10_research/gate_calc_candidates.json`, produced by `evidence/scripts/gate_calc.mjs` with the new `kit` block from `gate_inputs/pocket_door_candidates_RESEARCH_inputs.json`.

**Evidence labels:**

| Label | Meaning |
|---|---|
| **MFR** | Manufacturer-published (official page or datasheet) but **not confirmed for this project** |
| **RET** | Retailer-published; not manufacturer-verified |
| **MEAS** | Project-measured from the saved proposed DXF |
| **CALC** | Calculated from MFR / RET + MEAS values |
| **ASSUMPTION** | Stated assumption |
| **UNKNOWN** | Not published; needs written confirmation |

---

## 1. What was verified at source

| Candidate | Source (evidence) | Door leaf | Stated clear / passage | Frame width as published | Height (frame / passage) | Finished wall |
|---|---|---|---|---|---|---|
| **JB Kind POCSYSSGL915** | Manufacturer product page, size guide (S-01, **MFR**, undated) | 915 × 1,981 | **890** "Clear Opening Size (walkthrough area)" | **1,925** "Structural Opening Width (SW)" | 2,075 / 1,970 | **125 only** |
| JB Kind POCSYSSGL838 (reference) | S-01 (**MFR**) | 838 × 1,981 | 800 | 1,725 | 2,075 / 1,970 | 125 only |
| **ECLISSE Classic Single, PW 900 × 2,030** | Datasheet ECL-Classic-Single-UK-26, PDF created 2026-08-06 (S-02, **MFR**) | 926 × 2,040 | **900** "MAX. PASSAGE SIZE PW" | **1,894** "OVERALL DIMENSION W", plus 3–5 mm stud tolerance advised | 2,115 / 2,030 | **95 / 100 / 115 / 125** |
| ECLISSE Classic Single, PW 850 × 2,020 | S-02 (**MFR**) | 864 × 2,032 | 850 (maximum) | 1,844, plus 3–5 mm | 2,105 / 2,020 | 95 / 100 / 115 / 125 |
| Scrigno 926 × 2,040 (standard) | Door Superstore listing (S-06, **RET**) | 926 × 2,040 | 900 "Walk Through Area" | 1,910 "Structural opening size" | 2,140 / 2,030 | 125 (retailer) |
| Scrigno 926 × 2,040 (fire-rated listing) | Door Superstore listing (S-07, **RET**) | 926 × 2,040 | 896 (stated as reduced by 10 mm) | 1,930 | 2,005–2,505 / – | 125 (retailer) |

**How the research leads compare with the sources:**

- **JB Kind:** all four lead figures match the manufacturer page: 915 / 890 / 1,925 / 125.
- **ECLISSE:** the 900 mm passage and the 1,894 overall width match the official datasheet. Two qualifications:
  - The passage is a **maximum**. With flush pulls, ECLISSE recommends setting the stop so the door protrudes; the protrusion is not stated.
  - The datasheet advises a 3–5 mm stud tolerance.
- **ECLISSE wall options:** 100 mm and 125 mm are confirmed, and 95 mm and 115 mm are also listed.
- **ECLISSE dimensions 22 and 5:** the elevation shows these at the ends of W. Their meaning is **UNKNOWN**. If they add to the stud opening, the run grows by up to 27 mm.
- **Scrigno:** the lead's 926 / 896 / 1,930 / 900 figures come from the retailer's **fire-rated** listing. The same retailer's standard listing gives 1,910 / 900. No official Scrigno dimension table was found:
  - the brochure (S-05) has none;
  - the 24.9 MB technical file was not reviewed.
- **Scrigno, official FAQ (S-04, dated 30 Aug 2024):** Scrigno Base plasterboard frames exist in **100 and 125 mm** finished walls. The retailer listings show 125 mm only, and which Scrigno line they sell is not identified.

---

## 2. Project constraints (MEAS, proposed 0.2.3 scratch; dwelling B mirrors)

**Measured (MEAS):**

- External wall face x 300. Latch jamb x 2,100.
- **Wall run available to the frame: 1,800 mm.** The current pocket zone is 950 mm (x 300–1,250) and the passage gap 850.
- Kitchen base-run outline x 2,400 (300 mm nib), 1,900 mm long to the Q5 wall face at x 4,300.
- Utility-side return wall x 2,800. Tall-unit face x 900.
- Partition finished thickness **100 mm (PROVISIONAL)**.

**Not measured:**

- **No ceiling or head height** in the project (UNKNOWN).
- Recorded findings that are not product data: clear-opening ESTIMATE 770–810 for the current 850 mm gap; placeholder runs suggesting an 890–930 mm opening for 850 mm clear.

**Calculator assumptions (ASSUMPTION):**

- The frame's pocket end sits at the external wall face.
- The latch side of the frame's stud opening becomes the latch jamb.
- The kitchen nib stays 300 mm from the latch jamb, with **0 mm tolerance and the finished-face datum**, because OQ-05 is unresolved.
- Every millimetre of agreed tolerance, or of carcass offset if the outline is the carcass, shortens the base run by the same amount.

---

## 3. Decision matrix (CALC unless marked; dwelling A shown, dwelling B identical by mirror, checked)

| Candidate | Clear opening | Frame width (structural) | Pocket length needed vs 950 zone | Finished wall | Kitchen impact (latch move; base run; cut vs 0.2.2) | Evidence quality | Outstanding unknowns |
|---|---|---|---|---|---|---|---|
| **ECL-900** ECLISSE Classic PW 900 | 900 **max** (MFR); installed **UNKNOWN** (stop protrusion) | 1,894 + 3–5 = 1,897–1,899 | 997–999 vs 950: **does not fit** | **100 available** (MFR) | Latch +97 to +99 mm; base run 1,801–1,803; cut 397–399 (97–99 more than proposed 0.2.3) | **Best**: official dated datasheet | Installed clear with the chosen pull; meaning of the 22 / 5 dims; head height; lining and stop positions; written confirmation |
| **JBK-915** JB Kind 915 | 890 (MFR, "walkthrough", method undefined); installed **UNKNOWN** | 1,925 (tolerance UNKNOWN) | 1,035 vs 950: **does not fit** | **125 only**: conflicts with the 100 mm partition | Latch +125; base run 1,775; cut 425 (125 more); plus a 25 mm thicker Q4 | Good: official page, but **undated** and no datasheet or installation drawing | Clear-opening definition; 100 mm option?; tolerance; head height; dated documents |
| **SCR-926** Scrigno (retailer, standard) | 900 (RET); installed **UNKNOWN** | 1,910 (RET) | 1,010 vs 950: **does not fit** | 125 (RET); official FAQ: a 100 mm Base version exists | Latch +110; base run 1,790; cut 410 (110 more) | **Weak**: retailer only, two listings conflict | Official product line and table; 100 mm version sizes; clear definition; self-closer −50 mm if fitted |
| SCR-926-FR Scrigno fire-rated (retailer) | 896 (RET) | 1,930 (RET) | 1,034: **does not fit** | 125 (RET) | Latch +130; base run 1,770; cut 430 | Weak: retailer; FD30 variant probably not needed (REQUIRES CONFIRMATION by fire strategy) | As SCR-926 |
| ECL-850 ECLISSE Classic PW 850 | 850 **max**: **0 mm margin**; any protrusion → < 850 | 1,844 + 3–5 = 1,847–1,849 | 997–999: **does not fit** | 100 available | Latch +47 to +49; base run 1,851–1,853; cut 347–349 | Official datasheet | Meets 850 only with the door fully inside the pocket, which needs the PUSH&PULL accessory; ECLISSE disclaims liability if the door is set to enter the pocket completely |
| JBK-838 JB Kind 838 (reference) | 800: **below 850** | 1,725 | 925 vs 950: **fits** | 125 only | Latch could stay (75 mm spare) | Official page | Fails the 850 target; 125 mm wall |

**Checks that hold for every candidate (CALC):**

- Utility-side nib after the move: 570–653 mm, so ≥ 300 throughout.
- Kitchen approach: the passage starts at x ≥ 1,297, clear of the tall units at x 900.
- No drawn service lies in the frame zone. The fixing-exclusion (pocket) zone grows to about x 300–1,335 (A) or the mirror (B).
- A/B results are identical by mirror, checked in the calculator output.

---

## 4. Answers to the questions asked

**What was verified from primary manufacturer sources:**

- **ECLISSE Classic Single:** the full size table, from the official dated datasheet.
- **JB Kind single system:** the sizes, from the official (undated) web page.
- **Scrigno:** only the 100 / 125 mm wall-thickness FAQ. Scrigno dimensions were **not** verified at manufacturer level.

**Which candidates warrant a formal enquiry (designer's choice):**

1. **ECLISSE Classic Single, PW 900.** It is the only candidate with an official dated datasheet **and** a 100 mm wall option.
2. **JB Kind POCSYSSGL915.** Ask about a 100 mm wall version and how its 890 mm figure is defined.
3. **Scrigno.** Only through the manufacturer, for its official table and the 100 mm Base version.

The ECL-850 frame is a fallback question only, because it has no margin.

**Does any candidate fit the current 950 mm pocket zone?**

- **No candidate that states ≥ 850 mm fits.** They need 997–1,035 mm.
- Only the JB Kind 838 frame fits, and it gives 800 mm clear.

**What would be needed to reach 850 mm clear:**

1. A frame of the ECL-900 / JBK-915 / Scrigno class.
2. Moving the latch jamb about **97–130 mm** toward the kitchen in both dwellings, which rebuilds the partition Q4 opening.
3. Cutting the kitchen base run to about **1,770–1,803 mm**, i.e. 397–430 mm shorter than 0.2.2. Any agreed nib tolerance, or a carcass datum, adds to this.
4. Confirming the **installed** clear width with the selected pull or stop.
5. For JB Kind (and Scrigno per the retailer listings): a 125 mm partition. That changes the room depths by 25 mm and is not assessed in CAD. For example, the kitchen would go 3.2 → 3.175 m (12.70 m²), or the utility 2.0 → 1.975 m (4.94 m²) and the store to 2.77 m² (CALC).
6. A head height check against frame heights of 2,075–2,140 mm (the ceiling height is UNKNOWN).

**Does the 300 mm kitchen nib remain valid?**

- As a **dimension from the latch jamb**, yes: every scenario keeps 300 mm. But the base run must move with the latch jamb, so the current 300 mm dimension in the proposed 0.2.3 drawing would be wrong for any of these frames.
- Whether 300 mm survives construction depends on OQ-05 (datum and tolerance), which is still unresolved.

---

## 5. What closes OQ-06 / OQ-07 (unchanged requirements)

- **OQ-06:**
  - the designer names one product and configuration;
  - a dated datasheet and installation drawing for it;
  - the manufacturer's written answers to `RFI_01_POCKET_DOOR_MANUFACTURER_DRAFT.md`;
  - the designer's sign-off.
- **OQ-07:** the installed clear opening for that exact configuration (stop, pull and any closer), assessed in writing by the designer against the 850 mm target and the applicable Approved Document M provisions. **A published maximum passage is not enough.**
- **If a frame of this class is chosen**, the geometry change (latch move, base-run cut, possibly wall thickness) must be authorised separately. It would then be made in a **new, separately named scratch revision** and fully re-validated (`evidence/scripts/rerun_validation.sh`).
