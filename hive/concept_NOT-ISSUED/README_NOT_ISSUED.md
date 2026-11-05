# MMUCO ORION Hive System workspace

**MMUCO ORION HIVE SYSTEM — CONCEPT PROPOSAL — NOT ISSUED** (25 Oct 2026)

> **Public copy (25 Oct 2026).** This is a cleaned copy of a private working folder. `CLEANING_RECORD_NOT-ISSUED.md` lists every change and `cleaned-copy-crosswalk_2026-10-25.tsv` maps each file. Folder names follow the repository convention (`source-copies/`, `hive-dxf_NOT-ISSUED/`); some documents still use the original paths (`source-copies/`, `hive-dxf_NOT-ISSUED/`).

This is a separate proposal workspace for the Hive System: the duplex's ecological food-production garden. It was set up as the brief requires.

- **What exists so far:** a written concept plan, and a 2D concept plan `hive-dxf_NOT-ISSUED/hive.dxf` (25 Oct 2026). No 3D geometry has been made.
- **What it is not:** an approved design, construction drawing or compliance document.
- **Protected files:** the issued and frozen ORION records were checked before and after this work, and are unchanged.

| Path | What it is |
|---|---|
| `HIVE_CONCEPT_PLAN_NOT_ISSUED.md` | The seven deliverables the brief requires: system diagram, land-use schedule, crop-and-season table, water assessment, risks, assumptions and decisions (H-D1 to H-D10), and the proposed layout. It also has a science note on bees and wasps |
| `source-copies/hive_system_brief_2026-10-25.md` | The user's brief, unchanged |
| `source-copies/hd1_governance_policy_PROPOSED_2026-10-25.md` | The user's proposed H-D1 policy (ownership, access and harvest governance), unchanged. Status: PROPOSED — FOR REVIEW, not approved |
| `source-copies/backyard_concept_from_triplex.dxf` | The **public cleaned** Triplex backyard concept (sha256 `afc9bc11…`). Its geometry is identical to the private original; only a latitude label was removed. Used for the area measurements |
| `hive-dxf_NOT-ISSUED/` | `hive.dxf` (2D concept plan of the Hive garden), its README, validation report, previews and scripts. See `hive-dxf_NOT-ISSUED/HIVE_DXF_README.md` |
| `evidence/hive_measure.mjs`, `evidence/hive_measure_output.json` | Areas (50 mm grid sampling, with a positive control) and rainwater yield per 100 mm of rain |
| `MANIFEST_NOT_ISSUED.sha256` | Hashes of every file in this folder |

**Re-run the measurement:**

```bash
node evidence/hive_measure.mjs source-copies/backyard_concept_from_triplex.dxf
```

**Related work:** the Triplex workspace `../../triplex/draft-0.1/scratch_NOT-ISSUED/` (the public copy of the Triplex workspace) holds the compound decisions (D1–D21) and the backyard and basement concepts.
