# SCRATCH: NOT ISSUED

Nothing in this folder is a deliverable. These are working and test files used to produce and verify Draft 0.2.2. The issued Draft 0.2.2 files are in the parent folder and are listed in `MMUCO_ORION_Duplex_Draft_0.2.2_Manifest.sha256`.

| File | What it is |
|---|---|
| `WORKING_COPY_from_Draft_0.2.1.dxf` | Byte-identical copy of the issued `MMUCO_ORION_Duplex_Draft_0.2.1.dxf`. Opened in CADCraft so the issued file never was. It was never saved over (hash checked at the end) |
| `OPTION_STUDY_B1_B2_B3.dxf`, `option_study_panels.scr`, `OPTION_STUDY_B1_B2_B3_preview.pdf` | Source drawing, generating script and a preview of the B1 / B2 / B3 comparison sheet. The issued comparison sheet is `../MMUCO_ORION_Duplex_Draft_0.2.2_Hallway_Option_Comparison.pdf/.png` |
| `grip_test.dxf` | Failed first edit attempt: CADCraft grip indices are not vertex indices, so wall 127 came out distorted. Discarded; the edit was redone with `pedit` vertex moves. Kept only as a record |
| `WIP_0.2.2_pending_scale.dxf`, `WIP_0.2.2_pending_scale.pdf` | Draft 0.2.2 before the scale note was changed. The scale was measured on this PDF first |
| `TEST_moved_all_nonwall.dxf` | Dependency test: all 272 provisional and non-wall entities moved (+2,000, +3,000) mm. Dimensions must not change |
| `TEST_moved_room_boundaries.dxf` | Positive control: partitions 11D and 137 moved +100 mm. The anchored dimensions must update |
