# MMUCO ORION Duplex — Change Log, Draft 0.2.1 → Draft 0.2.2

**Issue:** `MMUCO_ORION_Duplex_Draft_0.2.2`, 24 October 2026
**Type:** design development.

- **Face Me and I Face You:** hallway double-door entries (Option B1), recorded as proposed item HALL-01.
- **Door register:** VF-04 (Option B), VF-05 (Option A), VF-06 (Option B) and VF-07 (Option B), as directed.

**Not approved; no compliance claim.** Details and test results are in `MMUCO_ORION_Duplex_Draft_0.2.2_Door_Resolution_Report.md`.

Coordinates are in mm. Dwelling A is listed; each dwelling-A change has an exact mirror in dwelling B (x′ = 18,600 − x), with its own handle shown. Old and new values are taken from the two DXF files by script (`Evidence/03_geometry_areas_dimensions/entity_changes_0.2.1_to_0.2.2.txt`).

## 1. Summary

| | Count |
|---|---|
| Draft 0.2.1 entities | 511 |
| Draft 0.2.2 entities | 533 |
| Identical (type, layer, every coordinate and text) | 442 |
| Removed | 16 (door lines and arcs) |
| Added | 38: 8 arcs, 14 lines, 4 polylines, 12 dimensions |
| Changed | 53: 16 partition polylines and their 16 associative hatches, 8 utility furniture/sanitary items, 2 conservatory outlines, 11 annotation texts |

**Unchanged (AUTOMATED CHECK):**

- every other wall, every window, the front, quiet-room, bathroom, living-room, conservatory and utility side doors;
- all other furniture and fittings;
- all provisional and external-works entities other than the conservatory outlines;
- the 33 Draft 0.2.1 dimensions;
- all room areas, GIA and the footprint.

## 2. HALL-01: Face Me and I Face You double-door entries (B1)

**Wall piers shortened.** Openings widen from 1,000 mm (y 2,800–3,800) to 1,400 mm (y 2,500–3,900):

| Handle | Was (y range) | Now (y range) | Mirror |
|---|---|---|---|
| 127 (hall / Room A, south pier) | 300–2,800 | 300–**2,500** | 128 |
| 129 (hall / Room A, north pier) | 3,800–4,300 | **3,900**–4,300 | 12A |
| 131 (hall / Room B, south pier) | 300–2,800 | 300–**2,500** | 132 |
| 133 (hall / Room B, north pier) | 3,800–5,000 | **3,900**–5,000 | 134 |

The associated wall hatches 2A0–2B1 updated with their polylines. All other wall polylines are unchanged.

**Doors removed (old endpoints and values):**

| Handle | Was |
|---|---|
| 16E / 16C (Room A) | Arc c(4,300, 3,800) r 1,000, 180°→270°; leaf (4,300, 3,800)–(3,300, 3,800) |
| 174 / 176 (Room B) | Leaf (6,000, 3,800)–(7,000, 3,800); arc c(6,000, 3,800) r 1,000, 270°→0° |
| 16D / 16F, 175 / 177 | Dwelling B mirrors |

**Doors added:**

| Handle | New |
|---|---|
| 25C1 / 25C2 | Room A main leaf 900: arc c(4,300, 3,900) r 900, 180°→270°; open leaf (4,300, 3,900)–(3,400, 3,900) |
| 25C3 / 25C4 | Room A secondary leaf 500: arc c(4,300, 2,500) r 500, 90°→180°; open leaf (4,300, 2,500)–(3,800, 2,500) |
| 25C5 / 25C6 | Room B main leaf 900: arc c(6,000, 3,900) r 900, 270°→0°; open leaf (6,000, 3,900)–(6,900, 3,900) |
| 25C7 / 25C8 | Room B secondary leaf 500: arc c(6,000, 2,500) r 500, 0°→90°; open leaf (6,000, 2,500)–(6,500, 2,500) |
| 25C9–25D0 | Dwelling B mirrors |

**Dimensions added** (inside the halls; associative to wall vertices):

