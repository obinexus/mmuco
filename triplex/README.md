# MMUCO ORION Triplex

The **MMUCO ORION Triplex Compound** has three spatial nodes:

1. the Orion Duplex housing, unchanged;
2. a shared public garden;
3. a shared patio and walkway.

**It is not three dwellings, and not three storeys.** The duplex stays two mirrored single-storey dwellings. **No triplex draft has been issued yet.**

> **Not an approved design, construction drawing or compliance document.**

## Current work

- [`draft-0.1/scratch_NOT-ISSUED/`](draft-0.1/scratch_NOT-ISSUED/): the 3D-model proposal, gate report and provisional parameters, plus two concept DXFs:
  - the backyard concept;
  - the basement concept (proposal D21, **not approved**): a habitable basement under each dwelling. It would change the duplex housing, so it needs its own option study and a new housing draft.
  - **Status:** scratch only, NOT ISSUED.
  - **Cleaned for publication:** see its `CLEANING_RECORD_NOT-ISSUED.md`.

## Starting the first triplex draft

The triplex is a new draft developed from the duplex records in [`../duplex/`](../duplex/). It does not replace or edit them.

1. Create `draft-<version>/` here, with a scratch folder (`scratch_NOT-ISSUED/`) for work in progress.
2. Name draft documents `orion-triplex_draft-<version>_<document>.<ext>`, for example `orion-triplex_draft-<version>_drawing.dxf`. Follow the rest of the naming convention in [`../duplex/README.md`](../duplex/README.md#naming-convention).
3. State which duplex draft it develops from (for example Draft 0.2.2, or 0.2.3 if that is issued first). Also state whether the duplex open questions (OQ-01, OQ-05 to OQ-07) carry over.
4. On issue, freeze the folder with its own `orion-triplex_draft-<version>_manifest.sha256`, and add that manifest and its SHA-256 to `tools/verify-orion.sh`.
