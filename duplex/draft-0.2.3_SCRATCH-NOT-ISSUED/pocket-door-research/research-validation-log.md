# Research and validation log: pocket-door research phase (24 Oct 2026)

Scope: research only. No drawing change, no product selection, no third-party contact, no OQ closed.

## 1. Starting state (21:55:59): `evidence/10_research/00_start_state.txt`

| Check | Result |
|---|---|
| Frozen manifests: Draft 0.2.2 (80), 0.2.1 (63), Verification (40), earlier documents (5), VF-07 investigation (49), Draft 0.1 record (3) | **240 / 240 OK**. Manifest-file hashes as recorded (0.2.2 d9062c5a…, 0.2.1 3fb2898a…, Verification 1d48e6e3…, earlier documents 35be2479…, VF-07 1508eb2b…) |
| Scratch manifest (revision 2, sha256 bdc7316a…) | **124 / 124 OK** |
| Proposed DXF / PDF / PNG | f8b0c4dd… / 4db5d27e… / 0e01d55c…: **identical** to the revision-1 record |
| Draft 0.2.3 files outside the scratch directory | **0** |

Files read before any change:

- README, the earlier issue-gate record, the open-question register, RFI-01 and RFI-02;
- `gate_calc.mjs` (re-read in full before running), the input template, and `rerun_validation.sh`.

## 2. Sources: what was tried and what happened

| # | Action | Outcome |
|---|---|---|
| 1 | WebFetch, JB Kind product page | Read. Size table extracted (S-01) |
| 2 | WebFetch, ECLISSE technical page | **HTTP 429** (rate limit), twice |
| 3 | Built-in browser, ECLISSE technical and Technical Specs pages | Read; datasheet links found (S-03) |
| 4 | WebFetch, ECLISSE `ECL-Classic-Single-UK-26.pdf` | No text layer extracted. The tool saved a temporary copy in the session folder (SHA-256 6A37CD93…). Page 1 was rendered to an image (Windows PDF renderer) and read (S-02). Pages 2–4 do not exist: the renderer reported an invalid page index |
| 5 | WebSearch, Scrigno 926 / 1,930 | Search summary only; **not used as evidence** (S-08) |
| 6 | WebFetch, Scrigno datasheet URL from the search | **HTTP 404** |
| 7 | Built-in browser, scrigno.com | Redirected to the official FAQ on 100 / 125 mm finished walls (S-04, dated 30 Aug 2024) |
| 8 | Built-in browser, Scrigno download area; WebFetch, Pocket Door Systems brochure 2024 | Brochure rendered (11 pages) and inspected: **no size tables** (S-05). The 24.9 MB technical file was **not reviewed** |
| 9 | WebFetch, two Door Superstore Scrigno listings | Read. Figures **conflict**: 1,910 / 900 vs 1,930 / 896 (S-06, S-07) |
| 10 | One Bash command (writing the source register) | **Refused by the Claude Code safety check**, because it ended with a stray removal of a root-level file `/tmp_src_reg.mjs`. Nothing in that command ran. The register was written by a script in the scratchpad instead. An end check confirms no such file exists |

**Third-party documents:** none was saved into the project. The two PDFs exist only as temporary tool copies in the session folder; their hashes are in the source register. Rendered page images stay in the session scratchpad.

## 3. Calculator inspection, extension and regression

**Inspection:**

- The original model treats `structuralOpening_mm` as the **drawn passage gap**, with leaf, pocket and end-allowance inputs.
- Manufacturers publish an overall frame or stud-opening width covering pocket **and** passage. Entering that as `structuralOpening_mm` would be wrong: it is the cassette = opening confusion.

**Extension:**

- An optional `kit` block was added, covering frame width, stud tolerance, stated passage, installed reduction, wall options and heights.
- It computes the frame run from the external wall face, the latch-jamb move, the pocket zone, the base-run outline at latch + 300 + tolerance (+ carcass offset), the base-run length, the utility-side nib, and kitchen-approach clearance. It runs for both dwellings.
- **ASSUMPTION:** the frame's pocket end sits at the external wall face.

**Regression:** the existing template and placeholder inputs were re-run after the extension. Outputs are **byte-identical** to `evidence/08_gate_calculator/` (`evidence/10_research/calc_regression/`).

**Runs:**

- **Blank new template:** every result is UNKNOWN or null (`gate_calc_NEW_TEMPLATE_blank.json`).
- **Research inputs (6 configurations):** `gate_calc_candidates.json`. Dwellings A and B give identical results by mirror; the calculator printed no "dwellings differ" note.

## 4. Results recorded (detail in `POCKET_DOOR_CANDIDATE_COMPARISON.md`)

- **No candidate stating ≥ 850 mm fits the current 950 mm pocket zone or 1,800 mm wall run.** The latch jamb would move 97–130 mm (ECL-850: 47–49 mm, but with 0 mm margin on a maximum passage).
- **Installed clear width:** UNKNOWN for every candidate.
- **Finished wall:** only ECLISSE publishes a 100 mm option.
- **Not checked:** head height, because the ceiling height is unknown.

## 5. Checks not run, and why

- **CAD validation of candidate geometries:** not run, because no geometry change was authorised. The proposed drawing was **not** altered.
- **PDF / PNG regeneration:** not needed, since there was no drawing change.
- **Planted-fault controls:** not re-run, since no checking code that touches the DXF changed. The calculator change was regression-tested instead.
- **ADM applicability:** not assessed (OQ-01 / OQ-02).

## 6. End state (22:05:47): `evidence/10_research/99_end_state.txt`

| Check | Result |
|---|---|
| Frozen manifests | **240 / 240 OK** |
| Proposed DXF / PDF / PNG | **Identical** to revision 1 |
| Draft 0.2.3 files outside the scratch directory | **0** |
| Stray root file | **None** |
| Source copy of the 0.2.2 DXF | Identical to the issued file |
| Scratch manifest | Regenerated **after** this log was written, so that it covers this log; its verification is reported in the session summary |
