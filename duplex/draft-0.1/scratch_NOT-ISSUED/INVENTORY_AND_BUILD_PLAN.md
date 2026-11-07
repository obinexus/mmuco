# Inventory and build plan

MMUCO ORION TRIPLEX COMPOUND — 3D MODEL PROPOSAL — NOT ISSUED (25 Oct 2026)

## 1. Sources and revisions used

| Source | Revision / status | Use in the model | SHA-256 |
|---|---|---|---|
| `MMUCO_ORION_Duplex_Draft_0.2.2.dxf` | **Latest issued.** Chain: Draft 0.2 baseline → 0.2.1 drafting corrections → 0.2.2 door resolution | Housing plan geometry | `2ec8d3f3…` (matches the issued manifest; a byte-identical copy is in `source_refs/`) |
| `MMUCO_ORION_Duplex_Draft_0.2.2.png` | Issued sheet image | Plan underlay for visual checks only | `7a60da12…` (copy in `source_refs/`) |
| `MMUCO_ORION_Duplex_Draft_0.2_Verification_Register.csv` | Frozen | Provisional assumptions PA-01 to PA-15 (heights, wall build-ups, north, paths) | Covered by the 0.2 Verification manifest |
| Proposed Draft 0.2.3 | **NOT ISSUED** | Not used. It changes only the kitchen base runs, not walls or openings | — |
| Otter transcript, "Orion Triplex and Garden Redesign" | Dictated by the client, 25 Oct 2026 | Compound programme and the 2:1 rule | `6ccd61d8…` (copy in `source_refs/`) |
| Written brief, "Approve SolidCraft Trial and Model the Three-Node Compound" | 25 Oct 2026, in conversation | Structure, components, acceptance checks | — |

## 2. What exists and what is missing

**Exists in Draft 0.2.2 (plan only):**

- External walls: 27 outlines, 300 mm, PROVISIONAL.
- Party wall: 200 mm, PROVISIONAL.
- Internal partitions: 33.
- Doors and glazing: positions and widths on plan.
- Roof elements: two 1.2 × 1.2 m rooflights and the porch roofs.
- Provisional external works: porches 2.4 × 2.0 m, side patios 1.8 × 5.0 m, conservatories 2.6 × 1.5 m with 300 mm chamfers, 1.5 m path stubs.
- Labelled rear gardens: unbounded, with no dimensions.

**Missing anywhere in the project:**

- **Elevations and sections:** none exist. No front, rear, LHS or RHS elevation and no section has ever been drawn. All 533 DXF entities are flat (no Z, elevation or thickness).
- **Heights:** none verified. The only recorded value is **PA-10, "Ceiling height 2.5 m; roof form not designed"** (an ASSUMPTION).
- **Roof:** the roof form is not designed.
- **Openings:** no window or door head heights. The only sill value is a maximum of 850 mm, for the living-room window.
- **Site:** no levels. No site boundary or survey ("Site boundary NOT SHOWN"). North is assumed (PA-07).
- **Gardens:** no garden or compound design of any kind.

**Consequence:** the brief asks to keep the existing front, rear, RHS and LHS elevations as reference views. That cannot be done, because they do not exist.

- **The plan view can be verified** against the issued drawing.
- **The four elevations will be orthographic projections of a model whose heights are PLACEHOLDERS.** They will be labelled as such, not as verified elevations.

## 3. Coordinate system

| Aspect | Convention |
|---|---|
| Units | mm, 1:1 |
| Coordinates | The issued DXF coordinates, unchanged |
| Origin | The front-left outer corner of the building |
| X | Building width: 0 to 18,600 |
| Y | Building depth: 0 to 12,300, positive towards the rear and the assumed north |
| Z | Up, with 0 at the ground-floor datum |
| Front | Faces −Y. Viewed from the front, LHS is the x = 0 gable and RHS the x = 18,600 gable |

Full detail is in `compound_parameters_PROVISIONAL.json`.

## 4. Measured areas and the 2:1 rule

The transcript's wording is: "keep the proportions … of the garden and public spaces, two to one ratio directly to the housing".

