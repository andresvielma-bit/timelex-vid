"""Genera pistas de música con MusicGen (local, sin cuentas).

Uso (tarda varios minutos en CPU; la primera vez descarga ~300 MB):
  uv run --no-project --with truststore --with "transformers<5" --with torch --with soundfile \
      --with numpy --with scipy python -I musicgen.py <carpeta_salida> [semilla]
Escribe opcion-a.wav, opcion-b.wav, opcion-c.wav (~30 s cada una).
Con otra semilla (por defecto 11) salen pistas distintas con los mismos estilos: así cada video tiene su música.
Para otro estilo, cambiar los textos de PROMPTS (en inglés, con instrumentos y BPM).
"""
import sys
from pathlib import Path

import truststore

truststore.inject_into_ssl()  # la red corporativa re-firma HTTPS: usar los certificados de Windows

import numpy as np
import soundfile as sf
import torch
from transformers import AutoProcessor, MusicgenForConditionalGeneration

PROMPTS = {
    "opcion-a": "modern trap hip hop instrumental, punchy 808 bass, crisp fast hi-hats, dark luxury vibe, confident and catchy, 140 bpm",
    "opcion-b": "upbeat afro house groove, energetic percussion, catchy plucked synth hook, luxury fashion vibe, 122 bpm",
    "opcion-c": "smooth hip hop r&b instrumental, groovy bass, elegant electric piano chords, punchy drums, 96 bpm",
}

out = Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)
torch.manual_seed(int(sys.argv[2]) if len(sys.argv) > 2 else 11)
proc = AutoProcessor.from_pretrained("facebook/musicgen-small")
model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
sr = model.config.audio_encoder.sampling_rate
inputs = proc(text=list(PROMPTS.values()), padding=True, return_tensors="pt")
with torch.no_grad():
    audio = model.generate(**inputs, do_sample=True, guidance_scale=3.5, max_new_tokens=1500)
for name, wav in zip(PROMPTS, audio):
    data = wav[0].cpu().numpy().astype(np.float32)
    sf.write(out / f"{name}.wav", data, sr)
    print("ok", name, f"{len(data) / sr:.1f}s", flush=True)
