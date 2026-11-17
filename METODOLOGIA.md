# Metodología de videos de venta — Timelex

Manual para hacer los videos de la tienda con HyperFrames. Sale del análisis del video viral (`Refs/3093309729997810150.mp4`, ~50 mil likes), de las otras referencias de `Refs/` y de las tres versiones del primer video (Nibosi 2628) con tus correcciones.

Hay dos tipos de reglas:
- **Fijas:** se cumplen en todos los videos (duración, cortes, nitidez, giro de la música, efectos, texto).
- **Flexibles:** cambian según el estilo del video (el tipo de hook, el guion, qué beneficios se cuentan).

---

## 1. Reglas fijas

| # | Regla |
|---|---|
| 1 | **Duración:** ~28 s. Lo ideal es no pasar de 30 s; el tope absoluto es 35 s. |
| 0 | **Siempre se edita con HyperFrames** (skill `/hyperframes`): composición en `index.html`, revisión con `npx hyperframes check`/`snapshot` y render con `npx hyperframes render`. No se usan otros editores ni se arma el video solo con ffmpeg (ffmpeg es solo para preparar tomas, voz y el volumen final). |
| 2 | **Duración de cada escena: mínimo 1,5 s, máximo 2 s, promedio entre 1,5 y 2 s.** Ninguna escena dura menos de 1,5 s, tampoco en el hook ni en los colores. Las escenas "bonitas" o más pausadas (la esfera, la toma de presentación) pueden llegar a **3 s como máximo**. Si una frase de la voz es muy corta para 1,5 s, se junta con la siguiente en la misma toma. |
| 3 | **Solo video, nunca fotos.** Si hace falta mostrar un detalle (día y fecha, broche), se hace un acercamiento sobre una toma de video. |
| 4 | **Solo tomas nítidas.** Se revisa el reloj de cerca en cada toma antes de usarla. Si se ve movido o desenfocado, se cambia. |
| 5 | **Nada de efectos sobre la imagen:** sin viñetas, sin fondos oscuros, sin filtros de "ambiente". Solo una corrección de color suave para que el acero brille. |
| 6 | **No se muestra la esfera antes del giro.** En el hook solo se ve la caja, la funda, la tarjeta y el paño. La esfera aparece por primera vez en el momento del giro. |
| 7 | **No van dos tomas casi iguales seguidas** (mismo video, mismo encuadre). |
| 8 | **La música arranca en el giro:** antes suena apagada y tranquila; en el giro entra completa con el ritmo. |
| 9 | **Siempre hay efectos de sonido** en el giro, en los cortes con movimiento y cuando aparece texto (ver § 7). |
| 10 | **Cada idea de la voz tiene su toma.** Si la voz dice "broche", se ve el broche; si dice "verde oliva", se ve solo el verde oliva. |
| 11 | **Etiquetas mínimas arriba** (precio, beneficios con ✅, colores, teléfono) **y siempre subtítulos de la voz abajo-centro** (ver § 6.1). |
| 12 | **El video termina en movimiento**, con la llamada a la acción en pantalla (el teléfono, o "Comenta LO QUIERO" en el formato sin precio ni teléfono); sin cuadro negro ni logo largo. |

---

## 2. Estructura del video

```
0 s          ~4 s                          ~18 s          ~24 s      ~28 s
|   HOOK     | GIRO + BENEFICIOS + COLORES  |  CONFIANZA   |  CIERRE   |
| misterio   | sale el reloj, drop musical  | caja, envío  | teléfono  |
```

Los tiempos son orientativos: mandan los de la voz grabada.

### 2.1 Hook (0 – ~4 s): misterio
- **Imagen:** 2–3 tomas (de 1,5–2 s cada una) que no muestran el reloj, elegidas entre: caja cerrada con el logo → abres la funda → caja interior o tarjeta → quitas el paño. El primer cuadro ya tiene movimiento.
- **Si no hay toma de la caja** con ese reloj (no sirve la caja de otro modelo ni la caja quieta al fondo del set): el hook se arma con **la correa, la tapa trasera y el broche**, sin que se vea la esfera, en cámara lenta suave (0,75x, columna `vel` del `edl.csv`) para que se sienta misterioso. Nunca se hace zoom sobre la caja que está de fondo en el set.
- **Encuadre:** acercamiento leve (1,2–1,3x) sobre la caja o la correa, con un empuje lento. La última toma antes del giro empuja más rápido (hasta ~1,55x).
- **Música:** tranquila (intro aparte de piano o pads) pero **se escucha**. Una subida (riser) crece hasta el giro.
- **Texto:** depende del tipo de hook (ver abajo).

**Tipos de hook (flexible):**

