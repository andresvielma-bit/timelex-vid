"""Transcribe audio en español con tiempos por palabra (faster-whisper, local).

Uso (desde la carpeta del proyecto):
  uv run --no-project --with faster-whisper --with truststore python -I tools/transcribe.py <audio.wav> [<audio2.wav> ...]

- Acepta WAV (pasar antes cualquier otro formato por ffmpeg: -ac 1 -ar 16000).
- El audio se pasa como arreglo numpy porque la versión de `av` que instala uv no acepta
  el parámetro que usa faster-whisper para abrir archivos.
- `truststore` es necesario en esta red: re-firma HTTPS y sin él falla la descarga del modelo.
- Imprime cada frase con sus tiempos y guarda <primer_audio>.transcripts.json con las palabras.
- Los inicios de palabra de whisper suelen ir ~0,1-0,2 s adelantados: para cortes exactos,
  cruzarlos con `ffmpeg -af silencedetect=noise=-35dB:d=0.06`.
"""
import json
import sys
import wave

import truststore

truststore.inject_into_ssl()

import numpy as np
from faster_whisper import WhisperModel

model = WhisperModel("small", device="cpu", compute_type="int8")
out = {}
for path in sys.argv[1:]:
    with wave.open(path) as w:
        ch = w.getnchannels()
        audio = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    if ch > 1:
        audio = audio.reshape(-1, ch).mean(axis=1)
    segs, _ = model.transcribe(audio, language="es", word_timestamps=True)
    rows = []
    for s in segs:
        rows.append({"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip(),
                     "words": [[round(w.start, 2), round(w.end, 2), w.word.strip()] for w in s.words]})
    out[path] = rows
    print(f"== {path}", flush=True)
    for r in rows:
        print(f"[{r['start']:6.2f}-{r['end']:6.2f}] {r['text']}", flush=True)
        print("   " + " | ".join(f"{a:.2f} {t}" for a, _, t in r["words"]), flush=True)
json.dump(out, open(sys.argv[1] + ".transcripts.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
