# MMUCO ORION proposed Draft 0.2.3: validation report

**SCRATCH REVIEW COPY: NOT ISSUED, NOT APPROVED, NOT A COMPLIANCE ASSESSMENT.**

- Every check below ran on the **saved** proposed DXF and its exported PDF/PNG, not on a script's intended output.
- Results are as measured. A check that could not be done is marked BLOCKED or NOT TESTED, not PASS.

| Status | Meaning |
|---|---|
| PASS | The measured result meets the stated test |
| FAIL | The measured result does not meet the test |
| BLOCKED | The test cannot be done until the stated item exists |
| NOT TESTED | No test was run; the reason is stated |

---

## 1. Decision

**Option A is implemented in the scratch copy, in both dwellings, and its geometry is verified.**

**Issue status: Draft 0.2.3 must not be issued yet.** Two stop conditions in the brief apply:

| Stop condition | Status | Detail |
|---|---|---|
| "The nib or clear opening cannot be measured reliably" | **Applies** | The clear opening cannot be measured: no pocket-door system is selected (V-07, OQ-06). The 300 mm nib is measured reliably at the drawn reference, but its finished-face value depends on supplier details not yet available (V-04b, OQ-05) |
| "A critical compliance question is presented as resolved without evidence" | **Avoided** | The planning condition, the sliding-door leading-edge rule and the unit-as-nib-edge question are all open (section 5) and are not presented as resolved |
| Frozen file changed, manifest failure, B change incomplete, geometric failure, unassessed collision / service conflict / dimension inconsistency | **None found** | See V-01 to V-21 |

---

## 2. Preservation and source control

| Check | Result | Status |
|---|---|---|
| Frozen manifests at start (21:20:53) | Draft 0.2.2 80/80, Draft 0.2.1 63/63, Verification 40/40, earlier documents 5/5, VF-07 investigation 49/49, Draft 0.1 3/3 → **240/240 OK**. Manifest files' own hashes as recorded (0.2.2 d9062c5a…, 0.2.1 3fb2898a…, Verification 1d48e6e3…, VF-07 1508eb2b…) | PASS |
| Source copies | `source_copies/MMUCO_ORION_Duplex_Draft_0.2.2.dxf` and `..._Room_Schedule.csv`: SHA-256 equal to the issued files and to the 0.2.2 manifest; `cmp` byte-identical | PASS |
| Working copy | `WORKING_COPY_from_Draft_0.2.2.dxf` byte-identical at the start, and still identical at the end (never saved over) | PASS |
| Frozen manifests at end (21:42:04) | **240/240 OK**; manifest-file hashes unchanged | PASS |
| No issued or approved 0.2.3 file | 0 files named `*0.2.3*` outside the scratch folder; every 0.2.3 file name carries `PROPOSED` / `SCRATCH` / `NOT_ISSUED` | PASS |

**Evidence:** `evidence/00_preservation/` (preservation_start.txt, source_copies.txt, preservation_end.txt).

---

## 3. Geometry and regression checks

Scripts are in `evidence/scripts/`. Outputs are in `evidence/01_measurements/` and `evidence/02_regression/`.