| Housing basis | Housing (m²) | Reading A: garden + patio/walkway = 2 × housing (m²) | Compound, A (m²) | Reading B: garden alone = 2 × housing (m²) |
|---|---|---|---|---|
| **H1: building footprint 18.60 × 12.30** (stated on the drawing, VERIFIED) | **228.78** | **457.56** | **686.34** | 457.56, plus the walkway on top |
| H2: H1 + conservatories (2 × 3.81) | 236.40 | 472.80 | 709.20 | 472.80, plus the walkway |
| H3: H2 + roofed porches (2 × 5.46) | 247.32 | 494.64 | 741.96 | 494.64, plus the walkway |

**Proposed reading: A with H1.** The transcript groups "garden and public spaces" against the housing, and H1 is the footprint stated on the issued drawing. Both are ASSUMPTIONS for decision D2.

The side patios (2 × 9.00 m²) are counted with neither node until decision D3.

## 5. Transcript and written brief compared

| Item | Transcript | Written brief | Proposed handling |
|---|---|---|---|
| Water fountain | Named first in the list of contents | Not listed | Optional component `12_WATER_FOUNTAIN` (decision D6) |
| Orangeries at 45° | "a conservatory facing the two orangeries at 45 degree angle, counterclockwise and clockwise" | Rotated ±45° to an agreed reference axis | Reference axis decision D5: the building front (X axis) or the conservatory facing direction |
| Rainwater | Collected in the well and "processed through the housing node", by people and agentic AI, by rope and bucket | Roof catchment → collection → storage → treatment and testing → approved use; rope and bucket only if appropriate | Shown as a concept only; **not shown as drinkable** |
| Generator | Diesel; powers "itself, the housing and the grid" | Provisional location; safety constraints listed | Placeholder enclosure with a maintenance zone; no fuel store near the well, food or gathering areas |
| Animals | Big dog kennel; "cat or dog to enter a house" | Kennel and separate cat provision | Kennel and cat shelter. A pet door into the dwellings is **not modelled** (it would change the issued housing) |
| 2:1 | "garden and public spaces … to the housing" | "garden/public-space area to housing area"; interpretation to be recorded | Section 4 |
| Back gate, security | "back gate and security built in by design" | Back gate, secure perimeter, controlled access | Back gate in the provisional boundary; access arrangements left for design review |

## 6. Staged build plan (to run in a session with SolidCraft tools)

| Stage | Work | Checks |
|---|---|---|
| **0. Tool gate and trials** | List the SolidCraft tools. Allow the tool to write to this folder only (`--allow-path`, a config change for approval). In a throwaway design, test: back, left and right views (orthographic?); save, reopen and re-measure; `sketch.insert_dxf` on the **copy** of the real DXF; a render | Every test recorded as PASS, FAIL or NOT SUPPORTED |
| **A. Reference** | Insert the DXF copy into a reference component; check the 18,600 and 12,300 overall dimensions | Within ±1 mm of the drawing |
| **B. Housing** `01_HOUSING_ORION_DUPLEX` | Extrude external, party and internal walls from their own layers, to the placeholder 2,500 mm. Cut door and window openings at their plan widths, with placeholder heights. Add a provisional flat roof slab, the rooflights, and the provisional porches, conservatories and patios. Build dwelling B from its own entities, not by mirroring | Bounding box 18,600 × 12,300 mm; footprint 228.78 m²; A and B mirror within ±1 mm |
| **C. Compound** `02`, `03`, `11` | Public garden and patio/walkway as separate bodies or regions on the north side; a conceptual boundary with the back gate | Measured areas meet the 2:1 target (reading A: 457.56 m² ±1%) |
| **D. Facilities** `04`–`10` (and `12` if approved) | Placeholder sizes from the parameter file. Orangeries at +45° and −45° | Measured angles of 45° ±0.1°; separation rules (section 7); routes kept clear |
| **E. Views** | Compound overview, top plan, housing front, rear, LHS and RHS (orthographic), garden overview, one close-up per component. Verified geometry and provisional geometry in distinct colours | All views generated from the one model |
| **F. Validation** | The brief's 11 acceptance checks; STEP export; manifest of this folder; protected-hash comparison with `evidence/` | Report, then stop for review |