| Tipo | Cómo arranca la voz | Texto en pantalla | Referencia |
|---|---|---|---|
| **Precio** | "Por tan solo 49 a tasa del Banco Central…" | El precio en verde lima, escribiéndose | Viral (34$ BCV) |
| **Prueba** | "¿Lo destruí?" / la prueba de rayado o agua | Pregunta grande en blanco | `Refs/4dd297…` |
| **Aspiracional** | "Para verte elegante no necesitas un reloj de mil dólares…" | Frase corta | `Refs/599692…` |
| **Historia / curiosidad** | "Te voy a mostrar un reloj donde nada es de adorno…" | Frase corta | `Refs/fc23c5…` |
| **Lista / consejo** | "Antes de comprar un reloj, fíjate en estas tres cosas." Primero… segundo… y tercero (el reloj sale en el tercero) | La frase del hook en la mitad baja; luego cada punto con su número grande en verde lima (1, 2, 3) | Poedagar 970 |

### Formato sin precio ni teléfono (flexible)
Para que no todos los videos se vean iguales, se puede hacer un video que **no dice el precio, ni el número del modelo, ni muestra el teléfono**:
- El modelo se nombra como *"nuestro nuevo modelo de Poedagar"* (en pantalla, "Nuevo Poedagar").
- El cierre es *"Comenta 'lo quiero' y te envío el catálogo."* En pantalla, "Comenta 💬 / "LO QUIERO" (verde lima) / y te envío el catálogo" hasta el último cuadro, con un `chime` en "lo quiero".
- Con el formato lista, el giro cae más tarde (~10 s, en "y tercero"). Durante el hook suena la intro tranquila y cada número entra con un `click`.

Sea cual sea el hook, la voz arranca en el segundo 0, sin saludo ni silencio.

**Dónde va el precio (flexible):**
- **En el hook:** abre el video. Es lo que mejor funcionó en el viral.
- **Al cierre:** si el hook es otro (prueba, historia, aspiracional), el precio va justo antes de la llamada a la acción, como remate: *"…y todo esto por tan solo 49 a tasa del Banco Central. Escríbenos…"*. Se muestra con el mismo estilo (verde lima, grande, escribiéndose) y queda en pantalla junto con el teléfono, uno arriba del otro, hasta el final. Lleva un `pop` al aparecer.
- Si no se especifica, se pregunta cuál quiero antes de escribir el guion.

### 2.2 Giro (~4 s): sale el reloj
- Coincide con la frase que presenta el reloj ("te podrás llevar este…").
- **Imagen:** la mano levanta el reloj o el reloj aparece de golpe. Es la primera vez que se ve la esfera.
- **Transición: entrada rápida del reloj.** Destello blanco corto (0,3 s) + la imagen entra desde un zoom grande (1,6x) con un leve giro (−7° → 0°) y cae a 1x en ~0,42 s (`expo.out`). El reloj no puede "aparecer de la nada" con un corte simple. Es la única transición con efecto de todo el video.
- **Sonido:** termina la subida, entra un `whoosh-cinematic`, un golpe de bajo y un brillo, y **la música cambia en ese mismo cuadro de tranquila a movida** (se tiene que notar que "se activa").

### 2.3 Beneficios (~4 – 14 s)
- Una toma por beneficio, con su etiqueta y ✅ cuando la voz lo dice.
- Primero el nombre del modelo sobre la mejor toma en la muñeca.
- Los detalles (día y fecha, broche) se muestran con acercamiento sobre video, nunca con foto.
- Se pueden intercalar colores distintos del mismo modelo para que no se sienta repetido.
- Cierra con la toma "bonita" (hasta 3 s).

### 2.4 Colores (~14 – 18 s)
- "Lo tienes en…" → todos los colores juntos.
- Cada color nombrado → **solo ese color**, con su nombre en pantalla (`● Negro · Plateado`).
- Cortes de 1,5–2 s (nunca menos de 1,5 s), cada uno con un golpe de zoom (1,1x → 1x en 0,3 s) y un whoosh corto.
- Nunca "lo tienes en tres colores" sin decir cuáles.

### 2.5 Confianza (~18 – 24 s)
- Caja original, delivery gratis en Caracas, envíos nacionales por MRW o Zoom.
- Cada frase lleva su etiqueta con ✅ y su toma (la caja abierta con el reloj, el reloj en la mano, cerrando el broche en la muñeca).

### 2.6 Cierre (~24 – 28 s)
- "Escríbenos al número que ves en pantalla y pide el tuyo."
- Todos los colores juntos, en 2–3 cortes.
- El teléfono grande (**¡0422-029-1685!**) desde que empieza la frase hasta el último cuadro, con un chime al aparecer.

---

## 3. Guion

- **75–82 palabras** para ~28 s (se habla a ~2,8 palabras por segundo). Más de 85 pasa de 30 s.
- Frases cortas, en tú, con tu vocabulario: "viene con", "cuenta con", "le da un acabado súper elegante", "pide el tuyo".
- Solo beneficios que se puedan mostrar y que sean ciertos. Si no hay toma o no está confirmado, sale del guion.
- Los colores se nombran uno por uno.
- El cierre se mantiene: *"Escríbenos al número que ves en pantalla y pide el tuyo."*

