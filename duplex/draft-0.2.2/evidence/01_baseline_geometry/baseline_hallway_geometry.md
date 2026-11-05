# Draft 0.2.2: baseline hallway geometry (read from `WORKING_COPY_from_Draft_0.2.1.dxf`, before any change)

- **Hallway (circulation spine):** clear 1500 mm wide (x 4400–5900) x 6600 mm long (y 300–6900) = 9.9 m2. Narrowest clear width 1500 mm along its whole length (parallel faces; no fixed object inside).
- **Room A = BEDROOM 1** (west of hall): bbox 300, 300, 4300, 4000; 4 x 3.7 m = 14.8 m2.
- **Room B = BEDROOM 2** (east of hall): bbox 6000, 300, 9200, 4300; 3.2 x 4 m = 12.8 m2.

## Walls between the hall and the rooms

| Side | Handle | Layer | x range | y range |
|---|---|---|---|---|
| West (hall/Room A, quiet room, store) | 127 | A-WALL-INT | 4300–4400 | 300–2800 |
| West (hall/Room A, quiet room, store) | 129 | A-WALL-INT | 4300–4400 | 3800–4300 |
| West (hall/Room A, quiet room, store) | 12B | A-WALL-INT | 4300–4400 | 5300–7400 |
| East (hall/Room B, bathroom) | 131 | A-WALL-INT | 5900–6000 | 300–2800 |
| East (hall/Room B, bathroom) | 133 | A-WALL-INT | 5900–6000 | 3800–5000 |
| East (hall/Room B, bathroom) | 135 | A-WALL-INT | 5900–6000 | 6000–6900 |

## Openings in the hall side walls

| Side | y range | Width | Door (arc, hinge, leaf, angles, leaf line) |
|---|---|---|---|
| W | 2800–3800 | 1000 | arc 16E, hinge (4300,3800), leaf 1000, 180°→270°, line 16C |
| W | 4300–5300 | 1000 | arc 172, hinge (4300,4300), leaf 1000, 90°→180°, line 170 |
| E | 2800–3800 | 1000 | arc 176, hinge (6000,3800), leaf 1000, 270°→0°, line 174 |
| E | 5000–6000 | 1000 | arc 17A, hinge (5900,6000), leaf 1000, 180°→270°, line 178 |

## Objects near the entries

- Room A side (x 2800–4300, y 2300–4000): 1C0 A-FURN [2550,3600,3000,4000]; 1C2 A-FURN [3700,600,4300,2400]
- Room B side (x 6000–7500, y 2300–4300): 1C6 A-FURN [7300,1325,9200,2675]; 1D2 A-FURN [7200,3700,9000,4300]
- Inside the hall: 218 A-ACCS [4400,1310,5900,2810]
