# Gate calculator status contract: PROPOSED — NOT ADOPTED

**This folder is an isolated implementation for review.** It is not adoption, release, design approval or regulatory sign-off.

- **Not changed:** the adopted `evidence/scripts/gate_calc.mjs`, the original proposal one level up (calculator, template, tests, README), the RFIs, drawings, evidence, manifests and earlier drafts. Their hashes were recorded before the work and verified after it (`evidence/`).
- **No gate status changed:** OQ-05, OQ-06 and OQ-07 remain OPEN. Draft 0.2.3 is not issued.
- **What CHECKS_PASSED means:** the configured project checks passed against the evidence references supplied. It is never design approval, manufacturer confirmation or regulatory compliance.

## Contents

| Path | What it is |
|---|---|
| `gate_calc_STATUS_CONTRACT_PROPOSED.mjs` | The calculator with the status contract (copied from `../gate_calc_PROPOSED.mjs`, then changed) |
| `POCKET_DOOR_CALCULATOR_INPUTS_TEMPLATE_STATUS_CONTRACT_PROPOSED.json` | Template copy: `kit.evidenceClass` is `null`; the instructions are updated |
| `tests/run_tests_STATUS_CONTRACT.mjs` | 94 tests: the 64 original tests ported, plus 25 contract tests T1–T21 (and extra protected-hash and regression checks) |
| `test_output/` | Test results (`test_results.md` / `.json`), tested field roles, adopted-calculator outputs, command-line fixtures and their outputs |
| `scripts/rfi_trace_STATUS_CONTRACT.mjs` | Copy of `evidence/scripts/rfi_trace.mjs`, pointed at this calculator; writes only to `traceability/` |
| `traceability/` | Adopted mapping (byte-identical to the protected CSV), dispositions against this calculator, field usage |
| `evidence/` | Protected-file snapshots before and after, copy provenance, and the original suite's baseline run |

**To run** (from the scratch folder):

```bash
node CALCULATOR_PROPOSAL_NOT_ADOPTED/STATUS_CONTRACT_PROPOSED/tests/run_tests_STATUS_CONTRACT.mjs CALCULATOR_PROPOSAL_NOT_ADOPTED/STATUS_CONTRACT_PROPOSED/test_output
```

```bash
node CALCULATOR_PROPOSAL_NOT_ADOPTED/STATUS_CONTRACT_PROPOSED/scripts/rfi_trace_STATUS_CONTRACT.mjs . CALCULATOR_PROPOSAL_NOT_ADOPTED/STATUS_CONTRACT_PROPOSED CALCULATOR_PROPOSAL_NOT_ADOPTED/STATUS_CONTRACT_PROPOSED/traceability
```

```bash
node CALCULATOR_PROPOSAL_NOT_ADOPTED/STATUS_CONTRACT_PROPOSED/gate_calc_STATUS_CONTRACT_PROPOSED.mjs evidence/01_measurements/door_geometry_023.json <inputs.json> [out.json]
```

## 1. Status contract

| Field | Values | Question |
|---|---|---|
| `calculationStatus` | `SUCCESS`, `INPUT_ERROR`, `CALCULATION_ERROR` | Did the software validate the input and finish the arithmetic? |
| `geometryStatus` | `POSSIBLE`, `IMPOSSIBLE`, `UNKNOWN` | Can the configuration exist in the measured plan? |
| `designStatus` | `PASS`, `CONFLICT`, `UNKNOWN` | Does it meet every mandatory project target and fit check? |
| `outcome` | see below | The only acceptance answer |

**Also on every result:**

- `exitCode`;
- `issues[]`, each with `code`, `severity`, `category`, `rule`, `dwelling`, `run`, `field`, `actual_mm`, `required_mm`, `shortfall_mm`, `targetSource` and `message`;
- `checks[]`, each with `rule`, `result` (`PASS` / `FAIL` / `UNKNOWN`), `actual_mm`, `required_mm`, `margin_mm`, `basis` and `targetSource`;
- `warnings[]` and `errors[]`, derived from the issues;
- `inputProvenance` (was `inputStatus`), `informationalKeys` and `disclaimer`.

