# SCRATCH: NOT ISSUED (proposed Draft 0.2.3, VF-07 Option A)

**Everything in this folder is an unissued review copy.**

- Nothing here is an issued drawing, an approved Draft 0.2.3, a construction drawing or a compliance document.
- The issued design is still Draft 0.2.2 in the parent folder, listed in `MMUCO_ORION_Duplex_Draft_0.2.2_Manifest.sha256`. It was not modified, renamed or deleted.
- A formal issue needs explicit human approval.
- Formal issue is also blocked by two open items, recorded in the Validation Report:
  - **OQ-06:** no pocket-door system is selected, so the clear opening cannot be measured.
  - **OQ-05:** the finished-face nib is unconfirmed (kitchen supplier details).

## Start here

**Pocket-door research phase (24 Oct 2026): research only, no product selected, no drawing changed.**

- `POCKET_DOOR_CANDIDATE_COMPARISON.md`: decision matrix and answers.
- `POCKET_DOOR_SOURCE_REGISTER.csv`: every source, with its evidence class.
- `ISSUE_GATE_STATUS.md`: OQ-05, OQ-06 and OQ-07, all OPEN.
- `RFI_01_POCKET_DOOR_MANUFACTURER_DRAFT.md` and `RFI_02_KITCHEN_SUPPLIER_DRAFT.md` (**DRAFT — NOT SENT**). These supersede the earlier RFI-01 / RFI-02 drafts.
- **Send-ready manufacturer enquiries (DRAFT — NOT SENT), in priority order:**
  1. `RFI_01A_ECLISSE_Classic_Single_PW900_DRAFT_NOT_SENT.md`
  2. `RFI_01B_JB_Kind_POCSYSSGL915_DRAFT_NOT_SENT.md`
  3. `RFI_01C_Scrigno_Single_Pocket_DRAFT_NOT_SENT.md`
- `POCKET_DOOR_CALCULATOR_INPUTS_TEMPLATE.json`: input template for the confirmed data.
- **RFI audit (24 Oct 2026), updated in revision 6:**
  - `RFI_SOURCE_VERIFICATION_REPORT.md`
  - `RFI_CALCULATOR_MAPPING_GAPS.md`
  - `RFI_CALCULATOR_FIELD_TRACEABILITY.csv`: 91 items mapped to the **adopted** calculator.
  - `RFI_CALCULATOR_FIELD_DISPOSITIONS.csv`: each of the 91 items' disposition against the **proposed** calculator.
  - Result:
    - The audit findings are applied. 01A PASS and 01B PASS; 01C BLOCKED (no manufacturer data). All three remain DRAFT — NOT SENT.
    - Adopted-calculator mapping: incomplete.
    - Proposed-calculator mapping: complete (the code, schema and tests agree).
- **`CALCULATOR_PROPOSAL_NOT_ADOPTED/` (revision 6):** a fail-closed calculator and 64 tests, **for review**. Start with `README_FOR_REVIEW.md`. The adopted `evidence/scripts/gate_calc.mjs` is unchanged and must not be used for decisions until the fixes are reviewed.
- `RESEARCH_VALIDATION_LOG.md`: start state, sources, failures, calculator regression and end state.

0. `MMUCO_ORION_Duplex_Draft_0.2.3_PROPOSED_Issue_Gate_SCRATCH.md`: what must happen before any issue (OQ-06, OQ-07, OQ-05, re-validation, approval), with current status. Two draft requests support it: `RFI-01_…` (door system) and `RFI-02_…` (kitchen end panel). **Neither has been sent.**
1. `MMUCO_ORION_Duplex_Draft_0.2.3_PROPOSED_VF07_Change_Report_SCRATCH.md`: what changed, with before/after measurements for both dwellings.
2. `MMUCO_ORION_Duplex_Draft_0.2.3_PROPOSED_Validation_Report_SCRATCH.md`: every check with PASS / FAIL / BLOCKED / NOT TESTED.
3. `MMUCO_ORION_Duplex_Draft_0.2.3_PROPOSED_VF07_Comparison_SCRATCH.pdf`: before/after drawing.
4. `MMUCO_ORION_Duplex_Draft_0.2.3_PROPOSED_Open_Question_Register_SCRATCH.csv`: open items with owners.

## Contents

| Item | What it is |
|---|---|
| `…_PROPOSED_SCRATCH_NOT_ISSUED.dxf / .pdf / .png` | Proposed drawing (A1 portrait, 1:50 verified from the PDF) |
| `…_PROPOSED_VF07_Comparison_SCRATCH.pdf / .png` | Before/after comparison, both dwellings (A1 landscape) |
| `…_Room_Schedule`, `…_Door_Schedule`, `…_Entity_Change_List`, `…_Open_Question_Register` (CSV) | Schedules and registers generated from the saved DXF |
| `…_VF07_Change_Report`, `…_Validation_Report`, `…_Change_Log` (MD) | Reports |
| `…_PROPOSED_Manifest_SCRATCH.sha256` | SHA-256 of every file in this folder (except the manifest itself) |
| `evidence/` | Preservation records, measurements, regression outputs and diffs, positive controls, entity diff, scale and render checks, visual crops, scripts |
| `source_copies/` | Byte-identical copies of the issued 0.2.2 DXF and room schedule, and the VF-07 design-basis files |
| `WORKING_COPY_from_Draft_0.2.2.dxf` | Copy opened in CADCraft as the starting point; never saved over (byte-identical to the issue) |
| `working_files/` | Intermediate saves (WIP) |
| `TEST_positive_controls/` | Disposable copies with deliberate faults, used to prove the checks detect them. Not design files |
| `comparison_source/` | Source DXF and script of the comparison sheet |
| `gate_inputs/` | Blank input template for the manufacturer / supplier data, and placeholder scenarios (not product data) |
| `evidence/scripts/gate_calc.mjs`, `evidence/scripts/rerun_validation.sh` | Gate calculator (adopted; known defects G3 and G6, so not for decisions until the fixes are reviewed), and a one-command rerun of all checks on a revised scratch DXF |
| `CALCULATOR_PROPOSAL_NOT_ADOPTED/` | Proposed fail-closed calculator, proposed template, test suite and test outputs. **Not adopted** |
