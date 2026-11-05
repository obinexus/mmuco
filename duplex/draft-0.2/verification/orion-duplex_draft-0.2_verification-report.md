# MMUCO ORION Duplex — Draft 0.2 Independent Verification Gate

**Project:** OBINexus Design · MMUCO ORION Duplex
**Subject:** the six issued Draft 0.2 (C2) deliverables, treated as a frozen concept-design baseline
**Date:** 24 October 2026. Baseline frozen at 18:41:37 +01:00; final integrity check in the Manifest.
**Companion files** (all new; nothing issued was modified):

- `MMUCO_ORION_Duplex_Draft_0.2_Verification_Manifest.csv` and `MMUCO_ORION_Duplex_Draft_0.2_Verification_Manifest.sha256`: SHA-256 manifest.
- `MMUCO_ORION_Duplex_Draft_0.2_Verification_Area_Reconciliation.csv`: area reconciliation.
- `MMUCO_ORION_Duplex_Draft_0.2_Verification_Register.csv`: register of findings, assumptions, site gaps, regulatory questions and risks.
- `MMUCO_ORION_Duplex_Draft_0.2_Verification_Visual_Evidence.png`: crops of the issued PNG.
- `MMUCO_ORION_Duplex_Draft_0.2_Verification_Evidence/`: scripts, raw results and crops.
- `MMUCO_ORION_Duplex_Draft_0.2_Verification_Change_Log.md`.

> **No compliance claim.** This gate checks what the files contain and whether they agree with each other and with the geometry they describe. It does not establish compliance with the Building Regulations 2010, Approved Document M (ADM), the NDSS or planning policy, and nothing here should be read as doing so. Where an ADM provision is quoted, the result is a **geometric reading** of the plan against that provision's dimensions. Whether the provision applies, how it is interpreted and whether it is met in the built work are matters for building control and qualified professionals. Jurisdiction is assumed to be England.

---

## 0. Gate result

| Area | Result |
|---|---|
| Concept geometry (walls, openings, rooms, areas, mirror symmetry) | **Verified independently.** All 18 rooms, GIA, partitions, walls and the footprint agree with the issued documents. Residual 0.00 m² (§3) |
| Issued sheet (A1 PDF and PNG) | **Not fit for scaled measurement.** It is plotted at about **1:48.23**, but the sheet and the issued documents say 1:50 (VF-01). The scale bar is correct |
| Dimensions | Values are correct and every chain sums. However, the **east chain describes the wrong features** (VF-02), and six wall dimensions are tied to provisional patio geometry (VF-03) |
| Accessibility geometry (M4(2) target) | Most geometric tests are met. **Four items need a design decision or professional interpretation:** store sliding door about 450 mm clear (VF-04); utility side door partly obstructed (VF-05); conservatory door nib if the provisional conservatory is built (VF-06); kitchen–utility push-side nib (VF-07) |
| Legibility | Readable on screen at full resolution. For paper: smallest text is 1.6 mm, several colours have low contrast on white, and some labels are crossed by other linework (VF-08 to VF-11) |
| Integrity | All six issued deliverables and Draft 0.1 were unchanged throughout the gate (Manifest) |

**Recommendation:** treat the issued DXF as the reliable record. Do not scale from the issued PDF or PNG with a 1:50 rule. Fix VF-01 to VF-03 (drafting only) in a new revision, with new filenames, after your approval. VF-04 to VF-07 are design or interpretation decisions for you and the professional team.

---

## 1. Evidence classes and independence

Every statement in this package carries one of these labels (requirement 7).

| Label | Meaning |
|---|---|
| **VERIFIED – independent** | Measured directly from the issued files by code that does not use the drawing generator (`gen_draft02.mjs`), the C2 coordinate model (`options.mjs`) or the issue-stage checks |
| **VERIFIED – official text** | Read from Approved Document text extracted from, or pages rendered from, the official PDF |
| **MODEL RESULT** | Output of the C2 coordinate model, the generator or an issue-stage script, or a calculation based on assumptions (MVHR energy, daylight factor). Not measured from the issued files |
| **ESTIMATE** | A value that depends on approximations (for example text extents, which rely on assumed glyph widths) |
| **ASSUMPTION / PROVISIONAL** | Introduced without project evidence |
| **INTERPRETATION** | The geometry is known, but whether and how a provision applies needs a professional or building-control judgement |
| **UNVERIFIED** | Could not be checked independently in this gate |
| **PROFESSIONAL APPROVAL REQUIRED** | Compliance or approval matters outside the scope of a drawing check |

