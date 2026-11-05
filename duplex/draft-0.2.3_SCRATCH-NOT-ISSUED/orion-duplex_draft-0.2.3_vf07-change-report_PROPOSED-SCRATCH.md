# MMUCO ORION proposed Draft 0.2.3: VF-07 Option A change report

**SCRATCH REVIEW COPY: NOT ISSUED, NOT APPROVED, NOT A COMPLIANCE ASSESSMENT.**

- No Draft 0.2.3 has been issued. Draft 0.2.2 and every earlier frozen file are unchanged; see the Validation Report, section 2.
- Every value below is **MEASURED** from the saved DXFs by script unless it is labelled ESTIMATE, ASSUMPTION or REQUIRES CONFIRMATION.

---

## 1. What was asked and what was done

**Selected option (your instruction): VF-07 Option A.**

- Keep the kitchen-to-utility pocket door and its opening location.
- Shorten the kitchen base run by 300 mm to give a nominal 300 mm kitchen-side nib.
- Do this in both dwellings.

**Done, in a scratch copy only:**

| Step | Action |
|---|---|
| 1 | Took a byte copy of the issued `MMUCO_ORION_Duplex_Draft_0.2.2.dxf` (SHA-256 2ec8d3f3…d17b) |
| 2 | Dwelling A, base run 1E0: moved vertices 0 and 3 from x 2,100 to x 2,400 (CADCraft `pedit` vertex move) |
| 3 | Dwelling B, base run 1E1: moved vertices 1 and 2 from x 16,500 to x 16,200. The B outline's vertex order is not the mirror of A's: its latch-end vertices are indices 1 and 2. The indices were read from the B entity itself |
| 4 | Added one associative nib dimension per dwelling: 47EF (wall 125 vertex 3 to 1E0 vertex 0) and 47F0 (1E1 vertex 1 to wall 126 vertex 2). Each anchor point belongs to exactly one entity, checked before dimensioning |
| 5 | Marked the sheet as a proposed, unissued scratch copy: title 2DA, status line 2DC, revision line 147E, notes 2F8, scale note 2FB |
| 6 | Updated the scale note 2FB only after measuring the plotted scale |
| 7 | Saved as `MMUCO_ORION_Duplex_Draft_0.2.3_PROPOSED_SCRATCH_NOT_ISSUED.dxf` |

Not changed: walls, the pocket door (opening, cavity, leaf), services, every other unit, every other dimension, and room labels. The whole-drawing entity diff shows **526 entities unchanged, 7 modified, 2 added, 0 removed**; see `..._Entity_Change_List_SCRATCH.csv`.

**Design basis:**

