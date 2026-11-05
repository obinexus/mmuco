# RFI source verification and draft-quality audit (Audits A and C)

**Scope:** `RFI_01A_ECLISSE_…`, `RFI_01B_JB_Kind_…`, `RFI_01C_Scrigno_…`, all **DRAFT — NOT SENT**. Audit date: 24 Oct 2026.

**Revision 6 (24 Oct 2026):** findings F-ALL1, F-A1, F-A2, F-B1, F-C1, F-C2 and F-ALL2 were applied to the three drafts, with the finalisation instructions. Every changed claim was re-checked against its source (section 0). Sections 1–4 are the revision-5 audit record.

**Constraints observed:**

- Nothing was sent and no manufacturer was contacted. The sources were only read.
- Revision 5 did not edit the RFIs. Revision 6 edited them only as listed in section 0, and all three remain **DRAFT — NOT SENT**.
- The proposed drawing is unchanged.
- OQ-05, OQ-06 and OQ-07 remain OPEN.

## 0. Revision 6: findings applied and changed claims re-checked

**Hashes:**

| RFI | Before revision 6 | After revision 6 | "DRAFT — NOT SENT" labels |
|---|---|---|---|
| 01A | `107f5a77…` | `17680be6…` | 2 |
| 01B | `b1862cb5…` | `f1bccac8…` | 2 |
| 01C | `3292f318…` | `16b09a7e…` | 2 |

**How the sources were re-checked (24 Oct 2026, revision 6):**

- **S-02:** the local copy's SHA-256 (`6a37cd93…`) is unchanged; the page-1 render was re-read.
- **S-01, S-06, S-07:** re-loaded in the built-in browser; the quoted strings were matched against the page text and the S-01 table cells.

