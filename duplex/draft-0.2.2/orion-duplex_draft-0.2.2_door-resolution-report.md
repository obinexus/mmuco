# MMUCO ORION Duplex — Draft 0.2.2 Door Resolution Report

**Issue:** `MMUCO_ORION_Duplex_Draft_0.2.2`, 24 October 2026
**Baseline:** issued Draft 0.2.1, used through a byte-identical working copy
**Scope:**

- "Face Me and I Face You" hallway entries, using Option B (double-door entries).
- Door register items VF-04 to VF-07, implemented as directed.

> **Status: design development, not approved.** Nothing here states or implies planning, Building Regulations, accessibility (ADM M4(2)) or construction-readiness compliance or approval. Every regulatory interpretation is marked **REQUIRES CONFIRMATION**. Clear door openings are **ESTIMATES** until a door schedule exists.

**Evidence labels:**

| Label | Meaning |
|---|---|
| **MEASURED** | Read from the saved DXF/PDF/PNG by scripts that do not use the drawing generator |
| **AUTOMATED CHECK** | Scripted pass/fail test, with its result |
| **ESTIMATE** | Calculated using a stated assumption |
| **ASSUMPTION** | No source or measurement behind it |
| **REQUIRES CONFIRMATION** | A professional or building-control judgement is needed |

Evidence files: `MMUCO_ORION_Duplex_Draft_0.2.2_Evidence/` (sections 01–07, `preservation/` and `scripts/`). Scratch files: `MMUCO_ORION_Duplex_Draft_0.2.2_SCRATCH_not_issued/`, **not issued**.

---

## 0. Summary

**Interpretation selected:**

- **Rooms.** "Face Me and I Face You" is applied to **Room A = Bedroom 1** (west of the hall) and **Room B = Bedroom 2** (east of the hall) in each dwelling. These are the only two rooms whose entries already face each other directly across the hall (both at y 2,800–3,800 in Draft 0.2.1). The quiet-room and bathroom entries are offset and stay single doors.
- **Double doors.** Option B is read as **B1: a pair of leaves at each room entrance**. Under B1 each room gets its own double-door entrance, so both entrances are visibly separate. B2 (one leaf at each of the two facing entrances) was tested as the reference and is **not** a double door at either entrance. B3 (two-leaf sliding) was rejected on measured conflicts (§3).

**As built in 0.2.2 (dwelling A; dwelling B is the exact mirror):**

| Item | Value |
|---|---|
| Hallway (spine) | 1,500 mm clear wide (x 4,400–5,900) × 6,600 mm (y 300–6,900) = 9.90 m², **unchanged** |
| Room A entry | Structural opening 1,400 mm at x 4,300–4,400, y 2,500–3,900. Leaves 900 (main, hinged at the north jamb) + 500 (secondary, hinged at the south jamb); both open into Room A |
| Room B entry | Structural opening 1,400 mm at x 5,900–6,000, y 2,500–3,900, **directly opposite** Room A's. Same leaves, opening into Room B |
| Clear opening (ESTIMATE) | 849 mm with the main leaf only; 1,298 mm with both leaves open |
| Hall clear width in the entry zone (y 2,500–3,900) | **1,500 mm** with doors closed, operating or fully open |
| Collisions | None: walls, furniture, fittings, the opposite entrance and every other door (AUTOMATED CHECK) |
| Room and hall areas | **Unchanged** (Room A 14.80, Room B 12.80, hall 9.90 m²). Only partition piers were shortened; no wall moved |
| Scale | PDF measured **1:50.000** (width, depth, scale bar); PNG 1:49.90–1:49.94 (anti-aliasing) |

**Door register (as directed):**

| Item | Direction | Result |
|---|---|---|
| VF-04 store | Option B | Opening widened to 1,600 mm with two 850 mm bypass panels: **750 mm** clear; walk-in store kept |
| VF-05 utility | Option A | MVHR/cylinder moved to the east end; the side-door approach strip is **clear** |
| VF-06 conservatory | Option B | Outline revised: pull-side nib **300 mm**; the 1,200 mm zone beyond the door fits inside |
| VF-07 kitchen to utility | Option B | Pocket sliding door feasible: 850 mm opening, about 810 mm clear. Kitchen-side latch-jamb nib **0 mm** (unresolved, §5.4) |

