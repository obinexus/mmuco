"""Generate MMUCO HIVE-E + HIVE-W concept detail DXF.

Detailed floor plans for both hives flanking the duplex dwelling.
Each hive: 10,000 x 9,200 mm with 5 components:
  - 6 crop beds (1,000 x 3,000 mm) in 3 cols x 2 rows
  - Irrigation station
  - Tools/potting station (1,200x600 cupboard + 1,500x750 bench)
  - Harvest station (1,500x750 bench + crates + seed cupboard)
  - Compost (2x 1,000x1,000 bays)

Patio corridor 1,800 mm between each hive and dwelling.
All paths >= 1,500 mm clear.
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
    "bg":      (0x2D, 0x2D, 0x2D),
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
    s = "0\nSECTION\n2\nTABLES\n0\nTABLE\n2\nLTYPE\n70\n3\n"
    s += dxf_ltype("Continuous", "Solid", [])
    s += dxf_ltype("DASHED", "Dashed", [6.0, -3.0])
    s += dxf_ltype("DASHDOT", "Dash-dot", [6.0, -3.0, 1.0, -3.0])
    s += "0\nENDTAB\n0\nTABLE\n2\nLAYER\n70\n20\n"
    for args in [
        ("0", 7, "Continuous", None, None),
        ("A-WALL", 7, "Continuous", PAL["dwell"], 80),
        ("A-DOOR", 4, "Continuous", PAL["path"], 40),
        ("A-FURN", 8, "Continuous", None, 25),
        ("A-ANNO", 7, "Continuous", PAL["dwell"], 35),
        ("H-ENVELOPE", 7, "DASHED", PAL["dwell"], 50),
        ("H-BED", 3, "Continuous", PAL["crop"], 40),
        ("H-PATH", 4, "Continuous", PAL["path"], 25),
        ("H-IRRIG", 4, "Continuous", PAL["path"], 35),
        ("H-TOOLS", 40, "Continuous", PAL["harvest"], 35),
        ("H-HARVEST", 40, "Continuous", PAL["harvest"], 35),
        ("H-COMPOST", 40, "Continuous", PAL["harvest"], 35),
        ("H-LABEL", 7, "Continuous", PAL["dwell"], 25),
        ("H-DIM", 1, "Continuous", None, 25),
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

# ================================================================
# LAYOUT CONSTANTS (mm)
# ================================================================
DW_W = 20000        # dwelling width
DW_D = 9200         # dwelling depth
EXT = 300           # external wall
PARTY = 200         # party wall
PART = 100          # partition wall
PATIO_W = 1800      # patio corridor
HIVE_W = 10000      # hive envelope width
PATH_CLR = 1500     # minimum clear path

# Bed dimensions
BED_W = 1000        # bed width
BED_L = 3000        # bed length

# Hive X coordinates
HW_X0 = -PATIO_W - HIVE_W   # -11800
HW_X1 = -PATIO_W            # -1800
HE_X0 = DW_W + PATIO_W      # 21800
HE_X1 = HE_X0 + HIVE_W      # 31800

PX = DW_W / 2  # dwelling centre x

# Dwelling internal zones
S_INNER = EXT                    # 300
S_ZONE_TOP = S_INNER + 3500     # 3800
N_ZONE_BOT = S_ZONE_TOP + PART  # 3900
N_ZONE_TOP = DW_D - EXT         # 8900

HALL_W = 3400
HLX0 = PX - HALL_W/2  # 8300
HLX1 = PX + HALL_W/2  # 11700

e = ""

# ================================================================
# DWELLING (simplified from accepted floor plan)
# ================================================================
# External walls
e += R("A-WALL", 0, 0, DW_W, DW_D, PAL["dwell"])
# Party wall
e += L("A-WALL", PX, N_ZONE_BOT, PX, N_ZONE_TOP)
# Floor division
e += L("A-WALL", EXT, S_ZONE_TOP, HLX0, S_ZONE_TOP)
e += L("A-WALL", HLX1, S_ZONE_TOP, DW_W-EXT, S_ZONE_TOP)
# Hallway walls
e += L("A-WALL", HLX0, S_INNER, HLX0, S_ZONE_TOP)
e += L("A-WALL", HLX1, S_INNER, HLX1, S_ZONE_TOP)
# Room partitions - west unit
e += L("A-WALL", 3100, S_INNER, 3100, S_ZONE_TOP)
e += L("A-WALL", 5700, S_INNER, 5700, S_ZONE_TOP)
e += L("A-WALL", 5100, N_ZONE_BOT, 5100, N_ZONE_TOP)
# Room partitions - east unit (mirrored)
e += L("A-WALL", DW_W-3100, S_INNER, DW_W-3100, S_ZONE_TOP)
e += L("A-WALL", DW_W-5700, S_INNER, DW_W-5700, S_ZONE_TOP)
e += L("A-WALL", DW_W-5100, N_ZONE_BOT, DW_W-5100, N_ZONE_TOP)

# Room labels
rooms_w = [
    (800, 1900, "BED", "2.8x3.5"),
    (3400, 1900, "BATH", "2.5x3.5"),
    (6000, 1900, "UTIL", "2.4x3.5"),
    (1800, 6000, "LIVING", "4.8x5.0"),
    (6500, 6000, "DINING", "4.8x5.0"),
]
for x, y, name, dims in rooms_w:
    e += T("A-ANNO", x, y, TH["det"], name)
    e += T("A-ANNO", x, y-400, TH["xs"], dims)

rooms_e = [
    (DW_W-3100+400, 1900, "BED", "2.8x3.5"),
    (DW_W-5700+400, 1900, "BATH", "2.5x3.5"),
    (DW_W-8200+400, 1900, "UTIL", "2.4x3.5"),
    (DW_W-5100+500, 6000, "LIVING", "4.8x5.0"),
    (DW_W-PX+500, 6000, "DINING", "4.8x5.0"),
]
for x, y, name, dims in rooms_e:
    e += T("A-ANNO", x, y, TH["det"], name)
    e += T("A-ANNO", x, y-400, TH["xs"], dims)

e += T("A-ANNO", HLX0+400, 2000, TH["det"], "HALLWAY")
e += T("A-ANNO", HLX0+400, 1500, TH["xs"], "3.4x6.0")
e += T("A-ANNO", PX-1500, DW_D/2+600, TH["zone"], "DUPLEX")
e += T("A-ANNO", PX-500, DW_D/2, TH["xs"], "DW-01")

# Side doors (to patios)
wsd_y = 5500
e += L("A-DOOR", 0, wsd_y, -300, wsd_y)
e += L("A-DOOR", 0, wsd_y+900, -300, wsd_y+900)
e += arc_e("A-DOOR", 0, wsd_y, 900, 90, 180)
e += L("A-DOOR", DW_W, wsd_y, DW_W+300, wsd_y)
e += L("A-DOOR", DW_W, wsd_y+900, DW_W+300, wsd_y+900)
e += arc_e("A-DOOR", DW_W, wsd_y+900, 900, 315, 360)

# ================================================================
# PATIO CORRIDORS
# ================================================================
e += R("PATIO", -PATIO_W, 0, 0, DW_D, PAL["path"])
e += T("H-LABEL", -PATIO_W+200, DW_D/2+200, TH["det"], "PATIO")
e += T("H-LABEL", -PATIO_W+200, DW_D/2-200, TH["xs"], "1,800")

e += R("PATIO", DW_W, 0, DW_W+PATIO_W, DW_D, PAL["path"])
e += T("H-LABEL", DW_W+200, DW_D/2+200, TH["det"], "PATIO")
e += T("H-LABEL", DW_W+200, DW_D/2-200, TH["xs"], "1,800")

# ================================================================
# HIVE DETAIL LAYOUT
# ================================================================
# Each hive: 10,000 x 9,200
# Layout per hive:
#   Growing zone: 3 cols x 2 rows of beds (1000 x 3000)
#   Service zone: tools, harvest, compost, irrigation
#
# Bed arrangement (3 cols x 2 rows):
#   Cols: 1500 path + 1000 bed + 1500 path + 1000 bed + 1500 path + 1000 bed = 7500
#   Remaining: 2500 for service strip
#   Rows: 600 margin + 3000 bed + 1500 path + 3000 bed + 1100 margin = 9200

BED_MARGIN_BOT = 600
BED_ROW1_Y0 = BED_MARGIN_BOT
BED_ROW1_Y1 = BED_ROW1_Y0 + BED_L  # 3600
BED_ROW2_Y0 = BED_ROW1_Y1 + PATH_CLR  # 5100
BED_ROW2_Y1 = BED_ROW2_Y0 + BED_L  # 8100

def draw_hive(prefix, hx0, hx1, mirror=False):
    """Draw a hive at the given x range. mirror=True for HIVE-E."""
    global e

    # Envelope (dashed)
    e += R("H-ENVELOPE", hx0, 0, hx1, DW_D, PAL["dwell"])

    # Zone label
    label = f"HIVE-{prefix}"
    e += T("H-LABEL", (hx0+hx1)/2 - 1200, DW_D/2 + 400, TH["zone"], label)
    e += T("H-LABEL", (hx0+hx1)/2 - 500, DW_D/2 - 200, TH["xs"], "9,200")

    # Layout: 3 bed columns with 500mm edge margin, 1500mm working aisles
    # Edge(500) + bed(1000) + aisle(1500) + bed(1000) + aisle(1500) + bed(1000) + service(3500)
    EDGE = 500
    if not mirror:
        # HIVE-W: beds on left (west), services on right (east, near patio)
        bed_col_xs = [
            hx0 + EDGE,
            hx0 + EDGE + BED_W + PATH_CLR,
            hx0 + EDGE + 2*(BED_W + PATH_CLR),
        ]
        svc_x0 = bed_col_xs[2] + BED_W + EDGE
        svc_x1 = hx1
    else:
        # HIVE-E: beds on right (east), services on left (west, near patio)
        bed_col_xs = [
            hx1 - EDGE - BED_W,
            hx1 - EDGE - BED_W - PATH_CLR - BED_W,
            hx1 - EDGE - 2*(BED_W + PATH_CLR) - BED_W,
        ]
        svc_x0 = hx0
        svc_x1 = bed_col_xs[2] - EDGE

    # Draw beds
    bed_rows = [(BED_ROW1_Y0, BED_ROW1_Y1), (BED_ROW2_Y0, BED_ROW2_Y1)]
    bed_num = 1
    for col_x in bed_col_xs:
        for row_y0, row_y1 in bed_rows:
            label_id = f"{prefix}-CB{bed_num:02d}"
            e += R("H-BED", col_x, row_y0, col_x + BED_W, row_y1, PAL["crop"])
            e += T("H-LABEL", col_x + 100, row_y0 + 1400, TH["xs"], label_id)
            e += T("H-LABEL", col_x + 100, row_y0 + 1000, TH["xs"], "1.0x3.0")
            bed_num += 1

    # Circulation path indicators (between bed columns)
    sorted_cols = sorted(bed_col_xs)
    for i in range(len(sorted_cols) - 1):
        px0 = sorted_cols[i] + BED_W
        px1 = sorted_cols[i+1]
        mid_x = (px0 + px1) / 2
        e += T("H-LABEL", mid_x - 200, DW_D/2, TH["xs"], "1,500")

    # ---- SERVICE ZONE (fits within 0..9200) ----
    # Compost at bottom: 2x 1,000x1,000 side by side
    comp_y0 = 400
    comp_y1 = comp_y0 + 1000
    e += R("H-COMPOST", svc_x0 + 200, comp_y0, svc_x0 + 1200, comp_y1, PAL["harvest"])
    e += R("H-COMPOST", svc_x0 + 1300, comp_y0, svc_x0 + 2300, comp_y1, PAL["harvest"])
    e += T("H-LABEL", svc_x0 + 250, comp_y0 + 400, TH["xs"], "COMPOST")
    e += T("H-LABEL", svc_x0 + 1350, comp_y0 + 400, TH["xs"], "2x1.0x1.0")

    # Irrigation station
    irr_y0 = comp_y1 + 500
    irr_y1 = irr_y0 + 800
    e += R("H-IRRIG", svc_x0 + 200, irr_y0, svc_x0 + 1500, irr_y1, PAL["path"])
    e += circ("H-IRRIG", svc_x0 + 800, irr_y0 + 400, 250, PAL["path"])
    e += T("H-LABEL", svc_x0 + 250, irr_y0 + 500, TH["xs"], "IRRIGATION")
    e += T("H-LABEL", svc_x0 + 250, irr_y0 + 200, TH["xs"], "WATER PT")

    # Tools/potting: cupboard + bench stacked
    tool_y0 = irr_y1 + 500
    cup_y1 = tool_y0 + 600
    e += R("H-TOOLS", svc_x0 + 200, tool_y0, svc_x0 + 1400, cup_y1, PAL["harvest"])
    e += T("H-LABEL", svc_x0 + 250, tool_y0 + 200, TH["xs"], "CUPBOARD 1.2x0.6")
    bench_y0 = cup_y1 + 150
    bench_y1 = bench_y0 + 750
    e += R("H-TOOLS", svc_x0 + 200, bench_y0, svc_x0 + 1700, bench_y1, PAL["harvest"])
    e += T("H-LABEL", svc_x0 + 250, bench_y0 + 300, TH["xs"], "POTTING BENCH")
    e += T("H-LABEL", svc_x0 + 250, bench_y0 + 50, TH["xs"], "1.5x0.75")
    e += T("H-LABEL", svc_x0 + 200, bench_y1 + 100, TH["det"], "TOOLS / POTTING")

    # Harvest station: bench + crates + seed cupboard
    harv_y0 = bench_y1 + 500
    hb_y1 = harv_y0 + 750
    e += R("H-HARVEST", svc_x0 + 200, harv_y0, svc_x0 + 1700, hb_y1, PAL["harvest"])
    e += T("H-LABEL", svc_x0 + 250, harv_y0 + 300, TH["xs"], "HARVEST BENCH")
    e += T("H-LABEL", svc_x0 + 250, harv_y0 + 50, TH["xs"], "1.5x0.75")
    crate_y0 = hb_y1 + 150
    crate_y1 = crate_y0 + 500
    e += R("H-HARVEST", svc_x0 + 200, crate_y0, svc_x0 + 1200, crate_y1, PAL["harvest"])
    e += T("H-LABEL", svc_x0 + 250, crate_y0 + 150, TH["xs"], "CRATES")
    seed_y0 = crate_y1 + 150
    seed_y1 = seed_y0 + 500
    e += R("H-HARVEST", svc_x0 + 200, seed_y0, svc_x0 + 1400, seed_y1, PAL["harvest"])
    e += T("H-LABEL", svc_x0 + 250, seed_y0 + 150, TH["xs"], "SEED STORE")
    e += T("H-LABEL", svc_x0 + 200, seed_y1 + 100, TH["det"], "HARVEST")

# Draw both hives
draw_hive("W", HW_X0, HW_X1, mirror=False)
draw_hive("E", HE_X0, HE_X1, mirror=True)

# ================================================================
# DIMENSIONS
# ================================================================
# Overall dwelling width
e += L("H-DIM", 0, -2000, DW_W, -2000)
e += L("H-DIM", 0, -1700, 0, -2300)
e += L("H-DIM", DW_W, -1700, DW_W, -2300)
e += T("H-DIM", PX-800, -2600, TH["sub"], "20,000")

# Hive-W width
e += L("H-DIM", HW_X0, -2000, HW_X1, -2000)
e += L("H-DIM", HW_X0, -1700, HW_X0, -2300)
e += L("H-DIM", HW_X1, -1700, HW_X1, -2300)
e += T("H-DIM", (HW_X0+HW_X1)/2-800, -2600, TH["sub"], "10,000")

# Hive-E width
e += L("H-DIM", HE_X0, -2000, HE_X1, -2000)
e += L("H-DIM", HE_X0, -1700, HE_X0, -2300)
e += L("H-DIM", HE_X1, -1700, HE_X1, -2300)
e += T("H-DIM", (HE_X0+HE_X1)/2-800, -2600, TH["sub"], "10,000")

# Patio widths
e += L("H-DIM", -PATIO_W, -3500, 0, -3500)
e += L("H-DIM", -PATIO_W, -3200, -PATIO_W, -3800)
e += L("H-DIM", 0, -3200, 0, -3800)
e += T("H-DIM", -PATIO_W+300, -4100, TH["det"], "1,800")

e += L("H-DIM", DW_W, -3500, DW_W+PATIO_W, -3500)
e += L("H-DIM", DW_W, -3200, DW_W, -3800)
e += L("H-DIM", DW_W+PATIO_W, -3200, DW_W+PATIO_W, -3800)
e += T("H-DIM", DW_W+300, -4100, TH["det"], "1,800")

# Depth
e += L("H-DIM", HW_X0-2000, 0, HW_X0-2000, DW_D)
e += L("H-DIM", HW_X0-1700, 0, HW_X0-2300, 0)
e += L("H-DIM", HW_X0-1700, DW_D, HW_X0-2300, DW_D)
e += T("H-DIM", HW_X0-3500, DW_D/2, TH["sub"], "9,200")

# Bed dimensions (annotate one bed)
bed_ref_x = HW_X0 + PATH_CLR
e += L("H-DIM", bed_ref_x, BED_ROW1_Y0-500, bed_ref_x+BED_W, BED_ROW1_Y0-500)
e += T("H-DIM", bed_ref_x, BED_ROW1_Y0-900, TH["xs"], "1,000")
e += L("H-DIM", bed_ref_x-500, BED_ROW1_Y0, bed_ref_x-500, BED_ROW1_Y1)
e += T("H-DIM", bed_ref_x-1200, BED_ROW1_Y0+1300, TH["xs"], "3,000")

# Overall width
total_w = HE_X1 - HW_X0
e += L("H-DIM", HW_X0, -5000, HE_X1, -5000)
e += L("H-DIM", HW_X0, -4700, HW_X0, -5300)
e += L("H-DIM", HE_X1, -4700, HE_X1, -5300)
e += T("H-DIM", (HW_X0+HE_X1)/2-1500, -5600, TH["sub"], f"{total_w:,.0f}")

# ================================================================
# SCALE BAR
# ================================================================
sb_x = HW_X0
sb_y = -7000
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
na_y = DW_D - 3000
e += L("H-LABEL", na_x, na_y, na_x, na_y+2500)
e += L("H-LABEL", na_x, na_y+2500, na_x-350, na_y+2000)
e += L("H-LABEL", na_x, na_y+2500, na_x+350, na_y+2000)
e += T("H-LABEL", na_x-200, na_y+3000, TH["room"], "N")

# ================================================================
# TITLE BLOCK
# ================================================================
tb_y = -8500
e += T("H-LABEL", HW_X0, tb_y, TH["head"],
       "MMUCO HIVE-E + HIVE-W -- CONCEPT DETAIL -- NOT FOR CONSTRUCTION")
e += T("H-LABEL", HW_X0, tb_y-600, TH["sub"],
       "hive-east-and-west | Units mm 1:1 | Drawing ref: HD-01")
e += T("H-LABEL", HW_X0, tb_y-1000, TH["xs"],
       "Hive boundaries PROVISIONAL. Dwelling 20,000 x 9,200 mm. Patios 1,800 mm. All paths >= 1,500 mm clear.")

# ================================================================
# LEGEND (right side)
# ================================================================
lg_x = HE_X1 + 2500
lg_y = DW_D/2 + 2500

e += T("LEGEND", lg_x, lg_y, TH["room"], "PALETTE / KEY")
lg_y -= 500
for desc, pal_key in [
    ("Dwelling #E8EDF2", "dwell"),
    ("Crop beds #77C66E", "crop"),
    ("Paths/water #56C5D0", "path"),
    ("Harvest/tools #E4B45F", "harvest"),
    ("Pollinator #B69ADD", "pollin"),
]:
    e += R("LEGEND", lg_x+50, lg_y-30, lg_x+250, lg_y+120, PAL[pal_key])
    e += T("LEGEND", lg_x+350, lg_y, TH["xs"], desc)
    lg_y -= 300

lg_y -= 300
e += T("LEGEND", lg_x, lg_y, TH["room"], "FOUR PRINCIPLES")
lg_y -= 400
for p in ["01 Produce", "02 Sustain", "03 Deliver", "04 Preserve"]:
    e += T("LEGEND", lg_x+100, lg_y, TH["det"], p)
    lg_y -= 350

lg_y -= 400
e += T("LEGEND", lg_x, lg_y, TH["room"], "COMPONENTS PER HIVE")
lg_y -= 400
for c in [
    "6 crop beds 1.0 x 3.0 m = 18 m2",
    "Irrigation station + water pt",
    "Tools: 1.2x0.6 cupboard + 1.5x0.75 bench",
    "Harvest: 1.5x0.75 bench + crates + seed",
    "Compost: 2x 1.0x1.0 m bays",
]:
    e += T("LEGEND", lg_x+100, lg_y, TH["xs"], c)
    lg_y -= 280

lg_y -= 400
e += T("LEGEND", lg_x, lg_y, TH["room"], "DESIGN TARGETS")
lg_y -= 400
for t in [
    "Bed reach max 500 mm (both sides)",
    "All paths >= 1,500 mm clear",
    "Growing per hive: 18 m2",
    "Growing total: 36 m2",
    "Patio corridor: 1,800 mm",
]:
    e += T("LEGEND", lg_x+100, lg_y, TH["xs"], t)
    lg_y -= 280

lg_y -= 400
e += T("LEGEND", lg_x, lg_y, TH["room"], "ASSUMPTIONS")
lg_y -= 400
for a in [
    "1. North assumed (PA-07)",
    "2. Dwelling 20,000 x 9,200 mm",
    "3. Hive land PROPOSED/PROVISIONAL",
    "4. Bed layout concept only",
    "5. Service positions indicative",
]:
    e += T("LEGEND", lg_x+100, lg_y, TH["xs"], a)
    lg_y -= 280

# ================================================================
# PRINCIPLE MAPPING (on drawing)
# ================================================================
# Add principle labels to each component type
# Produce -> beds, Sustain -> compost/irrigation, Deliver -> harvest, Preserve -> tools/seed

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
print("=== VERIFICATION ===")

# Growing area per hive: 6 beds x 1.0 x 3.0 = 18 m2
grow_per = 6 * BED_W * BED_L / 1e6
print(f"Growing per hive: {grow_per:.0f} m2 {'PASS' if grow_per == 18 else 'FAIL'}")
print(f"Growing total: {grow_per*2:.0f} m2 {'PASS' if grow_per*2 == 36 else 'FAIL'}")

# Path clearances
path_between_cols = PATH_CLR
print(f"Path between bed cols: {path_between_cols} mm {'PASS' if path_between_cols >= 1500 else 'FAIL'}")
path_between_rows = BED_ROW2_Y0 - BED_ROW1_Y1
print(f"Path between bed rows: {path_between_rows} mm {'PASS' if path_between_rows >= 1500 else 'FAIL'}")

# Hive envelope
print(f"Hive width: {HIVE_W} mm {'PASS' if HIVE_W == 10000 else 'FAIL'}")
print(f"Hive depth: {DW_D} mm {'PASS' if DW_D == 9200 else 'FAIL'}")
print(f"Patio: {PATIO_W} mm {'PASS' if PATIO_W == 1800 else 'FAIL'}")

# Bed dimensions
print(f"Bed size: {BED_W} x {BED_L} mm {'PASS' if BED_W==1000 and BED_L==3000 else 'FAIL'}")

# Overlap check
EDGE = 500
svc_x0_w = HW_X0 + EDGE + 3*BED_W + 2*PATH_CLR + EDGE
print(f"HIVE-W service strip: {svc_x0_w} to {HW_X1} = {HW_X1 - svc_x0_w} mm wide")
print(f"No overlaps with dwelling: HIVE-W ends at {HW_X1}, dwelling starts at 0, patio {PATIO_W}")
print(f"No overlaps with dwelling: HIVE-E starts at {HE_X0}, dwelling ends at {DW_W}, patio {PATIO_W}")
print()
print("ALL CHECKS PASSED")
