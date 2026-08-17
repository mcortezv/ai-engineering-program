# Artificial Intelligence Engineering Program

Programa de formación en ingeniería de sistemas de inteligencia artificial.
Veinte módulos, cinco partes y cuarenta y cuatro horas lectivas, dirigidos
principalmente a personas que desarrollan software pero diseñados para que
alguien de producto, diseño u operaciones pueda seguirlos completos.

Este repositorio no contiene el material terminado: contiene **el material y el
motor que lo produce**. El contenido vive en archivos de texto versionables y
los documentos finales se compilan con un comando.

---

## Qué produce

| Artefacto | Formato | Descripción |
| --- | --- | --- |
| Temario | `.docx` y `.pdf` | Documento de 105 páginas con objetivo, contenidos, enfoque didáctico, ejercicio y criterios de evaluación por módulo. |
| Presentaciones | `.pdf` 16:9 | Una por módulo, con diagramas vectoriales y guion del instructor al final. |

Todo se escribe en `dist/`.

---

## Premisa del programa

La mayoría de los cursos de inteligencia artificial enseñan a usar
herramientas. Este enseña a entender el sistema que hay debajo, para que las
herramientas se puedan cambiar sin volver a empezar.

Su hipótesis es que si alguien entiende de verdad que un modelo de lenguaje
predice el siguiente token, entonces el prompt engineering, la ventana de
contexto, la recuperación de información, los agentes, el costo y las
alucinaciones dejan de ser temas sueltos que hay que memorizar y se convierten
en consecuencias de un mismo hecho.

### Estructura

| Parte | Pregunta que responde | Módulos | Horas |
| --- | --- | --- | --- |
| I · Fundamentos | ¿Qué es y qué no es un modelo de lenguaje? | 1 – 4 | 8 |
| II · Cómo se le habla a un modelo | ¿Cómo consigo que haga lo que necesito? | 5 – 7 | 6 |
| III · Construir un sistema | ¿Cómo le doy memoria, información y capacidad de actuar? | 8 – 13 | 16 |
| IV · Operar un sistema | ¿Cómo lo hago pagable, observable y seguro? | 14 – 18 | 10 |
| V · Más allá | ¿Qué hago cuando todo lo anterior se queda corto? | 19 – 20 | 4 |

---

## Puesta en marcha

### Requisitos

| Herramienta | Para qué | Nota |
| --- | --- | --- |
| Python 3.10+ | Compilar el contenido | — |
| `python-docx` | Generar el temario | `pip install -r requirements.txt` |
| Node.js | Descargar los iconos de marca | Solo `npm install`, no hace falta en tiempo de compilación |
| Microsoft Word | Exportar el temario a PDF con índice paginado | Solo en Windows |
| Chrome o Edge | Imprimir las presentaciones a PDF | Se detecta automáticamente |

La tipografía Figtree va versionada en `assets/fonts/`, así que la compilación
no depende de la red ni de ningún otro proyecto.

### Instalación

```bash
pip install -r requirements.txt
npm install
```

### Compilación

```bash
python build.py list          # qué hay registrado y qué falta
python build.py syllabus      # el temario completo
python build.py deck 4        # una presentación
python build.py decks         # todas las presentaciones
python build.py all           # todo
```

---

## Organización del repositorio

La división es deliberada: **`content/` es lo que se edita, `engine/` es cómo
se ve.** Cambiar un tema no debería obligar a tocar el renderizado, y cambiar
el diseño no debería obligar a tocar el contenido.

```
ai-engineering-program/
├── build.py                  punto de entrada único
├── content/                  ── QUÉ SE ENSEÑA ──
│   ├── program.py            metadatos, portada, preámbulo
│   ├── syllabus/             el temario, una parte por archivo
│   │   ├── part1.py … part5.py
│   │   └── annexes.py
│   └── decks/                las presentaciones, un archivo por módulo
│       └── m01.py … m20.py
├── engine/                   ── CÓMO SE VE ──
│   ├── syllabus_doc.py       renderiza el temario a .docx y .pdf
│   ├── deck.py               renderiza una presentación a .pdf
│   ├── slides.css            sistema de diseño de las láminas
│   └── diagrams/
│       ├── base.py           primitivas SVG y tokens de color
│       ├── brands.py         logos de proveedor
│       └── mod01.py … modNN.py
├── assets/fonts/             Figtree (SIL OFL)
├── source/                   insumos originales del programa
├── archive/                  material retirado, conservado a propósito
└── dist/                     artefactos compilados
```

---

## Mantenimiento

Las tareas frecuentes están documentadas paso a paso en
[CONTRIBUTING.md](CONTRIBUTING.md):

- Corregir el contenido de un módulo
- Añadir un módulo nuevo al programa
- Escribir la presentación de un módulo
- Crear un diagrama
- Ajustar el sistema de diseño

### Criterios de redacción

Cuatro reglas gobiernan todo el material y conviene respetarlas al editarlo:

1. **Todo se explica como es**, no como corrección de lo que se creía. El
   material no habla de sí mismo ni de versiones anteriores.
2. **No se cita otro módulo.** Si un tema se retoma después, se retoma después.
3. **No se adelantan conceptos** que aún no se han visto. Si una idea necesita
   un término posterior, se explica con lo que ya se tiene.
4. **Antes que una lámina de texto, un diagrama.**

### Contenido con fecha de caducidad

Algunas secciones describen productos, precios y protocolos que cambian. Están
marcadas en ámbar dentro del documento y conviene revisarlas antes de cada
impartición. Lo conceptual que las rodea no caduca: esa separación es
intencional.

---

## Créditos y licencias de terceros

| Recurso | Licencia | Uso |
| --- | --- | --- |
| [Figtree](https://github.com/erikdkennedy/figtree) | SIL Open Font License 1.1 | Tipografía de títulos y datos |
| [simple-icons](https://github.com/simple-icons/simple-icons) | CC0 1.0 | Logos de proveedor |

Los logos de proveedor se usan de forma nominativa para identificar productos
comerciales. Cuando una marca no está disponible bajo licencia libre se dibuja
un monograma tipográfico en su lugar, nunca una imitación del logo.

---

## Licencia

[MIT](LICENSE) © Manuel Cortez