**There is no `status` key, and `OK` appears nowhere.**

### Outcomes, precedence and exit codes

| Precedence | Outcome | Exit | When | Dimensions in output |
|---|---|---|---|---|
| 1 | `CALCULATION_ERROR` | 1 | Geometry file unusable, exception, non-finite number in the output, contract violation, usage error | No |
| 2 | `INPUT_ERROR` | 2 | Malformed, non-finite, contradictory, missing-required or physically invalid input; input file unreadable or not JSON; no scenarios | No (fails closed) |
| 3 | `GEOMETRY_IMPOSSIBLE` | 3 | Utility-side nib < 0, or kitchen base run ≤ 0, in any dwelling or tolerance run | Yes; the values describe the impossible configuration |
| 4 | `DESIGN_CONFLICT` | 4 | A mandatory project target or fit check fails on known data | Yes |
| 5 | `REVIEW_REQUIRED` | 5 | A mandatory check is UNKNOWN, evidence is missing, or an unauthorised geometry change is needed | Yes |
| 6 | `CHECKS_PASSED` | 0 | Every mandatory check passes and every evidence reference is present | Yes |

**Single scenario** (`deriveOutcome`): the first matching row of the table wins.

**Several scenarios** (`aggregateOutcome`):

- The overall outcome is the highest-precedence outcome among the scenarios, so a favourable scenario can never mask an invalid one.
- An empty scenario list is `INPUT_ERROR`.
- The JSON `overallOutcome` and `exitCode` always equal the process exit code. T16 checks this on 32 command-line runs, including every ordering of six mixed files.

**Combined defects in one input:** every independently detectable input issue is reported in one pass, and no calculation runs.

- A consistency rule that depends on a malformed field is listed as `NOT_EVALUATED` (severity INFO), instead of being skipped silently.
- Mixing kit and legacy fields is judged on presence, so it is reported even when the kit value is itself malformed (T11).

**Allowed combinations** (`checkInvariants`; T17 checks every result produced):

- A failed calculation reports `UNKNOWN` geometry and design, no checks and no dimensions.
- `IMPOSSIBLE` geometry means the design is `UNKNOWN` (not evaluated).
- Design `PASS` requires geometry `POSSIBLE` and every design check `PASS`.
- Design `CONFLICT` requires a failed check and a `BLOCKING` issue.
- `CHECKS_PASSED` allows no `ERROR`, `IMPOSSIBLE`, `BLOCKING` or `REVIEW` issue.
- The command line converts any violation into `CALCULATION_ERROR`.

**Severities:**

| Severity | Effect |
|---|---|
| `ERROR` | Input or calculation |
| `IMPOSSIBLE` | Geometry |
| `BLOCKING` | Design conflict |
| `REVIEW` | Missing data, missing evidence or a geometry change |
| `WARNING` | Never changes any status (T15) |
| `INFO` | Never changes any status |

## 2. Rules and their severity