### 1.1 Which checks are independent of the drawing-generation script

| # | Check | Inputs | Implementation | Independence |
|---|---|---|---|---|
| I-1 | Blind DXF measurement (`blind_measure.mjs`): inventory, walls, junctions, openings, rooms, areas, dimensions, polygons, hatches | Issued DXF only | Written by a separate agent with a clean context. It was told not to read the generator, the model, the issue-stage scripts or the issued documents, and did not | **Independent of the generator and of the issue-stage code.** Same underlying AI model, so the implementation is independent but the reviewer is not |
| I-2 | Doors, nibs, beds, bathroom zones, kitchen clearances, 750 mm routes, mirror symmetry (`ver_access.mjs`) | Issued DXF; room boxes from I-1 | Written for this gate; imports nothing from the generator or model | Independent of the generator |
| I-3 | Text placement (`ver_text.mjs`) | Issued DXF, including dimension blocks | Written for this gate | Independent of the generator; text extents are ESTIMATES |
| I-4 | PDF scale (`ver_pdfscale.mjs`), PNG scale, colours and line visibility (`ver_png.mjs`), PNG reproducibility | Issued PDF, PNG and DXF | Own PNG decoder and PDF stream reader | Independent |
| I-5 | Visual review of 9 native-resolution crops | Issued PNG | Human-style inspection by the reviewer | Independent of the generator; subjective |
| M-1 | Issue-stage `verify_dxf.mjs` (DXF against the C2 model) | DXF and `options.mjs` | Issue stage | **Model-dependent**: it confirms the DXF matches the model, not that the model is right |
| M-2 | Issue-stage `final_tests.mjs` (furniture, zones, swings, nibs) | `options.mjs` | Issue stage | **Model-dependent.** Superseded here by I-2, which repeats the tests on the DXF |
| M-3 | Issued room schedule (`schedule_csv.mjs`) | `options.mjs` | Issue stage | **Model-dependent.** Re-checked here by I-1 (all 41 values agree) |
| U-1 | Opening the DXF in third-party CAD (AutoCAD, BricsCAD and similar) | — | **Not performed** | **UNVERIFIED** (VF-16) |

---

## 2. Independent review of the DXF (requirement 2)

### 2.1 File and inventory: VERIFIED – independent (I-1)

- **Format:** AC1032 (AutoCAD 2018 DXF); `$INSUNITS` = 4 (mm); model space only. 508 entities: 186 LWPOLYLINE, 100 LINE, 82 TEXT, 62 HATCH, 31 DIMENSION, 22 CIRCLE, 18 ARC, 4 ELLIPSE, 3 MTEXT.
- **Layer table:** 15 layers: 0, Defpoints and 13 named A- layers. **Nothing is on layer 0 or Defpoints**, and nothing is on a layer missing from the table.
- **Dimension style:** ORION, with DIMSCALE 70, DIMTXT 2.5 and DIMTSZ 1.25, so dimension text is 175 mm high.

### 2.2 Layer assignments: VERIFIED – independent (I-1, I-2)

| Layer | Contents found | Assessment |
|---|---|---|
| A-WALL-EXT / -PARTY / -INT | 26 / 1 / 32 building rectangles, plus one 500 × 300 legend swatch each | As described in the issued legend |
| A-GLAZ | 14 windows, each 1 polyline and 2 lines, all inside wall gaps | Consistent |
| A-DOOR | 18 swing doors (arc and open-leaf line); 4 sliding-panel lines (stores) | Consistent. The store doors have no swing (VF-04) |
| A-SANI / A-FURN | Fittings and furniture at ADM Appendix D sizes (§4) | Consistent |
| A-ROOF / A-PROV / A-EXT / A-ACCS | Rooflights and porch roofs; conservatories and patios; porches, posts and paths; reference zones | Consistent |
| A-ANNO-TEXT / A-ANNO-DIMS | All 85 texts / all 31 dimensions, plus the north arrow and scale-bar polylines | Consistent |
| HATCH | 62 hatches, each matching a wall polyline on the same layer (59 SOLID, 2 ANSI37 party wall and swatch). Every wall is hatched | Consistent |

