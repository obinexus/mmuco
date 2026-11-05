# MMUCO ORION Draft 0.2.2: VF-07 kitchen-side nib investigation

**Status: SCRATCH INVESTIGATION FOR REVIEW. NOT AN ISSUE, NOT APPROVED, NOT A COMPLIANCE ASSESSMENT.**

- Draft 0.2.2 and every earlier frozen file are unchanged; see section 2 for the hash checks.
- No Draft 0.2.3 has been created.
- The options exist only as scratch DXFs in `MMUCO_ORION_Duplex_Draft_0.2.2_VF07_SCRATCH_not_issued/`.
- Regulatory readings are marked **REQUIRES CONFIRMATION**.

Evidence labels used throughout:

| Label | Meaning |
|---|---|
| MEASURED | Read from a saved DXF by script |
| ESTIMATE | Derived from measured geometry by a stated rule |
| ASSUMPTION | A value chosen here, not sourced |
| REQUIRES CONFIRMATION | Needs a professional or the building control body (BCB) |

---

## 1. Summary

**The problem (MEASURED, Draft 0.2.2):**

- The kitchen–utility pocket door has an 850 mm structural opening (x 1,250–2,100 in partition Q4).
- Its clear opening is an ESTIMATE of 810 mm, in a range of 770–810 depending on linings and pull.
- On the kitchen face, base unit 1E0 starts exactly at the latch jamb (x 2,100), so the clear nib there is **0 mm**.
- On the utility face the nib is 700 mm, to wall 121.

**Which requirement governs: not established.**

- No planning condition imposing M4(2) is known (RQ-01 is open), so M4(1) is the default under ADM Vol 1 para 0.3.
- M4(2) is the project's design target, not a confirmed requirement.
- M4(1) has no nib provision, so the 0 mm nib is a regulatory issue only if M4(2) is imposed. **REQUIRES CONFIRMATION.**

**What was measured:**

- Four scratch options, plus the baseline.
- A sweep of every possible pocket-door position along Q4.

| Option | What it does | Kitchen-side nib at the latch | Kitchen change | Other change |
|---|---|---|---|---|
| **A** | Shorten base run 1E0 by 300 mm at its west end; pocket door as issued | **300** (zone 2,600 deep) | One 600 unit becomes 300 (run 2,200 → 1,900) | None |
| B | Move the opening west and reverse the pocket east; still needs the same 300 mm cut | 300, but the zone is only 600 deep (tall units) | Same as A | Q4 rebuilt; kitchen approach depth falls from 2,600 to 600 over 300 mm of the opening; pocket section crosses the MVHR line by 200 mm |
| C1 | Single hinged 826 mm leaf opening into the utility | 0, but the kitchen face becomes the **push** face; pull face (utility) 700 | None | Opening +50 mm; door swing takes 0.54 m² of utility floor |
| C2 | Unequal pair 826 + 350 opening into the kitchen | Paired-door NOTE 2 wording met (both leaves ≥ 300) | None | Opening +400 mm; open main leaf has 37 mm behind it to unit 1E0; swing 0.64 m² in the kitchen |

**Sweep result (MEASURED / ASSUMPTION):**

- **No pocket-door position on Q4 gives a kitchen-side nib of 300 mm or more without cutting the base run.**
- Keeping the 850 mm opening, the smallest cut is 300 mm, whichever side the pocket is on. That is Option A.
- A smaller cut needs a narrower opening:
  - 800 mm opening: 200 mm cut, but the clear opening falls to an ESTIMATE of 720–760.
  - 750 mm opening: 100 mm cut, clear 670–710.

**Recommendation for review: Option A.**

- It keeps the pocket door (the VF-07 direction).
- It gives a measured 300 mm clear nib on the kitchen face and 700 mm on the utility face, so it does not depend on how "leading edge" is read for a sliding door.
- Walls, door, services, room areas and approach space are unchanged.
- The cost is one 600 mm base unit becoming a 300 mm unit.
- C1 is the fallback if the full base run matters more than the pocket door. It depends on the push-face reading (RQ-03).
- B and C2 are not recommended (section 11).

---

## 2. Preservation and working method

**Start check:** `evidence/preservation_start.txt`, 2026-10-24 20:39.

| Manifest or record | Entries | Result |
|---|---|---|
| Draft 0.2.2 manifest (covers 0.2.2, its evidence, 0.2.1, 0.2, Draft 0.1, Verification manifests) | 80 | 80 OK |
| Draft 0.2.1 manifest | 63 | 63 OK |
| Verification manifest | 40 | 40 OK |
| Draft 0.1 record | 3 | 3 OK |
| Earlier documents (not in any manifest) | 5 | 5 OK |

**Working copy:**

- `WORKING_COPY_from_Draft_0.2.2.dxf` is a byte copy of the issued DXF (SHA-256 2ec8d3f3…).
- Each option was built by opening the working copy in CADCraft, editing it and saving under a **new** filename. The working copy was never saved over.

**End check:** `evidence/preservation_end.txt`. Its result is reported in section 13.

**Dwelling A only:**

- Dwelling B (mirror, x′ = 18,600 − x) was not changed in any scratch file.
- The whole-drawing entity diffs show no dwelling-B entity changed (section 5).

---

## 3. Which requirement applies (checked before any ADM provision was used)