---

## 1. Preservation (before any change)

| Check | Path | Result |
|---|---|---|
| Draft 0.2.1 manifest (63 entries: 0.2.1 files, evidence, frozen 0.2 / 0.1 / Verification manifests) | `MMUCO_ORION_Duplex_Draft_0.2.1_Manifest.sha256` | **63 / 63 OK** at 20:12:27 |
| Verification manifest (40 entries: issued Draft 0.2, Draft 0.1, Verification package) | `MMUCO_ORION_Duplex_Draft_0.2_Verification_Manifest.sha256` | **40 / 40 OK** |
| Draft 0.1 hashes recorded before any Draft 0.2 work | Session record `draft01.sha256` | **3 / 3 OK** |
| Earlier audit and decision documents (in no manifest) | `Evidence/preservation/earlier_documents_not_in_any_manifest.sha256` | Hashed at start; re-checked at the end (Change Log §6) |
| Working copy | `SCRATCH_not_issued/WORKING_COPY_from_Draft_0.2.1.dxf` | Byte-identical to the issued 0.2.1 DXF (`a64e476e…`). All CAD work used this copy; the issued file was never opened in CAD |

Full log: `Evidence/preservation/start_check.txt` (106 OK lines).

---

## 2. Baseline geometry (MEASURED from the working copy, before any change)

Labelled diagram: `Evidence/01_baseline_geometry/baseline_hallway_geometry.png`. Handles and table: `baseline_hallway_geometry.md`.

| Element | Handle(s) | Geometry |
|---|---|---|
| Hallway | (region) | x 4,400–5,900 × y 300–6,900; narrowest clear width **1,500** (parallel faces, nothing fixed inside) |
| Wall, hall / Room A | 127, 129, 12B (A-WALL-INT, 100) | 127 y 300–2,800; 129 y 3,800–4,300; 12B y 5,300–7,400 |
| Wall, hall / Room B | 131, 133, 135 | 131 y 300–2,800; 133 y 3,800–5,000; 135 y 6,000–6,900 |
| Room A entry (existing) | arc 16E, line 16C | Gap y 2,800–3,800 (1,000); hinge (4,300, 3,800); 1,000 leaf into Room A |
| Room B entry (existing) | arc 176, line 174 | Gap y 2,800–3,800 (1,000); hinge (6,000, 3,800); 1,000 leaf into Room B |
| Other hall doors | 172 (quiet room), 17A (bathroom, opens **into** the hall), 16A (front), 17E (living) | Unchanged in 0.2.2 |
| Room A | (region) | 4.0 × 3.7 m = 14.80 m² (x 300–4,300, y 300–4,000) |
| Room B | (region) | 3.2 × 4.0 m = 12.80 m² (x 6,000–9,200, y 300–4,300) |
| Objects near the entries | 1C2 wardrobe [3,700, 600, 4,300, 2,400]; 1C0 bedside table [2,550, 3,600, 3,000, 4,000]; 1D2 desk [7,200, 3,700, 9,000, 4,300]; 1C6 bed [7,300, 1,325, 9,200, 2,675]; 218 reference turning circle in the hall | — |

---

## 3. Option study (scratch; MEASURED / AUTOMATED CHECK)

**Comparison drawing:** `MMUCO_ORION_Duplex_Draft_0.2.2_Hallway_Option_Comparison.pdf` / `.png`. It is an ISO A2 landscape sheet at 1:50, with page fitting disabled and all content inside the clip box.

**Source:** scratch `OPTION_STUDY_B1_B2_B3.dxf`. **Measurements:** `Evidence/02_option_study/option_study_measurements.json`.