### 2.3 Walls and junctions: VERIFIED – independent (I-1)

- **Walls:** 59 building wall rectangles, axis-aligned, thicknesses 300 / 200 / 100 mm.
- **Areas:** union areas are external 10.62, party 2.46 and internal 6.30 m², and equal the sums of the pieces, so there are **no overlaps**. A direct rectangle-intersection test confirms this.
- **Junctions:** 118 wall-piece ends.
  - 46 abut a perpendicular wall face or a flush corner or party-wall end.
  - 72 are jambs at openings.
  - **0 are free ends.**

### 2.4 Dimensions: values VERIFIED – independent; two defects

| Check | Result |
|---|---|
| Value against definition points | All 31: stored measurement (code 42) equals the definition-point distance, block text matches, no text overrides |
| Chains sum to overall | North 18,600 ✓; west 12,300 ✓; east 12,300 ✓; south (dwelling A only) 9,300 to the party-wall centreline |
| Definition points on wall geometry | All lie on wall polygon vertices or edges |
| **Chains describe the features they sit beside** | **West ✓ and north ✓. East ✗ (VF-02):** break points are at y 4,300 / 4,400 / 6,900 / 7,000. The partitions that meet the east wall are at y 4,000 / 4,100, 6,600 / 6,700 and 8,700 / 8,800, the mirror of the west side. The east chain carries dwelling B's party-wall-side room pattern. Issued check V-2 passed it because it only tested the sums |
| **Associativity** | **VF-03:** 20 of 31 dimensions carry association data (13 complete, 7 partial); 11 carry none. Six wall dimensions (2CF, 2D0, 2D1, 2D6, 2D7, 2D8) are associated with **provisional** patio polygons 224 / 225 and path line 234. The issued documents call all 31 "associative" |
| South chain | Covers dwelling A only (VF-15) |

### 2.5 Openings: VERIFIED – independent (I-1, I-2)

| Count | Type | Detail |
|---|---|---|
| 36 | Total openings | All lie between collinear wall pieces of the same thickness band |
| 14 | Windows | All glazed |
| 18 | Swing doors | Each hinge sits on a gap end and the arc radius equals the gap. The exception is the front doors: 1,010 mm leaf in a 1,100 mm opening (VF-14) |
| 2 | Store openings | 1,000 mm with bypass sliding panels and no swing (VF-04) |
| 2 | Kitchen–living openings | 1,800 mm, no door, by design |

**No door or glazing entity lies outside a gap.** No obstacle lies inside any door swing.

### 2.6 Text placement: ESTIMATED extents, confirmed visually (I-3, I-5)

- **Clean:** no label overlaps a wall, and no label overlaps another label.
- **Crossed by other linework (VF-08; all still legible):**
  - Porch labels and the party-wall label are crossed by dimension extension lines.
  - Conservatory labels are crossed by the conservatory door swing.
  - The eight "100" dimension texts are crossed by their own extension lines.
  - The ROOFLIGHT label crosses its X and the edge of the coffee table.
  - The PATIO labels cross the patio slab lines.
- **Text heights:** range from 80 to 600 mm. 2 texts are 80 mm, 12 are 90 mm and 31 are 175 mm (dimensions).
- **Multiline text blocks:** the notes, room schedule and dimension key blocks do not overlap.

### 2.7 Rooms: VERIFIED – independent (I-1)

With openings closed there are 18 enclosed regions, 9 per dwelling.

- Every region is labelled and every one is a **perfect rectangle**.
- Every label's "W × D" and "m²" figures match the measured region.
- There are no unlabelled regions and no leaks to the outside.
- The room-schedule text on the sheet matches.

