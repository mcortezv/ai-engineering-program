# Mantenimiento del programa

Guía de las tareas que se repiten al mantener este material. Todas asumen el
entorno ya instalado (`pip install -r requirements.txt` y `npm install`).

La regla que ordena todo: **`content/` es lo que se enseña, `engine/` es cómo
se ve.** Si te encuentras tocando los dos para un mismo cambio, probablemente
haya una forma más limpia de hacerlo.

---

## Criterios de redacción

Antes de escribir una línea de contenido, cuatro reglas que gobiernan todo el
material:

1. **Todo se explica como es**, no como corrección de lo que se creía. El
   material nunca habla de sí mismo, del temario ni de versiones anteriores.
   Si algo estaba mal, se arregla y se explica bien; no se narra el arreglo.
2. **No se cita otro módulo.** Nada de «como vimos en el módulo 4» ni de «esto
   es todo el argumento del módulo 13». Si un tema se retoma después, se
   retoma después.
3. **No se adelantan conceptos** que aún no se han visto. Si una idea necesita
   un término que llega más adelante, se explica con lo que ya se tiene.
4. **Antes que una lámina de texto, un diagrama.** Sobre todo en lo difícil de
   imaginar: dimensiones, espacios vectoriales, flujos con bucles.

En el temario impreso hay una quinta: los títulos de sección **no** llevan la
regla morada inferior del CSS de origen. El morado es acento, no separador.

---

## Corregir el contenido de un módulo

**En el temario.** Los módulos están en `content/syllabus/partN.py` como
diccionarios `M1`, `M2`… Cada uno tiene la misma forma:

```python
M7 = {
    "num": 7,
    "title": "…",
    "tagline": "…",              # una línea bajo el título
    "objetivo": "…",
    "duracion": "2 horas",       # de aquí sale el total del programa
    "dependencias": "…",
    "contenidos": [ … ],         # str, o (str, [subpuntos])
    "enfoque": [ … ],            # bloques, ver abajo
    "ejercicio": [ … ],
    "evaluacion": [ … ],
}
```

Las horas de cada parte y el total del programa **se calculan solos** a partir
de `duracion`. No hay que actualizarlos a mano en ningún sitio.

**En la presentación.** Está en `content/decks/mNN.py`, en la lista `SLIDES`.

Después:

```bash
python build.py syllabus
python build.py deck 7
```

### Bloques disponibles en `enfoque`

| Bloque | Uso |
| --- | --- |
| `"texto"` | Un párrafo. Admite `**negrita**`, `*cursiva*` y `` `código` ``. |
| `("sub", "…")` | Subtítulo dentro del enfoque. |
| `("h3", "…")` | Subsección real; sí aparece en el índice. |
| `("bullets", [ … ])` | Lista. Un elemento puede ser `(texto, [subpuntos])`. |
| `("numbers", [ … ])` | Lista numerada; siempre reinicia en 1. |
| `("code", "…")` | Bloque monoespaciado. |
| `("table", [cabeceras], [filas], [anchos], "pie")` | Los anchos son proporciones. |
| `("box", tipo, "TÍTULO", [párrafos])` | Recuadro. Tipos abajo. |

### Recuadros

| Tipo | Color | Cuándo |
| --- | --- | --- |
| `nota` | morado | Una precisión o un apunte de método. |
| `correccion` | verde | Un criterio que conviene fijar. |
| `volatil` | ámbar | Contenido con fecha de caducidad: productos, precios, protocolos. |
| `alerta` | rojo | Un riesgo o un error caro. |

---

## Añadir un módulo nuevo

1. Escribe el diccionario del módulo en la parte que le corresponda,
   `content/syllabus/partN.py`.
2. Añádelo a la lista `modules` de esa parte, en su posición.
3. Renumera los `"num"` posteriores si lo insertaste en medio.
4. Revisa `content/syllabus/annexes.py`: la tabla de dependencias del Anexo A
   se mantiene a mano.
5. `python build.py list` para confirmar que aparece y que las horas cuadran.

No hace falta tocar `build.py` ni el motor: el registro se deriva de las partes.

---

## Escribir la presentación de un módulo

Crea `content/decks/mNN.py` con dos nombres, `DECK` y `SLIDES`, y opcionalmente
`NOTES`. La forma mínima:

```python
from engine.diagrams import modNN as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo N · …",
    "footer": "Programa de AI · Módulo N",
    "outfile": "Modulo NN - ….pdf",
}

SLIDES = [ … ]
NOTES  = [ … ]      # guion del instructor, al final del PDF
```

`build.py` lo detecta solo por el nombre del archivo. Compila con
`python build.py deck N`.

### Tipos de lámina

| `kind` | Campos | Para qué |
| --- | --- | --- |
| `cover` | `kicker`, `title`, `tagline`, `meta` | Portada. Una por deck. |
| `section` | `step`, `title`, `note` | Separador a sangre morada. |
| `statement` | `text`, `after` | Una afirmación a toda lámina. `<em>` la resalta. |
| `content` | `eyebrow`, `title`, `sub`, `html` | Todo lo demás. |

