# Controlled build session gate report

**MMUCO ORION TRIPLEX COMPOUND — 3D MODEL PROPOSAL — NOT ISSUED** (25 Oct 2026)

> **Public, cleaned copy.** Personal and third-party material has been removed or generalised; `CLEANING_RECORD_NOT-ISSUED.md` lists every change. Paths below are the original workspace paths: `source_refs/` is now `source-copies/`, `backyard_concept_NOT_ISSUED/` is `backyard-concept_NOT-ISSUED/` and `evidence/gate_session_2026-10-25/` is `evidence/gate-session_2026-10-25/` (see the crosswalk).

**Result: Gates 1–5 passed. The session has stopped at Gate 6. No geometry has been created and no SolidCraft design has been made, opened or saved.**

- **Warning: the end-of-session protected check FAILED (exit 1)** because files changed in `mmuco/` during the session. Section 2 gives the exact discrepancy. The user has since confirmed that they made the change (the restructure to `projects/orion/duplex/`). A re-baseline needs the user's separate approval; nothing has been repaired or re-baselined.
- **Approval needed before Stage 0:** the `--allow-path` configuration change in section 7.
- **Approval needed before Stages B–D:** decisions D1–D13.
- **This report is a review document.** It is not a design, construction or compliance document. It makes no compliance claims.

Evidence for this report is in `evidence/gate_session_2026-10-25/`. That folder holds the read-only parse scripts, their output (with a positive control) and the end-of-session hash check.

---

## 1. Gate 1: SolidCraft availability. PASS

| Check | Result |
|---|---|
| Tools exposed in this session | All 18 documented tools are present, with no extras: `list_commands`, `describe_command`, `execute`, `batch`, `inspect_design`, `measure`, `body_topology`, `set_parameter`, `screenshot`, `export`, `crash_reports`, `running`, `undo`, `redo`, `new_design`, `open`, `save`, `skill_reference` |
| `running` (read-only) | `{"running": []}`: the server responds and nothing is queued |
| `list_commands` filter `dxf` | `sketch.insert_dxf` is enabled (`path` or `text`; `at`, `scale`, `tolerance`, `plane`). `sketch.export_dxf`, `sheet.export_dxf` and `file.export_view_dxf` (2D DXF of the current view) are also enabled |
| `list_commands` filter `view` | `view.apply` takes `front`, `back`, `top`, `bottom`, `left`, `right`, `iso` and `home`. Named views and `view.navigate` are present. **Orthographic projection is not confirmed:** the camera has an `fov`, and `file.export_view_dxf` mentions perspective projection. This is a Stage 0 test |
| Configuration | Local scope for `<project root>`: `C:\Program Files\SolidCraft\solidcraft-cli.exe`, args `["mcp"]`. **There is no `--allow-path`** |
| File sandbox (from `solidcraft-cli.exe mcp --help`) | Files are limited to SolidCraft's recovery folder, a per-process temp folder and the open design's folder. `--allow-path DIR` adds one folder; `--allow-any-path` lifts the limit (**not proposed**) |

No other CAD tool was substituted. The CADCraft tools are also loaded in this session but were not used.

**Side effect, disclosed:** the `--help` call started the CLI briefly. It left an empty folder, `%LOCALAPPDATA%\Temp\solidcraft-mcp-8644-236db168`, outside the project. Seven similar empty folders from earlier sessions are also there, along with this session's own server folder (`-41408-`, also empty). Nothing in the project was touched.

## 2. Gate 2: protection. PASS at the gate; the end-of-session check FAILED (`mmuco/` only)

`bash evidence/verify_protected.sh` was run twice:

| Check | Expected | At Gate 2 (exit 0) | End of session, about 01:16 (exit 1) |
|---|---|---|---|
| Frozen records (6 manifests) | 240 OK | **240 OK** | **240 OK** |
| Draft 0.2.3 scratch manifest | 166 OK | **166 OK** | **166 OK** |
| Project files outside this workspace and `mmuco/.git` | 880, identical to `before_project_files.sha256` | **880 identical** | **DIFFERENT: 881 files** (see below) |
| Status-contract proposal list | 91 OK | **91 OK** | **91 OK** |

**The exact discrepancy at the end of the session.** The full lists are in `evidence/gate_session_2026-10-25/end_of_session_mmuco_discrepancy.txt`.

**Every difference is inside `mmuco/`, the publication copy.** Nothing outside `mmuco/` differs, and no path kept its name with changed content.

- **Removed:**
  - 485 paths under `mmuco/projects/orion-duplex/`;
  - `mmuco/tools/verify-orion-duplex.sh` (`e9edb444…`).
- **Added:**
  - 486 paths under `mmuco/projects/orion/duplex/`, with renamed files (for example, `draft-0.1/orion-duplex_draft-0.1_floor-plan.dxf`);
  - `mmuco/tools/verify-orion.sh` (`900c5d16…`, new content).
- **Content matching:** every content hash from the removed project paths reappears under the new paths. So it looks like a move and rename. The exceptions are the verify script, whose content changed, and one new file, `integrity/orion-duplex_path-crosswalk_2026-10-25.tsv` (`b705a916…`).
- **Timing:** the file timestamps are 01:15–01:16. `mmuco/.git/index` changed at 01:16:11. The refs and `COMMIT_EDITMSG` are unchanged since 00:34, so no new commit is visible. No git command was run to check this further.
- **Source: CONFIRMED by the user after this report was first written.** The user restructured `mmuco/` to `projects/orion/duplex/` themselves. This session did not make the change, and neither did the session that started it.
- **The snapshot is a point-in-time record.** The restructure was still in progress at 01:16. A read-only recount at 01:19 found four further changes, all READMEs:
  - added: `mmuco/projects/orion/README.md` and `mmuco/projects/orion/triplex/README.md`;
  - rewritten: `mmuco/README.md` and `mmuco/projects/orion/duplex/README.md`.

  `mmuco/` then held 493 files, not counting `.git`. Nothing outside `mmuco/` had changed.
- **Consequence:** `verify_protected.sh` will keep failing on the `mmuco/` paths at every later stage until the user approves a re-baseline. The user will approve that separately. **No re-baseline has been done**, at the user's instruction. The frozen originals in the project root are unaffected.

