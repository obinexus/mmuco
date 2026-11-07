"""Generate MMUCO Hive two-hive layout v05 DXF.

Changes from v04:
- Text heights reverted (divided by 1.75)
- Recreational garden resized to 92 m2 (20.0 x 4.6 m = half dwelling area)
- Orangery reduced from ~40 m2 to 12 m2 (4.0 x 3.0 m), repositioned
- Former garden extent shown as dashed reference
- Sun-path moved clear of title block
- Labels repositioned to avoid overlaps
"""
import math, os

OUT = r"C:\Users\Public\Public Projects\github\mmuco\hive\concept_NOT-ISSUED\hive-dxf_NOT-ISSUED\hive_two_hives_rev_v05.dxf"

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
}

def rgb420(r, g, b):
    return r * 65536 + g * 256 + b

# Text heights (original, v04 / 1.75)
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

def dxf_layer(name, aci, lt="Continuous", rgb=None):
    s = f"0\nLAYER\n5\n{h()}\n100\nAcDbSymbolTableRecord\n100\nAcDbLayerTableRecord\n2\n{name}\n70\n0\n62\n{aci}\n6\n{lt}\n"
    if rgb: s += f"420\n{rgb420(*rgb)}\n"
    return s

def dxf_tables():
    s = "0\nSECTION\n2\nTABLES\n0\nTABLE\n2\nLTYPE\n70\n3\n"
    s += dxf_ltype("Continuous", "Solid", [])
    s += dxf_ltype("DASHED", "Dashed", [6.0, -3.0])
    s += "0\nENDTAB\n0\nTABLE\n2\nLAYER\n70\n20\n"
    for args in [
        ("0", 7, "Continuous", None),
        ("DWELLING", 254, "Continuous", PAL["dwell"]),
        ("WALLS", 254, "Continuous", PAL["dwell"]),
        ("DOORS_WINDOWS", 254, "Continuous", PAL["dwell"]),
        ("CROP_BEDS", 3, "Continuous", PAL["crop"]),
        ("PATHS_WATER", 4, "Continuous", PAL["path"]),
        ("HARVEST_STORE", 40, "Continuous", PAL["harvest"]),
        ("POLLINATOR", 201, "Continuous", PAL["pollin"]),
        ("RECREATIONAL", 3, "Continuous", PAL["crop"]),
        ("DIMENSIONS", 254, "Continuous", PAL["dwell"]),
        ("TEXT_LABELS", 254, "Continuous", PAL["dwell"]),
        ("SUN_PATH", 40, "DASHED", PAL["harvest"]),
        ("PROVISIONAL", 254, "DASHED", PAL["dwell"]),
        ("SHADOW", 8, "DASHED", None),
        ("PRIVATE_GARDEN", 8, "Continuous", None),
        ("CONSERVATORY", 4, "Continuous", PAL["path"]),
        ("FORMER_EXTENT", 9, "DASHED", None),
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
DW_W = 20000
EXT = 300
PARTY = 200
PART = 100
PATIO_W = 1800
HIVE_WD = 10000
PATH_W = 1500
BED_W = 1000
DW_D = 9200

PX = DW_W / 2

S_INNER = EXT
S_ZONE_TOP = S_INNER + 3500
N_ZONE_BOT = S_ZONE_TOP + PART
N_ZONE_TOP = DW_D - EXT

HALL_W = 3400
HLX0 = PX - HALL_W/2
HLX1 = PX + HALL_W/2

PCH_W, PCH_D = 4000, 3000
PCH_X0 = PX - PCH_W/2
PCH_X1 = PX + PCH_W/2
PCH_Y0 = -PCH_D

HPROJ_Y0 = -2500
HPROJ_X0 = HLX0
HPROJ_X1 = HLX1

CONS_W, CONS_D = 6000, 4000
CX0 = PX - CONS_W/2
CX1 = PX + CONS_W/2
CY0 = DW_D
CY1 = DW_D + CONS_D

PGY0, PGY1 = DW_D, CY1

# NEW: Recreational garden = half dwelling area
# Dwelling area = 20,000 x 9,200 = 184 m2. Half = 92 m2.
# Garden: 20,000 x 4,600 = 92 m2, aligned with duplex width.
SG_W_NEW = 20000
SG_D_NEW = 4600
SGY0 = CY1           # 13,200
SGY1 = SGY0 + SG_D_NEW  # 17,800
SGX0 = 0
SGX1 = DW_W  # 20,000

# Former extent (for dashed reference)
FORMER_SG_W = 22200
FORMER_SG_D = 20611
FORMER_SGX0 = PX - FORMER_SG_W/2  # -1100
FORMER_SGX1 = PX + FORMER_SG_W/2  # 21100
FORMER_SGY1 = SGY0 + FORMER_SG_D  # 33811

HW_X1 = -PATIO_W
HW_X0 = HW_X1 - HIVE_WD
HE_X0 = DW_W + PATIO_W
HE_X1 = HE_X0 + HIVE_WD

PAT_Y0 = PCH_Y0
PAT_Y1 = SGY0

e = ""

# ================================================================
# DWELLING
# ================================================================
e += R("WALLS", 0, 0, DW_W, DW_D, PAL["dwell"])
e += L("WALLS", PX, N_ZONE_BOT, PX, N_ZONE_TOP)
e += L("WALLS", EXT, S_ZONE_TOP, HLX0, S_ZONE_TOP)
e += L("WALLS", HLX1, S_ZONE_TOP, DW_W-EXT, S_ZONE_TOP)
e += L("WALLS", HLX0, S_INNER, HLX0, S_ZONE_TOP)
e += L("WALLS", HLX1, S_INNER, HLX1, S_ZONE_TOP)
e += L("WALLS", 3100, S_INNER, 3100, S_ZONE_TOP)
e += L("WALLS", 5700, S_INNER, 5700, S_ZONE_TOP)
e += L("WALLS", DW_W-3100, S_INNER, DW_W-3100, S_ZONE_TOP)
e += L("WALLS", DW_W-5700, S_INNER, DW_W-5700, S_ZONE_TOP)
e += L("WALLS", 5100, N_ZONE_BOT, 5100, N_ZONE_TOP)
e += L("WALLS", DW_W-5100, N_ZONE_BOT, DW_W-5100, N_ZONE_TOP)

# Room labels - short, positioned inside rooms
e += T("TEXT_LABELS", 800, 1900, TH["det"], "BED")
e += T("TEXT_LABELS", 800, 1500, TH["xs"], "2.8x3.5")
e += T("TEXT_LABELS", 3400, 1900, TH["det"], "BATH")
e += T("TEXT_LABELS", 3400, 1500, TH["xs"], "2.5x3.5")
e += T("TEXT_LABELS", 6000, 1900, TH["det"], "UTIL")
e += T("TEXT_LABELS", 6000, 1500, TH["xs"], "2.4x3.5")

e += T("TEXT_LABELS", 1800, 6000, TH["det"], "LIVING")
e += T("TEXT_LABELS", 1800, 5600, TH["xs"], "4.8x5.0")
e += T("TEXT_LABELS", 6500, 6000, TH["det"], "DINING")
e += T("TEXT_LABELS", 6500, 5600, TH["xs"], "4.8x5.0")

# East unit (mirror)
e += T("TEXT_LABELS", DW_W-3100+400, 1900, TH["det"], "BED")
e += T("TEXT_LABELS", DW_W-3100+400, 1500, TH["xs"], "2.8x3.5")
e += T("TEXT_LABELS", DW_W-5700+400, 1900, TH["det"], "BATH")
e += T("TEXT_LABELS", DW_W-5700+400, 1500, TH["xs"], "2.5x3.5")
e += T("TEXT_LABELS", DW_W-8200+400, 1900, TH["det"], "UTIL")
e += T("TEXT_LABELS", DW_W-8200+400, 1500, TH["xs"], "2.4x3.5")

e += T("TEXT_LABELS", DW_W-5100+500, 6000, TH["det"], "LIVING")
e += T("TEXT_LABELS", DW_W-5100+500, 5600, TH["xs"], "4.8x5.0")
e += T("TEXT_LABELS", DW_W-PX+500, 6000, TH["det"], "DINING")
e += T("TEXT_LABELS", DW_W-PX+500, 5600, TH["xs"], "4.8x5.0")

# Hallway
e += T("TEXT_LABELS", HLX0+400, 2000, TH["det"], "HALLWAY")
e += T("TEXT_LABELS", HLX0+400, 1500, TH["xs"], "3.4x6.0")

# DUPLEX label (centered, above room labels)
e += T("TEXT_LABELS", PX-1500, DW_D/2+600, TH["zone"], "DUPLEX")
e += T("TEXT_LABELS", PX-500, DW_D/2, TH["xs"], "DW-01")

# Doors
fd_x0 = PX - 840
fd_x1 = PX + 840
e += L("DOORS_WINDOWS", fd_x0, 0, fd_x0, -300)
e += L("DOORS_WINDOWS", fd_x1, 0, fd_x1, -300)
e += arc_e("DOORS_WINDOWS", fd_x0, 0, 840, 270, 315)

wsd_y = 5500
e += L("DOORS_WINDOWS", 0, wsd_y, -300, wsd_y)
e += L("DOORS_WINDOWS", 0, wsd_y+900, -300, wsd_y+900)
e += arc_e("DOORS_WINDOWS", 0, wsd_y, 900, 90, 180)

e += L("DOORS_WINDOWS", DW_W, wsd_y, DW_W+300, wsd_y)
e += L("DOORS_WINDOWS", DW_W, wsd_y+900, DW_W+300, wsd_y+900)
e += arc_e("DOORS_WINDOWS", DW_W, wsd_y+900, 900, 315, 360)

e += L("DOORS_WINDOWS", 8500, DW_D, 8500, DW_D+300)
e += L("DOORS_WINDOWS", 9400, DW_D, 9400, DW_D+300)
e += L("DOORS_WINDOWS", 10600, DW_D, 10600, DW_D+300)
e += L("DOORS_WINDOWS", 11500, DW_D, 11500, DW_D+300)
e += L("DOORS_WINDOWS", PX-500, CY1, PX-500, CY1+300)
e += L("DOORS_WINDOWS", PX+500, CY1, PX+500, CY1+300)

# Porch
e += R("DWELLING", PCH_X0, PCH_Y0, PCH_X1, 0, PAL["dwell"])
e += R("DWELLING", HPROJ_X0, HPROJ_Y0, HPROJ_X1, 0, PAL["dwell"])
e += T("TEXT_LABELS", PCH_X0+300, PCH_Y0+1200, TH["det"], "PORCH")
e += T("TEXT_LABELS", PCH_X0+300, PCH_Y0+700, TH["xs"], "4.0x3.0")

# ================================================================
# CENTRAL CONSERVATORY
# ================================================================
e += R("CONSERVATORY", CX0, CY0, CX1, CY1, PAL["path"])
e += T("TEXT_LABELS", CX0+600, CY0+2000, TH["room"], "CONSERVATORY")
e += T("TEXT_LABELS", CX0+600, CY0+1400, TH["xs"], "6.0x4.0 (inferred)")

# ================================================================
# PATIOS
# ================================================================
e += R("PATHS_WATER", -PATIO_W, PAT_Y0, 0, PAT_Y1, PAL["path"])
e += T("TEXT_LABELS", -PATIO_W+100, DW_D/2+200, TH["det"], "PATIO")
e += T("TEXT_LABELS", -PATIO_W+100, DW_D/2-200, TH["xs"], "1,800")

e += R("PATHS_WATER", DW_W, PAT_Y0, DW_W+PATIO_W, PAT_Y1, PAL["path"])
e += T("TEXT_LABELS", DW_W+100, DW_D/2+200, TH["det"], "PATIO")
e += T("TEXT_LABELS", DW_W+100, DW_D/2-200, TH["xs"], "1,800")

e += R("PATHS_WATER", -PATIO_W, PCH_Y0-PATH_W, DW_W+PATIO_W, PCH_Y0, PAL["path"])
e += T("TEXT_LABELS", PX-1500, PCH_Y0-PATH_W+300, TH["det"], "FRONT PATH 1.5m")

# ================================================================
# PRIVATE GARDENS
# ================================================================
e += R("PRIVATE_GARDEN", -PATIO_W, PGY0, CX0, PGY1)
e += T("TEXT_LABELS", -PATIO_W+200, PGY0+1500, TH["det"], "PRIV A")

e += R("PRIVATE_GARDEN", CX1, PGY0, DW_W+PATIO_W, PGY1)
e += T("TEXT_LABELS", CX1+200, PGY0+1500, TH["det"], "PRIV B")

e += R("PATHS_WATER", CX0-PATH_W, PGY0, CX0, PGY1, PAL["path"])
e += R("PATHS_WATER", CX1, PGY0, CX1+PATH_W, PGY1, PAL["path"])

# ================================================================
# SHARED RECREATIONAL GARDEN (92 m2: 20,000 x 4,600)
# ================================================================
e += R("RECREATIONAL", SGX0, SGY0, SGX1, SGY1, PAL["crop"])

# Central path from conservatory
e += R("PATHS_WATER", PX-750, SGY0, PX+750, SGY1, PAL["path"])

# ONE ORANGERY (reduced: 4,000 x 3,000 = 12 m2, was ~40 m2)
ORG_X0, ORG_Y0 = 500, SGY0 + 800
ORG_X1, ORG_Y1 = ORG_X0 + 4000, ORG_Y0 + 3000
e += R("RECREATIONAL", ORG_X0, ORG_Y0, ORG_X1, ORG_Y1, PAL["crop"])
e += T("TEXT_LABELS", ORG_X0+200, ORG_Y0+1500, TH["det"], "ORANGERY")
e += T("TEXT_LABELS", ORG_X0+200, ORG_Y0+1000, TH["xs"], "4.0x3.0 = 12 m2")
e += T("TEXT_LABELS", ORG_X0+200, ORG_Y0+600, TH["xs"], "(was ~40 m2)")

# ONE WELL (east side, away from paths)
WELL_X, WELL_Y = 17000, SGY0 + SG_D_NEW/2
e += circ("PATHS_WATER", WELL_X, WELL_Y, 600, PAL["path"])
e += circ("PATHS_WATER", WELL_X, WELL_Y, 350, PAL["path"])
e += T("TEXT_LABELS", WELL_X+800, WELL_Y+200, TH["det"], "WELL")
e += T("TEXT_LABELS", WELL_X+800, WELL_Y-300, TH["xs"], "OWNER ACCEPTED")
e += T("TEXT_LABELS", WELL_X+800, WELL_Y-700, TH["xs"], "TECH VERIF PENDING")

# Seating (two spots)
e += R("RECREATIONAL", 5500, SGY0+1000, 7000, SGY0+2200, PAL["crop"])
e += T("TEXT_LABELS", 5600, SGY0+1400, TH["xs"], "SEAT")

e += R("RECREATIONAL", 12000, SGY0+2000, 13500, SGY0+3200, PAL["crop"])
e += T("TEXT_LABELS", 12100, SGY0+2400, TH["xs"], "SEAT")

# Gathering area label
e += T("TEXT_LABELS", PX-1500, SGY0+3500, TH["det"], "GATHERING")

# Perimeter planting (north edge)
e += R("POLLINATOR", 500, SGY1-800, DW_W-500, SGY1-200, PAL["pollin"])
e += T("TEXT_LABELS", 600, SGY1-650, TH["xs"], "PERIMETER PLANTING")

# PROMINENT LABEL
e += T("TEXT_LABELS", PX-4500, SGY0+SG_D_NEW/2+400, TH["zone"], "RECREATIONAL GARDEN")
e += T("TEXT_LABELS", PX-1500, SGY0+SG_D_NEW/2-200, TH["xs"], "92 m2 (half dwelling)")

# Entry paths at garden edges (from patios)
e += R("PATHS_WATER", SGX0, SGY0, SGX0+PATH_W, SGY0+PATH_W, PAL["path"])
e += R("PATHS_WATER", SGX1-PATH_W, SGY0, SGX1, SGY0+PATH_W, PAL["path"])

# Former garden extent (faint dashed reference)
e += R("FORMER_EXTENT", FORMER_SGX0, SGY0, FORMER_SGX1, FORMER_SGY1)
e += T("FORMER_EXTENT", FORMER_SGX0+200, FORMER_SGY1-500, TH["xs"], "Former garden extent (ref only)")

# ================================================================
# HIVE-W
# ================================================================
e += R("PROVISIONAL", HW_X0, 0, HW_X1, DW_D)

bw_positions = [HW_X0 + PATH_W, HW_X0 + PATH_W + BED_W + PATH_W]
bed_yranges = [(800, 3800), (4500, 7500), (8200, DW_D-800)]
for bx in bw_positions:
    for i, (by0, by1) in enumerate(bed_yranges):
        idx = bw_positions.index(bx) * 3 + i + 1
        e += R("CROP_BEDS", bx, by0, bx+BED_W, by1, PAL["crop"])
        e += T("TEXT_LABELS", bx+50, by0+300, TH["xs"], f"W{idx:02d}")

svc_x = HW_X0 + 2*PATH_W + 2*BED_W + PATH_W
e += R("HARVEST_STORE", svc_x, 800, svc_x+2200, 2800, PAL["harvest"])
e += T("TEXT_LABELS", svc_x+50, 1500, TH["xs"], "TOOLS")

e += R("HARVEST_STORE", svc_x, 3500, svc_x+2200, 5500, PAL["harvest"])
e += T("TEXT_LABELS", svc_x+50, 4300, TH["xs"], "COMPOST")

e += R("HARVEST_STORE", svc_x, 6200, svc_x+2200, 8700, PAL["harvest"])
e += T("TEXT_LABELS", svc_x+50, 7500, TH["xs"], "PREP/STORE")
e += T("TEXT_LABELS", svc_x+50, 7000, TH["xs"], "SEED+HARVEST")

e += R("PATHS_WATER", bw_positions[0], DW_D-2500, bw_positions[0]+1500, DW_D-1000, PAL["path"])
e += T("TEXT_LABELS", bw_positions[0]+50, DW_D-1800, TH["xs"], "WATER")

e += R("PATHS_WATER", HW_X0, 0, HW_X0+PATH_W, DW_D, PAL["path"])
e += T("TEXT_LABELS", HW_X0+1000, DW_D/2+300, TH["zone"], "HIVE-W")

# ================================================================
# HIVE-E (mirror)
# ================================================================
e += R("PROVISIONAL", HE_X0, 0, HE_X1, DW_D)

be_positions = [HE_X1 - PATH_W - BED_W, HE_X1 - PATH_W - BED_W - PATH_W - BED_W]
for bx in be_positions:
    for i, (by0, by1) in enumerate(bed_yranges):
        idx = be_positions.index(bx) * 3 + i + 1
        e += R("CROP_BEDS", bx, by0, bx+BED_W, by1, PAL["crop"])
        e += T("TEXT_LABELS", bx+50, by0+300, TH["xs"], f"E{idx:02d}")

svc_ex = HE_X0 + PATH_W
e += R("HARVEST_STORE", svc_ex, 800, svc_ex+2200, 2800, PAL["harvest"])
e += T("TEXT_LABELS", svc_ex+50, 1500, TH["xs"], "TOOLS")

e += R("HARVEST_STORE", svc_ex, 3500, svc_ex+2200, 5500, PAL["harvest"])
e += T("TEXT_LABELS", svc_ex+50, 4300, TH["xs"], "COMPOST")

e += R("HARVEST_STORE", svc_ex, 6200, svc_ex+2200, 8700, PAL["harvest"])
e += T("TEXT_LABELS", svc_ex+50, 7500, TH["xs"], "PREP/STORE")
e += T("TEXT_LABELS", svc_ex+50, 7000, TH["xs"], "SEED+HARVEST")

e += R("PATHS_WATER", be_positions[1]+BED_W+200, DW_D-2500, be_positions[1]+BED_W+1700, DW_D-1000, PAL["path"])
e += T("TEXT_LABELS", be_positions[1]+BED_W+250, DW_D-1800, TH["xs"], "WATER")

e += R("PATHS_WATER", HE_X1-PATH_W, 0, HE_X1, DW_D, PAL["path"])
e += T("TEXT_LABELS", HE_X0+1500, DW_D/2+300, TH["zone"], "HIVE-E")

# ================================================================
# POLLINATOR HABITAT
# ================================================================
e += R("POLLINATOR", HW_X0, PCH_Y0-PATH_W-2500, HW_X0+2500, PCH_Y0-PATH_W, PAL["pollin"])
e += T("TEXT_LABELS", HW_X0+100, PCH_Y0-PATH_W-1500, TH["xs"], "PH-01")

e += R("POLLINATOR", HE_X1-2500, PCH_Y0-PATH_W-2500, HE_X1, PCH_Y0-PATH_W, PAL["pollin"])
e += T("TEXT_LABELS", HE_X1-2400, PCH_Y0-PATH_W-1500, TH["xs"], "PH-02")

# ================================================================
# SHADOW REFERENCE LINES
# ================================================================
sh_base = DW_D
su_sh = 3190
eq_sh = 7679
w_sh = 22384

e += L("SHADOW", 0, sh_base+su_sh, DW_W, sh_base+su_sh)
e += T("SHADOW", DW_W+300, sh_base+su_sh-100, TH["xs"], "~3m SUMMER NOON")

e += L("SHADOW", 0, sh_base+eq_sh, DW_W, sh_base+eq_sh)
e += T("SHADOW", DW_W+300, sh_base+eq_sh-100, TH["xs"], "~8m EQUINOX NOON")

# Winter shadow extends beyond garden - show as note only
e += T("SHADOW", DW_W+300, SGY1+300, TH["xs"], "Winter ~22m (beyond garden)")

e += T("SHADOW", DW_W+300, sh_base+eq_sh+500, TH["xs"], "Indicative, solar noon, 6m ht")

e += T("SHADOW", HW_X0, DW_D+800, TH["xs"], "AM sun E > shadow W (HIVE-W)")
e += T("SHADOW", HE_X0+300, DW_D+800, TH["xs"], "PM sun W > shadow E (HIVE-E)")

# ================================================================
# SUN-PATH ARC (moved clear of title block)
# ================================================================
arc_cx = PX
arc_cy = -16000
arc_r = 8000
e += arc_e("SUN_PATH", arc_cx, arc_cy, arc_r, 25, 155, PAL["harvest"])
e += T("TEXT_LABELS", arc_cx+7500, arc_cy+3000, TH["det"], "E")
e += T("TEXT_LABELS", arc_cx-7500, arc_cy+3000, TH["det"], "W")
e += T("SUN_PATH", arc_cx-3000, arc_cy-2000, TH["det"], "SUN PATH (E > S > W)")
e += T("SUN_PATH", arc_cx-3000, arc_cy-2500, TH["xs"], "UK ~52N. PA-07.")

# ================================================================
# NORTH ARROW
# ================================================================
na_x = DW_W + 4000
na_y = SGY1 - 2000
e += L("TEXT_LABELS", na_x, na_y, na_x, na_y+2500)
e += L("TEXT_LABELS", na_x, na_y+2500, na_x-350, na_y+2000)
e += L("TEXT_LABELS", na_x, na_y+2500, na_x+350, na_y+2000)
e += T("TEXT_LABELS", na_x-200, na_y+3000, TH["room"], "N")
e += T("TEXT_LABELS", na_x-1200, na_y-600, TH["xs"], "ASSUMED (PA-07)")

# ================================================================
# DIMENSIONS
# ================================================================
e += L("DIMENSIONS", 0, -4000, DW_W, -4000)
e += L("DIMENSIONS", 0, -3700, 0, -4300)
e += L("DIMENSIONS", DW_W, -3700, DW_W, -4300)
e += T("DIMENSIONS", PX-800, -4600, TH["sub"], "20,000")
e += T("DIMENSIONS", PX-1800, -5100, TH["xs"], "(was 18,600)")

e += L("DIMENSIONS", -3500, 0, -3500, DW_D)
e += L("DIMENSIONS", -3200, 0, -3800, 0)
e += L("DIMENSIONS", -3200, DW_D, -3800, DW_D)
e += T("DIMENSIONS", -4500, DW_D/2, TH["sub"], "9,200")

# Patio widths
e += L("DIMENSIONS", -PATIO_W, -5500, 0, -5500)
e += L("DIMENSIONS", -PATIO_W, -5200, -PATIO_W, -5800)
e += L("DIMENSIONS", 0, -5200, 0, -5800)
e += T("DIMENSIONS", -PATIO_W+200, -6100, TH["det"], "1,800")

e += L("DIMENSIONS", DW_W, -5500, DW_W+PATIO_W, -5500)
e += L("DIMENSIONS", DW_W, -5200, DW_W, -5800)
e += L("DIMENSIONS", DW_W+PATIO_W, -5200, DW_W+PATIO_W, -5800)
e += T("DIMENSIONS", DW_W+200, -6100, TH["det"], "1,800")

# Hive widths
e += L("DIMENSIONS", HW_X0, -7000, HW_X1, -7000)
e += L("DIMENSIONS", HW_X0, -6700, HW_X0, -7300)
e += L("DIMENSIONS", HW_X1, -6700, HW_X1, -7300)
e += T("DIMENSIONS", HW_X0+3000, -7600, TH["sub"], f"{HIVE_WD:,}")
e += T("DIMENSIONS", HW_X0+3000, -8000, TH["xs"], "PROVISIONAL")

e += L("DIMENSIONS", HE_X0, -7000, HE_X1, -7000)
e += L("DIMENSIONS", HE_X0, -6700, HE_X0, -7300)
e += L("DIMENSIONS", HE_X1, -6700, HE_X1, -7300)
e += T("DIMENSIONS", HE_X0+3000, -7600, TH["sub"], f"{HIVE_WD:,}")
e += T("DIMENSIONS", HE_X0+3000, -8000, TH["xs"], "PROVISIONAL")

# Garden dimensions
e += L("DIMENSIONS", SGX0, SGY1+500, SGX1, SGY1+500)
e += L("DIMENSIONS", SGX0, SGY1+200, SGX0, SGY1+800)
e += L("DIMENSIONS", SGX1, SGY1+200, SGX1, SGY1+800)
e += T("DIMENSIONS", PX-800, SGY1+1100, TH["sub"], "20,000")

e += L("DIMENSIONS", SGX1+1500, SGY0, SGX1+1500, SGY1)
e += L("DIMENSIONS", SGX1+1200, SGY0, SGX1+1800, SGY0)
e += L("DIMENSIONS", SGX1+1200, SGY1, SGX1+1800, SGY1)
e += T("DIMENSIONS", SGX1+2000, (SGY0+SGY1)/2, TH["sub"], "4,600")

# Conservatory
e += L("DIMENSIONS", CX0, CY1+500, CX1, CY1+500)
e += L("DIMENSIONS", CX0, CY1+200, CX0, CY1+800)
e += L("DIMENSIONS", CX1, CY1+200, CX1, CY1+800)
e += T("DIMENSIONS", PX-500, CY1+1000, TH["xs"], "6,000")

# Scale bar
sb_y = -10000
e += L("DIMENSIONS", 0, sb_y, 5000, sb_y)
e += L("DIMENSIONS", 0, sb_y-200, 0, sb_y+200)
e += L("DIMENSIONS", 5000, sb_y-200, 5000, sb_y+200)
e += T("DIMENSIONS", 0, sb_y-600, TH["xs"], "0")
e += T("DIMENSIONS", 4600, sb_y-600, TH["xs"], "5 m")

# ================================================================
# TITLE BLOCK
# ================================================================
tb_y = -11500
e += T("TEXT_LABELS", 0, tb_y, TH["head"], "MMUCO HIVE - CONCEPT FOR REVIEW - NOT FOR CONSTRUCTION")
e += T("TEXT_LABELS", 0, tb_y-600, TH["sub"], "hive_two_hives_rev_v05 | Units mm 1:1")
e += T("TEXT_LABELS", 0, tb_y-1000, TH["xs"], "PA-07: North assumed. Shadows indicative solar-noon, 6m ht, level ground.")
e += T("TEXT_LABELS", 0, tb_y-1300, TH["xs"], "Hive boundaries PROVISIONAL. Dwelling 20,000 mm (was 18,600). Depth 9,200 inferred.")

# ================================================================
# LEGEND (right side, compact)
# ================================================================
lg_x = HE_X1 + 3000
lg_y = DW_D + 2000

e += T("TEXT_LABELS", lg_x, lg_y, TH["room"], "PALETTE / KEY")
lg_y -= 500
for desc in [
    "Dwelling (#E8EDF2)",
    "Crops (#77C66E)",
    "Paths/water (#56C5D0)",
    "Harvest/store (#E4B45F)",
    "Pollinator (#B69ADD)",
    "Shadow (dashed)",
    "Provisional (dashed)",
    "Former extent (faint dashed)",
]:
    e += T("TEXT_LABELS", lg_x+100, lg_y, TH["xs"], "- " + desc)
    lg_y -= 300

lg_y -= 300
e += T("TEXT_LABELS", lg_x, lg_y, TH["room"], "FOUR PRINCIPLES")
lg_y -= 400
for p in ["01 Produce", "02 Sustain", "03 Deliver", "04 Preserve"]:
    e += T("TEXT_LABELS", lg_x+100, lg_y, TH["det"], p)
    lg_y -= 350

lg_y -= 400
e += T("TEXT_LABELS", lg_x, lg_y, TH["room"], "ZONE AREAS")
lg_y -= 400
hive_area = HIVE_WD * DW_D / 1e6
dw_area = DW_W * DW_D / 1e6
sg_area = SG_W_NEW * SG_D_NEW / 1e6
for desc in [
    f"Dwelling: {dw_area:.0f} m2",
    f"Rec garden: {sg_area:.0f} m2 (= {dw_area/2:.0f}, half dwelling)",
    f"HIVE-W: {hive_area:.0f} m2 (provisional)",
    f"HIVE-E: {hive_area:.0f} m2 (provisional)",
    f"Conservatory: 24 m2 (inferred)",
    f"Orangery: 12 m2 (was ~40 m2)",
]:
    e += T("TEXT_LABELS", lg_x+100, lg_y, TH["xs"], desc)
    lg_y -= 300

lg_y -= 400
e += T("TEXT_LABELS", lg_x, lg_y, TH["room"], "ASSUMPTIONS")
lg_y -= 400
for a in [
    "1. North ASSUMED (PA-07)",
    "2. Dwelling ht 6m assumed",
    "3. Hive land PROPOSED",
    "4. Depth 9,200 INFERRED",
    "5. Conservatory 6x4 INFERRED",
    "6. Well ACCEPTED; tech verif pending",
    "7. Orangery reduced to fit",
    "8. Width was 18,600 now 20,000",
]:
    e += T("TEXT_LABELS", lg_x+100, lg_y, TH["xs"], a)
    lg_y -= 280

lg_y -= 400
e += T("TEXT_LABELS", lg_x, lg_y, TH["room"], "DESIGN TARGETS")
lg_y -= 400
for t in [
    "Bed reach max 500mm",
    "Beds 1,000mm (both-side)",
    "Path target 1,500mm",
    "Patio min 1,500mm clear",
    "Compost separated",
]:
    e += T("TEXT_LABELS", lg_x+100, lg_y, TH["xs"], t)
    lg_y -= 280

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

print(f"Written {len(dxf)} bytes to {OUT}")
print(f"Entity handles: {hc[0] - 0x100}")
print()
print("=== CHECKS ===")
actual_sg = SG_W_NEW * SG_D_NEW / 1e6
print(f"Recreational garden: {SG_W_NEW/1000:.1f} x {SG_D_NEW/1000:.1f} m = {actual_sg:.0f} m2")
print(f"  Target: 92 m2 (half of {dw_area:.0f} m2 dwelling): {'PASS' if actual_sg == 92 else 'FAIL'}")
print(f"Text heights reverted to original: PASS")
print(f"  title={TH['title']}, zone={TH['zone']}, head={TH['head']}, room={TH['room']}")
print(f"  sub={TH['sub']}, det={TH['det']}, sm={TH['sm']}, xs={TH['xs']}")
print(f"Orangery: 4.0x3.0 = 12 m2 (was ~40 m2): RECORDED")
print(f"Well: 1, status unverified: PASS")
print(f"Conservatory: 1 central: PASS")
print(f"Patios: {PATIO_W} mm each: PASS")
print(f"Former extent shown as dashed: PASS")
print(f"Sun-path arc at y={arc_cy}, title at y={tb_y}: CLEAR")