Source: `ADM1.txt`, the text of Approved Document M Volume 1 (2015 edition) held with the project research. Whether that edition and its amendments are current: **REQUIRES CONFIRMATION**.

### 3.1 How the category is set

- **Para 0.3:** M4(2) and M4(3) are optional requirements. They apply only where a planning condition imposes them; otherwise dwellings need only meet M4(1). Each dwelling is assessed against one category only.
- **Para 2.18:** Section 2B (M4(2)) applies only where a planning condition requires M4(2).
- **Project status:**
  - No site or planning condition is known; the register records RQ-01 as OPEN.
  - The approved C2 baseline uses M4(2) as a design target.
  - **So the governing category is not established. Default M4(1); M4(2) only if conditioned. REQUIRES CONFIRMATION** (planning adviser).

### 3.2 If M4(1) governs

- **1.15a:** every door to a habitable room, and to the room containing the WC, needs a minimum clear opening width as in Table 1.1.
  - Table 1.1 gives 750 mm with a head-on approach and a 900 mm corridor, or 750/775/800 mm with 1,200/1,050/900 mm corridors when the approach is not head-on.
  - Measurement is to Diagram 1.1.
- **Appendix A:** a habitable room includes a kitchen but **not a utility room**.
  - Whether 1.15a covers a door between a kitchen and a utility: **REQUIRES CONFIRMATION.**
- **Section 1B contains no nib provision.**
  - Under M4(1) the 0 mm kitchen-side nib is a design-quality question, not a regulatory one. **REQUIRES CONFIRMATION.**

### 3.3 If M4(2) governs

- **2.22c:** every door has a minimum clear opening width as in Table 2.1, which has the same values as Table 1.1.
- **2.22d:** a minimum 300 mm nib to the *leading edge* of every door within the entrance storey.
  - The dwelling is single-storey, so every door is in the entrance storey (Draft 0.2 Report).
  - Appendix A defines the leading edge as the surface facing the room into which the door opens, "sometimes referred to as 'the pull side'".
- **Diagram 2.3, Note 1:** the 300 mm nib is only required where the door opens inward (shown dotted). This is consistent with a pull-side-only reading for hinged doors. **REQUIRES CONFIRMATION** (RQ-03).
- **2.22 NOTE 2:** "Double doors effectively provide nibs where each leaf is at least 300mm wide."
  - This is about double (paired) doors. It is **not** applied to the single-leaf pocket door anywhere in this study.
- **Sliding and pocket doors are not addressed.**
  - A sliding leaf does not open "into" either room, so the pull side is undefined.
  - Whether 2.22d applies to one face, both faces or neither: **REQUIRES CONFIRMATION** (BCB or access consultant).
  - This study measures both faces at the latch jamb.

---

## 4. Baseline geometry (Draft 0.2.2), with handles and coordinates (MEASURED)

**Sources:**

- `evidence/01_baseline_geometry/01_baseline_entities_kitchen_utility.json`: 117 entities in x 0–4,700, y 6,400–12,300, read straight from the DXF.
- `evidence/02_measurements/measure_0_BASELINE.json`

Coordinates are in mm. The origin is at the west and front outer faces; north is +y.

| Element | Handle | Coordinates | Notes |
|---|---|---|---|
| Kitchen (room) | — | [300, 8,800, 4,300, 12,000], 4.0 × 3.2 = 12.80 m² | Independent parser region |
| Utility (room) | — | [300, 6,700, 2,800, 8,700], 2.5 × 2.0 = 5.00 m² | |
| Partition Q4, kitchen/utility, west piece | 123 | [300, 8,700, 1,250, 8,800] | 100 mm thick (PROVISIONAL). Holds the pocket |
| Partition Q4, east piece | 125 | [2,100, 8,700, 4,300, 8,800] | Starts at the latch jamb |
| Opening | — | x 1,250–2,100, **850 structural** | Gap between 123 and 125 |
| Pocket cavity | 25D5 | [350, 8,725, 1,250, 8,775], 900 long | Inside 123 only |
| Pocket leaf (closed) | 25D6 | (1,200, 8,750)–(2,100, 8,750), 900 | 50 mm overlap into the cavity |
| Latch jamb | — | x 2,100 | Pocket jamb at x 1,250 |
| Clear opening | — | **ESTIMATE 810** (850 − 40, 0.2.2 ASSUMPTION); range 770–810 if linings and pull take 40–80 | Not the nominal 850 |
| Kitchen base run (south) | 1E0 | [2,100, 8,800, 4,300, 9,400], 2,200 × 600 | Dividers 1E2/1E4/1E6 at x 2,700/3,300/3,900 → units 600/600/600/400 |
| Tall units incl. 2 larders | 1DE | [300, 9,400, 900, 11,400] | Front face x 900; south end 600 mm from Q4 |
| Rear run | 1DC | [300, 11,400, 4,300, 12,000] | |
| Kitchen sink (plumbing) | 19E / bowl 1A0 | [1,650, 11,500, 2,450, 11,900] | On the rear (north) wall under window 15C. Not on Q4 |
| Hob | 1A2 (rings 1A4/1A6/1A8/1AA) | [3,300, 11,450, 3,900, 11,950] | Rear wall |
| Utility sink base / sink | 25D9 / 1AC | [300, 6,700, 900, 7,200] / [375, 6,725, 875, 7,175] | On Q2 (south) and the west wall. Not on Q4 |
| Washer / dryer | 1AE / 1B2 (drums 1B0/1B4) | [900, 6,700, 1,500, 7,300] / [1,500, 6,700, 2,100, 7,300] | Under worktop 1EC [900, 6,700, 2,200, 7,300] |
| MVHR / cylinder allowance | 1E8 (circle 1EA) | [2,200, 6,700, 2,800, 7,300] | Ventilation and hot water. Duct and pipe routes **not drawn** |
| Utility side door | arc 186, leaf 184 | West wall, opening y 7,200–8,200, opens outward | |
| Utility/store partition Q3 | 121 | [2,800, 6,700, 2,900, 8,700] | T-junction with Q4 at x 2,800–2,900, utility side |
| Q5 (kitchen/living) | 12D, 12F | [4,300, 8,700, 4,400, 9,200], [4,300, 11,000, 4,400, 12,000] | Open gap y 9,200–11,000 to living/dining |
| West external wall | 106 | [0, 8,200, 300, 9,800] | Inner face x 300 |
| Dimensions on Q4 | 1471, 1472, 1473 | Anchored to 123 vertices 0 and 3 (x 300) | None of the options moves these vertices |