### Plantilla (hook de precio)
```
[HOOK]      Por tan solo [PRECIO] a tasa del Banco Central, te podrás llevar este [MODELO].
[BENEF.]    Te marca [X], es [Y] y cuenta con [Z] que le da un acabado súper elegante.
[COLORES]   Lo tienes en [COLOR 1], en [COLOR 2], en [COLOR 3] y en [COLOR 4].
[CONFIANZA] Te llega en su caja original, con delivery gratis en toda Caracas y envíos nacionales por MRW o Zoom.
[CTA]       Escríbenos al número que ves en pantalla y pide el tuyo.
```
### Plantilla (otro hook, precio al cierre)
```
[HOOK]      [Frase de prueba / historia / aspiracional, máx. ~12 palabras, que no nombre el modelo todavía]
[GIRO]      Te presento el [MODELO]...   (aquí sale el reloj y entra la música)
[BENEF.]    Te marca [X], es [Y] y cuenta con [Z] que le da un acabado súper elegante.
[COLORES]   Lo tienes en [COLOR 1], en [COLOR 2] y en [COLOR 3].
[CONFIANZA] Te llega en su caja original, con delivery gratis en toda Caracas y envíos nacionales por MRW o Zoom.
[PRECIO]    Y todo esto por tan solo [PRECIO] a tasa del Banco Central.
[CTA]       Escríbenos al número que ves en pantalla y pide el tuyo.
```
El total sigue en 75–82 palabras: si el hook es más largo, se recorta un beneficio.

En los dos casos, el giro (la frase que presenta el reloj) es el punto donde se ve la esfera por primera vez y entra la música.

---

## 4. Tomas: qué grabar y cómo elegirlas

### Qué grabar por cada modelo
- La caja cerrada en las manos (logo visible), abriendo la funda, la caja interior o la tarjeta, quitando el paño.
- Sacando el reloj de la caja (la mano lo levanta).
- Cada color en la muñeca, quieto, de cerca (3–5 s por color).
- Cada color en la mano o en los dedos, de frente.
- Primer plano del detalle principal (día y fecha, cronógrafo, broche abriéndose y cerrándose).
- Todos los colores juntos en las manos (como `IMG_1689`).
- Si se puede: una prueba (rayado, agua) y una toma con luz natural afuera.

Tips de grabación: mover la muñeca despacio y dejar 2–3 s quieto en cada pose. Cuando el reloj se mueve rápido, la toma sale borrosa y no sirve.

### Cómo elegir el tramo de cada toma
1. Hacer una hoja de cuadros de cada video (§ 9, paso 3) para ver qué hay y en qué segundo.
2. Elegir tramos donde el reloj esté quieto y enfocado.
3. **Revisar nitidez a ojo**: recortar el reloj en 3 momentos de la toma (inicio, mitad, final). La medición automática (`tools/sharpness.py`) sirve de apoyo, pero la textura de la manga la engaña, así que manda la vista.
4. Comprobar que el hook no muestra ninguna esfera.

---

## 5. Transiciones y movimiento

| Momento | Qué se hace |
|---|---|
| Cortes normales | Corte seco, en el movimiento de la mano. |
| Hook | Encuadre 1,2–1,3x sobre la caja y empuje lento (+0,05 en la toma). La última toma del hook empuja más (hasta 1,42x). |
| Giro | Entrada rápida: destello blanco (opacidad 0,95 → 0 en 0,3 s) + zoom 1,6x → 1x con giro −7° → 0° en ~0,42 s (`expo.out`). |
| Toma después del giro | Pequeño golpe de zoom 1,08x → 1x. |
| Detalle (día y fecha) | Acercamiento de 1,15x a 2,1x en ~1,5 s, centrado en el detalle. Se extrae esa toma en 4K para que no pierda nitidez. |
| Broche | Acercamiento fijo de 1,35–1,45x sobre la zona de las manos. |
| Colores | Golpe de zoom 1,1x → 1x en 0,3 s en cada corte. |
| Tomas largas | Empuje lento de 1,0 a 1,05x. |
| Color sin toma propia | Si un color solo sale en la toma de todos juntos, se toma el tramo donde ese reloj pasa más cerca de la cámara y se hace un acercamiento de ~2,5x con un encuadre que lo va siguiendo (keyframes de `transformOrigin`), para que se vea solo y centrado. Ej.: el verde menta del Poedagar 821. |

---

## 6. Texto en pantalla

Fuente: **Montserrat** (`assets/fonts/Montserrat-VF.ttf`, licencia libre). Todo el texto lleva borde negro grueso y sombra para leerse sobre fondos claros.

