# MMUCO ORION Duplex — Draft 0.2.1 Correction Report

**Issue:** `MMUCO_ORION_Duplex_Draft_0.2.1`
**Basis:** the approved C2 baseline and the frozen Draft 0.2 files
**Scope:** controlled drafting correction of VF-01, VF-02 and VF-03 only. This is **not** a redesign.
**Date:** 24 October 2026

**Companion files:**

- `..._Draft_0.2.1.dxf`, `.pdf`, `.png`: drawing
- `..._Draft_0.2.1_Room_Schedule.csv`: room schedule
- `..._Draft_0.2.1_Change_Log.md`: change log
- `..._Draft_0.2.1_Manifest.sha256`: hashes
- `MMUCO_ORION_Duplex_Draft_0.2.1_Evidence/`: scripts, raw results, crops and test files

> **No approval or compliance claim.** Draft 0.2.1 is a concept floor plan. Nothing here claims planning, Building Regulations, accessibility (ADM M4(2)) or construction-readiness approval. The corrections concern how the drawing is plotted and dimensioned, not whether the design complies with anything.

**Evidence labels:**

| Label | Meaning |
|---|---|
| **MEASURED** | Read directly from the saved 0.2.1 files by scripts that do not use the drawing generator or the C2 coordinate model |
| **AUTOMATED CHECK** | Scripted pass/fail test, with its result |
| **ASSUMPTION** | Carried over from Draft 0.2 unchanged |
| **PROFESSIONAL REVIEW** | Outside a drafting check |
| **UNVERIFIED / INCONCLUSIVE** | Could not be established here |

---

## 0. Release decision

| Correction | Result | Evidence |
|---|---|---|
| **VF-01** true 1:50 plotting | **Resolved and verified** | PDF vectors: building width 372.000 mm, depth 246.000 mm and scale bar 100.000 mm on the sheet, so 1:50.000 on three independent lengths. PNG (rendered from that PDF): 1:49.90–1:49.94, within 0.2 %, explained by anti-aliased edges (§2) |
| **VF-02** east dimension chain | **Resolved and verified** | Break points equal the actual east-side wall faces. Every segment equals its coordinate difference. Total 12,300 = overall (§3) |
| **VF-03** dimension associations | **Resolved, with one documented static point** | 65 of 66 definition points are associated to wall polylines. None reference provisional, external-works or furniture geometry. Moving all 262 non-wall entities changed 0 of 33 dimensions; moving two partitions updated exactly the 6 dimensions anchored to them (§4) |

**Design preservation:** verified.

- 485 of the 508 Draft 0.2 entities are byte-for-byte identical in geometry.
- No wall, opening, fitting, furniture, provisional or external-works entity changed.
- Rooms, areas and the accessibility geometry are identical to Draft 0.2 (§5).

**Release:** all three required corrections pass their verification. **Draft 0.2.1 is released as a drafting correction.** The open items in §7 still apply, VF-04 to VF-07 included. They were deliberately **not** resolved here.

---

## 1. Preservation of existing files

| Check | When | Result |
|---|---|---|
| Verification manifest (`..._Verification_Manifest.sha256`): 40 entries covering the six issued Draft 0.2 files, Draft 0.1 and the Verification package | Start, 19:07:50 +01:00 | **40 / 40 OK** |
| Draft 0.1 hashes recorded before any Draft 0.2 work (`draft01.sha256`) | Start | **3 / 3 OK** |
| Same two checks | End (see Manifest) | Recorded in `..._Draft_0.2.1_Manifest.sha256` and the Change Log |

All new work went to new filenames. The frozen Draft 0.2 DXF was only **opened**: once as a scratch copy for experiments, once as the production copy that was saved as 0.2.1, and once for a scratch movement test saved to the evidence folder. It was never saved back.

---

## 2. VF-01: true 1:50 plotting

**Configuration:** CADCraft `exportpdf` with `fit: false`, `scale: "1:50"`, paper ISO A1 (594 × 841 mm), portrait, centred, plot area = extents. The Draft 0.2 export omitted `fit: false`, so CADCraft fitted the drawing to the page.