**Measured conditions:**

| Condition | Kitchen side | Utility side |
|---|---|---|
| Nib at the latch jamb | **0** (unit 1E0); wall nib 2,200 (to Q5 wall 12D) | 700 (to wall 121); zone 300 × 1,400 deep |
| Approach depth in front of the opening | 2,600 | 1,400 |
| Nib at the pocket jamb (closing pull) | 950 | 950 |

- No fixings on the pocket section and no wall junction on it.
- No services drawn in Q4.
- No electrical layout is drawn.

**Observation outside the VF-07 scope (OBS-1, not changed here):**

- Tall units 1DE (x 300–900, y 9,400–11,400) stand in front of the whole of the west kitchen window 14A (y 9,800–11,000).
- Sill and head heights are not in the plan.
- Recorded for review only.

---

## 5. Options as drawn (scratch DXFs) and what changed

The whole-drawing entity diffs (`evidence/06_entity_diffs/`, ver_diff.mjs, by handle) show each option changes only the intended entities. The wall hatches follow their walls (associative). No dimension, text or dwelling-B entity changed.

| Option | Scratch file | Edits (CADCraft) | Diff result |
|---|---|---|---|
| A | `VF07_OPTION_A_shorten_base_run.dxf` | `pedit` 1E0 vertices 0 and 3 to x 2,400 | 1 changed (1E0) |
| B | `VF07_OPTION_B_move_opening_reverse_pocket.dxf` | 123 vertices 1–2 to x 600; 125 vertices 0 and 3 to x 1,450; 25D5 moved +1,100; 25D6 moved −600; 1E0 to x 2,400 | 7 changed (123, 125, 1E0, 25D5, 25D6, hatches 2A0, 2A2) |
| C1 | `VF07_OPTION_C1_hinged_single_leaf.dxf` | Erase 25D5 and 25D6; 123 vertices 1–2 to x 1,200; arc 47EB (hinge 1,237, 8,700, r 826, 270–360°), leaf 47EC | 2 changed, 2 removed, 2 added |
| C2 | `VF07_OPTION_C2_unequal_pair.dxf` | Erase 25D5 and 25D6; 123 vertices 1–2 to x 850; arc 47EB (hinge 2,063, 8,800, r 826, 90–180°) and leaf 47EC; arc 47ED (hinge 887, 8,800, r 350, 0–90°) and leaf 47EE | 2 changed, 2 removed, 4 added |

**Door-set assumptions for C1 and C2 (ASSUMPTION):**

- A standard 826 mm leaf (deemed 775 mm clear by ADM Table 1.1/2.1 NOTE 3) is drawn with 37 mm frame/lining zones each side.
- That gives a 900 mm structural opening for one leaf, and 1,250 mm for 826 + 350.
- Door-set sizes are not from a door schedule.

---

## 6. Measured option table

Generated by `gen_table.mjs` from the measurement, collision and diff JSON. The same table, with a "basis" column, is in `MMUCO_ORION_Duplex_Draft_0.2.2_VF07_Option_Table.csv`.

**Nib definitions (all in mm):**

- **Clear nib:** along the wall face, from the structural jamb to the first wall **or fixed unit** within 600 mm of the face.
- **Wall nib:** to the first perpendicular wall.
- Frames are not drawn. The ADM measures nibs to the inside edge of the door frame (Diagram 2.2 note 2), so every nib here **understates** the ADM nib by the lining thickness.

