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

// Sin titular a propósito: Facundo no quiere cerrarse a un rol. Una variante
// dirigida a un aviso puntual puede pasar `headline:` a `cv.with(...)`.
#let headline = none

#let contacto = "Castelar, Buenos Aires · (+54) 9 11 2408 4431 · facundomello34@gmail.com"
#let links = (
  ("LinkedIn", "https://www.linkedin.com/in/facundo-octavio-mello-ferreira-8a4206265"),
  ("GitHub", "https://github.com/facundomello34-byte"),
)

// --- Perfil ---------------------------------------------------------------
// Dos frases: qué estudia, qué maneja. Sin promedio y sin decir qué busca.
#let perfil = [
  Estudiante de Desarrollo de Software en UADE con experiencia en sistemas de
  gestión, soporte de primera línea y automatización de tareas. Manejo Python,
  SQL, PostgreSQL, Linux y Git, y tengo dos aplicaciones propias desplegadas con
  Next.js, React y TypeScript.
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
// Solo los desplegados. `title-link` convierte el título en el enlace.
#let proyectos = (
  av: (
    title: "AVENOR",
    subtitle: "Plataforma SaaS de automatización para comercios",
    dates: "2025 – presente",
    title-link: "https://avenor-software.web.app/",
    bullets: (
      [Desarrollé el back-end en FastAPI y PostgreSQL (pedidos, inventario y lógica de negocio) y el front en Next.js.],
      [Automaticé tareas repetitivas del local, con Docker para el entorno y Playwright para pruebas E2E.],
    ),
  ),
  fleetops: (
    title: "FleetOps Logistics",
    subtitle: "Centro de control logístico con mapa de Buenos Aires",
    dates: "2026",
    title-link: "https://fleetops-logistics.vercel.app",
    bullets: (
      [Centro de control con mapa real de CABA: cinco camiones sobre rutas OSRM y KPIs en vivo.],
      [Separé la animación del ciclo de render en React: mapa fluido con MapLibre, sin recalcular la interfaz.],
    ),
  ),
)

// --- Educación ------------------------------------------------------------
// Campos: title, subtitle, dates, link-url, link-label, note.
#let educacion = (
  (
    title: "Tecnicatura Universitaria en Desarrollo de Software",
    subtitle: "UADE",
    dates: "2025 – 2028 (en curso)",
    note: "Promedio 8.67.",
  ),
  (
    title: "Inglés técnico",
    note: "Lectura de documentación y vocabulario técnico.",
  ),
  (
    title: "Fundamentos de Ciberseguridad",
    subtitle: "Santander Open Academy · contenido de IBM",
    dates: "Ago 2026",
    link-url: "https://facundomello34-byte.github.io/CV-Automation-Typst-GitHub-Actions/certificados/ciberseguridad-santander-open-academy.pdf",
    link-label: "certificado",
    note: "1.5 h · N.º de serie OA-2026-0814003065713.",
  ),
)
