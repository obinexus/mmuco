# Change log: proposed Draft 0.2.3 (SCRATCH, NOT ISSUED)

24 October 2026. Base: issued Draft 0.2.2 (`MMUCO_ORION_Duplex_Draft_0.2.2.dxf`, SHA-256 2ec8d3f3…d17b). The scope is VF-07 Option A only, plus the annotation and dimension changes needed to show and verify it.

## Drawing entities changed

These are the full list from the whole-drawing entity diff. Everything else is unchanged: 526 entities.

| Handle | Type | Change |
|---|---|---|
| 1E0 | Kitchen base run, dwelling A | West end moved from x 2,100 to x 2,400 (vertices 0 and 3); 2,200 → 1,900 mm |
| 1E1 | Kitchen base run, dwelling B | East end moved from x 16,500 to x 16,200 (vertices 1 and 2); 2,200 → 1,900 mm |
| 47EF | Dimension (new) | Kitchen-side nib, dwelling A: 300, associated to wall 125 and unit 1E0 |
| 47F0 | Dimension (new) | Kitchen-side nib, dwelling B: 300, associated to unit 1E1 and wall 126 |
| 2DA | Title | "MMUCO ORION DUPLEX - PROPOSED 0.2.3 - NOT ISSUED" |
| 2DC | Status line | "…SCRATCH REVIEW COPY - NOT ISSUED - NOT APPROVED - NOT FOR CONSTRUCTION - NOT A COMPLIANCE DRAWING" |
| 147E | Revision line | Proposed 0.2.3 (scratch): VF-07 Option A description; keeps the 0.2.2 summary |
| 2F8 | Notes | Header "PROPOSED DRAFT 0.2.3, SCRATCH - NOT ISSUED"; note 2 adds the nib basis (finished face of end panel or worktop) and the door-system status |
| 2FB | Scale note | Refers to the 0.2.3 scratch Validation Report. Changed only after the plotted scale was measured |

## Deliberately not changed

- Walls and partitions, the pocket doors (openings, cavities, leaves) and all services.
- Every other unit, every room label and the on-sheet room schedule (2F9).
- The subtitle (2DB) and the legend (2E4), whose M4(2) wording is recorded as NF-02 / OQ-12.
- VF-04, VF-05, VF-06, the hallway door decisions and OBS-1, all carried unchanged.

## Files created (all under `MMUCO_ORION_Duplex_Draft_0.2.3_SCRATCH_not_issued/`)

**Proposed drawing:**

- `MMUCO_ORION_Duplex_Draft_0.2.3_PROPOSED_SCRATCH_NOT_ISSUED.dxf`, `.pdf` (A1 portrait, 1:50 verified), `.png`

**Comparison:**

- `MMUCO_ORION_Duplex_Draft_0.2.3_PROPOSED_VF07_Comparison_SCRATCH.pdf` / `.png`: before/after, both dwellings, 1:50 plans and 1:20 details
- Source drawing and script in `comparison_source/`

**Schedules and registers:**

- `…_PROPOSED_Room_Schedule_SCRATCH.csv`
- `…_PROPOSED_Door_Schedule_SCRATCH.csv`
- `…_PROPOSED_Entity_Change_List_SCRATCH.csv`
- `…_PROPOSED_Open_Question_Register_SCRATCH.csv`

**Reports:**

- `…_PROPOSED_VF07_Change_Report_SCRATCH.md`
- `…_PROPOSED_Validation_Report_SCRATCH.md`
- this change log
- `README_NOT_ISSUED.md`
- `…_PROPOSED_Manifest_SCRATCH.sha256`

**Working material:**

- `evidence/`: preservation records, measurements, regression outputs and diffs, positive controls, entity diff, scale and render checks, visual crops, scripts
- `source_copies/`: byte copies of the 0.2.2 DXF and room schedule, and the VF-07 design-basis files
- `WORKING_COPY_from_Draft_0.2.2.dxf`: never saved over
- `working_files/`: intermediate WIP saves
- `TEST_positive_controls/`: disposable fault copies, not deliverables

## Revision 2 (24 Oct 2026, 21:48 onwards): issue-gate preparation

There is no drawing change in this revision. The proposed DXF, PDF and PNG are unchanged; their hashes are as in revision 1.

**Added:**

