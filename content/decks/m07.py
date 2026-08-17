# -*- coding: utf-8 -*-
"""Deck: Módulo 7 — El LLM como servicio: API frente a chat."""

from engine.diagrams import mod07 as dg

DECK = {
    "mark": "HyperLabs",
    "title": "Módulo 7 · API frente a chat",
    "footer": "Programa de AI · Módulo 7",
    "outfile": "Modulo 07 - API frente a chat.pdf",
}


SLIDES = [
    {
        "kind": "cover",
        "kicker": "MÓDULO 7  ·  2 HORAS",
        "title": "El LLM como servicio",
        "tagline": "La API no tiene memoria. La arquitectura de contexto la diseñas "
                   "tú.",
        "meta": [
            "<b>Antes de esta sesión:</b> cómo se le habla a un modelo",
            "<b>Al terminar:</b> construyes una conversación desde cero y sabes lo "
            "que cuesta",
        ],
    },

    {
        "kind": "statement",
        "text": "Cada petición a la API es, literalmente, <em>el primer mensaje</em>.",
        "after": "No hay sesión. No hay usuario. No hay nada de lo que dijiste hace "
                 "dos minutos. Y esa sola frase reorganiza todo lo que viene "
                 "después.",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ruta de la sesión",
        "title": "Lo que vamos a ver",
        "html": """
        <ol class="pts">
          <li><b>Chat frente a API</b> — qué hace uno que el otro no.</li>
          <li><b>La petición mínima</b> — modelo, mensajes y parámetros.</li>
          <li><b>La ausencia de estado</b> — demostrada en tres peticiones.</li>
          <li><b>Simular una conversación</b> — y lo que eso cuesta.</li>
          <li><b>El campo de uso</b> — la fuente de verdad de tu consumo.</li>
          <li><b>Streaming, errores y límites</b> — lo que sí va a pasar en
            producción.</li>
        </ol>""",
    },

    # ── 01 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "01",
        "title": "Chat frente a API",
        "note": "Casi todos han usado un chat. Casi nadie ha pensado en qué hace "
                "que la API no haga.",
    },

    {
        "kind": "content", "covers": [1],
        "eyebrow": "La lista completa",
        "title": "Todo lo que el chat hace por ti",
        "html": dg.chat_vs_api(),
    },

    # ── 02 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "02",
        "title": "La petición",
        "note": "Modelo, mensajes y parámetros. Y una demostración que conviene "
                "hacer en vivo.",
    },

    {
        "kind": "content", "covers": [3, 4],
        "eyebrow": "La demostración",
        "title": "Tres peticiones que lo dejan claro",
        "html": dg.sin_estado(),
    },

    {
        "kind": "content", "covers": [2, 5],
        "eyebrow": "Los campos de la petición",
        "title": "Qué se manda y qué controla cada cosa",
        "html": """
        <table>
          <thead><tr><th style="width:24%">Campo</th><th style="width:40%">Qué es</th>
          <th>Lo que hay que saber</th></tr></thead>
          <tbody>
            <tr><td><b>modelo</b></td><td>Cuál de todos, con su versión.</td>
              <td>Fíjalo explícitamente. Los alias que apuntan «al último» cambian
                  el comportamiento sin avisar.</td></tr>
            <tr><td><b>mensajes</b></td><td>La lista completa, con sus roles.</td>
              <td>Aquí va todo el estado que quieras que exista. No hay otro
                  sitio.</td></tr>
            <tr><td><b>temperatura, top-p</b></td><td>Cómo se muestrea.</td>
              <td>Ajusta una u otra, no las dos.</td></tr>
            <tr><td><b>máximo de salida</b></td><td>Tope duro de tokens
                  generados.</td>
              <td>No es una sugerencia de longitud: si se alcanza, la respuesta se
                  corta a media frase.</td></tr>
            <tr><td><b>secuencias de parada</b></td><td>Texto que detiene la
                  generación.</td>
              <td>Útil con formatos propios.</td></tr>
            <tr><td><b>semilla</b></td><td>Intento de reproducibilidad.</td>
              <td>No garantiza determinismo en un servicio distribuido.</td></tr>
          </tbody>
        </table>
        <div class="box" style="margin-top:6mm">
          <p><b>Revisa siempre el motivo de finalización que devuelve la API.</b> Es
          lo único que distingue «terminó de responder» de «se quedó sin
          espacio», y los dos casos se ven igual desde fuera.</p>
        </div>""",
    },

    # ── 03 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "03",
        "title": "Lo que cuesta simular memoria",
        "note": "La consecuencia económica de reenviar el historial completo.",
    },

    {
        "kind": "content", "covers": [4],
        "eyebrow": "Turno a turno",
        "title": "Lo que mandas en cada petición de una conversación",
        "html": dg.crecimiento_historial(),
    },

    {
        "kind": "content", "covers": [6],
        "eyebrow": "El dato que hay que registrar desde la primera línea",
        "title": "El campo de uso de la respuesta",
        "html": """
        <ul class="pts">
          <li><b>Toda respuesta trae cuántos tokens costó.</b>
            <span class="n">De entrada, de salida, y según el proveedor también de
            razonamiento y de caché. Es la única fuente de verdad de tu
            consumo.</span></li>
          <li><b>Regístralo desde el primer día, no cuando llegue la factura.</b>
            <span class="n">Sin ese registro no puedes atribuir el gasto a una
            funcionalidad ni a un usuario, y cuando la factura suba no vas a saber
            qué recortar.</span></li>
          <li><b>Estimarlo a mano falla por mucho.</b>
            <span class="n">El texto que crees que mandas y el que realmente sale
            de tu sistema rara vez coinciden.</span></li>
        </ul>
        <div class="box" style="margin-top:6mm">
          <p>Con ese campo y un identificador de sesión ya puedes responder cuánto
          cuesta una conversación media. Es el cálculo más útil que vas a hacer en
          las primeras semanas de un proyecto.</p>
        </div>""",
    },

    # ── 04 ────────────────────────────────────────────────────────────────
    {
        "kind": "section", "step": "04",
        "title": "Lo que pasa en producción",
        "note": "Streaming, errores y límites de tasa.",
    },

    {
        "kind": "content", "covers": [7, 8],
        "eyebrow": "Dos realidades del servicio",
        "title": "Streaming y fallos",
        "html": """
        <div class="cols">
          <div class="col accent">
            <h3>Streaming</h3>
            <p>Los tokens aparecen uno a uno <b>porque se generan uno a uno</b>. La
            API los va enviando conforme salen.</p>
            <p>No es un efecto visual: baja mucho el tiempo percibido hasta la
            primera palabra, sin cambiar la latencia total.</p>
          </div>
          <div class="col">
            <h3>Lo que va a fallar</h3>
            <p>Límites de tasa. Saturación temporal del proveedor. Exceso de
            contexto. Respuestas que no cumplen el formato.</p>
            <p>No son casos raros: son el funcionamiento normal de un servicio
            compartido.</p>
          </div>
        </div>
        <div class="box alerta" style="margin-top:7mm">
          <p class="lab">La política mínima</p>
          <p>Reintento con espera creciente, un tope de intentos y un
          <b>presupuesto de reintentos</b>. Un bucle de reintentos sin límite no es
          un bug de robustez: es un incidente de facturación.</p>
        </div>""",
    },

    {
        "kind": "content", "covers": [9],
        "eyebrow": "Antes de cerrar",
        "title": "Acabas de usar un protocolo de comunicación",
        "html": """
        <ul class="pts">
          <li><b>Una API REST sobre HTTP: tú preguntas, el servidor responde.</b>
            <span class="n">Es un contrato entre dos sistemas que no se conocen:
            quién habla primero, en qué formato y qué significa cada
            respuesta.</span></li>
          <li><b>No es el único que va a aparecer en un sistema de AI.</b>
            <span class="n">Hay otros para cuando el trabajo tarda horas, para
            cuando los datos fluyen en vez de llegar de golpe, y para cuando quien
            necesita leer el contrato no es tu código.</span></li>
          <li><b>Los veremos juntos y por comparación.</b>
            <span class="n">Antes hace falta entender qué necesita un sistema que
            actúa por su cuenta, porque ese es el problema que los otros
            resuelven.</span></li>
        </ul>""",
    },

    {
        "kind": "content", "covers": [],
        "eyebrow": "Ejercicio práctico",
        "title": "Un chat de consola en menos de cincuenta líneas",
        "html": """
        <ol class="pts">
          <li><b>Sin bibliotecas de orquestación.</b> Mantén el historial en una
            lista y reenvíalo completo en cada turno.</li>
          <li><b>Imprime, después de cada respuesta</b>, los tokens de entrada, los
            de salida y el costo acumulado de la sesión con precios reales.</li>
          <li><b>Corta el historial</b> cuando supere un límite configurable, y avisa
            en pantalla cuando lo hagas.</li>
          <li><b>Consume la respuesta por streaming.</b></li>
        </ol>
        <div class="box big" style="margin-top:6mm">
          <p>La entrega incluye una captura tras veinte turnos y una respuesta
          escrita a: <b>¿por qué el turno veinte cuesta tanto más que el
          primero?</b></p>
        </div>""",
    },
]


NOTES = [
    {
        "lead": "Módulo 7 · El LLM como servicio.",
        "rows": [
            ("2", "Es el eje de la sesión y conviene decirlo antes de mostrar una "
                  "sola línea de código."),
            ("6", "<b>Construye la tabla con la sala antes de proyectarla.</b> "
                  "Pregunta qué hace un chat que la API no haga y deja que la "
                  "columna derecha se llene sola. La columna derecha es, en la "
                  "práctica, el índice de lo que queda del programa."),
            ("8", "<b>Hazlo en vivo.</b> Dos peticiones bastan para demostrar la "
                  "ausencia de estado, y la demostración convence mucho más que la "
                  "explicación."),
            ("11", "Deriva el crecimiento con ellos. El objetivo no es la cifra: es "
                   "la incomodidad de ver que el costo de una conversación no crece "
                   "de forma lineal."),
            ("12", "Insiste en registrar el campo de uso desde la primera línea de "
                   "código. Es una decisión de cinco minutos que después vale meses."),
            ("15", "Cierra abriendo el hilo de los protocolos, sin desarrollarlo. "
                   "Prepara la siguiente parte sin adelantar contenido."),
        ],
    },
]