| Tipo | Estilo | Posición | Cómo entra |
|---|---|---|---|
| Precio | Verde lima `#a8f43c`, 900, 150 px, borde 16 px | Arriba (y≈230) | Letra a letra, al ritmo de la voz ("49$" y luego " BCV") |
| Modelo | Blanco, 900, 82 px | Arriba (y≈300) | Letra a letra |
| Beneficio | Blanco, 800, 60 px + ✅ | Arriba (y≈300) | Letra a letra (~0,4 s) y el ✅ entra con un rebote |
| Color | Punto del color + nombre 74 px + material 50 px | Arriba | Aparece de golpe con un pequeño zoom |
| Teléfono | Blanco, 900, 104 px | Arriba | Letra a letra (~0,5 s) |

- Una sola etiqueta en pantalla a la vez.
- Las frases largas van en dos líneas armadas a mano ("Envíos Nacionales / por MRW o Zoom ✅"), nunca cortadas por el navegador.
- Fuera del 20 % de abajo y del borde derecho (botones de TikTok y Reels).
- ✅ y 💧 se dibujan como SVG dentro del HTML (no como emoji), para que se vean igual en el render.

### 6.1 Subtítulos (siempre)

Todos los videos llevan subtítulos de la voz, hechos en HyperFrames y sincronizados con los tiempos por palabra de la transcripción de la voz limpia (`tools/transcribe.py`).

| Aspecto | Cómo |
|---|---|
| Posición | **Centrados abajo, pero fuera de la zona prohibida**: el bloque va entre y≈1300 y y≈1450 (de 1920), centrado en x y con márgenes de ~120 px a cada lado (más a la derecha por los botones). Nunca en el 22 % de abajo (descripción, música y botones de TikTok/Reels) ni pegados al borde derecho. |
| Tamaño | Pequeños pero legibles: Montserrat 800, ~52–58 px, blanco con borde negro (~8 px) y sombra suave. Máximo una línea (dos solo si hace falta). |
| Ritmo | Dinámicos: grupos de 2–4 palabras que cambian con la voz; la palabra que se está diciendo se resalta (verde lima `#a8f43c` o un leve zoom 1,0 → 1,08). Cada grupo entra con un pop corto (escala 0,9 → 1 en ~0,12 s). |
| Texto | Lo que dice la voz, tal cual, con números como se muestran ("49$ BCV", "0422-029-1685"). Sin punto final. |
| Convivencia | Las etiquetas (precio, ✅, colores, teléfono) siguen arriba; los subtítulos nunca las tapan ni se duplican con ellas en la misma posición. |

Se revisan en los snapshots: que se lean sobre fondos claros, que no choquen con la mano/reloj principal y que no caigan en la zona de botones.

---

## 7. Sonido

### 7.1 Voz
- **Grabación:** tu voz, siguiendo el guion. Mejor con la app Notas de Voz del iPhone y enviando el archivo; la nota de voz de WhatsApp pierde agudos y suena "dentro de un pote".
- **Proceso** (`tools/voice.ps1`): **la voz no se modifica**.
  1. Se quita el silencio inicial y se acortan a ~0,1 s las pausas de más de 0,3 s. **Antes de cortar una pausa, se mira la envolvente de energía de esa zona** (no solo `silencedetect` ni el tiempo de whisper): las sílabas finales suaves ("to-**do**") quedan por debajo del umbral y se pierden. Después de procesar, se transcribe la voz limpia y se comprueba que estén todas las palabras del guion.
  2. Ganancia lineal (volumen parejo) hasta −16 LUFS o hasta −1 dBFS de pico, lo que llegue primero.
  3. Nada más: sin EQ, sin compresor, sin limitador y sin reducción de ruido.
- Después se vuelve a transcribir la voz limpia para sacar el tiempo exacto de cada palabra; los cortes y los textos se alinean a esos tiempos.

### 7.2 Música
- **Estructura:** antes del giro, una **intro tranquila** (piano o pads, sin batería) que se escucha bien; en el cuadro del giro entra la pista movida, sobre un golpe fuerte. El cambio de tranquila a emocionante se tiene que sentir.
  - Con dos pistas: `music_bed.py <movida> <voz> <salida> --intro <tranquila> --intro-gain -4 --duck 0.35 ...`
  - La versión vieja (la misma pista apagada con pasa-bajos) casi no se oía: no usarla con hooks largos.
- **Fuente:** sin servicios con login.
  - Tu propia canción, si me la pasas.
  - O generada en local con MusicGen (`tools/musicgen.py`): se generan varias opciones y se elige la que tenga pulso estable y sin huecos largos. **El trap no gustó** (Poedagar 970): usar afro house, reggaetón suave o pop electrónico.
- **Montaje** (`tools/music_bed.py`): alinea un golpe de la pista con el giro, pone la intro tranquila, baja un poco la música mientras hablas (`--duck`) y le pone un fade final de 0,7 s.
- Lo que no funcionó: la música sintetizada a mano (v1); el trap y la música tan baja que no se escuchaba (Poedagar 970 v1).

