# Backyard concept: README

**MMUCO ORION TRIPLEX COMPOUND — BACKYARD CONCEPT — NOT ISSUED** (25 Oct 2026)

This folder holds a 2D site concept made at the user's direct request: "create a backyard.dxf to complete the duplex and add a garage for car storage". It shows the Orion Duplex housing, the backyard (public garden plus shared patio/walkway) and a garage.

**It is a concept, not a design.** It is not for construction, planning or Building Regulations, and it makes no compliance claim.

| File | What it is |
|---|---|
| `backyard.dxf` | DXF R12 in mm, with 317 entities on 28 layers. The housing is on the `REF-` layers; the compound is on the `TX-` layers |
| `backyard_preview_NOT_ISSUED.png` | A preview rendered by CADCraft from `backyard.dxf` |
| `backyard_checks_output.txt` | Output of the independent read-back check (14 PASS, including a positive control) |
| `scripts/make_backyard_dxf.mjs` | The generator. It refuses any source that is not the issued Draft 0.2.2 copy (it checks the sha256) |
| `scripts/check_backyard_dxf.mjs` | The checker. It re-parses the saved DXF and measures areas, angles, sizes, containment and separations |
| `MANIFEST_NOT_ISSUED.sha256` | Hashes of every file in this folder |

To regenerate, run from the workspace folder:

```bash
node backyard-concept_NOT-ISSUED/scripts/make_backyard_dxf.mjs source-copies/MMUCO_ORION_Duplex_Draft_0.2.2.dxf backyard-concept_NOT-ISSUED/backyard.dxf
```

```bash
node backyard-concept_NOT-ISSUED/scripts/check_backyard_dxf.mjs backyard-concept_NOT-ISSUED/backyard.dxf
```

## What is in the drawing

| Item | Value | Class |
|---|---|---|
| Housing | Copied unchanged from the `source-copies/` copy of Draft 0.2.2 (187 entities): walls, glazing, doors, roof, provisional works and paths. Legend swatches are excluded. 26 external piers span 18,600 × 12,300 | VERIFIED as drawn |
| Private rear gardens A and B | 4.0 m deep behind the rear wall, divided on the party-wall line, each with a 1.0 m gate | PLACEHOLDER |
| Public node (garden + patio/walkway) | 22.2 × 20.611 m = **457.56 m²** = 2.000 × 228.78 (D2, reading A, basis H1). It spans the full site width, including the side patios. **This departs from D3's default of the housing width only**, because two ±45° orangeries do not fit in 18.6 m with a walkway between them | PLACEHOLDER |
| Shared walkway | 2.0 m wide (D4), 56.58 m². 45° branches run from each private-garden gate to a spine on the party-wall line, which leads to the back gate | PLACEHOLDER |
| Garden (public node minus walkway) | 400.98 m² = 1.753 × housing | Measured from the drawing |
| Fixed canopy | 8.0 × 6.0, overhead, 4.5 m off the rear wall so it does not darken the house (D14). It falls towards the well | PLACEHOLDER |
| Rainwater well | Ø 1.5, covered. **Not drinking water** | PLACEHOLDER |
| Pond | 6.0 × 4.0. **Not a swimming pool** (user decision, gate report section 11). Depth and edge safety are UNRESOLVED | PLACEHOLDER |
| Fountain | Ø 1.5, dashed. Optional; D6 is not approved | PLACEHOLDER |
| Orangeries | 2 × (8.0 × 5.0), at +45° and −45° to the X axis (D5), at the sunny far end. The glazing faces SE and SW, towards the house | PLACEHOLDER |
| Shed, kennel, cat shelter | 3.0 × 2.4; 2.4 × 1.8; 1.2 × 0.9 | PLACEHOLDER |
| Back gate | 1.2 m, on the far boundary, at the end of the walkway spine | PLACEHOLDER |
| **Garages (D19; the user chose one per side)** | Two single garages, one per dwelling, **one on each side**, mirrored about the party-wall line. Each is 3.0 × 6.0 m internal, with 200 mm walls (3.4 × 6.4 external), one car, and a 2.4 m door to the street side. Each is 4.2 m from its gable. Each has a 3.4 × 6.0 driveway to the street (the street's position is UNKNOWN). Both gables lose some light: dwelling A's in the evening, dwelling B's in the morning | PLACEHOLDER. Common UK guidance is about 3.0 × 6.0 m per car; check the local parking standard |
| **Generator service yard (D20 proposal)** | A 2.0 × 1.0 × 1.5 enclosure with 1.0 m clearance, behind garage A. It is **outside the shared garden**, and 13.5–23.6 m from the canopy, orangeries, well and pond. It is 6.6 m from the dwelling A gable, which raises noise near the homes. The fuel store is not shown | PLACEHOLDER; location NOT FIXED |
| Provisional boundary | T-shaped: wider at the front, where the two garages sit | PLACEHOLDER (no survey) |
| Orientation (D15) | North arrow marked ASSUMED (PA-07). Sun path: sunrise E, midday S, sunset W. Wind arrow marked "TO BE CONFIRMED" | Indicators only |

**Not drawn, because they need approval:**
- D16: rotated dwelling;
- D17: outdoor cooking;
- D18: fire pit.

The issued Draft 0.2.2 is **unchanged**. Its byte-identical copy in `source-copies/` was read, not written; its sha256 is still `2ec8d3f3…1d17b`.