- **Workspace self-check:** `sha256sum -c evidence/workspace_files.sha256` gave 12/12 OK, including all five `source_refs/` copies.
- **Issued DXF copy:** `source_refs/MMUCO_ORION_Duplex_Draft_0.2.2.dxf` (sha256 `2ec8d3f3…1d17b`) matches line 1 of the frozen `MMUCO_ORION_Duplex_Draft_0.2.2_Manifest.sha256`. The PNG copy matches line 3.
- **Files read:** no issued or frozen file was opened in SolidCraft. The only frozen files read were the Verification Register CSV and the Draft 0.2.2 manifest, both read-only with `grep`.

## 3. Source inventory summary

| Source (in `source_refs/` unless noted) | Status | Used for |
|---|---|---|
| `MMUCO_ORION_Duplex_Draft_0.2.2.dxf` | Latest issued, frozen; byte-identical copy | Housing plan geometry. Plan only: no Z, no heights, no site |
| `MMUCO_ORION_Duplex_Draft_0.2.2.png` | Issued sheet image; byte-identical copy | Visual underlay only |
| `MMUCO_ORION_Duplex_Draft_0.2_Verification_Register.csv` (project root, frozen) | Read-only | PA-01 to PA-15. PA-10 (2.5 m ceiling) is the only height |
| Otter transcript, "Orion Triplex and Garden Redesign" | Client dictation, 25 Oct 2026 | Programme and the 2:1 rule |
| `client_elevation_sketch_2026-10-25.jpg` | Client sketch, **not to scale**. It predates the 25 Oct date in its file name (see the note below the table) | D9–D13 conflicts only. Not used for geometry |
| `client_cadcraft_screenshot_2026-10-25.png` | **Not included in this public copy.** Probably a third party's quick, not-to-scale redraw of the sketch (see the note below the table) | Not design evidence |

**Provenance note (public copy):**

- **The hand sketch** predates the 25 Oct 2026 date in its file name. It is the client's own sketch and is not to scale.
- **The CADCraft image** was probably a quick, not-to-scale redraw of the sketch by a third party, not by the client. It carries no design intent and is **not included in this public copy**.
- **File metadata:** neither image carried an embedded date.
| Draft 0.2.3 | **Not issued**, scratch | Not used |

**Missing everywhere:**

- No elevations, sections, levels or roof design.
- No storey, head or floor-build-up heights.
- No site boundary, survey or true north (PA-07: north assumed).
- No foundations, drainage, structure or external-facility design.

None of these are invented in this report.

## 4. Gate 4: housing source verification

The checks were made by script on the `source_refs/` copy only. The scripts are in `evidence/gate_session_2026-10-25/scripts/`.

**Positive control: PASS.** A synthetic DXF with one Z = 2,500, one elevation, one thickness and a 228.78 m² outline was detected correctly by the same code.

| Item | Expected | Found | Result |
|---|---|---|---|
| External outline | 18,600 × 12,300 on A-WALL-EXT | 26 closed LWPOLYLINE wall piers in the building. Their union bounding box is (0, 0) → (18,600, 12,300), i.e. 228.78 m². DIMENSION entities measure 18,600 (×1) and 12,300 (×2), with no text overrides | **VERIFIED as drawn**, with the discrepancies below. PA-02 records these overall dimensions as an "ASSUMPTION (geometry VERIFIED)", because they depend on the provisional wall build-ups (PA-01) |
| Note 1 | 228.78 m² | MTEXT note 1: "Building footprint 18.60 x 12.30 m = 228.78 m2" | **MATCH** |
| Flat, 533 entities | No Z, elevation or roof data | ENTITIES: **533** (HATCH 62, LWPOLYLINE 190, LINE 104, ARC 20, CIRCLE 22, ELLIPSE 4, TEXT 83, DIMENSION 45, MTEXT 3), with 0 INSERTs. Non-zero Z (codes 30–37): **0**. Elevation (38): **0**. Thickness (39): **0**. Non-default extrusion: **0**. Block definitions: 278 entities, 0 non-zero Z. Header: `$EXTMIN`/`$EXTMAX` Z = 0, `$ELEVATION` 0, `$THICKNESS` 0, `$INSUNITS` 4 (mm) | **VERIFIED flat** |
| Roof data | None in 3D | A-ROOF holds 9 plan-only entities (rooflights and porch-roof outlines), with no heights. Note 3: "roof not designed" | **VERIFIED: no roof form** |
| Site boundary | Not shown | Note 6: "Site boundary NOT SHOWN (no survey)". None of the 13 layers has a boundary, site, level, section, elevation, topography or survey name | **VERIFIED: none** |
| 2,500 mm ceiling | Only PA-10 | Register row PA-10: "Ceiling height 2.5 m; roof form not designed"; position "Not shown"; class **ASSUMPTION**; resolved by "Roof design and sections". The only height anywhere in the DXF is note 2's living-room sill, max 850 mm | **VERIFIED as an ASSUMPTION only** |

**Discrepancies to fix before Stage A or B.** These are reported only; nothing has been changed.

1. **Legend swatches sit on the wall layers.** The legend at x 15,500–16,000, y −7,500 to −6,200 draws one closed swatch on each of these layers:
   - A-WALL-EXT (500 × 300, with its hatch);
   - A-WALL-PARTY;
   - A-WALL-INT.

   Effects:
   - The plan's "27 outlines" is in fact 26 building piers plus 1 swatch.
   - The party wall is 1 wall (x 9,200–9,400) plus 1 swatch.
   - The plan's "33 internal partitions" is 32 partitions plus 1 swatch.
   - **The A-WALL-EXT layer's extents are 18,600 × 18,800 (y −6,500 to 12,300), not 18,600 × 12,300.**

   Stage B's "extrude from their own layers" and its bounding-box check would both fail unless the legend area is excluded. Fix: filter to the building region (y ≥ 0 for the walls).
2. **There is no single outline polyline.** The external wall is 26 separate piers with gaps for openings. The 18,600 × 12,300 is their union bounding box.
3. **External openings, measured from the pier gaps.** No 1,400 mm opening exists in any external wall.
   - **Front:** glazing 1,500 and 1,200 per dwelling. Entrance 1,100 opening, single leaf (arc r = 1,010).
   - **Rear:** glazing 1,500 (×2 per dwelling). Door to the conservatory: 1,000 opening, single leaf.
   - **Gables:** glazing 1,200 (×3 per gable). A 1,000 opening from the utility to the side patio, single leaf. **The inventory (section 8) omits this gable door.**
   - **Every external door on the plan is a single leaf.**