| Test | B1 paired leaves | B2 one leaf each side | B3 two-leaf telescopic pocket |
|---|---|---|---|
| Structural opening (each room) | 1,400 (y 2,500–3,900) | 1,000 (y 2,800–3,800) | 1,400 |
| Leaves | 900 main + 500 secondary, hinged | 1,000 single, hinged | 2 × 725 sliding into one 750 mm pocket |
| Clear opening (ESTIMATE) | 849 main / 1,298 both | 949 | 1,360 |
| Swing or slide collisions | None | None | No swing. The wall must be thickened to about 200 mm over y 1,700–2,500, which **collides with Room A wardrobe 1C2 (0.07 m²)** |
| Hall clear width (closed / operating / open) | 1,500 / 1,500 / 1,500 | 1,500 / 1,500 / 1,500 | 1,500 (thickening goes into the rooms) |
| Room-side approach depth | A 1,300–1,750; B 1,200–3,010 | Same | Same |
| Wall change | Piers shortened 300 (south) and 100 (north) each side | None | Same as B1 plus 100 mm thickening into each room; −0.08 m² per room |
| Double door at each entrance? | **Yes** | **No** (single leaves) | Yes |
| Construction | Two leaves; secondary leaf needs flush bolts (floor socket); head across 1,400 | Standard doorsets | Telescopic gear, double pocket, no fixings on the pocket section, poorer acoustic seal, specialist hardware. A north pocket is impossible (Q1 junction at y 4,000, quiet-room door at 4,300) |
| **Decision** | **SELECTED** | Reference only | **REJECTED** |

**Why B1:**

- It is the only arrangement that gives each room its own unmistakable double entrance with no hall obstruction and no wall thickening or furniture conflict.
- The unequal pair (900 + 500) keeps the everyday leaf above the 800 mm investigation target (849, ESTIMATE). An equal pair (2 × 700) would give only about 649 per leaf.
- Both leaves open give about 1,298 for moving furniture or assisted access.

---

## 4. Implemented B1: door geometry (MEASURED from the saved 0.2.2 DXF)

| Entrance | Leaf (handle) | Width | Hinge | Handing | Closed position | Fully open position | Swing area | Enters hall? | Collisions |
|---|---|---|---|---|---|---|---|---|---|
| Room A | main (arc 25C1, line 25C2) | 900 | (4,300, 3,900) | North jamb; opens west into Room A | (4,300, 3,900)–(4,300, 3,000) | (4,300, 3,900)–(3,400, 3,900) | 0.61 m² | No | None |
| Room A | secondary (25C3 / 25C4) | 500 | (4,300, 2,500) | South jamb; opens west | (4,300, 2,500)–(4,300, 3,000) | (4,300, 2,500)–(3,800, 2,500) | 0.18 m² | No | None |
| Room B | main (25C5 / 25C6) | 900 | (6,000, 3,900) | North jamb; opens east into Room B | (6,000, 3,900)–(6,000, 3,000) | (6,000, 3,900)–(6,900, 3,900) | 0.61 m² | No | None |
| Room B | secondary (25C7 / 25C8) | 500 | (6,000, 2,500) | South jamb; opens east | (6,000, 2,500)–(6,000, 3,000) | (6,000, 2,500)–(6,500, 2,500) | 0.18 m² | No | None |

**Pair geometry (AUTOMATED CHECK):**

- In each pair the leaves meet at y 3,000 and fill the 1,400 mm opening exactly (900 + 500).
- No leaf sweep overlaps any other door's sweep. That covers the opposite entrance and the quiet-room, bathroom, front and living-room doors.

**Dwelling B:** the mirror check shows all 23 door entities match dwelling A's about x 9,300 (handles 25C9–25D0 for B's entries).

**Opening dimensions (associative to wall vertices; values equal the coordinate differences):**

| Chain (inside the hall) | Room A, x 4,700 (25DB / 25DC / 25DD) | Room B, x 5,600 (25DE / 25DF / 25E0) |
|---|---|---|
| Room south boundary (y 300) to opening | 2,200 | 2,200 |
| Opening | 1,400 | 1,400 |
| Opening to room north boundary | 100 (to Q1 at y 4,000) | 400 (to Q7 at y 4,300) |

Dwelling B has the same chains at x 13,900 and 13,000 (25E1–25E6).

---

## 5. Door register VF-04 to VF-07 (implemented as directed)

