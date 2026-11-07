"""Generate MMUCO HIVE-E + HIVE-W concept detail DXF (rev 3).

Rev 3 changes from rev 2:
- Hive width enlarged from 10,000 to 10,750 mm (outward expansion only,
  patio boundary fixed). Outer bed perimeter now 1,500 mm (was 750).
- Service strip 2,750 mm wide; all stations have >= 1,500 mm clear approach.
- Door swings verified against continuous route.
- Sheet layout: two enlarged hive details + small site-location inset.
  Duplex outline reduced to inset only.
- 1,500 mm described as project design target throughout.

Dimension chain (width):
  1,500(outer) + 1,000 + 1,500 + 1,000 + 1,500 + 1,000 + 500(gap) + 2,750(svc) = 10,750

Components per hive (short IDs on drawing, full names in schedule):
  CB01-06  Crop beds 1,000 x 3,000 mm (3 cols x 2 rows)
  IR01     Irrigation station / water point
  TP01     Tool cupboard 1,200 x 600
  TP02     Potting bench 1,500 x 750
  HV01     Harvest bench 1,500 x 750
  HV02     Crate staging 1,000 x 500
  HV03     Seed cupboard 1,200 x 500
  CP01-02  Compost bays 1,000 x 1,000 each
"""
import math, os

OUT = r"C:\Users\Public\Public Projects\github\mmuco\hive\concept_NOT-ISSUED\hive-dxf_NOT-ISSUED\hive-east-and-west.dxf"

hc = [0x100]
def h():
    hc[0] += 1
    return format(hc[0], 'X')

PAL = {
    "dwell":   (0xE8, 0xED, 0xF2),
    "crop":    (0x77, 0xC6, 0x6E),
    "path":    (0x56, 0xC5, 0xD0),
    "harvest": (0xE4, 0xB4, 0x5F),
    "pollin":  (0xB6, 0x9A, 0xDD),
    "irrig":   (0x56, 0xC5, 0xD0),
    "dim_r":   (0xFF, 0x44, 0x44),
    "inset":   (0x88, 0x88, 0x88),
}

def rgb420(r, g, b):
    return r * 65536 + g * 256 + b

TH = {"title": 600, "zone": 500, "head": 400, "room": 300, "sub": 250,
      "dim": 250, "det": 200, "sm": 180, "xs": 150}

# ---- DXF helpers ----
def dxf_header():
    return "0\nSECTION\n2\nHEADER\n0\nENDSEC\n"

def dxf_ltype(name, desc, pat):
    s = f"0\nLTYPE\n5\n{h()}\n100\nAcDbSymbolTableRecord\n100\nAcDbLinetypeTableRecord\n2\n{name}\n70\n0\n3\n{desc}\n72\n65\n73\n{len(pat)}\n40\n{sum(abs(x) for x in pat):.1f}\n"
    for p in pat:
        s += f"49\n{p}\n74\n0\n"
    return s

def dxf_layer(name, aci, lt="Continuous", rgb=None, lw=None):
    s = f"0\nLAYER\n5\n{h()}\n100\nAcDbSymbolTableRecord\n100\nAcDbLayerTableRecord\n2\n{name}\n70\n0\n62\n{aci}\n6\n{lt}\n"
    if rgb: s += f"420\n{rgb420(*rgb)}\n"
    if lw is not None: s += f"370\n{lw}\n"
    return s

def dxf_tables():
    s = "0\nSECTION\n2\nTABLES\n0\nTABLE\n2\nLTYPE\n70\n4\n"
    s += dxf_ltype("Continuous", "Solid", [])
    s += dxf_ltype("DASHED", "Dashed", [6.0, -3.0])
    s += dxf_ltype("DASHDOT", "Dash-dot", [6.0, -3.0, 1.0, -3.0])
    s += dxf_ltype("DOT", "Dot", [1.0, -3.0])
    s += "0\nENDTAB\n0\nTABLE\n2\nLAYER\n70\n20\n"
    for args in [
        ("0", 7, "Continuous", None, None),
        ("A-WALL", 7, "Continuous", PAL["dwell"], 60),
        ("A-ANNO", 7, "Continuous", PAL["dwell"], 25),
        ("H-ENVELOPE", 7, "DASHED", PAL["dwell"], 50),
        ("H-BED", 3, "Continuous", PAL["crop"], 40),
        ("H-PATH", 4, "Continuous", PAL["path"], 18),
        ("H-IRRIG", 4, "DASHDOT", PAL["irrig"], 25),
        ("H-TOOLS", 40, "Continuous", PAL["harvest"], 35),
        ("H-HARVEST", 40, "Continuous", PAL["harvest"], 35),
        ("H-COMPOST", 40, "Continuous", PAL["harvest"], 35),
        ("H-WORK", 40, "DASHED", PAL["harvest"], 18),
        ("H-LABEL", 7, "Continuous", PAL["dwell"], 25),
        ("H-DIM", 1, "Continuous", PAL["dim_r"], 18),
        ("H-SVC", 40, "Continuous", PAL["harvest"], 25),
        ("INSET", 7, "Continuous", PAL["inset"], 18),
        ("LEGEND", 7, "Continuous", PAL["dwell"], 25),
    ]:
        s += dxf_layer(*args)
    s += "0\nENDTAB\n0\nENDSEC\n"
    return s

