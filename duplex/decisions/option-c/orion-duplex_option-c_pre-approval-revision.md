# MMUCO ORION Duplex — Option C Pre-Approval Revision

**Status: NOT APPROVED.** Every item below is a recommendation awaiting your explicit approval. 24 October 2026.

- **CAD:** none generated, overwritten or finalised. Draft 0.1 (`MMUCO_ORION_Duplex_Floor_Plan.*`) is unchanged.
- **Earlier documents:** the earlier packages and the decision sheet are kept as the record. This revision sits on top of them.

> Concept design only. A passing geometry test shows that a layout *can* accommodate a provision. It is **not** evidence of compliance with Building Regulations Parts B, E, F, K, L, M or O, or with any planning condition. That needs detailed design, calculation and review by building control and qualified UK professionals. Jurisdiction is assumed to be **England**.

**Labels:**

- **VERIFIED:** read from the official document; ADM tables and diagrams were read from pages rendered from the official PDF.
- **TESTED:** checked by script against the coordinate model.
- **DERIVED:** calculated from verified guidance and the layout.
- **ASSUMPTION:** a generic input with no project source.
- **ESTIMATE:** an output that depends on assumptions.
- **UNCERTAIN:** not yet established.
- **Modelled values: none.** No SAP 10.2 / Home Energy Model, dynamic thermal (CIBSE TM59) or daylight simulation has been run.

---

## 1. Provisional baseline: C2 = M4(2) + Bathroom A (NOT APPROVED)

The room layout is unchanged from the Option C approval package: **GIA 104.13 m² per dwelling** and **footprint 18.6 × 12.3 m = 228.78 m²**. Only fittings, door positions and furniture change.

| Change from the approval-package layout | Reason (source) | Status |
|---|---|---|
| Bathroom fitted as **A**: bath 1,700 × 700 (over-bath shower), WC (centreline 450 mm from the party wall), basin; provision for a level-access shower at the bath position | ADM 2.29a–c, Diagram 2.5 | TESTED |
| Bathroom door y 5,000–6,000, **opens outward** into the hall | ADM 2.27d | TESTED |
| Conservatory door widened to a **1,000 mm opening (≈ 850 clear) at x 4,700–5,700**, leading-edge nib 300 mm on the west | ADM 2.21 → 2.20d, f (also meets M4(3) 3.23) | TESTED |
| Dining table moved **300 mm east** (x 6,300–7,900) to keep a 1.0 m route to the conservatory door | Furniture and route test | TESTED |
| Living-room principal window sill **≤ 850 mm** above floor | ADM 2.24c | Elevation detail; not in the plan |
| One openable rooflight over the south half of the living/dining room (§4) | Daylight (issue E1) | Roof element; not in the plan |
| MVHR unit within the existing 600 × 600 mm plant allowance in the utility room (§3) | ADF 1.67–1.73 | Space allowance only (ESTIMATE of unit size) |

**C2 room schedule** (clear internal, mm):

| Room | Size | Area (m²) |
|---|---|---|
| Bedroom 1 | 4,000 × 3,700 | 14.80 |
| Quiet work room | 4,000 × 2,500 | 10.00 |
| Utility and plant | 2,500 × 2,000 | 5.00 |
| Store | 1,400 × 2,000 | 2.80 |
| Kitchen | 4,000 × 3,200 | 12.80 |
| Hall | 1,500 × 6,600 | 9.90 |
| Bedroom 2 | 3,200 × 4,000 | 12.80 |
| Bathroom | 3,200 × 2,500 | 8.00 |
| Living / dining | 4,800 × 5,000 | 24.00 |
| **NIFA** | | **100.10** |
| Partitions | | 4.03 |
| **GIA** | | **104.13** |

---

## 2. M4(3)(a) alternative: C3 (concise; NOT APPROVED)

**What M4(3) adds (VERIFIED, ADM Vol 1):**