| Handles | Chain | Segments |
|---|---|---|
| 25DB / 25DC / 25DD | Room A chain at x 4,700 | (4,400, 300)–(4,400, 2,500) = 2,200; –(4,400, 3,900) = 1,400; –(4,300, 4,000) = 100 |
| 25DE / 25DF / 25E0 | Room B chain at x 5,600 | (5,900, 300)–(5,900, 2,500) = 2,200; –(5,900, 3,900) = 1,400; –(6,000, 4,300) = 400 |
| 25E1–25E6 | Dwelling B mirrors | At x 13,900 and 13,000 |

**Text positions:**

- 100 / 400 segment texts set beside their own lines: 25DD at (4,560, 3,950), 25E0 at (5,460, 4,100); dwelling B 25E3 and 25E6 mirrored.
- 2,200 text of 25DE moved to (5,460, 1,750), and 25E4 to (13,140, 1,750), to clear the front-door arc.

**Hall labels moved** to clear the new dimensions:

| Handle | Text | Move |
|---|---|---|
| 25C / 25D | "HALL" | +650 mm north |
| 25E / 25F | "1.5 x 6.6 9.90" | +690 mm north |

The text content is unchanged.

## 3. Door register

### VF-04 store (Option B): widen the opening, keep the walk-in store

| Handle | Was | Now |
|---|---|---|
| 12B (store / living wall, south pier) | y 5,300–7,400 | y 5,300–**7,100** (mirror 12C) |
| 12D (north pier) | y 8,400–9,200 | y **8,700**–9,200 (mirror 12E) |
| Store panels | 18C (4,330, 7,400)–(4,330, 7,950) and 18E (4,370, 7,850)–(4,370, 8,400): opening 1,000, panels 550, clear 450 | 25D1 (4,330, 7,100)–(4,330, 7,950) and 25D2 (4,370, 7,850)–(4,370, 8,700): opening **1,600**, panels **850**, overlap 100, clear **750** (dwelling B 25D3 / 25D4 replace 18D / 18F) |

### VF-05 utility (Option A): move equipment away from the doorway

| Handle | Was | Now |
|---|---|---|
| 1E8 MVHR / cylinder allowance | [300, 6,700, 900, 7,300] | [2,200, 6,700, 2,800, 7,300] (mirror 1E9) |
| 1EA circle | c(600, 7,000) | c(2,500, 7,000) (mirror 1EB) |
| 1EC worktop | [900, 6,700, 2,800, 7,300] | [900, 6,700, 2,200, 7,300] (mirror 1ED) |
| 1AC sink | [2,200, 6,750, 2,700, 7,200] | [375, 6,725, 875, 7,175] (mirror 1AD) |
| 25D9 sink base (new, A-FURN) | — | [300, 6,700, 900, 7,200], 500 mm deep (mirror 25DA) |
| 2FE label | "MVHR / CYL at W end" | "MVHR / CYL at E end" |
| 2FF label (dwelling B) | "MVHR / CYL at E end" | "MVHR / CYL at W end" |

### VF-06 conservatory (Option B): revise the conservatory outline (PROVISIONAL)

| Handle | Was | Now |
|---|---|---|
| 222 | (4,500, 12,300) (7,000, 12,300) (7,000, 13,050) (6,250, 13,800) (5,250, 13,800) (4,500, 13,050); 3.1875 m² | (4,400, 12,300) (7,000, 12,300) (7,000, 13,500) (6,700, 13,800) (4,700, 13,800) (4,400, 13,500); **3.81 m²**. Mirror 223 |

Pull-side nib at the conservatory door: 200 → **300 mm**.

### VF-07 kitchen to utility (Option B): pocket sliding door

| Handle | Was | Now |
|---|---|---|
| 123 (Q4 west piece) | x 300–1,000 | x 300–**1,250** (pocket section; mirror 124: x 17,350–18,300) |
| 125 (Q4 east piece) | x 2,000–4,300 | x **2,100**–4,300 (mirror 126: x 14,300–16,500) |
| Hinged door removed | 180 / 182: leaf (1,000, 8,700)–(1,000, 7,700), arc c(1,000, 8,700) r 1,000, 270°→0° | — (mirror 181 / 183) |
| 25D5 pocket cavity (new) | — | [350, 8,725, 1,250, 8,775] (mirror 25D7) |
| 25D6 closed pocket leaf (new) | — | (1,200, 8,750)–(2,100, 8,750) (mirror 25D8) |