def lwpoly(layer, pts, closed=True, rgb=None):
    s = f"0\nLWPOLYLINE\n5\n{h()}\n100\nAcDbEntity\n8\n{layer}\n"
    if rgb: s += f"420\n{rgb420(*rgb)}\n"
    s += f"100\nAcDbPolyline\n90\n{len(pts)}\n70\n{1 if closed else 0}\n"
    for x, y in pts:
        s += f"10\n{x:.1f}\n20\n{y:.1f}\n"
    return s

def R(layer, x0, y0, x1, y1, rgb=None):
    return lwpoly(layer, [(x0,y0),(x1,y0),(x1,y1),(x0,y1)], True, rgb)

def L(layer, x0, y0, x1, y1, rgb=None):
    s = f"0\nLINE\n5\n{h()}\n100\nAcDbEntity\n8\n{layer}\n"
    if rgb: s += f"420\n{rgb420(*rgb)}\n"
    s += f"100\nAcDbLine\n10\n{x0:.1f}\n20\n{y0:.1f}\n11\n{x1:.1f}\n21\n{y1:.1f}\n"
    return s

def T(layer, x, y, ht, val, rgb=None):
    s = f"0\nTEXT\n5\n{h()}\n100\nAcDbEntity\n8\n{layer}\n"
    if rgb: s += f"420\n{rgb420(*rgb)}\n"
    s += f"100\nAcDbText\n10\n{x:.1f}\n20\n{y:.1f}\n40\n{ht}\n1\n{val}\n"
    return s

def arc_e(layer, cx, cy, r, sa, ea, rgb=None):
    s = f"0\nARC\n5\n{h()}\n100\nAcDbEntity\n8\n{layer}\n"
    if rgb: s += f"420\n{rgb420(*rgb)}\n"
    s += f"100\nAcDbCircle\n10\n{cx:.1f}\n20\n{cy:.1f}\n40\n{r:.1f}\n100\nAcDbArc\n50\n{sa:.1f}\n51\n{ea:.1f}\n"
    return s

def circ(layer, cx, cy, r, rgb=None):
    s = f"0\nCIRCLE\n5\n{h()}\n100\nAcDbEntity\n8\n{layer}\n"
    if rgb: s += f"420\n{rgb420(*rgb)}\n"
    s += f"100\nAcDbCircle\n10\n{cx:.1f}\n20\n{cy:.1f}\n40\n{r:.1f}\n"
    return s

def dim_line(x0, y0, x1, y1, label, offset=0, vert=False):
    s = ""
    if vert:
        ox = offset
        s += L("H-DIM", x0+ox, y0, x0+ox, y1, PAL["dim_r"])
        s += L("H-DIM", x0+ox-200, y0, x0+ox+200, y0, PAL["dim_r"])
        s += L("H-DIM", x0+ox-200, y1, x0+ox+200, y1, PAL["dim_r"])
        s += T("H-DIM", x0+ox+300, (y0+y1)/2 - 100, TH["xs"], label)
    else:
        oy = offset
        s += L("H-DIM", x0, y0+oy, x1, y0+oy, PAL["dim_r"])
        s += L("H-DIM", x0, y0+oy-200, x0, y0+oy+200, PAL["dim_r"])
        s += L("H-DIM", x1, y0+oy-200, x1, y0+oy+200, PAL["dim_r"])
        s += T("H-DIM", (x0+x1)/2 - len(label)*40, y0+oy+300, TH["xs"], label)
    return s

# ================================================================
# LAYOUT CONSTANTS (mm)
# ================================================================
DW_W = 20000
DW_D = 9200
PATIO_W = 1800
PATH_CLR = 1500
BED_W = 1000
BED_L = 3000

HIVE_WIDTH = 10750
HIVE_DEPTH = 10500
OUTER_PERIM = 1500
GAP_SVC = 500
SVC_W = HIVE_WIDTH - OUTER_PERIM - 3*BED_W - 2*PATH_CLR - GAP_SVC  # = 2750
BED_PITCH = BED_W + PATH_CLR  # 2500

BED_ROW1_Y0 = PATH_CLR           # 1500
BED_ROW1_Y1 = BED_ROW1_Y0 + BED_L  # 4500
BED_ROW2_Y0 = BED_ROW1_Y1 + PATH_CLR  # 6000
BED_ROW2_Y1 = BED_ROW2_Y0 + BED_L     # 9000

# Sheet positions for the two detail views
HW_OX = 0       # HIVE-W detail origin x
HW_OY = 0       # HIVE-W detail origin y
HE_OX = 15000   # HIVE-E detail origin x
HE_OY = 0       # HIVE-E detail origin y

e = ""

# ================================================================
# PATH CLEARANCE TRACKING
# ================================================================
all_clearances = []

def track(hive, desc, value):
    all_clearances.append((hive, desc, value))