| Measure | Baseline (0.2.2) | A | B | C1 | C2 |
|---|---|---|---|---|---|
| Door type | single-leaf pocket sliding door | single-leaf pocket sliding door | single-leaf pocket sliding door | single hinged leaf | pair of hinged leaves (826 + 350) |
| Q4 wall pieces (handle [x1,y1,x2,y2]) | 123 [300,8700,1250,8800]; 125 [2100,8700,4300,8800] | 123 [300,8700,1250,8800]; 125 [2100,8700,4300,8800] | 123 [300,8700,600,8800]; 125 [1450,8700,4300,8800] | 123 [300,8700,1200,8800]; 125 [2100,8700,4300,8800] | 123 [300,8700,850,8800]; 125 [2100,8700,4300,8800] |
| Structural opening x / width (mm) | x 1,250-2,100 / 850 | x 1,250-2,100 / 850 | x 600-1,450 / 850 | x 1,200-2,100 / 900 | x 850-2,100 / 1,250 |
| Leaf or leaves (mm) | 25D6: 900 (closed x 1,200-2,100) | 25D6: 900 (closed x 1,200-2,100) | 25D6: 900 (closed x 600-1,500) | 47EB: 826 hinge (1,237, 8,700) into utility | 47EB: 826 hinge (2,063, 8,800) into kitchen; 47ED: 350 hinge (887, 8,800) into kitchen |
| Pocket cavity | 25D5 x 350-1250 (900), west of opening, in single wall piece 123: yes; holds leaf: yes | 25D5 x 350-1250 (900), west of opening, in single wall piece 123: yes; holds leaf: yes | 25D5 x 1450-2350 (900), east of opening, in single wall piece 125: yes; holds leaf: yes | none (pocket removed) | none (pocket removed) |
| Frame / lining zone each side (mm) | inside the 40 mm allowance below | inside the 40 mm allowance below | inside the 40 mm allowance below | W 37, E 37 | W 37, E 37 |
| Clear opening (mm) | 810 (range 770-810) | 810 (range 770-810) | 810 (range 770-810) | 775 | main leaf alone 775; both leaves 1,074 |
| Clear-opening basis | structural - 40 (0.2.2 ASSUMPTION); range structural - 80 to - 40 (ASSUMPTION) | structural - 40 (0.2.2 ASSUMPTION); range structural - 80 to - 40 (ASSUMPTION) | structural - 40 (0.2.2 ASSUMPTION); range structural - 80 to - 40 (ASSUMPTION) | leaf - 51 (ADM Table 1.1 / 2.1 NOTE 3 analogy) | leaf - 51 (ADM Table 1.1 / 2.1 NOTE 3 analogy) |
| Pull (leading-edge) face | none defined (sliding); both faces measured | none defined (sliding); both faces measured | none defined (sliding); both faces measured | utility | kitchen |
| Kitchen-face nib at latch / leading edge (mm) | east of jamb x 2,100: clear 0 (limited by unit 1E0); wall nib 2,200 (to wall 12D) | east of jamb x 2,100: clear 300 (limited by unit 1E0); wall nib 2,200 (to wall 12D) | west of jamb x 600: clear 300 (limited by wall 106); wall nib 300 (to wall 106) | PUSH east of jamb x 2,100: clear 0 (limited by unit 1E0); wall nib 2,200 (to wall 12D) | west of jamb x 850: clear 550 (limited by wall 106); wall nib 550 (to wall 106) / east of jamb x 2,100: clear 0 (limited by unit 1E0); wall nib 2,200 (to wall 12D) |
| Kitchen-face nib zone (width x clear depth, mm) | no zone (nib 0) | 300 x 2,600 (limited by unit 1DC) | 300 x 600 (limited by unit 1DE) | no zone (nib 0) | 300 x 600 (limited by unit 1DE) / no zone (nib 0) |
| Utility-face nib at latch / leading edge (mm) | east of jamb x 2,100: clear 700 (limited by wall 121); wall nib 700 (to wall 121) | east of jamb x 2,100: clear 700 (limited by wall 121); wall nib 700 (to wall 121) | west of jamb x 600: clear 300 (limited by wall 106); wall nib 300 (to wall 106) | PULL east of jamb x 2,100: clear 700 (limited by wall 121); wall nib 700 (to wall 121) | push face (not measured as a leading edge) |
| Utility-face nib zone (width x clear depth, mm) | 300 x 1,400 (limited by unit 1EC) | 300 x 1,400 (limited by unit 1EC) | 300 x 1,500 (limited by unit 25D9) | 300 x 1,400 (limited by unit 1EC) | - |
| Pocket-jamb nibs (closing pull), K / U (mm) | kitchen 950 / utility 950 | kitchen 950 / utility 950 | kitchen 950 / utility 1,350 | - | - |
| Paired leaves: each leaf >= 300 (ADM 2.22 NOTE 2 wording) | - | - | - | - | yes: 826 and 350; meet at x 1,237/1,237 |
| Paired leaves: clear depth in front of the other leaf (mm) | - | - | - | - | for 826 leaf: 350 leaf zone x 887-1,237, min depth 600 / for 350 leaf: 826 leaf zone x 1,237-2,063, min depth 2,600 |
| Approach depth in front of opening, kitchen (mm) | 2,600 [x 1250-2100: 2600] | 2,600 [x 1250-2100: 2600] | 600 [x 600-900: 600; x 900-1450: 2600] | 2,600 [x 1200-2100: 2600] | 600 [x 850-900: 600; x 900-2100: 2600] |
| Approach depth in front of opening, utility (mm) | 1,400 [x 1250-2100: 1400] | 1,400 [x 1250-2100: 1400] | 1,400 [x 600-900: 1500; x 900-1450: 1400] | 1,400 [x 1200-2100: 1400] | 1,400 [x 850-900: 1500; x 900-2100: 1400] |
| 1,200 mm deep clear band across whole opening (K / U) | yes (x 900-2,100) / yes (x 300-2,800) | yes (x 900-2,400) / yes (x 300-2,800) | no / yes (x 300-2,800) | yes (x 900-2,100) / yes (x 300-2,800) | no / yes (x 300-2,800) |
| Door swing collisions | n/a (sliding) | n/a (sliding) | n/a (sliding) | 47EB: none | 47EB: none; 47ED: none |
| Open leaf: clearance behind it (mm) | n/a | n/a | n/a | 826 leaf: >600 | 826 leaf: 37; 350 leaf: 587 |
| Door swing area (m2) | 0 (sliding) | 0 (sliding) | 0 (sliding) | kitchen 0; utility 0.536 | kitchen 0.636; utility 0 |
| Kitchen base run 1E0 | x 2,100-4,300, 2,200 long; units 600/600/600/400 | x 2,400-4,300, 1,900 long; units 300/600/600/400 | x 2,400-4,300, 1,900 long; units 300/600/600/400 | x 2,100-4,300, 2,200 long; units 600/600/600/400 | x 2,100-4,300, 2,200 long; units 600/600/600/400 |
| Base runs along walls (rear 1DC + south 1E0, mm) | 6,200 | 5,900 | 5,900 | 6,200 | 6,200 |
| ADM 2.24b clear: tall units to base-run end / rear to south run (mm) | 1,200 / 2,000 | 1,500 / 2,000 | 1,500 / 2,000 | 1,200 / 2,000 | 1,200 / 2,000 |
| Kitchen room area / free floor (m2) | 12.80 / 7.88 | 12.80 / 8.06 | 12.80 / 8.06 | 12.80 / 7.88 | 12.80 / 7.88 |
| Utility room area / free floor (m2) | 5.00 / 3.56 | 5.00 / 3.56 | 5.00 / 3.56 | 5.00 / 3.56 | 5.00 / 3.56 |
| GIA dwelling A / partitions / internal opening zones (m2) | 104.13 / 3.025 / 1.005 | 104.13 / 3.025 / 1.005 | 104.13 / 3.025 / 1.005 | 104.13 / 3.020 / 1.010 | 104.13 / 2.985 / 1.045 |
| Area reconciliation residual (mm2) | 0 | 0 | 0 | 0 | 0 |
| Fixings on pocket section / junctions on it | none / none | none / none | none / none | - | - |
| Pocket section overlap with MVHR/cylinder 1E8 line (mm) | 0 | 0 | 200 | - | - |
| Services moved (sinks 19E/1AC, hob 1A2, washer 1AE, dryer 1B2, MVHR/cyl 1E8) | - | none | none | none | none |
| Collision sweep (furniture/walls/doors) | NO COLLISIONS | NO COLLISIONS | NO COLLISIONS | NO COLLISIONS | NO COLLISIONS |
| Entities changed vs Draft 0.2.2 | - | changed 1 [1E0:LWPOLYLINE:A-FURN]; removed 0; added 0 | changed 7 [2A2:HATCH:A-WALL-INT, 2A0:HATCH:A-WALL-INT, 123:LWPOLYLINE:A-WALL-INT, 125:LWPOLYLINE:A-WALL-INT, 1E0:LWPOLYLINE:A-FURN, 25D5:LWPOLYLINE:A-DOOR, 25D6:LINE:A-DOOR]; removed 0; added 0 | changed 2 [2A0:HATCH:A-WALL-INT, 123:LWPOLYLINE:A-WALL-INT]; removed 2 [25D5:LWPOLYLINE, 25D6:LINE]; added 2 [47EB:ARC, 47EC:LINE] | changed 2 [2A0:HATCH:A-WALL-INT, 123:LWPOLYLINE:A-WALL-INT]; removed 2 [25D5:LWPOLYLINE, 25D6:LINE]; added 4 [47EB:ARC, 47EC:LINE, 47ED:ARC, 47EE:LINE] |

