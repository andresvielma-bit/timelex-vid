# Timelex — videos de venta de relojes

Lee este archivo completo al empezar cualquier conversación en esta carpeta. Te da el contexto para no tener que explicarlo todo de nuevo.

## Quién soy y qué necesito

Tengo **Timelex**, una tienda de relojes en Caracas. Vendo por redes sociales (TikTok / Instagram Reels) con videos cortos verticales.

Mi primera tanda de relojes fue un éxito: vendí en tres semanas lo que esperaba vender en dos meses, y fue gracias a los videos. Uno se hizo viral (~50 mil likes) y no pude cubrir la demanda. Después estuve un tiempo sin contenido porque la mercancía tardó en llegar (el terremoto retrasó los envíos). Ahora vuelvo a tener relojes y necesito retomar los videos.

Sé editar y lo hago bien, pero no me gusta. **Tú editas los videos** con **HyperFrames** (skill `/hyperframes`, ya instalada). Yo grabo las tomas y mi voz en off.

**No son motion graphics ni estilo After Effects.** Son videos de venta sencillos: mis tomas reales, bien cortadas, en el momento correcto, con transiciones, efectos de sonido, música y algo de texto en pantalla. Ritmo rápido pero que se entienda todo.

## Cómo está organizada la carpeta

| Ruta | Qué es |
|---|---|
| `METODOLOGIA.md` | **El manual del estilo**: reglas fijas, estructura, transiciones, texto, sonido, flujo paso a paso, checklist e historial de correcciones. Se sigue siempre. |
| `Refs/` | Videos de referencia ya publicados. `3093309729997810150.mp4` es **el viral** (el molde principal). Ahí también guardo los videos nuevos que salen bien (por ejemplo, el Nibosi 2628 final). |
| `<Modelo>/` (ej. `Nibosi 2628/`) | Las tomas crudas de cada modelo (iPhone, .MOV), el guion (`GUION.md`), mi voz grabada y el video final. |
| `tools/` | Scripts generales para cualquier video (voz, tomas, música, transcripción, nitidez, hojas de cuadros). No tienen datos de ningún modelo; se usan desde el proyecto del video. Ver § 9 de `METODOLOGIA.md`. |
| `videos/<modelo>/` | Proyecto HyperFrames de cada video: `index.html`, `edl.csv` (lista de tomas) y `assets/`. `videos/nibosi-2628/` es la referencia para copiar el `index.html`. |

## Cómo trabajamos (normalmente en tres mensajes)

1. **"Contextualízate"** → lees este archivo y `METODOLOGIA.md` completo, y analizas `Refs/` mirando los videos, no solo el resumen. Me respondes con un resumen corto de lo que entendiste del estilo (ritmo, hook, giro, música, texto) y de lo que viste en los últimos videos guardados. No edites nada todavía.
2. **"Revisa la carpeta `<Modelo>` y dame el guion"** → revisas todas las tomas (hojas de cuadros), me dices qué material hay y qué falta, me preguntas lo que no sepas (precio, características, colores, tipo de hook y dónde va el precio si no lo dije) y me das el guion siguiendo la metodología. Si te pido algo distinto (otro hook, el precio al final…), lo respetas sin romper las reglas fijas.
3. **"Aquí está la voz, crea el video"** → procesas la voz, armas la edición con HyperFrames, revisas nitidez y fotogramas, renderizas y me entregas el MP4 en la carpeta del modelo. Después ajustamos lo que yo te diga.

## Qué hacer en cada video nuevo

1. **Lee `METODOLOGIA.md` completo** antes de proponer nada.
2. **Analiza bien `Refs/`**, sobre todo el viral y los últimos videos que he guardado: cortes por segundo, cómo arranca el hook, cuándo entra la música, qué texto aparece, cómo cada toma acompaña lo que dice la voz. No te quedes con la descripción del manual: mira los videos (hojas de cuadros con ffmpeg, detección de cortes, transcripción).
3. **Revisa todas las tomas del modelo** (hojas de cuadros por video) y anota qué hay en cada segundo: caja, apertura, muñeca, mano, detalles, colores, pruebas.
4. **Pídeme lo que falte**: precio, características confirmadas, colores y tipo de hook que quiero esta vez. No inventes características.
5. **Escribe el guion** con la plantilla de la metodología (puedes usar `/copywriting`), con mi forma de hablar. Lo apruebo y **yo grabo la voz**.
6. **Edita con HyperFrames** siguiendo el flujo de la metodología, revisa la nitidez de cada toma y los fotogramas, y **renderiza** en 1080×1920, 30 fps, bitrate alto (~25 Mbps), audio a ~−15 LUFS.
7. Cuando corrija algo, **agrega la regla nueva a `METODOLOGIA.md`** (historial de correcciones) para no repetir el error.

## Lo esencial del estilo (resumen; el detalle está en la metodología)

- **Duración:** ~25–28 s, nunca más de 30 s.
- **Cortes:** cada escena dura máximo 2 s; solo una toma "bonita" del reloj puede llegar a 3 s.
- **Hook con misterio:** abrir la caja, sacarla, quitar el paño… sin mostrar la esfera. El hook puede ser el precio ("Por tan solo 49 a tasa del Banco Central…", que funcionó muy bien en el viral), una prueba, una frase aspiracional o una historia. Eso cambia según el video; la estructura no.
- **El giro:** cuando sale el reloj hay una transición (destello + zoom) y la música, que venía tranquila, agarra ritmo rápido justo ahí.
- **Después:** el reloj bonito, los detalles (correa, broche, día y fecha), las pruebas si las hay (agua, rayado), los colores uno por uno, la caja, el delivery y los envíos, y al final el número de teléfono.
- **Cada toma muestra lo que dice la voz** en ese momento.
- **Siempre:** tomas nítidas, solo video (nunca fotos), sin viñetas ni fondos oscuros, efectos de sonido en las transiciones, voz natural y clara.
- **Teléfono actual:** 0422-029-1685 (el viral muestra uno viejo, no lo uses).

## Restricciones de esta máquina

- No proponer logins a servicios externos (HeyGen, etc.); usar herramientas locales. La música sale de MusicGen local o de una canción que yo te pase.
- Las instrucciones de entorno (rutas de ffmpeg, navegador para el render, `--no-browser-gpu`) están en mi CLAUDE.md global y en la sección de flujo de `METODOLOGIA.md`.
