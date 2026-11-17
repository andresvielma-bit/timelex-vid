# Guion · Poedagar 970 · formato nuevo (sin precio y sin teléfono)

**Estado:** se grabó la **versión A** (voz: `voz_original.m4a`, 27,3 s ya sin pausas). Proyecto: `videos/poedagar-970/` (tomas en `edl.csv`; la s06 es el broche en cámara lenta 0,75x, extraída aparte). Música: MusicGen semilla 970, opción A (trap), golpe de 17,97 s en el giro (10,4 s), intro con pasa-bajos a 700 Hz, música a 0,36 de volumen (la voz salió bajita, −25 LUFS). Final: `volume=5.6dB,alimiter=limit=0.84` → −15,4 LUFS, pico −1,4 dB. Video: `Poedagar 970/Poedagar970_v1.mp4` (28,3 s, tomas de 1,5–2 s y la bonita de 3 s, con subtítulos).

**v2** (`Poedagar970_v2.mp4`): hook solo con correa, tapa y broche en cámara lenta 0,75x (columna `vel` del `edl.csv`); entrada rápida del reloj en 10,4 s (destello + 1,6x con giro −7°); "en su caja" con el reloj en la mano y la caja detrás, sin zoom; efectos variados solo en transiciones. Música: intro tranquila (`assets/bgm/intro-calma.wav`, MusicGen semilla 9700) + afro house (`opcion-d.wav`, tramo 12,43–24,22 s repetido en `opcion-d-loop.wav`), montada con `music_bed.py ... --hit 0.0 --intro assets\bgm\intro-calma.wav --intro-gain -4 --duck 0.35`, a 0,47 de volumen. Alternativa: pop electrónico (`opcion-f-loop.wav`, a 0,4). Muestras en `musica_opciones/`. Final: −15,2 LUFS, pico −1,4 dB.

**v3** (`Poedagar970_v3.mp4`, 28,75 s): voz rehecha con el tramo 12,13–15,40 (antes se cortaba el "-do" de "todo"), todo lo posterior corrido +0,45 s y la s09 alargada a 2,05 s. Efectos del giro bajados (subida 0,12, whoosh 0,1, golpe 0,07, brillo 0,14; golpe del cierre 0,07). Volumen final con `loudnorm` en dos pasadas (I=−15, TP=−1,5) → −15,0 LUFS, pico −1,5 dB; el giro queda a −13,4 LUFS sin saturar.

Pediste romper el molde: todos los videos anteriores siguen el mismo esquema (hook → "te presento" → ✅ beneficios → colores → delivery → precio en verde → teléfono). Este no dice el precio ni muestra el teléfono. En su lugar, el cierre pide un **comentario** ("comenta LO QUIERO"): cada comentario le dice al algoritmo que el video interesa, y la gente que pregunta "¿precio?" también suma.

## Qué hay en las tomas

Una sola toma: `IMG_1677.MOV` (45 s, 1080p vertical, 60 fps). Set de siempre: mesa negra, guantes negros, caja Poedagar blanca entre dos matas. Un solo color: **esfera plateada con las tres subesferas en azul**, bisel y correa de acero (la correa todavía tiene el plástico protector).

| Segundos | Qué se ve |
|---|---|
| 0–0,5 · 28–31,5 · 43–45 | Set vacío con la caja Poedagar cerrada al fondo (sin reloj) |
| 1,5–3,5 | Reloj en la mano, esfera de frente |
| 4–10 | Colgando de los dedos, esfera de frente (la más estable: 8,5–9,5) |
| 10,5–12 | Lo gira: canto y tapa trasera |
| 12–16 | Correa de lado, eslabones (**no se ve la esfera**) |
| 16,5–19,5 | Tapa trasera con stickers y broche desplegable abriéndose (**no se ve la esfera**) |
| 20–21 | **Pasa de la tapa a la esfera** (sirve para el giro) |
| 21–28 | En la mano, girándolo (se mueve bastante) |
| 31,5–35 | La mano entra con el reloj frente a la caja (en 32,0 hay un reflejo rojo, se evita) |
| 36–42,5 | **La mejor toma:** grande, de frente, en la mano (39,5–42) |

Lo que se ve del reloj: cronógrafo con tres subesferas, dos botones al lado de la corona, ventanita de fecha entre las 4 y las 5, caja octogonal con correa integrada de acero, broche desplegable tipo mariposa y la tapa trasera de acero.

**Lo que falta:**
- **No hay ninguna toma en la muñeca.**
- **No hay toma del cronógrafo funcionando** (apretar el botón y que arranque la aguja). Si no la hay, no podemos decir que "funciona de verdad".
- No hay apertura de caja, ni toma afuera con luz natural, ni otros colores.

---

## Versión A (recomendada) · "Antes de comprar un reloj, fíjate en esto" · ~76 palabras · ~27 s

Es un formato de **consejo con lista** (1, 2, 3), que nunca hemos usado. Le sirve a quien busca reloj aunque no conozca la marca, y se guarda y se comparte más que una venta directa. Además le sienta perfecto a esta toma: la correa, el broche y la tapa se pueden mostrar **sin enseñar la esfera**, así que el misterio dura hasta el punto 3 y el reloj sale justo cuando la voz dice "esfera".

