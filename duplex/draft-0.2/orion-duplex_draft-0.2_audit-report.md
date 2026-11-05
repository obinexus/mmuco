# MMUCO ORION Duplex — Requirements Audit and Draft 0.2 Proposal

**Project:** OBINexus Design · MMUCO ORION Duplex
**Document:** Requirements audit, geometry audit, revised concept and constraint check (Stages 1–4)
**Status:** DRAFT FOR CLIENT REVIEW · 24 October 2026. Draft 0.2 CAD is **not yet drawn**: it waits for the programme decision in §4.6.
**Supersedes:** nothing. Draft 0.1 (`MMUCO_ORION_Duplex_Floor_Plan.dxf/.pdf/.png`) is retained unchanged as the baseline.

> **Update, 24 Oct 2026:** §3.3, §3.4 and §4.6 are superseded by `MMUCO_ORION_Duplex_Draft_0.2_Decision_Package.md`, which:
> - shows the 5.12 m² of partitions inside the 119.54 m² GIA explicitly;
> - spells out the 263.12 m² footprint as main block plus entrance projection;
> - corrects the store and bathroom "Pass" entries (area met, documented rectangle not met);
> - compares Options A, B and C on verified geometry;
> - changes the recommendation from B to C.

> This is an architectural concept exercise. It is not a planning approval, a Building Regulations compliance statement, a fire strategy or a structural design. Jurisdiction is taken as **England** (Research L11; Logistics r3). Every compliance-related item below needs review by appropriately qualified UK professionals (architect, fire engineer, structural engineer, building control, planning adviser).

**Citation conventions**

- **Research Lnn**: line *nn* of `MMUCO_ORION_Duplex_Research.md`.
- **Logistics rnn**: line *nn* of `MMUCO_ORION_Duplex_Logistics.csv`, where line 1 is the header row.
- **Typology §x**: section of `MMUCO-ORION-SPATIAL-TYPOLOGY_1.md` (v0.2).
- **Schedule p.x**: page of `MMUCO_ORION_Phase_1_Measurement_Schedule.pdf`.
- **NDSS**: *Technical housing standards – nationally described space standard*, gov.uk, checked 24 Oct 2026.
- **CONCEPT-01**: the supplied "MMUCO ORION DUPLEX – Concept Floor Plan – United Kingdom" image.
- **SKETCH-01**: the supplied hand sketch "Full front porch 4x3m".

**Evidence classes:**

- **CONFIRMED**: an explicit, unambiguous statement in a supplied document or an official standard.
- **PROPOSED**: a design allowance in a project document, not a measurement.
- **BENCHMARK**: published guidance.
- **UNVERIFIED**: a tentative transcription or a scaled estimate.
- **CONFLICT**: sources disagree.
- **ASSUMPTION**: introduced by the drafter, with no source.

---

## Stage 1 — Evidence audit

### 1.1 Inventory

