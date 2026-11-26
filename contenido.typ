// =============================================================================
// contenido.typ — el contenido del CV, sin nada de diseño.
//
// Acá vive el texto real: perfil, competencias, experiencia, proyectos y
// educación. Las variantes (QA, soporte, desarrollo, inglés) importan este
// archivo y eligen qué mostrar y en qué orden; no reescriben el texto ni
// tocan el formato. Si un dato cambia, se cambia acá una sola vez.
// =============================================================================

// --- Datos de contacto ----------------------------------------------------
#let nombre = "FACUNDO OCTAVIO MELLO"
#let headline = "Estudiante de Desarrollo de Software · Soporte IT · QA · Análisis Funcional"
#let contacto = "Castelar, Buenos Aires · (+54) 9 11 2408 4431 · facundomello34@gmail.com"
#let links = (
  ("LinkedIn", "https://www.linkedin.com/in/facundo-octavio-mello-ferreira-8a4206265"),
  ("GitHub", "https://github.com/facundomello34-byte"),
  ("AVENOR", "https://avenor-software.web.app/"),
)
#let disponibilidad = "Disponibilidad: inmediata, coordinable con mi empleador actual · Presencial, híbrida o remota · Castelar, Buenos Aires."

// --- Perfil ---------------------------------------------------------------
#let perfil = [
  Estudiante de Desarrollo de Software en UADE (promedio 8.67) con experiencia
  operativa en sistemas de gestión, soporte de primera línea y automatización de
  tareas. Manejo Python, SQL, PostgreSQL, Linux y Git, y tengo aplicaciones propias
  desplegadas y en uso con Next.js, React, TypeScript y Playwright.
  Busco una posición Trainee, Junior o pasantía en desarrollo, soporte IT, QA o
  análisis funcional. Inglés técnico: lectura de documentación.
]

// --- Competencias ---------------------------------------------------------
#let competencias = (
  (
    "Desarrollo y bases de datos",
    "Python, JavaScript, TypeScript, HTML/CSS, FastAPI, React, Next.js, SQL, PostgreSQL.",
  ),
  (
    "Soporte técnico y sistemas",
    "Windows, Linux (uso diario), hardware, impresoras, redes Wi-Fi, PDA, sistemas POS (FUDO, MAXIREST), resolución de incidencias.",
  ),
  (
    "QA, análisis y automatización",
    "Playwright, pruebas E2E, validación de datos, relevamiento de requerimientos, documentación técnica, mejora de procesos.",
  ),
  (
    "Herramientas y tecnologías",
    "Git/GitHub, Docker, Vercel, bash, terminal/CLI.",
  ),
)

// --- Experiencia ----------------------------------------------------------
// Campos de cada entrada: title, subtitle, dates, bullets.
#let experiencia = (
  (
    title: "COTO Digital (COTO CICSA)",
    subtitle: "Operador",
    dates: "Oct 2025 – presente",
    bullets: (
      [Operé PDA y sistemas internos para impresión y control de comprobantes. Gestioné tickets operativos y el seguimiento de pedidos para sostener la continuidad de la operación.],
      [Resolví fallas básicas de impresoras y equipos del sector para evitar cortes en la operación.],
    ),
  ),
  (
    title: "Bon Air Cafetería",
    subtitle: "Encargado Administrativo",
    dates: "Nov 2024 – Sep 2025",
    bullets: (
      [Administré ventas, inventario y cierres de caja con el sistema FUDO POS.],
      [Resolví incidencias del sistema para evitar interrupciones en la operación.],
      [Reemplacé el registro manual de ventas, stock y cierres de caja por planillas digitales con fórmulas y validaciones, y quedó como el circuito diario del local.],
    ),
  ),
  (
    title: "Havanna",
    subtitle: "Soporte Operativo",
    dates: "Feb 2024 – Jul 2024",
    bullets: (
      [Operé el sistema MAXIREST para el control de la operación y la validación de información.],
      [Brindé asistencia técnica básica a las computadoras de los mozos y colaboré con la continuidad del servicio.],
    ),
  ),
)

// --- Proyectos ------------------------------------------------------------
// Mismas claves que experiencia + link-url / link-label para la demo pública.
#let proyectos = (
  av: (
    title: "AVENOR",
    subtitle: "Plataforma SaaS de automatización para comercios · Proyecto personal",
    dates: "2025 – presente",
    link-url: "https://avenor-software.web.app/",
    bullets: (
      [Desarrollé una plataforma SaaS para automatizar procesos comerciales, administrativos y operativos de comercios: pedidos, inventario y tareas repetitivas.],
      [Implementé el back-end con FastAPI y PostgreSQL —lógica de negocio, modelo de datos e integración de servicios— y el front-end con Next.js.],
      [Stack: Python, FastAPI, PostgreSQL, Docker, JavaScript, Next.js y Playwright.],
    ),
  ),
  fleetops: (
    title: "FleetOps Logistics",
    subtitle: "Centro de control logístico con mapa de Buenos Aires · Proyecto personal",
    dates: "2026",
    link-url: "https://fleetops-logistics.vercel.app",
    bullets: (
      [Desarrollé un centro de control con mapa real de la Ciudad de Buenos Aires: cinco camiones recorriendo rutas calculadas con OSRM, con panel de vehículo, KPIs y paradas en vivo.],
      [Separé la animación del estado de React: un único requestAnimationFrame publica posiciones a 60 fps para el mapa y una instantánea a ~9 fps para la interfaz, sin re-renderizar el panel en cada frame.],
      [Stack: Next.js 15, React 19, TypeScript, MapLibre GL JS y Playwright (pruebas E2E).],
    ),
  ),
  stock: (
    title: "Sistema de Stock Automatizado",
    subtitle: "Proyecto académico UADE · Cafetería",
    dates: "2025",
    bullets: (
      [Desarrollé una aplicación de gestión de inventarios en Python a partir de necesidades operativas del sector gastronómico.],
      [Implementé estructuras de datos y lógica de negocio para administrar productos, clientes y ventas, con registro automático de movimientos y reportes de control.],
    ),
  ),
  chiazza: (
    title: "Chocolates Chiazza",
    subtitle: "Análisis y diseño de gestión de stock · Proyecto integrador UADE",
    dates: "2025",
    bullets: (
      [Analicé el control manual de materias primas y armé el diagnóstico organizacional (FODA) del proceso.],
      [Relevé requerimientos y diseñé la propuesta de sistema (compras, consumos e inventario), con reportes y alertas de reposición por WhatsApp o Telegram. Alcance académico: diseño, sin implementación.],
    ),
  ),
)

// --- Educación ------------------------------------------------------------
// Campos: title, subtitle, dates, note.
#let educacion = (
  (
    title: "Tecnicatura Universitaria en Desarrollo de Software",
    subtitle: "UADE",
    dates: "2025 – 2028 (en curso)",
    note: "Graduación estimada: fines de 2028.",
  ),
  (
    title: "Inglés técnico",
    subtitle: "Clases particulares",
    dates: none,
    note: "Lectura de documentación y vocabulario técnico.",
  ),
  (
    title: "Fundamentos de Ciberseguridad",
    subtitle: "Curso certificado",
    dates: "Ago 2026",
    note: "48.5 h.",
  ),
)