- Dwelling A in the proposed DXF measures **identically** to the VF-07 Option A study on every compared value (evidence `01_measurements/crosscheck_vf07_measure_A_023.json`, using the investigation's own measuring code). The values compared were opening, both nibs, nib zone, approaches, base run, unit widths, ADM 2.24b clearances, free floor, GIA and residual.
- Against the Option A scratch DXF, the only differences are dwelling B's base run, the annotations and the two new dimensions.

---

## 2. Before and after, both dwellings (MEASURED, `d023_checks.mjs`)

**Measurement method:**

- Each dwelling is measured from its own entities in the saved DXF.
- Dwelling B is read through the exact reflection x′ = 18,600 − x, so the same code applies, and results are reported in B's native coordinates. No dwelling-A data is used for B.
- Nibs are measured along the wall face from the structural jamb at the latch end to the first wall or fixed unit within 600 mm of the face.

| Measure | A: 0.2.2 | A: 0.2.3 | B: 0.2.2 | B: 0.2.3 |
|---|---|---|---|---|
| Q4 wall pieces | 123 [300, 8,700, 1,250, 8,800]; 125 [2,100, 8,700, 4,300, 8,800] | unchanged | 124 [17,350, 8,700, 18,300, 8,800]; 126 [14,300, 8,700, 16,500, 8,800] | unchanged |
| Structural opening (x, width) | 1,250–2,100, **850** | 1,250–2,100, **850** | 16,500–17,350, **850** | 16,500–17,350, **850** |
| Pocket cavity / leaf | 25D5 [350, 8,725, 1,250, 8,775] 900 / 25D6 900, 50 overlap, in piece 123 | unchanged | 25D7 [17,350, 8,725, 18,250, 8,775] 900 / 25D8 900, 50 overlap, in piece 124 | unchanged |
| Latch jamb x | 2,100 | 2,100 | 16,500 | 16,500 |
| **Kitchen-side latch nib** | **0** (unit 1E0 at x 2,100) | **300** (unit 1E0 at x 2,400) | **0** (unit 1E1 at x 16,500) | **300** (unit 1E1 at x 16,200) |
| Kitchen nib zone (300 wide), clear depth | none | **2,600** (to rear run 1DC) | none | **2,600** (to rear run 1DD) |
| Kitchen wall nib (to the Q5 wall) | 2,200 (12D) | 2,200 | 2,200 (12E) | 2,200 |
| Utility-side latch nib | 700 (wall 121), zone 1,400 deep | 700, 1,400 | 700 (wall 122), zone 1,400 deep | 700, 1,400 |
| Pocket-jamb nibs, kitchen / utility | 950 / 950 | 950 / 950 | 950 / 950 | 950 / 950 |
| Approach depth across the opening, kitchen / utility | 2,600 / 1,400 | 2,600 / 1,400 | 2,600 / 1,400 | 2,600 / 1,400 |
| 1,200 mm-deep clear band on the kitchen side | x 900–2,100 (1,200 wide) | x 900–2,400 (1,500) | x 16,500–17,700 (1,200) | x 16,200–17,700 (1,500) |
| Base run | 1E0 [2,100, 8,800, 4,300, 9,400], 2,200 | 1E0 [2,400, 8,800, 4,300, 9,400], **1,900** | 1E1 [14,300, 8,800, 16,500, 9,400], 2,200 | 1E1 [14,300, 8,800, 16,200, 9,400], **1,900** |
| Unit widths from the latch end | 600 / 600 / 600 / 400 | **300** / 600 / 600 / 400 | 600 / 600 / 600 / 400 | **300** / 600 / 600 / 400 |
| Base-run footprint | 1.32 m² | 1.14 m² | 1.32 m² | 1.14 m² |
| ADM 2.24b readings: tall units to base-run end / rear to south run | 1,200 / 2,000 | **1,500** / 2,000 | 1,200 / 2,000 | **1,500** / 2,000 |
| Kitchen / utility room area | 12.80 / 5.00 m² | 12.80 / 5.00 m² | 12.80 / 5.00 m² | 12.80 / 5.00 m² |
| Collision sweep | none | none | none | none |
| Sliding leaf, closed / open, outside the cavity | no hits | no hits | no hits | no hits |

**Symmetry and parity:**

- All 15 compared A/B measures are equal in both versions.
- All building geometry pairs across the party wall: each of the 161 dwelling-A geometry entities matches a dwelling-B entity exactly. The other 7 B-side entities are legend swatches, which exist once by design. The unmatched dimensions (7) are dwelling A's front dimension chain, drawn once. Both conditions are identical in 0.2.2.
- The two new dimensions mirror exactly: same value, mirrored anchors, text-position error 0 mm.

---

## 3. Finished-face geometry: how the end panel and worktop affect the nib

**What the DXF draws:**

- Each base run is a single outline. The end panel, worktop edge and door lining are **not drawn**.
- The 300 mm nib is therefore measured to the drawn outline (MEASURED). Its meaning depends on what that outline represents.

**Rules and readings:**

- **Rule written into the proposed drawing (note 2):** the outline is the **finished face** of the end panel or worktop, whichever projects further. On that reading the nib is 300 mm with **0 mm margin**.
- **Reading 2, outline = carcass:** any end panel or worktop overhang outside the outline reduces the nib (ASSUMPTION, a range of thicknesses):

| End panel + worktop overhang outside the outline | 0 | 10 | 18 | 20 | 25 | 30 | 40 |
|---|---|---|---|---|---|---|---|
| Nib to finished face (mm), each dwelling | 300 | 290 | **282** | 280 | 275 | 270 | 260 |

- **Setting-out consequence:**
  - The carcass must start at x ≥ 2,400 + (panel + overhang) in A, and x ≤ 16,200 − (panel + overhang) in B.
  - Each run is fixed between that finished face and the Q5 wall face (x 4,300 / 14,300), so the 1,900 mm must **include** the end panel.
  - The kitchen supplier must confirm carcass widths (OQ-05, OQ-09).
- **Latch-side lining:** ADM measures nibs "from finished wall face to inside edge of door frame" (Diagram 2.2 note 2, project copy).
  - If the latch lining sits inside the structural opening, the nib to the frame edge grows by the lining thickness: 10 → 310, 20 → 320.
  - The clear opening shrinks by the same amount.
  - Skirting may be ignored (same note). Architraves are not addressed: REQUIRES CONFIRMATION (OQ-11).

Source: `evidence/01_measurements/finished_face_sensitivity.json`.

---

## 4. Pocket-door system and clear opening

- **No pocket-door system is selected anywhere in the project** (project folder and source pack searched 24 Oct 2026). The clear opening therefore cannot be measured.
- **ESTIMATE:** 810 mm, using the Draft 0.2.2 ASSUMPTION of opening − 40, with a sensitivity range of 770–810 mm.
- The nominal 850 mm opening is **not** treated as the clear opening.
- **Status: BLOCKED (OQ-06).** The manufacturer must confirm:
  - linings, leaf stand-out and pull or handle;
  - soft-close effect;
  - fit with the 100 mm partition (PROVISIONAL);
  - pocket length and end studs;
  - head detail and fixings;
  - operating force.

---

## 5. Services and other units (MEASURED, unchanged in both dwellings)

| | Dwelling A | Dwelling B |
|---|---|---|
| Kitchen sink / bowl | 19E [1,650, 11,500, 2,450, 11,900] / 1A0 | 19F [16,150, 11,500, 16,950, 11,900] / 1A1 |
| Hob | 1A2 [3,300, 11,450, 3,900, 11,950] | 1A3 [14,700, 11,450, 15,300, 11,950] |
| Utility sink | 1AC [375, 6,725, 875, 7,175] | 1AD [17,725, 6,725, 18,225, 7,175] |
| Washer / dryer | 1AE [900, 6,700, 1,500, 7,300] / 1B2 [1,500, 6,700, 2,100, 7,300] | 1AF [17,100, 6,700, 17,700, 7,300] / 1B3 [16,500, 6,700, 17,100, 7,300] |
| MVHR / cylinder allowance | 1E8 [2,200, 6,700, 2,800, 7,300] | 1E9 [15,800, 6,700, 16,400, 7,300] |
| Tall units / rear run | 1DE / 1DC unchanged | 1DF / 1DD unchanged |
| Fixings on the pocket section | none | none |

No plumbing, ventilation or other service was moved.

---

## 6. New findings recorded separately (not resolved here)

| ID | Finding | Evidence |
|---|---|---|
| NF-01 | **Project design target R-14** ("Access / internal door effective clear width", 850 mm, Logistics row 43, PROPOSED) is above the pocket-door estimate of 810 mm (770–810). Option A neither causes nor fixes this. The VF-07 sweep found a 900 mm opening would need a 400 mm base-run cut (clear 820–860 estimate). This is a project target, not a regulation | OQ-08 |
| NF-02 | The sheet subtitle (2DB) and legend (2E4) name M4(2) as the target. Note 2 correctly states that M4(2) applies only by planning condition. Left unchanged (outside VF-07) | OQ-12 |
| NF-03 | The DXF header extents moved 216 mm west (−4,596 → −4,812) because of the longer status line. The PDF's horizontal placement is unchanged (16.6 mm margins) and the plot scale is verified | Validation Report V-17 |
| NF-04 | The 300 mm nib has 0 mm margin against the 300 mm target. Any construction tolerance or uncounted finish reduces it | OQ-05 |

---

## 7. Review recommendation (not an approval)

**Geometry:** Option A is implemented and verified in both dwellings of the scratch copy.

- Both dwellings measure a 300 mm kitchen-side and 700 mm utility-side nib to the drawn references.
- Approaches, rooms, areas, services, walls and the door itself are unchanged.
- No collisions and no dimension inconsistency.
- Every check is reproducible from the saved files.

**Issue: do not issue Draft 0.2.3 yet.** Two of the brief's stop conditions apply:

1. **The clear opening cannot be measured reliably.** No pocket-door system is selected (OQ-06).
2. **The finished-face nib is not confirmed.** The drawing defines the outline as the finished face, but the kitchen supplier's end panel and worktop details, and the tolerance decision, are missing (OQ-05).

**Next investigation:**

1. Select, or shortlist, a pocket-door system for an 850 mm structural opening in the 100 mm partition. Obtain its data sheet and installation instructions.
2. Obtain the kitchen supplier's layout for the 1,900 mm runs (end panel, worktop end, carcass widths).
3. Re-run `d023_checks.mjs` with the real lining and stand-out, and confirm the clear opening and the nib to the inside edge of the frame.
4. In parallel, obtain the planning decision or LPA confirmation (OQ-01) before any regulatory reading is relied on.
