#!/usr/bin/env python3
"""CV principal de Facundo Mello, rediseñado.

Genera:
  - cv_master.typ  (Typst)
  - cv_master.docx (Word editable)

La versión final se compila a PDF con Typst y se copia como
Mello_Facundo_CV_IT.pdf / .docx.

No agregar experiencia, tecnologías ni resultados que no estén en el CV
original o en los proyectos confirmados por Facundo.
"""
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

OUT = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# Datos
# ---------------------------------------------------------------------------

NAME = "Facundo Octavio Mello"
HEADLINE = "Estudiante de Desarrollo de Software · Soporte IT · QA · Análisis Funcional"
LOCATION = "Castelar, Buenos Aires"
PHONE = "(+54) 9 11 2408 4431"
EMAIL = "facundomello34@gmail.com"
LINKS = [
    ("LinkedIn", "https://www.linkedin.com/in/facundo-octavio-mello-ferreira-8a4206265"),
    ("GitHub", "https://github.com/facundomello34-byte"),
    ("AVENOR", "https://avenor-software.web.app/"),
]

PETROL = "17324D"
BLUE = "2563EB"
GRAY = "374151"
LIGHT = "E5E7EB"
MUTED = "6B7280"

PROFILE = (
    "Estudiante de Desarrollo de Software en UADE (promedio 8.67) con experiencia "
    "operativa en sistemas de gestión, resolución de incidencias y automatización de "
    "tareas. Manejo Python, SQL, Linux, Git y Docker, y desarrollo un SaaS propio con "
    "FastAPI, PostgreSQL y Playwright. Busco una posición Trainee, Junior o pasantía en "
    "desarrollo, soporte IT, QA, análisis funcional o automatización. Inglés técnico en "
    "curso con clases particulares."
)

SKILLS = [
    ("Desarrollo y bases de datos", "Python, JavaScript, HTML/CSS, FastAPI, Next.js, SQL, PostgreSQL."),
    ("Soporte técnico y sistemas", "Windows, Linux (uso diario), hardware, impresoras, redes Wi-Fi, PDA, sistemas POS (FUDO, MAXIREST), resolución de incidencias."),
    ("QA, análisis y automatización", "Playwright, pruebas E2E, validación de datos, relevamiento de requerimientos, documentación técnica, mejora de procesos."),
    ("Herramientas y tecnologías", "Git/GitHub, Docker, bash, terminal/CLI."),
]

EXPERIENCE = [
    {
        "company": "COTO Digital (COTO CICSA)",
        "role": "Operador",
        "dates": "Oct 2025 – presente",
        "bullets": [
            "Operé PDA y sistemas internos para impresión y control de comprobantes. Gestioné tickets operativos y el seguimiento de pedidos para sostener la continuidad de la operación.",
            "Resolví fallas básicas de impresoras y equipos para sostener la continuidad del sector.",
            "Detecté tareas repetitivas y optimicé procesos con las herramientas disponibles.",
        ],
    },
    {
        "company": "Bon Air Cafetería",
        "role": "Encargado Administrativo",
        "dates": "Nov 2024 – Sep 2025",
        "bullets": [
            "Administré ventas, inventario y cierres de caja con el sistema FUDO POS.",
            "Resolví incidencias del sistema para evitar interrupciones en la operación.",
            "Implementé soluciones digitales para automatizar el registro de ventas, el control de stock y los cierres diarios.",
        ],
    },
    {
        "company": "Havanna",
        "role": "Soporte Operativo",
        "dates": "Feb 2024 – Jul 2024",
        "bullets": [
            "Operé el sistema MAXIREST para el control de la operación y la validación de información.",
            "Brindé asistencia técnica básica a las computadoras de los mozos y colaboré con la continuidad del servicio.",
            "Gestioné la caja y el funcionamiento del sector.",
        ],
    },
]