### 7.3 Efectos de sonido
Biblioteca offline de HyperFrames (`media-use/audio/assets/sfx`), copiada en `assets/sfx/`:

| Momento | Efecto | Volumen |
|---|---|---|
| Hook → giro | `riser`, que corona justo en el giro | 0,4 (sube) |
| Giro | `whoosh-cinematic` + `impact-bass-1` + `sparkle` | 0,5 / 0,6 / 0,25 |
| Aparece el precio | `pop` | 0,35 |
| Cortes secos (hook y la mayoría) | **Sin efecto.** No se pone un whoosh en cada corte | — |
| Solo los cortes con golpe de zoom o una transición de verdad (2–4 en todo el video) | Variar: `whoosh-short`, `whoosh`, `impact-bass-2` | 0,2–0,35 |
| Números de la lista | `click` | 0,45 |
| Cada ✅ | `click-soft` (o `pop`, pero sin repetir siempre el mismo) | 0,3–0,4 |
| Teléfono o "LO QUIERO" | `chime` | 0,4 |

Regla: los efectos se varían y se usan solo cuando algo entra con fuerza; si todos los cortes llevan el mismo whoosh, cansa.

**Volumen de los efectos:** los de la tabla son para una voz a ~−16 LUFS. Si la voz quedó más baja, se bajan en la misma proporción. `impact-bass-1` e `impact-bass-2` son muy densos (promedio −5 y −3 dB): nunca más de ~0,1, o el giro satura cuando se sube el volumen final. En el giro no se apilan todos fuertes: subida, whoosh, golpe y brillo suaves (Poedagar 970 v3: 0,12 / 0,1 / 0,07 / 0,14 con la voz a −25 LUFS).

### 7.4 Mezcla final
- Voz ~−16 LUFS; música ~5–6 dB por debajo de la voz. **La música tiene que escucharse clara** (con 8–10 dB por debajo no se oía). Si la voz grabada quedó baja, se compensa subiendo la voz en la mezcla, no bajando la música.
- El video final se entrega a **−15 LUFS** con picos por debajo de −1 dB (se sube el audio después del render, sin tocar el video).

---

## 8. Entrega
- MP4 H.264, **1080×1920, 30 fps, ~25 Mbps**, audio AAC 256 kbps.
- Se copia a la carpeta del modelo como `<Modelo>_vN.mp4`.

---

## 9. Flujo de producción (paso a paso)

### 9.0 Dónde está cada cosa
- **`tools/` (en la raíz de `Timelex videos`)**: los scripts generales, sirven para cualquier modelo y no tienen datos de ningún video. Se ejecutan **desde la carpeta del proyecto** (`videos/<modelo>/`) como `..\..\tools\<script>`. Cada uno explica su uso en las primeras líneas.

| Script | Para qué | Datos que recibe |
|---|---|---|
| `voice.ps1` | Corta silencios y nivela la voz sin tocar su sonido (§ 7.1) | `-In` (voz grabada), `-Segs "ini-fin,ini-fin,…"` (tramos a conservar) |
| `extract-shots.ps1` | Saca las tomas a 1080×1920 con el grade | `-Src` (carpeta del modelo), `-Edl edl.csv` (lista de tomas del proyecto), `-Only` (opcional) |
| `musicgen.py` | Genera 3 opciones de música en local | carpeta de salida (estilos en `PROMPTS`) |
| `music_bed.py` | Monta la música: intro apagada, golpe en el giro, ducking | pista, voz, salida, `--dur`, `--drop`, `--hit` |
| `transcribe.py` | Tiempos por palabra de la voz | WAV mono 16 kHz |
| `contact-sheet.ps1` | Hoja de cuadros con el segundo exacto | video, inicio, duración |
| `sharpness.py` | Nitidez de clips o ventanas (apoyo; manda la revisión a ojo) | carpeta de clips o video + rango |
| `analyze_music.py` | Tempo, pulso y espectrograma de opciones de música | pistas + imagen de salida |

- **`videos/<modelo>/`**: el proyecto de cada video: `index.html`, `edl.csv` (la lista de tomas de ese video) y `assets/` (tomas, voz, música, fuentes, efectos).
- **`videos/nibosi-2628/`**: el proyecto de referencia, para copiar su `index.html` como base.

### 9.1 Arrancar un modelo nuevo
1. `npx hyperframes init "videos/<modelo>" --non-interactive --example=blank`
2. Copiar desde el último proyecto (`videos/poedagar-821/` tiene el hook con pregunta y el precio al cierre; `videos/nibosi-2628/`, el hook de precio): `assets/fonts/`, `assets/sfx/` e `index.html` (base de estilos, textos y efectos). No copiar `assets/clips/`, `assets/voz.wav`, `assets/musica.wav`, `assets/bgm/` ni `edl.csv`: son de ese modelo.
   - Música nueva para cada video: `musicgen.py <carpeta> <semilla>` con una semilla distinta (por ejemplo, el número del modelo).