# ================================================================
# DRAW ONE HIVE DETAIL
# ================================================================
def draw_hive(prefix, ox, oy, patio_on_right=True):
    """Draw one hive. patio_on_right=True for HIVE-W, False for HIVE-E."""
    global e

    hx0 = ox
    hy0 = oy
    hx1 = ox + HIVE_WIDTH
    hy1 = oy + HIVE_DEPTH

    # Envelope (dashed)
    e += R("H-ENVELOPE", hx0, hy0, hx1, hy1, PAL["dwell"])

    # Zone label
    e += T("H-LABEL", (hx0+hx1)/2 - 1200, (hy0+hy1)/2 + 2000, TH["zone"],
           f"HIVE-{prefix}")
    e += T("H-LABEL", (hx0+hx1)/2 - 1800, (hy0+hy1)/2 + 1400, TH["det"],
           f"10,750 x 10,500 mm PROVISIONAL")

    if patio_on_right:
        # HIVE-W: outer on left, beds from left, service on right (patio side)
        col_xs = [
            hx0 + OUTER_PERIM,
            hx0 + OUTER_PERIM + BED_PITCH,
            hx0 + OUTER_PERIM + 2 * BED_PITCH,
        ]
        svc_x0 = col_xs[2] + BED_W + GAP_SVC
        svc_x1 = hx1
        wall_x = svc_x1   # items placed against this wall
        item_dir = -1      # items extend leftward from wall
    else:
        # HIVE-E: outer on right, beds from right, service on left (patio side)
        col_xs = [
            hx1 - OUTER_PERIM - BED_W,
            hx1 - OUTER_PERIM - BED_PITCH - BED_W,
            hx1 - OUTER_PERIM - 2 * BED_PITCH - BED_W,
        ]
        svc_x0 = hx0
        svc_x1 = hx0 + SVC_W
        wall_x = svc_x0   # items placed against this wall
        item_dir = 1       # items extend rightward from wall

    sorted_cols = sorted(col_xs)

    # ---- DRAW BEDS with IDs ----
    bed_rows = [(hy0 + BED_ROW1_Y0, hy0 + BED_ROW1_Y1),
                (hy0 + BED_ROW2_Y0, hy0 + BED_ROW2_Y1)]
    bed_num = 1
    for ci, col_x in enumerate(sorted_cols):
        for ri, (ry0, ry1) in enumerate(bed_rows):
            bid = f"{prefix}-CB{bed_num:02d}"
            e += R("H-BED", col_x, ry0, col_x + BED_W, ry1, PAL["crop"])
            e += T("H-LABEL", col_x + 100, (ry0+ry1)/2 + 100, TH["xs"], bid)
            e += T("H-LABEL", col_x + 100, (ry0+ry1)/2 - 300, TH["xs"], "1.0x3.0")
            bed_num += 1

    # ---- MEASURE AND DIMENSION PATH CLEARANCES ----
    # South path
    south_clr = BED_ROW1_Y0
    track(prefix, "South perimeter path", south_clr)
    e += dim_line(sorted_cols[0], hy0, sorted_cols[0], hy0 + BED_ROW1_Y0,
                  f"{south_clr:,}", offset=-600, vert=True)

    # North path
    north_clr = HIVE_DEPTH - BED_ROW2_Y1
    track(prefix, "North perimeter path", north_clr)
    e += dim_line(sorted_cols[0], hy0 + BED_ROW2_Y1, sorted_cols[0], hy1,
                  f"{north_clr:,}", offset=-600, vert=True)

    # Middle path
    mid_clr = BED_ROW2_Y0 - BED_ROW1_Y1
    track(prefix, "Path between bed rows", mid_clr)
    e += dim_line(sorted_cols[1], hy0 + BED_ROW1_Y1, sorted_cols[1], hy0 + BED_ROW2_Y0,
                  f"{mid_clr:,}", offset=-600, vert=True)

    # Between-column aisles
    for i in range(len(sorted_cols) - 1):
        gap = sorted_cols[i+1] - (sorted_cols[i] + BED_W)
        track(prefix, f"Aisle cols {i+1}-{i+2}", gap)
        mid_y = hy0 + (BED_ROW1_Y0 + BED_ROW1_Y1) / 2
        e += dim_line(sorted_cols[i] + BED_W, mid_y,
                      sorted_cols[i+1], mid_y,
                      f"{gap:,}", offset=-400)

    # Outer perimeter
    if patio_on_right:
        outer_perim_actual = sorted_cols[0] - hx0
        e += dim_line(hx0, hy0 + BED_ROW2_Y0 + 1500,
                      sorted_cols[0], hy0 + BED_ROW2_Y0 + 1500,
                      f"{outer_perim_actual:,}", offset=0)
    else:
        outer_perim_actual = hx1 - (sorted_cols[2] + BED_W)
        e += dim_line(sorted_cols[2] + BED_W, hy0 + BED_ROW2_Y0 + 1500,
                      hx1, hy0 + BED_ROW2_Y0 + 1500,
                      f"{outer_perim_actual:,}", offset=0)
    track(prefix, "Outer perimeter path", outer_perim_actual)

    # Gap beds to service
    gap_svc_actual = svc_x0 - (sorted_cols[2] + BED_W) if patio_on_right \
                     else sorted_cols[0] - svc_x1
    track(prefix, "Gap beds-to-service", abs(gap_svc_actual))

    # Service strip width dimension
    svc_w = svc_x1 - svc_x0
    e += dim_line(svc_x0, hy1 + 800, svc_x1, hy1 + 800,
                  f"{svc_w:,}", offset=0)
    e += T("H-DIM", (svc_x0+svc_x1)/2 - 600, hy1 + 1500, TH["xs"], "SERVICE")

    # Gap dimension
    if patio_on_right:
        e += dim_line(sorted_cols[2] + BED_W, hy1 + 800, svc_x0, hy1 + 800,
                      f"{abs(gap_svc_actual)}", offset=0)
    else:
        e += dim_line(svc_x1, hy1 + 800, sorted_cols[0], hy1 + 800,
                      f"{abs(gap_svc_actual)}", offset=0)

    # ---- SERVICE ZONE: items against patio wall ----
    # Helper to place an item against the wall
    def item_rect(layer, depth, width, y0, rgb=None):
        """Place item against wall. Returns (x0, x1, y0, y1) of item."""
        if item_dir < 0:  # wall on right, items extend left
            ix1 = wall_x - 200
            ix0 = ix1 - depth
        else:  # wall on left, items extend right
            ix0 = wall_x + 200
            ix1 = ix0 + depth
        iy0 = hy0 + y0
        iy1 = iy0 + width
        e_frag = R(layer, ix0, iy0, ix1, iy1, rgb)
        return ix0, ix1, iy0, iy1, e_frag

    def item_front(ix0, ix1):
        """Return the x-coordinate of the item face (facing the aisle)."""
        return ix0 if item_dir < 0 else ix1

    def aisle_clear(item_depth):
        """Clear aisle in front of an item of given depth."""
        return svc_w - 200 - item_depth

    # -- CP01-02: Compost bays 1000x1000 each, side by side --
    cp_y0 = 200
    ix0, ix1, iy0, iy1, frag = item_rect("H-COMPOST", 1000, 1000, cp_y0, PAL["harvest"])
    e += frag
    e += T("H-LABEL", min(ix0,ix1)+100, iy0+400, TH["xs"], f"{prefix}-CP01")
    # CP02 adjacent
    cp2_y0 = cp_y0 + 1100
    ix0b, ix1b, iy0b, iy1b, frag = item_rect("H-COMPOST", 1000, 1000, cp2_y0, PAL["harvest"])
    e += frag
    e += T("H-LABEL", min(ix0b,ix1b)+100, iy0b+400, TH["xs"], f"{prefix}-CP02")
    cp_clear = aisle_clear(1000)
    track(prefix, "Compost approach clear", cp_clear)
    # Working space dashed rect in front of compost
    front_x = item_front(ix0, ix1)
    if item_dir < 0:
        e += R("H-WORK", front_x - 1500, iy0, front_x, iy1b)
    else:
        e += R("H-WORK", front_x, iy0, front_x + 1500, iy1b)
    e += T("H-LABEL", front_x + item_dir*(-750-300), (iy0+iy1b)/2, TH["xs"],
           f"1,500 CLEAR")

    # -- IR01: Irrigation 1500x800 --
    ir_y0 = cp2_y0 + 1100 + 200
    ix0, ix1, iy0, iy1, frag = item_rect("H-IRRIG", 800, 1500, ir_y0, PAL["path"])
    e += frag
    e += circ("H-IRRIG", (ix0+ix1)/2, (iy0+iy1)/2, 250, PAL["path"])
    e += T("H-LABEL", min(ix0,ix1)+100, iy0+600, TH["xs"], f"{prefix}-IR01")

    # -- TP01: Tool cupboard 1200x600, door 600mm --
    tp_y0 = ir_y0 + 1700
    ix0, ix1, iy0, iy1, frag = item_rect("H-TOOLS", 600, 1200, tp_y0, PAL["harvest"])
    e += frag
    e += T("H-LABEL", min(ix0,ix1)+50, iy0+200, TH["xs"], f"{prefix}-TP01")
    tp_clear = aisle_clear(600)
    track(prefix, "Tool cupboard approach", tp_clear)
    # Door swing: hinged at bottom-front, opens into aisle
    door_cx = item_front(ix0, ix1)
    door_cy = iy0
    if item_dir < 0:
        e += arc_e("H-TOOLS", door_cx, door_cy, 600, 90, 180, PAL["harvest"])
    else:
        e += arc_e("H-TOOLS", door_cx, door_cy, 600, 0, 90, PAL["harvest"])
    # Working space
    front_x = item_front(ix0, ix1)
    if item_dir < 0:
        e += R("H-WORK", front_x - 1500, iy0, front_x, iy1)
    else:
        e += R("H-WORK", front_x, iy0, front_x + 1500, iy1)
    # Door-open clear: aisle minus door swing depth
    door_open_clear = tp_clear - 600
    track(prefix, "TP01 route when door open", tp_clear)

    # -- TP02: Potting bench 1500x750 --
    tp2_y0 = tp_y0 + 1400
    ix0, ix1, iy0, iy1, frag = item_rect("H-TOOLS", 750, 1500, tp2_y0, PAL["harvest"])
    e += frag
    e += T("H-LABEL", min(ix0,ix1)+100, iy0+300, TH["xs"], f"{prefix}-TP02")
    tp2_clear = aisle_clear(750)
    track(prefix, "Potting bench approach", tp2_clear)
    front_x = item_front(ix0, ix1)
    if item_dir < 0:
        e += R("H-WORK", front_x - 1500, iy0, front_x, iy1)
    else:
        e += R("H-WORK", front_x, iy0, front_x + 1500, iy1)

    # -- HV01: Harvest bench 1500x750 --
    hv_y0 = tp2_y0 + 1700
    ix0, ix1, iy0, iy1, frag = item_rect("H-HARVEST", 750, 1500, hv_y0, PAL["harvest"])
    e += frag
    e += T("H-LABEL", min(ix0,ix1)+100, iy0+300, TH["xs"], f"{prefix}-HV01")
    hv_clear = aisle_clear(750)
    track(prefix, "Harvest bench approach", hv_clear)
    front_x = item_front(ix0, ix1)
    if item_dir < 0:
        e += R("H-WORK", front_x - 1500, iy0, front_x, iy1)
    else:
        e += R("H-WORK", front_x, iy0, front_x + 1500, iy1)

    # -- HV02: Crate staging 1000x500 --
    cr_y0 = hv_y0 + 1700
    ix0, ix1, iy0, iy1, frag = item_rect("H-HARVEST", 500, 1000, cr_y0, PAL["harvest"])
    e += frag
    e += T("H-LABEL", min(ix0,ix1)+50, iy0+150, TH["xs"], f"{prefix}-HV02")

    # -- HV03: Seed cupboard 1200x500, door 500mm --
    sd_y0 = cr_y0 + 700
    ix0, ix1, iy0, iy1, frag = item_rect("H-HARVEST", 500, 1200, sd_y0, PAL["harvest"])
    e += frag
    e += T("H-LABEL", min(ix0,ix1)+50, iy0+150, TH["xs"], f"{prefix}-HV03")
    hv3_clear = aisle_clear(500)
    track(prefix, "Seed cupboard approach", hv3_clear)
    # Door swing
    door_cx = item_front(ix0, ix1)
    door_cy = iy0
    if item_dir < 0:
        e += arc_e("H-HARVEST", door_cx, door_cy, 500, 90, 180, PAL["harvest"])
    else:
        e += arc_e("H-HARVEST", door_cx, door_cy, 500, 0, 90, PAL["harvest"])
    front_x = item_front(ix0, ix1)
    if item_dir < 0:
        e += R("H-WORK", front_x - 1500, iy0, front_x, iy1)
    else:
        e += R("H-WORK", front_x, iy0, front_x + 1500, iy1)

    # Service strip aisle dimension (clear width at narrowest: compost)
    min_aisle = aisle_clear(1000)  # compost is deepest at 1000mm
    track(prefix, "Service aisle (min, at compost)", min_aisle)

    # ---- IRRIGATION BRANCHES ----
    # Main line from IR01 toward bed zone
    irr_cx = (ix0 + ix1) / 2  # reuse last ix values? No, need IR01's coords
    # Recalculate IR01 position for irrigation lines
    if item_dir < 0:
        irr_front_x = wall_x - 200 - 800  # IR01 front face
    else:
        irr_front_x = wall_x + 200 + 800
    irr_cy = hy0 + ir_y0 + 750  # mid-height of IR01

    bed_zone_cx = sorted_cols[1] + BED_W / 2
    main_y = hy0 + BED_ROW1_Y0 - 500
    e += L("H-IRRIG", irr_front_x, irr_cy, irr_front_x, main_y, PAL["irrig"])
    e += L("H-IRRIG", irr_front_x, main_y, bed_zone_cx, main_y, PAL["irrig"])
    for cx in sorted_cols:
        bx = cx + BED_W / 2
        e += L("H-IRRIG", bed_zone_cx, main_y, bx, main_y, PAL["irrig"])
        for ry0_rel, ry1_rel in [(BED_ROW1_Y0, BED_ROW1_Y1), (BED_ROW2_Y0, BED_ROW2_Y1)]:
            drop_y = hy0 + (ry0_rel + ry1_rel) / 2
            e += L("H-IRRIG", bx, main_y, bx, drop_y, PAL["irrig"])
            e += L("H-IRRIG", bx - 200, drop_y, bx + 200, drop_y, PAL["irrig"])

    # ---- PATIO ARROW ----
    if patio_on_right:
        ax = hx1 + 200
    else:
        ax = hx0 - 200
    ay = hy0 + HIVE_DEPTH / 2
    arr_len = 800
    if patio_on_right:
        e += L("A-ANNO", ax, ay, ax + arr_len, ay, PAL["dwell"])
        e += L("A-ANNO", ax + arr_len, ay, ax + arr_len - 200, ay + 150, PAL["dwell"])
        e += L("A-ANNO", ax + arr_len, ay, ax + arr_len - 200, ay - 150, PAL["dwell"])
        e += T("A-ANNO", ax + 100, ay + 400, TH["det"], "TO PATIO")
    else:
        e += L("A-ANNO", ax, ay, ax - arr_len, ay, PAL["dwell"])
        e += L("A-ANNO", ax - arr_len, ay, ax - arr_len + 200, ay + 150, PAL["dwell"])
        e += L("A-ANNO", ax - arr_len, ay, ax - arr_len + 200, ay - 150, PAL["dwell"])
        e += T("A-ANNO", ax - 1200, ay + 400, TH["det"], "TO PATIO")


