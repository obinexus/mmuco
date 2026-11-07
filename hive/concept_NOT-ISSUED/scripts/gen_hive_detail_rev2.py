"""Generate MMUCO HIVE-E + HIVE-W concept detail DXF (rev 2).

Enlarged detail views of both hives. Duplex shown as outline only
with "TO DUPLEX" arrows. All paths measured and dimensioned.

Envelope enlarged from 10,000 x 9,200 to 10,000 x 10,500 to achieve
1,500 mm paths on all sides of all beds. Perimeter path along outer
bed columns is 750 mm (flagged as constraint — see NOTES).

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
        ("PATIO", 4, "Continuous", PAL["path"], 25),
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
    """Draw a dimension with ticks and label."""
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

# ENVELOPE: enlarged depth to 10,500 to fit 1500mm paths N+S of beds
HIVE_WIDTH = 10000
HIVE_DEPTH = 10500

# Hive X coordinates
HW_X0 = -PATIO_W - HIVE_WIDTH   # -11800
HW_X1 = -PATIO_W                # -1800
HE_X0 = DW_W + PATIO_W          # 21800
HE_X1 = HE_X0 + HIVE_WIDTH      # 31800

PX = DW_W / 2

# Bed grid layout within each hive
# 3 cols x 2 rows, beds 1000w x 3000h
# Height: 1500 + 3000 + 1500 + 3000 + 1500 = 10500 ✓
BED_ROW1_Y0 = PATH_CLR                     # 1500
BED_ROW1_Y1 = BED_ROW1_Y0 + BED_L          # 4500
BED_ROW2_Y0 = BED_ROW1_Y1 + PATH_CLR       # 6000
BED_ROW2_Y1 = BED_ROW2_Y0 + BED_L          # 9000
# Top path: 9000 to 10500 = 1500 ✓
# Bottom path: 0 to 1500 = 1500 ✓

# Width: perimeter(750) + bed + 1500 + bed + 1500 + bed + perimeter(750) = 7500
# Service zone: 10000 - 7500 = 2500
PERIMETER_X = 750  # narrowest route — flagged as constraint
BED_PITCH = BED_W + PATH_CLR  # 2500

e = ""

# ================================================================
# DWELLING — outline only, no internal rooms
# ================================================================
e += R("A-WALL", 0, 0, DW_W, DW_D, PAL["dwell"])
e += T("A-ANNO", PX-1500, DW_D/2+300, TH["zone"], "DUPLEX")
e += T("A-ANNO", PX-1200, DW_D/2-400, TH["det"], "(see floor-plan sheet)")

# "TO DUPLEX" arrows from each patio
# West arrow
arr_x = -200
arr_y = DW_D / 2
e += L("A-ANNO", arr_x, arr_y, arr_x+600, arr_y, PAL["dwell"])
e += L("A-ANNO", arr_x+600, arr_y, arr_x+400, arr_y+150, PAL["dwell"])
e += L("A-ANNO", arr_x+600, arr_y, arr_x+400, arr_y-150, PAL["dwell"])
e += T("A-ANNO", arr_x-1200, arr_y+300, TH["det"], "TO DUPLEX")

# East arrow
arr_x = DW_W + 200
e += L("A-ANNO", arr_x, arr_y, arr_x-600, arr_y, PAL["dwell"])
e += L("A-ANNO", arr_x-600, arr_y, arr_x-400, arr_y+150, PAL["dwell"])
e += L("A-ANNO", arr_x-600, arr_y, arr_x-400, arr_y-150, PAL["dwell"])
e += T("A-ANNO", arr_x+200, arr_y+300, TH["det"], "TO DUPLEX")

# ================================================================
# PATIO CORRIDORS
# ================================================================
e += R("PATIO", -PATIO_W, 0, 0, DW_D, PAL["path"])
e += T("H-LABEL", -PATIO_W+200, DW_D/2+200, TH["det"], "PATIO")
e += T("H-LABEL", -PATIO_W+200, DW_D/2-200, TH["xs"], "1,800 mm")

e += R("PATIO", DW_W, 0, DW_W+PATIO_W, DW_D, PAL["path"])
e += T("H-LABEL", DW_W+200, DW_D/2+200, TH["det"], "PATIO")
e += T("H-LABEL", DW_W+200, DW_D/2-200, TH["xs"], "1,800 mm")

# ================================================================
# PATH CLEARANCE TRACKING
# ================================================================
all_clearances = []

def track(hive, desc, value):
    all_clearances.append((hive, desc, value))

# ================================================================
# HIVE DETAIL LAYOUT
# ================================================================
def draw_hive(prefix, hx0, hx1, mirror=False):
    global e

    # Envelope (dashed, enlarged depth)
    e += R("H-ENVELOPE", hx0, 0, hx1, HIVE_DEPTH, PAL["dwell"])

    # Zone label
    label = f"HIVE-{prefix}"
    e += T("H-LABEL", (hx0+hx1)/2 - 1200, HIVE_DEPTH/2 + 500, TH["zone"], label)

    # Bed column x-positions
    if not mirror:
        # HIVE-W: beds on west side, services on east (near patio)
        col_xs = [
            hx0 + PERIMETER_X,
            hx0 + PERIMETER_X + BED_PITCH,
            hx0 + PERIMETER_X + 2 * BED_PITCH,
        ]
        svc_x0 = col_xs[2] + BED_W + PERIMETER_X
        svc_x1 = hx1
    else:
        # HIVE-E: beds on east side, services on west (near patio)
        col_xs = [
            hx1 - PERIMETER_X - BED_W,
            hx1 - PERIMETER_X - BED_W - PATH_CLR - BED_W,
            hx1 - PERIMETER_X - 2*(BED_W + PATH_CLR) - BED_W,
        ]
        svc_x0 = hx0
        svc_x1 = col_xs[2] - PERIMETER_X

    sorted_cols = sorted(col_xs)

    # ---- DRAW BEDS with IDs ----
    bed_rows = [(BED_ROW1_Y0, BED_ROW1_Y1), (BED_ROW2_Y0, BED_ROW2_Y1)]
    bed_num = 1
    for ci, col_x in enumerate(sorted_cols):
        for ri, (ry0, ry1) in enumerate(bed_rows):
            bid = f"{prefix}-CB{bed_num:02d}"
            e += R("H-BED", col_x, ry0, col_x + BED_W, ry1, PAL["crop"])
            e += T("H-LABEL", col_x + 100, (ry0+ry1)/2 + 100, TH["xs"], bid)
            e += T("H-LABEL", col_x + 100, (ry0+ry1)/2 - 300, TH["xs"], "1.0x3.0")
            bed_num += 1

    # ---- MEASURE AND DIMENSION ALL PATH CLEARANCES ----
    # South path (y=0 to bed row 1)
    south_clr = BED_ROW1_Y0
    track(prefix, "South perimeter path", south_clr)
    e += dim_line(sorted_cols[0], 0, sorted_cols[0], BED_ROW1_Y0,
                  f"{south_clr:,}", offset=-600, vert=True)

    # North path (bed row 2 top to envelope top)
    north_clr = HIVE_DEPTH - BED_ROW2_Y1
    track(prefix, "North perimeter path", north_clr)
    e += dim_line(sorted_cols[0], BED_ROW2_Y1, sorted_cols[0], HIVE_DEPTH,
                  f"{north_clr:,}", offset=-600, vert=True)

    # Middle path (between rows)
    mid_clr = BED_ROW2_Y0 - BED_ROW1_Y1
    track(prefix, "Path between bed rows", mid_clr)
    e += dim_line(sorted_cols[1], BED_ROW1_Y1, sorted_cols[1], BED_ROW2_Y0,
                  f"{mid_clr:,}", offset=-600, vert=True)

    # Between-column paths
    for i in range(len(sorted_cols) - 1):
        gap = sorted_cols[i+1] - (sorted_cols[i] + BED_W)
        track(prefix, f"Aisle cols {i+1}-{i+2}", gap)
        mid_y = (BED_ROW1_Y0 + BED_ROW1_Y1) / 2
        e += dim_line(sorted_cols[i] + BED_W, mid_y,
                      sorted_cols[i+1], mid_y,
                      f"{gap:,}", offset=-400)

    # Outer perimeter paths (beside outermost bed columns)
    outer_west = sorted_cols[0] - hx0
    outer_east = hx1 - (sorted_cols[2] + BED_W)
    track(prefix, "Outer perimeter (boundary side)", min(outer_west, outer_east))
    track(prefix, "Gap beds-to-service", abs(svc_x0 - sorted_cols[2] - BED_W) if not mirror else abs(sorted_cols[2] - svc_x1))

    # Dimension outer perimeters
    e += dim_line(hx0, BED_ROW2_Y0 + 1500, sorted_cols[0], BED_ROW2_Y0 + 1500,
                  f"{outer_west}", offset=0)

    # ---- SERVICE ZONE ----
    svc_w = svc_x1 - svc_x0

    # All service items stacked bottom to top with working space
    # CP01-02: Compost bays
    comp_y0 = 300
    comp_y1 = comp_y0 + 1000
    e += R("H-COMPOST", svc_x0 + 200, comp_y0, svc_x0 + 1200, comp_y1, PAL["harvest"])
    e += R("H-COMPOST", svc_x0 + 1300, comp_y0, svc_x0 + 2300, comp_y1, PAL["harvest"])
    e += T("H-LABEL", svc_x0 + 250, comp_y0 + 400, TH["xs"], f"{prefix}-CP01")
    e += T("H-LABEL", svc_x0 + 1350, comp_y0 + 400, TH["xs"], f"{prefix}-CP02")
    # Working space in front of compost (1200mm clear above)
    ws_comp = 1200
    e += R("H-WORK", svc_x0 + 200, comp_y1, svc_x0 + 2300, comp_y1 + ws_comp)
    e += T("H-LABEL", svc_x0 + 400, comp_y1 + 500, TH["xs"], f"CLEAR {ws_comp}")

    # IR01: Irrigation station
    irr_y0 = comp_y1 + ws_comp + 200
    irr_y1 = irr_y0 + 800
    e += R("H-IRRIG", svc_x0 + 200, irr_y0, svc_x0 + 1500, irr_y1, PAL["path"])
    e += circ("H-IRRIG", svc_x0 + 800, irr_y0 + 400, 250, PAL["path"])
    e += T("H-LABEL", svc_x0 + 250, irr_y0 + 300, TH["xs"], f"{prefix}-IR01")

    # TP01: Tool cupboard 1200x600 with door swing
    tp_y0 = irr_y1 + 600
    tp_y1 = tp_y0 + 600
    e += R("H-TOOLS", svc_x0 + 200, tp_y0, svc_x0 + 1400, tp_y1, PAL["harvest"])
    e += T("H-LABEL", svc_x0 + 250, tp_y0 + 200, TH["xs"], f"{prefix}-TP01")
    # Door swing (600mm radius arc opening outward)
    door_cx = svc_x0 + 200
    door_cy = tp_y1
    e += arc_e("H-TOOLS", door_cx, door_cy, 600, 0, 90, PAL["harvest"])
    # Working space in front
    ws_tp = 1000
    e += R("H-WORK", svc_x0 + 200, tp_y1, svc_x0 + 1400, tp_y1 + ws_tp)
    e += T("H-LABEL", svc_x0 + 300, tp_y1 + 400, TH["xs"], f"CLEAR {ws_tp}")

    # TP02: Potting bench 1500x750
    pb_y0 = tp_y1 + ws_tp + 200
    pb_y1 = pb_y0 + 750
    e += R("H-TOOLS", svc_x0 + 200, pb_y0, svc_x0 + 1700, pb_y1, PAL["harvest"])
    e += T("H-LABEL", svc_x0 + 250, pb_y0 + 300, TH["xs"], f"{prefix}-TP02")
    # Working space
    ws_pb = 1000
    e += R("H-WORK", svc_x0 + 200, pb_y1, svc_x0 + 1700, pb_y1 + ws_pb)
    e += T("H-LABEL", svc_x0 + 300, pb_y1 + 400, TH["xs"], f"CLEAR {ws_pb}")

    # HV01: Harvest bench 1500x750
    hv_y0 = pb_y1 + ws_pb + 200
    hv_y1 = hv_y0 + 750
    e += R("H-HARVEST", svc_x0 + 200, hv_y0, svc_x0 + 1700, hv_y1, PAL["harvest"])
    e += T("H-LABEL", svc_x0 + 250, hv_y0 + 300, TH["xs"], f"{prefix}-HV01")
    # Working space
    ws_hv = 1000
    e += R("H-WORK", svc_x0 + 200, hv_y1, svc_x0 + 1700, hv_y1 + ws_hv)
    e += T("H-LABEL", svc_x0 + 300, hv_y1 + 400, TH["xs"], f"CLEAR {ws_hv}")

    # HV02: Crate staging 1000x500
    cr_y0 = hv_y1 + ws_hv + 150
    cr_y1 = cr_y0 + 500
    e += R("H-HARVEST", svc_x0 + 200, cr_y0, svc_x0 + 1200, cr_y1, PAL["harvest"])
    e += T("H-LABEL", svc_x0 + 250, cr_y0 + 150, TH["xs"], f"{prefix}-HV02")

    # HV03: Seed cupboard 1200x500 with door swing
    sd_y0 = cr_y1 + 150
    sd_y1 = sd_y0 + 500
    e += R("H-HARVEST", svc_x0 + 200, sd_y0, svc_x0 + 1400, sd_y1, PAL["harvest"])
    e += T("H-LABEL", svc_x0 + 250, sd_y0 + 150, TH["xs"], f"{prefix}-HV03")
    # Door swing
    e += arc_e("H-HARVEST", svc_x0 + 200, sd_y1, 500, 0, 90, PAL["harvest"])

    # ---- IRRIGATION BRANCHES (H-IRRIG layer, dashdot) ----
    # Main line from IR01 to bed zone
    irr_cx = svc_x0 + 800
    irr_cy = irr_y0 + 400
    # Horizontal main to bed area
    bed_zone_x = sorted_cols[1] + BED_W / 2  # centre of middle column
    main_y = BED_ROW1_Y0 - 500  # run below beds
    e += L("H-IRRIG", irr_cx, irr_cy, irr_cx, main_y, PAL["irrig"])
    e += L("H-IRRIG", irr_cx, main_y, bed_zone_x, main_y, PAL["irrig"])
    # Branch to each column (vertical stubs)
    for cx in sorted_cols:
        branch_x = cx + BED_W / 2
        e += L("H-IRRIG", branch_x, main_y, branch_x, main_y - 300, PAL["irrig"])
        e += L("H-IRRIG", bed_zone_x, main_y, branch_x, main_y, PAL["irrig"])
        # Drops to each bed in this column
        for ry0, ry1 in bed_rows:
            drop_y = (ry0 + ry1) / 2
            e += L("H-IRRIG", branch_x, main_y, branch_x, drop_y, PAL["irrig"])
            # Short horizontal tee at bed
            e += L("H-IRRIG", branch_x - 200, drop_y, branch_x + 200, drop_y, PAL["irrig"])

    # Dimension the service zone width
    e += dim_line(svc_x0, HIVE_DEPTH + 800, svc_x1, HIVE_DEPTH + 800,
                  f"{svc_w:,}", offset=0)

# Draw both hives
draw_hive("W", HW_X0, HW_X1, mirror=False)
draw_hive("E", HE_X0, HE_X1, mirror=True)

# ================================================================
# OVERALL DIMENSIONS
# ================================================================
dim_y = -1500
e += dim_line(HW_X0, dim_y, HW_X1, dim_y, f"{HIVE_WIDTH:,}", offset=0)
e += dim_line(-PATIO_W, dim_y, 0, dim_y, f"{PATIO_W:,}", offset=0)
e += dim_line(0, dim_y, DW_W, dim_y, f"{DW_W:,}", offset=0)
e += dim_line(DW_W, dim_y, DW_W+PATIO_W, dim_y, f"{PATIO_W:,}", offset=0)
e += dim_line(HE_X0, dim_y, HE_X1, dim_y, f"{HIVE_WIDTH:,}", offset=0)

total_w = HE_X1 - HW_X0
e += dim_line(HW_X0, dim_y - 2000, HE_X1, dim_y - 2000, f"{total_w:,}", offset=0)

# Depth dimension
e += dim_line(HW_X0, 0, HW_X0, HIVE_DEPTH, f"{HIVE_DEPTH:,}", offset=-2500, vert=True)
e += dim_line(0, 0, 0, DW_D, f"{DW_D:,}", offset=-1500, vert=True)

# Bed reference dimension
bed_ref_x = HW_X0 + PERIMETER_X
e += dim_line(bed_ref_x, BED_ROW1_Y0, bed_ref_x + BED_W, BED_ROW1_Y0,
              "1,000", offset=-800)
e += dim_line(bed_ref_x, BED_ROW1_Y0, bed_ref_x, BED_ROW1_Y1,
              "3,000", offset=-1500, vert=True)

# ================================================================
# SCALE BAR
# ================================================================
sb_x = HW_X0
sb_y = -5500
for i in range(6):
    e += L("H-DIM", sb_x + i*1000, sb_y, sb_x + i*1000, sb_y+300)
e += L("H-DIM", sb_x, sb_y, sb_x+5000, sb_y)
e += T("H-DIM", sb_x, sb_y-500, TH["xs"], "SCALE BAR (METRES)")
for i, lbl in enumerate(["0", "1", "2", "3", "4", "5 m"]):
    e += T("H-DIM", sb_x + i*1000 - 50, sb_y+500, TH["xs"], lbl)

# ================================================================
# NORTH ARROW
# ================================================================
na_x = HE_X1 + 3000
na_y = HIVE_DEPTH - 3000
e += L("H-LABEL", na_x, na_y, na_x, na_y+2500)
e += L("H-LABEL", na_x, na_y+2500, na_x-350, na_y+2000)
e += L("H-LABEL", na_x, na_y+2500, na_x+350, na_y+2000)
e += T("H-LABEL", na_x-200, na_y+3000, TH["room"], "N")

# ================================================================
# TITLE BLOCK
# ================================================================
tb_y = -7000
e += T("H-LABEL", HW_X0, tb_y, TH["head"],
       "MMUCO HIVE-E + HIVE-W -- CONCEPT DETAIL -- NOT FOR CONSTRUCTION")
e += T("H-LABEL", HW_X0, tb_y-500, TH["sub"],
       "hive-east-and-west rev 2 | Units mm 1:1 | Drawing ref: HD-01")
e += T("H-LABEL", HW_X0, tb_y-900, TH["xs"],
       "Hive envelopes PROVISIONAL 10,000 x 10,500 mm (enlarged from 9,200 depth).")
e += T("H-LABEL", HW_X0, tb_y-1200, TH["xs"],
       "Patios 1,800 mm. Main paths 1,500 mm. Perimeter beside outer beds: 750 mm (see NOTES).")

# ================================================================
# COMPONENT SCHEDULE (right side)
# ================================================================
lg_x = HE_X1 + 2500
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
    "Main paths: 1,500 mm clear",
    f"Growing per hive: {grow_per:.0f} m2",
    f"Growing total: {grow_per*2:.0f} m2",
    "Patio corridor: 1,800 mm",
    f"Envelope: {HIVE_WIDTH:,} x {HIVE_DEPTH:,} mm (PROVISIONAL)",
]:
    e += T("LEGEND", lg_x+100, lg_y, TH["xs"], t)
    lg_y -= 250

lg_y -= 400
e += T("LEGEND", lg_x, lg_y, TH["room"], "NOTES / CONSTRAINTS")
lg_y -= 350
for n in [
    "1. Envelope enlarged to 10,500 depth (was 9,200)",
    "   to achieve 1,500 mm N+S of beds.",
    "2. Perimeter beside outer bed columns: 750 mm.",
    "   Below 1,500 mm main-path standard.",
    "   ACCESS CONSTRAINT: single-file, no wheelbarrow.",
    "3. Hive extends 1,300 mm beyond dwelling north face.",
    "4. Bed and service positions are concept only.",
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

print()
print("=== DIMENSION CHECKS ===")
print(f"  Envelope: {HIVE_WIDTH:,} x {HIVE_DEPTH:,} mm")
print(f"  Beds: {BED_W} x {BED_L} mm, 6 per hive")
print(f"  Growing per hive: {grow_per:.0f} m2")
print(f"  Growing total: {grow_per*2:.0f} m2")
print(f"  Patio: {PATIO_W:,} mm")
print(f"  Main paths (between beds): {PATH_CLR:,} mm")
print(f"  Perimeter beside outer beds: {PERIMETER_X:,} mm — CONSTRAINT")
print(f"  South path: {BED_ROW1_Y0:,} mm — {'OK' if BED_ROW1_Y0 >= 1500 else 'FAIL'}")
print(f"  North path: {HIVE_DEPTH - BED_ROW2_Y1:,} mm — {'OK' if HIVE_DEPTH - BED_ROW2_Y1 >= 1500 else 'FAIL'}")
print(f"  Row-to-row: {BED_ROW2_Y0 - BED_ROW1_Y1:,} mm — {'OK' if BED_ROW2_Y0 - BED_ROW1_Y1 >= 1500 else 'FAIL'}")
print()
print("=== UNRESOLVED ACCESS CONSTRAINTS ===")
print("  1. Outer bed column perimeter: 750 mm (single-file, no wheelbarrow)")
print("  2. Hive envelope 1,300 mm taller than dwelling — extends beyond north face")
print("  3. Service zone working spaces adequate but tight (1,000-1,200 mm clear)")