---

## 7. Collision checks

Source: `evidence/03_collisions/`, collisions.mjs, region x 0–4,400, y 6,600–12,000, 10 mm sampling.

**Checks run:**

- Fixed units against walls.
- Fixed units against each other.
- Every door swing (arc sector) against walls and units.
- The sliding leaf, closed and open, against walls and units outside its cavity.

| State | Furniture in walls | Furniture overlaps | Door swings | Sliding leaf | Result |
|---|---|---|---|---|---|
| Baseline | 0 | 0 | 186: none | Closed x 1,200–2,100, open x 350–1,250 (inside cavity): none | No collisions |
| A | 0 | 0 | 186: none | As baseline: none | No collisions |
| B | 0 | 0 | 186: none | Closed x 600–1,500, open x 1,450–2,350 (inside cavity): none | No collisions |
| C1 | 0 | 0 | 186, 47EB: none | — | No collisions |
| C2 | 0 | 0 | 186, 47EB, 47ED: none; leaf-to-leaf overlap 0 | — | No collisions |

**Positive control:**

- The same check was run on a copy of C1 with the leaf radius set to 1,600 mm.
- It reported collisions with wall 121 (0.0070 m²) and worktop 1EC (0.0989 m²), so the check can detect a clash.
- File: `positive_control_C1_leaf_radius_1600.json`.

