# MMUCO ORION Duplex — Draft 0.2 Verification Gate: Change Log

**Date:** 24 October 2026
**Scope:** independent verification of the six issued Draft 0.2 (C2) deliverables, treated as a frozen baseline.

## 1. Issued files: no changes

None of these files was opened for writing, re-saved, re-exported or overwritten. SHA-256, size and modification time were identical at the start (18:41:37 +01:00) and the end of the gate; see the Manifest.

| File | Status |
|---|---|
| `MMUCO_ORION_Duplex_Draft_0.2.dxf` | Unchanged |
| `MMUCO_ORION_Duplex_Draft_0.2.pdf` | Unchanged |
| `MMUCO_ORION_Duplex_Draft_0.2.png` | Unchanged |
| `MMUCO_ORION_Duplex_Draft_0.2_Room_Schedule.csv` | Unchanged |
| `MMUCO_ORION_Duplex_Draft_0.2_Report.md` | Unchanged |
| `MMUCO_ORION_Duplex_Draft_0.2_Change_Log.md` | Unchanged |
| `MMUCO_ORION_Duplex_Floor_Plan.dxf / .pdf / .png` (Draft 0.1) | Unchanged |
| Earlier audit, decision and approval documents | Unchanged |

The DXF was read by text parsers, and reopened read-only in CADCraft before the gate. The CADCraft session was used only to export two **scratch** PDFs to the scratchpad, testing whether a true 1:50 plot is possible (VF-01). Those test files are not deliverables and are not in the project folder.

## 2. New files (verification stage)

| # | File | Purpose |
|---|---|---|
| 1 | `MMUCO_ORION_Duplex_Draft_0.2_Verification_Report.md` | Gate result; DXF review; area reconciliation summary; accessibility review; visual review; evidence classes |
| 2 | `MMUCO_ORION_Duplex_Draft_0.2_Verification_Manifest.csv` | SHA-256, size, modification time and verification timestamps for the issued deliverables, Draft 0.1 and this package |
| 3 | `MMUCO_ORION_Duplex_Draft_0.2_Verification_Manifest.sha256` | The same hashes in `sha256sum -c` format |
| 4 | `MMUCO_ORION_Duplex_Draft_0.2_Verification_Area_Reconciliation.csv` | 41 rows. Generated from measured results by `ver_areas_csv.mjs`, not retyped |
| 5 | `MMUCO_ORION_Duplex_Draft_0.2_Verification_Register.csv` | 68 rows: findings (VF), provisional assumptions (PA), missing site information (SI), regulatory questions (RQ), design risks (DR) |
| 6 | `MMUCO_ORION_Duplex_Draft_0.2_Verification_Visual_Evidence.png` | 9 native-resolution crops of the issued PNG with captions |
| 7 | `MMUCO_ORION_Duplex_Draft_0.2_Verification_Evidence/scripts/` | `blind_measure.mjs` (blind agent), `ver_access.mjs`, `ver_text.mjs`, `ver_png.mjs`, `ver_pdfscale.mjs`, `ver_areas_csv.mjs`, `ver_dump.mjs`, `ver_crops.ps1`, `renderpdf_w.ps1` |
| 8 | `MMUCO_ORION_Duplex_Draft_0.2_Verification_Evidence/results/` | Raw outputs: `blind_results.json`, `ver_access.json`, `ver_text.json`, `ver_png.json`, `ver_pdfscale.json.txt`, `ver_rooms_from_blind.json`, `freeze_t0.txt`, `ver_png_reproducibility.txt` |
| 9 | `MMUCO_ORION_Duplex_Draft_0.2_Verification_Evidence/crops/` | `crop_01.png` to `crop_09.png` |
| 10 | `MMUCO_ORION_Duplex_Draft_0.2_Verification_Change_Log.md` | This file |

## 3. Findings raised (no files changed in response)

| ID | Finding | Priority | Proposed action (needs your approval; would be a new revision with new filenames) |
|---|---|---|---|
| VF-01 | PDF and PNG are about 1:48.23, not the stated 1:50 | High | Re-plot with `fit: false` (tested: exactly 1:50); correct the sheet note, report and change log |
| VF-02 | East dimension chain dimensions the wrong partitions | High | Replace it with the mirror of the west chain |
| VF-03 | 11 dimensions have no association; 6 are tied to provisional patio and path geometry | Medium | Re-associate to walls or disassociate; correct the "31 associative" statement |
| VF-04 | Store bypass sliding door about 450 mm clear | Medium | Design decision after the 2.22 Note 1 interpretation |
| VF-05 | MVHR/cylinder allowance overlaps the utility side-door opening by 100 mm | Medium | Move the opening or the allowance |
| VF-06 | Conservatory door pull-side nib 200 mm if the provisional conservatory is built as drawn | Medium | Re-hand the door, or resolve with the conservatory size |
| VF-07 | Kitchen–utility door push-side nib 100 mm | Low | Interpretation; shorten the base run if needed |
| VF-08 to VF-11 | Label crossings; low-contrast colours; patio B edge masked; 1.6 mm smallest text | Low | Drafting tidy-up and a monochrome plot style |
| VF-12 to VF-16 | Vector-only PDF text; "partitions" wording; door-leaf drafting; south chain covers dwelling A only; third-party CAD not tested | Info / Low | Note, clarify, or test in third-party CAD |

## 4. Method notes

- **Two implementations.** A separate agent wrote a blind parser with no access to the generator, the model or the issued documents. Its results agree with this gate's own DXF-only checks and with every figure in the issued documents, except the defects listed above.
- **Model-dependent checks.** The issue-stage checks that compared the DXF with the C2 coordinate model are identified as such and are **not** relied on for any result in this gate.