### 5.1 VF-04 store: Option B, widen the opening and keep the walk-in store

- **Opening:** wall pieces 12B (top moved y 7,400 → 7,100) and 12D (bottom moved 8,400 → 8,700). Opening **1,600 mm** (y 7,100–8,700); mirrored as 12C / 12E in dwelling B.
- **Leaves:** two bypass panels of **850 mm** each (25D1 at x 4,330, y 7,100–7,950; 25D2 at x 4,370, y 7,850–8,700), overlapping by 100 mm.
- **Clear opening** with one panel parked behind the other: **750 mm** (MEASURED geometry). Was 450 in Draft 0.2.1.
- **Walk-in store kept:** 1.4 × 2.0 m = 2.80 m², free floor about 1.0 × 1.6 m. The opening is aligned with the free floor; the south shelving ends at y 7,100.
- **Approach:** free depth on the living-room side 2,200 mm. When the existing hall-to-living door (17E) is open, its sweep overlaps 0.44 m² of the approach zone (operational note).
- **REQUIRES CONFIRMATION:**
  - Whether ADM 2.22 applies to the store (Note 1, "large enough to be entered"). If it does, 750 equals the Table 2.1 figure but is below the 800 investigation target.
  - The double head track within a 100 mm partition (product).

### 5.2 VF-05 utility: Option A, relocate equipment away from the doorway

| Item | Moved from | Moved to |
|---|---|---|
| MVHR / cylinder allowance (1E8, circle 1EA) | x 300–900 | x 2,200–2,800, east end of the south run |
| Worktop 1EC | x 900–2,800 | x 900–2,200 |
| Sink 1AC | [2,200, 6,750, 2,700, 7,200] | [375, 6,725, 875, 7,175], on a new 500 mm-deep sink base 25D9 [300, 6,700, 900, 7,200] |

Mirrored in dwelling B: 1E9, 1EB, 1ED, 1AD and new base 25DA. Labels updated: dwelling A "MVHR / CYL at E end", dwelling B "at W end".

**Results:**

- **AUTOMATED CHECK:** no furniture or equipment in the strip inside the side door (x 300–600, y 7,200–8,200). Was a 100 mm obstruction in 0.2.1.
- The hinged kitchen-to-utility door that used to swing into the utility is removed (see §5.4).

**REQUIRES CONFIRMATION:**

- MVHR duct and cylinder pipework routes to the new position.
- Sink waste route.
- A 500 mm-deep sink base (product).

### 5.3 VF-06 conservatory: Option B, revise the conservatory outline

**Polygon 222** (provisional):

| | Vertices | Area |
|---|---|---|
| Was | (4,500, 12,300) (7,000, 12,300) (7,000, 13,050) (6,250, 13,800) (5,250, 13,800) (4,500, 13,050) | 3.1875 m² |
| Now | (4,400, 12,300) (7,000, 12,300) (7,000, 13,500) (6,700, 13,800) (4,700, 13,800) (4,400, 13,500) | **3.81 m²** |

The bounding box is now 2.6 × 1.5 m with 300 mm chamfers. Mirrored as 223.

**AUTOMATED CHECK:**

- Conservatory door (hinge x 5,700, leading edge x 4,700, opens outward): **pull-side nib 300 mm** (was 200).
- The zone 300 mm nib + door width, 1,200 mm deep beyond the door ([4,400, 12,300] to [5,700, 13,500]), lies **inside** the outline.
- The door swing lies inside the outline.

The conservatory stays **PROVISIONAL**: size, ADO and Part L effects, and planning are unresolved.

### 5.4 VF-07 kitchen to utility: Option B, investigate a pocket sliding door

**Investigation:**

- Q4 runs x 300–2,800 between the west wall and the store-wall T-junction (Q3).
- The kitchen base run starts at x 2,100 on the kitchen side.
- So the opening must end at x ≤ 2,100, and the pocket must lie west of it within a single wall piece (it cannot cross a junction).
- An 850 mm opening with a 900 mm leaf (50 mm overlap) needs a 900 mm pocket: x 350–1,250 fits inside piece 123 (x 300–1,250).
- An east-side pocket is not possible: only 700 mm exists before the Q3 junction.