| # | File | What it is | Relevance to the duplex | Reliability |
|---|---|---|---|---|
| 1 | `MMUCO_ORION_Duplex_Research.md` (Rev 0.1, 8 Sep 2026) | Duplex research and dimensional brief | **Primary brief.** Design basis (L7), room programme (L43–57), access targets (L63), kitchens (L67), entrances and separation (L69), overheating/acoustics (L79), planning issues (L83–87) | Programme is explicitly a "working assumption" (L7) and "original concept programme" (L41) |
| 2 | `MMUCO_ORION_Duplex_Logistics.csv` | 79-row schedule with BENCHMARK / PROPOSED / CALCULATED / IMAGE-UNVERIFIED / TBD tags | **Primary schedule.** Room rectangles r20–37, access r40–46, kitchen/work/bath r47–53, link r54–55, services r56–62, safety r65, structure r66–68, site r69–76 | Tags are explicit; nothing beyond NDSS benchmarks is a code requirement |
| 3 | `MMUCO_ORION_Phase_1_Measurements.csv` + `…Measurement_Schedule.pdf` (5 pp.) | **Phase 1 agricultural support infrastructure** at Forest Farm Peace Garden / Allotments, Hainault, Ilford IG6 2XN (Schedule p.1 §1) | **Not a duplex document.** A3 "conservatory / covered growing or welfare space 5 m × 4 m" and A4 "front French double doors 1680 mm" are Phase 1 items. Schedule p.2 §5: "Separate Phase 1 agricultural works from any future housing / compound proposal." | A3 Medium/high, A4 Medium, "verify on site" |
| 4 | `MMUCO-ORION-SPATIAL-TYPOLOGY_1.md` (v0.2, 8 Sep 2026) | Transcription of sheets S-01…S-08 and dictation T-01 | Typology invariants (§2.2), square prohibited (§2.7), S-08 dwelling schedule (§4), Ngaji naming (§4.1), porch vs patio and "two porches" (§4.2), S-01 Beckton survey (§6), open items (§8), T-01 decisions (§9) | Sheets high on figures; T-01 "low per phrase". **T-01 itself is not among the supplied files**, so T-01-derived claims cannot be checked here |
| 5 | `MMUCO ORION.pdf` (15 pp.) / `.docx` | Constitutional and spatial framework | p.4: agricultural/welfare kept apart from later residential. p.9 §7.1: paired dwellings "facing one another across a protected shared threshold". p.12–14: Node B / Phase 4 accessible dwellings, shared courtyards, protected pedestrian routes | Narrative intent, no dimensions |
| 6 | `Site Planning.pdf` (5 pp.) | "OBINexus Spatial Measurement Standard v1" | p.1: buildings in mm, areas in m². p.4–5: no cm or imperial units, 300 mm grid, floor plans 1:100, site plans 1:500. p.3 "Bedroom = 3m × 3.6m" is a worked example, not a requirement | Drawing convention |
| 7 | `MMUCO Orion OS.zip` → Compound Spec, Zone Specs, Action Roadmap (May 2026) | 1,000,000 m² compound at **Nnewi, Anambra State, Nigeria** | Zone Specs §1.3 (UCHE zone): paths ≥2 m, doors ≥1 m clear, ramps ≤1:12. Roadmap Phase 3A: all paths 2 m, all buildings wheelchair accessible and sensory-regulated | Different site and jurisdiction; treated as aspiration where it conflicts |
| 8 | `Screenshot_8-7-2026…planningportal.co.uk.jpeg` | Draft fee calculator | 4 new dwellinghouses; agricultural building 2 m²; glasshouses 20,000 m²; waste disposal and other change of use ticked; site area blank | Draft selections only (Research L21, L89) |
| 9 | `MMUCO ORION Duplex.jpg` (S-08) | Pen room plan | Living 4.8 × 5, dining 4.8 × 5, bathroom 4 × 2.5, conservatory 2.5 × 1.5, patios, kitchen "Spoon / Ngaji", detached orangery | Sheet geometry (Typology §4). Typology O-8 asks whether S-08 is an ORION dwelling or a proposal over an existing property |
| 10 | `Floor Plan.jpg` ≡ `WIN_20260528_21_03_01_Pro.jpg` (identical MD5) | S-01: **measured survey of the existing Beckton property** (Typology §6) | Source of "conservatory 5 × 4" and "French doors 1.971 × 1.168" | High for that property; **not an ORION dimension** |
| 11 | `Site Plan.jpg` ≡ `WIN_20260528_21_03_36_Pro.jpg` (identical MD5) | S-02 compound ideation | Zones; "2 per plot household" | No usable dimensions |
| 12 | `WIN_20260703_13_25_02/13_28_07/13_28_14` | S-03 to S-05 butterfly wing studies | Shape and cardinal points only | No dimensions (Research L20, L23) |
| 13 | `WIN_20260905_01_09_52_Pro.jpg` | S-07 "Bird and dragon motif" duplex | Superseded study (Typology §3.1); central arched opening on the axis | No dimensions |
| 14 | `mmuco-orion-face-me-typology_1.svg`, `mmuco-orion-tessellation.svg` | Typology diagrams | Invariants I-1…I-6; "NOT TO SCALE" | Diagrammatic |
| 15 | `MMUCO Sensory CyberNetic Housing - 10 MAY 2026.tif` | TIFF, 1920 × 944 | **Blank:** one frame, no non-white pixels | No content |
| 16 | Two otter.ai transcripts | Voice notes | No porch, kitchen, bedroom or entrance requirements found. Glasshouse/conservatory/orangery for agricultural use mentioned | Not T-01 |
| 17 | Legal memo (md/docx/pdf), Drift Theorem pdf, Agile Methodology pdf, OBINexus OS pdf | Governance and OS | No dwelling requirements (keyword search) | — |
| 18 | CONCEPT-01 (attachment) | Rendered concept plan | Living 4.8 × 5 and dining 4.8 × 5 per home; bedroom 2.8 × 3.5; bathroom; utility/storage; shared hallway; "Front Entrance (3 Porches)"; conservatories; patios. Notes: "Dimensions are indicative", "extended family living model", "energy independence". Sustainability: solar, battery, efficient heating, rainwater, smart monitoring | Labelled dimensions indicative (its own note 1) |
| 19 | SKETCH-01 (attachment) | Hand sketch | Projecting hall, double door, "Full front porch 4x3m" | Client instruction; dimensions scaled, not measured |
| 20 | Draft 0.1 DXF/PDF/PNG (this project) | Earlier CAD | Baseline for the Stage 2 audit | Drafted from 18 and 19 plus items 3 and 10 (wrongly, see §1.3) |

### 1.2 What is confirmed, proposed, conflicting or unknown

**Confirmed (explicit in a source, or an official standard)**

- Two-dwelling duplex concept with mirrored halves: CONCEPT-01; Typology §2.2 I-1, I-3.
- Each home "should have a suitable independent entrance and escape arrangement", and an enclosed connection "must not casually breach dwelling fire or acoustic separation": Research L69. Logistics r42 refers to "two private entrances".
- Private kitchens in the base two-home scheme: Research L67.
- NDSS technical requirements, checked at source:
  - A double bedroom is at least 11.5 m² (para 10(d)).
  - One double is at least 2.75 m wide and every other double at least 2.55 m (para 10(e)).
  - A built-in wardrobe counts toward bedroom area, and any amount over 0.72 m² counts toward storage (para 10(h)).
  - GIA is measured to the internal faces of the perimeter walls, including partitions (para 8).
  - 1-storey dwellings need at least 50 m² GIA and 1.5 m² storage for 1b2p, or 70 m² and 2.0 m² for 2b4p (Table 1).
  - NDSS applies only where the local planning authority has adopted it (Research L39).