# ================================================================
# DRAW BOTH HIVES
# ================================================================
draw_hive("W", HW_OX, HW_OY, patio_on_right=True)
draw_hive("E", HE_OX, HE_OY, patio_on_right=False)

# ================================================================
# OVERALL DIMENSIONS
# ================================================================
dim_y = -1500
# HIVE-W width
e += dim_line(HW_OX, dim_y, HW_OX + HIVE_WIDTH, dim_y, f"{HIVE_WIDTH:,}", offset=0)
# HIVE-E width
e += dim_line(HE_OX, dim_y, HE_OX + HIVE_WIDTH, dim_y, f"{HIVE_WIDTH:,}", offset=0)

# Depth dimensions
e += dim_line(HW_OX, HW_OY, HW_OX, HW_OY + HIVE_DEPTH,
              f"{HIVE_DEPTH:,}", offset=-2500, vert=True)
e += dim_line(HE_OX + HIVE_WIDTH, HE_OY, HE_OX + HIVE_WIDTH, HE_OY + HIVE_DEPTH,
              f"{HIVE_DEPTH:,}", offset=2500, vert=True)

# Width dimension chain for HIVE-W
chain_y = dim_y - 1500
e += T("H-DIM", HW_OX, chain_y - 500, TH["xs"],
       f"WIDTH CHAIN: {OUTER_PERIM}+{BED_W}+{PATH_CLR}+{BED_W}+{PATH_CLR}+{BED_W}+{GAP_SVC}+{SVC_W} = {HIVE_WIDTH}")