**Measurement method (AUTOMATED CHECK, `ver_pdfmeasure.mjs`).** The script reads the PDF content stream and measures three known drawing lengths, plus the legend swatch as a fourth:

1. **Building width:** extent of the 26 black-filled external-wall pieces (18,600 mm in the DXF).
2. **Building depth:** the same pieces (12,300 mm).
3. **Printed scale bar:** five red 1,000 × 200 mm rectangles (5,000 mm).
4. **Legend swatch:** 500 × 300 mm.

Sheet mm = pt × 25.4 / 72. Acceptance: within ±0.5 % of 1:50.

**The method was validated on two controls before use:**

| PDF | Width | Depth | Scale bar | Swatch | Result |
|---|---|---|---|---|---|
| Control: issued Draft 0.2 (known defect) | 1:48.229 | 1:48.229 | 1:48.229 | 1:48.23 | FAIL, as expected |
| Control: scratch `fit: false` test | 1:50.000 | 1:50.000 | 1:50.000 | 1:50.001 | PASS, as expected |

**Sequence for 0.2.1:**

| Step | Time | Sheet note at that moment | Result |
|---|---|---|---|
| 1. Export with the note set to "PDF sheet scale: VERIFICATION PENDING – use the scale bar…" | 19:15:56 | Pending | Width 1,054.488 pt = **372.000 mm** → 1:50.000. Depth 697.323 pt = **246.000 mm** → 1:50.000. Scale bar 283.464 pt = **100.000 mm** → 1:50.000 (segments 56.692–56.693 pt). Swatch 1:50.001. All content inside the clip box; margins ≥ 16.6 mm. **PASS** |
| 2. Note changed (only after step 1 passed) | — | "PDF sheet: ISO A1 portrait at 1:50 – scale verified by measurement (see Draft 0.2.1 Correction Report)…" | — |
| 3. Deliverable DXF saved; deliverable PDF exported | 19:16:14 | Verified note | Same four measurements, identical to step 1: **PASS** |
| 4. PNG rendered from the deliverable PDF (Windows PDF renderer, 7,500 px wide), twice | 19:16:30 | — | Both renders byte-identical (SHA-256 `6f22c54a…0897`); the deliverable PNG is that render |

**PNG measurement (MEASURED, `ver_png.mjs`, own PNG decoder):**

| Feature | PNG | Expected at 1:50 (12.626 px per sheet mm) | Implied |
|---|---|---|---|
| Building width (black wall faces) | 4,703 px | 4,697.0 px | 1:49.94 |
| Building depth | 3,112 px | 3,106.1 px | 1:49.90 |
| Scale bar (outer edge of the red outline) | 1,265 px | 1,262.6 px | 1:49.9 (5,009 mm) |
| Party-wall red band | 3,540–3,596 px, centre 3,568 | 3,568.5 predicted from DXF | 0.5 px off |