3. Crear el `edl.csv` del modelo nuevo (mismo formato: `id,archivo,entrada,duracion,4k`).
4. En `index.html` cambiar: `data-duration` de la raíz, los `data-start`/`data-duration` de cada toma, los textos y sus tiempos (`data-at`), los efectos de sonido y los tiempos del giro en el `<script>`.

### 9.2 Pasos

1. **Material:** las tomas en `<Modelo>/`, el precio, las características confirmadas y los colores.
2. **Guion:** se escribe con la plantilla (§ 3) y lo apruebas. Queda en `<Modelo>/GUION.md`.
3. **Revisión de tomas:** hojas de cuadros de cada video (vista general y luego `tools/contact-sheet.ps1` en los tramos que interesan).
   ```
   ffmpeg -i <toma>.MOV -vf "fps=2,scale=200:356,tile=8x6" -frames:v 1 hoja.jpg
   ```
4. **Voz:** grabas y la dejas en la carpeta del modelo.
   - Silencios: `ffmpeg -i <voz> -af silencedetect=noise=-38dB:d=0.12 -f null NUL`. El silencio inicial se quita y cada pausa de más de 0,3 s se deja en ~0,1 s; esos tramos van en `-Segs`.
   - `powershell -ExecutionPolicy Bypass -File ..\..\tools\voice.ps1 -In "..\..\<Modelo>\<voz>" -Segs "1.70-9.08,9.34-16.34,…"`
   - Luego `tools/transcribe.py` sobre la voz limpia (pasada a WAV mono 16 kHz) para tener el tiempo de cada palabra. Los inicios de palabra se afinan con `silencedetect` (d=0.06) sobre la voz limpia.
   - El giro se coloca en el inicio de la frase que presenta el reloj.
5. **Edición (EDL):** se escribe `edl.csv` con el tramo de cada toma siguiendo la estructura y los tiempos de la voz, y se extraen:
   `powershell -ExecutionPolicy Bypass -File ..\..\tools\extract-shots.ps1 -Src "..\..\<Modelo>" -Edl edl.csv`
6. **Nitidez:** recorte del reloj de cada toma en 3 momentos y revisión a ojo; se cambia lo que esté borroso (y se re-extrae con `-Only s07,s11`).
7. **Música:** `tools/musicgen.py` (o tu canción) → `tools/music_bed.py <pista> assets/voz.wav assets/musica.wav --dur 28 --drop 3.85 [--hit 3.76]`.
8. **Composición (HyperFrames):** `index.html` (tomas, textos, subtítulos § 6.1, efectos, audio).
9. **Revisión:** `npx hyperframes check` (sin errores) y `npx hyperframes snapshot --at ...` en los momentos clave.
10. **Render:**
    ```
    npx hyperframes render --fps 30 --video-bitrate 25M --max-bitrate 35M --video-frame-format png --no-browser-gpu -o renders/<modelo>_raw.mp4
    ```
    Luego el volumen final:
    ```
    ffmpeg -i renders/<modelo>_raw.mp4 -c:v copy -af "volume=4dB,alimiter=limit=0.89:level=disabled" -c:a aac -b:a 256k <Modelo>/<Modelo>_vN.mp4
    ```
    Se mide con `ebur128` y se ajusta la ganancia hasta ~−15 LUFS.

Notas de esta máquina:
- MusicGen necesita `truststore` porque la red corporativa re-firma HTTPS.
- Openverse no responde desde esta red; los efectos salen de la biblioteca incluida.
- Para render y snapshot: `HYPERFRAMES_BROWSER_PATH` y `--no-browser-gpu`.

---

## 10. Checklist antes de entregar

- [ ] ¿Dura ~28 s (máximo 30)?
- [ ] ¿Se editó y renderizó con HyperFrames?
- [ ] ¿Ninguna escena dura menos de 1,5 s ni más de 2 s (salvo las bonitas/pausadas, máximo 3 s), con promedio entre 1,5 y 2 s?
- [ ] ¿Hay subtítulos dinámicos abajo-centro, legibles y fuera de la zona de botones?
- [ ] ¿Todas las tomas están nítidas (revisadas de cerca)?
- [ ] ¿No hay fotos, viñetas ni fondos oscuros?
- [ ] ¿El hook no muestra ninguna esfera?
- [ ] ¿La música arranca justo en el giro?
- [ ] ¿Hay efectos en el giro, en los cortes y en los ✅?
- [ ] ¿Cada etiqueta coincide con la palabra que se dice?
- [ ] ¿Cada color se nombra y se ve solo cuando se dice?
- [ ] ¿No hay dos tomas casi iguales seguidas?
- [ ] ¿El teléfono correcto (0422-029-1685) está en pantalla al final?
- [ ] ¿La voz suena natural (sin "pote" ni saturación) y el video está a ~−15 LUFS?
- [ ] ¿Se entiende el video con el volumen apagado?