- A second WC for dwellings with ≥ 4 bedspaces (3.36b). It must meet Diagram 3.13; Example 3.14A is 1,200 × 1,700 mm with the door opening outward (3.40).
- A wheelchair storage and transfer space of 1,100 × 1,700 mm off a space ≥ 1,200 mm wide, with a power socket, **additional to** the general storage (3.25).
- An installed level-access shower 1,200 × 1,200 mm with potential for a bath over it (3.41a; Diagram 3.10).
- 1,500 mm kitchen clearance (3.32b) and worktop ≥ 4,730 mm (Table 3.3).
- Bedroom zones of 1,000 mm and 1,200 × 1,200 mm manoeuvring space (3.35).
- At the entrance: a 1,500 × 1,500 mm landing covered 1,200 × 1,200 mm, a 1,500 turning circle inside, and 300 / 200 mm nibs (3.22).
- 300 / 200 mm nibs on every door (3.24f, g).
- A hoist-ready ceiling (3.35c).

**How C3 provides them:** each dwelling gets a **front projection** (x 2,900–7,500, y −2,000 to 0, external) centred on the hall. It holds:

- the wheelchair storage space, west of the hall;
- the hall itself, extended forward 2.0 m;
- the WC/cloakroom, east of the hall.

```
          ┌─────────── projection 4.6 × 2.0 m (external) ───────────┐
 y=0      │ WHEELCHAIR   │   HALL (extended)   │ WC/CLOAKROOM │       ← old front-wall pieces retained
          │ STORAGE      │   1.5 clear         │ 1.2 × 1.7    │         as internal walls
          │ 1.2 × 1.7    │ ( 1500 turning )    ⇠ door (out)   │
 y=-2000  └──────────────┴──── front door ─────┴──────────────┘
                         [ porch 2.4 × 2.0, moved forward ]
```

### C3 room schedule (per dwelling; clear internal)

| Room | W × D (mm) | Area (m²) | Requirement (VERIFIED source) | Test |
|---|---|---|---|---|
| Bedroom 1 (principal) | 4,000 × 3,700 | 14.80 | ≥ 13.5 m², ≥ 3 m wide; 1,000 mm zones; 1,200 manoeuvring (3.35d, e) | Pass with wardrobe on the south wall and bed moved 450 mm east |
| Quiet work room | 4,000 × 2,500 | 10.00 | r28–29; 1,200 × 1,200 inside the door if used as a bedroom (3.35b) | Pass |
| Utility and plant | 2,500 × 2,000 | 5.00 | r34–35 | Pass |
| Store (general storage) | 1,400 × 2,000 | 2.80 | ≥ 2.0 m² for 2 bedrooms (Table 3.1) | Pass |
| Kitchen | 4,000 × 3,200 | 12.80 | 1,500 clear (3.32b); worktop ≥ 4,730 (Table 3.3) | Pass: 2.0 m clear; worktop ≈ 6,300 mm |
| **Hall (extended)** | 1,500 × 8,600 | **12.90** | ≥ 1,050 / 1,200 (3.24a, b); 1,500 turning inside the entrance (3.22d) | Pass |
| Bedroom 2 | 3,200 × 4,000 | 12.80 | 1,200 manoeuvring (3.35b) | Pass |
| Bathroom **B** (level-access shower) | 3,200 × 2,500 | 8.00 | 3.41a; Diagram 3.10; wet room (3.36c) | Pass. Door moved to y 4,600–5,600 for the 200 mm following-edge nib |
| Living / dining | 4,800 × 5,000 | 24.00 | Living + dining + kitchen ≥ 29 m² (Table 3.2) | Pass (36.8 m²) |
| **Wheelchair storage / transfer** | 1,200 × 1,700 | **2.04** | 1,100 × 1,700 off a ≥ 1,200 space, with socket (3.25) | Pass |
| **WC / cloakroom** | 1,200 × 1,700 | **2.04** | Diagram 3.13; Example 3.14A; outward door (3.40) | Pass. WC centreline 450 mm; hand-rinse basin encroaches 200 mm (the permitted maximum) |
| **NIFA** | | **107.18** | | |
| Partitions and retained internal wall pieces | | 4.95 | | |
| **GIA per dwelling** | | **112.13** (+8.00) | Budget 110 m² (r17) | **Exceeds the budget by 2.13 m²** |
| **Two dwellings** | | 224.26 | Research L59: 220 | Over by 4.26 |

