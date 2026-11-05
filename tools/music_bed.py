"""Convierte una pista en la cama musical del video.

- Busca un golpe fuerte de la pista y lo alinea con DROP (el reveal del reloj).
- Antes del drop la música suena apagada (pasa-bajos + más baja) -> "tranquila".
- En el drop se abre completa -> "agarra ritmo".
- Debajo de la voz baja sola (ducking) y termina con un fade corto.

Uso:
  uv run --no-project --with librosa python -I music_bed.py <pista.wav> <voz.wav> <salida.wav> \
      --dur 28 --drop 3.85 [--hit 3.76]

  --dur   duración del video (s)
  --drop  segundo del video donde está el giro (sale el reloj)
  --hit   segundo de la pista que debe caer en el giro (un golpe fuerte tras un silencio).
          Sin --hit se elige el beat con más graves entre 4 y 12 s de la pista.
"""
import argparse
import wave

import librosa
import numpy as np
from scipy.signal import butter, sosfilt

ap = argparse.ArgumentParser()
ap.add_argument("src")
ap.add_argument("voice")
ap.add_argument("out")
ap.add_argument("--dur", type=float, required=True)
ap.add_argument("--drop", type=float, required=True)
ap.add_argument("--hit", type=float)
args = ap.parse_args()

SR = 48000
DUR = args.dur
DROP = args.drop
src, voice_path, out_path = args.src, args.voice, args.out

y, _ = librosa.load(src, sr=SR, mono=True)

# Pista corta: repetirla con un cruce de 0,5 s para cubrir el video desde el punto elegido
def loop_to(y, n):
    xf = int(0.5 * SR)
    out = y.copy()
    while len(out) < n:
        a, b = out[-xf:], y[:xf]
        ramp = np.linspace(0, 1, xf)
        out = np.concatenate([out[:-xf], a * (1 - ramp) + b * ramp, y[xf:]])
    return out

# Golpes: el beat con más energía en graves entre 4 s y 12 s de la pista será el drop
tempo, beats = librosa.beat.beat_track(y=y, sr=SR, units="time")
low = sosfilt(butter(4, 150, "low", fs=SR, output="sos"), y)
def low_energy(t):
    i = int(t * SR)
    return float(np.sqrt(np.mean(low[i:i + int(0.12 * SR)] ** 2))) if i < len(low) else 0
cands = [b for b in beats if 4.0 <= b <= 12.0] or list(beats)
hit = args.hit if args.hit is not None else max(cands, key=low_energy)  # o el golpe que se indique
offset = hit - DROP  # segundo de la pista que cae en t=0 del video
if offset < 0:  # el golpe está antes del drop: se agrega silencio al inicio
    y = np.concatenate([np.zeros(int(-offset * SR) + 1), y])
    offset = 0.0
print(f"tempo ~{float(np.atleast_1d(tempo)[0]):.0f} BPM, drop de la pista en {hit:.2f}s, offset {offset:.2f}s")

need = int((DUR + max(0, offset)) * SR) + SR
y = loop_to(y, need)
start = int(offset * SR)
seg = y[start:start + int(DUR * SR)]
seg = np.pad(seg, (0, int(DUR * SR) - len(seg)))
t = np.arange(len(seg)) / SR

# Intro apagada: pasa-bajos a 350 Hz que se abre en los últimos 0,6 s antes del drop
muffled = sosfilt(butter(2, 350, "low", fs=SR, output="sos"), seg)
mix = np.clip((t - (DROP - 0.6)) / 0.6, 0, 1) ** 2
mix[t >= DROP] = 1.0
bed = muffled * (1 - mix) + seg * mix
bed *= np.where(t < DROP, 0.75, 1.0)
# entrada suave
bed *= np.clip(t / 0.15, 0, 1)

# Ducking bajo la voz (ataque 40 ms, relajación 250 ms, -6 dB)
with wave.open(voice_path) as w:
    ch, fr = w.getnchannels(), w.getframerate()
    v = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
v = v.reshape(-1, ch).mean(axis=1)
if fr != SR:
    v = np.interp(np.arange(int(len(v) * SR / fr)) / SR, np.arange(len(v)) / fr, v)
v = np.pad(v, (0, max(0, len(bed) - len(v))))[:len(bed)]
win = int(0.03 * SR)
rms = np.sqrt(np.convolve(v ** 2, np.ones(win) / win, mode="same"))
speaking = (rms > 0.02).astype(float)
env = np.zeros(len(bed))
acc = 0.0
att, rel = np.exp(-1 / (0.04 * SR)), np.exp(-1 / (0.25 * SR))
for i in range(len(bed)):
    c = att if speaking[i] > acc else rel
    acc = c * acc + (1 - c) * speaking[i]
    env[i] = acc
duck = 1 - 0.5 * env
duck = np.where((t >= DROP - 0.05) & (t < DROP + 0.45), np.maximum(duck, 0.85), duck)
bed *= duck

# Final: fade de 0,7 s
bed *= np.clip((DUR - t) / 0.7, 0, 1)

# Nivel: el tramo después del drop queda ~ -24 LUFS aprox. (RMS objetivo), con pico máximo -2 dBFS
post = bed[t >= DROP]
rms_post = np.sqrt(np.mean(post ** 2))
bed *= (10 ** (-23 / 20)) / max(rms_post, 1e-9)
peak = np.max(np.abs(bed))
if peak > 0.79:
    bed *= 0.79 / peak

out = (np.stack([bed, bed], axis=1) * 32767).astype(np.int16)
with wave.open(out_path, "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(out.tobytes())
print("ok", out_path)