---

## 11. Lo que aprendimos (historial de correcciones)

| Versión | Qué no funcionó | Regla que quedó |
|---|---|---|
| Guion v1 | 70 palabras / 25 s se sentía corto; "tres colores" sin nombrarlos | 75–82 palabras; colores uno por uno con su toma |
| Video v1 | Voz procesada con reducción de ruido: sonaba "en un pote", detrás de una puerta | EQ correctiva, sin reducción de ruido, compresión suave |
| Video v1 | Música sintetizada a mano | MusicGen local o tu canción, alineada al giro |
| Video v1 | La esfera se veía en la caja antes del giro | El hook solo muestra la caja, la funda, la tarjeta y el paño |
| Video v1 | Una foto con zoom en "día y fecha" | Nunca fotos; acercamiento sobre video en 4K |
| Video v1 | Sin efectos de sonido | Riser, impacto, whooshes, pops y chime (§ 7.3) |
| Video v2 | Fondo oscuro "misterioso" en el hook | Nada de viñetas ni efectos sobre la imagen |
| Video v2 | Tomas borrosas (6–7 s, 12 s, 16 s) | Revisión de nitidez a ojo de cada toma |
| Video v2 | Dos tomas casi iguales seguidas | Variar encuadre o video entre tomas seguidas |
| Guion Poedagar 821 v1 | La voz narraba el clip ("Clic… giras la muñeca…"); "correa integrada a la caja" no se entiende; "que no se note lo poco que gastaste" suena a mala calidad | El guion es voz de venta que se graba aparte: nunca describe lo que hace la mano en la toma. Beneficios en palabras que entienda cualquiera. Nada que insinúe barato o mala calidad: el precio se dice como oportunidad, no como "gastaste poco" |
| Nibosi 2653 | Se procesó la voz con EQ y compresión (`voice.ps1`) | **La voz queda natural**: solo se quitan los silencios y se sube con ganancia lineal, sin EQ, compresor ni limitador |
| Guion Onola 3826 v1 | Hook "¿Cuánto crees que cuesta?" en el reloj más caro de la tienda: hacía pensar que era barato | Antes de elegir el hook, preguntar dónde está el modelo en la gama de precios. En los de gama alta, el hook vende exclusividad o presencia (nunca juega a adivinar el precio) y el precio va al cierre sin "tan solo" |
| Poedagar 970 | Todos los videos tenían el mismo esquema (precio, ✅, colores, teléfono) y ya cansaba | Se puede variar el formato completo: hook de lista/consejo, sin precio, sin número de modelo y sin teléfono (§ 2.1, "Formato sin precio ni teléfono") |
| Video Poedagar 970 v1 | Trap que no gustó y música tan baja que no se escuchaba; el mismo whoosh en todos los cortes; el hook arrancaba en el set vacío con zoom a la caja del fondo y el reloj salía con un corte simple; en "te llega en su caja" se hacía zoom a la caja del fondo | Intro tranquila aparte + pista movida en el giro, música a ~5–6 dB de la voz (§ 7.2, 7.4). Efectos variados y solo en transiciones reales (§ 7.3). Sin toma de caja, el hook es la correa/tapa/broche en cámara lenta (§ 2.1). Entrada rápida del reloj en el giro (§ 2.2). Nunca zoom a la caja del fondo |
| Video Poedagar 970 v2 | El giro saturaba (golpe de bajo y whoosh demasiado fuertes) y la voz decía "con absolutamente…" sin el "todo": el corte de pausas se comió la sílaba final | Efectos del giro mucho más bajos, y los `impact-bass` nunca pasan de ~0,1 (§ 7.3). Antes de cortar una pausa se mira la energía, y después se comprueba con la transcripción que estén todas las palabras (§ 7.1) |
| Guion Poedagar 970 | "Broche desplegable" (se dice "broche mariposa"); "que la esfera no sea de adorno" no gustó; "Comenta lo quiero y te escribo" sonaba incompleto | Decir "broche mariposa". No usar el ángulo "de adorno". El cierre sin teléfono es "Comenta 'lo quiero' y te envío el catálogo" |
| Guion Sinobi 9883 | Todos los videos seguían el mismo molde (precio, ✅, teléfono). Los guiones en "tono de creador" (primera persona, "lo que más me gusta…") no gustaron, y tampoco que se repitieran sus palabras tal cual | Formato alternativo cuando se pida: sin precio, sin teléfono y sin llamada a la acción; cierra con una pregunta que invite a comentar ("¿Redondo o cuadrado?"). En la voz se dice solo la marca, nunca el número del modelo. No copiar en el guion las frases que el usuario dice al explicar el producto |
| Pedido nov. 2026 | Escenas de 0,5–1 s se sentían demasiado rápidas; faltaban subtítulos | Escenas de 1,5 s mínimo, 2 s máximo (promedio 1,5–2 s; bonitas hasta 3 s). Subtítulos dinámicos siempre, abajo-centro fuera de la zona prohibida (§ 6.1). Siempre HyperFrames |