- `…_PROPOSED_Issue_Gate_SCRATCH.md`: the issue gate (OQ-06, OQ-07, OQ-05, CAD validation, approval) with current status and the evidence still needed. All are OPEN or NOT GIVEN except CAD validation, which passes for the current geometry.
- `RFI-01_Pocket_Door_System_DRAFT_not_sent.md` and `RFI-02_Kitchen_End_Panel_Setting_Out_DRAFT_not_sent.md`: requests for the designer to send. **Not sent.**
- `gate_inputs/OQ05_OQ06_inputs_TEMPLATE.json`: blank input file for the manufacturer and supplier data.
- `gate_inputs/PLACEHOLDER_scenarios_NOT_PRODUCT_DATA.json`: illustration only.
- `evidence/scripts/gate_calc.mjs`: turns supplied data into clear opening, pocket fit, finished-face nib and the geometry needed for an 850 mm clear opening. Reports UNKNOWN when data is missing.
- `evidence/scripts/rerun_validation.sh`: one-command rerun of the validation suite on a revised scratch DXF. Its first self-test failed (relative output path); fixed, then rerun on the current proposed DXF: 9 of 10 outputs are byte-identical to the recorded evidence, and the tenth differs only in the source-file path string (`evidence/09_rerun_selftest/`).
- `evidence/08_gate_calculator/`: calculator outputs for the blank template (all UNKNOWN) and the placeholders.

**Updated:**

- Open-question register: OQ-05, OQ-06 and OQ-07 now carry the closure evidence and owners set out in the issue-gate instruction. OQ-07 states that the 850 mm target is not demonstrated.
- README and this log.
- The scratch manifest, regenerated to include the new files.

## Revision 3 (24 Oct 2026, 21:56 onwards): pocket-door research phase

There is no drawing change: the proposed DXF, PDF and PNG are byte-identical to revisions 1 and 2. No product was selected, no OQ was closed, and no third party was contacted.

**Added:**

- `POCKET_DOOR_CANDIDATE_COMPARISON.md`
- `POCKET_DOOR_SOURCE_REGISTER.csv`
- `POCKET_DOOR_CALCULATOR_INPUTS_TEMPLATE.json`
- `RFI_01_POCKET_DOOR_MANUFACTURER_DRAFT.md` and `RFI_02_KITCHEN_SUPPLIER_DRAFT.md`, both DRAFT — NOT SENT
- `ISSUE_GATE_STATUS.md`
- `RESEARCH_VALIDATION_LOG.md`
- `gate_inputs/pocket_door_candidates_RESEARCH_inputs.json`
- `evidence/10_research/`
- `evidence/scripts/gen_source_register.mjs`

**Changed:**

- `evidence/scripts/gate_calc.mjs` gains an optional `kit` block. It reads manufacturer frame widths as published and never uses them as the passage gap. Existing outputs are unchanged: the template and placeholder runs are byte-identical before and after.
- Open-question register: the OQ-06 and OQ-07 evidence fields now cite the research. The statuses are unchanged (OPEN).
- README and this log.
- The scratch manifest, regenerated.

## Revision 4 (24 Oct 2026, 22:16 onwards): send-ready enquiry drafts

**Instruction:** treat ECLISSE Classic Single PW 900 as the first enquiry, then pursue all three candidates. No drawing change: the proposed DXF, PDF and PNG are unchanged. Nothing was sent and no OQ status changed.

**Added (each DRAFT — NOT SENT, standalone email draft with questions and a figures-to-confirm table mapped to the calculator fields):**

- `RFI_01A_ECLISSE_Classic_Single_PW900_DRAFT_NOT_SENT.md` (priority 1)
- `RFI_01B_JB_Kind_POCSYSSGL915_DRAFT_NOT_SENT.md` (priority 2)
- `RFI_01C_Scrigno_Single_Pocket_DRAFT_NOT_SENT.md` (priority 3)

**Contact details:** ECLISSE's are copied from its datasheet. JB Kind and Scrigno are left for the designer to confirm, because they were not taken from a verified source.

**Updated:**

- `RFI_01_POCKET_DOOR_MANUFACTURER_DRAFT.md`: index of the send-ready drafts.
- `ISSUE_GATE_STATUS.md`: enquiry order recorded; drafts prepared, not sent.
- README and this log.
- The scratch manifest, regenerated.

## Revision 5 (24 Oct 2026, 22:22 onwards): RFI audit

This was an audit only.

**Not changed:**

- the three RFIs, `gate_calc.mjs` and both input templates (hashes compared before and after);
- the proposed DXF, PDF and PNG.

Nothing was sent and no OQ was closed.

**Added:**

- `RFI_SOURCE_VERIFICATION_REPORT.md` (Audits A and C)
- `RFI_CALCULATOR_MAPPING_GAPS.md` (Audit B gaps and proposed schema changes, not applied)
- `RFI_CALCULATOR_FIELD_TRACEABILITY.csv` (89 items, generated by `evidence/scripts/rfi_trace.mjs`)
- `evidence/11_rfi_audit/`, containing the start and end state, template-field usage, and the gap demonstration inputs and results

**Results:**