> Antes de comprar un reloj, fíjate en estas tres cosas.
> Primero, que la correa sea de acero inoxidable.
> Segundo, que tenga broche mariposa, para que no se te abra solo.
> Y tercero, que te combine con todo.
> Este es nuestro nuevo Poedagar.
> Tiene cronógrafo, te marca la fecha y es súper elegante.
> Te llega en su caja, con delivery gratis en Caracas y envíos por MRW o Zoom.
> Comenta "lo quiero" y te envío el catálogo.

**Otras opciones para el punto 3** (ahí sale el reloj, así que tiene que sonar a remate):
- "Y tercero, que se vea bien de día y de noche."
- "Y tercero, que lo puedas usar en la oficina y el fin de semana." (se parece al hook del 821)

| Voz | Toma (aprox., se afina en la edición) | En pantalla |
|---|---|---|
| "Antes de comprar un reloj," | 0,0 · set con la caja (empuje lento) | **Antes de comprar un reloj…** (grande, blanco) |
| "fíjate en estas tres cosas." | 10,6 · lo gira, se ve el canto | ″ |
| "Primero, que la correa sea de acero inoxidable." | 12,5 · eslabones de lado → 14,5 · otro ángulo | **1 · Correa de acero** |
| "Segundo, que tenga broche mariposa…" | 16,8 · el broche abriéndose → 18,5 | **2 · Broche mariposa** |
| "Y tercero, que te combine con todo." | **Giro** en "tercero": 20,0 · pasa de la tapa a la esfera (destello + zoom, la música entra completa) | **3 · Que combine con todo** |
| "Este es nuestro nuevo Poedagar." | 39,5 · la toma bonita (hasta 3 s) | Nuevo Poedagar |
| "Tiene cronógrafo," | 8,8 · acercamiento a las subesferas (mejor si grabas el botón arrancando la aguja) | Cronógrafo ✅ |
| "te marca la fecha y es súper elegante." | 40,8 · acercamiento a la fecha (máx. ~1,6x, la fuente es 1080p) | Fecha ✅ |
| "Te llega en su caja," | 32,6 · el reloj frente a la caja Poedagar | Caja Original ✅ |
| "con delivery gratis en Caracas" | 5,0 · colgando de los dedos | Delivery GRATIS en Caracas ✅ |
| "y envíos por MRW o Zoom." | 24,5 · de lado con el broche | Envíos Nacionales / por MRW o Zoom ✅ |
| "Comenta 'lo quiero' y te envío el catálogo." | 36,5 y 41,5 · dos cortes en la mano, termina en movimiento | **Comenta "LO QUIERO"** / y te envío el catálogo |

Cambios de edición frente a los videos anteriores:
- La música no arranca apagada 8 s: suena baja con pulso desde el inicio (los números 1, 2, 3 caen en golpes) y **explota en el giro** ("tercero").
- Los números de la lista entran grandes, con un golpe de zoom y un `pop`.
- El final no tiene teléfono ni precio: queda "Comenta LO QUIERO / y te envío el catálogo" grande hasta el último cuadro.

---

## Versión B · "Valió la pena la espera" · ~69 palabras · ~25 s

Una historia corta y personal: la gente que te siguió el primer video sabe que estuviste sin mercancía. No menciono el terremoto a propósito, para no usar una tragedia para vender.

> Este reloj tardó dos meses en llegar a Caracas.
> Y apenas lo abrí, supe que valió la pena la espera.
> Te presento nuestro nuevo Poedagar.
> Es de acero inoxidable, tiene cronógrafo, te marca la fecha y trae broche mariposa.
> Te llega en su caja, con delivery gratis en Caracas y envíos por MRW o Zoom.
> Llegaron pocos, así que comenta "lo quiero" y te envío el catálogo.

Hook en pantalla: **Tardó 2 meses en llegar…** sobre el set con la caja, la correa de lado y el broche. Giro en "Te presento". "Llegaron pocos" solo va si es verdad.

---

## Cómo grabarla

- Arranca a hablar apenas le das a grabar: la primera palabra es el primer cuadro.
- En la A, dilo como un consejo de amigo, no como anuncio. Marca un poquito "primero… segundo… y tercero".
- No se dice el número del modelo: solo "nuestro nuevo Poedagar".
- Mejor con Notas de Voz del iPhone que con WhatsApp. La dejas en esta carpeta y me avisas.

## Antes de grabar, confírmame

1. **¿Versión A o B?** (o cambia lo que quieras).
2. **¿El cronógrafo funciona** (los botones arrancan, paran y reinician la aguja)? Si no, quito "tiene cronógrafo".
3. **¿La correa y la caja son de acero inoxidable?** ¿Es resistente al agua?
4. **¿Viene en su caja original?** ¿Hay otros colores además del plateado con azul?
5. **El cierre** es "comenta lo quiero y te envío el catálogo": hay que mandar el catálogo por DM a cada uno.
6. **Si puedes grabar 20 segundos más:** el reloj en la muñeca (quieto, 5 s), el cronógrafo funcionando de cerca (apretar el botón y que arranque la aguja) y, si se puede, una toma afuera con luz natural.
