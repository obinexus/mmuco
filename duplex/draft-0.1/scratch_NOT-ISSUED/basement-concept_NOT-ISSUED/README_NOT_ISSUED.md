# Basement concept: README

**MMUCO ORION TRIPLEX COMPOUND — BASEMENT CONCEPT (D21 PROPOSAL) — NOT ISSUED** (25 Oct 2026)

This is a 2D concept basement plan under the Orion Duplex, made at the user's request ("create a basement.dxf"). It illustrates **proposal D21**, which is **not approved**: see section 14 of `../GATE_REPORT_2026-10-25_NOT_ISSUED.md`.

**It is not a design.** It is not for construction, planning or Building Regulations, and it makes no compliance or feasibility claim. The issued Draft 0.2.2 is unchanged; a real basement would need an option study and a new housing draft.

| File | What it is |
|---|---|
| `basement.dxf` | DXF R12 in mm, with 153 entities on 13 layers. The ground floor of Draft 0.2.2 is a grey overlay on the `REF-GF-` layers; the basement is on the `BS-` layers |
| `basement_preview_plan_NOT_ISSUED.png`, `basement_preview_sheet_NOT_ISSUED.png` | Previews rendered by CADCraft from `basement.dxf`: the plan, and the full sheet with its notes |
| `basement_checks_output.txt` | Output of the independent read-back check (14 PASS, including a positive control) |
| `scripts/make_basement_dxf.mjs` | The generator. It refuses any source that is not the issued Draft 0.2.2 copy (it checks the sha256) |
| `scripts/check_basement_dxf.mjs` | The checker. It re-parses the saved DXF and measures it |
| `MANIFEST_NOT_ISSUED.sha256` | Hashes of every file in this folder |

To regenerate, run from this folder:

```bash
node scripts/make_basement_dxf.mjs ../source-copies/MMUCO_ORION_Duplex_Draft_0.2.2.dxf basement.dxf
```

```bash
node scripts/check_basement_dxf.mjs basement.dxf
```

## What is drawn

| Item | Value | Class |
|---|---|---|
| Basement outline | The verified external outline, 18,600 × 12,300 | VERIFIED (plan geometry) |
| Retaining wall | 300 mm all round, aligned with the provisional 300 external wall (PA-01) | PLACEHOLDER. The build-up is NOT DESIGNED |
| Basements | One per dwelling (the D21 default), each 8,900 × 11,700 = **104.13 m²** inside the walls. That is the same faces, and the same figure, as each dwelling's ground-floor GIA. **Use: habitable rooms** (the user's decision, 25 Oct 2026; D21 itself is not approved) | Measured from the drawing |
| Separating wall | 200 mm, under the party wall (x 9,200–9,400) | PROVISIONAL. Fire and acoustic separation to review |
| Stair | 1.0 × 4.0 zone in each 1.5 × 6.6 m hall | **INDICATIVE ONLY.** Its length depends on the basement depth, which is UNKNOWN. A stair here would block the hall doors, so the ground floor must be redesigned |
| Sump pits | Ø 0.6, one in each basement's rear outer corner | PLACEHOLDER |
| Perimeter drain | Runs 500 mm outside the walls, to both sumps | INDICATIVE route. Falls and outfall NOT DESIGNED; it never discharges into the rainwater well |
| Lightwell and escape window | 2.0 × 1.0 on the rear wall of each dwelling, clear of the conservatories | **REQUIRED**, because the use is habitable. One per dwelling is a placeholder: the number, size, depth, guarding and climb-out route depend on the room layout, which is NOT DESIGNED |
| North arrow | ASSUMED (PA-07) | Indicator only |

**Not drawn or not designed:**
- depth, floor level and ceiling height;
- slab, waterproofing and foundations;
- radon protection;
- ventilation, fire and escape detail;
- the ground-floor changes the stairs would need.

A **ground investigation** (soil, groundwater, radon) and a **structural engineer** are needed before any of these can be fixed.

**Because the use is habitable**, the design must also meet daylight, ventilation, escape, fire and damp requirements. See the D21 update in section 14 of the gate report for what each one adds and where it sits (Approved Documents B, C, E, F, K, L and M; BS 8102; BS EN 17037). No compliance is claimed.