- 01A PASS (minor edits recommended)
- 01B PASS (minor edits recommended)
- 01C BLOCKED: manufacturer verification unavailable
- Calculator mapping INCOMPLETE: no item maps to a validated field

## Revision 6 (24 Oct 2026): audit findings applied, enquiries finalised, calculator fix proposed

**Instructions:**

- Apply findings F-ALL1, F-A1, F-A2, F-B1, F-C1, F-C2 and F-ALL2, keeping the drafts DRAFT — NOT SENT.
- Fix the calculator with fail-closed validation and tests, **without changing the existing calculator until review**.
- Give every RFI item an explicit disposition.
- Finalise the three enquiries.
- Keep the issue gate closed.

**Not changed:**

- `evidence/scripts/gate_calc.mjs` (SHA-256 `f4f0ddcb…`, checked before and after every test run);
- both adopted input templates;
- the proposed DXF, PDF and PNG;
- every frozen file.

Nothing was sent, no manufacturer was contacted, and no OQ was closed.

**Edited (all still DRAFT — NOT SENT):**

- `RFI_01A_…`:
  - F-ALL1, F-A1 and F-A2 applied.
  - Distinguishes the two PW 900 rows (PH 2030 vs PH 1971) in the body and in Q1.
  - Annotation questions retained.
- `RFI_01B_…`:
  - F-ALL1, F-B1 and F-ALL2 applied.
  - Uses JB Kind's exact headings "Clear Opening Size (walkthrough area)" and "Structural Opening Size of the Unit".
- `RFI_01C_…`:
  - F-ALL1, F-C1, F-C2 and F-ALL2 applied.
  - The standard and fire-rated retailer listings are kept separate (Appendix C now has 10 rows).
  - Asks Scrigno to identify the product line and official dimensions of each.

**Added:**

- `CALCULATOR_PROPOSAL_NOT_ADOPTED/`:
  - `gate_calc_PROPOSED.mjs`
  - `POCKET_DOOR_CALCULATOR_INPUTS_TEMPLATE_PROPOSED.json`
  - `tests/run_tests.mjs`
  - `test_output/`
  - `README_FOR_REVIEW.md`
- `RFI_CALCULATOR_FIELD_DISPOSITIONS.csv`
- `evidence/12_rfi_revision6/` (start and end state)

**Updated:**

- `evidence/scripts/rfi_trace.mjs`:
  - parses follow-on paragraphs;
  - re-keys RFI_01C Appendix C;
  - updates the evidence notes;
  - adds the dispositions and the code / schema / test agreement check.
- `RFI_CALCULATOR_FIELD_TRACEABILITY.csv`: regenerated, 91 items.
- `RFI_SOURCE_VERIFICATION_REPORT.md` and `RFI_CALCULATOR_MAPPING_GAPS.md`.
- `ISSUE_GATE_STATUS.md`: decision path only; no status changed.
- The README, this log, and the scratch manifest.

**Results:**

- **Changed claims:** all re-checked against S-02 (local copy, hash unchanged) and against S-01, S-06 and S-07 (re-loaded). All verified.
- **Drafts:** 01A PASS; 01B PASS; 01C BLOCKED (no manufacturer data).
- **Tests:** 64 of 64 passed:
  - regression on all four existing input files: identical, except the 132 legacy values that are deliberately not computed in kit mode;
  - the demonstrated G3 / G6 defects are now rejected;
  - 31 fields CALC, 24 ECHO and 4 NONE, each confirmed by perturbation.
- **Dispositions:**
  - 91 items: 82 VALIDATED_FIELD (58 influence a calculation, 24 echo only), 9 EVIDENCE_ONLY, 0 SCHEMA_GAP.
  - Complete against the proposed calculator only. 16 RFI Appendix C field cells need updating if it is adopted.
- **Known item:** the internal designer's note in RFI_01A (to be deleted before sending) still names `gate_calc.mjs`. The issue-gate decision path now says no calculator is to be used for decisions until the fixes are reviewed.

## Process notes

- **Dimension placement:** the nib dimensions were placed twice before the final position. The first text clashed with the "tall units" label; the second line sat 16.5 mm above the unit front. The final dimension line is at y 9,100 inside the nib, and the text is in clear floor.
- **Dimension text mirroring:** B's text was moved to x 16,750, so it mirrors A's exactly (error 0 mm).
- **Title length:** the title was first written longer and ran 520 mm past the existing sheet extents. It was shortened so the plot frame did not move.
- **Hardened check script:** `d023_checks.mjs` crashed on positive control PC2 (base run displaced into the wall). The lookup was hardened and every result was re-run; outputs were byte-identical to the earlier runs.
- **Corrected root-file test:** the first end-check test for "no 0.2.3 files at the project root" was wrong (`ls` listed the scratch folder's contents). It was replaced with a files-only `find` (count 0) and the record rewritten.
