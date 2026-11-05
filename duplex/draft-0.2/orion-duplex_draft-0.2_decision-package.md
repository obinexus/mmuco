# MMUCO ORION Duplex — Draft 0.2 Decision Package

**Status:** numerical and requirements-validation checkpoint · 24 October 2026
**No CAD has been produced.** Draft 0.1 (`MMUCO_ORION_Duplex_Floor_Plan.dxf/.pdf/.png`) is unchanged.
**Supersedes:** §3.3, §3.4 and §4.6 of `MMUCO_ORION_Duplex_Draft_0.2_Audit_Report.md`. The rest of that report stands.

> This is a concept-design checkpoint. Nothing here claims planning permission or Building Regulations compliance. Jurisdiction is assumed to be England (Research L11; Logistics r3). Fire, accessibility, structure and acoustics need review by qualified UK professionals.

### Terms used in this package

| Term | Meaning here |
|---|---|
| **Clear internal** | Finished face to finished face of one room. All room sizes are clear internal. |
| **NIFA** (net internal floor area) | Sum of clear room areas, **including** halls and corridors, **excluding** internal partitions. This is defined for this package; it is not the RICS "NIA". |
| **GIA** | NDSS para 8: floor area within the internal faces of the dwelling's perimeter walls (external walls and the separating wall), **including** internal partitions. GIA = NIFA + partitions. |
| **Footprint / GEA** | Area within the **outer faces** of the external walls, including the whole party wall. Measured per building. |
| **Overall dimension** | External, outer face to outer face. |
| Coordinates | mm. x = 0 at the west outer face; y = 0 at the front outer face of the main block; north +y. Each layout gives the **left** dwelling; the right dwelling is its mirror, x′ = 2·XC − x, where XC is the party-wall centreline. |

**Evidence labels**

- **CONFIRMED**: an explicit statement in a supplied document or an official standard.
- **PROPOSED**: a design allowance in a project document.
- **CONTRADICTED**: sources disagree.
- **UNRESOLVED**: no decision in any source.
- **ASSUMPTION**: introduced by the drafter, with no source.

---

## 1. Corrected calculations (Option B as previously reported)

### 1.1 What did not reconcile

Nothing has been changed. My chat summary listed rooms totalling **114.42 m²** and then stated a GIA of **119.54 m²** without showing the **5.12 m²** of internal partitions that GIA includes (NDSS para 8). The audit report (§3.3) did show that line; the chat summary left it out. The tables below show every term.

**A new finding from this check:** the Option B store and bathroom meet the documented **areas** but **do not contain the documented rectangles** (1.05 × 2.0 m and 2.5 × 3.0 m). The audit report marked both simply "Pass". That is corrected here.

### 1.2 Option B room areas, recomputed from dimensions

| Room | W × D (m, clear) | Area (m²) | Type |
|---|---|---|---|
| Bedroom 1 | 3.50 × 4.20 | 14.70 | Room |
| Bedroom 2 | 3.00 × 4.20 | 12.60 | Room |
| Quiet work room | 2.50 × 3.20 | 8.00 | Room |
| Store | 2.50 × 0.90 | 2.25 | Room |
| Living / dining | 4.80 × 5.00 | 24.00 | Room |
| Kitchen | 3.00 × 4.00 | 12.00 | Room |
| Pantry | 3.00 × 0.90 | 2.70 | Room |
| Bathroom | 2.90 × 2.60 | 7.54 | Room |
| Utility and plant | 2.90 × 2.30 | 6.67 | Room |
| **Rooms excluding circulation** | | **90.46** | |
| Lobby (inside the projection, y −2,200 to 300) | 1.60 × 2.50 | 4.00 | Circulation |
| Hall (inside the main block, y 300 to 5,800) | 1.60 × 5.50 | 8.80 | Circulation |
| Corridor | 9.30 × 1.20 | 11.16 | Circulation |
| **Circulation** | | **23.96** | |
| **NIFA** | | **114.42** | |

**Internal partitions** (100 mm). Each area is computed from its own rectangle, not by subtraction:

| Partition | x (mm) | y (mm) | Length × thickness | Area (m²) |
|---|---|---|---|---|
| P1 Bedroom 1 / Bedroom 2 | 3,800–3,900 | 300–4,500 | 4.20 × 0.10 | 0.42 |
| P2 Bedroom 2 / quiet + store | 6,900–7,000 | 300–4,500 | 4.20 × 0.10 | 0.42 |
| P3 Quiet / store | 7,000–9,500 | 3,500–3,600 | 2.50 × 0.10 | 0.25 |
| P4 Quiet + store / hall | 9,500–9,600 | 300–4,500 | 4.20 × 0.10 | 0.42 |
| P5 Front rooms / corridor | 300–9,600 | 4,500–4,600 | 9.30 × 0.10 | 0.93 |
| P6 Corridor + hall / rear rooms | 300–11,200 | 5,800–5,900 | 10.90 × 0.10 | 1.09 |
| P7 Living-dining / pantry + kitchen | 5,100–5,200 | 5,900–10,900 | 5.00 × 0.10 | 0.50 |
| P8 Pantry / kitchen | 5,200–8,200 | 6,800–6,900 | 3.00 × 0.10 | 0.30 |
| P9 Kitchen / bath + utility | 8,200–8,300 | 5,900–10,900 | 5.00 × 0.10 | 0.50 |
| P10 Bath / utility | 8,300–11,200 | 8,500–8,600 | 2.90 × 0.10 | 0.29 |
| **Partitions** | | | | **5.12** |

