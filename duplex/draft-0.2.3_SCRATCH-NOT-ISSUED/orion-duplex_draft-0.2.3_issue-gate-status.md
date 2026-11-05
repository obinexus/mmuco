# Proposed Draft 0.2.3: issue-gate status (DRAFT, research phase)

**As at 24 Oct 2026, after the pocket-door research: gate NOT passed. Draft 0.2.3 must not be issued. No drawing is approved.**

**Revision 6 (24 Oct 2026):** the enquiry drafts were finalised and a calculator fix was proposed. **No gate status changed:** OQ-05, OQ-06 and OQ-07 remain OPEN.

This updates `MMUCO_ORION_Duplex_Draft_0.2.3_PROPOSED_Issue_Gate_SCRATCH.md` with the research results. No status is changed: published product data is not evidence for this project's exact configuration.

## OQ-06: pocket-door system

| Field | Entry |
|---|---|
| Status | **OPEN** |
| Owner | Designer selects; manufacturer confirms |
| Evidence received | Published data for candidates, not selections (`POCKET_DOOR_CANDIDATE_COMPARISON.md`): ECLISSE Classic Single official datasheet (UK-26); JB Kind official size guide (undated); Scrigno retailer listings (conflicting) and the Scrigno official 100 / 125 mm FAQ |
| Missing evidence | Designer's choice of one product and configuration; the manufacturer's dated datasheet and installation drawing **for that configuration**; written answers to the enquiries (**DRAFT — NOT SENT**); designer sign-off |
| Enquiries (24 Oct 2026) | Order instructed: **ECLISSE Classic Single PW 900 first**, all three pursued. Send-ready drafts: `RFI_01A_ECLISSE_…`, `RFI_01B_JB_Kind_…`, `RFI_01C_Scrigno_…`. **None sent.** Pursuing a candidate is not a selection |
| Acceptance criteria | Named manufacturer, product and model. Dated documents. Stud opening, linings, stops and hardware confirmed in writing. Compatible with the agreed finished wall thickness |
| Dependencies | Wall thickness decision (100 mm PROVISIONAL; JB Kind publishes 125 only); head height (UNKNOWN); fire strategy (fire rating not specified) |
| Closure authority | Responsible designer, on manufacturer confirmation |

## OQ-07: clear opening

| Field | Entry |
|---|---|
| Status | **OPEN** (depends on OQ-06) |
| Owner | Designer (written assessment); building control for the regulatory reading |
| Evidence received | Published **maximum / walkthrough** widths only: ECLISSE 900 maximum, JB Kind 890, Scrigno 900 / 896 (retailer). The installed clear width is **UNKNOWN** for every candidate. The current drawn 850 mm gap remains an ESTIMATE of 770–810, so **the 850 mm target is not demonstrated** |
| Missing evidence | Installed clear width for the selected configuration (stop, pull, closer); the designer's written assessment against the 850 mm target and the applicable Approved Document M provisions (category still open, OQ-01 / OQ-02) |
| Acceptance criteria | Installed clear width ≥ 850 mm confirmed by the manufacturer for the specified configuration, **or** a documented designer decision resolving the shortfall before issue |
| Dependencies | OQ-06. Geometry: every candidate stating ≥ 850 needs the latch jamb moved 97–130 mm and the base run cut to about 1,770–1,803 mm (CALC). That change needs separate authorisation and a new scratch revision |
| Closure authority | Responsible designer (and building control where the regulation applies) |

## OQ-05: kitchen finished-face nib

| Field | Entry |
|---|---|
| Status | **OPEN** |
| Owner | Designer and kitchen supplier |
| Evidence received | None from the supplier. Drawn nib 300 mm (MEASURED) with 0 mm margin. Carcass reading with an 18 mm panel gives 282 |
| Missing evidence | Supplier's dimensioned elevation or setting-out drawing; written confirmation of the finished-face datum and installed position for both dwellings (`RFI_02_KITCHEN_SUPPLIER_DRAFT.md`, **DRAFT — NOT SENT**); designer-signed nib and tolerance |
| Acceptance criteria | Installed finished face ≥ 300 mm + agreed tolerance from the latch jamb, in both dwellings, **measured from the final latch-jamb position** |
| Dependencies | **OQ-06**: if the latch jamb moves, the base run moves with it, so OQ-05 cannot close before the door frame is fixed |
| Closure authority | Responsible designer, on supplier confirmation |

## Gate summary

| Gate | Status |
|---|---|
| OQ-06 door system specified and documented | **OPEN** |
| OQ-07 installed clear opening assessed and accepted | **OPEN** |
| OQ-05 finished-face datum and tolerance agreed | **OPEN** |
| CAD validation | **PASS for the current proposed scratch geometry only** (Validation Report V-01 to V-21). Not run for any candidate geometry, because no geometry change has been authorised. Must be re-run on any new scratch revision |
| Approval | **NOT GIVEN** |

## Decision path

1. **Done (24 Oct 2026):** enquiry order set: ECLISSE Classic Single PW 900 first, then JB Kind, then Scrigno via the manufacturer. Send-ready drafts are prepared.
2. The designer reviews, completes and sends `RFI_01A`, `RFI_01B`, `RFI_01C` and `RFI_02_KITCHEN_SUPPLIER_DRAFT.md`. **Not yet sent.** Revision 6 (24 Oct 2026) applied the audit findings to RFI_01A, RFI_01B and RFI_01C, which are finalised for review and still **DRAFT — NOT SENT**.
3. **The calculator must not be used for decisions until its fixes are reviewed.** The adopted `gate_calc.mjs` has demonstrated defects: contradictory results (G3) and no input validation (G6). A fail-closed replacement and its tests are in `CALCULATOR_PROPOSAL_NOT_ADOPTED/` (64 of 64 tests pass), awaiting review and authorisation. When the answers arrive and a calculator is adopted, enter them in its template and run it. Use `RFI_CALCULATOR_FIELD_DISPOSITIONS.csv` to place each answer.
4. If the chosen frame needs the latch jamb or wall thickness to change, the designer authorises a new scratch revision.
5. Create it under a new name and re-validate it in full (`evidence/scripts/rerun_validation.sh`, plus the PDF/PNG and positive controls).
6. Close OQ-06, OQ-07 and OQ-05 with signed evidence.
7. The designer authorises the issue, and a new issue manifest is created and verified.
