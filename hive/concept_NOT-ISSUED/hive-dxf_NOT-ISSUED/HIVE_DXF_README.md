# hive.dxf: README

**MMUCO ORION HIVE SYSTEM — CONCEPT PROPOSAL — NOT ISSUED** (25 Oct 2026)

> **Public copy (25 Oct 2026).** This is a cleaned copy of a private working folder. `../CLEANING_RECORD_NOT-ISSUED.md` lists every change and `../cleaned-copy-crosswalk_2026-10-25.tsv` maps each file. Folder names follow the repository convention (`source-copies/`, `hive-dxf_NOT-ISSUED/`); some documents still use the original paths (`source_refs/`, `hive_dxf_NOT_ISSUED/`).

`hive.dxf` is an editable 2D plan of the proposed Hive garden: the duplex's ecological food-production area inside the **residents-only shared garden** (Q-A).

- **It is a concept.** It is not a design for construction, planning or Building Regulations. It is not issued or approved, and it makes no compliance claim.
- **No 3D geometry** was made.
- **The issued Draft 0.2.2 is unchanged.**

## Files

| File | What it is |
|---|---|
| `hive.dxf` | DXF R12 (AC1009), **millimetres at 1:1** (`$INSUNITS` = 4), 203 entities on 18 layers. SHA-256 is in `MANIFEST_NOT_ISSUED.sha256` |
| `HIVE_DXF_VALIDATION_REPORT.md` | Validation results: parser, tools, extents, area checks, protected-file checks |
| `hive_validation_output.txt` | Raw output of the validator (26 PASS, 0 FAIL) |
| `hive_preview_plan_NOT_ISSUED.png`, `hive_preview_sheet_NOT_ISSUED.png` | Previews rendered by CADCraft from `hive.dxf` (supplementary only) |
| `scripts/make_hive_dxf.mjs` | The generator. It reads the backyard concept copy, checks it, and writes `hive.dxf` |
| `scripts/check_hive_dxf.mjs` | The independent validator. It re-parses the saved DXF and compares it with the source |

## Opening it

Open `hive.dxf` in any DXF-capable CAD application (CADCraft, LibreCAD, AutoCAD, QCAD, DraftSight and others). It uses only basic R12 entities: POLYLINE, LINE, CIRCLE and TEXT. It was opened and rendered in **CADCraft** (headless) with no warnings.

The drawing is at true size in mm. Use "zoom extents", and don't scale it to fit a page.

To regenerate and re-validate, run from this folder:

```bash
node scripts/make_hive_dxf.mjs ../source-copies/backyard_concept_from_triplex.dxf hive.dxf
```

```bash
node scripts/check_hive_dxf.mjs hive.dxf ../source-copies/backyard_concept_from_triplex.dxf
```

The generator writes to the path given. To keep the current file, write to a new name.

## Layers

| Layer | Contents |
|---|---|
| `HIVE_BOUNDARY` | Planning outline of the open shared ground available to the Hive (3 closed polylines, 255.77 m² after amenities are subtracted). **It is not a fence, title or ownership line** (Q-A, H-D1) |
| `HOUSING_REFERENCE` | Duplex external walls, party wall, conservatories and side patios, copied unchanged from the source. Reference only |
| `SHARED_GARDEN` | The residents-only shared garden (22,200 × 20,611), from the source |
| `SHARED_AMENITIES` | Shed, kennel, cat shelter, pond, fountain (optional, D6) and canopy, from the source. **The pond is a shared amenity, not a fish-production system** |
| `CROP_BEDS` | CB-1 to CB-9: **90.00 m²** (PROPOSED) |
| `POLLINATOR_HABITAT` | PH-1 to PH-4: **45.00 m²** (PROPOSED) |
| `RICE_FISH_TRIAL` | RF-1: **12.00 m²** (OPTIONAL, subject to feasibility, H-D4; fenced; separate from the pond and the well) |
| `COMPOST` | CP-1: **6.00 m²** (PROPOSED; plant waste only) |
| `WATER_STORAGE` | WS-1, the rain tank footprint: **4.00 m²** (PROVISIONAL; capacity, height, access and clearances UNKNOWN). Also the existing Triplex well (Ø 1.5, depth UNKNOWN) |
| `RAINWATER_COLLECTION` | Schematic roof downpipe to the tank, and the canopy-to-well and well-to-tank links |
| `IRRIGATION` | A schematic main and branches from the tank. Routes, falls and sizes are not designed |
| `ORANGERIES` | The two existing proposed orangeries (2 × 40 m² covered growing), from the source. They are **kept at +45° and −45°, which puts them at 90° to each other** (the user confirmed this on 25 Oct 2026, and the validator checks it) |
| `PATHS_ACCESS` | The shared walkway, from the source. Maintenance access is the 300–600 mm corridors between zones, inside the unallocated space |
| `PRIVATE_GARDEN` | Private rear gardens A and B, from the source. Not part of the Hive (Q-B open) |
| `DIMENSIONS` | Key dimensions: garden 22,200 × 20,611, housing 18,600 × 12,300, tank and compost widths |
| `TEXT_LABELS` | Zone labels (ID, area, status), title, H-D1 note, schedule, notes, legend, north arrow (ASSUMED) |
| `PROVISIONAL_ELEMENTS` | Red dashed markers around elements whose size and position are placeholders: RF-1, CP-1, WS-1 |

## Source measurements and what is measured or provisional

| Item | Value | Class |
|---|---|---|
| Duplex footprint | 18,600 × 12,300 mm | **Verified** as drawn (Draft 0.2.2; the build-up is provisional, PA-01/PA-02) |
| Shared garden | 22,200 × 20,610.811 mm = 457.56 m² | **Measured** from the backyard concept. That concept's size is the Triplex 2:1 target (D2), a placeholder |
| Open shared garden for the Hive | **255.77 m²** exact (the earlier grid measure was 255.43 m²) | **Calculated** from the drawing's polygons |
| Orangeries | 80.00 m² (2 × 40) | **Measured**; their size is a Triplex placeholder |
| Open private garden | 81.18 m² (2 × 40.59) | **Measured** |
| Roof-water estimate | 28.82 m³ per 100 mm of rain | **Calculated**, with placeholder runoff (0.8) and filter (0.9) coefficients (`../evidence/hive_measure_output.json`) |
| Zones (90 / 45 / 12 / 6 / 4 m²) | Exactly as scheduled | **Provisional** proposals, drawn to the schedule |
| Unallocated | 98.77 m² | **Calculated** residual. It includes the access corridors |

## Assumptions and unresolved issues

- **North is ASSUMED** (PA-07), as in the source. It is not true north. The site boundary, levels, survey and climate are UNKNOWN.
- **Zone placement** follows the sun on the assumed north:
  - crops sit mainly south of the orangeries and in the garden core;
  - pollinator habitat sits beside the walkway spine and in the far corners.
  - Crop beds CB-8 and CB-9 get afternoon shade from the orangeries, and CB-3 and CB-6 get partial winter shade from the house (heights are placeholders).
- **Clearances:** 300 mm to amenities and orangeries; 300–600 mm between zones for access.
- **Not drawn:** a managed beehive (H-D5), drinking-water infrastructure (separate; route unknown), ownership or title lines, and the D17 outdoor cooking and D18 fire pit candidates.
- **Crop viability is not assessed.** The rice and yam trials need climate, soil, water and season data. No yield is claimed.
- **Open decisions:**
  - H-D1: PROPOSED; five owner questions, plus Q-B;
  - H-D2 to H-D10;
  - the Triplex decisions the Hive depends on (D2, D3, D5–D7, D14, D20).
