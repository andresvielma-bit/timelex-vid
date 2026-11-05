import sys
import librosa
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

paths = sys.argv[1:-1]
fig, axes = plt.subplots(len(paths), 1, figsize=(14, 3.2 * len(paths)))
for ax, p in zip(axes, paths):
    y, sr = librosa.load(p, sr=32000)
    onset = librosa.onset.onset_strength(y=y, sr=sr)
    tempo, beats = librosa.beat.beat_track(onset_envelope=onset, sr=sr, units="time")
    ac = librosa.autocorrelate(onset - onset.mean())
    ac = ac / ac[0]
    lag = int(round(60 / float(np.atleast_1d(tempo)[0]) * sr / 512))
    pulse = float(ac[lag]) if lag < len(ac) else 0
    ibi = np.diff(beats)
    rms = librosa.feature.rms(y=y, hop_length=16000)[0]
    db = 20 * np.log10(rms + 1e-9)
    cent = float(np.mean(librosa.feature.spectral_centroid(y=y, sr=sr)))
    low = float(np.mean(np.abs(librosa.stft(y))[:20]))
    print(f"{p.split(chr(92))[-1]}: tempo {float(np.atleast_1d(tempo)[0]):.0f}  beats {len(beats)}  "
          f"beat-interval std {np.std(ibi)*1000:.0f}ms  pulse {pulse:.2f}  centroid {cent:.0f}Hz  "
          f"RMS/0.5s min {db.min():.0f} max {db.max():.0f}")
    S = librosa.amplitude_to_db(np.abs(librosa.stft(y, n_fft=2048, hop_length=512)), ref=np.max)
    librosa.display.specshow(S, sr=sr, hop_length=512, x_axis="time", y_axis="log", ax=ax) if hasattr(librosa, "display") else ax.imshow(S, aspect="auto", origin="lower")
    for b in beats:
        ax.axvline(b, color="w", alpha=0.25, lw=0.6)
    ax.set_title(p.split(chr(92))[-1])
plt.tight_layout()
plt.savefig(sys.argv[-1], dpi=70)
