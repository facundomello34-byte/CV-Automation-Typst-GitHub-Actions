#set document(title: "Facundo Octavio Mello · CV", author: "Facundo Octavio Mello")
#set page(paper: "a4", margin: (x: 1.5cm, y: 1.15cm))
#set text(font: ("Lato", "Liberation Sans"), size: 10.0pt, fill: rgb("#374151"), lang: "es", hyphenate: false)
#set par(justify: false, leading: 0.53em, spacing: 0.53em)
#set list(indent: 0.3em, body-indent: 0.25em, spacing: 0.22em, marker: text(fill: rgb("#2563EB"), size: 8.5pt)[•])

#let petrol = rgb("#17324D")
#let blue = rgb("#2563EB")
#let gray = rgb("#374151")
#let light = rgb("#E5E7EB")
#let muted = rgb("#6B7280")

#let section(title, body) = {
  v(0.6em)
  text(size: 10.5pt, weight: "bold", fill: petrol, tracking: 0.08em)[#upper(title)]
  v(-0.42em)
  line(length: 100%, stroke: 0.5pt + light)
  v(0.18em)
  body
}

#let job(title, subtitle, dates) = block(width: 100%)[
  #text(weight: "bold", fill: petrol)[#title] #text(fill: gray)[· #subtitle] #h(1fr) #text(size: 8.8pt, fill: muted)[#dates]
]

#align(center)[
  #text(size: 21pt, weight: "black", fill: petrol, tracking: 0.01em)[FACUNDO OCTAVIO MELLO]
  #v(-0.22em)
  #text(size: 10.4pt, weight: "medium", fill: gray)[Estudiante de Desarrollo de Software · Soporte IT · QA · Análisis Funcional]
  #v(-0.16em)
  #text(size: 8.9pt, fill: gray)[Castelar, Buenos Aires · (+54) 9 11 2408 4431 · facundomello34\@gmail.com]
  #linebreak()
  #text(size: 8.9pt)[#link("https://www.linkedin.com/in/facundo-octavio-mello-ferreira-8a4206265")[#text(fill: blue)[LinkedIn]] #text(fill: muted)[|] #link("https://github.com/facundomello34-byte")[#text(fill: blue)[GitHub]] #text(fill: muted)[|] #link("https://avenor-software.web.app/")[#text(fill: blue)[AVENOR]]]
]

#v(0.28em)
#line(length: 100%, stroke: 0.6pt + light)

#section("Perfil")[
  Estudiante de Desarrollo de Software en UADE (promedio 8.67) con experiencia operativa en sistemas de gestión, resolución de incidencias y automatización de tareas. Manejo Python, SQL, Linux, Git y Docker, y desarrollo un SaaS propio con FastAPI, PostgreSQL y Playwright. Busco una posición Trainee, Junior o pasantía en desarrollo, soporte IT, QA, análisis funcional o automatización. Inglés técnico en curso con clases particulares.
]

#section("Competencias")[
  #text(weight: "bold", fill: petrol)[Desarrollo y bases de datos:] Python, JavaScript, HTML/CSS, FastAPI, Next.js, SQL, PostgreSQL.
  #linebreak()
  #text(weight: "bold", fill: petrol)[Soporte técnico y sistemas:] Windows, Linux (uso diario), hardware, impresoras, redes Wi-Fi, PDA, sistemas POS (FUDO, MAXIREST), resolución de incidencias.
  #linebreak()
  #text(weight: "bold", fill: petrol)[QA, análisis y automatización:] Playwright, pruebas E2E, validación de datos, relevamiento de requerimientos, documentación técnica, mejora de procesos.
  #linebreak()
  #text(weight: "bold", fill: petrol)[Herramientas y tecnologías:] Git/GitHub, Docker, bash, terminal/CLI.
]

#section("Experiencia")[
  #job([COTO Digital (COTO CICSA)], [Operador], [Oct 2025 – presente])
  #list(
    [Operé PDA y sistemas internos para impresión y control de comprobantes. Gestioné tickets operativos y el seguimiento de pedidos para sostener la continuidad de la operación.],
    [Resolví fallas básicas de impresoras y equipos para sostener la continuidad del sector.],
    [Detecté tareas repetitivas y optimicé procesos con las herramientas disponibles.],
  )
  #job([Bon Air Cafetería], [Encargado Administrativo], [Nov 2024 – Sep 2025])
  #list(
    [Administré ventas, inventario y cierres de caja con el sistema FUDO POS.],
    [Resolví incidencias del sistema para evitar interrupciones en la operación.],
    [Implementé soluciones digitales para automatizar el registro de ventas, el control de stock y los cierres diarios.],
  )
  #job([Havanna], [Soporte Operativo], [Feb 2024 – Jul 2024])
  #list(
    [Operé el sistema MAXIREST para el control de la operación y la validación de información.],
    [Brindé asistencia técnica básica a las computadoras de los mozos y colaboré con la continuidad del servicio.],
    [Gestioné la caja y el funcionamiento del sector.],
  )
]

#section("Proyectos")[
  #job([AVENOR], [Plataforma SaaS de automatización para comercios · Proyecto personal], [2025 – presente])
  #list(
    [Desarrollé un prototipo funcional de SaaS para automatizar procesos comerciales, administrativos y operativos.],
    [Implementé lógica de negocio, gestión de datos en PostgreSQL e integración de servicios con FastAPI, con módulos de pedidos, inventarios y automatización.],
    [Construí el prototipo con Python, FastAPI, PostgreSQL, Docker, JavaScript, Next.js y Playwright; quedan pendientes la estrategia de testing y el despliegue productivo.],
  )
  #job([Sistema de Stock Automatizado], [Proyecto académico UADE · Cafetería], [2025])
  #list(
    [Desarrollé una aplicación de gestión de inventarios en Python a partir de necesidades operativas del sector gastronómico.],
    [Implementé estructuras de datos, funciones y lógica de negocio para administrar productos, clientes y ventas.],
    [Automaticé el registro de movimientos de stock y la generación de reportes para el control de inventario.],
  )
  #job([Chocolates Chiazza], [Análisis y diseño de un sistema de gestión de stock · Proyecto integrador UADE], [])
  #list(
    [Analicé procesos y realicé un diagnóstico organizacional (FODA) sobre el control manual de materias primas.],
    [Relevé necesidades y definí requerimientos funcionales, niveles mínimos de seguridad, reportes y alertas de reposición por WhatsApp o Telegram.],
    [Diseñé una propuesta de sistema de información para centralizar compras, consumos e inventarios. Proyecto académico, no implementado ni desplegado en la empresa.],
  )
]

#section("Educación")[
  #job([Tecnicatura Universitaria en Desarrollo de Software], [UADE], [2025 – 2028 (en curso)])
  #text(size: 8.7pt, fill: muted)[Promedio 8.67 · Graduación estimada: fines de 2028.]
  #job([Inglés técnico], [Clases particulares], [2026 – en curso])
  #text(size: 8.7pt, fill: muted)[Lectura de documentación y vocabulario técnico.]
  #job([Fundamentos de Ciberseguridad], [Curso certificado], [Ago 2026])
  #text(size: 8.7pt, fill: muted)[48.5 h.]
]

#v(0.45em)
#text(size: 8.7pt, fill: muted)[Disponibilidad: inmediata, coordinable con mi empleador actual · Presencial, híbrida o remota · Castelar, Buenos Aires.]