**Footprint:**

- Main block 228.78 m² + 2 projections × (4.60 × 2.00 = 9.20 m²) = **247.18 m²** (+18.40).
- Overall depth 12.3 m + 2.0 m projection = **14.3 m**, or 16.3 m with the porch (moved forward 2.0 m).
- Width unchanged at 18.6 m.

**Consequences:**

- **Front elevation:** the bedroom windows move to clear the projection. Bedroom 1 goes to x 1,300–2,800, 100 mm from the projection face; Bedroom 2 to x 7,800–9,000, 300 mm from it. Expect some loss of daylight and a privacy edge to resolve (UNCERTAIN).
- **Entrance:** the front door becomes a 1,000 mm opening (≈ 850 clear) to give 300 / 200 mm nibs.
- **Not covered:** M4(3)(2)(**b**) "accessible" is not covered. The Diagram 3.11 bathroom, the 6,530 mm worktop with a 2,200 mm adjustable section (3.34) and the full wheelchair-accessible fit-out are not tested.

---

## 3. MVHR vs MEV: assumptions and calculations (all ESTIMATES; nothing modelled)

| Input | Value used | Type | Source / what replaces it |
|---|---|---|---|
| Whole-dwelling ventilation rate Q | max(0.3 × 104.13, 25) = **31.2 l/s** (112 m³/h) | DERIVED | ADF 2021 whole-dwelling rate + Table 1.3 (VERIFIED). Occupancy-based checks in the final design |
| Occupancy | 4 persons (2b4p) | ASSUMPTION (Logistics r2) | Here the rate is set by floor area, not occupancy. Occupancy affects moisture and boost use |
| Air heat capacity | 1.206 kJ/m³K | Physical constant (approx.) | — |
| Ventilation heat-loss coefficient H | 1.206 × 0.0312 = **37.7 W/K** | DERIVED | — |
| Climate: heating degree-days (15.5 °C base) | **1,800 / 2,100 / 2,400** K·day | ASSUMPTION (generic England range) | Site-specific degree-day data once the site is known |
| Annual ventilation heat loss | 37.7 × DD × 24 / 1000 = **1,628 / 1,899 / 2,170 kWh/yr** | ESTIMATE | SAP/HEM model |
| MVHR in-use heat-recovery efficiency | **70 / 80 / 90 %** | ASSUMPTION (generic; laboratory figures are usually higher than in use) | Product Characteristics Database (PCDB) data for the selected unit |
| Heat recovered (DD 2,100) | **1,329 / 1,519 / 1,709 kWh/yr** | ESTIMATE | SAP/HEM |
| Fan specific power | MVHR 0.5 / 0.8 / 1.2 W/(l/s); MEV 0.3 / 0.45 / 0.6 W/(l/s) | ASSUMPTION | PCDB / manufacturer data at the commissioned flow |
| Fan electricity (continuous, 8,760 h) | MVHR **137 / 219 / 328 kWh/yr**; MEV **82 / 123 / 164 kWh/yr**; difference at mid values **≈ 96 kWh/yr** | ESTIMATE | Commissioning records |
| Heating system | Heat pump SCOP 3.0, **or** gas boiler 90 % | ASSUMPTION | Heating design |
| Net delivered-energy effect (mid values) | Heat pump: 1,519 / 3.0 = 506 kWh saved − 96 kWh fan = **≈ 410 kWh/yr electricity saved**. Gas: **≈ 1,690 kWh/yr gas saved**, offset by ≈ 96 kWh/yr extra electricity | ESTIMATE | SAP/HEM |
| Running-cost effect | ≈ **£110/yr** in the heat-pump case at an assumed £0.27/kWh | ESTIMATE (illustrative price) | Current tariffs |
| **Airtightness** | Infiltration ≈ q50 × envelope area / 20. Envelope ≈ 282 m² (floor + roof + external walls, party wall excluded). q50 = 3 / 5 / 8 m³/(h·m²) gives **≈ 11.7 / 19.6 / 31.3 l/s** of leakage, i.e. **38 / 63 / 100 %** of the mechanical rate, **none of it recovered** | ASSUMPTION (rule of thumb) | Design air-permeability target and an air test. **MVHR is only worthwhile with a tight envelope** (target to be set by the energy designer; the Part L limit is UNCERTAIN here) |
| Maintenance | Filters about every 6–12 months (≈ £40–£120/yr); access to unit, coils and ducts (ADF 1.8, VERIFIED); duct cleaning about every 5–10 years | ESTIMATE | Manufacturer O&M; MEV filters and grilles about annually |
| Capital cost | MVHR ≈ **£4k–£8k** vs MEV ≈ **£1.5k–£3k** installed per dwelling | ESTIMATE (generic market range, not quotations) | Quantity surveyor / contractor quotes |
| Noise | ≤ 30 dB L<sub>Aeq,T</sub> in bedrooms and living rooms at low rate; ≤ 45 dB in kitchens and bathrooms | Guidance (ADF 1.5–1.7, VERIFIED) | Commissioning measurements |
| Ducts | MVHR: about 5 supply + 3 extract terminals, plus insulated intake and exhaust; needs a roof void (roof not designed). MEV: 3 extract runs + 4 background ventilators of ≥ 4,000 mm² each (ADF 1.64, VERIFIED) | DERIVED layout / ASSUMPTION routes | Services design |

