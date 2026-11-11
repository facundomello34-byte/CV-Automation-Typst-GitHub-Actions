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
  #text(size: 9.8pt)[Estudiante de Desarrollo de Software · Soporte IT / QA / Análisis Funcional]
  #v(-0.2em)
  #text(size: 8.6pt)[Castelar, Buenos Aires · (+54) 9 11 2408 4431 · facundomello34\@gmail.com]
  #linebreak()
  #text(size: 8.6pt)[#link("https://www.linkedin.com/in/facundo-octavio-mello-ferreira-8a4206265")[linkedin.com/in/facundo-octavio-mello-ferreira-8a4206265]]
  #linebreak()
  #text(size: 8.6pt)[#link("https://github.com/facundomello34-byte")[github.com/facundomello34-byte] · #link("https://avenor-software.web.app/")[avenor-software.web.app]]
]

#section("Perfil")[
  Estudiante de la Tecnicatura Universitaria en Desarrollo de Software en UADE (promedio 8.67) con experiencia operativa en sistemas de gestión, resolución de incidencias de primera línea y automatización de tareas. Busco una pasantía o posición junior en soporte técnico, QA, análisis funcional o automatización. Uso Linux a diario y trabajo con Python, SQL, Git y Docker. Inglés técnico en curso (clases particulares), orientado a lectura de documentación.
]

#section("Competencias")[
#text(weight: "bold")[Soporte IT:] Windows, Linux (uso diario), hardware, impresoras, redes Wi-Fi, PDA, sistemas POS, emisión y seguimiento de tickets, atención de usuarios.
#linebreak()
#text(weight: "bold")[Desarrollo y datos:] Python, JavaScript, HTML/CSS, FastAPI, Next.js, SQL, PostgreSQL.
#linebreak()
#text(weight: "bold")[QA y análisis:] pruebas E2E, validación de datos, relevamiento de requerimientos, documentación técnica, mejora de procesos.
#linebreak()
#text(weight: "bold")[Herramientas:] Git/GitHub, Docker, Playwright, bash.
#linebreak()
#text(weight: "bold")[Idiomas:] español nativo; inglés técnico en curso (clases particulares), lectura de documentación.
]

#section("Experiencia")[
#job([Operador], [COTO Digital (COTO CICSA)], [Oct 2025 – presente])
#list(
  [Operación diaria con PDA y sistemas internos: impresión y control de vouchers, emisión de tickets y seguimiento de pedidos.],
  [Resolución autónoma de fallas básicas de impresoras y equipos para sostener la continuidad del sector.],
  [Detección de tareas repetitivas y optimización del uso de las herramientas disponibles.],
)
#job([Encargado Administrativo], [Bon Air Cafetería], [Nov 2024 – Sep 2025])
#list(
  [Administración integral del local con el sistema de gestión FUDO POS: ventas, stock y cierres de caja.],
  [Resolución de incidencias del sistema para evitar interrupciones en la operación.],
  [Implementación de soluciones digitales para automatizar el registro de ventas, el control de stock y los cierres diarios.],
)
#job([Soporte Operativo], [Havanna], [Feb 2024 – Jul 2024])
#list(
  [Manejo y soporte de los sistemas internos de la operación con el software MAXIREST.],
  [Validación de información y soporte técnico a las computadoras de los mozos.],
  [Responsable de caja y del correcto funcionamiento del sector.],
)
]

#section("Proyectos")[
#job([AVENOR · Plataforma SaaS de automatización para comercios], [Proyecto personal], [2025 – presente])
#list(
  [Desarrollo de un prototipo funcional de plataforma SaaS para automatizar procesos comerciales, administrativos y operativos.],
  [Implementación de lógica de negocio, gestión de información en PostgreSQL e integración de servicios con FastAPI; funcionalidades de pedidos, inventarios y automatización.],
  [Stack: Python, FastAPI, PostgreSQL, Docker, JavaScript, Next.js y Playwright. Proyecto en desarrollo, con estrategia de testing y despliegue productivo pendientes.],
)
#job([Sistema de Stock Automatizado], [Proyecto académico UADE · Cafetería], [2025])
#list(
  [Desarrollo de una aplicación de gestión de inventarios en Python, basada en necesidades operativas del sector gastronómico.],
  [Implementación de estructuras de datos, funciones y lógica de negocio para administrar productos, clientes y ventas.],
  [Automatización del registro de movimientos de stock y generación de reportes para el control de inventarios.],
)
#job([Chocolates Chiazza · Análisis y diseño de un sistema de gestión de stock], [Proyecto integrador UADE], [])
#list(
  [Análisis de procesos empresariales y diagnóstico organizacional (FODA) sobre el control manual de materias primas.],
  [Diseño de una propuesta de sistema de información para centralizar compras, consumos e inventarios, con requerimientos funcionales, seguridad mínima, reportes y alertas de reposición por WhatsApp o Telegram.],
  [Proyecto académico de análisis y propuesta de mejora; no fue un sistema implementado ni desplegado en la empresa.],
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
