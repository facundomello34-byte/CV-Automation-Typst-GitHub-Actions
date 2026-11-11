#set page(paper: "a4", margin: (x: 1.55cm, y: 1.25cm))
#set text(font: ("Liberation Sans", "DejaVu Sans"), size: 9.8pt, lang: "es", hyphenate: false)
#set par(justify: false, leading: 0.5em, spacing: 0.55em)
#set list(indent: 0.32em, body-indent: 0.26em, spacing: 0.22em)

#let section(title, body) = {
  v(0.5em)
  text(size: 10.2pt, weight: "bold", tracking: 0.06em)[#upper(title)]
  v(-0.42em)
  line(length: 100%, stroke: 0.5pt)
  v(0.1em)
  body
}

#let job(role, company, dates) = block(width: 100%)[
  #text(weight: "bold")[#role] · #company #h(1fr) #text(size: 8.5pt)[#dates]
]

#align(center)[
  #text(size: 18pt, weight: "bold", tracking: 0.02em)[FACUNDO OCTAVIO MELLO]
  #v(-0.25em)
  #text(size: 9.8pt)[Estudiante de Desarrollo de Software · Pasantías en Administración, Operaciones y Gestión de Información]
  #v(-0.2em)
  #text(size: 8.6pt)[Castelar, Buenos Aires · (+54) 9 11 2408 4431 · facundomello34\@gmail.com]
  #linebreak()
  #text(size: 8.6pt)[#link("https://www.linkedin.com/in/facundo-octavio-mello-ferreira-8a4206265")[linkedin.com/in/facundo-octavio-mello-ferreira-8a4206265]]
  #linebreak()
  #text(size: 8.6pt)[#link("https://github.com/facundomello34-byte")[github.com/facundomello34-byte] · #link("https://avenor-software.web.app/")[avenor-software.web.app]]
]

#section("Perfil")[
  Estudiante de la Tecnicatura Universitaria en Desarrollo de Software en UADE (promedio 8.67) con experiencia en administración de locales, control de stock, cierres de caja y uso de sistemas de gestión (FUDO POS, MAXIREST). Busco una pasantía en administración, operaciones, logística o gestión de información donde pueda aportar orden, validación de datos y automatización de tareas. Manejo herramientas digitales y tengo formación en Python y SQL.
]

#section("Competencias")[
#text(weight: "bold")[Administración y operaciones:] control de stock e inventarios, cierres de caja, registro y validación de datos, seguimiento de pedidos, atención de incidencias.
#linebreak()
#text(weight: "bold")[Sistemas:] FUDO POS, MAXIREST, PDA, sistemas internos, Windows.
#linebreak()
#text(weight: "bold")[Datos y automatización:] Python, SQL, PostgreSQL, Git/GitHub; automatización de reportes y tareas repetitivas.
#linebreak()
#text(weight: "bold")[Competencias:] organización, atención al detalle, trabajo en equipo, resolución de problemas, aprendizaje rápido.
#linebreak()
#text(weight: "bold")[Idiomas:] español nativo; inglés técnico (lectura de documentación), en formación.
]

#section("Experiencia")[
#job([Operador], [COTO Digital (COTO CICSA)], [Oct 2025 – presente])
#list(
  [Emisión de tickets, seguimiento de pedidos y control de vouchers con PDA y sistemas internos.],
  [Resolución de incidencias técnicas básicas para sostener la continuidad de la operación.],
  [Optimización de tareas repetitivas mediante el uso eficiente de las herramientas disponibles.],
)
#job([Encargado Administrativo], [Bon Air Cafetería], [Nov 2024 – Sep 2025])
#list(
  [Administración integral del local: ventas, control de stock y cierres de caja con FUDO POS.],
  [Implementación de soluciones digitales para automatizar el registro de ventas, el stock y los cierres diarios.],
  [Validación y registro de datos operativos; resolución de incidencias del sistema.],
)
#job([Soporte Operativo], [Havanna], [Feb 2024 – Jul 2024])
#list(
  [Manejo y control de los sistemas internos de la operación con MAXIREST.],
  [Validación de información y soporte a las computadoras de los mozos.],
  [Responsable de caja y del funcionamiento del sector.],
)
]

#section("Proyectos")[
#job([Sistema de Stock Automatizado], [Proyecto UADE], [2025])
#list(
  [Backend en Python para la gestión de stock de una cafetería: productos, clientes, ventas, reportes y automatización de inventario.],
)
#job([AVENOR · Plataforma SaaS de automatización para comercios], [Proyecto propio], [2025 – presente])
#list(
  [Desarrollo de un SaaS para automatizar procesos administrativos de comercios con Python, FastAPI, PostgreSQL, Docker y Playwright.],
  [Automatización de tareas, integración de servicios y pruebas E2E.],
)
]

#section("Educación")[
#job([Tecnicatura Universitaria en Desarrollo de Software], [UADE], [2025 – 2028 (en curso)])
#text(size: 8.8pt)[Promedio 8.67.]
#job([Inglés técnico], [Clases particulares], [2026 – en curso])
#text(size: 8.8pt)[Lectura de documentación y vocabulario técnico.]
#job([Fundamentos de Ciberseguridad], [Curso certificado], [Ago 2026])
#text(size: 8.8pt)[48.5 h.]
]

#v(0.45em)
#text(size: 8.6pt)[Disponibilidad: inmediata, coordinable con mi empleador actual · Presencial, híbrida o remota · Castelar, Buenos Aires.]
