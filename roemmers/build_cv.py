#!/usr/bin/env python3
"""Genera los dos CV para Roemmers en PDF (Typst) y DOCX (python-docx).

Los datos salen de data_es.typ. No agregar tecnologías, métricas ni
responsabilidades que no estén en el CV original.
"""
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

OUT = Path(__file__).resolve().parent

NAME = "Facundo Octavio Mello"
LOCATION = "Castelar, Buenos Aires"
PHONE = "(+54) 9 11 2408 4431"
EMAIL = "facundomello34@gmail.com"
GITHUB = "github.com/facundomello34-byte"
PORTFOLIO = "avenor-software.web.app"
LINKEDIN = "linkedin.com/in/facundo-octavio-mello-ferreira-8a4206265"

PROFILE_TECH = (
    "Estudiante de la Tecnicatura Universitaria en Desarrollo de Software en UADE "
    "(promedio 8.67) con experiencia operativa en sistemas de gestión, resolución de "
    "incidencias de primera línea y automatización de tareas. Busco una pasantía o "
    "posición junior en soporte técnico, QA, análisis funcional o automatización. "
    "Uso Linux a diario y trabajo con Python, SQL, Git y Docker. Inglés técnico en "
    "curso (clases particulares), orientado a lectura de documentación."
)

SKILLS_TECH = [
    ("Soporte IT", "Windows, Linux (uso diario), hardware, impresoras, redes Wi-Fi, PDA, sistemas POS, emisión y seguimiento de tickets, atención de usuarios."),
    ("Desarrollo y datos", "Python, JavaScript, HTML/CSS, FastAPI, Next.js, SQL, PostgreSQL."),
    ("QA y análisis", "pruebas E2E, validación de datos, relevamiento de requerimientos, documentación técnica, mejora de procesos."),
    ("Herramientas", "Git/GitHub, Docker, Playwright, bash."),
    ("Idiomas", "español nativo; inglés técnico en curso (clases particulares), lectura de documentación."),
]

PROFILE_ADMIN = (
    "Estudiante de la Tecnicatura Universitaria en Desarrollo de Software en UADE "
    "(promedio 8.67) con experiencia en administración de locales, control de stock, "
    "cierres de caja y uso de sistemas de gestión (FUDO POS, MAXIREST). Busco una "
    "pasantía en administración, operaciones, logística o gestión de información donde "
    "pueda aportar orden, validación de datos y automatización de tareas. Manejo "
    "herramientas digitales y tengo formación en Python y SQL."
)

SKILLS_ADMIN = [
    ("Administración y operaciones", "control de stock e inventarios, cierres de caja, registro y validación de datos, seguimiento de pedidos, atención de incidencias."),
    ("Sistemas", "FUDO POS, MAXIREST, PDA, sistemas internos, Windows."),
    ("Datos y automatización", "Python, SQL, PostgreSQL, Git/GitHub; automatización de reportes y tareas repetitivas."),
    ("Competencias", "organización, atención al detalle, trabajo en equipo, resolución de problemas, aprendizaje rápido."),
    ("Idiomas", "español nativo; inglés técnico (lectura de documentación), en formación."),
]

EXPERIENCE = [
    {
        "role": "Operador",
        "company": "COTO Digital (COTO CICSA)",
        "dates": "Oct 2025 – presente",
        "tech": [
            "Operación diaria con PDA y sistemas internos: impresión y control de vouchers, emisión de tickets y seguimiento de pedidos.",
            "Resolución autónoma de fallas básicas de impresoras y equipos para sostener la continuidad del sector.",
            "Detección de tareas repetitivas y optimización del uso de las herramientas disponibles.",
        ],
        "admin": [
            "Emisión de tickets, seguimiento de pedidos y control de vouchers con PDA y sistemas internos.",
            "Resolución de incidencias técnicas básicas para sostener la continuidad de la operación.",
            "Optimización de tareas repetitivas mediante el uso eficiente de las herramientas disponibles.",
        ],
    },
    {
        "role": "Encargado Administrativo",
        "company": "Bon Air Cafetería",
        "dates": "Nov 2024 – Sep 2025",
        "tech": [
            "Administración integral del local con el sistema de gestión FUDO POS: ventas, stock y cierres de caja.",
            "Resolución de incidencias del sistema para evitar interrupciones en la operación.",
            "Implementación de soluciones digitales para automatizar el registro de ventas, el control de stock y los cierres diarios.",
        ],
        "admin": [
            "Administración integral del local: ventas, control de stock y cierres de caja con FUDO POS.",
            "Implementación de soluciones digitales para automatizar el registro de ventas, el stock y los cierres diarios.",
            "Validación y registro de datos operativos; resolución de incidencias del sistema.",
        ],
    },
    {
        "role": "Soporte Operativo",
        "company": "Havanna",
        "dates": "Feb 2024 – Jul 2024",
        "tech": [
            "Manejo y soporte de los sistemas internos de la operación con el software MAXIREST.",
            "Validación de información y soporte técnico a las computadoras de los mozos.",
            "Responsable de caja y del correcto funcionamiento del sector.",
        ],
        "admin": [
            "Manejo y control de los sistemas internos de la operación con MAXIREST.",
            "Validación de información y soporte a las computadoras de los mozos.",
            "Responsable de caja y del funcionamiento del sector.",
        ],
    },
]