En `html` sirve cualquier clase de `engine/slides.css`: `ul.pts`, `ol.pts`,
`.cols`, `.grid.c3/.c4/.c5`, `.card`, `.box`, `table`, `pre`. Para insertar un
diagrama, basta con `"html": dg.nombre_del_diagrama()`.

### Guion del instructor

`NOTES` sigue en los archivos de deck pero **ya no se imprime**: el guion del
instructor y los enunciados de ejercicio no van en la presentación. Los
ejercicios viven en el temario, en el campo `ejercicio` de cada módulo.

El contenido de `NOTES` se conserva porque está escrito y es útil; si algún día
hace falta como documento aparte, `engine/deck.py` todavía tiene
`render_notes()` listo.

---

## Crear un diagrama

Los diagramas son SVG generados en Python, un archivo por módulo en
`engine/diagrams/modNN.py`. Devuelven una cadena `<svg>` completa.

```python
from engine.diagrams.base import ACC, DEFS, HAIR, INK, INK3, _rect, _svg, _txt


def mi_diagrama():
    b = [DEFS]
    b.append(_rect(10, 10, 400, 120, fill="#ffffff", stroke=HAIR))
    b.append(_txt(30, 60, "Hola", 20, INK, "700"))
    return _svg(200, "".join(b))
```

Convenciones que evitan sorpresas:

- El lienzo mide **1120 unidades de ancho** y se escala al ancho útil de la
  lámina (unos 298 mm). Una unidad es aproximadamente un píxel.
- La altura la eliges tú en `_svg(alto, …)`. Entre 320 y 400 llena bien.
- Usa siempre los tokens de color de `base.py`, nunca hexadecimales sueltos.
- Un pie de diagrama centrado se escribe con `anchor="middle"` en `x=560`.
  Alinearlo a la izquierda lo saca del lienzo.

### Logos de proveedor

```python
from engine.diagrams.brands import _mark

_mark("anthropic", "A", cx, cy, 36)     # marca oficial si existe
_mark(None, "xAI", cx, cy, 36)          # monograma si no
```

Las marcas salen de `simple-icons`. **OpenAI no está en ese paquete**: la
retiraron a petición de la propia empresa. Para esa y para cualquier otra que
falte, `_mark` dibuja un monograma. No añadas imitaciones de logos.

---

## Ajustar el diseño

| Qué | Dónde |
| --- | --- |
| Colores, tipografías y tamaños de las láminas | `engine/slides.css` |
| Colores y estilos del temario | `engine/syllabus_doc.py`, funciones `build_styles` y las constantes de arriba |
| Colores de los diagramas | `engine/diagrams/base.py` |

Los tres comparten la paleta. Si cambias un color, cámbialo en los tres o
quedarán desalineados.

---

## Cómo se compila

| Paso | Herramienta | Por qué |
| --- | --- | --- |
| Temario → `.docx` | `python-docx` | Estilos reales de Word, índice como campo. |
| `.docx` → `.pdf` | Word por automatización COM | Es lo único que pobla el índice con números de página reales. |
| Presentación → HTML | Plantillas en `engine/deck.py` | — |
| HTML → `.pdf` | Chrome headless | Word no da flexbox, grid ni color a sangre. |

### Dos reglas de la tipografía que no se deben romper

**Nunca uses la versión variable de Figtree.** Chrome la exporta al PDF como
fuente Type3 —un formato donde cada glifo es un mini programa de dibujo— y el
texto se ve mal definido, además de triplicar el peso del archivo. En
`assets/fonts/` van instancias estáticas, una por peso y estilo, y
`engine/deck.py` declara un `@font-face` para cada una.

**No uses glifos que Figtree no tiene** (✓, ✕, flechas decorativas). Chrome mete
una fuente de respaldo como Type3 solo para ese carácter. Si necesitas una
marca, dibújala con un `path` en el diagrama o usa una etiqueta de texto.

Para comprobarlo:

```bash
python -c "import fitz,glob; print(sum(1 for f in glob.glob('dist/*.pdf') "\n  "for p in fitz.open(f) for x in p.get_fonts(full=True) if x[2]=='Type3'))"
```

Debe imprimir `0`.

La fuente se incrusta en base64 en el HTML: el PDF debe ser reproducible sin
red.

---

## Archivos binarios

Los `.pdf`, `.docx` y `.woff2` se versionan con **Git LFS** (ver
`.gitattributes`). Si clonas el repositorio y los binarios aparecen como
punteros de texto:

```bash
git lfs install
git lfs pull
```

---

## Antes de subir un cambio

```bash
python build.py all
python build.py layout
```

`layout` revisa los PDF recién escritos y busca los dos fallos que `check` no
puede ver, porque ninguno da error al compilar:

- **Desborde vertical.** Cuando el cuerpo de una lámina no cabe, `.body` está
  centrado y el contenido sobra por arriba y por abajo a la vez, así que acaba
  tapando el titular. Suele pasar al juntar una tabla larga con dos recuadros.
- **Texto sobre texto.** Dos etiquetas de un diagrama que caen encima. Los
  separadores de sección se saltan: ahí el numeral gigante comparte sitio con
  el titular por diseño.

Y después, una revisión a ojo del PDF: que el índice tenga números de página y
que las listas numeradas empiecen en 1.