Opening 1,000 → **850 mm**; estimated clear opening about 810 mm. Kitchen-side latch-jamb nib **0 mm**, unresolved (Report §5.4).

## 4. Annotation

| Handle | Was | Now |
|---|---|---|
| 2DA title | "MMUCO ORION DUPLEX - DRAFT 0.2.1" | "MMUCO ORION DUPLEX - DRAFT 0.2.2" |
| 147E revision line | Draft 0.2.1 text | "Draft 0.2.2 (24 Oct 2026): B1 double-door entries to Bedrooms 1 and 2 (Face Me and I Face You); door items VF-04 to VF-07 as directed. Not approved - see Door Resolution Report." |
| 2FB scale note (step 1) | — | "PDF sheet scale: VERIFICATION PENDING …" until the 0.2.2 PDF measured 1:50.000 |
| 2FB scale note (final) | — | "PDF sheet: ISO A1 portrait at 1:50 - scale verified by measurement (see Draft 0.2.2 Door Resolution Report). …" |
| 2F8 notes block | Header "NOTES - DRAFT 0.2 (OPTION C2)"; note 6 conservatory "S-08 2.5 x 1.5 m" | Header "NOTES - DRAFT 0.2.2 (OPTION C2)". Note 2 adds the double doors, store opening and pocket door. Note 6 now reads "conservatory outline (S-08 basis; revised in Draft 0.2.2 to 2.6 x 1.5 m with 300 mm chamfers)" |
| 1466 dimension key | "conservatory 2.5 x 1.5" | "conservatory 2.6 x 1.5" |

## 5. Files

### New deliverables

| File | Note |
|---|---|
| `MMUCO_ORION_Duplex_Draft_0.2.2.dxf` | AutoCAD 2018 DXF, 533 entities |
| `MMUCO_ORION_Duplex_Draft_0.2.2.pdf` | ISO A1 portrait, page fitting off, measured 1:50.000 |
| `MMUCO_ORION_Duplex_Draft_0.2.2.png` | 7,500 × 10,619 px, rendered from the PDF; two renders identical |
| `MMUCO_ORION_Duplex_Draft_0.2.2_Room_Schedule.csv` | Recalculated from the 0.2.2 DXF. Rooms unchanged; partitions note updated; conservatory 3.81 |
| `MMUCO_ORION_Duplex_Draft_0.2.2_Door_Resolution_Report.md` | Test results and decisions |
| `MMUCO_ORION_Duplex_Draft_0.2.2_Change_Log.md` | This file |
| `MMUCO_ORION_Duplex_Draft_0.2.2_Hallway_Option_Comparison.pdf` / `.png` | B1 / B2 / B3 comparison sheet. ISO A2 landscape at 1:50; design study, not an issued plan |
| `MMUCO_ORION_Duplex_Draft_0.2.2_Manifest.sha256` | Hashes of all of the above, the evidence folder and the frozen files |
| `MMUCO_ORION_Duplex_Draft_0.2.2_Evidence/` | Sections 01–07, `preservation/`, `scripts/` |

### Scratch, not issued

`MMUCO_ORION_Duplex_Draft_0.2.2_SCRATCH_not_issued/` holds the working copy, option-study source, WIP and test drawings, and a README. It is **not** listed in the deliverable manifest.

## 6. Preservation record

| Check | Start (20:12:27) | End |
|---|---|---|
| `MMUCO_ORION_Duplex_Draft_0.2.1_Manifest.sha256` | 63 / 63 OK | See `Evidence/preservation/end_check.txt` |
| `MMUCO_ORION_Duplex_Draft_0.2_Verification_Manifest.sha256` | 40 / 40 OK | See `Evidence/preservation/end_check.txt` |
| Draft 0.1 original hashes | 3 / 3 OK | See `Evidence/preservation/end_check.txt` |
| Earlier audit and decision documents (5 files, in no manifest) | Hashed | See `Evidence/preservation/end_check.txt` |
| Working copy vs issued 0.2.1 DXF | Identical | See `Evidence/preservation/end_check.txt` |

No issued file (Draft 0.1, Draft 0.2, the Verification package, Draft 0.2.1 and its evidence, report, change log and manifest) was opened for writing, overwritten, moved or deleted.
