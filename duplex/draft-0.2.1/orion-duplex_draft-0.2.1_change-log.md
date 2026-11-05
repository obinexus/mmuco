# MMUCO ORION Duplex — Change Log, Draft 0.2 → Draft 0.2.1

**Issue:** `MMUCO_ORION_Duplex_Draft_0.2.1`, 24 October 2026
**Type:** controlled drafting correction of VF-01, VF-02 and VF-03. No design change.
**Basis:** approved C2 baseline; frozen Draft 0.2 files (unchanged; see §6).

> Not a planning, Building Regulations, accessibility or construction-readiness approval.

## 1. Summary of changes

| # | Change | Finding | Files affected |
|---|---|---|---|
| CL-1 | PDF plotted at true 1:50 on ISO A1 portrait, with page fitting disabled (`fit: false`). Measured scale 1:50.000 | VF-01 | `.pdf`, `.png` |
| CL-2 | PNG regenerated from the corrected PDF (7,500 × 10,619 px; deterministic render) | VF-01 | `.png` |
| CL-3 | Sheet scale note (handle 2FB) changed, **after** the scale measurement passed | VF-01 | `.dxf`, `.pdf`, `.png` |
| CL-4 | East dimension chain replaced: 7 dimensions erased, 9 added, matching the actual east-side partitions | VF-02 | `.dxf`, `.pdf`, `.png` |
| CL-5 | South and west chain dimensions re-created on wall-polyline vertices; patio, path and static anchors removed | VF-03 | `.dxf`, `.pdf`, `.png` |
| CL-6 | Title (handle 2DA) changed to "MMUCO ORION DUPLEX - DRAFT 0.2.1" | Issue identification | `.dxf`, `.pdf`, `.png` |
| CL-7 | Revision line added (new text 147E, y 15,960): "Draft 0.2.1 (24 Oct 2026): drafting corrections VF-01 to VF-03 only (plot scale, east dimension chain, dimension anchors). Design unchanged from Draft 0.2." | Issue identification | `.dxf`, `.pdf`, `.png` |
| CL-8 | Room schedule issued under the 0.2.1 name; **content identical** to Draft 0.2 (same SHA-256) | No change needed | `_Room_Schedule.csv` |

**Not changed:** every wall, opening, door, window, fitting, furniture, roof, accessibility-zone, provisional and external-works entity; all room labels; the notes, room-schedule and dimension-key text blocks; the 10 dimensions listed in §3.4. The entity diff shows 485 of 508 Draft 0.2 entities identical, and 0 non-annotation entities changed.

## 2. VF-01: plot configuration and scale note

| Item | Draft 0.2 | Draft 0.2.1 |
|---|---|---|
| Export settings | `exportpdf`, A1 portrait, `scale: "1:50"`, **fit not set** (CADCraft fitted to page) | `exportpdf`, A1 portrait, `scale: "1:50"`, **`fit: false`**, centred, extents |
| Measured scale (PDF vectors) | 1:48.229 (width, depth, scale bar) | **1:50.000** (width 372.000 mm, depth 246.000 mm, scale bar 100.000 mm on the sheet) |
| Measured scale (PNG pixels) | 1:48.14–1:48.16 | 1:49.90–1:49.94 (within 0.2 %; anti-aliasing bias) |
| Scale note (2FB) | "PDF sheet: ISO A1 portrait at 1:50. Dimensions in mm. For any other print size use the scale bar; do not scale from prints." (incorrect) | 1. Interim (exported 19:15:56): "PDF sheet scale: VERIFICATION PENDING - use the scale bar. Dimensions in mm; do not scale from prints." 2. Final, set only after the interim export measured PASS: "PDF sheet: ISO A1 portrait at 1:50 - scale verified by measurement (see Draft 0.2.1 Correction Report). Dimensions in mm. For other print sizes use the scale bar; do not scale from prints." |