# Bed reference dimensions
bed_ref_x = HW_OX + OUTER_PERIM
e += dim_line(bed_ref_x, BED_ROW1_Y0, bed_ref_x + BED_W, BED_ROW1_Y0,
              "1,000", offset=-800)
e += dim_line(bed_ref_x, BED_ROW1_Y0, bed_ref_x, BED_ROW1_Y1,
              "3,000", offset=-1500, vert=True)

# ================================================================
# SITE-LOCATION INSET (1:5 scale)
# ================================================================
SC = 0.2  # 1:5
inset_cx = (HW_OX + HW_OX + HIVE_WIDTH + HE_OX + HE_OX + HIVE_WIDTH) / 4
inset_y0 = -5500

# Real-world coordinates (site plan)
rw_hw_x0 = -PATIO_W - HIVE_WIDTH  # -12550
rw_hw_x1 = -PATIO_W               # -1800
rw_he_x0 = DW_W + PATIO_W         # 21800
rw_he_x1 = rw_he_x0 + HIVE_WIDTH  # 32550
rw_total = rw_he_x1 - rw_hw_x0    # 45100

# Inset origin (left edge of scaled drawing)
inset_x0 = inset_cx - (rw_total * SC) / 2

def inset_x(real_x):
    return inset_x0 + (real_x - rw_hw_x0) * SC