**Reading of the estimates:** on energy alone, the payback of MVHR's extra capital is long. **ESTIMATE:** roughly (£4k–£8k − £1.5k–£3k) / ≈ £110/yr, i.e. decades. The case for MVHR in Option C rests on:

- the internal bathroom;
- no trickle vents in ground-floor bedrooms (security, noise);
- filtered supply air;
- comfort with windows closed;
- Research L75.

Energy saving is not the deciding factor. Recommendation unchanged (MVHR, MEV fallback), **NOT APPROVED**, subject to the energy model and quotations.

---

## 4. Rooflight recommendation (NOT APPROVED)

| Aspect | Recommendation and rationale |
|---|---|
| **Position** | One unit over the south half of the living/dining room, about x 6,000–7,200, y 7,700–8,900: centred in the darkest zone, about 2.0 m from the party-wall face. Avoid placing it directly above the TV wall, because of glare |
| **Size** | ≈ **1.0 m² net glazing** (about a 1.2 × 1.2 m nominal unit; ESTIMATE). Final size by daylight calculation |
| **Daylight rationale** (BRE average daylight factor DF = T·Aw·θ / (A(1−R²)); A = 97 m², R = 0.5; vertical glazing T = 0.68, rooflight T = 0.60, θ = 180°; ESTIMATE, generic method) | **Without rooflight:** north window 1.41 m² + glazed door 1.24 m² net gives DF ≈ **2.2 %** with an open outlook (θ 90°), or ≈ **1.5 %** if a conservatory or fence obstructs (θ 60°). Most of it is near the north wall, and the room is 5.0 m deep. **With a 1.0 m² rooflight:** ≈ **3.7 % / 3.0 %**, with light delivered to the back of the room. Assessment against BS EN 17037 and its UK National Annex targets by a specialist is **UNCERTAIN / required** |
| **Openable area** | Purge for living/dining needs ≥ **1.20 m²** openable (1/20 of 24 m², hinged ≥ 30°, sash or doors; ADF Table 1.4, VERIFIED). Provide this from the north window (casement ≥ 30°) **plus** an openable rooflight. The high-level opening adds stack ventilation. A rain sensor and actuator are recommended |
| **Shading** | Solar-control glazing (g ≈ 0.4, ASSUMPTION), plus an **external** blind or awning (most effective), or an internal blind as the minimum |
| **Overheating** | Peak summer gain through 1.0 m² is ≈ **340 W** with g 0.4 and ≈ **70 W** with an external blind (ESTIMATE, at about 850 W/m² on the horizontal). The ADO-style glazing share of living/dining rises from 12.3 % to 16.9 % (room area capped at 4.5 m depth per ADO Appendix A, VERIFIED), still under the 37 % most-glazed-room limit for north / cross-ventilated (Table 1.1). **How rooflights are classified in the simplified method is UNCERTAIN**, so a TM59 assessment may be needed |
| **Fallback** | Sun pipe(s) if the roof form makes a rooflight impractical |