| Rule | Check | On FAIL | On missing data | Source of the requirement |
|---|---|---|---|---|
| **DT-1** | Installed clear width ≥ `targets.projectClearTarget_mm`. Kit: manufacturer-stated installed width, else stated passage − confirmed reduction. A stated passage below the target is a certain fail, because the installed width cannot exceed it. Legacy: project-basis clear | BLOCKING, "project-target conflict" | REVIEW | **Project design target R-14, status PROPOSED, OQ-08 open.** A configured project target: not an approved requirement and not a regulatory minimum |
| **DT-2** | Kitchen finished-face nib ≥ nib target + agreed tolerance, per dwelling. After a latch move, the calculated base-run position gives the nib (part of GC-1) | BLOCKING | REVIEW. The kit dimensions still assume finished face and 0 mm (`nibBasis` says so), but that is never a pass | **Project design target** (300 mm, from the M4(2) design intent, ADM para 2.22d). Not established for this project: OQ-01, OQ-02 and OQ-03 are open |
| **DT-3** (Option A) | Utility-side nib ≥ nib target, per dwelling, at **every** tolerance run (the worst case governs). 300 passes; 299 fails | BLOCKING, with dwelling, run, actual, required and shortfall | REVIEW | Same project target. No construction tolerance on this side |
| **GI-1 / GI-2** | Utility-side nib ≥ 0; base run > 0 (signed values, no `Math.abs`) | IMPOSSIBLE | — | Model integrity |
| **CP-1** | Kit finished-wall options include the project partition | BLOCKING, "fit conflict" | REVIEW | Fit to the drawn construction |
| **CP-2** | Available head height ≥ required (the larger of the stated minimum head height and the stud-opening height; frame height alone is only a lower bound) | BLOCKING | REVIEW | Fit |
| **CP-3** | Legacy: pocket + end allowance ≤ available; leaf ≤ pocket | BLOCKING | REVIEW | Fit |
| **GC-1** | Latch jamb move ≠ 0 | REVIEW (needs authorisation and a new scratch revision) | — | Issue gate |
| **EV-1 to EV-5** | Written-confirmation reference; datasheet date **and** installation-drawing reference; `kit.evidenceClass` exactly "manufacturer-confirmed for this project"; kitchen confirmation reference; same kitchen detail in both dwellings = `true` | REVIEW | REVIEW | Presence only: the software cannot verify a document |
| **Warnings** | Tolerance ignored with a stud opening; panel ignored; target below 300 (check units); unknown `doorSystem` key; passage starts in front of the tall units | WARNING | — | Not targets |
| **Info** | ADM table rows; `statedMeets850`; the legacy latch-move suggestion and its feasibility (D6) | INFO | — | Reference only |

**Consequences of these rules:**

- **Legacy mode can at best reach REVIEW_REQUIRED.** It has no wall-thickness or head-height inputs, so CP-1 and CP-2 stay UNKNOWN.
- **Every issue message says "project-target conflict" or "fit conflict" and "Not a regulatory finding".** T17 scans every message for regulatory-breach wording.

## 3. The three clarifications

1. **Project targets vs approved or statutory requirements.**
   - DT-1 carries the `targetSource` above (R-14, PROPOSED, OQ-08 open; "not an approved requirement and not a regulatory minimum").
   - DT-2 and DT-3 carry the M4(2) design-intent wording, with OQ-01 to OQ-03 open.
   - A changed target is reported as "set in the input", with its difference from R-14.
   - Tested in T3 and T14.
2. **T2 and T3 checked against the real formula.**
   - The utility nib is (external-wall face to utility-return face) − pocket-end gap − run.
   - From the measured faces (`limitX_native`, both dwellings) that distance is **2,500 mm**. The faces derived from the `wallNib_mm` fields agree (GEO2).
   - So a **2,200 mm** stud opening gives **300 mm** and **2,201 mm** gives **299 mm**, in both dwellings. These values were also run through the calculator before coding.
   - The tests derive every boundary value from the geometry and never type them in: T1 zero-move run 1,800; T2 2,200; T3 2,201; T4 2,550; T5 base run 97 mm.
   - For T5, the measured geometry file is not changed. The test uses an in-memory copy with a shorter base run, because the real plan reaches the return wall first.
3. **Deterministic precedence for combined results.** See section 1. Tested in T16 (command line, every ordering) and T17 (all 36 outcome pairs and all 54 status combinations).

## 4. Validation policy (what "validated" means)

**Numbers:** finite JSON numbers only.

- Rejected: numeric strings, strings with units, `""`, booleans, lists, objects, `NaN`, `Infinity`, and `1e999` (which JSON reads as `Infinity`).
- Minimums follow each field's meaning: lengths ≥ 1 mm; allowances, tolerances, offsets and reductions ≥ 0.

**Required inputs:**

- Both stud-tolerance limits or neither (`TOLERANCE_PAIR`; new).
- A reduction needs a stated passage (`REDUCTION_NEEDS_PASSAGE`; was a warning).
- The carcass datum needs the panel thickness and the overhang.
- All other fields are optional: a missing value gives `UNKNOWN`, then `REVIEW_REQUIRED`, never a pass.