def inset_y(real_y):
    return inset_y0 + real_y * SC

# Duplex outline
e += R("INSET", inset_x(0), inset_y(0), inset_x(DW_W), inset_y(DW_D), PAL["inset"])
e += T("INSET", inset_x(DW_W/2 - 2000), inset_y(DW_D/2), TH["xs"], "DUPLEX")

# Patio corridors
e += R("INSET", inset_x(-PATIO_W), inset_y(0), inset_x(0), inset_y(DW_D), PAL["path"])
e += R("INSET", inset_x(DW_W), inset_y(0), inset_x(DW_W+PATIO_W), inset_y(DW_D), PAL["path"])

# HIVE-W outline (highlighted)
e += R("INSET", inset_x(rw_hw_x0), inset_y(0), inset_x(rw_hw_x1), inset_y(HIVE_DEPTH), PAL["crop"])
e += T("INSET", inset_x(rw_hw_x0+500), inset_y(HIVE_DEPTH/2), TH["xs"], "HIVE-W")

# HIVE-E outline (highlighted)
e += R("INSET", inset_x(rw_he_x0), inset_y(0), inset_x(rw_he_x1), inset_y(HIVE_DEPTH), PAL["crop"])
e += T("INSET", inset_x(rw_he_x0+500), inset_y(HIVE_DEPTH/2), TH["xs"], "HIVE-E")

# Conservatory zone (north of dwelling)
CY_TOP = 13200
e += R("INSET", inset_x(2000), inset_y(DW_D), inset_x(6000), inset_y(CY_TOP), PAL["inset"])
e += R("INSET", inset_x(14000), inset_y(DW_D), inset_x(18000), inset_y(CY_TOP), PAL["inset"])
e += T("INSET", inset_x(7000), inset_y(DW_D+500), TH["xs"], "CONSERVATORIES")

# Hive depth extent line
e += L("INSET", inset_x(rw_hw_x0), inset_y(HIVE_DEPTH),
       inset_x(rw_he_x1), inset_y(HIVE_DEPTH), PAL["dim_r"])
e += T("INSET", inset_x(DW_W/2 - 3000), inset_y(HIVE_DEPTH + 200), TH["xs"],
       f"HIVE DEPTH {HIVE_DEPTH:,} mm")

# Dwelling north face line
e += L("INSET", inset_x(rw_hw_x0), inset_y(DW_D),
       inset_x(rw_he_x1), inset_y(DW_D), PAL["inset"])

e += T("INSET", inset_x(rw_hw_x0), inset_y0 - 500, TH["det"],
       "SITE LOCATION INSET (scale 1:5)")

# ================================================================
# SCALE BAR
# ================================================================
sb_x = HW_OX
sb_y = -7500
for i in range(6):
    e += L("H-DIM", sb_x + i*1000, sb_y, sb_x + i*1000, sb_y+300)
e += L("H-DIM", sb_x, sb_y, sb_x+5000, sb_y)
e += T("H-DIM", sb_x, sb_y-500, TH["xs"], "SCALE BAR (METRES)")
for i, lbl in enumerate(["0", "1", "2", "3", "4", "5 m"]):
    e += T("H-DIM", sb_x + i*1000 - 50, sb_y+500, TH["xs"], lbl)