The interim DXF and PDF are kept as evidence in `MMUCO_ORION_Duplex_Draft_0.2.1_Evidence/test_files/`.

## 3. VF-02 and VF-03: dimension changes (old and new endpoints and values)

Coordinates are in mm (x, y), with y = 0 at the front outer face and x = 0 at the west outer face.

- **Association** names the entity each definition point is attached to: "wall" plus its handle, "static", **PROVISIONAL** (A-PROV patio) or **EXT-WORKS** (A-EXT path/slab line).
- All tables were generated from the two DXF files by `ver_dims.mjs`, not retyped.

### 3.1 South chain (dwelling A front, dimension line y = −4,000)

Values unchanged. The interior points move from the outer face (y = 0, no vertex, static) to the partition corners on the inner face (y = 300).

| | Handle | From (x,y) | To (x,y) | Value | Association p13 / p14 |
|---|---|---|---|---|---|
| Old (erased) | 2C2 | 300,0 | 4300,0 | 4000 | wall 10A / static |
| Old (erased) | 2C3 | 4300,0 | 4400,0 | 100 | static / static |
| Old (erased) | 2C4 | 4400,0 | 5900,0 | 1500 | static / static |
| Old (erased) | 2C5 | 5900,0 | 6000,0 | 100 | static / static |
| Old (erased) | 2C6 | 6000,0 | 9200,0 | 3200 | static / wall 11B |
| **New** | 1467 | 300,0 | 4300,300 | 4000 | wall 10A / wall 127 |
| **New** | 1468 | 4300,300 | 4400,300 | 100 | wall 127 / wall 127 |
| **New** | 1469 | 4400,300 | 5900,300 | 1500 | wall 127 / wall 131 |
| **New** | 146A | 5900,300 | 6000,300 | 100 | wall 131 / wall 131 |
| **New** | 146B | 6000,300 | 9200,0 | 3200 | wall 131 / wall 11B |

### 3.2 West chain (dwelling A, dimension line x = −2,700)

Values unchanged. Associations moved off the provisional patio 224 and the path/slab line 234, onto wall vertices.

| | Handle | From (x,y) | To (x,y) | Value | Association p13 / p14 |
|---|---|---|---|---|---|
| Old (erased) | 2C9 | 0,0 | 0,300 | 300 | wall 100 / static |
| Old (erased) | 2CA | 0,300 | 0,4000 | 3700 | static / static |
| Old (erased) | 2CB | 0,4000 | 0,4100 | 100 | static / static |
| Old (erased) | 2CC | 0,4100 | 0,6600 | 2500 | static / static |
| Old (erased) | 2CD | 0,6600 | 0,6700 | 100 | static / static |
| Old (erased) | 2CE | 0,6700 | 0,8700 | 2000 | static / static |
| Old (erased) | 2CF | 0,8700 | 0,8800 | 100 | static / **EXT-WORKS 234** |
| Old (erased) | 2D0 | 0,8800 | 0,12000 | 3200 | **EXT-WORKS 234** / **PROVISIONAL 224** |
| Old (erased) | 2D1 | 0,12000 | 0,12300 | 300 | **PROVISIONAL 224** / wall 108 |
| **New** | 146C | 0,0 | 300,300 | 300 | wall 100 / wall 10A |
| **New** | 146D | 300,300 | 300,4000 | 3700 | wall 10A / wall 11D |
| **New** | 146E | 300,4000 | 300,4100 | 100 | wall 11D / wall 11D |
| **New** | 146F | 300,4100 | 300,6600 | 2500 | wall 11D / wall 11F |
| **New** | 1470 | 300,6600 | 300,6700 | 100 | wall 11F / wall 11F |
| **New** | 1471 | 300,6700 | 300,8700 | 2000 | wall 11F / wall 123 |
| **New** | 1472 | 300,8700 | 300,8800 | 100 | wall 123 / wall 123 |
| **New** | 1473 | 300,8800 | 300,12000 | 3200 | wall 123 / wall 112 |
| **New** | 1474 | 300,12000 | 0,12300 | 300 | wall 112 / wall 108 |

