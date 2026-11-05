# hive.dxf validation report

**MMUCO ORION HIVE SYSTEM — CONCEPT PROPOSAL — NOT ISSUED** (25 Oct 2026)

> **Public copy.** This report records the validation run in the private workspace, where the source was the private backyard copy (sha256 `5a9533e2…`). In this repository the source is the public cleaned backyard (sha256 `afc9bc11…`), whose geometry is identical; only a latitude label was removed. Here `hive.dxf` regenerates **byte-identically** from it, and the validator passes 26/26 (see `../CLEANING_RECORD_NOT-ISSUED.md`).

| Item | Result |
|---|---|
| File | `<project root>\MMUCO_ORION_Hive_System_CONCEPT_PROPOSAL_NOT_ISSUED\hive_dxf_NOT_ISSUED\hive.dxf` |
| SHA-256 | `5fcad9cf5ba4e99f177f7c35c8d17076b96ca79f1b27f384609e99a2eee2a2cc` (also in `MANIFEST_NOT_ISSUED.sha256`) |
| Format | DXF R12 (`$ACADVER` AC1009), ASCII, CRLF |
| Units | `$INSUNITS` = 4 (millimetres), model scale 1:1 |
| Entities | 203 (POLYLINE counted once): 18 layers defined, all used |

## 1. Before drawing

| Check | Result |
|---|---|
| Existing `hive.dxf` anywhere under the project root, including `mmuco/` | **None.** Nothing was overwritten. Two earlier drafts made during this same task were moved aside to the session scratchpad, not overwritten |
| Hive workspace location | `MMUCO_ORION_Hive_System_CONCEPT_PROPOSAL_NOT_ISSUED/` in the private project root. **It is not part of the `mmuco` GitHub repository**, and nothing was added to the repository |
| Protected files | Frozen records **240 OK**; Draft 0.2.3 scratch manifest **166 OK**; status-contract list **91 OK**. Triplex workspace 12/12 and 24/24; backyard 6/6; basement 7/7; Hive workspace 7/7 |
| Source copy | `source_refs/backyard_concept_from_triplex.dxf` sha256 `5a9533e2…`, byte-identical to the Triplex backyard concept. The generator refuses any other source |
| Reported measurements | All confirmed against the source, with no conflicts. Duplex 18,600 × 12,300; open shared garden 255.43 m² (grid; 255.77 exact); orangeries 80.02 (grid; 80.00 exact); open private garden 81.18; roof water 28.82 m³ per 100 mm. Schedule: 90 + 45 + 12 + 6 + 4 + 98 = 255. The measured residual is 98.43 (grid) or 98.77 (exact), so "98" is rounding |

## 2. Tools

| Tool | What it did |
|---|---|
| `scripts/check_hive_dxf.mjs` (Node.js; a custom DXF parser written for this check) | Independent read-back of the saved file: 26 checks, including a positive control |
| **CADCraft** (headless MCP session) | Opened `hive.dxf`: **203 entities, no warnings**. Rendered `hive_preview_plan_NOT_ISSUED.png` and `hive_preview_sheet_NOT_ISSUED.png`. The previews were inspected: labels sit in their zones, and nothing overlaps after two label-placement fixes |

No other CAD application was used. This report does not claim that any other program has opened the file.

## 3. Results (from `hive_validation_output.txt`: 26 PASS, 0 FAIL)

| Check | Result |
|---|---|
| Positive control: area, 300 mm gap, overlap and self-intersection detection | PASS |
| Readable; units mm; R12; all geometry flat (no Z) | PASS |
| All 16 requested layers defined and used | PASS |
| Housing reference = source walls and provisional works, unchanged; 18,600 × 12,300 | PASS (31 polylines) |
| Shared garden, orangeries, private gardens and walkway = source geometry | PASS |
| Orangeries kept at +45° and −45°, which is **90° to each other** (8,000 × 5,000); added 25 Oct 2026 at the user's request | PASS: −45.000° and +45.000°, **90.000° between them** |
| Area polylines closed, ≥ 3 vertices, non-zero area, not self-intersecting | PASS (34 checked) |
| No duplicate entities | PASS (104 geometric entities) |
| Crop beds 90 m² | **90.000 m²** (10 polylines) |
| Pollinator habitat 45 m² | **45.000 m²** (4) |
| Rice–fish trial 12 m² | **12.000 m²** (1) |
| Compost 6 m² | **6.000 m²** (1) |
| Water storage 4 m² | **4.000 m²** (1) |
| Every zone inside the Hive open-ground outline (none in the walkway, covered patio or outside the garden) | PASS (17 zones) |
| Clearance from orangeries and amenities | Minimum **299 mm**. The design value is 300; the circles for the well and fountain are checked as 180-sided polygons |
| No overlaps; gap between zones | Minimum **300 mm** |
| Open shared garden recomputed from the DXF | **255.77 m²** (agrees with the grid measure of 255.43 to within 1 m²) |
| Zones + unallocated = open ground | 157.00 + **98.77** = 255.77 m². The schedule is a subdivision of the open ground, not added on top of it |
| Title, verbatim H-D1 note, zone labels, pond and drinking-water notes, ASSUMED north | PASS |

## 4. Measured extents

- **Geometry (excluding text):** x −1,800 to 23,680 mm, y −1,200 to 37,611 mm. This runs from the side patio and the housing dimension line to the north arrow and the top garden dimension.
- **Including text:** the title and notes block, starting at x 23,500, extends to about x 72,000. `$EXTMAX` in the header is set to 72,000 × 38,000.

## 5. Protected files after writing

| Check | Result |
|---|---|
| Frozen records | **240 OK, 0 not OK** |
| Draft 0.2.3 scratch manifest | **166 OK** |
| Status-contract list | **91 OK** |
| Issued Draft 0.2.2 DXF | sha256 `2ec8d3f3…`, unchanged |
| Triplex workspace | 12/12, 24/24, backyard 6/6, basement 7/7: unchanged |
| Hive workspace, earlier files | 7/7: unchanged |
| Every other project file | Identical to the baseline. The only known differences are in `mmuco/` (your restructure, and the uncommitted triplex sync), which this task didn't touch |
| `mmuco` | `tools/verify-orion.sh` reports VERIFIED |

No frozen or issued file was modified, and no 3D geometry was created.