**Near-misses the swing check does not count as collisions (MEASURED):**

- **C2:** the open 826 leaf lies 37 mm from the end of unit 1E0. Leaf thickness is not drawn; a 40–44 mm leaf (ASSUMPTION) would bear on the unit before reaching 90°.
- **C2:** when open, the main leaf projects 226 mm beyond the base-run front line (y 9,626 against 9,400).
- **C2:** the 350 leaf's zone (x 887–1,237) overlaps the tall-unit line (x 900) by 13 mm. This is where its minimum clear depth of 600 comes from; the other 337 mm of that zone is 2,600 deep.

---

## 8. Room areas (MEASURED, independent DXF parser)

| | Baseline | A | B | C1 | C2 |
|---|---|---|---|---|---|
| Kitchen room (m²) | 12.80 | 12.80 | 12.80 | 12.80 | 12.80 |
| Kitchen fixed-unit footprint / free floor (m²) | 4.92 / 7.88 | 4.74 / 8.06 | 4.74 / 8.06 | 4.92 / 7.88 | 4.92 / 7.88 |
| Kitchen door-swing area (m²) | 0 | 0 | 0 | 0 | 0.636 |
| Utility room (m²) | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 |
| Utility free floor (m²) | 3.56 | 3.56 | 3.56 | 3.56 | 3.56 |
| Utility door-swing area (m²) | 0 | 0 | 0 | 0.536 (15 % of free floor) | 0 |
| GIA, dwelling A (m²) | 104.13 | 104.13 | 104.13 | 104.13 | 104.13 |
| Partition polygons / internal opening zones (m²) | 3.025 / 1.005 | 3.025 / 1.005 | 3.025 / 1.005 | 3.020 / 1.010 | 2.985 / 1.045 |
| Reconciliation residual (mm²) | 0 | 0 | 0 | 0 | 0 |

**What this shows:**

- No option changes any room rectangle, GIA or footprint.
- C1 and C2 only move 50 mm and 400 mm of Q4 from "partition" to "opening zone".
- A and B reduce the kitchen fixed-unit footprint by 0.18 m² (300 × 600).

---

## 9. Services, construction and door operation

| | A | B | C1 | C2 |
|---|---|---|---|---|
| Plumbing moved | No. Kitchen sink 19E (rear wall) and utility sink 1AC (west end of Q2) unchanged | No | No | No |
| Ventilation / hot water moved | No. MVHR/cylinder 1E8 unchanged | No | No | No |
| Pocket section | x 300–1,300 (unchanged). No fixings, no junctions, no overlap with the MVHR line | x 1,400–2,400. No fixings or junctions, but it **overlaps the MVHR/cylinder line (x 2,200–2,800) by 200 mm**. A duct, pipe or cable crossing Q4 from 1E8 must avoid x 2,200–2,400 or go through the ceiling void (routes not designed) | No pocket. Q4 is solid and can take fixings | No pocket |
| Kitchen latch-side wall | x 2,100–2,400 on the kitchen face is solid wall 125: a possible switch position | x 300–600 solid wall 123 | — | — |
| Operation | Unchanged sliding operation. Needs flush pull or D-pull hardware and operating-force check (REQUIRES CONFIRMATION) | As A | Push from the kitchen, pull from the utility. Hinged doors are generally easier with limited grip, but hardware is not designed | Two leaves. The 350 leaf normally needs bolts releasing (REQUIRES CONFIRMATION) |
| Kitchen unit change | One 600 unit (x 2,100–2,700) becomes 300 (x 2,400–2,700). Base runs along walls 6,200 → 5,900 mm | As A | None | None |

**Unit appliance allocation is not drawn.** If the 600 unit at x 2,100–2,700 was meant to hold an appliance, A and B change that (REQUIRES CONFIRMATION).

**For information only:** earlier project documents tested worktop length against the M4(3) benchmark of 4,730 mm (Table 3.3), which does not govern an M4(1) or M4(2) dwelling. The 5,900 mm in A remains above it.

---

## 10. Can moving the opening (Option B) do better than A? Pocket-position sweep

Source: `evidence/07_pocket_position_sweep/pocket_position_sweep.json`.

**Method:**

- Every single-leaf pocket position on Q4, on a 50 mm grid, for openings of 750, 800, 850 and 900 mm, with the pocket west or east.
- Fixed geometry is MEASURED from the baseline JSON.
- ASSUMPTIONS, as in 0.2.2:
  - leaf = opening + 50;
  - a 50 mm stud at each closed end of the pocket;
  - nothing fixed on the pocket section (so the base run must clear an east pocket);
  - clear opening = opening − 40 (range − 80).

**Results:** 104 positions give a kitchen-side latch nib of at least 300. None does so without cutting the base run.

| Opening | Pocket side | Smallest base-run cut | Clear opening ESTIMATE (range) | Kitchen approach depth |
|---|---|---|---|---|
| 750 | W or E | 100 | 710 (670–710): below the 750 Table 1.1/2.1 minimum | W: 2,600; E: 600 |
| 800 | W or E | 200 | 760 (720–760): may be below 750 | W: 2,600; E: 600 |
| **850 (as issued)** | **W (Option A)** | **300** | **810 (770–810)** | **2,600** |
| 850 | E (Option B) | 300 | 810 (770–810) | 600 |
| 900 | W or E | 400 | 860 (820–860) | W: 2,600; E: 600 |