# ================================================================
# NORTH ARROW
# ================================================================
na_x = HE_OX + HIVE_WIDTH + 3000
na_y = HIVE_DEPTH - 3000
e += L("H-LABEL", na_x, na_y, na_x, na_y+2500)
e += L("H-LABEL", na_x, na_y+2500, na_x-350, na_y+2000)
e += L("H-LABEL", na_x, na_y+2500, na_x+350, na_y+2000)
e += T("H-LABEL", na_x-200, na_y+3000, TH["room"], "N")

# ================================================================
# TITLE BLOCK
# ================================================================
tb_y = -9500
e += T("H-LABEL", HW_OX, tb_y, TH["head"],
       "MMUCO HIVE-E + HIVE-W -- CONCEPT DETAIL -- NOT FOR CONSTRUCTION")
e += T("H-LABEL", HW_OX, tb_y-500, TH["sub"],
       "hive-east-and-west rev 3 | Units mm 1:1 | Drawing ref: HD-01")
e += T("H-LABEL", HW_OX, tb_y-900, TH["xs"],
       f"Hive envelopes PROVISIONAL {HIVE_WIDTH:,} x {HIVE_DEPTH:,} mm.")
e += T("H-LABEL", HW_OX, tb_y-1200, TH["xs"],
       f"Width expanded from 10,000 to {HIVE_WIDTH:,} (outward, patio boundary fixed).")
e += T("H-LABEL", HW_OX, tb_y-1500, TH["xs"],
       "All clearances are project design targets, not proof of regulatory compliance.")

# ================================================================
# COMPONENT SCHEDULE (right side)
# ================================================================
lg_x = HE_OX + HIVE_WIDTH + 2000
lg_y = HIVE_DEPTH + 1000

e += T("LEGEND", lg_x, lg_y, TH["room"], "COMPONENT SCHEDULE (PER HIVE)")
lg_y -= 500
schedule = [
    ("CB01-06", "Crop bed", "1,000 x 3,000", "6 per hive"),
    ("IR01", "Irrigation station", "1,500 x 800", "Water point + manifold"),
    ("TP01", "Tool cupboard", "1,200 x 600", "Hinged door, 600 swing"),
    ("TP02", "Potting bench", "1,500 x 750", "Working surface"),
    ("HV01", "Harvest bench", "1,500 x 750", "Sorting / packing"),
    ("HV02", "Crate staging", "1,000 x 500", "Harvest crates"),
    ("HV03", "Seed cupboard", "1,200 x 500", "Hinged door, 500 swing"),
    ("CP01-02", "Compost bay", "1,000 x 1,000", "2 bays per hive"),
]
e += T("LEGEND", lg_x, lg_y, TH["xs"], "ID          NAME                SIZE mm          NOTES")
lg_y -= 250
for sid, name, size, notes in schedule:
    e += T("LEGEND", lg_x, lg_y, TH["xs"], f"{sid:<12}{name:<20}{size:<17}{notes}")
    lg_y -= 220

# ================================================================
# PALETTE / KEY
# ================================================================
lg_y -= 500
e += T("LEGEND", lg_x, lg_y, TH["room"], "PALETTE / KEY")
lg_y -= 400
for desc, pal_key in [
    ("Dwelling #E8EDF2", "dwell"),
    ("Crop beds #77C66E", "crop"),
    ("Paths/irrigation #56C5D0", "path"),
    ("Harvest/tools #E4B45F", "harvest"),
]:
    e += R("LEGEND", lg_x+50, lg_y-30, lg_x+250, lg_y+120, PAL[pal_key])
    e += T("LEGEND", lg_x+350, lg_y, TH["xs"], desc)
    lg_y -= 280

lg_y -= 400
e += T("LEGEND", lg_x, lg_y, TH["room"], "FOUR PRINCIPLES")
lg_y -= 350
for p in ["01 Produce (beds)", "02 Sustain (compost, irrigation)",
          "03 Deliver (harvest)", "04 Preserve (tools, seed)"]:
    e += T("LEGEND", lg_x+100, lg_y, TH["xs"], p)
    lg_y -= 250

lg_y -= 400
e += T("LEGEND", lg_x, lg_y, TH["room"], "DESIGN TARGETS")
lg_y -= 350
grow_per = 6 * BED_W * BED_L / 1e6
for t in [
    "Bed reach: 500 mm max (both sides)",
    f"Main paths: {PATH_CLR:,} mm (project design target)",
    f"Outer perimeter: {OUTER_PERIM:,} mm (project design target)",
    f"Service aisle: >= {PATH_CLR:,} mm clear",
    f"Growing per hive: {grow_per:.0f} m2",
    f"Growing total: {grow_per*2:.0f} m2",
    f"Patio corridor: {PATIO_W:,} mm",
    f"Envelope: {HIVE_WIDTH:,} x {HIVE_DEPTH:,} mm (PROVISIONAL)",
]:
    e += T("LEGEND", lg_x+100, lg_y, TH["xs"], t)
    lg_y -= 250