### 3.3 East chain (dwelling B, dimension line x = 21,000): VF-02

The old break points (4,300 / 4,400 / 6,900 / 7,000) were partitions beside the party wall. The new ones (4,000 / 4,100, 6,600 / 6,700, 8,700 / 8,800) are the partitions that meet the east wall (11E, 120, 124). The patio association is removed.

| | Handle | From (x,y) | To (x,y) | Value | Association p13 / p14 |
|---|---|---|---|---|---|
| Old (erased) | 2D2 | 18600,0 | 18600,300 | 300 | wall 101 / static |
| Old (erased) | 2D3 | 18600,300 | 18600,4300 | **4000** | static / static |
| Old (erased) | 2D4 | 18600,4300 | 18600,4400 | 100 | static / static |
| Old (erased) | 2D5 | 18600,4400 | 18600,6900 | 2500 | static / static |
| Old (erased) | 2D6 | 18600,6900 | 18600,7000 | 100 | static / **PROVISIONAL 225** |
| Old (erased) | 2D7 | 18600,7000 | 18600,12000 | **5000** | **PROVISIONAL 225** / **PROVISIONAL 225** |
| Old (erased) | 2D8 | 18600,12000 | 18600,12300 | 300 | **PROVISIONAL 225** / wall 109 |
| **New** | 1475 | 18600,0 | 18300,300 | 300 | wall 101 / wall 10B |
| **New** | 1476 | 18300,300 | 18300,4000 | **3700** | wall 10B / wall 11E |
| **New** | 1477 | 18300,4000 | 18300,4100 | 100 | wall 11E / wall 11E |
| **New** | 1478 | 18300,4100 | 18300,6600 | 2500 | wall 11E / wall 120 |
| **New** | 1479 | 18300,6600 | 18300,6700 | 100 | wall 120 / wall 120 |
| **New** | 147A | 18300,6700 | 18300,8700 | **2000** | wall 120 / wall 124 |
| **New** | 147B | 18300,8700 | 18300,8800 | 100 | wall 124 / wall 124 |
| **New** | 147C | 18300,8800 | 18300,12000 | **3200** | wall 124 / wall 113 |
| **New** | 147D | 18300,12000 | 18600,12300 | 300 | wall 113 / wall 109 |

**Old values:** 300 + 4,000 + 100 + 2,500 + 100 + 5,000 + 300 = 12,300. The total was right but the features were wrong.

**New values:** 300 + 3,700 + 100 + 2,500 + 100 + 2,000 + 100 + 3,200 + 300 = 12,300. Each segment equals the y-difference of its anchor vertices, and the total equals overall dimension 2D9.

### 3.4 Kept unchanged (geometry and association)

| Handle | Side | From | To | Value | Association p13 / p14 |
|---|---|---|---|---|---|
| 2BB | North | 0,12300 | 18600,12300 | 18600 | wall 108 / wall 109 |
| 2BC | North | 0,12300 | 300,12300 | 300 | wall 108 / wall 108 |
| 2BD | North | 300,12300 | 9200,12300 | 8900 | wall 108 / wall 118 |
| 2BE | North | 9200,12300 | 9400,12300 | 200 | wall 118 / wall 119 |
| 2BF | North | 9400,12300 | 18300,12300 | 8900 | wall 119 / wall 109 |
| 2C0 | North | 18300,12300 | 18600,12300 | 300 | wall 109 / wall 109 |
| 2C1 | South | 0,0 | 300,0 | 300 | wall 100 / wall 10A |
| 2C7 | South | 9200,0 | 9300,0 | 100 | wall 11B / **static** (party-wall centreline: no vertex exists) |
| 2C8 | West | 0,0 | 0,12300 | 12300 | wall 100 / wall 108 |
| 2D9 | East | 18600,0 | 18600,12300 | 12300 | wall 101 / wall 109 |