PROJECTS = [
    {
        "name": "AVENOR",
        "descriptor": "Plataforma SaaS de automatización para comercios · Proyecto personal",
        "dates": "2025 – presente",
        "bullets": [
            "Desarrollé un prototipo funcional de SaaS para automatizar procesos comerciales, administrativos y operativos.",
            "Implementé lógica de negocio, gestión de datos en PostgreSQL e integración de servicios con FastAPI, con módulos de pedidos, inventarios y automatización.",
            "Construí el prototipo con Python, FastAPI, PostgreSQL, Docker, JavaScript, Next.js y Playwright; quedan pendientes la estrategia de testing y el despliegue productivo.",
        ],
    },
    {
        "name": "Sistema de Stock Automatizado",
        "descriptor": "Proyecto académico UADE · Cafetería",
        "dates": "2025",
        "bullets": [
            "Desarrollé una aplicación de gestión de inventarios en Python a partir de necesidades operativas del sector gastronómico.",
            "Implementé estructuras de datos, funciones y lógica de negocio para administrar productos, clientes y ventas.",
            "Automaticé el registro de movimientos de stock y la generación de reportes para el control de inventario.",
        ],
    },
    {
        "name": "Chocolates Chiazza",
        "descriptor": "Análisis y diseño de un sistema de gestión de stock · Proyecto integrador UADE",
        "dates": "",
        "bullets": [
            "Analicé procesos y realicé un diagnóstico organizacional (FODA) sobre el control manual de materias primas.",
            "Relevé necesidades y definí requerimientos funcionales, niveles mínimos de seguridad, reportes y alertas de reposición por WhatsApp o Telegram.",
            "Diseñé una propuesta de sistema de información para centralizar compras, consumos e inventarios. Proyecto académico, no implementado ni desplegado en la empresa.",
        ],
    },
]

EDUCATION = [
    {
        "title": "Tecnicatura Universitaria en Desarrollo de Software",
        "subtitle": "UADE",
        "dates": "2025 – 2028 (en curso)",
        "detail": "Promedio 8.67 · Graduación estimada: fines de 2028.",
    },
    {
        "title": "Inglés técnico",
        "subtitle": "Clases particulares",
        "dates": "2026 – en curso",
        "detail": "Lectura de documentación y vocabulario técnico.",
    },
    {
        "title": "Fundamentos de Ciberseguridad",
        "subtitle": "Curso certificado",
        "dates": "Ago 2026",
        "detail": "48.5 h.",
    },
]

AVAILABILITY = (
    "Disponibilidad: inmediata, coordinable con mi empleador actual · "
    "Presencial, híbrida o remota · Castelar, Buenos Aires."
)


# ---------------------------------------------------------------------------
# Typst
# ---------------------------------------------------------------------------

def esc_typ(s: str) -> str:
    out = []
    for ch in s:
        if ch in "\\#$@%&_*[]<>~`":
            out.append("\\" + ch)
        else:
            out.append(ch)
    return "".join(out)