---

## 12. Análisis del video viral (referencia)

| Qué | Dato |
|---|---|
| Duración | 28,5 s, 18 tomas (1,6 s de promedio) |
| Hook | 4 cortes en 3 s; precio en la primera frase |
| Voz | ~80 palabras, 2,8 por segundo, sin pausas |
| Música | Los graves suben justo cuando aparece el reloj |
| Texto | Precio + pocas etiquetas con ✅ + teléfono |
| Imagen ↔ voz | Cada toma muestra lo que se dice en ese momento |

Las otras referencias duran más de 30 s, ninguna dice el precio y algunas tienen silencios largos al inicio; rindieron menos.

---

## Anexo: edición final del Nibosi 2628 (v3)

Guion: [`Nibosi 2628/GUION.md`](Nibosi%202628/GUION.md). Proyecto: `videos/nibosi-2628/` (lista de tomas en `edl.csv`). Video: `Nibosi 2628/Nibosi2628_v3.mp4`.

Comandos usados (desde `videos/nibosi-2628/`):
```
powershell -ExecutionPolicy Bypass -File ..\..\tools\voice.ps1 -In "..\..\Nibosi 2628\WhatsApp Audio 2026-10-31 at 2.49.35 PM (1).mp4" -Segs "1.70-9.08,9.34-16.34,16.62-20.29,20.63-26.83,27.08-30.22"
powershell -ExecutionPolicy Bypass -File ..\..\tools\extract-shots.ps1 -Src "..\..\Nibosi 2628" -Edl edl.csv
uv run --no-project --with librosa python -I ..\..\tools\music_bed.py assets\bgm\opcion-a.wav assets\voz.wav assets\musica.wav --dur 28 --drop 3.85 --hit 3.76
```

| # | Tiempo (s) | Fuente @ entrada | Qué se ve | Texto |
|---|---|---|---|---|
| 1 | 0,00–1,00 | 1585 @ 2,10 | Caja con logo | — |
| 2 | 1,00–2,10 | 1585 @ 12,60 | Abriendo la funda | 49$ |
| 3 | 2,10–2,95 | 1585 @ 14,00 | Caja interior con tarjeta | 49$ |
| 4 | 2,95–3,85 | 1585 @ 82,00 | Quitando el paño | 49$ BCV |
| 5 | 3,85–5,00 | 1585 @ 95,60 | **Giro:** sale el reloj azul | — |
| 6 | 5,00–6,20 | 1584 @ 3,70 | Azul en la muñeca | Nibosi 2628 |
| 7 | 6,20–7,42 | 1553 @ 44,15 | Azul en la palma | Nibosi 2628 |
| 8 | 7,42–8,98 | 1553 @ 31,00 (4K) | Acercamiento al día y la fecha | Día y Fecha ✅ |
| 9 | 8,98–10,40 | 1586 @ 84,00 | Verde oliva en la mano | Resistente al Agua 💧✅ |
| 10 | 10,40–12,05 | 1644 @ 15,00 | Broche abriéndose | Broche Desplegable ✅ |
| 11 | 12,05–13,20 | 1585 @ 101,00 | Azul en los dedos | — |
| 12 | 13,20–14,40 | 1587 @ 44,50 | Chocolate en la muñeca | — |
| 13 | 14,40–14,94 | 1689 @ 6,00 | Los cuatro juntos | — |
| 14 | 14,94–15,48 | 1644 @ 33,20 | Negro | Negro · Plateado |
| 15 | 15,48–16,13 | 1584 @ 16,10 | Azul | Azul · Plateado |
| 16 | 16,13–17,04 | 1586 @ 56,75 | Verde oliva | Verde Oliva · Oro Rosa |
| 17 | 17,04–18,08 | 1587 @ 69,60 | Chocolate | Chocolate · Oro Rosa |
| 18 | 18,08–19,46 | 1586 @ 5,60 | Verde oliva en su caja | Caja Original ✅ |
| 19 | 19,46–20,56 | 1585 @ 97,00 | Azul en la mano | Delivery GRATIS en Caracas ✅ |
| 20 | 20,56–21,55 | 1584 @ 17,60 | Azul en la muñeca | ″ |
| 21 | 21,55–22,80 | 1644 @ 21,00 | Cerrando el broche | Envíos Nacionales por MRW o Zoom ✅ |
| 22 | 22,80–24,28 | 1584 @ 11,30 | Azul de cerca | ″ |
| 23 | 24,28–25,60 | 1689 @ 2,40 | Los cuatro juntos | ¡0422-029-1685! |
| 24 | 25,60–26,75 | 1689 @ 8,30 | Verde oliva + azul | ″ |
| 25 | 26,75–28,00 | 1689 @ 10,25 | Negro + chocolate | ″ |