### 3.5 Dimension totals

| | Draft 0.2 | Draft 0.2.1 |
|---|---|---|
| Dimensions | 31 | 33 (east chain 7 → 9) |
| Definition points associated to wall vertices | 25 of 62 | **65 of 66** |
| Static points | 29 | **1** (2C7 p14) |
| Points associated to provisional or external-works geometry | 8 | **0** |
| Dimensions associated at both ends | 9 | **32** |

### 3.6 Text positions of the 100 mm segments

Set as in Draft 0.2 (`dimtedit`, no overrides):

- **South:** 1468 at (4,350, −4,150) and 146A at (5,950, −4,150).
- **West:** 146E, 1470, 1472 at (−2,830, 4,050), (−2,830, 6,650) and (−2,830, 8,750).
- **East:** 1477, 1479, 147B at (20,870, 4,050), (20,870, 6,650) and (20,870, 8,750).

### 3.7 Temporary displacement used during creation

Furniture entities 1E8, 1DC, 1E9 and 1DD each shared a vertex with an intended wall anchor. CADCraft would otherwise have attached the dimension to the furniture. They were moved (0, +100,000) and then (0, −100,000) mm. The entity diff confirms they are identical to Draft 0.2.

## 4. Files created (new files only)

| File | Note |
|---|---|
| `MMUCO_ORION_Duplex_Draft_0.2.1.dxf` | AutoCAD 2018 DXF, 511 entities, saved by CADCraft |
| `MMUCO_ORION_Duplex_Draft_0.2.1.pdf` | ISO A1 portrait, 1:50 |
| `MMUCO_ORION_Duplex_Draft_0.2.1.png` | 7,500 × 10,619 px, rendered from the PDF |
| `MMUCO_ORION_Duplex_Draft_0.2.1_Room_Schedule.csv` | Identical content to Draft 0.2 |
| `MMUCO_ORION_Duplex_Draft_0.2.1_Correction_Report.md` | Test results and release decision |
| `MMUCO_ORION_Duplex_Draft_0.2.1_Change_Log.md` | This file |
| `MMUCO_ORION_Duplex_Draft_0.2.1_Manifest.sha256` | Hashes of all new files plus the frozen files they depend on |
| `MMUCO_ORION_Duplex_Draft_0.2.1_Evidence/` | 14 scripts, 17 result files, 10 crop images, 5 test files (scratch states; **not** deliverables) |

## 5. Not changed in this issue (retained as open)

The following stay open, with geometry identical to Draft 0.2:

- **VF-04 to VF-07:** store sliding door; utility side-door obstruction; conservatory door nib; kitchen–utility push-side nib.
- **VF-08 to VF-16:** label crossings, low-contrast colours, smallest text, PDF vector text, partitions wording, door-leaf drafting, south chain covering dwelling A only, third-party CAD.
- **The full register** of provisional assumptions, missing site information, regulatory questions and design risks in `MMUCO_ORION_Duplex_Draft_0.2_Verification_Register.csv`.

The notes block header still reads "NOTES - DRAFT 0.2 (OPTION C2)". The block was kept byte-identical.

## 6. Preservation record

| Check | Start (19:07:50) | End (19:21:47) |
|---|---|---|
| `MMUCO_ORION_Duplex_Draft_0.2_Verification_Manifest.sha256`: six issued Draft 0.2 files, Draft 0.1 and the Verification package | 40 / 40 OK | 40 / 40 OK |
| Draft 0.1 original hashes (recorded before any Draft 0.2 work) | 3 / 3 OK | 3 / 3 OK |
| Verification manifest files themselves (`.csv` `d1a7f2fd…`, `.sha256` `1d48e6e3…`) | Recorded | Unchanged |
| Issued `MMUCO_ORION_Duplex_Draft_0.2_Report.md` (`672bc39c…`) | Recorded | Unchanged |

No existing file was overwritten, moved or deleted.