### 2.8 Mirror symmetry: VERIFIED – independent (I-2)

156 geometry entities in dwelling A and 156 in dwelling B. **All match** their mirror about x = 9,300 on the same layer. The one intended text difference is the utility label "at W end" / "at E end".

### 2.9 Audit of statements in the issued documents

| Issued statement | Where | Result |
|---|---|---|
| "ISO A1 portrait at 1:50" / "true 1:50" | Sheet note; Report §2, §3, V-5; Change Log C-30 | ✗ About **1:48.23** (VF-01) |
| "31 associative dimensions" | Change Log C-27; Report §2, V-4 | ✗ Partly: 20 with association data, 11 without, 6 tied to provisional geometry (VF-03) |
| V-2 "chains sum, Pass" | Report §4 | ✓ The sums are right, but the check was incomplete: the east chain is misplaced (VF-02) |
| GIA 104.13; NIFA 100.10; partitions 4.03; footprint 228.78; walls 18.06 / 2.46 | Sheet, CSV, Report | ✓ "Partitions" includes 0.88 m² of opening zones (VF-13) |
| Room sizes and areas (18 rooms) | Sheet, CSV | ✓ |
| Conservatory 3.19 m² (hexagon) | CSV, Change Log C-17 | ✓ 3.1875 m² measured from the DXF polygon |
| 508 entities, 13 layers, no text overrides | Report | ✓ |
| PNG 7,500 × 10,619 px, about 320 dpi at A1 | Report | ✓ PNG header; 7,500 px / 594 mm = 320.7 dpi |
| "No furniture in any swing" | Report V-8 (model) | ✓ Confirmed independently from the DXF (I-2) |
| Conservatory door "leading-edge nib 300 mm on the west" | Change Log C-13; Pre-Approval Revision | ⚠ True on the **inside (push)** face. The door opens outward, so the pull face is outside (VF-06) |

---

## 3. Area reconciliation (requirement 3)

All values are **VERIFIED – independent** (I-1) unless marked. Full table: `..._Verification_Area_Reconciliation.csv` (41 rows; every comparable issued value agrees).

| Ref | Item | m² |
|---|---|---|
| AR-01 | Footprint to outer faces, 18.60 × 12.30 m | **228.78** |
| AR-02 / 03 | Each dwelling, inside the internal faces of the external walls and the party wall (8.90 × 11.70 m) = **GIA as issued** | **104.13** each |
| AR-04 / 05 | Sum of the 9 room rectangles (NIFA) per dwelling | 100.10 |
| AR-06 | Drawn partition polygons per dwelling | 3.15 |
| AR-07 | Door and opening zones within partition lines per dwelling (6 doors × 0.10 + store 0.10 + kitchen opening 0.18) | 0.88 |
| AR-08 | Partitions including their opening zones (the issued "partitions") | 4.03 |
| AR-09 | Residual 100.10 + 4.03 − 104.13 | **0.00** |
| AR-11 / 12 / 13 | External walls: drawn 10.62 + window and door zones 7.44 = zone | 18.06 |
| AR-14 | Party wall, 0.20 × 12.30 (full depth; excluded from both GIAs) | 2.46 |
| AR-15 | Residual 228.78 − (2 × 104.13 + 18.06 + 2.46) | **0.00** |
| AR-16 | *Sensitivity only (DERIVED):* GIA if measured to the party-wall centreline: + 0.10 × 11.70 | 105.30 |
| AR-17 / 18 | **Conservatory as drawn:** 6-vertex polygon (4500, 12300) / (7000, 12300) / (7000, 13050) / (6250, 13800) / (5250, 13800) / (4500, 13050), i.e. the 2.5 × 1.5 m box less two 750 × 750 mm corner triangles (3.75 − 0.5625) | **3.1875** each |
| AR-19 / 20 | Patios, 1.8 × 5.0 m | 9.00 each |
| AR-21 | Porch outline, 2.4 × 2.0 m | 4.80 each |
| AR-22 / 23 | Rooflight outline 1.2 × 1.2 m (net glazing "about 1.0 m²" is an **ESTIMATE**); porch-roof outline 2.6 × 2.1 m | 1.44 / 5.46 each |

