# MMUCO ORION TRIPLEX COMPOUND — 3D MODEL PROPOSAL — NOT ISSUED

> **Public, cleaned copy (25 Oct 2026).** Personal and third-party material has been removed; `CLEANING_RECORD_NOT-ISSUED.md` lists every change. Folder names follow the repository convention (`source-copies/`, `backyard-concept_NOT-ISSUED/`, `evidence/gate-session_2026-10-25/`); the documents still use the original workspace paths (see the crosswalk). The empty `model/` and `views/` folders are not included, and `evidence/verify_protected.sh` only runs when this folder sits in the private project root.

**Status (25 Oct 2026): inventory and build plan done. No geometry has been built yet.**

- **Why no geometry yet:** SolidCraft's tools were not loaded in the session that prepared this folder, and the brief requires them to be available before any geometry is created.
- **Not an approved design, construction model or compliance document.**
- **"Triplex" means a compound of three spatial nodes:**
  1. housing: the existing Orion Duplex;
  2. public garden;
  3. public patio and walkway.

  It is not three dwellings or three storeys. The issued Orion Duplex drawings are unchanged and are not renamed.

## Contents

| Path | What it is |
|---|---|
| `INVENTORY_AND_BUILD_PLAN.md` | Sources and revisions, what exists and what is missing, measured areas and the 2:1 calculation, differences between the transcript and the written brief, staged build plan, decisions needed |
| `compound_parameters_PROVISIONAL.json` | Every dimension the model will use, each classed VERIFIED / STATED / ASSUMPTION / PLACEHOLDER |
| `source_refs/` | Byte-identical copies of the issued Draft 0.2.2 DXF and PNG (hashes match the issued manifest), the Otter transcript, and the client's elevation sketch (25 Oct; see section 8 of the plan). The CADCraft screenshot named in the plan is not included in this public copy. SolidCraft reads **only** these copies, never the originals |
| `evidence/` | Hash snapshot of the whole project taken before this folder was created (1,377 files; frozen files 240/240), plus `verify_protected.sh`, which checks the project against that snapshot |
| `model/`, `views/` | Empty until the build: the `.solidcraft` model, STEP export, and the orthographic and overview images |

## Starting the build

1. **Open a new Claude Code session in the project root.** SolidCraft is configured only for that folder; from `u\mmuco` it is not available.
2. **Confirm the SolidCraft tools are listed**, then follow the build plan, stage by stage.
3. **Allow SolidCraft to write here and nowhere else:** add `--allow-path` for this folder to its configuration before saving. Never open or save a design inside the issued drafts.