PROJECTS_TECH = [
    {
        "role": "AVENOR · Plataforma SaaS de automatización para comercios",
        "company": "Proyecto personal",
        "dates": "2025 – presente",
        "bullets": [
            "Desarrollo de un prototipo funcional de plataforma SaaS para automatizar procesos comerciales, administrativos y operativos.",
            "Implementación de lógica de negocio, gestión de información en PostgreSQL e integración de servicios con FastAPI; funcionalidades de pedidos, inventarios y automatización.",
            "Stack: Python, FastAPI, PostgreSQL, Docker, JavaScript, Next.js y Playwright. Proyecto en desarrollo, con estrategia de testing y despliegue productivo pendientes.",
        ],
    },
    {
        "role": "Sistema de Stock Automatizado",
        "company": "Proyecto académico UADE · Cafetería",
        "dates": "2025",
        "bullets": [
            "Desarrollo de una aplicación de gestión de inventarios en Python, basada en necesidades operativas del sector gastronómico.",
            "Implementación de estructuras de datos, funciones y lógica de negocio para administrar productos, clientes y ventas.",
            "Automatización del registro de movimientos de stock y generación de reportes para el control de inventarios.",
        ],
    },
    {
        "role": "Chocolates Chiazza · Análisis y diseño de un sistema de gestión de stock",
        "company": "Proyecto integrador UADE",
        "dates": "",
        "bullets": [
            "Análisis de procesos empresariales y diagnóstico organizacional (FODA) sobre el control manual de materias primas.",
            "Diseño de una propuesta de sistema de información para centralizar compras, consumos e inventarios, con requerimientos funcionales, seguridad mínima, reportes y alertas de reposición por WhatsApp o Telegram.",
            "Proyecto académico de análisis y propuesta de mejora; no fue un sistema implementado ni desplegado en la empresa.",
        ],
    },
]

PROJECTS_ADMIN = [
    {
        "role": "Sistema de Stock Automatizado",
        "company": "Proyecto UADE",
        "dates": "2025",
        "bullets": [
            "Backend en Python para la gestión de stock de una cafetería: productos, clientes, ventas, reportes y automatización de inventario.",
        ],
    },
    {
        "role": "AVENOR · Plataforma SaaS de automatización para comercios",
        "company": "Proyecto propio",
        "dates": "2025 – presente",
        "bullets": [
            "Desarrollo de un SaaS para automatizar procesos administrativos de comercios con Python, FastAPI, PostgreSQL, Docker y Playwright.",
            "Automatización de tareas, integración de servicios y pruebas E2E.",
        ],
    },
]

EDUCATION = [
    {
        "role": "Tecnicatura Universitaria en Desarrollo de Software",
        "company": "UADE",
        "dates": "2025 – 2028 (en curso)",
        "detail": "Promedio 8.67.",
    },
    {
        "role": "Inglés técnico",
        "company": "Clases particulares",
        "dates": "2026 – en curso",
        "detail": "Lectura de documentación y vocabulario técnico.",
    },
    {
        "role": "Fundamentos de Ciberseguridad",
        "company": "Curso certificado",
        "dates": "Ago 2026",
        "detail": "48.5 h.",
    },
]

AVAILABILITY = (
    "Disponibilidad: inmediata, coordinable con mi empleador actual · "
    "Presencial, híbrida o remota · Castelar, Buenos Aires."
)

CVS = {
    "tech": {
        "file": "cv_roemmers_tech",
        "headline": "Estudiante de Desarrollo de Software · Soporte IT / QA / Análisis Funcional",
        "profile": PROFILE_TECH,
        "skills": SKILLS_TECH,
        "experience_key": "tech",
        "projects": PROJECTS_TECH,
    },
    "admin": {
        "file": "cv_roemmers_admin",
        "headline": "Estudiante de Desarrollo de Software · Pasantías en Administración, Operaciones y Gestión de Información",
        "profile": PROFILE_ADMIN,
        "skills": SKILLS_ADMIN,
        "experience_key": "admin",
        "projects": PROJECTS_ADMIN,
    },
}


