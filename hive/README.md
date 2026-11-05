# MMUCO ORION Hive System

> **Not an approved design, construction drawing or compliance document.**

**The Hive System** is the Orion Duplex's ecological food-production garden. It sits inside the Triplex Compound's **residents-only shared garden** (see [`../triplex/`](../triplex/)), and covers:
- crop beds, plus the orangeries for covered growing;
- pollinator habitat;
- rainwater storage and irrigation;
- compost;
- an optional rice–fish trial.

It is a **design hypothesis to be tested**. No food yield or self-sufficiency is claimed.

| Folder | What it is | Status |
|---|---|---|
| [`concept_NOT-ISSUED/`](concept_NOT-ISSUED/) | The written concept plan (system diagram, land-use schedule, crops and seasons, water, risks, decisions H-D1 to H-D10), plus `hive.dxf`: a 2D plan of the Hive zones with its validation | **Concept proposal, not issued** |

**Key points:**
- **The duplex housing is unchanged** (Draft 0.2.2).
- **H-D1** (community-managed Hive; the landowner keeps title; access for residents and their households; essential food needs first) is **PROPOSED — FOR REVIEW**, not an approved legal arrangement.
- **Orientation:** north is ASSUMED, and there is no site survey.
- **Not drawn:** a managed beehive (H-D5), and drinking-water infrastructure, which is kept separate.

**Verify the copy:** see `concept_NOT-ISSUED/CLEANING_RECORD_NOT-ISSUED.md`. To regenerate and re-check `hive.dxf`, run from `concept_NOT-ISSUED/hive-dxf_NOT-ISSUED/`:

```bash
node scripts/check_hive_dxf.mjs hive.dxf ../source-copies/backyard_concept_from_triplex.dxf
```