**Conclusion:**

- Moving the opening never reduces the cut for a given width.
- Reversing the pocket east always puts the latch beside the tall units, so the kitchen-side approach depth falls to 600.
- The only way to cut less than A is a narrower opening. That trades clear width the dwelling may need, so it is not recommended.

---

## 11. Regulatory reading per option (ALL REQUIRES CONFIRMATION)

**Tests applied:**

- **Clear opening (both categories):** the A/B pocket estimate is 810 (range 770–810). It meets the 750 mm Table 1.1/2.1 width for a head-on approach with a 900 mm corridor at every point of the range.
  - The kitchen approach is head-on on a 1,500 mm band (A) or 1,200 mm band (baseline, C1).
  - The utility approach is on a 2,500 mm band.
  - It meets 775 or 800 only if the product allowance is at most 75 or 50 mm.
- **M4(1):** no nib provision. Every option meets the Table 1.1 widths on these estimates, if 1.15a applies to this door at all (VQ-02).
- **M4(2):** each option is tested against 2.22d and NOTE 2 below.

| Option | Reading against M4(2) 2.22d / NOTE 2, if M4(2) is imposed |
|---|---|
| Baseline | Kitchen face nib 0. If either face of a sliding door counts as a leading edge, the kitchen face fails. **This is VF-07, unresolved** |
| **A** | 300 on the kitchen face and 700 on the utility face, so a 300 mm nib exists on **both** faces whichever face is read as "leading". This holds if fixed units count as the nib limit and 300 to the unit face is acceptable (VQ-04). **The 300 has no tolerance**: an end panel or worktop overhang reduces it, so the unit must be set out to give ≥ 300 to the finished face (VQ-04). Clear opening as above |
| B | 300 on both faces. But the kitchen-side nib zone is only 600 deep (tall units 1DE) and the approach in front of the west 300 mm of the opening is 600 deep, so a head-on approach is only available on x 900–1,450 (550 mm). Usability is worse than A, for the same unit change |
| C1 | Pull face (utility) nib 700 meets 2.22d. Push face (kitchen) nib 0 is acceptable **only if** 2.22d and Diagram 2.3 Note 1 need no push-face nib (RQ-03 / VQ-05). Clear 775 (NOTE 3 deemed value for an 826 leaf) meets Table 2.1 at 775 with head-on approach or a 1,050 mm corridor |
| C2 | NOTE 2 wording ("each leaf is at least 300mm wide") met geometrically: leaves 826 and 350. The nib for the main leaf's leading edge is the closed 350 leaf, whose zone is clear 2,600 deep apart from the 13 mm tall-unit overlap. The main leaf alone gives 775 (the 2.20e "main leaf provides the width" rule is for entrance doors; for internal doors it is not stated: VQ-06). It is unconfirmed whether a bolted secondary leaf "effectively provides" a nib (VQ-06). The open main leaf cannot reach 90° clear of unit 1E0 (37 mm), which may reduce its clear width |

---

## 12. Recommendation for review (not an approval)

**Adopt Option A in a future issue, after review.**

**Why A:**

1. It preserves access and usability.
   - Kitchen-face nib becomes 300 (zone 2,600 deep); utility face stays 700.
   - Approach depths are unchanged (2,600 / 1,400).
   - The clear band in front of the opening widens from 1,200 to 1,500 mm.
   - The 2.24b space from the tall units to the base-run end improves from 1,200 to 1,500.
2. It is the smallest kitchen change that keeps the 850 mm opening and the pocket door.
   - One 600 base unit becomes 300.
   - The sweep shows no pocket position gives the nib without at least this cut.
3. Nothing else changes: walls, door, dimensions, services and room areas.
   - Collision sweep: none.
   - Exactly one entity changes (1E0).
4. It does not depend on how 2.22d applies to a sliding door, because both faces get ≥ 300.

**Conditions before any issue:**

1. Confirm the governing category (VQ-01).
2. Confirm that 300 to the fixed-unit face is acceptable, and fix the setting-out datum (carcass, end panel or worktop edge) with the kitchen supplier (VQ-04, VQ-11).
3. Confirm the pocket kit for a 100 mm partition, and its clear opening (VQ-07, VQ-08).
4. Mirror the change in dwelling B: 1E1 [14,300, 8,800, 16,500, 9,400] → [14,300, 8,800, 16,200, 9,400]. Not modelled here (VQ-12).

**Fallback C1:** if the client would rather keep the full base run than the pocket door, and the BCB confirms the push face needs no nib (RQ-03).

**Not recommended:**

- **B:** the same unit cut as A, plus Q4 rebuilt, a worse approach, and a pocket over the MVHR line.
- **C2:** the opening is widened 400 mm, the leaf bears on the base unit, the swing is in the kitchen, and the secondary-leaf operation and the NOTE 2 reading are unconfirmed.

---

## 13. End-of-work checks

Source: `evidence/preservation_end.txt`, 2026-10-24 21:12.

