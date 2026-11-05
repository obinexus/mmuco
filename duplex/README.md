# MMUCO ORION Duplex

Two mirrored single-storey dwellings (A and B), drawn as DXF at 1:50 on A1. ORION is becoming a triplex; these are the duplex drafts it develops from (see [`../triplex/`](../triplex/)).

> **Not an approved design, construction drawing or compliance document.** The 850 mm clear width and the 300 mm nib are project design targets, not established regulatory requirements.

## Status (25 Oct 2026)

| Item | Status |
|---|---|
| Latest issued draft | **Draft 0.2.2** |
| Proposed Draft 0.2.3 (VF-07 Option A: kitchen base runs shortened to give a 300 mm nib) | **Scratch only, NOT ISSUED** |
| Issue gate for 0.2.3 | **Not passed.** OQ-05 (kitchen finished-face nib), OQ-06 (pocket-door system) and OQ-07 (installed clear opening) are OPEN. Approval NOT GIVEN |
| Manufacturer enquiries RFI-01A (ECLISSE), RFI-01B (JB Kind), RFI-01C (Scrigno) | **DRAFT — NOT SENT** |
| Gate-calculator fixes (two proposals) | **PROPOSED — NOT ADOPTED** |
| Accessibility category | M4(1) by default; whether M4(2) applies is open (OQ-01) |

## Layout

```
duplex/
├── draft-0.1/                      first floor plan + its preservation record
├── draft-0.2/                      drawing, room schedule, report, change log, audit report, decision package
│   └── verification/               0.2 verification report, register, manifest, evidence/
├── decisions/option-c/             Option C approval package, decision sheet, pre-approval revision
├── draft-0.2.1/                    drawing, room schedule, correction report, change log, manifest, evidence/
├── draft-0.2.2/                    LATEST ISSUED: drawing, room schedule, door resolution report,
│   │                               hallway option comparison, change log, manifest, evidence/
│   ├── vf07-investigation/         VF-07 kitchen-side nib investigation (recommended Option A), own manifest
│   ├── vf07-scratch_NOT-ISSUED/    VF-07 option drawings
│   └── scratch_NOT-ISSUED/         working and test files used to produce 0.2.2
├── draft-0.2.3_SCRATCH-NOT-ISSUED/ proposed 0.2.3 — start with README_NOT_ISSUED.md
│   ├── rfi/                        manufacturer and supplier enquiries (DRAFT — NOT SENT) and RFI traceability
│   ├── pocket-door-research/       candidate comparison, source register, research log
│   ├── calculator-proposal_PROPOSED-NOT-ADOPTED/
│   │   └── status-contract_PROPOSED-NOT-ADOPTED/
│   ├── evidence/  gate-inputs/  source-copies/  comparison-source/  test-positive-controls/  working-files/
└── integrity/                      path crosswalk (see Integrity)
```

## Naming convention

- **Folders:** lowercase, hyphenated: `draft-<version>/`, `evidence/`, `vf07-investigation/`.
- **Draft documents** (at the top of a draft folder): `orion-duplex_draft-<version>_<document>.<ext>`, for example `orion-duplex_draft-0.2.2_room-schedule.csv`. The drawing itself is `…_drawing.dxf / .pdf / .png`.
- **Status markers** stay in capitals at the end of a file or folder name, so they cannot be missed: `NOT-ISSUED`, `SCRATCH`, `PROPOSED`, `PROPOSED-NOT-ADOPTED`, `DRAFT-NOT-SENT`, `TEMPLATE`. A marker is never added or removed by a rename.
- **Inside `evidence/` folders, scratch folders, `source-copies/` and code folders,** files keep the names they were generated with: scripts and reports refer to them by those names.
- **A triplex draft** uses `orion-triplex_draft-<version>_<document>.<ext>` under [`../triplex/`](../triplex/).

## Integrity

These records were moved and renamed on 25 Oct 2026 from `projects/orion-duplex/files/` and `projects/orion-duplex/integrity/`. **No file's bytes changed.**

- `integrity/orion-duplex_path-crosswalk_2026-10-25.tsv` lists every record as `sha256 <TAB> original path <TAB> new path`. Original paths are relative to the old `projects/orion-duplex/` folder; new paths are relative to this folder.
- The issue manifests are unchanged, so they still list the **original** file names. To find a file a manifest or report names, look its original path up in the crosswalk.
- `bash tools/verify-orion.sh` (from the repository root) checks the crosswalk against its recorded hash and every file at its new path. It then checks each original manifest against its recorded hash and every file it lists, translated through the crosswalk:

| Record (new location) | Files listed | SHA-256 of the record file |
|---|---|---|
| `integrity/orion-duplex_path-crosswalk_2026-10-25.tsv` | 484 | `b705a916…` |
| `draft-0.2.2/orion-duplex_draft-0.2.2_manifest.sha256` | 80 | `d9062c5a…` |
| `draft-0.2.1/orion-duplex_draft-0.2.1_manifest.sha256` | 63 | `3fb2898a…` |
| `draft-0.2/verification/orion-duplex_draft-0.2_verification-manifest.sha256` | 40 | `1d48e6e3…` |
| `draft-0.2.2/evidence/preservation/earlier_documents_not_in_any_manifest.sha256` | 5 | `35be2479…` |
| `draft-0.2.2/vf07-investigation/orion-duplex_draft-0.2.2_vf07-investigation-manifest.sha256` | 49 | `1508eb2b…` |
| `draft-0.1/orion-duplex_draft-0.1_preservation-record.sha256` | 3 | `9854ad03…` |
| `draft-0.2.2/orion-duplex_draft-0.2.2_scratch-publication-snapshot_2026-10-25.sha256` | 10 | `a3e7ecb1…` |
| `draft-0.2.3_SCRATCH-NOT-ISSUED/orion-duplex_draft-0.2.3_manifest_PROPOSED-SCRATCH.sha256` | 166 | `960de61c…` |
| `…/status-contract_PROPOSED-NOT-ADOPTED/evidence/03_isolated_files.sha256` | 91 | `f57602b4…` |

**Notes:**

- The Draft 0.1 preservation record (24 Oct 2026) and the 0.2.2 scratch publication snapshot are hash records, not issue manifests. The snapshot records the 10 Draft 0.2.2 scratch files as published; it cannot show whether they changed before 25 Oct 2026.
- **Coverage:** every file in this folder is in the crosswalk, apart from this README and the crosswalk itself. The manifests overlap: later manifests also list earlier drafts.
- **Re-running evidence scripts:** scripts inside the evidence folders use the original relative paths (and some use absolute `C:\Users\…` paths). They will not run unchanged from the new layout. Run a copy from a scratch folder that recreates the original names, using the crosswalk.

## Before publishing: points for the owner

- **Your Windows username:** 21 evidence and script files contain local paths that include it (`C:\Users\Nnamdi\…`). Most are covered by manifests, so they cannot be edited without breaking verification.
- **Manufacturer contact details:** the RFI drafts and research files contain the published business contact details of ECLISSE UK and JB Kind, as printed on their own datasheet or web page.
- **Unsent enquiries:** the RFI drafts are unsent letters to the manufacturers. Publishing them makes their content public before they are sent.
- **Licence:** none has been chosen yet.