**Conventions:**

- GIA is measured to the internal faces of the perimeter walls including partitions, as NDSS para 8 was read at issue, with the party wall treated as a perimeter wall. AR-16 shows the effect of measuring to the party-wall centreline instead. Which convention applies is a matter for the surveyor or planning authority (PA-14).
- Provisional external items are excluded from GIA.

---

## 4. Accessibility review, room by room (requirement 4)

**Target:** M4(2), which applies only where a planning condition requires it (ADM 0.3, 2.18; **VERIFIED – official text**).

- **Geometric columns:** measured from the DXF for dwelling A (**VERIFIED – independent**, I-2). Dwelling B is an exact mirror (§2.8).
- **Interpretation columns:** items a plan cannot settle (INTERPRETATION / PROFESSIONAL APPROVAL REQUIRED).
- **Criteria:** dimensions are quoted from ADM Vol 1 2015 incl. 2016 amendments, paras 2.20–2.30, Table 2.1, Diagrams 2.3 and 2.5, and Appendix D.

### Nib convention

ADM 2.22d asks for "a minimum 300mm nib … to the leading edge of every door". Diagram 2.3 Note 1 says the nib is "only required where door opens inward". Which face this refers to is an **INTERPRETATION** (RQ-03), so nibs are reported on both faces. The **pull face** is the side the leaf swings into.

| Room | Geometric checks (measured → criterion → reading) | Needs interpretation or professional input |
|---|---|---|
| **Entrance and porch** | Landing (provisional porch) 2.4 × 2.0 m → ≥ 1.2 × 1.2 m (2.20a) → met if built as drawn. Cover (porch roof) 2.6 × 2.1 m → ≥ 0.9 × 0.6 m (2.20b) → met if built. Opening 1,100 mm, leaf 1,010 mm. Pull-face nib (hall) **300 mm** → ≥ 300 (2.20f) → met; the 1.5 m hall maintains the width more than 1,200 mm beyond. Push face more than 3 m | Clear opening ≥ 850 mm measured per Diagram 2.2 (product; VF-14). Level landing and accessible threshold (2.20a, h). Reveal ≤ 200 mm on the leading side of a 300 mm wall (2.20g; leaf drawn at the inner face; frame not designed). Lighting (2.20c) |
| **Hall** | Clear width **1,500 mm** → ≥ 900 (2.22a) → met. With a 1,500 mm corridor, doors need ≥ 750 mm clear when not approached head-on (Table 2.1); all hinged openings are 1,000 mm. No obstruction is drawn. The outward bathroom door leaves 500 mm of hall while open (DR-04) | Clear opening widths depend on the door product. Radiators not designed (2.22b) |
| **Bedroom 1 (principal)** | Bed 2,000 × 1,500 (Appendix D principal double). Side zones: west **750**, east **1,150** → ≥ 750 both sides (2.25b) → met, with 400 × 400 bedside tables at the head. Foot **1,700** → ≥ 750 → met. A 750 mm-wide route reaches **both** windows from the door (2.25a) → met. Door nibs: pull 400 (to the wardrobe), push 2,500 | Whether bedside tables sit within the permitted zone "a" (Diagram 2.4 note 2; RQ-08) |
| **Bedroom 2 (double)** | Bed 1,900 × 1,350 (Appendix D other double). Sides **1,020 / 1,020** → ≥ 750 one side (2.25c) → met. Foot **1,300** → met. Route to the window → met. Nibs 2,500 / 2,500 | As above |
| **Quiet work room** | Not a bedroom. Door nibs: pull 1,300, push 1,600 | If it were used as a bedroom, 2.25 would apply; not assessed |
| **Living / dining** | Living area on the entrance storey (2.24a) → met (single storey). Hall-to-living door nibs 300 / 300. **Conservatory door** (external door, 2.21 → 2.20d–i): 1,000 mm opening, opens outward. Pull face (outside): open with no enclosure; **200 mm if the provisional conservatory is built as drawn**, and its chamfer cuts the 1,200 mm zone (VF-06). Push face (inside) 300 | Principal window sill ≤ 850 mm (2.24c; elevation, not in plan; Part K guarding). Conservatory door handing against the conservatory design. Threshold |
| **Ngaji / kitchen** | Clear space (2.24b ≥ 1,200 mm): between the rear and south runs **2,000**; in front of the tall units more than 3,000; between the tall units and the end of the base run **1,200** → met. Kitchen-to-utility door: pull face (utility) 800; **push face (kitchen) 100** (VF-07) | Whether a push-face nib is required (RQ-03) |
| **Bathroom** | WC, basin and bath present, on the same storey as the principal bedroom (2.29a). Fittings match Appendix D sizes. WC centreline **450 mm** from the party-wall face → 400–500 (Diagram 2.5) → met. WC zone 1,350 × 1,100 → clear. Basin zone 700 × 1,100, measured conservatively from the basin front → clear. Bath zone 700 × 1,100 → clear at either end. Door **opens out of the bathroom** (2.27d) → met | Potential level-access shower (2.29c): falls, drainage and size. Strengthened walls (2.26). Radiator or towel rail clear of zones (Diagram 2.5 note 5; not designed). Services heights (2.30) |
| **Utility** | Kitchen door swings in with no obstacle in the swing. **Side door** (external, opens outward): pull face (outside) clear; push face 500; **the 600 × 600 MVHR/cylinder allowance overlaps 100 mm of the opening's inside face** (VF-05) | Effect on the ≥ 850 mm clear opening (2.21 → 2.20d) |
| **Store** | **Bypass sliding panels 2 × 550 mm in a 1,000 mm opening → about 450 mm clear** (VF-04). Free floor about 1.0 × 1.6 m | Whether 2.22 applies: the Note 1 cupboard exclusion does not cover a store "large enough to be entered". If it applies, Table 2.1's ≥ 750 mm is not met as drawn |
| **Whole dwelling** | Single storey: step-free between rooms if floors are level (2.23a) | Levels, thresholds, services heights (2.30), strengthened walls (2.26) and window handle heights are not in the plan |