| Check | Result |
|---|---|
| Draft 0.2.2 manifest | 80 / 80 OK. Manifest file still SHA-256 d9062c5a…80f1 |
| Draft 0.2.1 manifest | 63 / 63 OK |
| Verification manifest | 40 / 40 OK |
| Earlier documents | 5 / 5 OK |
| Draft 0.1 record | 3 / 3 OK |
| Total | **191 OK, 0 failures** |
| Working copy vs issued `MMUCO_ORION_Duplex_Draft_0.2.2.dxf` | Identical (2ec8d3f3…d17b): never saved over |
| PDF scale of the comparison sheet | Pass: 1:50 plans and 1:20 details, nothing clipped |

The start check written to `preservation_start.txt` holds 188 lines: the three manifests plus the earlier-documents list. The three Draft 0.1 files were also checked at the start (3 / 3 OK, shown in the session) but were not written to that file. They are in the end check.

---

## 14. Unresolved regulatory and construction questions

| ID | Question | Affects | Who |
|---|---|---|---|
| VQ-01 | Is M4(2) imposed by planning condition, or does M4(1) govern? (RQ-01) | All | Planning adviser |
| VQ-02 | M4(1) 1.15a: does it apply to a door between a kitchen (habitable) and a utility (not habitable)? | All, if M4(1) | BCB |
| VQ-03 | M4(2) 2.22d: for a sliding or pocket door, which face, if any, has the "leading edge"? | Baseline, A, B | BCB / access consultant |
| VQ-04 | Do fixed kitchen units limit a nib, and is the 300 measured to the carcass, end panel or worktop edge? What setting-out tolerance applies? | A, B | BCB / access consultant; kitchen supplier |
| VQ-05 | 2.22d / Diagram 2.3 Note 1: is a push-face nib required for a hinged door? (RQ-03) | C1 | BCB |
| VQ-06 | NOTE 2: does a normally bolted secondary leaf "effectively provide" a nib? Must the main leaf alone meet Table 2.1? | C2 | BCB |
| VQ-07 | The pocket door's clear opening from product data (linings, leaf stand-out, pull), replacing the 40 mm assumption (range 770–810) | Baseline, A, B | Architect / supplier |
| VQ-08 | A pocket kit for a 100 mm finished stud partition (thickness PROVISIONAL); head track and ceiling void; no sockets, switches, rails or fixings on the pocket section | Baseline, A, B | Architect / contractor |
| VQ-09 | Operating force and hardware for users with limited grip (pocket pulls, soft-close; hinged lever handles) | All | Access consultant |
| VQ-10 | MVHR duct, cylinder pipework and electrical routes: none may cross the pocket section (A: x 300–1,300; B: x 1,400–2,400, overlapping the MVHR line by 200) | A, B | M&E designer |
| VQ-11 | Kitchen layout: was the 600 unit at x 2,100–2,700 meant for an appliance? Is a 300 unit acceptable to the client? | A, B | Client / kitchen designer |
| VQ-12 | Dwelling B mirror of the chosen option (not modelled) | Chosen option | Architect |
| VQ-13 | Door-set sizes (826 leaf in a 900 opening; 826 + 350 in 1,250) and leaf thickness | C1, C2 | Architect / door supplier |
| VQ-14 | Is the ADM Vol 1 text used (2015 edition) current, with amendments? | All | Architect |
| OBS-1 | Tall units 1DE in front of west kitchen window 14A (pre-existing, outside VF-07) | — | Architect |

---

## 15. Files

**Investigation:** `MMUCO_ORION_Duplex_Draft_0.2.2_VF07_Investigation/`

| File | What it is |
|---|---|
| `MMUCO_ORION_Duplex_Draft_0.2.2_VF07_Investigation_Report.md` | This report |
| `MMUCO_ORION_Duplex_Draft_0.2.2_VF07_Option_Comparison.pdf` | Comparison drawing, A1 landscape. Plans 1:50 and door details 1:20, verified from the PDF vectors (`evidence/05_sheet_scale_and_render/pdf_scale_check.json`: frame 800.000 × 550.000 mm; Q3 wall 2.0 × 40.0 mm in all five plans, 1:50; 5.0 × 70.0 mm in all five details, 1:20; nothing clipped) |
| `MMUCO_ORION_Duplex_Draft_0.2.2_VF07_Option_Comparison.png` | Rendered from that PDF (9,933 × 7,016 px) |
| `MMUCO_ORION_Duplex_Draft_0.2.2_VF07_Option_Table.csv` | Measured option table with a basis column |
| `MMUCO_ORION_Duplex_Draft_0.2.2_VF07_Investigation_Manifest.sha256` | Hashes of every file in this folder and the scratch folder |

**`evidence/` subfolders:**

| Subfolder | Contents |
|---|---|
| `01_baseline_geometry/` | Entities with handles and coordinates |
| `02_measurements/` | One JSON per state, plus independent-parser JSON |
| `03_collisions/` | Includes the positive control |
| `04_comparison_sheet_meta.json` | Entities each option changed, found by comparison |
| `05_sheet_scale_and_render/` | PDF scale check |
| `06_entity_diffs/` | Whole-drawing diffs |
| `07_pocket_position_sweep/` | Sweep results |
| `scripts/` | Every script used |
| `preservation_start.txt`, `preservation_end.txt` | Hash checks |

**Scratch (not issued):** `MMUCO_ORION_Duplex_Draft_0.2.2_VF07_SCRATCH_not_issued/`. Contents: the working copy, the four option DXFs, the sheet source and script, and a README.