**Unknown keys:** an `INPUT_ERROR` in the calculation blocks; a `WARNING` in `doorSystem`. A misspelt evidence key therefore leaves the evidence missing, which gives `REVIEW_REQUIRED`.

**Validation depth:** recorded per field in `traceability/RFI_CALCULATOR_FIELD_DISPOSITIONS_STATUS_CONTRACT.csv`, column `validation_depth`.

- Text fields are checked for type only. Their content (a reference number, a date) is **not verified** by software.
- Manufacturer figures can be checked for type, range and consistency, but **not for whether they were entered under the right definition**. For example, whether JB Kind's "Structural Opening Size of the Unit" is the stud opening, or whether Scrigno's 896 is already net of the 10 mm. That stays with the designer.

**Legacy tri-state values** (`nib.ok`, `meetsProjectTarget850`, `statedMeets850`, `installedMeets850`, `headHeightOk`, `compatible`, `fitsCurrentWallRun`, `kitchenApproachClearOfTallUnits`):

- They are kept for regression traceability and listed in `informationalKeys` as not for acceptance.
- T17 confirms that no `CHECKS_PASSED` result has any of the mandatory ones false or `"UNKNOWN"`.

## 5. Changes from the original proposal

| Change | Effect |
|---|---|
| `status` replaced by the four fields; `inputStatus` renamed `inputProvenance` | D1 |
| Per-run `geometryStatus` renamed `geometryCheck`; it no longer carries `CONFLICT` | The nib conflict now lives in `checks[]` and `issues[]` |
| Option A, the evidence checks, CP checks and GC-1 added | Existing scenarios are no longer "OK" (section 6) |
| All independent input issues reported; `NOT_EVALUATED` marks dependent checks | D12 |
| `TOLERANCE_PAIR` and `REDUCTION_NEEDS_PASSAGE` are errors | Required inputs |
| Required head height = the larger of the stated minimum and the stud-opening height (was: stated minimum first) | Stricter; no existing input has both |
| `installedClearWidthCalculated_mm` added beside the stated and manufacturer-installed widths | The three widths kept distinct |
| Field role `ACCEPTANCE` added for 6 evidence fields | D8 |
| `kit.evidenceClass`: free text, but only the exact value "manufacturer-confirmed for this project" passes EV-3 | **A deviation from the letter of D8, which said "becomes an enum".** All six research inputs use other free-text classes. An enum would turn them into INPUT_ERROR and destroy their 742-value regression comparison. The acceptance effect is identical: anything else needs review. The template value is now `null`, as D8 asked |
| Command line: one payload with `overallOutcome`, `exitCode` and `outcomeCounts`; summary line; exit codes 0–5 | D9 |

**Dimensional arithmetic is unchanged.** Against the original proposal on all 11 existing scenarios (R5): 1,086 dimensional values; 1,064 identical, 22 renamed (`geometryStatus` → `geometryCheck`), 14 added.

## 6. Results (25 Oct 2026)

**Baseline:** the original 64-test suite, run unchanged, passed 64 of 64. Its output is in `evidence/baseline_original_suite/`.

**This suite: 94 of 94 passed.**

- **69 ported tests:** the original 64 less the 2 role tests, which became T21a and T21, plus 7 extra hash and regression checks.
- **25 contract tests.**
- **12 changed expectations**, each with its reason, are listed in `test_output/test_results.md`. In summary:
  - the helpers use the four fields;
  - R1–R4 assert `calculationStatus` SUCCESS;
  - P6 becomes DESIGN_CONFLICT (D6);
  - P8: the research file exits 4;
  - N1 gives both tolerance limits;
  - S4: the blank template is REVIEW_REQUIRED;
  - T21 uses the four-role taxonomy;
  - D3 is strengthened.

**Regression against the adopted calculator** (R1–R4): 1,084 adopted values compared; 952 identical, and 132 legacy values intentionally not computed in kit mode (G3). No other difference.

**Existing scenarios, before → after:**