| Item | RFI | Text now in the draft | Source entry re-checked | Verdict |
|---|---|---|---|---|
| F-ALL1 | all three | Appendix A "Pocket end": "Intended to abut the inner face of the external wall…; to be confirmed with your detail (question 8)" in 01A, "(question 7)" in 01B and 01C | Design ASSUMPTION (S-09; the calculator's kit branch). Each RFI asks the manufacturer for the detail | **APPLIED**: now stated as an intention plus a question |
| F-A1 | 01A | Appendix C: "UK-26 (PDF metadata date 2026-08-06; no revision printed)" | S-02 PDF Info CreationDate `D:20260806…`; no revision printed on the sheet | **APPLIED**; VERIFIED as metadata |
| F-A2 | 01A | Appendix C linings: "UNKNOWN: see the 25 mm annotations (meaning unconfirmed)" | S-02 plan: "25" either side of PW, with no definition | **APPLIED**: no guessed value remains |
| Finalisation | 01A | Body: the second row "PW 900 × PH 1971, W 1894 × H 2056, door 3ft. 0in. × 6ft. 6in. (914 × 1981 mm)", and "Our enquiry is about the PW 900 × PH 2030 row only". Q1 asks for the PH 2030 code and confirmation that it differs from the PH 1971 code | S-02 table row "900 x 1971 / 1894 x 2056 / 95 - 100 -115 - 125 / 3ft. 0in. x 6ft. 6in. (914 x 1981 mm)"; row "900 x 2030 / 1894 x 2115 / … / 926 / 2040" | **APPLIED**; VERIFIED (MFR) |
| Finalisation | 01A | Questions on the undefined annotations kept: Q2 (22, 5, 12.5, and whether they add to the stud opening); Q3 (25) | S-02 elevation and plan annotations | **RETAINED**; meanings still UNRESOLVED in the source |
| F-B1 | 01B | Body, Q3 and Appendix C use the exact headings "Clear Opening Size (walkthrough area)" and "Structural Opening Size of the Unit", with sub-labels Width (OW), Height (OH), Width (SW), Height (SH) | S-01 table header: "Clear Opening Size (walkthrough area) / Structural Opening Size of the Unit"; sub-labels "Width (OW) / Height (OH) / Width (SW) / Height (SH)" (OW and OH have a line break before the bracket). Row "POCSYSSGL915 / 915 / 1981 / 890 / 1970 / 1925 / 2075 / 125" | **APPLIED**; VERIFIED (MFR, undated) |
| F-C1 | 01C | "A UK retailer lists two versions of a Scrigno "926 × 2040" single system: a standard one and a fire-rated one … neither listing names the Scrigno product line" | S-06 and S-07 are both Door Superstore pages. S-07 is titled "Scrigno Single Fire Rated Pocket Door Sliding System (726mm x 2040mm)", with a 926 option and FD30 certification | **APPLIED**; VERIFIED (RET) |
| F-C2 | 01C | Q3(b) and Appendix C: walk-through "896 × 1,900–2,400" | S-07: "Walk Through Area: (W) 896mm* x (H) 1900mm to 2400mm" | **APPLIED**; VERIFIED (RET) |
| Finalisation | 01C | The listings are kept separate: Q3 (a) and (b); separate Appendix C rows for structural opening and walk-through; Q3 asks which product line and code **each** corresponds to, and whether 896 is net of the 10 mm | S-06: "Structural Opening Size: (W) 1910mm x (H) 2140mm", "Walk Through Area: (W) 900mm x (H) 2030mm", "Cassette Width: 900mm", "Finished Wall Thickness: 125mm", "Once fitted this reduces the clear opening by 50mm". S-07: "Structural Opening Size: (W) 1930mm x (H) 2005mm to 2505mm", "The effective clear opening size is reduced in width by 10mm", "Finished Wall Thickness: 125mm" | **APPLIED**; VERIFIED (RET); not merged |
| F-ALL2 | 01B, 01C | Appendix C names `doorSystem.datasheetDateOrRevision` and `doorSystem.installationDrawingRef` | Both keys exist in the adopted and proposed templates | **APPLIED** |

**Searches repeated:** "1896" and "1,896" are still absent from S-06 and S-07.

**Not changed in the drafts:** recipients, Appendix A project data, the designer's notes, and the Appendix C "Our calculator field" column. That column still names the adopted calculator's fields; see `RFI_CALCULATOR_MAPPING_GAPS.md` section 2.

**Verdict classes:**

| Class | Meaning |
|---|---|
| VERIFIED (MFR) | Matches an official manufacturer source |
| VERIFIED (RET) | Matches a retailer source; not manufacturer evidence |
| PROJECT DATA | From the measured scratch geometry, not a manufacturer fact |
| DERIVED | Our calculation from the above, flagged as a question in the RFI |
| INTERPRETATION | Our reading, not stated by the source |
| UNRESOLVED | The source does not answer it; the RFI asks |
| UNSUPPORTED | Stated without support |

## 1. Sources re-checked during this audit

| ID | Source | Revision / date | Page | How re-checked on 24 Oct 2026 |
|---|---|---|---|---|
| S-02 | ECLISSE `ECL-Classic-Single-UK-26.pdf` (official) | PDF Info: Title `ECL_Schede_web_UK_26_NEW.indd`, CreationDate `D:20260806142525+02'00'`, ModDate `D:20260806143651+02'00'`. **No revision or date printed on the sheet** | 1 of 1 (Windows PDF renderer page count = 1) | Temporary copy SHA-256 6A37CD93… unchanged; page re-rendered at 4,500 px and annotations read |
| S-03 | eclisse.co.uk `pages/technical` and `pages/technical-specs` (official) | none | web pages | Link labels and target file names (read earlier in this session) |
| S-01 | JB Kind single and double pocket door systems page (official) | none shown (footer "© 2026 JB Kind Doors") | web page, single size-guide table | Re-fetched |
| S-04 | Scrigno FAQ, Base counter frames on plasterboard walls (official) | 30 August 2024 | web page | Read earlier in this session |
| S-06 | Door Superstore, "Scrigno Single Pocket Door Sliding System 926mm x 2040mm" (**retailer**) | none | web page | Re-fetched |
| S-07 | Door Superstore, "Scrigno Single Fire Rated Pocket Door Sliding System (726mm x 2040mm)", Metric 926 option (**retailer**) | none | web page | Re-fetched |

## 2. Audit A: claim-by-claim verification

### RFI_01A, ECLISSE Classic Single PW 900

| # | Claim in the RFI | Source and exact supporting entry | Verdict |
|---|---|---|---|
| A1 | Recipient: ECLISSE UK Ltd, Richmond House, Occupation Lane, Gonerby Moor, Grantham, Lincs NG32 2BP; Tel 0333 577 0828; enquiries@eclisse.co.uk | S-02 p.1 footer: "ECLISSE UK Ltd • Richmond House - Occupation Lane - Gonerby Moor - Grantham - Lincs NG32 2BP / Tel 0333 577 0828 • enquiries@eclisse.co.uk • eclisse.co.uk" | VERIFIED (MFR) |
| A2 | Product "CLASSIC SINGLE" pocket door system | S-02 p.1 header: "ECLISSE CLASSIC SINGLE / SINGLE POCKET DOOR SYSTEM" | VERIFIED (MFR) |
| A3 | Row PW 900 × PH 2030; W 1894 × H 2115; door panel 926 × 2040; FW 95–100–115–125 | S-02 p.1 table "FRAMES FOR SINGLE DOORS", row: "900 x 2030 / 1894 x 2115 / 95 - 100 -115 - 125 / 926 / 2040" | VERIFIED (MFR). **Note:** a second row "900 x 1971 / 1894 x 2056 / … / 3ft. 0in. x 6ft. 6in. (914 x 1981 mm)" has the same PW and W. The RFI correctly identifies the row by PH 2030 and the 926 × 2040 door |
| A4 | 3–5 mm stud tolerance | S-02 p.1 "PLEASE NOTE" box: "ECLISSE advise you build a 3-5mm tolerance into your stud dimensions for both width and height" | VERIFIED (MFR) |
| A5 | Technical page lists CLASSIC assembly instructions for 70/90 and 75/100 profiles | S-03 link labels "70/90" → `0476_Classic_Frame_Assembly_Instructions_70-90_profile.pdf`; "75/100" → `0461_Classic_Frame_Assembly_Instructions_75-100_profile.pdf` | VERIFIED (MFR) by link label and file name. The documents themselves were **not opened** |
| A6 | 22 mm and 5 mm "at the ends of W on the elevation"; 12.5 mm "on the plan"; 25 mm "either side of PW on the plan" | S-02 p.1 drawings: "22" and "5" at the ends of W (elevation and plan); "12,5" on the plan beside the board layer; "25" either side of PW on the plan | Annotations VERIFIED as present. **Meaning UNRESOLVED:** no text on the sheet defines them. INTERPRETATION only: in the elevation, 22 (latch end) and 5 (pocket end) appear to lie within W, 12,5 appears to be the board layer, and 25 appears to be the jamb/lining zones. The RFI correctly asks rather than asserts |
| A7 | Stop regulated for flush pulls; PUSH&PULL; BIAS; BIAS DS; self-closing mechanism | S-02 p.1 NOTES: "When fitting flush pull handles we recommend the stop be regulated so the door protudes [sic] from the pocket to avoid risk to fingers." ACCESSORIES: "ECLISSE BIAS - Soft close…", "ECLISSE BIAS DS - Bi-directional soft close…", "ECLISSE PUSH&PULL - Touch latch system…", "Self-Closing Mechanism…" | VERIFIED (MFR) |
| A8 | Timber lining kit | S-02 p.1 NOTES: "Includes complete timber lining kit for a professional finish." | VERIFIED (MFR) |
| A9 | Leaf 926 × 2040, 35–44 mm thick | S-02 p.1 table DW 926 DH 2040; NOTES: "Suitable for use with 35-44mm thick doors." Also: "Doors, plasterboard and final architrave not supplied." | VERIFIED (MFR) |
| A10 | CLASSIC WIRING-READY frame exists | S-03 Technical Specs: "CLASSIC Pocket Door System WIRING-READY Single" | VERIFIED (MFR) as a product. Its availability **in this size** is not verified (the RFI asks) |
| A11 | PW 850 × 2020, W 1,844 × H 2,105 | S-02 p.1 row "850 x 2020 / 1844 x 2105 / 95 - 100 -115 - 125 / 2ft. 10in. x 6ft. 8in. (864 x 2032 mm)" | VERIFIED (MFR) |
| A12 | Appendix C: "UK-26 (file created 2026-08-06)" | S-02 PDF Info CreationDate 2026-08-06; "UK-26" from the file name | VERIFIED as **file metadata**, not a printed revision. Wording should say so (finding F-A1) |
| A13 | Appendix C: stud opening 1,897–1,899 (W + 3–5)?; height 2,118–2,120? | Arithmetic on A3 + A4 | DERIVED, correctly flagged with "?" |
| A14 | Appendix C: linings "UNKNOWN (25?)" | Reading of the A6 annotation | INTERPRETATION shown as a guess (finding F-A2) |
| A15 | Appendix A: wall run 1,800; extendable to about 2,200; latch ≥ 300 from return wall | S-09 measured geometry (x 300 → 2,100; return wall x 2,800) | PROJECT DATA (labelled "from our current design drawing") |
| A16 | Appendix A: "Pocket end abuts the inner face of the external wall" | Calculator ASSUMPTION; frame position not designed | Stated as fact; it is a design assumption (finding F-ALL1) |
| A17 | Designer's note: latch move about 97–99 mm | CALC (`gate_calc_candidates.json`) | DERIVED; internal note, marked for deletion |

### RFI_01B, JB Kind POCSYSSGL915

| # | Claim | Source and exact supporting entry | Verdict |
|---|---|---|---|
| B1 | Recipient: placeholder, contact route to be confirmed | S-01 shows only a general number, "Tel: 01283 554197", not labelled technical | Not fabricated. The designer may use the verified general number |
| B2 | Code POCSYSSGL915; door 915 × 1981; OW 890, OH 1970; SW 1925, SH 2075; FW 125 | S-01 single size-guide row: "POCSYSSGL915 \| 915 \| 1981 \| 890 \| 1970 \| 1925 \| 2075 \| 125" | VERIFIED (MFR, undated) |
| B3 | Labels "Clear Opening Width (OW)…", "Structural Opening Width (SW)…" | S-01 headings: "Clear Opening Size (walkthrough area)" with sub-labels "Width (OW)", "Height (OH)"; **"Structural Opening Size of the Unit"** with "Width (SW)", "Height (SH)" | VERIFIED in substance. The RFI paraphrases the structural-opening heading; the exact heading matters, because SW is an **opening for the unit** (finding F-B1) |
| B4 | "Clear Opening Size (walkthrough area)" quoted in Q2 | S-01 heading, verbatim; no definition on the page | VERIFIED (MFR); definition UNRESOLVED |
| B5 | Timber accessory kit | S-01: "confirm which timber accessory kit you would like" | VERIFIED (MFR) |
| B6 | 125 only | S-01: every single and double row lists 125 | VERIFIED (MFR) |
| B7 | Datasheet / installation drawing: none found | S-01: no technical document linked; no page date | VERIFIED as an absence |
| B8 | Appendix A project data; pocket-end statement | S-09; calculator assumption | PROJECT DATA; F-ALL1 applies |

### RFI_01C, Scrigno (to the manufacturer)

| # | Claim | Source and exact supporting entry | Verdict |
|---|---|---|---|
| C1 | Recipient: placeholder | none | Not fabricated |
| C2 | FAQ (30 Aug 2024): Base plasterboard frames for 100 and 125 mm finished walls, on 75 and 100 mm profiles | S-04: "Scrigno counter frames in the plasterboard version with finished wall thicknesses of 100mm, 125mm are suitable for interior partition walls formed by structures with 75 and 100mm profiles, respectively" | VERIFIED (MFR) |
| C3 | Set (a): structural opening 1,910 × 2,140; walk-through 900 × 2,030; cassette 900; FW 125 | S-06: "Structural Opening Size: (W) 1910mm x (H) 2140mm"; "Walk Through Area: (W) 900mm x (H) 2030mm"; "Cassette Width: 900mm"; "Finished Wall Thickness: 125mm" (listed after the metric systems) | VERIFIED (RET) |
| C4 | Set (b), fire-rated: 1,930 × 2,005–2,505; walk-through 896; "reduced in width by 10mm"; FW 125 | S-07, under "Metric 926mm x 2040mm System": "Structural Opening Size: (W) 1930mm x (H) 2005mm to 2505mm"; "Walk Through Area: (W) 896mm* x (H) 1900mm to 2400mm"; "*The effective clear opening size is reduced in width by 10mm"; "Finished Wall Thickness: 125mm"; "certified for use with 30 minute fire doors (FD30 rating)" | VERIFIED (RET). The RFI omits the 1,900–2,400 walk-through height (finding F-C2) |
| C5 | Self-closer reduces clear opening by 50 mm | S-06: "Once fitted this reduces the clear opening by 50mm" | VERIFIED (RET) |
| C6 | Email body: "UK **retailers** list…" | Both listings come from **one** retailer (Door Superstore) | UNSUPPORTED plural (finding F-C1) |
| C7 | Appendix A project data; pocket-end statement | S-09; calculator assumption | PROJECT DATA; F-ALL1 applies |

### The conflicting Scrigno figure sets

- **What the sources actually contain:**
  - **Standard listing (S-06):** 926 × 2,040; structural 1,910 × 2,140; walk-through 900 × 2,030; cassette 900; internal frame 70; FW 125; no fire rating stated.
  - **Fire-rated listing (S-07):** 926 × 2,040 option; structural 1,930 × 2,005–2,505; walk-through 896 × 1,900–2,400, "reduced in width by 10mm"; cassette 900; internal frame 69; FW 125; FD30 certified.
- **The figure "1,896" does not appear in either source.** Searches of both pages found no 1896 or 1,896. The audit brief's "926 / 900 / 1,896" set has no source; the closest source sets are 926 / 900 / **1,910** and 926 / 896 / **1,930**. Not reconciled.
- **Different product lines?** The evidence shows **two different retailer products**:
  - different titles, one "Fire Rated" with FD30 certification;
  - different structural widths (+20 mm);
  - different height regimes (fixed 2,140 vs adjustable 2,005–2,505);
  - different internal frame thickness (70 vs 69).
- **What remains unresolved:**
  - Neither listing names a Scrigno product line.
  - Scrigno's official download area lists fire-rated sliding documents ("Sliding Fire Solution Door Closer Instructions", "EI30 DOOR INSTALLATION", "Istruzioni telaio soluzione tagliafuoco scorrevole"). These are consistent with a separate fire-rated product family, but **nothing links either listing to a specific Scrigno line**.
  - The 10 mm reduction may already be applied in the 896 figure. That cannot be confirmed.
- **Status:** UNRESOLVED. RFI_01C Q3 correctly asks the manufacturer.

## 3. Audit C: draft quality

| Check | RFI_01A | RFI_01B | RFI_01C |
|---|---|---|---|
| Precise model and requested configuration | PASS: PW 900 × PH 2030, W 1894 × 2115, door 926 × 2040, FW 100, 2 frames handed | PASS: POCSYSSGL915 (915 × 1981); asks for a 100 mm version | PASS **as framed**: no model can be named from official sources, so the RFI asks Scrigno to identify one (the model itself is BLOCKED until answered) |
| Separates clear passage from structural opening and cassette | PASS: PW vs W vs stud opening kept apart | PASS: OW vs SW kept apart (but see F-B1) | PASS: walk-through vs structural opening vs cassette kept apart |
| Requests dated technical drawing | PASS (Q13) | PASS (Q11) | PASS (Q11) |
| Requests explicit confirmation of unresolved dimensions | PASS: Q2–Q4, Appendix C, written confirmation | PASS: Q2–Q5, Appendix C | PASS: Q2–Q5, Appendix C |
| No placeholder geometry presented as manufacturer fact | PASS with F-A2: "(25?)" is a guess in the "our reading" column, flagged with "?" | PASS | PASS |
| No unsupported claims; no fabricated contacts | PASS with F-A1 and F-ALL1. Contact verified | PASS with F-ALL1. Placeholder contact | **Minor finding F-C1** (plural "retailers"); F-ALL1. Placeholder contact |
| Send-ready apart from sender / contact placeholders and the designer's note | PASS | PASS | PASS |
| Labelled DRAFT — NOT SENT | PASS (2 occurrences) | PASS (2) | PASS (2) |

### Findings (revision 5) and their status

| ID | RFI | Finding | Recommended edit | Status |
|---|---|---|---|---|
| F-ALL1 | All three | Appendix A states "Pocket end: Abuts the inner face of the external wall" as fact. It is a design **assumption**, also built into the calculator | "Intended to abut … (to be confirmed with your detail)" | **APPLIED** in revision 6 (section 0) |
| F-A1 | 01A | "UK-26 (file created 2026-08-06)" comes from PDF metadata, not a printed revision | "UK-26 (PDF metadata date 2026-08-06; no revision printed)" | **APPLIED** |
| F-A2 | 01A | "UNKNOWN (25?)" guesses the lining from an undefined annotation | "UNKNOWN: see the 25 mm annotations (meaning unconfirmed)" | **APPLIED** |
| F-B1 | 01B | Paraphrases "Structural Opening Size of the Unit" as "Structural Opening Width (SW)" | Quote the exact heading so that SW is understood as the opening for the unit | **APPLIED** |
| F-C1 | 01C | "UK retailers list…" (one retailer, two listings) | "A UK retailer lists two versions…" | **APPLIED** |
| F-C2 | 01C | Set (b) omits the walk-through height 1,900–2,400 | Add it | **APPLIED** |
| F-ALL2 | 01B, 01C | Appendix C names `doorSystem.*` (wildcard) | Name `doorSystem.datasheetDateOrRevision` and `doorSystem.installationDrawingRef` | **APPLIED** |

## 4. Unsupported dimensions

- **No manufacturer or retailer dimension in any RFI is unsupported:**
  - every quoted product figure matches its cited source (section 2);
  - the Scrigno figures are correctly attributed to a retailer.
- **Non-source numbers, all labelled as ours:**
  - DERIVED with "?": 1,897–1,899 and 2,118–2,120 (01A Appendix C).
  - PROJECT DATA: 1,800, about 2,200 and the 300 mm return clearance (Appendix A of all three).
  - DERIVED in the internal designer's notes, marked for deletion: 97–99, 125 and 110–130 mm.
- **One INTERPRETATION shown as a guess:** "25?" (F-A2). Removed in revision 6.
- **The audit brief's "1,896 mm" figure is unsupported by any source.** No RFI uses it.

## 5. Results (revision 6)

| RFI | Audit A: source verification | Audit C: draft quality | Overall |
|---|---|---|---|
| RFI_01A ECLISSE | **PASS**: all product figures, both PW 900 rows, contact and accessory claims verified against the official datasheet (p.1) and website. Annotation meanings UNRESOLVED in the source and asked explicitly | **PASS**: F-A1, F-A2 and F-ALL1 applied | **PASS**; DRAFT — NOT SENT, awaiting review and authorisation |
| RFI_01B JB Kind | **PASS**: code, all seven figures and the exact headings verified against the official page (undated; no datasheet exists online) | **PASS**: F-B1, F-ALL1 and F-ALL2 applied | **PASS**; DRAFT — NOT SENT, awaiting review and authorisation |
| RFI_01C Scrigno | **BLOCKED** at manufacturer level: product dimensions exist only in two retailer listings, accurately attributed and kept separate. The official source verifies only the wall-thickness FAQ. The conflict is unresolved | **PASS**: F-C1, F-C2, F-ALL1 and F-ALL2 applied | **BLOCKED** for verification; the draft is fit to send to obtain the evidence; DRAFT — NOT SENT |
| Calculator mapping (Audit B) | — | — | **Adopted calculator: INCOMPLETE** (0 of 91 validated). **Proposed calculator (not adopted): complete**; the code, schema and 64 passing tests agree. See `RFI_CALCULATOR_MAPPING_GAPS.md` |

**Not verified in this audit:**

- the ECLISSE 70/90 and 75/100 assembly-instruction PDFs (only their links and file names);
- the WIRING-READY datasheet;
- Scrigno's 24.9 MB technical file;
- any manufacturer confirmation for this project (none exists).