def typst() -> str:
    def bullets(items):
        inner = ",\n".join(f"    [{esc_typ(i)}]" for i in items)
        return f"  #list(\n{inner},\n  )"

    skills = "\n  #linebreak()\n".join(
        f"  #text(weight: \"bold\", fill: petrol)[{esc_typ(k)}:] {esc_typ(v)}"
        for k, v in SKILLS
    )

    exp = []
    for job in EXPERIENCE:
        exp.append(
            f"  #job([{esc_typ(job['company'])}], [{esc_typ(job['role'])}], [{esc_typ(job['dates'])}])\n"
            + bullets(job["bullets"])
        )

    proj = []
    for p in PROJECTS:
        proj.append(
            f"  #job([{esc_typ(p['name'])}], [{esc_typ(p['descriptor'])}], [{esc_typ(p['dates'])}])\n"
            + bullets(p["bullets"])
        )

    edu = []
    for e in EDUCATION:
        edu.append(
            f"  #job([{esc_typ(e['title'])}], [{esc_typ(e['subtitle'])}], [{esc_typ(e['dates'])}])\n"
            f"  #text(size: 8.7pt, fill: muted)[{esc_typ(e['detail'])}]"
        )

    links = " #text(fill: muted)[|] ".join(
        f"#link(\"{url}\")[#text(fill: blue)[{label}]]" for label, url in LINKS
    )

    return f"""#set document(title: "Facundo Octavio Mello · CV", author: "Facundo Octavio Mello")
#set page(paper: "a4", margin: (x: 1.5cm, y: 1.15cm))
#set text(font: ("Lato", "Liberation Sans"), size: 10.0pt, fill: rgb("#{GRAY}"), lang: "es", hyphenate: false)
#set par(justify: false, leading: 0.53em, spacing: 0.53em)
#set list(indent: 0.3em, body-indent: 0.25em, spacing: 0.22em, marker: text(fill: rgb("#{BLUE}"), size: 8.5pt)[•])

#let petrol = rgb("#{PETROL}")
#let blue = rgb("#{BLUE}")
#let gray = rgb("#{GRAY}")
#let light = rgb("#{LIGHT}")
#let muted = rgb("#{MUTED}")

#let section(title, body) = {{
  v(0.6em)
  text(size: 10.5pt, weight: "bold", fill: petrol, tracking: 0.08em)[#upper(title)]
  v(-0.42em)
  line(length: 100%, stroke: 0.5pt + light)
  v(0.18em)
  body
}}

#let job(title, subtitle, dates) = block(width: 100%)[
  #text(weight: "bold", fill: petrol)[#title] #text(fill: gray)[· #subtitle] #h(1fr) #text(size: 8.8pt, fill: muted)[#dates]
]

#align(center)[
  #text(size: 21pt, weight: "black", fill: petrol, tracking: 0.01em)[FACUNDO OCTAVIO MELLO]
  #v(-0.22em)
  #text(size: 10.4pt, weight: "medium", fill: gray)[{esc_typ(HEADLINE)}]
  #v(-0.16em)
  #text(size: 8.9pt, fill: gray)[{esc_typ(LOCATION)} · {esc_typ(PHONE)} · {esc_typ(EMAIL)}]
  #linebreak()
  #text(size: 8.9pt)[{links}]
]

#v(0.28em)
#line(length: 100%, stroke: 0.6pt + light)

#section("Perfil")[
  {esc_typ(PROFILE)}
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
#text(size: 8.7pt, fill: muted)[{esc_typ(AVAILABILITY)}]
"""


# ---------------------------------------------------------------------------
# DOCX
# ---------------------------------------------------------------------------

def set_run(run, size, color, bold=False, italic=False, spacing=None):
    run.font.name = "Lato"
    run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), "Lato")
    run.font.size = Pt(size)
    run.font.color.rgb = RGBColor.from_string(color)
    run.bold = bold
    run.italic = italic
    if spacing is not None:
        rPr = run._element.get_or_add_rPr()
        sp = OxmlElement("w:spacing")
        sp.set(qn("w:val"), str(spacing))
        rPr.append(sp)


def bottom_border(paragraph, color=LIGHT, size=6, space=1):
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(size))
    bottom.set(qn("w:space"), str(space))
    bottom.set(qn("w:color"), color)
    pBdr.append(bottom)
    pPr.append(pBdr)


def add_hyperlink(paragraph, url, text, color=BLUE, size=8.9):
    part = paragraph.part
    r_id = part.relate_to(url, RT.HYPERLINK, is_external=True)
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    rFonts = OxmlElement("w:rFonts")
    rFonts.set(qn("w:ascii"), "Lato")
    rFonts.set(qn("w:hAnsi"), "Lato")
    rFonts.set(qn("w:eastAsia"), "Lato")
    rPr.append(rFonts)
    c = OxmlElement("w:color")
    c.set(qn("w:val"), color)
    rPr.append(c)
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), str(int(size * 2)))
    rPr.append(sz)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "none")
    rPr.append(u)
    run.append(rPr)
    t = OxmlElement("w:t")
    t.text = text
    run.append(t)
    hyperlink.append(run)
    paragraph._p.append(hyperlink)