**Summary of the geometric readings:**

- **Met:** about 30 dimensional readings.
- **Not met as drawn, or conditional:** 4 (VF-04 to VF-07), each linked to a decision or interpretation.
- **Not determinable from a plan:** 12+ provisions.

This is **not** an accessibility compliance assessment.

---

## 5. Register (requirement 5)

`..._Verification_Register.csv` has 68 rows, each with position, evidence class, resolution route, owner and a priority (reviewer judgement):

| Category | Rows | Highest priority items |
|---|---|---|
| Verification findings (VF) | 16 | VF-01 scale (High), VF-02 east chain (High), VF-03 associativity (Medium), VF-04 to VF-06 door geometry (Medium) |
| Provisional assumptions (PA) | 15 | Wall build-ups and therefore the overall dimensions (High) |
| Missing site information (SI) | 10 | Boundary, levels, planning authority and conditions, designations (High) |
| Regulatory questions (RQ) | 14 | Planning scope; Parts B, E and L (High); Part M interpretations RQ-02 to RQ-08 |
| Unresolved design risks (DR) | 13 | Wall thickening, prints mis-measured until VF-01 is fixed (High) |

---

## 6. Visual review of the issued A1 PDF and PNG (requirement 6)

### 6.1 Formats: VERIFIED – independent (I-4)

- **PDF:** one page, MediaBox 1,683.78 × 2,383.94 pt = **594 × 841 mm (ISO A1 portrait)**. Clip box has 18 pt (6.35 mm) margins. Producer: CADCraft.
  - **No font objects:** text is drawn as vector strokes, so it cannot be searched or extracted (VF-12). Label consistency between DXF and PDF could therefore only be checked visually.
- **PNG:** 7,500 × 10,619 px, RGBA, same aspect ratio as A1.
  - Re-rendering the issued PDF with the same renderer gives a **byte-identical** PNG (SHA-256 `7d29629a…77c6`), so the PNG is exactly reproducible from the PDF.

