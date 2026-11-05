# Proposed calculator fixes: FOR REVIEW, NOT ADOPTED

**Status:** proposal only (revision 6, 24 Oct 2026).

- The adopted calculator, `evidence/scripts/gate_calc.mjs`, is **unchanged** (SHA-256 `f4f0ddcb…`, checked before and after every test run).
- Nothing in this folder may be used for decisions until a reviewer accepts the fixes and the regression tests, and authorises adoption.
- The calculator closes no open question. OQ-05, OQ-06 and OQ-07 remain OPEN.
- All test values are TEST DATA, not product data.

## Contents

| File | What it is |
|---|---|
| `gate_calc_PROPOSED.mjs` | Proposed calculator: same arithmetic as the adopted one, plus a field registry, fail-closed validation and the new optional fields |
| `POCKET_DOOR_CALCULATOR_INPUTS_TEMPLATE_PROPOSED.json` | Proposed input template: every accepted field, with the G9 renaming note |
| `tests/run_tests.mjs` | Test suite (64 tests): regression, malformed, contradictory and physically impossible inputs, new fields, field roles, schema |
| `test_output/test_results.md` / `.json` | Results: **64 of 64 passed** |
| `test_output/field_roles_TESTED.json` | Tested role of every field: CALC, ECHO or NONE |
| `test_output/adopted_outputs/` | Outputs of the **adopted** calculator, used as the regression reference and for the defect contrast |

**To run** (from the scratch folder):

```bash
node CALCULATOR_PROPOSAL_NOT_ADOPTED/tests/run_tests.mjs CALCULATOR_PROPOSAL_NOT_ADOPTED/test_output
```

## 1. Demonstrated defects and the proposed fixes

| Defect (gap ID) | Adopted calculator today (MEASURED by running it) | Proposed behaviour | Tests |
|---|---|---|---|
| **G3** contradictory clear-opening results | Kit PW 900 with 25 / 25 linings in `door.*` gives legacy clear 800 ("meets 850: false") and kit "stated meets 850: true" **in the same result** | With any kit dimension, legacy `door.*` values are an INPUT_ERROR and the legacy drawn-gap outputs are not computed. The latch lining has its own field, `kit.latchLiningIntoPassage_mm` | D1, C2, C3, N8 |
| **G6** malformed numbers silently accepted | `"1894mm"` → NaN → `fitsCurrentWallRun = false`; `"1894"` and `""` are coerced | Each field has a type and minimum. Anything else is an INPUT_ERROR and nothing is calculated. Unknown keys are errors (warnings in `doorSystem`) | D2, M1–M19 |
| Invalid tolerance range accepted | min 5 / max 3 accepted | INPUT_ERROR | D3, D3b, C1 |
| Negative pocket length accepted | passage 900 > frame 800 → `pocketZoneNeeded_mm = -95` | Passage must be smaller than the frame / stud opening: INPUT_ERROR | D3b, P1, P2 |
| Wall options as text | `"100"` accepted, so `compatible: true` | Must be a non-empty list of numbers | D3, M6–M8 |
| Impossible geometry shown as numbers | `Math.abs` hides a latch jamb moved past the utility return wall | Status `GEOMETRY_IMPOSSIBLE` (not OK); command-line exit code 2 | P5–P8 |
| No thicker wall option | Text reads "would need Infinity mm" | "no thicker option published…" | N7 |
| **G1** no field for a stated stud / structural opening | Run = frame width + tolerance only, so an opening entered with a tolerance is double-counted | `kit.studOpeningWidth_mm` / `kit.studOpeningHeight_mm`. If given, the width is the run and any tolerance is ignored, with a warning | N1, C6, C10 |
| **G4** no field for a stated installed clear width | Must be hand-converted to a reduction | `kit.manufacturerInstalledClearWidth_mm` + `kit.configuration`. If a reduction is also given, the two must agree (INPUT_ERROR otherwise) | N3, N4, C4, C5 |
| **G2** no field for external-wall clearance | Frame ASSUMED to start at the wall face | `kit.pocketEndOffset_mm` (default 0), added to the latch move and the pocket zone | N2, P7 |
| **G5** no head-height check | Project head height hard-coded UNKNOWN | `kit.minHeadHeightAboveFFL_mm`, `project.availableHeadHeight_mm`. Frame height alone is reported only as a **lower bound** | N6, C11 |
| **G7** evidence fields not in the output | Kitchen supplier, confirmation reference and reduction basis are never read | Echoed in the result | N10 |
| **G10** evidence answers have no home | none | `doorSystem.leafSize`, `leafThickness_mm`, `handing` (echo only) | F1 |