| ID | Check | Method | Dwelling A | Dwelling B | Status |
|---|---|---|---|---|---|
| V-01 | Option A implemented (base run shortened 300 mm at the latch end) | Entity diff; d023_checks | 1E0 [2,100→2,400, 8,800, 4,300, 9,400], 2,200 → 1,900 | 1E1 [14,300, 8,800, 16,500→16,200, 9,400], 2,200 → 1,900 | PASS |
| V-02 | Implemented A equals the reviewed VF-07 Option A | VF-07 measure.mjs on the proposed DXF vs the Option A basis | All 13 compared values identical | n/a (B was not in the study) | PASS |
| V-03 | Kitchen-side latch nib ≥ 300 mm target, at the drawn reference | Scan along the kitchen face from the latch jamb to the first wall or fixed unit within 600 mm | **300** (unit 1E0), zone 2,600 deep | **300** (unit 1E1), zone 2,600 deep | PASS (0 mm margin) |
| V-04b | Kitchen-side nib to the **finished** face as built | Requires the end panel / worktop / lining details | Drawn outline defined as the finished face (note 2); sensitivity: 18 mm outside → 282 | Same | **BLOCKED** (kitchen supplier and jamb detail; OQ-05, OQ-11) |
| V-05 | Utility-side latch nib unchanged | As V-03 | 700 (wall 121), zone 1,400 | 700 (wall 122), zone 1,400 | PASS |
| V-06 | Structural opening unchanged | Gap between Q4 wall pieces | 1,250–2,100 = 850 | 16,500–17,350 = 850 | PASS |
| V-07 | Clear opening, finished | Needs the selected door system | ESTIMATE 810 (770–810) | ESTIMATE 810 (770–810) | **BLOCKED** (no system selected; OQ-06) |
| V-08 | Door panel and pocket cavity geometry | Cavity in one wall piece; holds the leaf; overlap; fixings; junctions | 25D5 900 in piece 123, leaf 25D6 900, overlap 50, no fixings | 25D7 900 in piece 124, leaf 25D8 900, overlap 50, no fixings | PASS |
| V-09 | Door movement and unit collisions | Sliding leaf closed/open vs walls and units; door-arc sectors (10 mm grid); units vs walls; units vs units | No hits (closed 1,200–2,100; open 350–1,250 inside the cavity); side door 186 swing clear | No hits (closed 16,500–17,400; open 17,350–18,250); side door 187 swing clear | PASS |
| V-10 | Kitchen and utility approach spaces | Perpendicular ray casts across the opening | 2,600 / 1,400 (unchanged); kitchen 1,200 band now 1,500 wide | 2,600 / 1,400 (unchanged); band 1,500 wide | PASS |
| V-11 | Base-run length and remaining units (geometry) | Outline and divider lines | 1,900; 300/600/600/400 from the latch end | 1,900; 300/600/600/400 | PASS (geometry) |
| V-11b | Usability of the 300 mm unit and appliance allocation | — | — | — | **NOT TESTED** (no unit or appliance schedule; OQ-09) |
| V-12 | Sink, hob, washer, dryer, MVHR/cylinder locations | Coordinates in 0.2.2 vs 0.2.3 | 19E, 1A2, 1AC, 1AE, 1B2, 1E8 unchanged | 19F, 1A3, 1AD, 1AF, 1B3, 1E9 unchanged | PASS |
| V-13 | Wall and partition continuity, overlaps, gaps | Entity diff (no wall entity changed); independent parser: wall junctions, openings and reconciliation sections identical to 0.2.2 | No change | No change | PASS |
| V-14 | Dimensions associated with modified geometry | ver_dims (47 dims: no overrides, stored = geometry for all); the 45 existing dims unchanged; 2 new dims anchored to wall + unit | 47EF = 300 (125 v3 / 1E0 v0) | 47F0 = 300 (1E1 v1 / 126 v2) | PASS |
| V-15 | Room areas, GIA, schedule reconciliation | Independent parser; schedule regenerated from the proposed DXF; reconciliation against the issued 0.2.2 schedule | Kitchen 12.80, utility 5.00, GIA 104.13, residual 0 mm² | Same | PASS: of 41 reconciliation items, the 32 with an issued value all agree (9 have no issued value to compare); schedule numbers identical (only the basis/status text changed) |
| V-16 | A/B symmetry and mirrored entities | Reflection match of every geometry entity; 15 parity measures; dimension mirror | 161 entities, each matched | 161 matched + 7 legend swatches (single by design) | PASS. New dims mirror exactly; dwelling A's front dimension chain (7 dims) is single, as in 0.2.2 |
| V-17 | Drawing scale (proposed PDF, A1 portrait, 1:50) | Vector measurement of the PDF: building 18,600 × 12,300 mm, scale bar, swatch | Building 372.000 × 246.000 mm → **1:50.000**; bar 1:50; swatch 1:50.001; inside the clip; L/R margins 16.6 mm (as 0.2.2); content 7 mm lower than 0.2.2 (two more note lines) | — | PASS |
| V-18 | Raster consistency (proposed PNG) | Two renders from the PDF (DestinationWidth 5,000, as 0.2.2) plus the deliverable; ver_png calibration | 7,500 × 10,619 px; renders identical (0E01D55C…46C4); raster scale reading 1:49.94, identical to the 0.2.2 reading by the same method; 89 px vertical shift = the 7 mm move | — | PASS |
| V-19 | Text legibility and clashes | ver_text (estimated text boxes vs linework and other text); visual crops | 133 texts; 26 clash findings, **identical to 0.2.2** (all pre-existing, none involving the new or edited text); new dimension text 175 mm = 3.5 mm on paper; minimum text 80 mm = 1.6 mm (pre-existing, VF-08) | — | PASS (no new clashes); pre-existing legibility items carried |
| V-20 | Downstream schedules, annotations, reference geometry | Notes, title and revision text updated; on-sheet room schedule (2F9) unchanged and still correct; door-check script: only the VF-07 nib changed; access script: only 1E0's extent changed | — | — | PASS |
| V-21 | Comparison drawing (A1 landscape) | Vector check: frame 800 × 550 mm, Q3 wall 2 × 40 mm (4 plans), 5 × 70 mm (4 details) | Plans 1:50, details 1:20; nothing clipped; two renders identical (F0C4F794…506B) | — | PASS |