def docx() -> Document:
    doc = Document()
    sec = doc.sections[0]
    sec.page_width = Cm(21.0)
    sec.page_height = Cm(29.7)
    sec.top_margin = Cm(1.1)
    sec.bottom_margin = Cm(1.0)
    sec.left_margin = Cm(1.5)
    sec.right_margin = Cm(1.5)

    cp = doc.core_properties
    cp.title = "Facundo Octavio Mello · CV"
    cp.author = "Facundo Octavio Mello"
    cp.subject = "CV · Desarrollo de Software · Soporte IT · QA · Análisis Funcional"

    style = doc.styles["Normal"]
    style.font.name = "Lato"
    style.font.size = Pt(10.0)
    style.font.color.rgb = RGBColor.from_string(GRAY)
    style.element.rPr.rFonts.set(qn("w:eastAsia"), "Lato")
    style.paragraph_format.space_after = Pt(1.5)
    style.paragraph_format.space_before = Pt(0)
    style.paragraph_format.line_spacing = 1.0

    def para(text="", size=10.0, color=GRAY, bold=False, align=None,
             space_after=1.5, space_before=0):
        p = doc.add_paragraph()
        if align is not None:
            p.alignment = align
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.line_spacing = 1.0
        if text:
            r = p.add_run(text)
            set_run(r, size, color, bold=bold)
        return p

    def heading(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(1.5)
        p.paragraph_format.line_spacing = 1.0
        r = p.add_run(title.upper())
        set_run(r, 10.5, PETROL, bold=True, spacing=20)
        bottom_border(p, LIGHT, 6, 1)
        return p

    def job(title, subtitle, dates):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(0.8)
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.tab_stops.add_tab_stop(Cm(18.0), alignment=2)
        r1 = p.add_run(title)
        set_run(r1, 10.1, PETROL, bold=True)
        r2 = p.add_run(" · " + subtitle)
        set_run(r2, 10.0, GRAY)
        if dates:
            r3 = p.add_run("\t" + dates)
            set_run(r3, 8.8, MUTED)
        return p

    def bullet(text):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(0.38)
        p.paragraph_format.first_line_indent = Cm(-0.38)
        p.paragraph_format.space_after = Pt(1.0)
        p.paragraph_format.line_spacing = 1.0
        r1 = p.add_run("•  ")
        set_run(r1, 9.3, BLUE)
        r2 = p.add_run(text)
        set_run(r2, 10.0, GRAY)

    def detail(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(1.5)
        p.paragraph_format.line_spacing = 1.0
        r = p.add_run(text)
        set_run(r, 8.9, MUTED)

    para(NAME.upper(), size=21, color=PETROL, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=1)
    para(HEADLINE, size=10.6, color=GRAY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0.5)
    para(f"{LOCATION} · {PHONE} · {EMAIL}", size=9.0, color=GRAY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.0
    for i, (label, url) in enumerate(LINKS):
        if i:
            sep = p.add_run("  |  ")
            set_run(sep, 9.0, MUTED)
        add_hyperlink(p, url, label, BLUE, 9.0)
    bottom_border(p, LIGHT, 6, 4)

    heading("Perfil")
    para(PROFILE, space_after=2)

    heading("Competencias")
    for k, v in SKILLS:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(1.0)
        p.paragraph_format.line_spacing = 1.0
        r1 = p.add_run(k + ": ")
        set_run(r1, 10.0, PETROL, bold=True)
        r2 = p.add_run(v)
        set_run(r2, 10.0, GRAY)

    heading("Experiencia")
    for job_data in EXPERIENCE:
        job(job_data["company"], job_data["role"], job_data["dates"])
        for b in job_data["bullets"]:
            bullet(b)

    heading("Proyectos")
    for p_data in PROJECTS:
        job(p_data["name"], p_data["descriptor"], p_data["dates"])
        for b in p_data["bullets"]:
            bullet(b)

    heading("Educación")
    for e in EDUCATION:
        job(e["title"], e["subtitle"], e["dates"])
        detail(e["detail"])

    p = para(AVAILABILITY, size=8.7, color=MUTED, space_before=4, space_after=0)
    p.paragraph_format.line_spacing = 1.0

    return doc


def main():
    (OUT / "cv_master.typ").write_text(typst(), encoding="utf-8")
    docx().save(OUT / "cv_master.docx")
    print("generado: cv_master.typ")
    print("generado: cv_master.docx")


if __name__ == "__main__":
    main()
