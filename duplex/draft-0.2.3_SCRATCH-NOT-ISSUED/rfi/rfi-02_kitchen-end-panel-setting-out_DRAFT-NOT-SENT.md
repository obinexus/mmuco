# RFI-02: kitchen base run end panel and setting-out (DRAFT, NOT SENT)

**Prepared for:** the responsible designer, to send to the kitchen supplier.

**Project:** MMUCO ORION Duplex, two mirrored single-storey dwellings.

**Drawing basis:** proposed Draft 0.2.3, a scratch review copy (not issued). All dimensions are in mm.

**Purpose:** close OQ-05 by fixing the finished face that the 300 mm kitchen-side nib is measured to, and agreeing a construction tolerance.

## 1. The run in question (MEASURED from the drawing)

| Item | Dwelling A | Dwelling B (mirror) |
|---|---|---|
| Door latch jamb (finished wall end) | x 2,100 | x 16,500 |
| Base-run end nearest the door, as drawn | x 2,400: **300** from the jamb | x 16,200: 300 from the jamb |
| Other end of the run (wall face) | x 4,300 | x 14,300 |
| Run length available | **1,900** | 1,900 |
| Depth | 600 | 600 |
| Units as drawn, from the door end | 300 / 600 / 600 / 400 | 300 / 600 / 600 / 400 |

**What the drawing assumes:** drawing note 2 assumes the run outline is the **finished face**, meaning the end panel or worktop edge, whichever projects further. The 300 mm therefore has **no construction margin**. If the outline is instead taken as the carcass, an 18 mm end panel reduces the nib to 282 mm.

## 2. Information requested

1. A **dimensioned setting-out drawing or elevation** of this run for both dwellings (handed), showing:
   - end panel;
   - worktop end;
   - carcass widths;
   - any filler or scribe at the wall end.
2. End panel thickness, and whether the worktop is flush with it or overhangs it (and by how much).
3. The **finished-face position** of the run end relative to the door jamb (x 2,100 / x 16,500): the dimension from the jamb to the outermost finished surface.
4. How the 1,900 mm is made up, including the end panel. Is a 300 mm-class unit available to suit, or what is proposed instead?
5. The installation tolerance you work to on run positions, and the tolerance you recommend so that **at least 300 mm** remains after installation.
6. Any appliance or service intended in the unit at the door end.

**Please confirm the finished-face position in writing** for both dwellings.

## 3. What the designer will do with the answers

- Enter the datum, panel, overhang and agreed tolerance in `gate_inputs/OQ05_OQ06_inputs_TEMPLATE.json` and run `gate_calc.mjs`.
- If the required finished-face position differs from the drawing, revise the **scratch** copy only, then rerun the dimension, collision, symmetry and regression checks (`evidence/scripts/rerun_validation.sh`).
- Sign off the agreed nib dimension and tolerance for both dwellings.