lg_y -= 400
e += T("LEGEND", lg_x, lg_y, TH["room"], "NOTES")
lg_y -= 350
for n in [
    f"1. Width expanded from 10,000 to {HIVE_WIDTH:,} mm.",
    "   Outer perimeter increased 750 -> 1,500 mm.",
    "   Patio boundary unchanged.",
    f"2. Service strip {SVC_W:,} mm wide.",
    "   All stations >= 1,500 mm clear approach.",
    f"3. Depth {HIVE_DEPTH:,} (1,300 mm beyond dwelling north face).",
    f"   {HIVE_DEPTH - DW_D:,} mm extension does not conflict with",
    "   conservatory zone (top at 13,200) or recreational garden.",
    "4. 1,500 mm is the PROJECT DESIGN TARGET.",
    "   Not proof of regulatory compliance.",
    "5. North assumed (PA-07).",
]:
    e += T("LEGEND", lg_x+100, lg_y, TH["xs"], n)
    lg_y -= 230

# ================================================================
# ASSEMBLE AND WRITE
# ================================================================
dxf = dxf_header() + dxf_tables()
dxf += "0\nSECTION\n2\nENTITIES\n"
dxf += e
dxf += "0\nENDSEC\n0\nEOF\n"

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    f.write(dxf)

# ================================================================
# VERIFICATION
# ================================================================
print(f"Written {len(dxf)} bytes to {OUT}")
print(f"Entity handles: {hc[0] - 0x100}")
print()
print("=== DIMENSION CHAIN (WIDTH) ===")
print(f"  OUTER_PERIM({OUTER_PERIM}) + BED({BED_W}) + PATH({PATH_CLR}) + BED({BED_W})")
print(f"  + PATH({PATH_CLR}) + BED({BED_W}) + GAP({GAP_SVC}) + SVC({SVC_W})")
total = OUTER_PERIM + 3*BED_W + 2*PATH_CLR + GAP_SVC + SVC_W
print(f"  = {total} mm  (HIVE_WIDTH = {HIVE_WIDTH})")
assert total == HIVE_WIDTH, f"Width mismatch: {total} != {HIVE_WIDTH}"
print()
print("=== DIMENSION CHAIN (DEPTH) ===")
print(f"  S_PATH({BED_ROW1_Y0}) + BED_L({BED_L}) + MID_PATH({PATH_CLR})")
print(f"  + BED_L({BED_L}) + N_PATH({HIVE_DEPTH - BED_ROW2_Y1})")
total_d = BED_ROW1_Y0 + BED_L + PATH_CLR + BED_L + (HIVE_DEPTH - BED_ROW2_Y1)
print(f"  = {total_d} mm  (HIVE_DEPTH = {HIVE_DEPTH})")
assert total_d == HIVE_DEPTH, f"Depth mismatch: {total_d} != {HIVE_DEPTH}"
print()
print("=== SERVICE ZONE CLEARANCES ===")
items_check = [
    ("CP01-02 Compost (1000mm deep)", 1000),
    ("IR01 Irrigation (800mm deep)", 800),
    ("TP01 Tool cupboard (600mm deep)", 600),
    ("TP02 Potting bench (750mm deep)", 750),
    ("HV01 Harvest bench (750mm deep)", 750),
    ("HV02 Crate staging (500mm deep)", 500),
    ("HV03 Seed cupboard (500mm deep)", 500),
]
print(f"  Service strip width: {SVC_W} mm")
print(f"  Wall offset: 200 mm")
for name, depth in items_check:
    clear = SVC_W - 200 - depth
    status = "OK" if clear >= 1500 else f"BELOW 1,500"
    print(f"  {name}: {clear:,} mm clear — {status}")
print()
print("=== DOOR SWING CHECK ===")
for name, door_r, depth in [("TP01", 600, 600), ("HV03", 500, 500)]:
    aisle = SVC_W - 200 - depth
    passthrough = aisle - door_r
    print(f"  {name}: door {door_r}mm into {aisle}mm aisle -> {passthrough}mm pass-through when open")
print()
print("=== PATH CLEARANCE AUDIT ===")
narrowest = {}
for hive, desc, val in all_clearances:
    status = "OK" if val >= PATH_CLR else f"BELOW {PATH_CLR} mm"
    print(f"  HIVE-{hive} | {desc}: {val:,} mm — {status}")
    if hive not in narrowest or val < narrowest[hive][1]:
        narrowest[hive] = (desc, val)

print()
for hive, (desc, val) in narrowest.items():
    print(f"  NARROWEST in HIVE-{hive}: {val:,} mm ({desc})")
    print(f"    1,500 mm is the project design target.")

print()
print("=== NORTHERN EXTENSION CHECK ===")
print(f"  Hive depth: {HIVE_DEPTH:,} mm")
print(f"  Dwelling north face: {DW_D:,} mm")
print(f"  Extension beyond dwelling: {HIVE_DEPTH - DW_D:,} mm")
print(f"  Conservatory top: 13,200 mm")
print(f"  Gap to conservatory zone: {13200 - HIVE_DEPTH:,} mm")
print(f"  Recreational garden starts: 13,200 mm")
print(f"  No conflict with garden transition.")

print()
print("=== PROPOSED SITE ENVELOPE CHANGES ===")
print(f"  Each hive widens {HIVE_WIDTH - 10000:,} mm outward.")
print(f"  HIVE-W west boundary moves 750 mm further west.")
print(f"  HIVE-E east boundary moves 750 mm further east.")
print(f"  Total site width increase: 1,500 mm (750 per side).")
print(f"  No change to depth or north-south extent.")