4. **The source cited for the walkway width (D4) is stretched.** PA-06 is "Paths 1.5 m wide". It mentions the 2.0 m compound standard only as a competing figure. The parameter file's wording "PA-06 records a 2.0 m compound standard" overstates this.

## 5. Gate 3: decisions D1–D13

Classes:

- **VERIFIED:** measured from the issued DXF.
- **PROVISIONAL:** a recorded project assumption, or a stated value that is not approved.
- **UNRESOLVED:** a placeholder with no evidence, or a conflict between sources.

Every row needs explicit approval because none is approved yet. Approving a row approves it **as a labelled placeholder for the proposal model**. That does not make the value verified.

| ID | Proposed value (exact) | Source / justification | Class | Impact if wrong | Explicit approval? |
|---|---|---|---|---|---|
| **D1** Heights and roof | Walls 2,500 mm; flat roof slab 300 mm; door and window heads 2,100 mm; sills 850 mm. All labelled PLACEHOLDER | 2,500: PA-10 (ASSUMPTION; "roof form not designed"). 850: note 2, a **maximum** for the living-room principal window only. 300 and 2,100: PLACEHOLDER, with no evidence | 2,500 **PROVISIONAL**; 850 **PROVISIONAL** (one window); 300 and 2,100 **UNRESOLVED** | All four elevations, building volume, the roof-catchment concept for the well, and the rooflight and canopy relationships. Taking the walls to the 2,500 ceiling height understates the real wall height, because floor and ceiling build-ups are ignored. Elevations could be mistaken for design | **Yes.** Elevations must carry "PLACEHOLDER HEIGHTS: NOT A VALIDATED ELEVATION" |
| **D2** 2:1 basis | Reading A on basis H1: garden + patio/walkway = 2 × 228.78 = **457.56 m²** (compound 686.34 m²) | Transcript: "two to one ratio directly to the housing". The H1 footprint is stated in note 1 and **verified** here | Housing area **VERIFIED as drawn** (but it depends on PA-01/PA-02 build-ups). The reading and basis are **UNRESOLVED** | Alternative targets: H2 → 472.80; H3 → 494.64; reading B adds the walkway on top. **Not in the inventory:** a GIA basis (208.26 m² for two dwellings, from the drawing's room schedule) gives 416.52 m² (−9%). A change to the wall build-ups (DR-01) moves every target | **Yes** |
| **D3** Position of the public node | North of the housing, behind the conservatories, across the housing's 18.6 m width. The labelled rear gardens stay with the housing | PLACEHOLDER. North is an ASSUMPTION (PA-07). There is no site boundary or survey | **UNRESOLVED** | The whole compound layout. It may not fit the real site. Arithmetic only: 457.56 m² across 18.6 m would be a strip about 24.6 m deep beyond the conservatories. If the rear gardens are later counted as public, the area is double-counted | **Yes** |
| **D4** Walkway width | 2,000 mm | The parameter file cites PA-06. PA-06 itself records **1.5 m** paths (ASSUMPTION) and gives 2.0 m only as the competing compound standard (Logistics r40 vs 2.0 m) | **PROVISIONAL**, with conflicting sources (1.5 vs 2.0) | Walkway area, which sets the garden-alone figure under reading A. Route widths and access. No compliance is implied | **Yes**: choose 1.5 m or 2.0 m |
| **D5** Reference axis for the orangeries' ±45° | The building front (X axis) | Transcript: "a conservatory facing the two orangeries at 45 degree angle, counterclockwise and clockwise". The brief: ±45° to an agreed axis | **UNRESOLVED** | For rectangles, ±45° to X and ±45° to Y give the same pair of angles. What changes is which orangery is "clockwise" and what the orangeries face. The transcript ties the angle to "a conservatory" (singular), but there are two, one per dwelling. Solar orientation depends on the assumed north (PA-07) | **Yes**: confirm the axis and which conservatory |
| **D6** Water fountain | Included as optional component `12_WATER_FOUNTAIN`, Ø 1,500 PLACEHOLDER | Transcript only (named first); not in the written brief | **UNRESOLVED** | Another water body near children and animals. Needs a water source, and separation from the well | **Yes**: include or omit |
| **D7** Component sizes | Orangeries 8,000 × 5,000 × 3,500 (×2); canopy 8,000 × 6,000, eaves 2,700; well Ø 1,500, depth UNKNOWN; shed 3,000 × 2,400 × 2,400; kennel 2,400 × 1,800; cat shelter 1,200 × 900; pond 6,000 × 4,000, depth UNKNOWN; generator 2,000 × 1,000 × 1,500 plus 1,000 clearance; fountain Ø 1,500; back gate 1,200 | PLACEHOLDER, from the transcript's adjectives ("medium", "large", "big") | **UNRESOLVED** | Whether everything fits. Arithmetic on the placeholders only: their unrotated footprints total about 170 m², 37% of 457.56 m². The ±45° rotation needs more area. The generator's size and clearance are safety-relevant (section 6) | **Yes** |
| **D8** Pet access into the dwellings | Not modelled | Transcript: "cat or dog to enter a house". Adding it would change the frozen Draft 0.2.2 housing | **UNRESOLVED** | If it is wanted, it needs a new housing draft through the issue process, not the 3D proposal | **Yes**: confirm the exclusion |
| **D9** Front entrance | Keep the plan's single leaf (arc r = 1,010 in a 1,100 opening; product per PA-11). Record the sketch's double door as a conflict | Plan: **VERIFIED** single leaf, and every external door on the plan is a single leaf (section 4). The sketch does not say which elevation it shows, so matching it to the front entrance is an inference | Plan geometry **VERIFIED**; door product **PROVISIONAL** (PA-11); conflict **UNRESOLVED** | A double door would change the issued housing (opening width and hall), so it would need a new draft issue. It also changes the front elevation | **Yes** |
| **D10** Steps or level threshold | Keep the level threshold and approach (PA-12). Record the sketch's steps (about 3; the riser count is uncertain) as a conflict | PA-12 is an **ASSUMPTION**. Note 2 calls M4(2) "an optional requirement that applies only where a planning condition requires it". Which category governs is still open (OQ-01) | **UNRESOLVED** | The floor datum Z = 0 and every height. Approach, threshold and the accessibility target. No compliance claim is made either way | **Yes** |
| **D11** "1400 × 1000" | Unresolved. Plan widths stay; the 1,000 height is not applied | No 1,400 opening exists in any external wall (**VERIFIED**, section 4). The annotation sits below the sketch's ground line, horizontally under the window. Linking it to the window, and reading it as W × H, are both interpretations. The sketch window is drawn about square | **UNRESOLVED** | A 1,000 height would set the head and sill on every elevation. A 1,400 width would change the issued plan | **Yes**: the client to say which element, and W × H or H × W |
| **D12** Lattice glazing bars | Shown only if approved; appearance only | The sketch, and the CADCraft screenshot, which is probably a third party's quick redraw (section 3). In the screenshot the two casements have different lattice densities; that is probably an artefact of the quick redraw and not information | **UNRESOLVED** | Low if they are glazing bars. **If they are fixed security bars or grilles**, any escape-window function (bedrooms) needs review | **Yes** |
| **D13** Right-hand element of the sketch | Not modelled | A vertical line, a diagonal and horizontal lines at the right of the sketch. Not identified; possible readings (a return wall, ramp, gate or fence) are questions, not findings | **UNRESOLVED** | Unknown | **Yes**: the client to identify it |

**Which stages need which decisions:**

- Stage 0 (throwaway trials) needs **none**.
- Stage A (DXF reference) needs **none**. It does need the legend-swatch filter.
- Stage B (housing) needs **D1 and D8–D12**.
- Stage C (compound) needs **D2–D4**.
- Stage D (facilities) needs **D5–D7**.

## 6. Gate 5: compound definition and ratios

**Definition followed:** "Triplex" means three spatial nodes:

1. the Orion Duplex housing, unchanged;
2. the shared public garden;
3. the shared public patio and walkway.

It does not mean three storeys or three units. Every shared facility stays outside the housing node.

**A wording note on the transcript, flagged and not acted on:** it says "the triplex is the open gardening space it occupies" and "the third uniplex is the space". That could be read as two dwellings plus one public space. Under either reading the shared facilities stay outside the housing. Reporting the garden and the patio/walkway separately, as below, covers both readings.

**Ratios.** These are **targets, not measurements: 0 m² is modelled.** The 2:1 rule is a provisional reading of the transcript, not a site constraint, because there is no site boundary or survey.

| Ratio | Reading A (proposed, D2) | Reading B (alternative) | Measured |
|---|---|---|---|
| Garden : housing (H1 = 228.78 m²) | (457.56 − W) / 228.78. Below 2:1; the exact value is not defined until the walkway area W is set by D3 and D4 | **2.00 : 1** (garden = 457.56 m²) | Not measurable: no geometry |
| (Garden + patio/walkway) : housing | **2.00 : 1** (457.56 m²) | (457.56 + W) / 228.78, above 2:1 | Not measurable: no geometry |

Stage C will report both ratios from measured model areas: 457.56 m² ±1% under reading A, or whichever target D2 sets.

## 7. Outstanding decisions and safety constraints

**Approvals requested (none has been actioned):**

1. **Configuration change: needed for Stage 0's DXF test and for any save into this workspace.** Change the local-scope `solidcraft` server args from `["mcp"]` to:
   `["mcp", "--allow-path", "<project root>\\MMUCO_ORION_Triplex_Compound_3D_MODEL_PROPOSAL_NOT_ISSUED"]`
   - It takes effect only in a **new** session started in `u\`.
   - **Do not use `--allow-any-path`.**
   - The project root, which holds the issued drafts, stays outside the sandbox.
   - **Residual risk:** the allowance covers the whole workspace, including `source_refs/`. Mitigation: re-check `evidence/workspace_files.sha256` and run `verify_protected.sh` after every stage.
   - **A tighter alternative:** allow only `model\` and `views\`, and pass the DXF to `sketch.insert_dxf` as `text` instead of `path`.
   - **APPLIED, 25 Oct 2026, after the user's explicit approval** of the whole-workspace option.
     - This session ran `claude mcp remove solidcraft -s local` and `claude mcp add -s local solidcraft -- "C:\Program Files\SolidCraft\solidcraft-cli.exe" mcp --allow-path "<project root>\MMUCO_ORION_Triplex_Compound_3D_MODEL_PROPOSAL_NOT_ISSUED"` from `<project root>`.
     - `claude mcp get solidcraft` confirms: local scope, Connected, `Args: mcp --allow-path <project root>\MMUCO_ORION_Triplex_Compound_3D_MODEL_PROPOSAL_NOT_ISSUED`.
     - The previous args were `["mcp"]`. There is no user-scope entry and no `.mcp.json`.
     - The change takes effect only in a new session started in `u\`. Stage 0 has **not** been started.
   - **A second entry also now exists.** The user ran the same commands from `u\mmuco`, which created a local-scope SolidCraft entry for `<project root>/mmuco`, with the same args. SolidCraft was previously not available from `u\mmuco`, the public repository.
     - With this entry, sessions started there also got SolidCraft, with write access to this workspace and to the open design's folder.
     - **Removed at the user's instruction:** this session ran `claude mcp remove solidcraft -s local` from `u\mmuco`.
     - **Confirmed afterwards:**
       - from `u\mmuco`: `No MCP server named "solidcraft"`;
       - from `u`: Connected, with the `--allow-path` args above;
       - `~/.claude.json` now holds one SolidCraft entry, local scope for `<project root>`, and no user-scope entry.
2. Decisions **D1–D13** (section 5), at least before the stages that depend on them.
3. Whether to correct the inventory and parameter file for the section 4 discrepancies: the legend swatches, the missing gable door, the PA-06 wording, and the GIA basis. These were reported, not edited. The original documents are unchanged and still match `evidence/workspace_files.sha256`.

**Safety and control constraints that stay in force:**

- **Issued files:**
  - Issued and frozen files are read-only.
  - SolidCraft must never open an issued file. It uses only the `source_refs/` copies.
  - Any file access goes only through the workspace allowance.
- **Placeholders:**
  - Placeholder heights and elevations must never be presented as validated designs.
  - Every view must carry the label "MMUCO ORION TRIPLEX COMPOUND — 3D MODEL PROPOSAL — NOT ISSUED".
  - Provisional geometry must be coloured differently from verified geometry.
- **Not to be invented:** site dimensions, storey heights, roof form, foundations, drainage, structure, or the design of the external facilities.
- **Water:** rain and well water are never shown as drinkable. Drinking use needs treatment, testing, hygienic storage and a water-safety plan. The well needs a cover or barrier.
- **Pond:** it is not a swimming pool. Its depth, edge protection (children and animals), water source and maintenance are unresolved. It must stay distinct from the well.
- **Generator (diesel):** noise, exhaust, ventilation, fire separation, fuel storage, weather protection, the electrical connection, drainage and maintenance access all need assessment before a location is fixed. Keep it and any fuel away from the well, the orangeries, the canopy and the pond. The separation distances are UNKNOWN.
- **Animals:** keep them separate from the well, from food growing and from food storage. Hygiene review is needed.
- **Canopy:** structure, wind and drainage are not designed.
- **Access:** no component may block the walkway, the back gate or emergency egress. Perimeter and gate security are for design review.
- **Housing:** party-wall fire and acoustic performance and all wall build-ups are provisional (PA-01).
- **Outputs and sending:**
  - Outputs stay inside this workspace.
  - Make no compliance claims.
  - Send nothing.
  - Make no git commit or push in `mmuco/`.

## 8. Proposed first modelling operation: Stage 0 (throwaway trials only)

This runs in a new session, after the configuration change is approved and the server restarted. All of it happens in an **unsaved throwaway design**. Nothing becomes project geometry.

| # | Operation | Expected output | Records |
|---|---|---|---|
| 0.1 | `running`, then `new_design` (throwaway) | An empty design | PASS / FAIL |
| 0.2 | `solid.box` 1,000 × 2,000 × 3,000. The three different sizes make each view identifiable | One body; `inspect_design` and `measure` confirm 1,000 / 2,000 / 3,000 | PASS / FAIL |
| 0.3 | `view.apply` for `back`, `left` and `right` (also `front`, `top` and `iso`), with a `screenshot` of each. Test whether the projection is orthographic: are the edges parallel, and do the proportions match 1:2:3? Can the camera be set to orthographic? | Six screenshots, plus a verdict on orthographic projection | Each view PASS / FAIL / NOT SUPPORTED |
| 0.4 | `save` to the per-process temp folder or `model/_stage0_throwaway/`; `open` it again; re-`measure` | The dimensions are unchanged after reopening | PASS / FAIL |
| 0.5 | `sketch.insert_dxf` on `source_refs/MMUCO_ORION_Duplex_Draft_0.2.2.dxf` (the **copy**), then `inspect_design` | The number of curves created. The building piers span 18,600 × 12,300 ±1 mm. The legend swatches appear outside, at y < 0. Note what happens to HATCH, TEXT and DIMENSION entities. **Without `--allow-path`** this is expected to be refused, which also confirms the sandbox works | PASS / FAIL / NOT SUPPORTED |
| 0.6 | A render (`screenshot` of the shaded view; optionally `file.export_view_dxf` of one elevation) | One image | PASS / FAIL |
| 0.7 | Discard the throwaway design. Re-run `verify_protected.sh` and the workspace hash list | 240 / 166 / 91 OK. The 880-file comparison will still differ on the `mmuco/` paths until the user approves the re-baseline (section 2) | PASS / FAIL |

**Stage 0 deliverable:** `evidence/stage0_trials_NOT_ISSUED.md`, a PASS / FAIL / NOT SUPPORTED log, plus labelled screenshots in `views/stage0_throwaway/`. After that it **stops for review** before Stage A.

## 9. Design principle received after the gate: maximise natural light

**The principle (the user, 25 Oct 2026):** use as much natural light as possible. This is a design intent for the proposal, not a measured value.

**Sun path:** this report uses the standard sun path. The sun rises in the east and sets in the west. A message in this session stated the reverse; that was corrected and not adopted.

**What the principle means on the plan.** Everything here rests on the **ASSUMED** north (PA-07: +Y is north, gardens to the north). True north (SI-03), the site's latitude and hemisphere, the site boundary and any neighbouring obstructions are all **UNKNOWN**.

| Face (under PA-07) | Sun it would receive |
|---|---|
| Front (−Y, porches, bedrooms) faces **south** | Midday sun if the site is in the northern hemisphere; less if it is in the southern |
| Rear (+Y: kitchens, living/dining, conservatories, the rear gardens and the proposed public node) faces **north** | The reverse |
| LHS gable (x = 0, dwelling A) faces **west** | Afternoon and evening sun |
| RHS gable (x = 18,600, dwelling B) faces **east** | Morning sun |

The dwellings mirror each other, but the sun does not. Dwelling A's gable rooms (bedroom 1, the quiet work room and the kitchen) get evening light; dwelling B's get morning light.

**Proposed D14 (UNRESOLVED; needs explicit approval and site information):** use natural light as a layout criterion for the compound. It depends on true north and the site location, and it affects:

- **D3:** a public node north of the housing would sit partly in the building's shadow if the site is in the northern hemisphere.
- **D5 and D7:** glazed orangeries for food growing need sun. Their ±45° orientation and position should follow the true sun path, not the assumed north.
- **D1, D11 and D12:** window heads and sills, the 1,400 × 1,000 window question, and lattice bars that would reduce glazed area.
- **The canopy (component 05):** it would shade whatever lies beneath it.

**Balance and evidence:**

- More glazing also raises overheating risk and heat loss. Note 4 on the drawing already makes the rooflight subject to daylight (BS EN 17037) and overheating (ADO / TM59) assessment.
- The proposal model makes **no daylight or compliance claim**.
- **SolidCraft has no sun-position or shadow command:** the `list_commands` filters `sun` and `shadow` return nothing. Its render lighting is an environment map with rotation and intensity only.
- A real sun or shadow study needs the site's latitude and true north first. It then needs either computed sun vectors with a geometric shadow check, or a specialist daylight tool.

## 10. Further client direction (25 Oct 2026, recorded only; no geometry made)

**Site orientation (public copy).** Orientation readings supplied by the client are recorded privately and are not published here. None has been confirmed, so PA-07 (north ASSUMED) is unchanged. A proper site bearing needs one of:

- a compass reading taken outdoors on site, corrected for magnetic declination;
- a bearing taken from a map of the site;
- a survey.

**Sun path:** the standard sun path is used: the sun rises in the east and sets in the west.

**Proposed D15: orientation indicators on every plan and overview (UNRESOLVED; needs explicit approval).** These would be indicators only, with no analysis behind them:

- **North arrow:** labelled ASSUMED until true north is confirmed.
- **Cardinal labels:** N, E, S and W.
- **Sun-path arrows:** sunrise in the east, sunset in the west. The midday direction is shown only once the hemisphere and latitude are known.
- **Prevailing-wind arrow:** labelled "TO BE CONFIRMED (no site wind data)". No direction will be invented.

In the model these would sit in their own component, `00_ORIENTATION_INDICATORS`. Their purpose is to let the engineer design for sun, wind and insulation.

**Proposed D16: rotate one dwelling ("uniplex") by 90° (UNRESOLVED; this is a housing design change).** The user's aims are to separate the two dwellings and to make the form less square.

What it would change:

- **Party wall:** the two dwellings would no longer share the 200 mm party wall (x 9,200–9,400) as mirror images. They would become detached, or linked at one corner or a short wall, which changes fire and acoustic separation.
- **Footprint:** each dwelling needs its own external wall where the half party wall was, so the footprint changes. The 228.78 m² basis for the 2:1 rule (D2) changes with it.
- **Entrances, windows and rooms:** the entrances, the gable windows and the rooms that faced the party wall would all need re-planning.
- **Heat loss:** more external wall per floor area means more heat loss. That cuts against insulation and needs weighing against the gains in daylight, ventilation and privacy.

**Scope:** Draft 0.2.2 is frozen, and this proposal keeps the duplex unchanged. D16 therefore cannot be modelled as an edit to the issued housing. It needs its own option study in a scratch folder, followed by a new draft through the issue process.

**Also needed first:** the rotation and the orientation of each dwelling should follow true north (D14), which is not yet known.

**How a confirmed bearing would be applied.** Bearings are measured clockwise from north (north 0°, east 90°, south 180°, west 270°). If F is the bearing faced when looking straight out from the front of the duplex, the drawing's coordinates stay unchanged: only the north arrow and the indicators rotate, and the drawing's "up" (+Y, the rear and gardens) has bearing F + 180°.

| Front faces (F) | Rear / gardens face | North arrow on the drawing |
|---|---|---|
| 225° (SW) | 45° (NE) | 45° anticlockwise from up |
| 135° (SE) | 315° (NW) | 45° clockwise from up |
| 45° (NE) | 225° (SW) | 135° clockwise from up |
| 315° (NW) | 135° (SE) | 135° anticlockwise from up |

A bearing is recorded as USER-MEASURED, not SURVEYED, until a survey confirms it. Until true north is known, the orientation-dependent decisions (D3, D5, D7 and D16) cannot be settled.

## 11. Decisions confirmed by the user

| Component | Decision | Date | Effect |
|---|---|---|---|
| `09_POND` | **A pond, not a swimming pool. CONFIRMED by the user.** This was prompted by a reference backyard plan the user shared, which shows a swimming pool and spa | 25 Oct 2026 | The parameter file's existing wording, "not a swimming pool", is now a user decision, not just a modelling note. No pool, pool fencing or pool water treatment is modelled. The pond's footprint (6,000 × 4,000) remains a PLACEHOLDER. Its depth, edge protection for children and animals, water source and maintenance remain UNRESOLVED. It stays separate from the rainwater well and any drinking-water route |

`compound_parameters_PROVISIONAL.json` is not edited, because it is in the workspace hash list. This table is the record of the decision.

## 12. Candidate components (added at the user's request, 25 Oct 2026; need approval)

These come from the backyard-design material the user shared. They are **not** in the client transcript's programme. The user asked for them to be recorded as candidates with safety separation.

**Neither will be modelled until it is approved.** If approved, each would first appear as a labelled placeholder zone. No sizes, fuels or separation distances are invented: each stays UNKNOWN until decided and reviewed.

| ID | Candidate component | Proposed value | Class | Approval |
|---|---|---|---|---|
| **D17** | `13_OUTDOOR_COOKING_CANDIDATE`: a shared outdoor cooking area | Size, fuel (gas, charcoal or wood) and equipment: **not set** | UNRESOLVED | Needed |
| **D18** | `14_FIRE_PIT_CANDIDATE`: a shared fire pit | Size, type (wood, smokeless or gas) and surround: **not set** | UNRESOLVED | Needed |

**Separation rules proposed for D17 and D18.** These are qualitative. The distances are **UNKNOWN** until a fire-safety review, in the same way as the generator rules.

| Keep clear of | Outdoor cooking area (D17) | Fire pit (D18) | Why |
|---|---|---|---|
| **Diesel generator (10) and any fuel store** | Yes. Any bottled-gas store for cooking must be kept apart from the diesel store too | Yes | Ignition, fuel fire and exhaust |
| **Fixed canopy (05)** | No open flame, charcoal or wood cooking under the canopy unless its structure and materials are designed and approved for it. Smoke must be kept clear of the gathering area | **Never under the canopy** | The canopy's structure and materials are not designed; heat, smoke and fire spread |
| **Orangeries (04)** | Yes: away from the glazing, vents and crops | Yes | Heat and smoke on the glazing and plants; fire spread |
| **Shed (07)** | Recommended | Yes | Timber, tools and stored fuel |
| **Animal facilities (08)** | Yes: food hygiene (the existing rule) | Yes | Hygiene; animal safety |
| **Rainwater well (06) and water use** | Use mains water for food preparation. **Do not use well water** unless it is treated and tested | Water or sand for putting fires out may be kept nearby | Well water is not shown as drinkable |
| **Dwellings** | Away from openings and ventilation intakes (MVHR, note 3; locations not yet designed) | Yes | Smoke entering the homes |
| **Walkway, back gate and emergency routes** | Must not block them (the existing rule) | Must not block them; not on an escape route | Access and egress |
| **Boundary hedges and trees** | Recommended | Yes: no overhanging branches | Fire spread |

**Further conditions:**
- **Both:** a non-combustible surface around each one. Supervision and a guard where children and animals are present. Placement downwind of the gathering areas and the homes, once the prevailing wind is known (it is UNKNOWN).
- **Daylight:** neither may shade the orangeries' sun zone or block daylight to the house (D14).
- **Area:** if approved, both count within the public garden and patio area for the 2:1 check (D2).
- **No compliance claim:** this is not a fire-safety or compliance assessment. A professional review is required.

## 13. Backyard concept DXF (created at the user's direct request, 25 Oct 2026)

The user asked for "a backyard.dxf … to complete the duplex", with a garage for car storage. This is the first geometry produced in this workspace. It is a **2D concept in a separate folder**, `backyard_concept_NOT_ISSUED/`. It is not the SolidCraft model, and Stage 0 has still not been run. The folder's README lists every value and its class.

**Evidence:**
- The independent read-back check passes 13/13, including a positive control.
- **Housing:** the copied reference is 26 piers spanning 18,600 × 12,300, with no legend swatch.
- **Areas:** the public node is 457.56 m² (2.000 × housing); the walkway is 56.58 m²; the garden alone is 400.98 m² (1.753 × housing).
- **Orangeries:** 8,000 × 5,000 at +45.000° and −45.000°.
- **Garage:** 6,000 × 6,000 internal.
- **Containment and overlap:** every component is inside the provisional boundary, and none of the checked pairs overlap.
- **CADCraft:** it opened the file with 305 entities and no warnings, and rendered `backyard_preview_NOT_ISSUED.png`.

**New proposals introduced by this drawing (UNRESOLVED; need approval):**

| ID | Proposal | Default drawn |
|---|---|---|
| **D19** | Garage for car storage | Double: 6.0 × 6.0 m internal, one bay per dwelling, on the west (LHS) side, with a street-side driveway. Every value is a PLACEHOLDER |
| **D20** | Move the generator out of the shared garden | A service yard behind the garage. Location NOT FIXED: noise near dwelling A, exhaust, fire, fuel and the cable route all need review |
| **D3 departure** | Width of the public node | The full site width including the side patios (22.2 m), not the housing width (18.6 m), so that the ±45° orangeries and the walkway fit |

**Unchanged:**
- The issued Draft 0.2.2.
- The `source_refs/` copy (sha256 `2ec8d3f3…`).
- `compound_parameters_PROVISIONAL.json`.
- Every frozen record.

**Update to section 13 (25 Oct 2026): garages.** At the user's choice, the double garage has been replaced by **one single garage per dwelling, one on each side** (D19).

- **Size:** each is 3.0 × 6.0 m internal (3.4 × 6.4 external), with a 2.4 m street-side door, one car and its own driveway. All of these are PLACEHOLDERS.
- **Position:** each is 4.2 m from its gable, mirrored about the party-wall line.
- **Boundary:** the provisional boundary is now T-shaped.
- **Generator:** the yard stays behind garage A (D20).
- **Re-check:** 14/14 PASS. The public node is still 457.56 m² (2.000 × housing); the garages total 43.52 m², in the housing node and outside the 2:1 basis. CADCraft opened the file with 317 entities and no warnings, and the preview was re-rendered.

## 14. Proposal D21: add a basement to the duplex (25 Oct 2026; UNRESOLVED; needs approval)

**The proposal (the user):** consider adding a basement to the duplex. Its prompt was a foundation video the user shared, showing US precast basement construction.

**Class: UNRESOLVED. A housing design change.**
- Draft 0.2.2 is frozen, and this proposal keeps the duplex unchanged.
- So, like D16, a basement **cannot** be added by editing the issued housing. It needs its own option study in a scratch folder, then a new housing draft through the issue process.
- None of these are designed, and none is invented here: basement depth, floor level, ceiling height, retaining-wall build-up, waterproofing, structure, foundations, drainage and radon protection.

**What a basement would change:**

| Area | Change |
|---|---|
| **Scope and status** | The dwellings would no longer be single-storey: each would have a ground floor plus a basement. This still fits the Triplex definition, which rules out three storeys, not a basement. It needs a new housing draft |
| **Use (to decide first)** | Storage or plant only, or habitable rooms. Habitable rooms bring daylight, ventilation, an escape window or door, fire safety, ceiling height and damp control into play. Storage or plant needs far less |
| **One per dwelling or shared** | The default is one basement per dwelling, divided by a separating wall continued down from the party wall, which keeps fire and acoustic separation. A shared basement would need its own access and separation |
| **Stairs and the ground-floor plan** | Each dwelling needs an internal stair. The likely place is the 1.5 × 6.6 m hall, but a stair there would block the bedroom and bathroom doors. **The ground-floor plan would have to be redesigned**, which affects the room sizes and the accessibility targets. A stair is not step-free; no compliance claim is made |
| **Structure and foundations** | The basement walls retain soil, and the floor slab becomes the lowest structure. Wall and slab design, the waterproofing approach (in the UK, usually by reference to BS 8102, for an engineer to confirm) and the load path from the ground-floor walls all need a structural engineer |
| **Ground conditions** | A **ground investigation becomes essential**: soil, groundwater level, contamination, and the effect on neighbouring foundations. High groundwater can make a basement costly or unsuitable |
| **Radon** | A basement is more exposed to ground gas. Check the site against the official UK radon maps. If protection is needed, a membrane or sub-slab sump goes in before the slab |
| **Drainage and power** | A perimeter drain to a sump pump is likely. The **sump discharge must stay separate from the rainwater well** (the section 7 water rules). A sump pump needs power; backup from the D20 generator would need assessing |
| **Daylight (D14)** | A basement gets little daylight. Lightwells or escape windows would follow the true sun path, which is not yet known. They must be kept away from the generator's exhaust (D20) |
| **Levels (D10)** | The ground-floor level sets how deep the basement is and whether the entrances need steps. This ties directly to the open conflict between the steps in the sketch and the level threshold on the plan |
| **2:1 rule (D2)** | On basis H1, the building footprint, the basement changes nothing: the footprint stays 228.78 m². **If the basis became floor area**, the basement would add floor area and raise the public-garden target |
| **Garages, garden and well** | The excavation and lightwells sit next to the private rear gardens and the side passages. Any change to groundwater near the rainwater well needs considering |
| **Cost and programme** | Excavation, spoil removal, temporary works and waterproofing would lengthen the build and raise its cost |

**Needed before D21 can be decided:**
1. The basement's **use**: storage or plant, or habitable.
2. **One per dwelling, or shared.**
3. A **ground investigation** (soil, groundwater, radon).
4. A **structural engineer** and a waterproofing specialist.
5. Then an option study in scratch and a new housing draft.

No compliance or feasibility claim is made.

**Basement concept DXF (created at the user's request, 25 Oct 2026).** `basement_concept_NOT_ISSUED/basement.dxf` illustrates D21. It does not approve it. The folder README lists every value and its class.

What it shows:
- **Housing:** the Draft 0.2.2 ground floor, unchanged, as a grey overlay.
- **Basements:** one per dwelling under the verified 18,600 × 12,300 outline, with a 300 retaining wall (PLACEHOLDER) and a 200 separating wall under the party wall. Each measures 104.13 m² inside the walls.
- **Indicative:** a stair zone in each hall, sumps and a perimeter drain.
- **Optional:** rear lightwells.
- **Orientation:** a north arrow marked ASSUMED.

**Checks:**
- The independent read-back check passes 13/13, including a positive control.
- CADCraft opened the file with 153 entities and no warnings, and rendered the plan and sheet previews.
- Depth, levels, structure, waterproofing, drainage and radon remain NOT DESIGNED.

**D21 update (25 Oct 2026): use decided by the user. The basements would hold HABITABLE ROOMS.**

D21 itself is still a proposal and is **not approved**. This settles only the intended use, if a basement goes ahead. It turns daylight, ventilation, escape, fire and damp from "only if habitable" into **requirements of the design**.

The references below show where the requirements sit (in England, the Approved Documents and the standards they cite). **None is claimed as met.** The applicable route is for the designer, the fire and structural engineers and Building Control to confirm.

| Topic | What habitable use adds | Where it sits |
|---|---|---|
| **Daylight** | **Lightwells or sunken courts become required, not optional.** Each habitable room needs useful daylight, so the number, size and depth of the lightwells depend on the basement room layout, which is not designed. A daylight assessment would be needed (the drawing already cites BS EN 17037 for the rooflight). **This conflicts with D14:** a basement is the hardest place to light naturally. The lightwells should face the true sun path, which is not yet known, and they take area from the 4 m private rear gardens | Daylight assessment (BS EN 17037); natural-light principle D14 |
| **Ventilation** | Background ventilation and purge ventilation (openable windows) for every habitable room. The dwellings already plan MVHR (note 3); it would need extending to the basement, with duct routes through the ground floor. Ventilation also controls condensation | Approved Document F |
| **Escape** | A basement habitable room needs a safe way out if fire blocks the stair. Usual routes are an **escape window or door into a lightwell**, with a route from it up to a place of safety, or a **protected stair**. Which applies depends on the layout. The lightwell then also needs guarding at ground level and a way to climb out | Approved Document B (means of escape); Approved Document K (guarding) |
| **Fire** | Fire separation between the basement and the ground floor. Smoke or heat detection in the basement, linked to the dwelling's alarms. The 200 separating wall under the party wall must give fire and acoustic separation between the two basements. Lightwells and escape windows must stay away from the D20 generator, its fuel and its exhaust | Approved Document B; Approved Document E (separating wall) |
| **Damp** | Habitable space needs the highest waterproofing grade: in BS 8102 terms, no water penetration, with ventilation or dehumidification (the engineer to confirm). Condensation control. A sump pump with a power backup (D20) and a failure alarm. Drainage for each lightwell. Radon protection if the site needs it. The flood risk must be checked by the ground investigation | BS 8102 (waterproofing below ground); Approved Document C (moisture, radon) |

**Also follows from habitable use:**
- **Ceiling height:** a usable height is needed. If the national space standard (NDSS) is applied, it sets a minimum height over most of the floor. The depth is still UNKNOWN.
- **Insulation:** of the basement walls and floor (Approved Document L).
- **The stair:** stair geometry and guarding (Approved Document K).
- **Access:** the basement storey is not step-free (Approved Document M). No claim is made against the M4(2) target.
- **Occupancy and space:** if bedrooms go below ground, the 2 bed / 4 person occupancy (PA-13) and the room sizes change.
- **Area:** each basement adds about 104 m² of internal floor area, which affects any floor-area basis for the 2:1 rule (D2).

**Unchanged:**
- One basement per dwelling (the default).
- The ground-floor stair problem: each hall would still need redesigning.
- A ground investigation and a structural engineer come first.

## 15. Access clarification: the shared garden is RESIDENTS-ONLY (Q-A, 25 Oct 2026)

**Source:** the user's answer to question Q-A, raised under H-D1 in the Hive concept plan (`../MMUCO_ORION_Hive_System_CONCEPT_PROPOSAL_NOT_ISSUED/`, section 6.1).

**Clarification.** The compound's "public" garden (also called the public node, public space or public area) is **shared and residents-only**. It is for the tenants of the Orion Duplex and their households, and **not open to the general public**. This applies throughout this report, including:
- the Gate 5 node names ("public garden", "public patio and walkway");
- the 2:1 target (D2: "public area 457.56 m²");
- the provenance and backyard sections;
- the drawing labels ("PUBLIC NODE").

**History is kept.** The earlier wording in sections 1 to 14 is **not rewritten**; read "public" there as "shared, residents-only". The backyard and basement DXFs are unchanged: no geometry or labels were edited. A later drawing revision can relabel "PUBLIC NODE" as "SHARED GARDEN (RESIDENTS-ONLY)".

**Consistency and effects:**
- **The transcript:** this matches its "public space shared by … tenants".
- **The back gate:** it matches the back gate's "secure, controlled access" (boundary and back gate, component 11; the transcript's "security built in by design").
- **2:1 rule (D2):** unchanged in area. The 457.56 m² target now reads as shared residents' space.
- **Hive (H-D1, PROPOSED):** the Hive can sit inside the shared garden with no separate boundary. Safety guards still apply inside it: the covered well, pond edge protection, a fenced rice–fish cell if approved, and compost bins.

**Unchanged:** every decision's substance, the frozen and issued files, and the drawings.
