# -*- coding: utf-8 -*-
"""Deck: Módulo 5 — Prompt engineering: cómo habla un modelo."""

from engine.diagrams import mod05 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 5 · Prompt engineering",
    "footer": "Programa de AI · Módulo 5",
    "outfile": "Modulo 05 - Prompt engineering.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 5  ·  3 HORAS",
        "title": "Prompt engineering",
        "tagline": "No es cómo escribir prompts bonitos. Es la única interfaz que "
                   "existe con el modelo.",
        "meta": [
            "<b>Antes de esta sesión:</b> qué hace un modelo al recibir un prompt",
            "<b>Al terminar:</b> diagnosticas por qué falla un prompt, no lo "
            "reescribes a ciegas",
        ],
    },

    {
        "kind": "statement",
        "text": "La pregunta no es «¿qué palabras uso?». Es <em>«¿cómo construyo el "
                "contexto para que la continuación más probable sea la que "
                "necesito?»</em>",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ruta de la sesión",
        "title": "Lo que vamos a ver",
        "html": """
        <ol class="pts">
          <li><b>Los tres roles</b> — la estructura real de una petición.</li>
          <li><b>Instrucciones y contexto</b> — especificidad medible, y por qué la
            posición dentro del prompt cambia el resultado.</li>
          <li><b>Ejemplos y delimitadores</b> — qué comunica mejor cada uno.</li>
          <li><b>Cadenas de pensamiento</b> — por qué funcionan y cuándo hacen
            daño.</li>
          <li><b>Salidas estructuradas</b> — tres niveles de garantía, y qué no
            garantiza ninguno.</li>
          <li><b>Anti-patrones y depuración</b> — cómo se arregla un prompt con
            método en lugar de por intuición.</li>
        </ol>""",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "01",
        "title": "La estructura de una petición",
        "note": "Antes de las técnicas, la forma. Un prompt no es una cadena suelta.",
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "Los tres roles",
        "title": "Quién dice qué, y qué cambia entre peticiones",
        "html": dg.roles(),
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "Una consecuencia poco conocida",
        "title": "Puedes ponerle palabras en la boca",
        "html": """
        <ul class="pts">
          <li><b>El rol <code>assistant</code> no es solo historial: también acepta
            el <em>principio</em> de la respuesta que quieres.</b>
            <span class="n">Si escribes ahí la primera línea del formato esperado,
            el modelo continúa desde ahí en lugar de decidir por dónde
            empezar.</span></li>
          <li><b>Es la forma más efectiva de forzar un formato sin discutirlo.</b>
            <span class="n">Más fiable que pedir «responde solo con la tabla», que
            es una petición que compite con todo lo demás del contexto.</span></li>
          <li><b>Y sirve para cortar los preámbulos.</b>
            <span class="n">Elimina de raíz el «Claro, con gusto te ayudo con
            eso…» que se come tokens de salida en cada llamada.</span></li>
        </ul>""",
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "02",
        "title": "Instrucciones y contexto",
        "note": "Dos reglas que leídas parecen obvias y aplicadas casi nadie cumple.",
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "Regla 1",
        "title": "Específico quiere decir verificable",
        "html": """
        <div class="cols">
          <div class="col">
            <h3>No es una instrucción</h3>
            <p>«Resume esto brevemente.»</p>
            <p>«Escribe en tono profesional.»</p>
            <p>«Que quede conciso y de alta calidad.»</p>
          </div>
          <div class="col accent">
            <h3>Sí lo es</h3>
            <p>«Resume en máximo tres frases, sin adjetivos valorativos, mencionando
            las cifras exactas que aparezcan.»</p>
            <p>«Escribe como se lo explicarías a alguien del área comercial.»</p>
          </div>
        </div>
        <div class="box" style="margin-top:7mm">
          <p><b>La prueba:</b> si dos personas del equipo pueden cumplir la
          instrucción de formas muy distintas y las dos serían válidas, la
          instrucción está incompleta.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [2],
        "eyebrow": "Regla 2",
        "title": "Di qué hacer, no qué evitar",
        "html": """
        <ul class="pts">
          <li><b>«No uses lenguaje técnico» deja al modelo sin destino.</b>
            <span class="n">Ha excluido una región del espacio de continuaciones,
            pero no ha señalado ninguna. Y encima mantiene el concepto presente en
            el contexto.</span></li>
          <li><b>«Explícalo como a alguien de ventas» sí lo señala.</b>
            <span class="n">Aporta tokens que empujan hacia la zona deseada en lugar
            de describir una zona a evitar.</span></li>
          <li><b>No es psicología del modelo: es cómo se construye la
            predicción.</b>
            <span class="n">Una instrucción positiva añade señal. Una negativa solo
            añade ruido con una etiqueta de prohibición encima.</span></li>
        </ul>""",
    },

    {
        "kind": "content", "covers": [3],
        "eyebrow": "Dónde va cada cosa",
        "title": "La posición dentro del prompt no es neutra",
        "html": """
        <ul class="pts">
          <li><b>Lo crítico va al principio o al final, nunca enterrado.</b>
            <span class="n">Con contextos largos funciona muy bien repetir la
            instrucción clave al final, después del material.</span></li>
          <li><b>El material de referencia va claramente separado.</b>
            <span class="n">Si no se distingue de las instrucciones, el modelo puede
            tratar como orden algo que era un dato.</span></li>
          <li><b>Menos contexto relevante gana a más contexto por si acaso.</b>
            <span class="n">Meter documentos de sobra no es prudencia: es diluir la
            señal que sí importaba.</span></li>
        </ul>""",
    },

    # ── 03 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "03",
        "title": "Ejemplos y delimitadores",
        "note": "Dos herramientas que resuelven problemas distintos y se confunden "
                "todo el tiempo.",
    },

    {
        "kind": "content", "covers": [4],
        "eyebrow": "Cuál usar para qué",
        "title": "Forma se enseña, criterio se explica",
        "html": dg.ejemplos_vs_instrucciones(),
    },

    {
        "kind": "content", "covers": [4],
        "eyebrow": "Advertencias sobre los ejemplos",
        "title": "Cuatro cosas que pasan y no se ven venir",
        "html": """
        <ol class="pts">
          <li><b>El sesgo de los ejemplos se copia.</b>
            <span class="n">Si los tres son largos, las respuestas serán largas. Si
            por casualidad son del mismo tipo, generalizará ese tipo.</span></li>
          <li><b>Hay que incluir el caso difícil.</b>
            <span class="n">Los ejemplos fáciles no enseñan nada que no hiciera ya.
            El valioso es el ambiguo, el que muestra qué hacer cuando falta
            información.</span></li>
          <li><b>Cuestan en cada petición.</b>
            <span class="n">Veinte ejemplos en el prompt se pagan un millón de veces
            si haces un millón de llamadas.</span></li>
          <li><b>Menos rinden más de lo que se cree.</b>
            <span class="n">Dos o tres bien elegidos suelen bastar. La costumbre de
            poner diez viene de modelos de otra generación.</span></li>
        </ol>""",
    },

    {
        "kind": "content", "covers": [5],
        "eyebrow": "Por qué funcionan de verdad",
        "title": "Los delimitadores marcan fronteras, no decoran",
        "html": dg.anatomia_prompt(),
    },

    {
        "kind": "content", "covers": [5],
        "eyebrow": "Un detalle que se vuelve un agujero",
        "title": "Si el contenido viene de fuera, puede cerrar tu etiqueta",
        "html": """
        <div class="box danger">
          <p class="lab">El problema</p>
          <p>Si insertas texto de un usuario entre delimitadores, ese usuario puede
          escribir el delimitador de cierre y seguir escribiendo <b>fuera</b> del
          bloque, donde su texto ya no se lee como dato sino como instrucción.</p>
        </div>
        <ul class="pts" style="margin-top:7mm">
          <li><b>Escapa el contenido</b> antes de insertarlo, o</li>
          <li><b>elige marcas que no puedan aparecer</b> en el contenido, o</li>
          <li><b>usa un identificador aleatorio</b> en la etiqueta de cada
            petición.</li>
        </ul>""",
    },

    # ── 04 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "04",
        "title": "Cadenas de pensamiento",
        "note": "Por qué funcionan, y las cuatro situaciones en que hacen daño.",
    },

    {
        "kind": "content", "covers": [6],
        "eyebrow": "El mecanismo",
        "title": "No piensa más: se construye contexto a sí mismo",
        "html": """
        <div class="box big">
          <p>Cada token generado entra como entrada para el siguiente. Si el modelo
          escribe primero los pasos intermedios, <b>esos pasos ya están en el
          contexto</b> cuando calcula la respuesta final.</p>
        </div>
        <ul class="pts" style="margin-top:7mm">
          <li>Por eso ayuda en problemas de varios pasos, y no en los de uno.</li>
          <li>Por eso el orden importa: primero razonar, después concluir. Si pides
            la conclusión antes, el razonamiento ya no la influye.</li>
        </ul>""",
    },

    {
        "kind": "content", "covers": [6],
        "eyebrow": "Cuándo NO pedirla",
        "title": "Cuatro casos en que resta en lugar de sumar",
        "html": """
        <div class="grid c4">
          <div class="card no"><div class="k">01</div>
            <div class="t">Con modelos de razonamiento</div>
            <div class="d">Ya generan pensamiento intermedio por su cuenta. Pedirlo
            además interfiere y duplica el gasto.</div></div>
          <div class="card no"><div class="k">02</div>
            <div class="t">En tareas de un solo paso</div>
            <div class="d">Clasificar, extraer un campo, traducir. No hay
            razonamiento intermedio que aportar.</div></div>
          <div class="card no"><div class="k">03</div>
            <div class="t">Cuando la latencia importa</div>
            <div class="d">Todo ese texto se genera antes de que aparezca la primera
            palabra útil.</div></div>
          <div class="card no"><div class="k">04</div>
            <div class="t">Con salida estructurada limpia</div>
            <div class="d">Mezclar razonamiento y datos complica el parseo. Sepáralos
            en dos campos o en dos llamadas.</div></div>
        </div>""",
    },

    # ── 05 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "05",
        "title": "Salidas estructuradas",
        "note": "Tres niveles de garantía. Conviene saber cuál tienes.",
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "Del deseo a la garantía",
        "title": "Tres niveles, y lo que asegura cada uno",
        "html": dg.rigor_salida(),
    },

    {
        "kind": "content", "covers": [7],
        "eyebrow": "Diseño del esquema",
        "title": "El esquema también es prompt engineering",
        "html": """
        <ul class="pts">
          <li><b>El nombre del campo es una instrucción.</b>
            <span class="n"><code>monto_total_con_impuestos</code> guía mucho mejor
            que <code>total</code>.</span></li>
          <li><b>Describe cada campo dentro del esquema.</b>
            <span class="n">La mayoría de los formatos lo permiten y esa descripción
            llega al modelo.</span></li>
          <li><b>Planos antes que profundos.</b>
            <span class="n">La calidad se degrada con el anidamiento. Tres niveles
            ya es mucho.</span></li>
          <li><b>Siempre una salida para abstenerse.</b>
            <span class="n">Un booleano <code>encontrado</code> o un nivel de
            confianza. Un esquema que obliga a llenar un campo obliga al modelo a
            inventarlo.</span></li>
        </ul>""",
    },

    # ── 06 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "06",
        "title": "Anti-patrones y depuración",
        "note": "Lo que separa a quien improvisa de quien controla.",
    },

    {
        "kind": "content", "covers": [8],
        "eyebrow": "Los tres que más se repiten",
        "title": "Anti-patrones",
        "html": """
        <div class="grid c3">
          <div class="card no"><div class="k">01</div>
            <div class="t">El prompt kilométrico</div>
            <div class="d">Creció por acumulación durante meses y ya nadie sabe qué
            línea hace qué. Nadie se atreve a borrar nada por si acaso.</div></div>
          <div class="card no"><div class="k">02</div>
            <div class="t">Instrucciones que se contradicen</div>
            <div class="d">Se añadieron en momentos distintos para arreglar casos
            distintos. El modelo obedece una y parece que ignora la otra.</div></div>
          <div class="card no"><div class="k">03</div>
            <div class="t">Adjetivos vacíos</div>
            <div class="d">Profesional, conciso, de alta calidad, claro. No
            restringen nada y ocupan espacio.</div></div>
        </div>""",
    },

    {
        "kind": "content", "covers": [9],
        "eyebrow": "El método",
        "title": "Cómo se depura un prompt",
        "html": """
        <ol class="pts">
          <li><b>Junta quince o veinte casos reales antes de tocar nada.</b>
            <span class="n">Sin un conjunto fijo no puedes saber si un cambio mejoró
            o solo movió el problema de sitio.</span></li>
          <li><b>Cambia una cosa a la vez</b> y vuelve a pasar los casos.</li>
          <li><b>Registra el prompt exacto que se envió</b>, no la plantilla.
            <span class="n">Un bug que no puedes reproducir es un bug que no puedes
            arreglar.</span></li>
          <li><b>Sabe cuándo parar.</b>
            <span class="n">Si van cinco iteraciones y sigue fallando, el problema
            probablemente no es el prompt: le falta contexto, le falta una
            herramienta, o el modelo es el equivocado.</span></li>
        </ol>""",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Cierre",
        "title": "Lo que te llevas de esta sesión",
        "html": """
        <div class="grid c4">
          <div class="card"><div class="k">01</div><div class="t">Tres roles, no un texto</div>
            <div class="d">Lo estable arriba, lo variable abajo.</div></div>
          <div class="card"><div class="k">02</div><div class="t">Específico = verificable</div>
            <div class="d">Si dos personas lo cumplen distinto, falta precisión.</div></div>
          <div class="card"><div class="k">03</div><div class="t">Di qué hacer</div>
            <div class="d">Lo negativo excluye pero no señala.</div></div>
          <div class="card"><div class="k">04</div><div class="t">La posición pesa</div>
            <div class="d">Nada crítico enterrado en medio.</div></div>
          <div class="card"><div class="k">05</div><div class="t">Ejemplos para forma</div>
            <div class="d">Instrucciones para criterio.</div></div>
          <div class="card"><div class="k">06</div><div class="t">Razonar no siempre suma</div>
            <div class="d">Hay cuatro casos donde estorba.</div></div>
          <div class="card"><div class="k">07</div><div class="t">Deja salida para «no sé»</div>
            <div class="d">Si obligas a llenar, se inventa.</div></div>
          <div class="card no"><div class="k">✓</div><div class="t">Depura con casos fijos</div>
            <div class="d">No por impresión.</div></div>
        </div>""",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ejercicio práctico",
        "title": "Rediseña un prompt tuyo de producción",
        "html": """
        <ol class="pts">
          <li><b>Reúne diez casos de entrada reales</b> y registra la salida actual
            de cada uno.</li>
          <li><b>Reescribe el prompt aplicando la sesión:</b> separa roles, delimita
            bloques, convierte lo negativo en positivo, sustituye los adjetivos
            vacíos por criterios medibles y añade un esquema con campo para
            abstenerse.</li>
          <li><b>Vuelve a pasar los diez casos</b> y compara en una tabla de tres
            columnas: caso, antes, después.</li>
          <li><b>Mide los tokens de las dos versiones</b> y anota la diferencia.</li>
        </ol>
        <div class="box" style="margin-top:6mm">
          <p>La entrega es la tabla más un párrafo explicando <b>qué cambio produjo
          la mejora y por qué</b>, apoyándote en cómo se construye la predicción.</p>
        </div>""",
    },
]


NOTES = [
    {
        "lead": "Módulo 5 · Prompt engineering — láminas 1 a 14.",
        "rows": [
            ("2", "Descarta de entrada la lectura popular del tema: no van a "
                  "aprender trucos ni palabras mágicas. Plantéalo como un problema "
                  "de diseño de entrada y todo lo demás se deduce."),
            ("6", "Lo de poner palabras en boca del asistente sorprende siempre. Si "
                  "hay tiempo, demuéstralo en vivo: es de las cosas que más "
                  "rápido adopta la gente."),
            ("8", "Aplica la prueba con la sala. Pide una instrucción vaga, que dos "
                  "personas digan cómo la cumplirían, y deja que la diferencia "
                  "hable sola."),
            ("13", "<b>Insiste en que los delimitadores no son cosmética.</b> Y el "
                   "agujero del cierre de etiqueta conviene enseñarlo aquí aunque "
                   "duela: es un fallo real y barato de evitar."),
        ],
    },
    {
        "lead": "Láminas 15 a 24.",
        "rows": [
            ("16", "El punto contraintuitivo del módulo. Casi todo el mundo cree que "
                   "pedir razonamiento siempre ayuda. Detente en el primer caso: con "
                   "modelos de razonamiento puede empeorar el resultado."),
            ("18", "Recorre los tres niveles de izquierda a derecha y pregunta en "
                   "cuál está su sistema hoy. Casi siempre en el primero."),
            ("19", "La regla que hay que dejar dicha en voz alta: el esquema "
                   "garantiza la forma, nunca la verdad. Valida en tu código de "
                   "todos modos."),
            ("22", "<b>El método vale más que las técnicas.</b> Si se llevan una "
                   "sola práctica, que sea la de los veinte casos fijos antes de "
                   "tocar el prompt."),
        ],
    },
]