---

## 4. Positive and negative controls (disposable copies)

Copies are in `TEST_positive_controls/`, built from the proposed DXF and never used as deliverables. Results are in `evidence/03_positive_controls/`.

| ID | Fault introduced | Expected | Result | Status |
|---|---|---|---|---|
| PC1 | Both base runs set 50 mm too close (1E0 at x 2,350; 1E1 at x 16,250) | Nib check fails in both; associated dimensions follow | Nib 250 / 250, `meetsTarget` false / false; 47EF and 47F0 300 → 250, the other 45 dims unchanged | PASS (detected) |
| PC2 | Both base runs pushed 50 mm into Q4 (south edge at y 8,750) | Collision sweep flags both | 1E0 × wall 125 = 0.0950 m²; 1E1 × wall 126 = 0.0950 m² | PASS (detected). The first run crashed; the base-run lookup was hardened and **all** 0.2.2 / 0.2.3 results were re-run, byte-identical to before |
| PC3 | Dwelling A shortened, B not (the VF-07 Option A file) | Symmetry and parity fail | Symmetric false: 1E0 / 1E1 unmatched; parity fails on nib, zone, run length, units, 2.24b | PASS (detected) |
| PC4 | Unrelated units moved (hob 1A2 group, sink 19F +100 mm) | No dimension changes | 47 / 47 dimensions unchanged | PASS (no false change) |
| VF-07 PC | Leaf radius 1,600 on a C1 copy (from the investigation) | Swing collision | Wall 121 and unit 1EC flagged | PASS (carried) |

---

## 5. Regulatory and compliance status (nothing here is a compliance claim)

| Item | Status | Owner |
|---|---|---|
| Governing category: M4(1) by default; M4(2) only if a planning condition imposes it (ADM Vol 1 para 0.3) | **OPEN**: no planning decision found (OQ-01) | Planning authority; architect/designer to obtain |
| M4(1) 1.15a applicability to a kitchen-utility door | OPEN (OQ-02). M4(1) has no nib provision; that does not settle usability | Building control |
| M4(2) 2.22d "leading edge" for a sliding door | OPEN (OQ-03). Not interpreted here | Building control |
| Fixed units as the nib edge | OPEN (OQ-04) | Building control / access consultant |
| Clear opening against Table 1.1 / 2.1 | BLOCKED (OQ-07) | Building control, after OQ-06 |
| Project design target R-14 (850 mm clear) | Not met by the ESTIMATE (OQ-08, NF-01). A target, not a regulation | Client / architect/designer |

**The 300 mm nib is a measured geometric result. It is not proof of compliance.** External guidance was not consulted for this task. ADM wording was read from the project's copy of ADM Vol 1 (2015 edition; currency OQ-13).

---

## 6. Not tested, and why

- **Door operation forces, hardware and soft-close behaviour:** no product selected.
- **Usability of the 300 mm base unit:** no unit or appliance schedule.
- **Services routes:** not designed; only fixed positions were checked.
- **Heights, levels, thresholds, sockets and switches:** not in the plan.
- **Dwelling B finished-face condition:** the same as A by definition in note 2, but not physically verifiable without supplier details.