**Questions to be confirmed by building control or a qualified designer:**

1. ADO: how are horizontal rooflights treated in the simplified method (orientation, glazing area, free area)? Or is a TM59 assessment needed?
2. ADF: does the rooflight's opening (angle and type) count toward purge ventilation under Table 1.4?
3. ADB: what are the limits on rooflights and roof coverings near the separating (compartment) wall, and the roof-junction fire-stopping?
4. Part L: rooflight U-value, kerb thermal bridging and condensation risk.
5. Structure: is the roof form (r68 TBD) suitable, and how are the trimming and the kerb or upstand detailed?
6. Daylight: a BS EN 17037 / UK National Annex assessment of the final room and glazing.
7. Maintenance and safety: cleaning and repair access to the roof (CDM, working at height); actuator servicing.
8. Security, plus rain and wind closure for an openable unit on a single-storey roof.
9. Acoustics: rain noise on the rooflight.
10. Planning: is the roof alteration visible, and is it acceptable under any local design code?

---

## 5. Outstanding decisions and site-dependent assumptions

| # | Item | Type | Current position | Evidence needed to resolve | Who |
|---|---|---|---|---|---|
| 1 | Approve the C2 layout (M4(2) + Bathroom A) | Decision | Proposed | Your approval | You |
| 2 | Accessibility standard: M4(2) or M4(3)(a)/(b), and for which home | Decision + planning | M4(2) proposed | Local plan policy and any planning condition (ADM 0.3, 0.5); intended occupants | Planning adviser / you |
| 3 | Bathroom A or B | Decision | A (follows #2) | Decision #2; your preference | You |
| 4 | Accept the M4(3) area overrun (112.13 m²) if M4(3) is chosen | Decision | Not applicable unless #2 = M4(3) | Budget confirmation | You / QS |
| 5 | Rooflight (or sun-pipe fallback) | Decision | Rooflight proposed | Roof form; daylight and overheating checks (§4 questions) | You / architect / BC |
| 6 | MVHR or MEV | Decision | MVHR proposed | SAP/HEM model; air-tightness target; quotations | Energy / services designer, QS |
| 7 | Food storage: larder units (walk-in pantry does not fit without compromise) | Decision | Larder units | Your acceptance | You |
| 8 | Two or four dwellings | Decision + planning | Two | Planning scope (screenshot conflict) | You / planning adviser |
| 9 | Square-plan principle (Typology I-6) | Decision | Rectilinear kept | Your design intent | You |
| 10 | Optional WC (M4(2) route) | Decision | Not included | Your preference (fits within budget only with a re-plan) | You |
| 11 | Site address, boundary, levels | Site assumption | Unknown | Title plan; measured and topographic survey | Surveyor |
| 12 | Orientation (gardens north) | Site assumption | From CONCEPT-01 only | Site plan with true north | Surveyor / architect |
| 13 | ADO risk location (moderate or high) | Site assumption | Unknown | Site postcode against ADO Appendix C | Energy designer |
| 14 | Planning authority, NDSS adoption, M4 conditions, London Plan if applicable | Site / planning | Unknown | Local plan; pre-application advice | Planning adviser |
| 15 | Heating degree-days, climate | Site assumption | Generic 1,800–2,400 K·day | Site-specific climate data | Energy designer |
| 16 | Wall build-ups (300 / 200 / 100 mm) | Assumption | Placeholder | Structural, fire (ADB), sound (ADE) and Part L specification | Engineers / architect |
| 17 | Roof form and ceiling height (2.5 m assumed; affects GIA headroom, rooflight, ducts, hoist structure) | Assumption | Not designed (r68) | Roof design; structural engineer | Architect / engineer |
| 18 | Conservatory size (S-08 2.5 × 1.5 m provisional) | Provisional | Excluded from GIA | Target size; ADO / Part L; planning | You / architect |
| 19 | Path width (1.5 m vs 2.0 m) | Provisional | 1.5 m (≥ 1,200 for M4) | Site layout; compound-standard decision | You |
| 20 | Battery storage location | Provisional | Not placed | Specialist fire and electrical design (e.g. domestic battery guidance; not reviewed here) | Specialist |
| 21 | External works (porches, patios, drainage, parking, bins) | Provisional | Placeholders | Survey; drainage strategy; planning requirements | Architect / engineer |
| 22 | Approach gradients and thresholds (level or ≤ 15 mm) | Site assumption | Assumed level | Levels survey; threshold and drainage detail (ADM 0.15) | Architect |
| 23 | Door products (actual clear widths ≥ 850) | Assumption | Openings sized | Door schedule and product data | Architect |
| 24 | Separating-wall fire and sound performance; porch and roof junctions | Assumption | Not designed | Fire strategy; ADE robust details or testing | Fire engineer / acoustician |

---

## 6. Verification after the proposed changes (TESTED; geometry only, not compliance)

| Check | C2 baseline (M4(2) + A) | C3 alternative (M4(3)(a)) |
|---|---|---|
| Room dimensions vs documented rectangles | All pass, including store 1.05 × 2.0 and bathroom 2.5 × 3.0 | All pass, plus wheelchair storage 1.1 × 1.7 and WC 1.2 × 1.7 |
| GIA (exact) | 104.13 m²; NIFA 100.10 + partitions 4.03 | 112.13 m²; NIFA 107.18 + partitions 4.95 |
| Footprint (exact) | 228.78 m² | 247.18 m² |
| No overlaps / full tiling / openings in walls connecting the stated rooms | Pass | Pass |
| Furniture and clear zones | All 9 rooms pass: M4(2) bedroom zones; Diagram 2.5 bathroom zones; 1,200 kitchen; 1.0 m routes | All 11 rooms pass: M4(3) bedroom 1,000 zones and 1,200 manoeuvring; Diagram 3.10 bathroom; Diagram 3.13 WC; 1,500 kitchen; wheelchair storage access; entrance turning circle |
| Door swings | No furniture in any swing. Outward bathroom door crosses the hall while open | No furniture in any swing. The WC and bathroom doors open outward across the hall while open |
| Door nibs | M4(2): every inward-opening door has ≥ 300 mm on the pull side (front, both bedrooms, quiet room, hall-to-living, utility) | M4(3): every door has ≥ 300 mm leading and ≥ 200 mm following on each internal face. Front door 300 / 200 |
| Circulation | Hall 1.5 m; turning circle at the entrance clear of the door swing | Hall 1.5 m, extended 2.0 m; 1,500 turning circle in front of the closed front door |

---

## 7. Decision table (all NOT APPROVED)

| # | Design choice | Recommended option | Evidence and source | Impact on layout and area | Outstanding risk | **Your approval status** |
|---|---|---|---|---|---|---|
| 1 | Accessibility standard | **M4(2)** (provisional baseline C2) | ADM 0.3, 0.5, 2.20–2.30 (VERIFIED) | None to area; door, sill and nib details | Planning conditions unknown | ☐ NOT APPROVED |
| 2 | M4(3)(a) alternative | Hold as alternative **C3** | ADM 3.22–3.41, Tables 3.1–3.3, Diagrams 3.10, 3.13 (VERIFIED) | GIA **112.13** (+8.00); footprint **247.18** (+18.40); front projection | Exceeds budget by 2.13 m²; front windows and elevation; (b) not covered | ☐ NOT APPROVED |
| 3 | Bathroom | **A** with M4(2) / **B** with M4(3) | ADM 2.29, 3.41; Diagrams 2.5, 3.10 (VERIFIED); TESTED | None; B moves the door | Wet-room or drainage detailing; outward doors | ☐ NOT APPROVED |
| 4 | Living/dining daylight | **Openable rooflight ≈ 1.0 m²** with solar control and external blind | ADF Table 1.4; ADO App. A, Table 1.1 (VERIFIED); DF ESTIMATE | Roof opening; no plan change | §4 questions 1–10 | ☐ NOT APPROVED |
| 5 | Ventilation | **MVHR** (MEV fallback) | ADF 1.5–1.8, 1.60–1.73 (VERIFIED); §3 ESTIMATES | Plant allowance in utility; ducts to about 8 terminals | Airtightness, roof void, cost, commissioning | ☐ NOT APPROVED |
| 6 | Food storage | **Tall larder units** | Pantry tests (TESTED) | None | Capacity preference | ☐ NOT APPROVED |
| 7 | Conservatory door | **1,000 opening at x 4,700–5,700**; table moved 300 east | ADM 2.21, 3.23 (VERIFIED); TESTED | None to area | — | ☐ NOT APPROVED |
| 8 | Living-room window sill | **≤ 850 mm** | ADM 2.24c / 3.31c (VERIFIED) | Elevation only; slight glazing increase | ADO re-check | ☐ NOT APPROVED |
| 9 | Conservatory size, wall build-ups, orientation, path width, battery, external works | **Keep provisional** | §5 items 16–22 | — | See §5 | ☐ NOT APPROVED |
| 10 | Carried over: 2 or 4 dwellings; square-plan principle; optional WC | Unchanged | Earlier packages | — | Planning scope; design intent | ☐ NOT APPROVED |

**Waiting for your explicit approval. No Draft 0.2 CAD will be generated until you give it.**

### Sources

- [ADM Vol 1 (gov.uk page)](https://www.gov.uk/government/publications/access-to-and-use-of-buildings-approved-document-m); [ADM Vol 1 PDF](https://assets.publishing.service.gov.uk/media/5a7f8a82ed915d74e622b17b/BR_PDF_AD_M1_2015_with_2016_amendments_V3.pdf): paras 0.3–0.6, 2.20–2.30, 3.22–3.43; Tables 2.1, 3.1–3.4; Diagrams 2.5, 3.10, 3.11, 3.13, 3.14 (rendered pages 25, 28, 42, 44–46, 50, 51, 53)
- [ADF Vol 1, 2021](https://assets.publishing.service.gov.uk/media/61deba42d3bf7f054fcc243d/ADF1.pdf): 1.5–1.8, 1.24–1.31, 1.48–1.52, 1.60–1.73; Tables 1.1–1.4
- [ADO, 2021](https://assets.publishing.service.gov.uk/media/6218c5aad3bf7f4f0b29b624/ADO.pdf): 1.3–1.13, 3.6–3.7, Appendix A
- [NDSS](https://www.gov.uk/government/publications/technical-housing-standards-nationally-described-space-standard/technical-housing-standards-nationally-described-space-standard)
- Project sources as cited in the earlier packages