**Implemented:**

- Wall 123 now x 300–1,250; wall 125 now starts at x 2,100.
- Opening **850 mm** (x 1,250–2,100); pocket cavity 25D5 [350, 8,725, 1,250, 8,775] (900 mm, holds the 900 mm leaf).
- Closed leaf 25D6 at x 1,200–2,100.
- **Clear opening ESTIMATE 810 mm** (opening − 40 mm pull/stop allowance, ASSUMPTION).
- No fixings on the pocket wall section on either side (AUTOMATED CHECK).

**Conflict found (UNRESOLVED, not silently fixed):** the latch-jamb nib on the **kitchen side is 0 mm**, because base unit 1E0 starts at x 2,100. The utility side has 700 mm.

**Options:**

- Accept it, if a nib is not required for a sliding door (REQUIRES CONFIRMATION).
- Shorten the kitchen base run by 300 mm, which is a kitchen design change and would need approval.

**REQUIRES CONFIRMATION:** a pocket-door kit for a 100 mm stud partition (finished thickness); operating force and handle for users with limited grip.

---

## 6. Acceptance tests

Values are mm or m². **PASS** means the measured value meets the stated *investigation* target or check. It is not a compliance finding.

| # | Test | Method | Target | Actual | Status |
|---|---|---|---|---|---|
| S1 | Rooms face each other across the hall | Opening y-ranges compared | Same y-range, opposite walls | Both y 2,500–3,900; walls x 4,300–4,400 and 5,900–6,000 | PASS |
| S2 | Each room has its own distinct entry | Gap analysis | Two separate openings | Separate gaps (jambs 127 / 129 and 131 / 133), 1,500 apart | PASS |
| S3 | Openings dimensioned to room boundaries | Chains anchored to wall vertices | Break points = room faces and jambs | 300 / 2,500 / 3,900 / 4,000 (A) and 4,300 (B); values = coordinate differences | PASS |
| S4 | Hall continuous and not blocked by the entry doors | Swing sweep in the hall | 0 intrusion | 0 (all leaves open into rooms) | PASS |
| D1 | Structural opening and clear opening recorded separately | Gap; leaf − 51 | Recorded | 1,400 structural; 849 / 1,298 clear (ESTIMATE) | PASS (recorded) |
| D2 | Main-leaf clear opening ≥ 800 (investigation target) | leaf − 51 | ≥ 800 | 849 (ESTIMATE) | PASS (estimate); **REQUIRES CONFIRMATION** with a door schedule |
| D3 | Leaf widths, handing, swing arcs, open and closed positions | DXF entities | Recorded | §4 table | PASS (recorded) |
| D4 | Collisions: leaves × walls, furniture, fittings, opposite entrance, other doors | Sweep sampling (25 mm) | None | None | PASS |
| D5 | Handles and door furniture collisions | — | — | Hardware not drawn | **NOT TESTED** |
| D6 | Sliding and pocket doors: track and pocket shown with construction space | DXF entities | Shown | Store bypass panels (double track); pocket 25D5 900 mm | PASS (drawn); construction **REQUIRES CONFIRMATION** |
| D7 | Entrances distinguishable on plan | Visual (crops 02 / 03) | Clear | Two double-leaf symbols facing across the hall | PASS (visual) |
| C1 | Hall narrowest clear width, doors closed | Section sampling | Record | 1,500 | PASS (recorded) |
| C2 | Hall narrowest clear width in the entry zone, doors operating or open | Section sampling | No reduction | 1,500 / 1,500 | PASS |
| C3 | Hall narrowest anywhere, existing doors operating or open | Section sampling | Record | About 415 (front door mid-swing, y 325, transient); 500 (bathroom door 17A open, y 6,000) | Recorded; **existing condition (DR-04), unchanged** |
| C4 | Approach space both sides of each entrance | Rays from the opening | Record | Hall side 1,500 × 1,400; room side A 1,300–1,750, B 1,200–3,010 | PASS (recorded) |
| C5 | Minimum hallway width or door clearance requirement | — | — | Not invented. ADM 2.22a (900 hall) and Table 2.1 are quoted only as references | **REQUIRES CONFIRMATION** |
| A1 | Room and hall area changes | Flood-fill regions | Recorded | Room A 14.80, Room B 12.80, hall 9.90: **0 change** | PASS |
| A2 | Areas recalculated from actual polylines | Blind parser | Residual 0 | Footprint 228.78 = 2 × 104.13 + 18.06 + 2.46; residual 0 mm² | PASS |
| A3 | No unintended gaps, overlaps, duplicate walls, invalid openings | Blind parser | 0 / 0 / 0 | 0 overlaps; 0 free ends; 36 openings, all bounded by wall pieces | PASS |
| A4 | Unrelated rooms, openings, furniture unchanged | Entity diff 0.2.1 → 0.2.2 | Only intended changes | 442 identical. Changes limited to the listed doors, walls, utility items, conservatory and annotation (Change Log) | PASS |
| G1 | DXF reopens and is editable | CADCraft reopen | No warnings | 533 entities, no warnings | PASS |
| G2 | Dimension associations | xdata audit | No provisional or non-wall anchors | 89 / 90 points on wall vertices; 1 static (2C7, party-wall centreline) | PASS |
| G3 | Moving provisional or unrelated geometry changes no building dimension | Move 272 non-wall entities | 0 changed | 0 / 45 | PASS |
| G4 | Associations live (positive control) | Move Q1 and Q7 +100 | Anchored dimensions update | 5 dimensions updated correctly (e.g. 100 → 200, 400 → 500) | PASS |
| P1 | PDF at true 1:50, page fitting disabled | Vector measurement (width, depth, scale bar) | 1:50 ± 0.5 % | 1:50.000 / 1:50.000 / 1:50.000 | PASS |
| P2 | PNG from the verified PDF, same drawing, scale consistent | Two renders; pixel measurement | Identical; ± 0.5 % | Renders identical (`7a60da12…`); 1:49.90–1:49.94 | PASS |
| P3 | Labels, dimension text, door symbols legible | Visual + text-box test | No new clashes in door areas | 6 new minor crossings: the two Room A "2,200" labels cross the dashed reference turning circle; four "100" / "400" labels cross their own extension lines (existing VF-08 pattern) | PASS with minor findings |
| M1 | Mirror symmetry kept | Entity mirror test | All matched | 161 / 161; doors 23 / 23 | PASS |
| R1 | Bed zones, bathroom zones, kitchen clearance unchanged | DXF-only accessibility checks | Identical to 0.2.1 | Identical; 750 mm routes reach every bedroom window | PASS |