| Scenario | Original proposal | This contract | Exit | Deciding checks |
|---|---|---|---|---|
| Blank template; OQ05 template | OK | REVIEW_REQUIRED | 5 | No data |
| P1 placeholder (deductions 40) | OK | DESIGN_CONFLICT | 4 | DT-1: 810 < 850 |
| P2, P3 placeholders | OK | DESIGN_CONFLICT | 4 | DT-1: 770; DT-2: kitchen nib 282 / 272 < 310 |
| JBK-915 | OK | DESIGN_CONFLICT | 4 | CP-1: 125 mm wall only |
| JBK-838 | OK | DESIGN_CONFLICT | 4 | DT-1: stated 800; CP-1 |
| ECL-900, ECL-850 | OK | REVIEW_REQUIRED | 5 | Installed width, head height and kitchen datum unknown; latch move; evidence missing |
| SCR-926, SCR-926-FR | OK | DESIGN_CONFLICT | 4 | CP-1: 125 mm wall only |

DT-3 changes none of these scenarios: their utility nibs are 570–775 mm (700 mm as drawn in legacy mode).

**Field roles (tested by perturbation):** 31 CALC, 6 ACCEPTANCE, 18 ECHO and 4 NONE (59 fields). All agree with the declared roles.

**Traceability** (`traceability/`):

- 91 items, every one with a disposition: 82 VALIDATED_FIELD, 9 EVIDENCE_ONLY, 0 SCHEMA_GAP. The code, isolated template and tests agree.
- **Influence:**

  | Influence | Items |
  |---|---|
  | YES | 31 |
  | YES, with acceptance-only or echo-only fields | 27 |
  | Acceptance only | 15 |
  | Echo only | 9 |
  | No field | 9 |

- 15 items moved from echo only to acceptance only; these are the documentary evidence references.
- No disposition or field mapping changed.
- 16 RFI Appendix C cells would still need updating on adoption.
- The adopted-mapping CSV regenerated here is byte-identical to the protected `RFI_CALCULATOR_FIELD_TRACEABILITY.csv`.

## 7. Backward compatibility and remaining questions

- **Downstream callers:** no script consumes either calculator's status or exit code. The only callers are the test suites and `rfi_trace.mjs`. Human instructions in `ISSUE_GATE_STATUS.md`, the Issue Gate document, the RFI_01A designer's note and the template `howToRun` text would need updating on adoption.
- **Inputs that previously ran and are now rejected:** numbers as text; `""` for a blank (use `null`); kit and `door.*` together; a single tolerance limit; a reduction without a passage.
- **External evidence still required for any CHECKS_PASSED result on a real product:**
  - installed clear width for a named configuration;
  - stud opening or tolerance;
  - pocket-end detail;
  - minimum head height, and the project's available head height (no section exists);
  - wall-thickness option;
  - kitchen datum and tolerance (OQ-05);
  - written confirmation, dated datasheet and installation drawing.
- **Any latch move still needs an authorised geometry change** (GC-1).
- **Open decisions** (not made here):
  - whether R-14 stays the configured clear-width target (OQ-08);
  - whether the 300 mm nib applies at all, and to which face (OQ-01 to OQ-03);
  - whether the evidence-class deviation from D8 is acceptable.

## 8. Correction to `../README_FOR_REVIEW.md` (that file is not edited)

Its section 5, step 4 says to update `rerun_validation.sh` on adoption. **That is wrong:** `evidence/scripts/rerun_validation.sh` does not call either calculator (checked 25 Oct 2026).

**Corrected adoption steps, if adoption is ever authorised:**

1. Replace `evidence/scripts/gate_calc.mjs` with the reviewed calculator, recording the old and new hashes.
2. Replace the inputs template.
3. Update the 16 RFI Appendix C "Our calculator field" cells, then re-hash and re-check the RFIs. They stay DRAFT — NOT SENT.
4. Update the adopted mapping in `evidence/scripts/rfi_trace.mjs`, and the human instructions listed in section 7.
5. Re-run the tests, the regression and the traceability generator, then regenerate the scratch manifest.