### 6.2 Scale: VERIFIED – independent; defect VF-01

| Method | Measured | At true 1:50 | Implied scale |
|---|---|---|---|
| PDF vectors: 500 mm legend swatch | 29.387 pt | 28.346 pt | **1:48.23** |
| PNG: building width (black external-wall faces) | 4,876 px | 4,697 px | 1:48.16 |
| PNG: building depth | 3,226 px | 3,106 px | 1:48.14 |
| PNG: 5 m scale bar | 1,311 px | 1,263 px | 1:48.16 |
| PNG: party-wall centre against DXF position | 3,561.5 px | 3,562.0 px predicted | consistent (0.5 px) |

**Cause:** CADCraft's PDF export fitted the drawing to the printable width even though `scale: "1:50"` was requested.

**Fix tested (scratch file only, not issued):** re-exporting with `fit: false` gives exactly 1:50 (28.346 pt per 500 mm). The drawing then fits A1 portrait with margin.

**Consequences:**

- The scale bar is drawn in model units, so it is correct at any print size.
- The dimension values are text, so they are unaffected.
- Anyone scaling the issued print with a 1:50 rule would over-read by about **3.7 %** (18,600 mm would read about 19,280).

### 6.3 Legibility

Native-resolution crops 01–09 are in the Visual Evidence sheet: title, dimension key and schedule, smallest text, patio B, conservatory, 100 mm chain, hall and bathroom, legend and scale bar, north arrow.

- **On screen:** all text is legible at native resolution.
- **On paper at 1:50 on A1 (VERIFIED heights):**

| Text height (model) | On sheet | Count |
|---|---|---|
| 80 mm | 1.6 mm | 2 |
| 90 mm | 1.8 mm | 12 |
| 100–120 mm | 2.0–2.4 mm | 27 |
| ≥ 130 mm | ≥ 2.6 mm | 72 (incl. 31 dimension texts at 3.5 mm) |

- **Standard comparison (UNVERIFIED citation):** secondary sources give **1.8 mm** as the smallest nominal lettering height in the ISO 3098 series (now ISO 3098-1). One drafting guide suggests about 2.5 mm for notes on A1–A3. I could not check the standard's own text. On that basis the two 80 mm labels are below the series minimum (VF-11).

### 6.4 Colour contrast on white paper: VERIFIED pixel colours; the WCAG contrast ratio is used only as a proxy

| Layer / element | Rendered colour | Contrast with white |
|---|---|---|
| External walls (fill), text | black | 21 : 1 |
| A-GLAZ windows | blue | 8.6 : 1 |
| A-ANNO-DIMS, party wall | red | 4.0 : 1 |
| A-WALL-INT partitions | grey 128 | 4.0 : 1 |
| A-ROOF | magenta | 3.1 : 1 |
| **A-PROV provisional** | orange (255,127,0) | **2.5 : 1** |
| **A-DOOR swings, A-SANI fittings** | cyan | **1.25 : 1** |
| **A-ACCS zones** | light green (dashed) | **1.22 : 1** |
| **A-EXT paths** | green | **1.15 : 1** |

Door swings, fittings, accessibility zones and paths are faint on paper and could disappear on a monochrome printer (VF-09).

### 6.5 Visibility of provisional lines: VERIFIED (I-4)

Fraction of each A-PROV outline (excluding edges on the building face) with orange ink within 3 px:

| Outline | Inked |
|---|---|
| Conservatory A | 82 % |
| Conservatory B | 82 % |
| Patio A | 77 % |
| **Patio B** | **33 %** (VF-10) |

The expected value for a dashed line is about 70–85 %. Patio B's top and bottom edges lie under red dimension extension lines (crop 04). Every provisional item also carries a "PROVISIONAL" text label, so none is shown as confirmed.

### 6.6 Dimension classification

- The dimension key is present and legible (crop 02). It labels the overall dimensions and chains EXTERNAL, room labels CLEAR INTERNAL, and wall-thickness segments and external-works sizes PROVISIONAL.
- Every dimension on the sheet is an exterior chain; there are no internal dimension lines.
- Exception: the **east chain is misleading** (VF-02), so a reader would mis-locate dwelling B's partitions on the east side.