- A porch is attached and roofed; a patio is open and at ground level: Typology §4.2.
- Kitchen naming rule NM-1 ("Spoon / Ngaji", Igbo first-class): Typology §4.1, T-01 decision 9.
- Drawing units mm, areas m², floor plans 1:100: Site Planning.pdf p.4–5; Typology header.

**Proposed (project allowances, not measurements)**

- The whole room programme (Research L43–57; Logistics r20–38), each row tagged "PROPOSED … verify in furnished CAD design".
- Path 1.5 m (r40), corridors 1.2 m (r41), entrance door 0.9 m clear (r42), internal doors 0.85 m clear (r43), turning circle 1.5 m (r44), landing 1.5 × 1.5 m (r45–46), shower zone 1.2 × 1.2 m (r52–53), GIA budget 110 m² per home (r17).

**Conflicts**

- **Bedrooms per home:** 1 (CONCEPT-01) or 2 doubles, 4 bedspaces (Research L7; r2 tagged ASSUMPTION).
- **Living and dining:** two separate 24 m² rooms (CONCEPT-01; S-08 via Typology §4) or one combined 24 m² room (Research L45; r20).
- **Dwelling count:** 2 (CONCEPT-01; Research L7) or 4 (Planning screenshot).
- **Conservatory:** 5 × 4 m (Phase 1 A3 and S-01 Beckton, neither a duplex source), 2.5 × 1.5 m hexagonal (S-08, Typology §4), or larger and undimensioned (CONCEPT-01 graphic).
- **Front doors:** 1680 mm (Schedule A4), 1.168 m (S-01, Typology §6) or "numbers unclear" (r6). None of the three is a duplex source.
- **Porch count:** "3 porches" (CONCEPT-01), "two porches" (Typology §4.2 / T-01 #10) or one full porch 4 × 3 m (SKETCH-01).
- **Path width:** 1.5 m (r40) or 2.0 m (Zone Specs §1.3; Roadmap 3A, Nigerian compound).
- **Entrance door clear width:** 0.9 m (r42) or 1.0 m (Zone Specs §1.3).
- **Shared space:**
  - "Shared Family Spaces" and an "extended family living model" (CONCEPT-01).
  - The typology's enclosed neck: "N is the sole enclosed connection", and every habitable room opens onto N (Typology §2.2 I-2, I-4).
  - Against both: self-contained homes with fire and acoustic separation (Research L69).
- **Plan geometry:** rectilinear (CONCEPT-01) or "square plan prohibited", "tessellation required" (Typology §2.7, I-6; T-01 #6, #7).
- **Planning entries:** agricultural 2 m² and glasshouse 20,000 m² (screenshot), or 40 m² and 30 m² "matches Planning Portal entry" (Schedule p.1 A1–A2).

**Unknown**

- Site address and boundary for the duplex (Research L11; r69–70). Phase 1 lists Forest Farm, Hainault, but only for agricultural works.
- Local planning authority and whether NDSS is adopted.
- Site designations.
- Occupants and the Part M category (Research L63).
- Ceiling and roof form (r68).
- Wall build-ups and thicknesses (r67).
- Acoustic and fire specification (r64–65).
- Foundations, drainage and services (r66, r72–73).
- Orientation: CONCEPT-01's north arrow only. The typology orientation rules are written for Nnewi at about 6°N, not England.

### 1.3 Findings that change Draft 0.1

1. **Draft 0.1 used two Phase 1 / Beckton dimensions as if they were duplex dimensions.**
   - The 5 × 4 m conservatory is Schedule A3, a Phase 1 "covered growing or welfare space", and also the S-01 existing-property survey.
   - The 1680 mm front doors are Schedule A4. The same handwriting reads 1.168 m in Typology §6, and r6 says the numbers are unclear.
   - Neither is confirmed for the duplex. Logistics r4 says the conservatory reference is "Not included in base dwelling areas".
2. **Draft 0.1 drew an invented plot boundary** (28.0 × 23.5 m). No site survey exists (r69). It must not appear in Draft 0.2.
3. **The kitchen, bedroom and independent-entrance requirements are real but carry PROPOSED status.** NDSS 11.5 m² is a benchmark that applies where the LPA has adopted it. The 2.8 × 3.5 m bedroom fails it.

---

## Stage 2 — Geometry audit of Draft 0.1

Values are measured from `MMUCO_ORION_Duplex_Floor_Plan.dxf`. Room sizes are clear internal; overall dimensions are external faces.

| Item | Draft 0.1 value | Check |
|---|---|---|
| Main block | 20.0 × 9.2 m = 184.0 m² | — |
| Projecting hall | 4.0 × 2.5 m = 10.0 m² | 2.5 m scaled from SKETCH-01 (ASSUMPTION) |
| Enclosed footprint (excl. conservatories) | 194.0 m² | — |
| Conservatories | 2 × (5.0 × 4.0 less two 1 × 1 m chamfers) = 2 × 19.0 m² | Size not supported for the duplex (§1.3) |
| Porch | 4.0 × 3.0 m = 12.0 m², roofed | Size from SKETCH-01 only |
| Walls | External 300, party 200, partitions 100 | ASSUMPTION; r67 TBD |
| Living + dining (open plan) | 9.6 × 5.0 m = 48.0 m² (2 × 24.0) | Matches CONCEPT-01; conflicts with r20 (24 m² combined) |
| Bedroom | 2.8 × 3.5 m = **9.8 m²** | **Fails** NDSS 10(d) 11.5 m²; width 2.8 ≥ 2.75 passes |
| Bathroom | 2.5 × 3.5 m = 8.75 m² | ≥ r30–31 (7.5) |
| Utility / storage | 2.4 × 3.5 m = 8.4 m² | Sink and washer only; **no kitchen** (fails Research L67) |
| Built-in storage | None designated (about 1.0 m² tall cupboard in utility) | **Unclear / fails** NDSS 1.5 m² (1b2p) |
| Shared hall | 3.4 × 6.0 m = 20.4 m², doors to both dining rooms | **Fails** independence (Research L69, r42); breaches separation |
| GIA per home (excl. shared hall) | ≈ 76.4 m² | ≥ NDSS 1b2p 50 m² |
| Internal door openings | 800 mm (bath, utility), 900 mm (bedroom, hall) | 800 openings give < 850 clear: **fails** r43 |
| Front door | 1680 mm French pair, shared | Not a duplex dimension; not private (r42) |
| Bedroom access | Off the open-plan living area (inner room) | Escape window needed; ADB review |
| Plot boundary | Drawn 28.0 × 23.5 m | **Invented**: remove |
| Path | 1.5 m | = r40; conflicts with 2.0 m compound standard |

---

## Discrepancy table

| Requirement | Source evidence | Current design (0.1) | Gap | Required action | Status |
|---|---|---|---|---|---|
| Self-contained homes, own entrance | Research L7, L69; r42 "two private entrances" | One shared hall and front door | Not independent | Private lobby and front door per home | PROPOSED requirement → addressed in 0.2 |
| Fire / acoustic separation between homes | Research L69, L79; r64–65 (TBD); ADB / ADE | Hall connects both dining rooms | Separation breached | Continuous separating wall; no internal link | Addressed in principle; **professional review** |
| Private kitchen 3.0 × 4.0 m | Research L46, L67; r22–23 | None | Missing | Kitchen next to dining, extract to outside (r57) | PROPOSED → added in 0.2 |
| Double bedroom ≥ 11.5 m², ≥ 2.75 m (first) / 2.55 m (others) | NDSS 10(d), (e); r10–12 | 9.8 m², 2.8 m | −1.7 m² | Enlarge | BENCHMARK → met in 0.2 |
| Bedroom 1 3.5 × 4.0 / Bedroom 2 3.0 × 4.0 | r24–27 | One bedroom only | Programme conflict | Client decision (§4.6) | **CONFLICT** |
| Living and dining | r20–21 (one 24 m² room) vs CONCEPT-01 and S-08 (two 24 m² rooms) | 48 m² open plan | Conflict | Client decision (§4.6) | **CONFLICT** |
| Quiet work room 2.5 × 3.2 m | Research L49, L65; r28–29 | None | Missing | Add, away from plant | PROPOSED → added in 0.2 |
| Bathroom 2.5 × 3.0 m; level shower 1.2 × 1.2 m | r30–31, r52–53; S-08 4 × 2.5 | 2.5 × 3.5 m, bath | Size OK; no level-access shower | Level shower zone | PROPOSED → 0.2 |
| Additional WC 1.2 × 2.0 m (optional) | r32–33 | None | Optional | Defer | OPEN |
| Utility and plant 2.0 × 2.0 m | r34–35; Research L65 | 2.4 × 3.5 m utility/storage | OK | Keep plant away from bedrooms | PROPOSED → 0.2 |
| Built-in storage ≥ 1.5 / 2.0 m²; store 1.05 × 2.0 m | NDSS Table 1; r16, r36–37 | None designated | Fails | Dedicated store | BENCHMARK → 0.2 |
| Circulation: corridor 1.2 m, turning 1.5 m, allowance 10 m² | r38, r41, r44 | Shared 3.4 m hall | Shared | Private hall 1.6 m + corridor 1.2 m | PROPOSED → 0.2 (24 m², **over allowance**) |
| Entrance door ≥ 0.9 m clear | r42 vs Zone Specs §1.3 (1.0 m, Nigeria) | 1680 pair, shared | Not private | One leaf ≈ 1,010 mm per home | **CONFLICT** (0.9 / 1.0) |
| Internal doors ≥ 0.85 m clear | r43 | 800 / 900 openings | 800 fails | Openings for 926 mm leaves | PROPOSED → 0.2 |
| Front doors 1680 mm | Schedule A4 (Phase 1); Typology §6 1.168 m (S-01); r6 TBD | Used | Not a duplex source | Do not carry forward | **UNVERIFIED / misattributed** |
| Conservatory 5 × 4 m | Schedule A3 (Phase 1); r4–5 IMAGE-UNVERIFIED; Typology §6 (S-01) vs §4 (S-08 2.5 × 1.5) | 2 × 5 × 4 m | Not confirmed for the duplex | Provisional outline; size after ADO assessment (Research L79) | **CONFLICT / UNVERIFIED** |
| Roofed porch | Typology §4.2; SKETCH-01 (4 × 3 m); CONCEPT-01 ("3 porches") | One 4 × 3 m porch | Count conflict | One roof over two private landings (each 2.0 × 3.0 m ≥ r45–46) | Porch type CONFIRMED; size client-sketch |
| Front path 1.5 m | r40 vs Roadmap 3A / Zone Specs §1.3 (2.0 m) | 1.5 m | Minor conflict | Keep 1.5 m; flag | **CONFLICT** (minor) |
| Hall projection 2.5 m | SKETCH-01 (scaled) | 2.5 m | No document | Keep; confirm | ASSUMPTION |
| Wall thicknesses | None (r67 TBD) | 300 / 200 / 100 | Party wall likely thicker for ADE/ADB | Keep for concept; flag | ASSUMPTION |
| Site boundary | r69–70 TBD | Invented 28 × 23.5 m | Fabricated | Remove | **FIX** in 0.2 |
| Plan geometry | Typology §2.7, I-6; T-01 #6 vs CONCEPT-01 | Rectilinear | Conflict | Client decision; 0.2 stays rectilinear | **CONFLICT** |
| Shared threshold | MMUCO ORION.pdf p.9 §7.1; Typology I-2, I-4 vs Research L69 | Enclosed shared hall | Conflict with independence | Shared threshold made **external** (covered porch) | **CONFLICT**, 0.2 resolves toward Research L69 |
| Patios | CONCEPT-01; S-08 (×3); Typology §4.2 | 1.8 × 7.6 m each | Size unsourced | Provisional | ASSUMPTION |
| Orientation | CONCEPT-01 north arrow; Typology §2.4 (Nnewi) | Gardens to north | UK solar not assessed | Overheating and daylight check | OPEN |
| Igbo/English naming | Typology §4.1 NM-1, O-5 | English only | Partial | "NGAJI / KITCHEN"; others await O-5 | PARTIAL |
| Accessibility category | Research L63; Roadmap 3A | None stated | Undecided | Choose M4(1)/(2)/(3) | OPEN |
| Ventilation | r56–62; Research L73–75 | Windows only | Extracts not shown | Note on drawing; services design | OPEN |
| Ceiling height ≥ 2.3 m over 75% (2.5 m proposed) | NDSS 10(i); r15, r39 | Plan only | Not shown | Sections in a later stage | OPEN |
| Dwelling count 2 vs 4; planning categories | Screenshot vs CONCEPT-01 / Research L83–86 vs Schedule p.1 | 2 | Conflict | Resolve before any application | **CONFLICT** (outside plan) |

---

## Stage 3 — Revised concept (Draft 0.2 proposal)

### 3.1 Design moves

1. **Independent homes, shared threshold kept outdoors.**
   - The party wall now runs unbroken from the rear wall to the front of the projecting entrance block.
   - The block, still 4.0 m wide and projecting 2.5 m as in SKETCH-01, now holds **two private entrance lobbies** (1.6 m clear each), each with its own front door.
   - Both doors open under **one roofed 4.0 × 3.0 m porch**, the "protected shared threshold" of MMUCO ORION.pdf p.9 §7.1, realised as the "covered outdoor connection" option in Research L69.
   - A screen on the party-wall line gives each home a 2.0 × 3.0 m landing (≥ r45–46).
   - There is no internal connection between the homes.
2. **A private hall and corridor in each home.**
   - Hall 1.6 m clear (meets the r44 turning circle); corridor 1.2 m clear (r41).
   - Every bedroom and the quiet room opens onto the hall or corridor, which leads to the front door.
3. **Kitchen next to living/dining** with a wide opening.
   - Pantry/food store behind the kitchen, utility and plant off the kitchen with a back door, and the bathroom grouped with them.
   - All wet rooms sit in one services zone, mirrored either side of the party wall.
4. **Bedrooms meet NDSS:** 14.7 m² and 12.6 m², both with wardrobe space.
5. **The quiet work room sits at the front, away from plant** (Research L65). At 8.0 m² and 2.5 m wide it could also serve as a single bedroom (NDSS 10(c)).
6. **Conservatory provisional.**
   - Shown as a dashed outline off the living/dining room, using the only dimension written on an ORION sheet: S-08, 2.5 × 1.5 m hexagonal.
   - Excluded from GIA; size waits on an ADO overheating assessment (Research L79).
   - The conservatories move to the outer rear corners, so they no longer meet at the party wall.
7. **Removed from 0.1:**
   - The invented plot boundary.
   - The 5 × 4 m conservatory dimension.
   - The 1680 mm door dimension.
   - The shared internal hall.

### 3.2 Indicative layout (left home; right home mirrored; north up)

```
 rear (garden) ─────────────────────────────────────────────────────────────┐
  ┌─────────────────────┬───────────────┬──────────────╥── mirror ...
  │ LIVING / DINING     │ NGAJI/KITCHEN │ UTILITY &    ║
  │ 4.8 × 5.0  (patio   │ 3.0 × 4.0     │ PLANT 2.9×2.3║  back door
  │  doors W; conserv.  ├───────────────┼──────────────║
  │  provisional N)     │ PANTRY 3.0×0.9│ BATHROOM     ║
  ├──────door───────────┴───────────────┤ 2.9 × 2.6    ║
  │ CORRIDOR 1.2 clear ─────────────────┴───door───┐   ║  ← party wall 200
  ├────door────┬────door─────┬──────────┐  HALL    │   ║    continuous
  │ BEDROOM 1  │ BEDROOM 2   │ STORE    │  1.6     │   ║
  │ 3.5 × 4.2  │ 3.0 × 4.2   ├──────────┤  clear   │   ║
  │            │             │ QUIET    door       │   ║
  │            │             │ 2.5×3.2  │          │   ║
  └────────────┴─────────────┴──────────┼  LOBBY   ║ LOBBY (right home)
                                        └──door────╨────door──┘
                                         PORCH 4.0 × 3.0 (one roof, two landings)
                                                 │ path 1.5 │
```

### 3.3 Proposed room schedule (per home; both homes identical, mirrored)

All dimensions are **clear internal** (finished face to finished face) in metres. Areas are calculated from those dimensions.

| Room | W × D (m) | Area (m²) | Requirement and source | Check |
|---|---|---|---|---|
| Bedroom 1 (double) | 3.50 × 4.20 | 14.70 | ≥ 11.5 m², ≥ 2.75 m (NDSS 10(d), (e)); 3.5 × 4.0 proposed (r24–25) | Pass |
| Bedroom 2 (double) | 3.00 × 4.20 | 12.60 | ≥ 11.5 m², ≥ 2.55 m (NDSS 10(d), (e)); 3.0 × 4.0 proposed (r26–27) | Pass |
| Quiet work room | 2.50 × 3.20 | 8.00 | 2.5 × 3.2 (r28–29); desk 1.6 × 0.8 + 1.2 m behind chair (r49–51) | Pass |
| Store (built-in) | 2.50 × 0.90 | 2.25 | ≥ 2.0 m² (NDSS Table 1, 2b4p); 2.1 m² proposed (r36–37) | Pass |
| Living / dining | 4.80 × 5.00 | 24.00 | 4.8 × 5.0 (r20–21) | Pass (see §4.6) |
| Ngaji / kitchen | 3.00 × 4.00 | 12.00 | 3.0 × 4.0 (r22–23); aisle ≥ 1.2 m with 0.6 m worktops (r47–48) | Pass |
| Pantry / food store | 3.00 × 0.90 | 2.70 | Brief item 3A (food storage); design proposal | — |
| Bathroom | 2.90 × 2.60 | 7.54 | ≈ 7.5 m² (r30–31); level shower 1.2 × 1.2 m (r52–53) | Pass; turning circle to verify |
| Utility and plant | 2.90 × 2.30 | 6.67 | ≥ 2.0 × 2.0 m (r34–35) | Pass |
| Entrance hall (incl. lobby) | 1.60 × 8.00 | 12.80 | 1.5 m turning (r44) | Pass |
| Corridor | 9.30 × 1.20 | 11.16 | 1.2 m clear (r41) | Pass |
| **Sum of rooms** | | **114.42** | | |
| Partitions and ducts | | 5.12 | | |
| **GIA per home** (internal faces of perimeter walls, incl. lobby) | | **119.54** | NDSS 2b4p ≥ 70 m²; budget 110 m² (r17) | NDSS pass; **+9.5 m² over budget** |
| Circulation within GIA | | 23.96 | Allowance 10 m² (r38) | **Over** (see §4.5) |

**Two-home totals:** GIA 239.1 m² (budget 220 m², Research L59), excluding the porch, conservatories and patios.

### 3.4 Overall dimensions (external, provisional)

| Element | Dimensions | Area | Status |
|---|---|---|---|
| Main block | **22.6 m wide × 11.2 m deep** (was 20.0 × 9.2) | 253.1 m² GEA | Derived from the clear rooms plus assumed walls |
| Entrance projection (two lobbies) | 4.0 × 2.5 m | 10.0 m² | 2.5 m = ASSUMPTION (SKETCH-01) |
| **Enclosed footprint** (excl. conservatories) | | **263.1 m²** (was 194.0) | — |
| Porch (roofed, open-sided) | 4.0 × 3.0 m | 12.0 m² | Size from SKETCH-01 |
| Depth from the front of the porch to the rear wall | 16.7 m (13.7 m to the front of the lobbies) | — | — |
| Conservatories (2) | 2.5 × 1.5 m hexagonal each (S-08) | ≈ 3.2 m² each | PROVISIONAL, excluded from GIA |
| Patios (2, west and east) | 1.8 × 5.0 m each | 9.0 m² each | PROVISIONAL (unsourced) |
| Front path | 1.5 m wide | — | r40 (PROPOSED) |
| Site boundary | **Not shown** | — | No survey (r69) |

---

## Stage 4 — Constraint check

### 4.1 Dimensional conflicts and unavoidable trade-offs

1. **Programme (main decision, §4.6).** Draft 0.2 as proposed follows the only written room programme (2 double bedrooms, quiet room, one 24 m² living/dining). CONCEPT-01's separate 24 m² dining room is merged into the living/dining room.
2. **GIA +9.5 m² over the 110 m² budget, and circulation 24 m² against a 10 m² allowance.**
   - Cause: SKETCH-01's single central projecting entrance puts each front door at the party wall, so a long corridor is needed to reach the far rooms.
   - To get back to about 110 m²: move each front door to the middle of its own façade with its own porch. That matches "two porches" (Typology §4.2) but gives up the central composition in SKETCH-01.
3. **The building grows** from 20.0 × 9.2 m to 22.6 × 11.2 m (footprint +69 m²) to fit the kitchens, compliant bedrooms and private circulation.
4. **Typology invariants I-2 and I-4** (an enclosed shared neck, with habitable rooms opening onto it) are **not met**. Meeting them would make the homes share internal circulation, which conflicts with Research L69 independence and separation. Draft 0.2 keeps the threshold outdoors.
5. **The 1680 mm French pair is not carried forward.** Each home gets one leaf of about 1,010 mm, giving ≥ 900 mm clear (r42). A pair would not fit a 1.6 m lobby.
6. **The bath becomes a level-access shower** (r52–53). A bath can go back in if you prefer, at some cost to turning space.
7. **The optional WC is omitted** (r32–33). It can be added at about +2.4 m² per home.
8. **Rectilinear plan kept**, in conflict with Typology I-6 ("square prohibited"). A tessellating geometry is a separate design study.

### 4.2 Fire safety (England, Approved Document B Vol 1). All items for qualified review; nothing here is a compliance claim

- **Separating wall:** fire-resisting and continuous from foundations to the underside of the roof, including through the projecting lobby block and the shared porch roof. Fire-stop all junctions. The party wall is drawn 200 mm thick as a concept assumption; the specified system may be thicker.
- **Escape (ground storey):** every bedroom and the quiet room opens onto the hall or corridor leading to the front door. Living/dining has patio doors and the utility has a back door as alternative exits. Emergency escape windows may still be required: confirm.
- **Alarms:** smoke and heat detection per ADB / BS 5839-6, by designer.
- **Battery storage (concept sustainability goal):** location, enclosure and separation from the escape route need specialist design (for example PAS 63100). Do not assume the utility room is suitable until reviewed.
- **External fire spread:** boundary distances are unknown (r70). Conservatory glazing and the porch near the boundary need checking once a site exists.
- **Fire service access:** TBD (r71).

### 4.3 Accessibility (Approved Document M)

- **Category not chosen** (Research L63). The Nigerian compound standard aims for "all buildings wheelchair accessible" (Roadmap 3A).
- **Drawn provisions:**
  - Level threshold assumed at the front doors.
  - Front door ≥ 900 mm clear.
  - Internal openings sized for 926 mm leaves (≈ 850 mm clear).
  - 1.2 m corridor and 1.5 m turning space in the hall.
- **Bathroom:** a level-access shower is drawn. Door swing direction, WC transfer space and the turning circle still need checking against the chosen category.
- **Approach:** 1.5 m path drawn (r40); the compound standard is 2.0 m. Gradients and levels are unknown.

### 4.4 Structure, services, planning

- **Structure:** spans up to 5.0 m in the rear band; roof form TBD (r68); foundations TBD (r66). The conservatory and porch roofs need detailing.
- **Ventilation:** kitchen extract to outside (13 L/s continuous high rate); bathroom and utility 8 L/s each (r57–58; ADF 2021, edition to confirm). MVHR space in the utility/plant room. The bathroom and pantry are internal and need mechanical extract.
- **Energy and water (CONCEPT-01 goals only):** solar PV, battery, efficient heating, rainwater use and monitoring. Plant space is reserved; nothing is sized.
- **Planning:**
  - Dwelling count (2 or 4) and the fee-calculator categories need resolving (Research L83–87).
  - NDSS applies only if the LPA has adopted it.
  - The site and its designations are unknown.
  - The Phase 1 site (Forest Farm, IG6) is for agricultural works only. Whether housing is intended there is unconfirmed (Schedule p.2 §5 asks for separation).
- **Orientation:** gardens are shown north, following CONCEPT-01. For England this gives north-facing gardens. Check daylight and overheating (ADO) before fixing glazing.

### 4.5 Missing information that blocks finalisation

- Site address, boundary survey and levels.
- Dwelling count.
- Occupancy and Part M category.
- Separating-wall and external-wall build-ups.
- Roof form.
- Conservatory size.
- Patio sizes.
- Confirmation of the 2.5 m projection and the 4.0 × 3.0 m porch.
- Igbo names for spaces other than the kitchen (Typology O-5).

### 4.6 Decision needed before CAD: programme option

| Per home | Draft 0.1 | **0.2-B (recommended)** | 0.2-C | 0.2-A |
|---|---|---|---|---|
| Basis | CONCEPT-01 | Research / Logistics programme | Programme + CONCEPT-01's separate dining | CONCEPT-01 rooms + fixes only |
| Bedrooms | 1 (9.8 m², fails) | 2 doubles + quiet room | 2 doubles + quiet room | 1 double |
| Living / dining | 48 m² open plan | 24 m² combined | 24 + 24 m² | 24 + 24 m² |
| Kitchen | None | 12 m² + pantry | 12 m² | 12 m² |
| NDSS type | 1b2p | 2b4p | 2b4p | 1b2p |
| GIA per home | ≈ 76 (+ shared hall) | **119.5 (laid out)** | ≈ 144 (estimate, not laid out) | ≈ 110–118 (estimate, not laid out) |
| Main block | 20.0 × 9.2 m | **22.6 × 11.2 m** | ≈ 27–32 m wide (estimate) | ≈ 22–23 m wide (estimate) |

**Recommendation: 0.2-B.**

- Every room traces to a documented row.
- Both bedrooms meet NDSS.
- It stays close to the 110 m² budget.
- It does not change the dwelling type further than the research brief already does.

**C** keeps CONCEPT-01's two 24 m² rooms at about +25 m² per home. **A** keeps one bedroom but gains little space, because the central entrance still needs the same corridor.

---

## Assumptions register (still to be confirmed)

| # | Assumption | Used for | Basis |
|---|---|---|---|
| AS-1 | Hall/lobby projection 2.5 m | Entrance block depth | Scaled from SKETCH-01 |
| AS-2 | Porch 4.0 × 3.0 m, one roof over two landings | Porch | SKETCH-01 text; porch count conflicts |
| AS-3 | External walls 300 mm | All dimensions | None (r67 TBD) |
| AS-4 | Party (separating) wall 200 mm | Footprint | None (r64–65 TBD); likely to increase |
| AS-5 | Partitions 100 mm | GIA | None |
| AS-6 | Front door leaf ≈ 1,010 mm; internal leaves 926 mm | Openings | Derived from r42–43 clear widths |
| AS-7 | Conservatory 2.5 × 1.5 m hexagonal (S-08) | Provisional outline | Only ORION-sheet dimension |
| AS-8 | Patios 1.8 × 5.0 m | Provisional | None |
| AS-9 | Gardens to the north | Orientation | CONCEPT-01 north arrow |
| AS-10 | Level thresholds | Access | Design intent (r45–46) |
| AS-11 | England jurisdiction | Benchmarks | Research L11; r3 |
| AS-12 | Path 1.5 m, not 2.0 m | Approach | r40 over the compound standard |

## Proposed change log, Draft 0.1 → Draft 0.2 (final version issued with the CAD)

| # | Change | Why | Source |
|---|---|---|---|
| C-1 | Shared internal hall replaced by two private lobbies and halls; party wall continuous | Independence and separation | Research L7, L69; r42, r65 |
| C-2 | Kitchen (Ngaji) 3.0 × 4.0 m + pantry added per home | No kitchen in 0.1 | Research L46, L67; r22–23; Typology §4.1 |
| C-3 | Bedroom 2.8 × 3.5 → 3.5 × 4.2 m; second double 3.0 × 4.2 m added | NDSS 11.5 m² | NDSS 10(d), (e); r24–27 |
| C-4 | Quiet work room 2.5 × 3.2 m added | Programme | Research L49, L65; r28–29 |
| C-5 | Dedicated store 2.25 m² | NDSS storage | NDSS Table 1; r36–37 |
| C-6 | Utility/plant 2.9 × 2.3 m with back door; bathroom with level shower | Programme; access | r30–35, r52–53 |
| C-7 | Living + dining 48 m² → 24 m² combined (if B is chosen) | Programme | r20–21 (conflicts with CONCEPT-01) |
| C-8 | Conservatory 5 × 4 m → provisional 2.5 × 1.5 m outline at the outer rear | 5 × 4 m is not a duplex source | Schedule A3; r4–5; Typology §4, §6; Research L79 |
| C-9 | 1680 mm French pair → one ≥ 900 mm clear leaf per home | Not a duplex source; private entrances | Schedule A4; Typology §6; r6, r42 |
| C-10 | Internal openings widened for 850 mm clear | Access | r43 |
| C-11 | Porch kept 4.0 × 3.0 m, divided into two landings | Two front doors | Typology §4.2; SKETCH-01; r45–46 |
| C-12 | Invented plot boundary removed | No survey | r69 |
| C-13 | Footprint 20.0 × 9.2 → 22.6 × 11.2 m | Consequence of C-1 to C-6 | — |
| C-14 | Title "Draft 0.2"; dimension basis and provisional items stated on the sheet | Traceability | Brief §5 |
