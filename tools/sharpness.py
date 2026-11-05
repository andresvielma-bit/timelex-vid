"""Mide la nitidez (varianza del Laplaciano) de clips o de ventanas de un archivo fuente.

Uso:
  python sharpness.py clips <carpeta>                    -> nitidez media y mínima de cada clip
  python sharpness.py scan <video> <ini> <fin> <largo>   -> mejores ventanas de <largo> s entre ini y fin

Se mide sobre el 60 % central del cuadro (donde está el reloj), a 540 px de ancho.
Más alto = más nítido. Por debajo de ~60-70 % de la mejor toma del mismo material suele verse blando.
"""
import sys
from pathlib import Path

import cv2
import numpy as np


def sharp(frame):
    h, w = frame.shape[:2]
    scale = 540 / w
    g = cv2.cvtColor(cv2.resize(frame, (540, int(h * scale))), cv2.COLOR_BGR2GRAY)
    H, W = g.shape
    c = g[int(H * 0.2):int(H * 0.8), int(W * 0.2):int(W * 0.8)]
    return cv2.Laplacian(c, cv2.CV_64F).var()


def read(path, t0=0.0, t1=None, step=0.1):
    cap = cv2.VideoCapture(str(path))
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    t1 = t1 if t1 is not None else n / fps
    out = []
    t = t0
    while t < t1:
        cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000)
        ok, f = cap.read()
        if not ok:
            break
        out.append((t, sharp(f)))
        t += step
    return out


if sys.argv[1] == "clips":
    for p in sorted(Path(sys.argv[2]).glob("*.mp4")):
        v = [s for _, s in read(p, step=0.1)]
        print(f"{p.stem}: media {np.mean(v):6.0f}  min {np.min(v):6.0f}")
else:
    path, a, b, L = sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
    vals = read(path, a, b, step=0.1)
    k = int(round(L / 0.1))
    wins = []
    for i in range(0, len(vals) - k + 1):
        seg = [s for _, s in vals[i:i + k]]
        wins.append((min(seg), np.mean(seg), vals[i][0]))
    wins.sort(reverse=True)
    picked = []
    for w in wins:
        if all(abs(w[2] - p[2]) > L for p in picked):
            picked.append(w)
        if len(picked) == 5:
            break
    print(Path(path).name)
    for mn, me, t in picked:
        print(f"  desde {t:6.2f}s  min {mn:6.0f}  media {me:6.0f}")