def esc_typ(s: str) -> str:
    """Escapa caracteres con significado en Typst."""
    out = []
    for ch in s:
        if ch in "\\#$@%&_*[]<>~`":
            out.append("\\" + ch)
        else:
            out.append(ch)
    return "".join(out)


def typst_cv(spec: dict) -> str:
    def bullets(items):
        inner = ",\n".join(f"  [{esc_typ(i)}]" for i in items)
        return f"#list(\n{inner},\n)"

    exp = []
    for job in EXPERIENCE:
        exp.append(
            f"#job([{esc_typ(job['role'])}], [{esc_typ(job['company'])}], [{esc_typ(job['dates'])}])\n"
            + bullets(job[spec["experience_key"]])
        )

    proj = []
    for p in spec["projects"]:
        proj.append(
            f"#job([{esc_typ(p['role'])}], [{esc_typ(p['company'])}], [{esc_typ(p['dates'])}])\n"
            + bullets(p["bullets"])
        )

    edu = []
    for e in EDUCATION:
        edu.append(
            f"#job([{esc_typ(e['role'])}], [{esc_typ(e['company'])}], [{esc_typ(e['dates'])}])\n"
            f"#text(size: 8.8pt)[{esc_typ(e['detail'])}]"
        )

    skills = "\n#linebreak()\n".join(
        f"#text(weight: \"bold\")[{esc_typ(k)}:] {esc_typ(v)}"
        for k, v in spec["skills"]
    )

    return f"""#set page(paper: "a4", margin: (x: 1.55cm, y: 1.25cm))
#set text(font: ("Liberation Sans", "DejaVu Sans"), size: 9.8pt, lang: "es", hyphenate: false)
#set par(justify: false, leading: 0.5em, spacing: 0.55em)
#set list(indent: 0.32em, body-indent: 0.26em, spacing: 0.22em)

#let section(title, body) = {{
  v(0.5em)
  text(size: 10.2pt, weight: "bold", tracking: 0.06em)[#upper(title)]
  v(-0.42em)
  line(length: 100%, stroke: 0.5pt)
  v(0.1em)
  body
}}

#let job(role, company, dates) = block(width: 100%)[
  #text(weight: "bold")[#role] · #company #h(1fr) #text(size: 8.5pt)[#dates]
]

#align(center)[
  #text(size: 18pt, weight: "bold", tracking: 0.02em)[FACUNDO OCTAVIO MELLO]
  #v(-0.25em)
  #text(size: 9.8pt)[{esc_typ(spec['headline'])}]
  #v(-0.2em)
  #text(size: 8.6pt)[{esc_typ(LOCATION)} · {esc_typ(PHONE)} · {esc_typ(EMAIL)}]
  #linebreak()
  #text(size: 8.6pt)[#link("https://www.{LINKEDIN}")[{LINKEDIN}]]
  #linebreak()
  #text(size: 8.6pt)[#link("https://{GITHUB}")[{GITHUB}] · #link("https://{PORTFOLIO}/")[{PORTFOLIO}]]
]

#section("Perfil")[
  {esc_typ(spec['profile'])}
]

#section("Competencias")[
{skills}
]

#section("Experiencia")[
{chr(10).join(exp)}
]

#section("Proyectos")[
{chr(10).join(proj)}
]

#section("Educación")[
{chr(10).join(edu)}
]

#v(0.45em)
#text(size: 8.6pt)[{esc_typ(AVAILABILITY)}]
"""


def add_bottom_border(paragraph):
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "4")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "999999")
    pBdr.append(bottom)
    pPr.append(pBdr)