**Reconciliation:**

- NIFA 114.42 + partitions 5.12 = **119.54 m² GIA**.
- Independently, the GIA envelope is the main block's internal faces, 10.90 × 10.60 = 115.54, plus the lobby, 1.60 × 2.50 = 4.00, giving **119.54 m²**.
- Difference: **0.00 m²**.
- **Omitted rooms:** none drawn have been left out. The optional additional WC (Logistics r32–33) is not included in any option.
- **Unallocated area:** 0.00 m². A 100 mm raster check found no gaps, no double-counted cells and no overlaps.

### 1.3 Footprint: why 253.12 m² and 263.12 m² are both correct

| Component | Outer-face geometry (mm) | Arithmetic | Area (m²) |
|---|---|---|---|
| Main block | x 0–22,600, y 0–11,200 | 22.60 × 11.20 | **253.12** |
| Entrance projection (two lobbies) | x 9,300–13,300, y −2,500–0 | 4.00 × 2.50 | **10.00** |
| **Enclosed footprint** | | 253.12 + 10.00 | **263.12** |

The report's 263.1 m² **is the main block plus the entrance projection.** The projection was listed on its own row; the total did not spell the addition out. Breakdown of the projection's 10.00 m²:

- Side walls: 2 × 0.30 × 2.50 = 1.50
- Front wall: 3.40 × 0.30 = 1.02
- Party wall: 0.20 × 2.20 = 0.44
- Lobby floors: 2 × 1.60 × 2.20 = 7.04
- Total: 1.50 + 1.02 + 0.44 + 7.04 = **10.00**

*Note:* each lobby's GIA (1.60 × 2.50 = 4.00) is **larger** than its floor inside the projection (1.60 × 2.20 = 3.52). The extra 0.48 m² lies at y 0–300, inside the main-block outline, where the front wall is left out to let the hall through. It is counted once, inside the 253.12.

**Roofed but not enclosed, or provisional:**

| Item | Geometry | Area (m²) | Status |
|---|---|---|---|
| Porch (one roof, two landings) | 4.00 × 3.00 | 12.00 | ASSUMPTION (SKETCH-01) |
| Conservatory, each | S-08 "2.5 × 1.5 m, hexagonal". Bounding rectangle 3.75; **assumed** hexagon with its two outer corners cut 0.75 × 0.75 m: 3.75 − 2 × 0.281 | 3.19 | PROVISIONAL; geometry assumed |
| Conservatories, both | 2 × 3.19 | 6.38 | Excluded from GIA |
| Patios, each | 1.80 × 5.00 | 9.00 | ASSUMPTION (no source) |

Totals:

- Enclosed: 263.12.
- Plus conservatories: 269.50.
- Plus porch: **281.50 m² of roofed area**.

---

## 2. Option comparison

### 2.1 Common basis for all options

- **Programme:** Logistics r20–37 (all PROPOSED). The optional WC (r32–33) is excluded throughout.
  - Kitchen 3.0 × 4.0
  - Bedroom 1 3.5 × 4.0
  - Bedroom 2 3.0 × 4.0
  - Quiet work room 2.5 × 3.2
  - Bathroom 2.5 × 3.0
  - Utility and plant 2.0 × 2.0
  - Store 1.05 × 2.0
- **Dining:** Option A adds a separate 4.8 × 5.0 dining room (CONCEPT-01, S-08). Option B and C use one combined 4.8 × 5.0 living/dining room (r20–21).
- **Every option has:** private entrances; no internal link between homes; a continuous party wall; provisional conservatories.
- **Two tests per room:**
  1. Area at least the documented area.
  2. The documented rectangle fits inside the room, either way round.

The checkpoint needs both, and both are reported.

**Entrance arrangement is a second independent choice,** so the comparison is a 2 × 2 grid:

| Living / dining ↓ · Entrance → | Central shared porch (keeps SKETCH-01) | Own front door and porch per home |
|---|---|---|
| **Combined** | **Option B**: GIA 119.54 | **Option C**: GIA 104.13 |
| **Separate** | Option A1: GIA 144.04 | **Option A** (= A2): GIA 128.61 |

Option A as you defined it is shown as **A2**, the more efficient of the two ways to provide it. A1 is summarised for completeness.

### 2.2 Summary (per dwelling unless stated)