## 7. Safety and technical reviews (the model does not settle any of these)

- **Water:** rain and well water must not be presented as drinkable. Drinking use needs treatment, testing, hygienic storage and a water-safety plan. The well needs a cover or barrier.
- **Pond:** purpose, depth, water source, edge protection (children and animals) and maintenance are unresolved. It is not a swimming pool.
- **Generator:** noise, exhaust, ventilation, fire separation, fuel storage, weather protection, electrical connection, drainage and maintenance access all need assessment before any location is fixed.
- **Animals:** hygiene and separation from food growing, food storage and water.
- **Canopy:** structure, wind and drainage.
- **Access:** routes and accessibility, emergency egress, and security of the perimeter and gate.
- **Housing:** party wall fire and acoustic performance. All wall build-ups are provisional (PA-01).

## 8. Elevation evidence received after the inventory (25 Oct 2026)

Two client images, copied byte-identical into `source_refs/`:

| File | What it shows | SHA-256 |
|---|---|---|
| `client_elevation_sketch_2026-10-25.jpg` | Hand sketch of an elevation: a double door in a frame, steps below it, a two-casement window with diagonal lattice bars annotated **"1400 x 1000"**, the wall outline, and an unidentified element at the right with a diagonal line | `3bc54339…` |
| `client_cadcraft_screenshot_2026-10-25.png` | The same door, steps and lattice window drawn in the client's own CADCraft window. The file was not identified and could not be inspected; no dimensions are visible | `81c997f2…` |

**Classification:** CLIENT SKETCH, **not to scale**. The window is drawn nearly square but annotated 1400 × 1000. The only measurable evidence is that annotation.

**Checked against the issued Draft 0.2.2 plan:**

- **Door: conflict.** The plan's front entrance door is a **single** 1,010 mm leaf (a 1,100 mm opening, PA-11), and the rear door is a single 1,000 mm leaf. The sketch shows a **double** door.
- **Window width: conflict.** **No 1,400 mm window exists** on the plan. Front windows are 1,500 (bedroom 1) and 1,200 (bedroom 2); gable windows 1,200; rear windows 1,500. The 1,000 mm height would be new information, since no heights exist.
- **Steps: conflict.** The plan assumes a level threshold and approach (PA-12), and the drawing's accessibility target is M4(2). The sketch shows **about three steps** up to the door; the riser count is uncertain.
- **New information, not on the plan:** diagonal lattice bars to the casements, and a raised floor (implied by the steps).

**Not used to change the model until decisions D9–D13 are made.**

## 9. Decisions needed

| ID | Decision | Proposed default if no decision is given |
|---|---|---|
| D1 | Heights and roof | Placeholders: walls 2,500 mm (PA-10), flat 300 mm roof slab, openings 2,100 mm head and 850 mm sill. All labelled PLACEHOLDER |
| D2 | 2:1 basis | Reading A with H1: public area 457.56 m² |
| D3 | Where the public node sits, and whether the labelled rear gardens stay with the housing | North of the housing, behind the conservatories, across the housing's width. The rear gardens stay with the housing |
| D4 | Walkway width | 2.0 m (the PA-06 compound standard) |
| D5 | Reference axis for the orangeries' ±45° | The building front (X axis) |
| D6 | Water fountain | Included as an optional, placeholder component |
| D7 | Component sizes | The placeholders in the parameter file |
| D8 | Pet access into the dwellings | Not modelled: it would change the issued housing |
| D9 | Front entrance: single 1,010 leaf (plan) or double door (sketch) | The plan (issued) stays; the sketch is recorded as a conflict |
| D10 | Steps (sketch) or level threshold (PA-12, M4(2) target) | The plan assumption stays (level); the steps are recorded as a conflict |
| D11 | Which window is 1400 × 1000 (none on the plan), and is it W × H? | Unresolved: plan widths stay; the 1,000 height is not applied |
| D12 | Lattice glazing bars | Shown only if approved; appearance only |
| D13 | The right-hand element of the sketch (diagonal line) | Unidentified: not modelled |