def docx_cv(spec: dict) -> Document:
    doc = Document()
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(1.15)
    section.bottom_margin = Cm(1.1)
    section.left_margin = Cm(1.5)
    section.right_margin = Cm(1.5)

    style = doc.styles["Normal"]
    style.font.name = "Arial"
    style.font.size = Pt(9.7)
    style.element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
    style.paragraph_format.space_after = Pt(1.5)
    style.paragraph_format.space_before = Pt(0)
    style.paragraph_format.line_spacing = 1.0

    def para(text="", size=9.7, bold=False, align=None, space_after=1.5, space_before=0):
        p = doc.add_paragraph()
        if align is not None:
            p.alignment = align
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.line_spacing = 1.0
        if text:
            r = p.add_run(text)
            r.font.name = "Arial"
            r.font.size = Pt(size)
            r.bold = bold
        return p

    def heading(title):
        p = para(title.upper(), size=10.2, bold=True, space_before=6, space_after=1.5)
        add_bottom_border(p)

    def bullet(text):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(0.38)
        p.paragraph_format.first_line_indent = Cm(-0.38)
        p.paragraph_format.space_after = Pt(1.0)
        p.paragraph_format.line_spacing = 1.0
        r = p.add_run("•  " + text)
        r.font.name = "Arial"
        r.font.size = Pt(9.7)

    def job(role, company, dates):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(0.8)
        p.paragraph_format.line_spacing = 1.0
        r1 = p.add_run(role)
        r1.bold = True
        r1.font.name = "Arial"
        r1.font.size = Pt(9.4)
        r2 = p.add_run(" · " + company + "   ")
        r2.font.name = "Arial"
        r2.font.size = Pt(9.7)
        tab_stops = p.paragraph_format.tab_stops
        tab_stops.add_tab_stop(Cm(18.0), alignment=2)  # right
        r3 = p.add_run("\t" + dates)
        r3.font.name = "Arial"
        r3.font.size = Pt(8.5)
        r3.font.color.rgb = RGBColor(0x44, 0x44, 0x44)

    para(NAME, size=18, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=1)
    para(spec["headline"], size=9.8, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0.5)
    para(f"{LOCATION} · {PHONE} · {EMAIL}", size=8.6, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)
    para(LINKEDIN, size=8.6, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)
    para(f"{GITHUB} · {PORTFOLIO}", size=8.6, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)

    heading("Perfil")
    para(spec["profile"], space_after=2)

    heading("Competencias")
    for k, v in spec["skills"]:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(1.0)
        p.paragraph_format.line_spacing = 1.0
        r1 = p.add_run(k + ": ")
        r1.bold = True
        r1.font.name = "Arial"
        r1.font.size = Pt(9.7)
        r2 = p.add_run(v)
        r2.font.name = "Arial"
        r2.font.size = Pt(9.7)

    heading("Experiencia")
    for job_data in EXPERIENCE:
        job(job_data["role"], job_data["company"], job_data["dates"])
        for b in job_data[spec["experience_key"]]:
            bullet(b)

    heading("Proyectos")
    for p in spec["projects"]:
        job(p["role"], p["company"], p["dates"])
        for b in p["bullets"]:
            bullet(b)

    heading("Educación")
    for e in EDUCATION:
        job(e["role"], e["company"], e["dates"])
        para(e["detail"], size=8.8, space_after=1.0)

    p = para(AVAILABILITY, size=8.6, space_before=4, space_after=0)
    p.paragraph_format.line_spacing = 1.0

    return doc


def text_version(spec: dict) -> str:
    def line(role, company, dates):
        base = f"{role} · {company}"
        return f"{base} | {dates}" if dates else base

    lines = [
        NAME,
        spec["headline"],
        f"{LOCATION} · {PHONE} · {EMAIL}",
        LINKEDIN,
        f"{GITHUB} · {PORTFOLIO}",
        "",
        "PERFIL",
        spec["profile"],
        "",
        "COMPETENCIAS",
    ]
    for k, v in spec["skills"]:
        lines.append(f"{k}: {v}")
    lines += ["", "EXPERIENCIA"]
    for job_data in EXPERIENCE:
        lines.append(line(job_data["role"], job_data["company"], job_data["dates"]))
        lines += [f"- {b}" for b in job_data[spec["experience_key"]]]
    lines += ["", "PROYECTOS"]
    for p in spec["projects"]:
        lines.append(line(p["role"], p["company"], p["dates"]))
        lines += [f"- {b}" for b in p["bullets"]]
    lines += ["", "EDUCACIÓN"]
    for e in EDUCATION:
        lines.append(line(e["role"], e["company"], e["dates"]))
        lines.append(e["detail"])
    lines += ["", AVAILABILITY, ""]
    return "\n".join(lines)


def main():
    for key, spec in CVS.items():
        typ_path = OUT / f"{spec['file']}.typ"
        typ_path.write_text(typst_cv(spec), encoding="utf-8")
        docx_path = OUT / f"{spec['file']}.docx"
        docx_cv(spec).save(docx_path)
        print("generado:", typ_path.name, docx_path.name)

    (OUT / "cv_roemmers_texto.md").write_text(
        "# CV A — Tecnología / Soporte IT / QA\n\n```text\n"
        + text_version(CVS["tech"])
        + "```\n\n# CV B — Pasantías / Administración / Operaciones\n\n```text\n"
        + text_version(CVS["admin"])
        + "```\n",
        encoding="utf-8",
    )
    print("generado: cv_roemmers_texto.md")


if __name__ == "__main__":
    main()