**Other input checks (fail-closed):**

- A stated installed width cannot exceed the stated passage.
- A reduction must be smaller than the passage.
- Passage height must be below the frame height and the stud-opening height.
- A stud-opening height cannot be below the frame height.
- A minimum head height cannot be below the frame height.
- The carcass datum needs the panel thickness and the overhang.
- Legacy deductions cannot consume the whole opening.
- A legacy stated clear width cannot exceed the opening.

## 2. Regression against the adopted calculator

Every existing input file was run through **both** calculators, and every output value of the adopted one was compared.

| Input file | Scenarios | Adopted values compared | Identical | Intentionally not computed (G3) |
|---|---|---|---|---|
| `POCKET_DOOR_CALCULATOR_INPUTS_TEMPLATE.json` | 1 | 93 | 93 | 0 |
| `gate_inputs/OQ05_OQ06_inputs_TEMPLATE.json` | 1 | 48 | 48 | 0 |
| `gate_inputs/PLACEHOLDER_scenarios_NOT_PRODUCT_DATA.json` | 3 | 201 | 201 | 0 |
| `gate_inputs/pocket_door_candidates_RESEARCH_inputs.json` | 6 | 742 | 610 | 132 |

**The only differences are the 132 legacy values in kit mode, which are deliberately not computed (22 per candidate).** For the six research candidates, the adopted calculator reports "NOT CALCULABLE" clear openings on the drawn 850 mm gap beside the kit results. Every kit value is identical.

New output values are added: `status`, `mode`, `warnings`, `kitchenEvidence`, `geometryStatus`, `runBasis`, `pocketEndOffset_mm`, `nibToInsideEdgeOfFrame_mm` and the head-height fields.

## 3. Field roles (tested, not just declared)

Each of the 59 fields was changed on its own in a valid scenario, and the outputs were compared:

- **CALC (31):** the change altered a calculated output.
- **ECHO (24):** the only outputs that changed were copies of the input value. These are validated but do not influence any calculation.
- **NONE (4):** nothing changed. These are template help (`howToRun`, `door.notes`, `kitchen.datumOptions`) and the deprecated `door.requiredFinishedWallThickness_mm`.

All 59 tested roles agree with the roles declared in the code (test F1). The per-field results are in `test_output/field_roles_TESTED.json`.

**Note:** `kit.passageHeight_mm` is ECHO: it is validated against the frame height, but no project requirement uses it.

## 4. Assumptions and limits that remain

- **ASSUMPTION:** the pocket end of the frame sits `kit.pocketEndOffset_mm` (default 0) from the external wall face. The manufacturers are asked to confirm this (RFI_01A Q8; RFI_01B and RFI_01C Q7).
- **ASSUMPTION:** dwellings A and B are exact mirrors. Test N9 confirms the calculator treats them so.
- **Head height:** the frame height alone is a lower bound, and no project section exists. `project.availableHeadHeight_mm` REQUIRES CONFIRMATION by the designer.
- **Status meanings:**
  - `OK` means the inputs were consistent and the arithmetic ran. It is not a compliance result.
  - A `CONFLICT` geometry status (utility-side nib below target) is reported, but it does not stop the run.
- **What validation cannot check:** whether a manufacturer figure is entered under the right definition. For example, whether Scrigno's 896 is already net of the 10 mm. Those choices stay with the designer, guided by the dispositions in `RFI_CALCULATOR_FIELD_DISPOSITIONS.csv`.

## 5. If adoption is authorised (not done)

1. Replace `evidence/scripts/gate_calc.mjs` with the proposal, and record the old and new hashes.
2. Replace the inputs template with the proposed template.
3. Update the 16 Appendix C "Our calculator field" cells in the RFIs that name adopted fields; see the `rfi_column_update_on_adoption` column of the dispositions CSV. These were deliberately left unchanged, so that the RFIs do not cite an unadopted schema.
4. Update `rerun_validation.sh` and the adopted mapping in `rfi_trace.mjs`.
5. Re-run the tests, the regression and the traceability generator, then regenerate the scratch manifest.