| | **Option A (A2)** | **Option B** | **Option C** | A1 (reference) |
|---|---|---|---|---|
| Bedrooms | 2 double | 2 double | 2 double | 2 double |
| Living / dining | Separate 24.00 + 24.00 | Combined 24.00 | Combined 24.00 | Separate 24.00 + 24.00 |
| Kitchen | 4.00 × 3.20 = 12.80 | 3.00 × 4.00 = 12.00 (+ pantry 2.70) | 4.00 × 3.20 = 12.80 | 12.00 + pantry |
| Entrance | Own door and porch, mid-façade | Private lobby, shared porch roof | Own door and porch, mid-façade | As B |
| Circulation | 9.90 (hall) | 23.96 (lobby 4.00 + hall 8.80 + corridor 11.16) | **9.90** (hall) | 23.96 |
| NIFA | 124.10 | 114.42 | **100.10** | 138.42 |
| Partitions | 4.51 | 5.12 | 4.03 | 5.62 |
| **GIA** | **128.61** | **119.54** | **104.13** | **144.04** |
| GIA vs 110 m² budget (r17) | **+18.61, fails** | **+9.54, fails** | **−5.87, within** | +34.04, fails |
| All documented room **areas** met | Yes | Yes | Yes | Yes |
| All documented **rectangles** fit | Yes (8/8) | **No** (6/8: store, bath) | **Yes (8/8)** | No (store, bath) |
| NDSS 2b4p (≥ 70 m² GIA, ≥ 2.0 m² storage, doubles ≥ 11.5 m²) | Meets the benchmark | Meets | Meets | Meets |
| Habitable rooms with an external window | **No: dining room is internal** (rooflight or borrowed light) | Yes | Yes | Yes |
| Living space aspect | Living dual; dining none | L/D dual (west + north) | L/D **single (north)** | Living dual; dining north |
| Two-home GIA | 257.22 | 239.08 | **208.26** | 288.08 |
| Main block (overall, external) | 18.60 × 12.30 | 22.60 × 11.20 | **18.60 × 12.30** | 22.60 × 11.20 core |
| Other enclosed parts | Rear living wing 10.40 × 5.10 = 53.04 | Entrance projection 4.00 × 2.50 = 10.00 | — | Projection 10.00; two living wings 4.90 × 5.60 = 27.44 each |
| **Enclosed footprint** | **281.82** | **263.12** | **228.78** | **318.00** |
| Porch(es) | 2 × 2.40 × 2.00 = 9.60 | 1 × 4.00 × 3.00 = 12.00 | 2 × 2.40 × 2.00 = 9.60 | 12.00 |
| Conservatories (provisional) | 6.38 | 6.38 | 6.38 | 6.38 |
| Overall width × depth | 18.6 × 17.4 m (19.4 with porches) | 22.6 × 11.2 m (13.7 with projection; 16.7 with porch) | **18.6 × 12.3 m** (14.3 with porches) | 32.4 × 11.2 m (16.7 with porch) |
| Overall dimensions on the 300 mm grid (Site Planning p.5) | Yes | No | **Yes** | No |

**Can a separate-dining option meet both the room programme and 110 m²? No, by arithmetic alone.**

- Documented rooms with separate living and dining: 24 + 24 + 12 + 14 + 12 + 8 + 7.5 + 4 + 2.1 = **107.6 m²**.
- Add the r38 circulation allowance of 10 m²: **117.6 m²**, already over 110 before any partition.
- With combined living/dining the same sum is 83.6 + 10 = 93.6 m², which leaves room for partitions. Option C shows that in a real layout (104.13).

**The 110 m² budget does not override a room requirement.** Both are PROPOSED (r17; r20–37). Options A and B meet every room area and miss the budget. Option C meets both.

### 2.3 Option A (A2): compact plan with separate living and dining rooms

XC = 9,300 (party wall x 9,200–9,400). The rear living wing is shared by both homes and runs x 4,100–14,500.

| Room | x (mm) | y (mm) | W × D (m, clear) | Area | Requirement / source | Area | Rectangle |
|---|---|---|---|---|---|---|---|
| Bedroom 1 | 300–4,300 | 300–4,000 | 4.00 × 3.70 | 14.80 | 3.5 × 4.0 (r24–25) | Pass | Fits |
| Quiet work room | 300–4,300 | 4,100–6,600 | 4.00 × 2.50 | 10.00 | 2.5 × 3.2 (r28–29) | Pass | Fits |
| Utility and plant | 300–2,800 | 6,700–8,700 | 2.50 × 2.00 | 5.00 | 2.0 × 2.0 (r34–35) | Pass | Fits |
| Store | 2,900–4,300 | 6,700–8,700 | 1.40 × 2.00 | 2.80 | 1.05 × 2.0 (r36–37) | Pass | Fits |
| Kitchen | 300–4,300 | 8,800–12,000 | 4.00 × 3.20 | 12.80 | 3.0 × 4.0 (r22–23) | Pass | Fits |
| Hall | 4,400–5,900 | 300–6,900 | 1.50 × 6.60 | 9.90 | Circulation (r41, r44) | — | — |
| Bedroom 2 | 6,000–9,200 | 300–4,300 | 3.20 × 4.00 | 12.80 | 3.0 × 4.0 (r26–27) | Pass | Fits |
| Bathroom | 6,000–9,200 | 4,400–6,900 | 3.20 × 2.50 | 8.00 | 2.5 × 3.0 (r30–31) | Pass | Fits |
| Dining room | 4,400–9,200 | 7,000–12,000 | 4.80 × 5.00 | 24.00 | 4.8 × 5.0 (CONCEPT-01) | Pass | Fits |
| Living room | 4,400–9,200 | 12,100–17,100 | 4.80 × 5.00 | 24.00 | 4.8 × 5.0 (CONCEPT-01) | Pass | Fits |

