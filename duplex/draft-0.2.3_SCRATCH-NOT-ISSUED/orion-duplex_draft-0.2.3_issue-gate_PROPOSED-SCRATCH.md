# Proposed Draft 0.2.3: issue gate (SCRATCH, NOT ISSUED)

**Status at 24 Oct 2026: gate NOT passed. Draft 0.2.3 must not be issued.**

## Gate

| Gate | Required outcome | Status | Evidence on file | Evidence still needed | Owner |
|---|---|---|---|---|---|
| **OQ-06** | Door system specified and documented | **OPEN** | None: no product selected. RFI-01 drafted, not sent | Manufacturer, product name and model; dated datasheet and installation drawing; verified clear opening for the configuration; designer's written sign-off | Designer selects; manufacturer confirms |
| **OQ-07** | Actual clear opening assessed and accepted | **OPEN** (blocked by OQ-06) | ESTIMATE only, 770–810 mm. **The 850 mm project target is not demonstrated.** The nominal 850 mm opening is not the clear opening | The selected system's clear width; designer's written assessment against the 850 mm target and the applicable Approved Document M provisions; if the target is missed, the designer's resolution before issue | Designer; building control for the regulatory reading |
| **OQ-05** | Finished-face datum and tolerance agreed | **OPEN** | Drawn nib 300 mm (MEASURED, both dwellings) with 0 mm margin. Note 2 assumes the outline is the finished face. Carcass reading with an 18 mm panel gives 282. RFI-02 drafted, not sent | Supplier's dimensioned setting-out drawing; written confirmation of the finished-face position; designer-signed nib dimension and tolerance; confirmation for both dwellings | Designer and kitchen supplier |
| **CAD validation** | Affected dimensions, collisions, symmetry and regression checks pass | **PASS for the current scratch geometry** (Validation Report V-01 to V-21; positive controls PC1–PC4) | `evidence/`; one-command rerun `evidence/scripts/rerun_validation.sh`, self-test identical to the recorded results | Must be **re-run** after any change made for OQ-05, OQ-06 or OQ-07 | Designer (scripted checks available) |
| **Approval** | Responsible designer authorises the issue; final manifest verified | **NOT GIVEN** | Scratch manifest verifies; it is not an issue manifest | Designer's written authorisation, then a new issue manifest | Responsible designer |

The planning condition (OQ-01) and building-control interpretations (OQ-02 to OQ-04) also stay open. They decide which Approved Document M provisions the OQ-07 assessment must use.

## How the remaining work runs

1. **In parallel:** the designer sends RFI-01 (door system) and RFI-02 (kitchen end panel).
2. **Enter the answers** in `gate_inputs/OQ05_OQ06_inputs_TEMPLATE.json`, then run:
   `node evidence/scripts/gate_calc.mjs evidence/01_measurements/door_geometry_023.json gate_inputs/<filled>.json <out>.json`
   This gives the clear opening (ADM basis, with handles ignored, and project basis), the pocket fit, the finished-face nib against the agreed tolerance, and the geometry change needed for an 850 mm clear opening.
3. **If the geometry must change:**
   - Edit the **scratch** copy only, saved under a new filename.
   - Then run `bash evidence/scripts/rerun_validation.sh <new.dxf> <out_dir> <new.pdf>`.
   - Check the dimensions, collisions, symmetry, areas and entity diff before accepting the change.
   - Draft 0.2.2 is never edited.
4. **The designer records** the OQ-06 product and the OQ-07 assessment, and signs off OQ-05.
5. **The designer authorises the issue.** Only then is a formal Draft 0.2.3 produced, with its own verified manifest.

## What the placeholder runs indicate (ASSUMPTIONS, not product data)

`evidence/08_gate_calculator/gate_calc_PLACEHOLDER_scenarios.json`; the results are the same for both dwellings.

| Placeholder | Clear opening (ADM / project) | Reaches 850? | Opening needed for 850 | Latch-jamb move | Base run after (0.2.2 was 2,200) | Utility nib after | Kitchen nib (finished / required) |
|---|---|---|---|---|---|---|---|
| P1: deductions 40, finished-face datum, no tolerance | 810 / 810 | No | 890 | 80 | 1,820 | 620 | 300 / 300 |
| P2: deductions 60, handle 20, carcass with 18 mm panel, tolerance 10 | 790 / 770 | No | 930 | 160 | 1,712 | 540 | 282 / 310 |
| P3: deductions 80, carcass with 18 mm panel + 10 overhang, tolerance 10 | 770 / 770 | No | 930 | 160 | 1,702 | 540 | 272 / 310 |

**Reading:**

- With the current 850 mm structural opening, none of the plausible deduction sets reaches 850 mm clear.
- Meeting the target would move the latch jamb further from the pocket and shorten the kitchen base run further: by 80–200 mm more than proposed 0.2.3, so 380–500 mm against 0.2.2.
- The current pocket already uses all 950 mm of wall between the external wall face and the opening.

These are illustrations only. **They do not close any OQ.**