### 6.7 Consistency between formats

| Pair | Method | Result |
|---|---|---|
| PNG ↔ PDF | Re-render and hash | Identical |
| PDF ↔ DXF | Same vector content plotted by CADCraft; scale from the swatch; visual comparison of labels | Consistent except the scale statement (VF-01). Text not machine-comparable (VF-12) |
| PNG ↔ DXF | Pixel positions of walls and party wall against DXF coordinates | Consistent to about 2 mm (drawing) |
| CSV ↔ DXF | 41 values (I-1) | All agree |
| Sheet room schedule ↔ CSV ↔ DXF | Text cross-check (I-1) | All agree |

---

## 7. Fact, model result, assumption, approval (requirement 7)

| Statement | Class |
|---|---|
| Footprint 228.78 m²; GIA 104.13 m² per dwelling; NIFA 100.10; room sizes; wall areas; reconciliation residual 0 | VERIFIED – independent |
| Conservatory polygon 3.1875 m²; patios, porches and roof outlines | VERIFIED – independent (sizes PROVISIONAL) |
| Dwelling B is an exact mirror of A | VERIFIED – independent |
| PDF and PNG scale about 1:48.2; PNG reproducible from PDF | VERIFIED – independent |
| Door widths, nibs, bed zones, bathroom zones, kitchen clearances, routes (as drawn) | VERIFIED – independent (geometry) |
| ADM provision wording and dimensions; Appendix D sizes | VERIFIED – official text |
| Whether those geometric readings satisfy the provisions | INTERPRETATION / PROFESSIONAL APPROVAL REQUIRED |
| Issue-stage furniture and zone tests; issued room schedule generation | MODEL RESULT (now re-checked independently) |
| MVHR energy and cost figures; daylight factor; rooflight net glazing about 1.0 m²; airflow 31.2 l/s | MODEL RESULT / ESTIMATE (issue-stage; not re-checked here) |
| Text extents in the clash test | ESTIMATE (confirmed visually) |
| Wall build-ups; overall dimensions; orientation; conservatory, porch, patio and path sizes; ceiling height; door products; level thresholds | ASSUMPTION / PROVISIONAL |
| Site boundary, levels, planning authority and conditions, designations | UNKNOWN (register SI) |
| Third-party CAD compatibility; ISO 3098 threshold citation | UNVERIFIED |
| Planning, Building Regulations (Parts A, B, E, F, G, H, K, L, M, O, P, Q) and fire-safety compliance | PROFESSIONAL APPROVAL REQUIRED; **not claimed** |

---

## 8. Integrity (requirement 1)

See `..._Verification_Manifest.csv` / `.sha256`. For all six issued deliverables and the three Draft 0.1 files, the SHA-256, size and modification time were recorded at the start (18:41:37) and the end of the gate. All are **unchanged**.

The issued Report.md hash `672bc39c…12bd` is recorded here for the first time; it was not part of the issued report itself.

## 9. Limits of this gate

- **Reviewer independence:** the blind review is independent in implementation and context, not in reviewer. The same AI model wrote both sides. A human or third-party check is still advisable.
- **No third-party CAD:** no other CAD package opened the DXF.
- **No OCR:** text in the PDF and PNG was compared visually, not by machine.
- **Estimated text extents:** CADCraft font metrics are not in the DXF.
- **Plan geometry only:** no elevation, section, roof, structural, fire, acoustic, energy, daylight, drainage or site checks.

### Sources

- Approved Document M Vol 1 (2015 incl. 2016 amendments), paras 0.3, 2.18–2.30, Table 2.1, Diagrams 2.3–2.5, Appendix D. Text extracted from, and pages rendered from, the gov.uk PDF used at issue.
- [Technical lettering — Wikipedia](https://en.wikipedia.org/wiki/Technical_lettering) and [CAD Setter Out — lettering heights](https://cadsetterout.com/drawing-standards/lettering-heights/), for the ISO 3098 nominal height series only (secondary).
