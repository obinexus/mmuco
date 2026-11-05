# Cleaning record

**MMUCO ORION HIVE SYSTEM — PUBLIC CLEANED COPY — NOT ISSUED** (25 Oct 2026)

This folder is a cleaned copy of the private working folder `MMUCO_ORION_Hive_System_CONCEPT_PROPOSAL_NOT_ISSUED/`. `cleaned-copy-crosswalk_2026-10-25.tsv` gives, for every file, the original SHA-256 and path, the action taken, and the new SHA-256 and path.

## What changed

| File (path in this copy) | Change |
|---|---|
| `source-copies/backyard_concept_from_triplex.dxf` | **Replaced** with the public cleaned Triplex backyard drawing (sha256 `afc9bc11…`, the same file as `../../triplex/draft-0.1/scratch_NOT-ISSUED/backyard-concept_NOT-ISSUED/backyard.dxf`). The private copy carried a site-latitude label. The geometry is identical |
| `hive-dxf_NOT-ISSUED/scripts/make_hive_dxf.mjs` | The source hash it accepts is now the public cleaned backyard (`afc9bc11…`); one usage-comment path updated |
| `hive-dxf_NOT-ISSUED/scripts/check_hive_dxf.mjs` | One usage-comment path updated |
| `README_NOT_ISSUED.md` | Public-copy notice; source line updated; paths updated to the new folder names; link to the public Triplex copy |
| `hive-dxf_NOT-ISSUED/HIVE_DXF_README.md` | Public-copy notice; command paths updated |
| `hive-dxf_NOT-ISSUED/HIVE_DXF_VALIDATION_REPORT.md` | Public-copy note added. The private validation record is kept as history |
| `MANIFEST_NOT_ISSUED.sha256`, `hive-dxf_NOT-ISSUED/MANIFEST_NOT_ISSUED.sha256` | Regenerated so they verify against this copy |
| Folders | `source_refs/` became `source-copies/`, and `hive_dxf_NOT_ISSUED/` became `hive-dxf_NOT-ISSUED/` (repository convention). Files inside keep their names |

**Removed:** nothing. The Hive workspace held no personal data apart from the latitude label in the backyard copy.

## Proof that the copy is equivalent

These were run here in the repository, using only the public sources:

1. `evidence/hive_measure.mjs` on `source-copies/backyard_concept_from_triplex.dxf` reproduces `evidence/hive_measure_output.json` **identically**.
2. `hive-dxf_NOT-ISSUED/scripts/make_hive_dxf.mjs` regenerates `hive.dxf` **byte-identically** (sha256 `5fcad9cf…`).
3. `hive-dxf_NOT-ISSUED/scripts/check_hive_dxf.mjs` passes **26/26**, with output identical to `hive_validation_output.txt`. That includes the check that the orangeries are kept at +45° and −45°, which is 90° to each other.

## Kept deliberately

- **"UK" wording** (for example "temperate (UK-type) climate", "UK winds"). The issued duplex drawings already cite UK regulations, so this reveals nothing new. No town, latitude or site is given.
- **The user's brief and the proposed H-D1 policy**, in `source-copies/`. They hold no personal data.

**Not done:** nothing was committed or pushed.
