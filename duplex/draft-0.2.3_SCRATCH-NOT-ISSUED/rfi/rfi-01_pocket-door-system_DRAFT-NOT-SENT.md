# RFI-01: pocket-door system, kitchen-to-utility door (DRAFT, NOT SENT)

**Prepared for:** the responsible designer, to send to a pocket-door manufacturer or supplier of their choice.

**Project:** MMUCO ORION Duplex, two mirrored single-storey dwellings.

**Drawing basis:** proposed Draft 0.2.3, a scratch review copy (not issued). All dimensions are in mm, measured from that drawing.

**Purpose:** close OQ-06 (system selection and data) and allow OQ-07 (clear-opening assessment). Nothing in this request selects a product.

## 1. Where the door goes (MEASURED from the drawing; dwelling B is the mirror image)

| Item | Dwelling A | Dwelling B |
|---|---|---|
| Partition | 100 mm finished thickness, stud build-up PROVISIONAL | same |
| Wall run available for the frame, from the external wall face to the latch jamb | x 300 → x 2,100 = **1,800** | x 18,300 → x 16,500 = 1,800 |
| Structural opening as drawn | **850** (x 1,250–2,100) | 850 (x 16,500–17,350) |
| Pocket drawn | 900 long (x 350–1,250), leaf 900; **0 mm spare** against the wall face | mirrored |
| How far east the latch jamb could move | Utility-side wall return at x 2,800; to keep ≥ 300 mm beside the latch on the utility side, the latch jamb must stay at x ≤ 2,500 | x ≥ 16,100 |
| Kitchen side of the latch jamb | Base units start 300 mm from the jamb (nib) | same |

## 2. Targets the designer will assess against (for information, not a specification)

**Project design target R-14:** internal door effective clear width **850 mm**. The project note asks for frame, handle projection, opening angle and approach space to be checked. This is a project target, not a regulation.

**Approved Document M reference values:**

- Table 1.1 / Table 2.1 clear widths: 750 mm with a head-on approach and a 900 mm corridor; otherwise 750 / 775 / 800 mm with 1,200 / 1,050 / 900 mm corridors.
- Measurement: per Diagram 1.1 / 2.2, where "Handles, other door furniture and weatherboards may be ignored when measuring clear opening width."
- Which of these applies is not yet established (planning condition OQ-01; building control OQ-02 / OQ-03). The designer will assess this.

## 3. Information requested

Please give answers for **(a)** a system that fits the current 850 mm structural opening, and **(b)** the smallest configuration that gives **≥ 850 mm clear**.

1. Manufacturer, product name, model / kit reference, and frame type (single pocket, finished wall thickness).
2. **Dated** technical datasheet and **installation drawing** (revision or date shown).
3. Overall frame length, structural opening, leaf size, and pocket length required.
4. Latch-side jamb or receiver, pocket-side jamb and lining: how far each sits inside the structural opening.
5. Door stops: position, and whether the leaf stops short of the pocket jamb when fully open (leaf stand-out).
6. Handle or pull type (flush pull, edge pull, D-handle) and how far it projects into the opening with the leaf fully open.
7. **Clear opening of the installed configuration**, measured from the latch-side jamb or stop to the leaf edge or stop with the leaf fully open, and the basis of the figure.
8. Effect of any soft-close or damper on the fully-open position.
9. Compatibility with a 100 mm finished partition: stud size, board thickness, and any minimum thickness.
10. Head detail, track length and fixing, and the ceiling or head height needed.
11. Restrictions on fixings, sockets, switches, pipes or ducts within the pocket section.
12. Operating force, and hardware options for users with limited grip.

**Please confirm the answers in writing**, referencing the datasheet and drawing revisions.

## 4. What the designer will do with the answers

- Enter the values in `gate_inputs/OQ05_OQ06_inputs_TEMPLATE.json` and run `gate_calc.mjs`.
- Record the manufacturer, model, datasheet date and the verified clear opening.
- Write the designer's assessment against the 850 mm target and the applicable Approved Document M provisions (OQ-07).
- If the selected system cannot reach 850 mm clear, resolve the conflict before any issue. Options include a wider opening, a revised target, or another door type. Placeholder runs suggest a wider opening needs a further cut to the kitchen base run.