---

## 7. Area and geometry changes (MEASURED)

| Item | Draft 0.2.1 | Draft 0.2.2 | Change |
|---|---|---|---|
| Room A (Bedroom 1) | 14.80 | 14.80 | 0 |
| Room B (Bedroom 2) | 12.80 | 12.80 | 0 |
| Hall | 9.90 | 9.90 | 0 |
| All 18 rooms, NIFA per dwelling | 100.10 | 100.10 | 0 |
| Drawn partition polygons per dwelling | 3.150 | 3.025 | −0.125 (wider openings) |
| Door and opening zones in partition lines per dwelling | 0.880 | 1.005 | +0.125 |
| Partitions including opening zones; GIA | 4.03; 104.13 | 4.03; 104.13 | 0 |
| Footprint | 228.78 | 228.78 | 0 |
| Conservatory (provisional, outside GIA) | 3.1875 | 3.81 | +0.6225 |

Full reconciliation: `Evidence/03_geometry_areas_dimensions/area_reconciliation_022.csv` (41 rows; all 32 comparable rows agree with the 0.2.2 Room Schedule).

---

## 8. Accessibility, safety and construction review (REQUIRES CONFIRMATION throughout)

**Accessibility (ADM Vol 1):**

- M4(2) applies only where a planning condition requires it (para 0.3); it is the project target, not a confirmed requirement.
- **2.22c / Table 2.1:** with a 1,500 mm hall (not head-on approach) the doorway clear-opening figure is 750 mm. The main leaf is about 849 (ESTIMATE). Confirm with the door schedule, measured per Diagram 2.2.
- **2.22d / Table 2.1 Note 2:** "Double doors effectively provide nibs where each leaf is at least 300mm wide". The leaves are 900 and 500. Whether this applies to these internal pairs needs confirmation. Measured wall beside the jambs:
  - Room A: 100 mm north (to Q1) and 100 mm south (to the wardrobe).
  - Room B: 400 mm north and 2,200 mm south.