- **Totals:** NIFA 124.10 + partitions 4.51 (Option C's Q1–Q8 = 4.03, plus Q9 dining/living 0.48) = **GIA 128.61**. The envelope gives the same: 8.90 × 11.70 = 104.13, plus the wing 4.80 × 5.10 = 24.48, = 128.61.
- **Compromises:**
  - The dining room has **no external wall**, so it needs a rooflight (possible on one storey).
  - 18.61 m² over budget.
  - Deep 17.4 m plan.
  - Loses the SKETCH-01 central entrance.
  - The store opens off the dining room.
  - The bathroom is internal (mechanical extract).

### 2.4 Option B: central shared porch, combined living/dining

XC = 11,300. Rooms and partitions are as in §1.2. Coordinates are in §4.

- **Compromises:**
  - 9.54 m² over budget.
  - Circulation is 24 m² against the 10 m² allowance (r38): a 9.3 m corridor.
  - The store (2.50 × 0.90) and bathroom (2.90 × 2.60) do not contain the documented rectangles.
  - The two front doors share one porch roof and need a privacy screen.
  - The party wall must continue through the shared porch roof (fire-stopping to review).
  - The bathroom is internal.
- **Advantages:**
  - Keeps the SKETCH-01 central projecting entrance and the 4.0 × 3.0 m porch as a shared outdoor threshold.
  - Dual-aspect living/dining.
  - Pantry.

### 2.5 Option C: compact, own entrance per home

XC = 9,300. The rooms are those of §2.3 without the living-room wing; the combined **living/dining** occupies x 4,400–9,200, y 7,000–12,000 (4.80 × 5.00 = 24.00).

| Partition (100 mm) | x (mm) | y (mm) | Area (m²) |
|---|---|---|---|
| Q1 Bedroom 1 / quiet | 300–4,300 | 4,000–4,100 | 0.40 |
| Q2 Quiet / utility + store | 300–4,300 | 6,600–6,700 | 0.40 |
| Q3 Utility / store | 2,800–2,900 | 6,700–8,700 | 0.20 |
| Q4 Utility + store / kitchen | 300–4,300 | 8,700–8,800 | 0.40 |
| Q5 West rooms / hall + living | 4,300–4,400 | 300–12,000 | 1.17 |
| Q6 Hall / east rooms | 5,900–6,000 | 300–6,900 | 0.66 |
| Q7 Bedroom 2 / bath | 6,000–9,200 | 4,300–4,400 | 0.32 |
| Q8 Hall + bath / living-dining | 4,400–9,200 | 6,900–7,000 | 0.48 |
| **Total** | | | **4.03** |

- **Totals:** NIFA 100.10 (rooms 90.20 + hall 9.90) + partitions 4.03 = **GIA 104.13** = envelope 8.90 × 11.70.
- **Compromises:**
  - Loses SKETCH-01's single central entrance and 4.0 × 3.0 m porch. It becomes two porches, which matches Typology §4.2 "two porches".
  - The shared threshold becomes the shared front garden and path, a weaker expression than B's.
  - Living/dining is **single-aspect (north if gardens are north)**. Check daylight and overheating.
  - The store opens off the living/dining room.
  - The bathroom is internal.
  - No pantry; larder units in the kitchen.

### 2.6 Option A1 (reference only)

Option B's plan moved 4,900 mm east, with a 4.80 × 5.00 living room added as a west wing (x 300–5,100, y 5,900–10,900) and B's living/dining becoming the dining room.

- GIA = 115.54 + 4.00 + 24.50 = **144.04**.
- Footprint = 253.12 + 10.00 + 2 × 27.44 = **318.00**.
- Inherits B's corridor and the store and bathroom rectangle shortfalls.
- Not recommended.

### 2.7 Every figure that remains an assumption

| Figure | Used in | Status |
|---|---|---|
| External walls 300, party wall 200, partitions 100 mm | All | ASSUMPTION (r64, r67 TBD). See §4.1 |
| Front door opening 1,100 for a ≈1,010 mm leaf; internal openings 1,000 for 926 mm leaves | All | ASSUMPTION, derived from r42–43 clear widths |
| Room dimensions not equal to the documented rectangles (e.g. bedrooms 4.2 m deep in B; kitchen 4.0 × 3.2 in C) | All | Design proposal to fit the plan; each tested above |
| Pantry 3.0 × 0.9 m | B, A1 | Design proposal (brief item 3A); no documented size |
| Entrance projection 2.5 m; porch 4.0 × 3.0 m; porch screen | B, A1 | ASSUMPTION from SKETCH-01 |
| Porch 2.4 × 2.0 m per home | A2, C | ASSUMPTION (meets the r45–46 1.5 × 1.5 m landing) |
| Conservatory 2.5 × 1.5 m (S-08), with 0.75 m corner cuts | All | PROVISIONAL; corner geometry assumed |
| Patios 1.8 × 5.0 m | All | ASSUMPTION |
| Gardens to the north | All | ASSUMPTION from the CONCEPT-01 north arrow |
| Level thresholds | All | ASSUMPTION |
| England jurisdiction | All | ASSUMPTION (Research L11) |
| Path 1.5 m | All | PROPOSED (r40); see register item 5 |

---

## 3. Source-conflict decision register

| # | Item | Evidence (source and exact location) | Classification | Recommended decision (a design proposal, not a requirement) |
|---|---|---|---|---|
| 1 | One or two bedrooms per dwelling | CONCEPT-01 Key Features: "2 Bedrooms" for the duplex; one "Bedroom (2.8 x 3.5 m)" per dwelling; Note 1 "Dimensions are indicative". Typology §4 (S-08): one "Bedroom 4 × 5 m". Research L7: "each with two double bedrooms … This is an explicit working assumption". Logistics r2: "ASSUMPTION — … each 2 bedrooms / 4 bedspaces"; r24–27 PROPOSED | **UNRESOLVED** (drawn sources show one; the written brief assumes two; none confirmed) | Two doubles (2b4p). It is the only written programme, it adapts better, and the quiet room can serve as a single bedroom (NDSS 10(c)). **Your decision.** |
| 2 | Separate or combined living/dining | CONCEPT-01 labels "Living Room (4.8 x 5 m)" and "Dining Room (4.8 x 5 m)"; "2 Living Rooms", "2 Dining Rooms". Typology §4 (S-08): "TV / Living Room 4.8 × 5 m", "Dining Room 4.8 × 5 m"; §4.3 "exactly equal at 24.00 m²". Research L45 and Logistics r20–21: one "Living and dining 4.8 × 5 … 24 m²" (PROPOSED) | **CONTRADICTED** | Combined, unless separate dining is a priority. Separate dining costs ≥ 24.5 m² per home and **cannot** meet 110 m² (§2.2). **Your decision.** |
| 3 | Two or four dwellings | Planning screenshot: "How many new dwellinghouses are you proposing to create? 4". Research L7 ("must be resolved before a planning submission"), L83 ("Confirm two homes or four. Four could mean two duplex buildings"). Logistics r2 ("Four homes … remain unconfirmed"), r19 ("Not adopted base scope"). Typology §5 (S-02): "OBI — 2 per plot household". CONCEPT-01: one duplex | **UNRESOLVED** | Draft 0.2 is one duplex (two homes). If four, repeat the duplex on a site plan once a site exists. Do not submit until confirmed. **Your decision.** |
| 4 | Shared enclosed hallway or shared outdoor connection | CONCEPT-01: shared "Hallway"; "Shared Family Spaces"; Note 2 "extended family living model". Typology §2.2: I-2 "N is the sole enclosed connection"; I-4 "every habitable room has a door onto N". MMUCO ORION.pdf p.9 §7.1: "protected shared threshold". Research L69: "The narrow link is unresolved: choose a covered outdoor connection, an enclosed shared space, or a different arrangement. Each home should have a suitable independent entrance … must not casually breach dwelling fire or acoustic separation." Logistics r54 (link 1.8 m, outside GIA), r55 TBD, r65 TBD | **CONTRADICTED** (typology versus research); the research itself leaves it **UNRESOLVED** | Shared **outdoor** connection only, with no internal link: Option B's shared porch, or C's shared front garden. An enclosed link would need its own fire, acoustic and management design and may change the self-contained status. |
| 5 | Paths 1.5 m or 2.0 m | Logistics r40: "main approach clear width 1.5 — PROPOSED". Research L63 ("project targets, not a claim of Part M compliance"). Zone Specs §1.3 (UCHE zone, Nnewi compound): "Paths, 2m minimum width"; §1.2.3 "Walking paths (2m minimum width…)". Roadmap Phase 3A: "All paths: 2m minimum width, ≤1:12 ramp slope" | **CONTRADICTED**. Both PROPOSED, for different projects; neither binding | 1.5 m for each private approach; 2.0 m for any shared or compound route. Adopting 2.0 m everywhere is cheap if you want the compound standard. |
| 6 | Door clear width 0.9 m or 1.0 m | Logistics r42: "entrance door effective clear width 0.9 — PROPOSED … two private entrances"; r43 internal 0.85. Zone Specs §1.3: "Doors, 1m minimum clear width, Lever handles, no locks (emergency exit always accessible)" | **CONTRADICTED**. The 1.0 m figure is a public-zone standard ("no locks") written for a different site | ≥ 0.9 m clear at front doors, ≥ 0.85 m internal. Fix after the Part M category is chosen; use 1.0 m if you want the compound standard (larger leaves). |
| 7 | Prohibition on square plans | Typology §2.2 I-6: "the wing polygon tessellates the plane; n = 4 is prohibited". §2.7: "The square is prohibited … constitutional, not aesthetic". §9 decision #6 "Square plan prohibited" (from T-01, **not supplied**; §1 rates T-01 "low per phrase"). `mmuco-orion-tessellation.svg`: "The square (n = 4) is prohibited". CONCEPT-01 is rectilinear. Research L23: preserve wing geometry "but test room fit…" | **PROPOSED** design principle in a v0.2 draft, **CONTRADICTED** by CONCEPT-01. Not a regulatory requirement; its source transcript cannot be checked here | All four options are rectilinear and **break I-6**. Recommendation: accept rectilinear for Draft 0.2 and run a separate tessellating-geometry study if you want I-6 honoured; it would change every dimension. **Your decision.** |
| 8a | Conservatory dimensions | Schedule p.1 §2 A3: "Conservatory / covered growing or welfare space, 5 m x 4 m … verify on site" (Phase 1 agricultural project; p.2 §5 "Separate Phase 1 agricultural works from any future housing"). Logistics r4–5: "IMAGE-UNVERIFIED … Not included in base dwelling areas". Typology §6: S-01 **existing Beckton property**, conservatory 5 × 4 m. Typology §4: S-08 "Conservatory (rear, hexagonal) 2.5 × 1.5 m". Research L17 ("Treat dimensions as unverified"), L79 (assess overheating "before fixing glazing or conservatory size"). CONCEPT-01: drawn, undimensioned | **CONTRADICTED**; 5 × 4 m is **not a duplex source** | Provisional S-08 outline (2.5 × 1.5 m), excluded from GIA. Fix the size after an overheating (ADO) assessment. **Your decision on the target size.** |
| 8b | French-door width | Schedule p.1 §2 A4: "1680 mm opening width — Medium … confirm manufacturer/opening size". Typology §6: S-01 "Front French double doors 1.971 × 1.168 m" (existing property). Logistics r6: "TBD — Handwritten numbers unclear". Research L17: "door numbers are unclear" | **CONTRADICTED** (1,680 vs 1,168 from the same handwriting); **not a duplex source** | Do not carry it into the duplex. Specify front doors by clear width (item 6). Size any garden or conservatory doors later. |

---

## 4. Geometry check

### 4.1 Wall thicknesses: all assumptions

No supplied source specifies wall build-ups (Logistics r67 "TBD — Select structural system … before thickness"; r64 acoustic TBD; r65 fire TBD).

| Wall | Assumed | Basis | Likely direction |
|---|---|---|---|
| External | 300 mm | Concept placeholder for a UK insulated cavity wall | May grow to 350 mm or more under Future Homes Standard U-values |
| Party (separating) | 200 mm | Placeholder carried from Draft 0.1 | Likely 250–300 mm for a tested fire and sound system (ADB / ADE). Specialist to confirm |
| Partitions | 100 mm | Typical stud or block | — |

**Sensitivity.** GIA does **not** change with wall thickness, because rooms are fixed clear sizes. Footprint does:

- Each +50 mm on external walls adds 0.10 m to overall width and depth.
- +100 mm on the party wall adds 0.10 m to width.
- With 350 mm external and 300 mm party walls:
  - Option C becomes 18.80 × 12.40 = 233.12 m² (from 228.78).
  - Option B's main block becomes 22.80 × 11.30 = 257.64 m², plus the projection 4.20 × 2.55 = 10.71, giving 268.35 m² (from 263.12).

### 4.2 How the two dwellings fit together

- **Mirror:** each option is drawn for the left dwelling; the right dwelling is the exact mirror about XC. A 200 mm party wall is centred on XC and runs the full depth of the enclosed building.
- **No internal connection:** no room or partition of either dwelling reaches the party wall half (checked).
- **Entrances:**
  - **B:** the two lobbies (each 1.60 m clear) sit either side of the party wall inside the 4.0 m projection, under one porch roof split by a screen on the party-wall line.
  - **C and A2:** each front door is on the dwelling's own front wall at its hall. The porch edges are 5.90 m apart (left porch x 3,950–6,350; right 12,250–14,650).
- **Conservatories:**
  - B: 2.50 m outlines at x 1,450–3,950 and 18,650–21,150, 14.7 m apart.
  - C: x 4,500–7,000 and 11,600–14,100, 4.6 m apart.

#### Option C: openings (left dwelling)

| Opening | Type | In wall | x (mm) | y (mm) | Span (mm) | Connects |
|---|---|---|---|---|---|---|
| Front door (≈1,010 leaf) | Door | W2 front external | 4,600–5,700 | 0–300 | 1,100 | Outside / hall |
| Bedroom 1 door | Door | Q5 | 4,300–4,400 | 2,800–3,800 | 1,000 | Bedroom 1 / hall |
| Quiet room door | Door | Q5 | 4,300–4,400 | 4,300–5,300 | 1,000 | Quiet room / hall |
| Bedroom 2 door | Door | Q6 | 5,900–6,000 | 2,800–3,800 | 1,000 | Hall / Bedroom 2 |
| Bathroom door | Door | Q6 | 5,900–6,000 | 5,000–6,000 | 1,000 | Hall / bathroom |
| Hall to living door | Door | Q8 | 4,650–5,650 | 6,900–7,000 | 1,000 | Hall / living-dining |
| Store door | Door | Q5 | 4,300–4,400 | 7,400–8,400 | 1,000 | Store / living-dining |
| Kitchen opening | Opening | Q5 | 4,300–4,400 | 9,200–11,000 | 1,800 | Kitchen / living-dining |
| Utility door | Door | Q4 | 1,000–2,000 | 8,700–8,800 | 1,000 | Utility / kitchen |
| Utility side door | Door | W1 west external | 0–300 | 7,200–8,200 | 1,000 | Outside / utility |
| Conservatory doors | Door pair | W3 rear external | 5,000–6,500 | 12,000–12,300 | 1,500 | Living-dining / conservatory |
| Bedroom 1 windows | Window | W2 front; W1 west | 1,500–3,000; 0–300 | 0–300; 1,500–2,700 | 1,500; 1,200 | Bedroom 1 / outside |
| Bedroom 2 window | Window | W2 front | 7,000–8,200 | 0–300 | 1,200 | Bedroom 2 / outside |
| Quiet room window | Window | W1 west | 0–300 | 4,800–6,000 | 1,200 | Quiet room / outside |
| Kitchen windows | Window | W3 rear; W1 west | 1,200–2,700; 0–300 | 12,000–12,300; 9,800–11,000 | 1,500; 1,200 | Kitchen / outside |
| Living rear window | Window | W3 rear | 7,300–8,800 | 12,000–12,300 | 1,500 | Living-dining / outside |

**External walls (C, left):**

- W1 west: x 0–300, y 0–12,300.
- W2 front: x 300–9,200, y 0–300.
- W3 rear: x 300–9,200, y 12,000–12,300.
- W4 party, half: x 9,200–9,300.

**External spaces (C):**

- Porch: x 3,950–6,350, y −2,000–0 (ASSUMPTION).
- Patio: x −1,800–0, y 7,000–12,000 (ASSUMPTION).
- Conservatory: x 4,500–7,000, y 12,300–13,800 (PROVISIONAL).
- Path: 1.5 m wide, south of the porch, to the boundary (no site survey).

#### Option B: openings (left dwelling)

| Opening | Type | In wall | x (mm) | y (mm) | Span (mm) | Connects |
|---|---|---|---|---|---|---|
| Front door (≈1,010 leaf) | Door | W4 lobby front | 9,900–11,000 | −2,500 to −2,200 | 1,100 | Outside / lobby |
| Lobby sidelight | Window | W3 lobby side | 9,300–9,600 | −1,800 to −800 | 1,000 | Lobby / outside |
| Quiet room door | Door | P4 | 9,500–9,600 | 2,000–3,000 | 1,000 | Quiet room / hall |
| Store bi-fold doors | Door | P5 | 7,700–8,700 | 4,500–4,600 | 1,000 | Store / corridor |
| Bedroom 1 door | Door | P5 | 2,700–3,700 | 4,500–4,600 | 1,000 | Bedroom 1 / corridor |
| Bedroom 2 door | Door | P5 | 4,000–5,000 | 4,500–4,600 | 1,000 | Bedroom 2 / corridor |
| Living/dining door | Door | P6 | 3,700–4,700 | 5,800–5,900 | 1,000 | Corridor / living-dining |
| Bathroom door | Door | P6 | 9,900–10,900 | 5,800–5,900 | 1,000 | Hall / bathroom |
| Kitchen opening | Opening | P7 | 5,100–5,200 | 8,000–9,800 | 1,800 | Living-dining / kitchen |
| Pantry door | Door | P8 | 6,200–7,000 | 6,800–6,900 | 800 | Pantry / kitchen |
| Utility door | Door | P9 | 8,200–8,300 | 9,400–10,400 | 1,000 | Kitchen / utility |
| Utility back door | Door | W5 rear | 9,900–10,900 | 10,900–11,200 | 1,000 | Utility / outside |
| Patio French doors | Door pair | W1 west | 0–300 | 7,500–9,300 | 1,800 | Patio / living-dining |
| Conservatory doors | Door pair | W5 rear | 1,950–3,450 | 10,900–11,200 | 1,500 | Living-dining / conservatory |
| Bedroom 1, Bedroom 2, quiet room windows | Window | W2 front | 1,300–2,800 / 4,800–6,000 / 7,650–8,850 | 0–300 | 1,500 / 1,200 / 1,200 | Room / outside |
| Corridor window | Window | W1 west | 0–300 | 4,750–5,650 | 900 | Corridor / outside |
| Kitchen window | Window | W5 rear | 6,100–7,300 | 10,900–11,200 | 1,200 | Kitchen / outside |

**External walls (B, left):**

- W1 west: x 0–300, y 0–11,200.
- W2 front: x 300–9,300, y 0–300.
- W3 lobby side: x 9,300–9,600, y −2,500–300.
- W4 lobby front: x 9,600–11,200, y −2,500 to −2,200.
- W5 rear: x 300–11,200, y 10,900–11,200.
- W6 party, half: x 11,200–11,300, y −2,500–11,200.

**External spaces (B):**

- Porch: x 9,300–13,300, y −5,500 to −2,500.
- Patio: x −1,800–0, y 5,900–10,900.
- Conservatory: x 1,450–3,950, y 11,200–12,700.

Options A2 and A1 use C's and B's openings respectively, with the changes listed in §2.3 and §2.6. They were included in the same checks.

### 4.3 Indicative plan of Option C (left home; right home mirrored)

```
 y=12.3 ┌──────────────┬────────────────────────────┐
        │ KITCHEN      │ LIVING / DINING            │  ← conservatory (provisional) off rear wall
        │ 4.0 × 3.2    ═ 4.8 × 5.0                  │
        ├──────┬───────┤                            │
        │UTIL. │ STORE ╡                            ║
        │2.5×2 │1.4×2  │                            ║ party
        ├──────┴───────┼─────door─────┬─────────────╢ wall
        │ QUIET ROOM   ╡  HALL        ╞ BATHROOM    ║ 200
        │ 4.0 × 2.5    │  1.5 clear   │ 3.2 × 2.5   ║
        ├──────────────┤              ├─────────────╢
        │ BEDROOM 1    ╡              ╞ BEDROOM 2   ║
        │ 4.0 × 3.7    │              │ 3.2 × 4.0   ║
 y=0    └──────────────┴──front door──┴─────────────╜
                       [ porch 2.4 × 2.0 ]
                        path 1.5 →
 x=0                 4.3  4.4      5.9 6.0          9.2|9.3 (XC)
```

### 4.4 Verification performed (scripted, 100 mm raster)

| Check | Result |
|---|---|
| No two rooms or partitions overlap; no wall overlaps a room | **Pass**, all four options |
| Rooms plus partitions tile each GIA envelope exactly (no gaps, no double counting) | **Pass**: difference 0.00 m² in each option |
| No room reaches into the party wall | **Pass** |
| Every door and window lies wholly within an external wall or partition and connects the two stated spaces | **Pass** (A1: 21, B: 19, C: 18, A2: 20 openings) |
| Every habitable room has an external wall and a window or glazed door | **Pass**, except **A2 dining room** (no external wall) |
| Footprint by raster union equals the arithmetic sum | **Pass** (263.12 / 228.78 / 281.82 / 318.00) |
| Checker sensitivity (planted overlap, gap and wrong door) | All three faults detected |

---

## 5. Questions that need your decision

In priority order:

1. **Bedrooms:** two double bedrooms per home (2b4p, written brief) or one (CONCEPT-01)?
2. **Living/dining:** combined 24 m², or separate 24 + 24 m², accepting at least +24.5 m² per home and missing the 110 m² budget?
3. **Entrance:** a central shared porch (keeps your sketch; Option B) or each home with its own front door and porch (Option C)?
4. **Two or four dwellings** for this proposal and any planning application?
5. **Square-plan principle (Typology I-6):** accept a rectilinear Draft 0.2, or commission a tessellating-geometry study first?
6. **Conservatory:** keep the provisional S-08 2.5 × 1.5 m outline, or set a target size to test against overheating?
7. **Accessibility target:** M4(1), M4(2) or M4(3)? This decides door widths (0.9 or 1.0 m), bathroom layout and thresholds.
8. **Paths:** 1.5 m private approaches, or the 2.0 m compound standard everywhere?
9. **Optional WC:** include it? About +2.5 m² GIA; it fits within 110 m² only in Option C, with a layout change not yet drawn.

## 6. Recommendation

**Option C**, a change from my earlier recommendation of B. Now that the compact layout has been worked out and checked, C beats B on every measured criterion except keeping your sketch's central entrance:

1. **The only option that satisfies both tests.** Every documented room area **and** rectangle fits (8/8), and GIA is 104.13 m², within the 110 m² budget. B misses the budget by 9.54 m² and two rectangles.
2. **Circulation 9.90 m²**, in line with the 10 m² allowance (r38). B's is 23.96 m².
3. **Independence:** its own front door, porch and hall per home; no shared internal space. Every bedroom and the quiet room opens off a 1.5 m hall that leads straight to the front door.
4. **Smallest footprint:** 228.78 m² against 263.12 m² for B. Overall 18.6 × 12.3 m, on the 300 mm grid (Site Planning p.5).
5. **Matches "two porches"** (Typology §4.2).

**Accepting C means:**

- Giving up the single central entrance and 4 × 3 m porch.
- A north-facing single-aspect living/dining room, which needs a daylight and overheating check.
- The store opening off the living room.
- An internal bathroom.

If a separate dining room matters more than the budget, choose **A (A2)** rather than A1: 128.61 m² against 144.04 m². It needs a rooflight over the dining room.

**Waiting for your approval before any Draft 0.2 CAD is produced.**
