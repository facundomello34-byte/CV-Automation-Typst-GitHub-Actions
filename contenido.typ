// =============================================================================
// contenido.typ — el contenido del CV, sin nada de diseño.
//
// Regla de redacción: un bullet = una línea, un logro concreto. La experiencia
// principal va primero y con dos bullets; lo secundario, con uno. Si un bullet
// no aporta evidencia, no va.
//
// Las variantes importan este archivo y eligen qué mostrar y en qué orden; no
// reescriben el texto ni tocan el formato.
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
// Tres frases: quién soy, qué manejo, qué busco.
#let perfil = [
  Estudiante de Desarrollo de Software en UADE (promedio 8.67) con experiencia en
  sistemas de gestión, soporte de primera línea y automatización de tareas. Manejo
  Python, SQL, PostgreSQL, Linux y Git; tengo dos aplicaciones propias desplegadas
  con Next.js, React y TypeScript. Busco mi primera posición Trainee o Junior en
  desarrollo, soporte IT o QA.
]

// --- Competencias ---------------------------------------------------------
#let competencias = (
  (
    "Desarrollo y datos",
    "Python, JavaScript, TypeScript, React, Next.js, FastAPI, SQL, PostgreSQL.",
  ),
  (
    "Soporte IT",
    "Windows, Linux, hardware, impresoras, redes, PDA, POS (FUDO, MAXIREST), tickets.",
  ),
  (
    "QA y automatización",
    "Playwright, pruebas E2E, validación de datos, relevamiento, documentación técnica.",
  ),
  (
    "Herramientas",
    "Git/GitHub, Docker, Vercel, bash.",
  ),
)

// --- Experiencia ----------------------------------------------------------
// La más relevante primero, dos bullets. Lo anterior, un bullet por puesto.
#let experiencia = (
  (
    title: "COTO Digital (COTO CICSA)",
    subtitle: "Operador",
    dates: "Oct 2025 – presente",
    bullets: (
      [Operé PDA y sistemas internos: comprobantes, tickets y seguimiento de pedidos.],
      [Resolví fallas de impresoras y equipos para sostener la continuidad del sector.],
    ),
  ),
  (
    title: "Bon Air Cafetería",
    subtitle: "Encargado Administrativo",
    dates: "Nov 2024 – Sep 2025",
    bullets: (
      [Administré ventas, stock y cierres de caja con FUDO POS, y resolví sus incidencias.],
      [Reemplacé el registro manual por planillas con fórmulas y validaciones.],
    ),
  ),
  (
    title: "Havanna",
    subtitle: "Soporte Operativo",
    dates: "Feb 2024 – Jul 2024",
    bullets: (
      [Operé MAXIREST y di asistencia técnica a las computadoras de los mozos.],
    ),
  ),
)

// --- Proyectos ------------------------------------------------------------
// Dos bullets para los desplegados, uno para los académicos.
#let proyectos = (
  av: (
    title: "AVENOR",
    subtitle: "SaaS de automatización para comercios · Proyecto personal",
    dates: "2025 – presente",
    link-url: "https://avenor-software.web.app/",
    bullets: (
      [Desarrollé un SaaS de pedidos e inventario para comercios: FastAPI y PostgreSQL en el back, Next.js en el front.],
      [Automaticé tareas repetitivas del local, con Docker para el entorno y Playwright para pruebas E2E.],
    ),
  ),
  fleetops: (
    title: "FleetOps Logistics",
    subtitle: "Centro de control logístico con mapa de Buenos Aires · Proyecto personal",
    dates: "2026",
    link-url: "https://fleetops-logistics.vercel.app",
    bullets: (
      [Centro de control con mapa real de CABA: cinco camiones sobre rutas OSRM y KPIs en vivo (Next.js, React, TypeScript, MapLibre).],
      [Saqué la animación del estado de React: 60 fps al mapa y ~9 fps a la interfaz, sin re-render del panel.],
    ),
  ),
  stock: (
    title: "Sistema de Stock Automatizado",
    subtitle: "Proyecto académico UADE · Cafetería",
    dates: "2025",
    bullets: (
      [App de inventario en Python: lógica de negocio, movimientos automáticos y reportes.],
    ),
  ),
  chiazza: (
    title: "Chocolates Chiazza",
    subtitle: "Análisis y diseño de gestión de stock · Proyecto integrador UADE",
    dates: "2025",
    bullets: (
      [Relevé requerimientos y diseñé un sistema de compras, consumos e inventario con alertas automáticas.],
    ),
    note: "Alcance académico: diseño, sin implementación.",
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
    subtitle: "Santander Open Academy · contenido de IBM",
    dates: "Ago 2026",
    link-url: "https://facundomello34-byte.github.io/cv/certificados/ciberseguridad-santander-open-academy.pdf",
    link-label: "certificado",
    note: "1.5 h · N.º de serie OA-2026-0814003065713.",
  ),
)