- **2.25:** bed zones and 750 mm routes are unchanged and still met geometrically.
- **Thresholds:** internal doors are assumed level. A secondary leaf usually needs flush bolts with a floor keep; the floor socket must not create a trip or wheel obstruction. Specify a flush dust-proof socket or automatic bolts.
- **Manoeuvring:** the reference turning circle in the hall is unaffected. Both leaves open give about 1,298 for assisted wheelchair transfer and furniture.

**Fire (ADB Vol 1):**

- Escape from ground-storey bedrooms: escape windows, or a hall leading to a final exit.
- Whether any internal door must be a fire door in this single-storey dwelling. Double doors with meeting stiles are harder to make fire- or smoke-resisting if that is ever required.
- The pocket and bypass doors are not suitable as fire doors without specific products.

**Sound (ADE):**

- Wider openings mean bedroom privacy relies more on the doors.
- The meeting stile needs a seal.
- Confirm the internal sound provisions for bedroom walls (Part E, E2) and how doors are treated.

**Structure and construction:**

- Head and lintel over the 1,400 mm openings in 100 mm partitions.
- The 1,600 mm store head carries a double bypass track.
- A pocket-door frame in a 100 mm partition: no fixings on the pocket section, access for maintenance.
- All partition build-ups are still PROVISIONAL (300 / 200 / 100).

**Services (VF-05):** MVHR duct and cylinder pipework re-routing; sink waste to the west end.

---

## 9. Unresolved questions (carried forward)

1. Pocket door (VF-07): kitchen-side latch-jamb nib is 0 mm. Accept for a sliding door, or shorten the kitchen base run by 300 mm? **Decision needed.**
2. Store (VF-04): does 2.22 apply? If so, is 750 mm acceptable, below the 800 investigation target?
3. Double-door leaf sizes and handing, flush-bolt and threshold detail, and the door schedule for the 849 / 1,298 clear-opening estimates.
4. Whether the "Face Me and I Face You" pairing should also apply to other rooms. This issue applied it to the only directly opposing pair (Bedroom 1 / Bedroom 2).
5. The bathroom door (17A) still opens into the hall: 500 mm left when fully open (existing DR-04, unchanged).
6. Fire-door, acoustic and structural questions in §8.
7. Every open item in the Verification Register (PA / SI / RQ / DR) and VF-08 to VF-16. Of these, the patio and conservatory visibility is unchanged or improved, and the new minor label crossings are listed in §6 P3.

**Register status:** the hallway arrangement is recorded as an **additional design resolution item, "HALL-01 (proposed ID)"**. It is not an existing VF item, has not been formally approved, and existing items were not renumbered.

---

## 10. Deviations from the stated design intent

- **Unequal pair (900 + 500), not equal leaves.** Chosen because an equal pair (about 700 each) would give an estimated 649 mm per leaf, below the 800 investigation target for everyday single-leaf use.
- **Pairing applied to Bedroom 1 and Bedroom 2 only.** The quiet-room and bathroom entries stay single, offset doors.
- **VF-07 kitchen-side nib of 0 mm.** Recorded as unresolved rather than forced (§5.4).
- **Hall annotation moved.** The HALL labels moved 650 to 690 mm north to clear the new opening dimensions. Room labels and areas are otherwise unchanged.
- **Notes and dimension key text updated.** These now carry the Draft 0.2.2 door and conservatory changes (Change Log §4).

No requirement of the design principle was knowingly traded away. The two rooms visibly and functionally face each other across a continuous, unobstructed 1,500 mm hall, and each has its own double entrance.