**Interpretation:** the PNG is about 0.15 % long because the pixel-run method counts anti-aliased edge pixels and stroke width. The same bias appeared on the issued 0.2 PNG (1:48.16 against the PDF's 1:48.23). The PDF's vector measurement is exact and authoritative. The PNG is consistent with 1:50 within the ±0.5 % acceptance band.

**Same drawing in both formats:**

- The PNG is a deterministic raster of the deliverable PDF (identical hash on re-render).
- DXF coordinates predict PNG pixel positions to within 0.5–6 px (≤ 0.12 % of the building width).
- The visual review (§6) found identical content.

---

## 3. VF-02: east dimension chain

**Actual east-side geometry (MEASURED from the saved DXF).** Partitions meeting the inner face of the east wall (x = 18,300):

| Handle | y range |
|---|---|
| 11E | 4,000–4,100 |
| 120 | 6,600–6,700 |
| 124 | 8,700–8,800 |

The external wall inner faces are at y = 300 (front, piece 10B) and y = 12,000 (rear, piece 113); the outer faces are at y = 0 and 12,300 (pieces 101 and 109). So the expected break points are 0, 300, 4,000, 4,100, 6,600, 6,700, 8,700, 8,800, 12,000, 12,300.

**Intended chain:** the mirror of the west chain, which was already correct in Draft 0.2: 300 / 3,700 / 100 / 2,500 / 100 / 2,000 / 100 / 3,200 / 300.

**Correction:** the 7 erased dimensions were replaced by 9 new ones (full endpoint and value table in the Change Log).

| Draft 0.2 (erased) | Draft 0.2.1 (new) |
|---|---|
| 300 / **4,000** / **100** / 2,500 / **100** / **5,000** / 300, break points at y 300, **4,300, 4,400, 6,900, 7,000**, 12,000. These are the partitions beside the *party wall* (handles 138, 13C), not the east wall | 300 / 3,700 / 100 / 2,500 / 100 / 2,000 / 100 / 3,200 / 300, break points at y 300, 4,000, 4,100, 6,600, 6,700, 8,700, 8,800, 12,000 |

**Checks (AUTOMATED CHECK, `ver_dims.mjs`):**

- Break points equal the wall faces: **PASS**.
- Each segment value equals the coordinate difference of its two anchor vertices: **PASS** (9 / 9).
- Chain is contiguous: **PASS**.
- Sum 12,300 = overall dimension 2D9 (12,300): **PASS**.

As the correction order required, the chain was **not** passed merely because its values add up; the break points were compared with the geometry.

---

## 4. VF-03: dimension associations

### 4.1 Inspection of all 31 Draft 0.2 dimensions (MEASURED from DXF xdata `CADCRAFT / ASSOC`)

| Status of the 62 definition points | Count |
|---|---|
| Associated to a wall polyline vertex | 25 |
| Static (no association) | 29 |
| Associated to **provisional** patio polygons 224 / 225 (A-PROV) | 6 |
| Associated to path/slab line 234 (A-EXT) | 2 |
| Dimensions associated to walls at both ends | 9 of 31 |

**Demonstration of the defect:** on a scratch copy of Draft 0.2, the 32 provisional and external-works entities were moved by (+2,000, +3,000). **6 wall dimensions changed** (2CF 100 → 3,100; 2D1 300 → 2,700; 2D6 100 → 3,100; 2D8 300 → 2,700; 2D0 and 2D7 relocated). Test file: `Evidence/test_files/test_02_moved_prov.dxf`.

### 4.2 How CADCraft associates (established by scratch experiments)

- Association is made to an entity **vertex or line end** at the definition point. A point on a wall face that is not a vertex gets **no** association.
- Where several entities share a vertex, CADCraft picked the **non-wall** entity:
  - At (300, 6,700) it chose the MVHR/cylinder furniture 1E8 over partition 11F.
  - Freezing the furniture layer did not change that choice.
- Moving an associated wall **does** update its dimensions (live associativity).
- Single-object dimensioning measures the polyline's first segment only, so it was not usable for wall thicknesses.

### 4.3 Method used

1. **Anchor on wall vertices.** Each chain point was moved from the outer face (no vertex there) to the nearest wall vertex on the same line. For west, east and south chains these are the partition corners on the inner face; the outer corners keep the outer face. Values are unchanged because each dimension measures only along its axis.
2. **Resolve shared vertices.** Exactly four anchor points shared a vertex with non-wall geometry: (300, 6,700) with 1E8, (300, 12,000) with 1DC, (18,300, 6,700) with 1E9, (18,300, 12,000) with 1DD (`Evidence/results/anchor_conflicts.txt`). Those four furniture entities were moved by exactly (0, +100,000) mm, the dimensions created, and the entities moved back by exactly (0, −100,000) mm. The entity diff (§5) proves they are **identical** to Draft 0.2.
3. **One static point.** The south chain's last point is the party-wall **centreline** (9,300, 0), where no geometry vertex exists. Dimension 2C7 (9,200 → 9,300 = 100) therefore remains **static at that end**. This is documented, not hidden.

### 4.4 Result (AUTOMATED CHECK on the saved 0.2.1 DXF)

| Status of the 66 definition points (33 dimensions) | Count |
|---|---|
| Associated to a wall polyline vertex that exactly matches the definition point | **65** |
| Static | **1** (2C7 p14, party-wall centreline) |
| Associated to provisional, external-works, furniture or any other non-wall geometry | **0** |
| Dimensions associated at both ends | **32 of 33** |
| Text overrides | 0 |

### 4.5 Movement tests on the saved 0.2.1 DXF, reopened

| Test | Entities moved | Dimensions changed | Result |
|---|---|---|---|
| Negative: provisional and unrelated geometry | All 262 entities on A-PROV, A-EXT, A-FURN, A-SANI, A-GLAZ, A-DOOR, A-ROOF, A-ACCS moved (+2,000, +3,000) | **0 of 33** | **PASS** |
| Positive control: associativity is live | Partitions 11D and 11E moved +100 mm in y | Exactly 146D, 146E, 146F, 1476, 1477, 1478 (3,700 → 3,800; 100 → 100; 2,500 → 2,400) | **PASS** (correct dimensions, correct new values) |

Test DXFs are in `Evidence/test_files/`. They are scratch states, **not** deliverables.

### 4.6 Limitation (UNVERIFIED)

The associations are stored as CADCraft application xdata (`1001 CADCRAFT`, `ASSOC`). Other CAD applications, AutoCAD included, are **not expected** to interpret them, and would most likely treat all 33 dimensions as **static**. This has not been tested. Within CADCraft, associativity is verified as above. **The drawing does not claim that the dimensions are associative in other software.**

---

## 5. Design preservation (AUTOMATED CHECK)

**Entity diff, Draft 0.2 → 0.2.1** (`ver_diff.mjs`; compares type, layer and every coordinate, size, angle and text group by handle):

| Category | Count | Detail |
|---|---|---|
| Unchanged | **485 of 508** | All walls, hatches, openings, glazing, doors, fittings, furniture (including the four temporarily moved items), roof, accessibility, provisional and external-works entities, the room labels, the notes, room schedule and dimension key blocks, and the 10 kept dimensions |
| Removed | 21 | Dimensions only (VF-02 / VF-03) |
| Added | 24 | 23 dimensions and 1 revision text |
| Edited | 2 | Title (2DA: "… DRAFT 0.2" → "… DRAFT 0.2.1") and scale note (2FB) |
| Non-annotation entities changed | **0** | — |

**Blind parser re-run on the 0.2.1 DXF** (same independent script as the Verification gate):

- 59 wall pieces, no overlaps, 0 free ends;
- 36 openings (14 windows, 18 swing doors, 2 sliding, 2 open);
- 18 rectangular rooms, all labels matching;
- footprint 228.78 m²;
- 104.13 m² per dwelling;
- reconciliation residual **0 mm²**.

**Area reconciliation:** all 41 rows agree with the 0.2.1 Room Schedule (`Evidence/results/area_reconciliation_021.csv`).

**Room Schedule:** `..._Draft_0.2.1_Room_Schedule.csv` is byte-identical to the issued Draft 0.2 schedule (SHA-256 `c5aa59b5…503b`), because no room or area changed. It is generated from the C2 coordinate model (MODEL RESULT) and verified against the 0.2.1 DXF by the blind parser (MEASURED).

**Accessibility geometry** (`ver_access.mjs`: door openings and nibs, swings, store sliding door, beds and zones, bathroom zones, kitchen clearances, 750 mm routes, mirror symmetry) is **identical** to the Draft 0.2 result. VF-04 to VF-07 are therefore unchanged and remain open.

---

## 6. Visual inspection of the corrected A1 PDF and full-resolution PNG

Native-resolution crops are in `Evidence/crops/` and on the summary sheet `evidence_sheet_021.png`.

| Item | Observation | Status |
|---|---|---|
| Scale | Measured 1:50 (§2); the scale bar reads 0–5 m over 100 mm | PASS |
| Title, scale note, revision line | "DRAFT 0.2.1"; verified-scale note; revision statement placed between the scale note and the 18,600 dimension text with no collision | PASS |
| East chain | Reads 300 / 3,700 / 100 / 2,500 / 100 / 2,000 / 100 / 3,200 / 300. Extension lines start at the partition corners on the inner face and cross the 300 mm wall (red over black, visible) | PASS |
| West and south chains | Same values as Draft 0.2. Extension lines now start at the inner-face partition and wall corners | PASS |
| 100 mm segment labels | Legible. Still crossed by their own extension lines | **Open (VF-08, not in scope)** |
| Other label crossings | Porch labels and the party-wall label crossed by extension lines (as in 0.2). The east patio label is now crossed by the east-chain extension lines, as the west one was in 0.2. Text-box test: 20 crossing findings against 19 in 0.2 (+1 for the extra 100 mm east segment); no label overlaps another label or a wall | **Open (VF-08)** |
| Provisional linework | Conservatories: 82–83 % of outline length inked (0.2: 82 %). Patio B improved to 63 % (0.2: 33 %), because the old east-chain lines no longer cover its bottom edge. Patio A measured 64 % (0.2: 77 %) on the colour threshold. In the crops both patio outlines are visibly dashed; the drop is lighter anti-aliasing at the new pixel alignment | Pass by visual inspection; metric **INCONCLUSIVE** for patio A |
| Colour contrast on white | Unchanged layer colours: cyan doors and fittings 1.25 : 1, accessibility zones about 1.2 : 1 | **Open (VF-09, not in scope)** |
| Smallest text | 80 mm = 1.6 mm at a true 1:50 (on the 0.2 sheet it was 1.66 mm) | **Open (VF-11, not in scope)** |

---

## 7. Items deliberately not resolved (retained as open)

| ID | Item | Status after 0.2.1 |
|---|---|---|
| VF-04 | Store bypass sliding door about 450 mm clear | **Open**; geometry unchanged |
| VF-05 | Utility side door obstructed 100 mm by the MVHR/cylinder allowance | **Open**; unchanged |
| VF-06 | Conservatory door pull-side nib 200 mm if the provisional conservatory is built as drawn | **Open**; unchanged |
| VF-07 | Kitchen–utility push-side nib 100 mm | **Open**; unchanged |
| VF-08 to VF-11 | Label crossings; low-contrast colours; smallest text; patio visibility | **Open** (patio B improved as a side effect) |
| VF-12 | PDF text drawn as vector strokes | **Open** (unchanged by design) |
| VF-13 | "Partitions 4.03 m²" includes 0.88 m² of opening zones | **Open**; schedule wording unchanged |
| VF-14 / VF-15 | Front-door leaf drafting; south chain covers dwelling A only | **Open** |
| VF-16 | Third-party CAD compatibility, now including associativity (§4.6) | **UNVERIFIED** |
| — | Notes block header still reads "NOTES – DRAFT 0.2 (OPTION C2)". The block was kept byte-identical; the title and revision line identify the issue as 0.2.1 | Minor; noted |
| PA / SI / RQ / DR | All provisional assumptions, missing site information, regulatory questions and design risks in the Verification Register | **Unchanged and open** |

---

## 8. Summary by evidence class

| Statement | Class |
|---|---|
| PDF at 1:50.000 (width, depth, scale bar); PNG consistent within 0.2 % | MEASURED |
| East chain matches the east-side wall faces; segment values equal coordinate differences; total 12,300 | MEASURED / AUTOMATED CHECK |
| 65 of 66 definition points associated to wall vertices; 0 to provisional geometry; 1 static point | MEASURED |
| Moving 262 non-wall entities changes no dimension; moving partitions updates the right 6 | AUTOMATED CHECK |
| Walls, openings, rooms, areas and accessibility geometry identical to Draft 0.2 | AUTOMATED CHECK |
| Room schedule values | MODEL RESULT, verified against the DXF |
| Wall build-ups, conservatory, porches, patios, paths, orientation, door products | ASSUMPTION / PROVISIONAL (unchanged) |
| Associativity in software other than CADCraft; patio A line visibility by metric | UNVERIFIED / INCONCLUSIVE |
| Planning, Building Regulations, accessibility compliance, construction readiness | PROFESSIONAL REVIEW; **not claimed** |
