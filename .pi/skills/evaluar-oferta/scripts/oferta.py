#!/usr/bin/env python3
"""
oferta.py — baja un aviso de empleo y devuelve la ficha + las señales que importan.

No puntúa ni decide: extrae datos y marca coincidencias para que las lea el
agente. El veredicto sale de SKILL.md, no de este script.

Uso:
    python3 oferta.py URL [URL ...]        # ficha legible
    python3 oferta.py URL --json           # todo en JSON
    python3 oferta.py URL --cuerpo         # solo el texto del aviso
    python3 oferta.py --archivo aviso.html # HTML o texto ya bajado
    cat aviso.txt | python3 oferta.py -

Fuentes:
    LinkedIn  → API guest /jobs-guest/jobs/api/jobPosting/<id> (sin login)
    Otras     → fetch directo. Si Cloudflare devuelve 403, usar la skill
                web-search: search.sh --url <URL>, o pegar el texto a mano.

Solo stdlib. Sin dependencias.
"""

import argparse
import html
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.request

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)
TIMEOUT = 25


# ── utilidades ────────────────────────────────────────────────────────────────

def norm(s: str) -> str:
    """Minúsculas, sin acentos, espacios colapsados. Para comparar."""
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s.lower()).strip()


def limpiar(s: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def html_a_texto(h: str) -> str:
    h = re.sub(r"(?is)<(script|style|noscript|svg|iframe)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?i)<br\s*/?>", "\n", h)
    h = re.sub(r"(?i)</(p|div|li|ul|ol|h[1-6]|tr|section|article|blockquote)>", "\n", h)
    h = re.sub(r"(?s)<[^>]+>", " ", h)
    h = html.unescape(h)
    h = h.replace("\xa0", " ")
    lineas = [re.sub(r"[ \t]+", " ", l).strip() for l in h.split("\n")]
    salida, vacias = [], 0
    for l in lineas:
        if l:
            salida.append(l)
            vacias = 0
        elif vacias < 1 and salida:
            salida.append("")
            vacias += 1
    return "\n".join(salida).strip()


class SinContenido(Exception):
    """La página cargó pero el aviso no está en el HTML (SPA / JS)."""


def fetch(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "es-AR,es;q=0.9,en;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        data = r.read()
        charset = r.headers.get_content_charset() or "utf-8"
    return data.decode(charset, errors="replace")


def clase(h: str, nombre: str, etiqueta: str = r"\w+") -> str:
    """Texto del primer elemento con esa clase (regex tolerante)."""
    m = re.search(
        rf'class="[^"]*\b{re.escape(nombre)}\b[^"]*"[^>]*>(.*?)</{etiqueta}>', h, re.S
    )
    return limpiar(m.group(1)) if m else ""


def criterio(criterios: dict, *claves: str) -> str:
    """LinkedIn localiza los títulos de los criterios; buscar por varias claves."""
    for k, v in criterios.items():
        if any(c in norm(k) for c in claves):
            return v
    return ""

# ── LinkedIn ─────────────────────────────────────────────────────────────────

def id_linkedin(url: str):
    m = re.search(r"(?:jobs/view/)?(\d{8,})", url)
    return m.group(1) if m else None


def es_linkedin(url: str) -> bool:
    return "linkedin.com" in url


def bajar_linkedin(job_id: str):
    url = f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}"
    h = fetch(url)
    titulo = clase(h, "topcard__title", "h2")
    empresa = clase(h, "topcard__org-name-link", "a") or clase(h, "topcard__flavor", "span")
    ubicacion = clase(h, "topcard__flavor--bullet", "span")
    publicado = clase(h, "posted-time-ago__text", "span")
    postulantes = clase(h, "num-applicants__caption", "span")

    criterios = {}
    for m in re.finditer(
        r'description__job-criteria-subheader"[^>]*>(.*?)</h3>.*?'
        r'description__job-criteria-text[^>]*>(.*?)</span>',
        h,
        re.S,
    ):
        criterios[limpiar(m.group(1))] = limpiar(m.group(2))

    cuerpo = ""
    m = re.search(
        r'class="[^"]*show-more-less-html__markup[^"]*"[^>]*>(.*?)'
        r'<button[^>]*show-more-less-html__button',
        h,
        re.S,
    )
    if m:
        cuerpo = html_a_texto(m.group(1))
    if not cuerpo:
        m = re.search(r'class="[^"]*description__text[^"]*"[^>]*>(.*?)</section>', h, re.S)
        if m:
            cuerpo = html_a_texto(m.group(1))

    return {
        "fuente": "linkedin",
        "url": f"https://www.linkedin.com/jobs/view/{job_id}",
        "titulo": titulo,
        "empresa": empresa,
        "ubicacion": ubicacion,
        "publicado": publicado,
        "postulantes": postulantes,
        "seniority_linkedin": criterio(criterios, "seniority", "antiguedad", "nivel"),
        "criterios": criterios,
        "texto": cuerpo,
    }


# ── genérico ────────────────────────────────────────────────────────────────

def bajar_generico(url: str):
    try:
        h = fetch(url)
    except urllib.error.HTTPError as e:
        cuerpo = e.read().decode("utf-8", errors="replace")
        if e.code in (403, 429) or "Just a moment" in cuerpo:
            raise PermissionError("Cloudflare")
        raise
    if "Just a moment" in h or "cf-browser-verification" in h:
        raise PermissionError("Cloudflare")
    t = re.search(r"(?is)<title[^>]*>(.*?)</title>", h)
    og = re.search(r'(?is)<meta[^>]+property="og:title"[^>]+content="([^"]*)"', h)
    sitio = re.search(r'(?is)<meta[^>]+property="og:site_name"[^>]+content="([^"]*)"', h)
    texto = html_a_texto(h)
    if len(texto) < 400:
        raise SinContenido(
            "la página cargó pero el aviso no está en el HTML: es una SPA que se "
            "arma con JavaScript (típico de Bumeran y Computrabajo)."
        )
    return {
        "fuente": "web",
        "url": url,
        "titulo": limpiar(og.group(1) if og else (t.group(1) if t else "")),
        "empresa": limpiar(sitio.group(1)) if sitio else "",
        "ubicacion": "",
        "publicado": "",
        "postulantes": "",
        "seniority_linkedin": "",
        "criterios": {},
        "texto": texto,
    }


# ── señales ─────────────────────────────────────────────────────────────────

INGLES = [
    (r"ingles (?:excluyente|indispensable|obligatorio)", "excluyente"),
    (r"ingles (?:intermedio|avanzado|fluido|conversacional|basico|tecnico)", "nivel"),
    (r"\b(?:b1|b2|c1|c2)\b", "marco comun"),
    (r"english (?:intermediate|advanced|fluent|proficient|bilingual)", "nivel"),
    (r"(?:fluent|advanced|proficient) (?:in )?english", "nivel"),
    (r"(?:entrevista|proceso|dia a dia|day[- ]to[- ]day)[^.\n]{0,40}ingles", "oral"),
    (r"ingles[^.\n]{0,20}(?:oral|hablado|conversacional)", "oral"),
    (r"(?:oral y escrito|spoken and written|written and spoken)", "oral+escrito"),
    (r"(?:escritas? y orales?|orales? y escritas?)", "oral+escrito"),
    (r"comunicacion(?:es)?[^.\n]{0,30}(?:orales?|spoken)", "oral"),
    (r"(?:leer|lectura|read)[^.\n]{0,30}(?:documentacion|documentation|docs)", "solo lectura"),
    (r"no (?:se requiere|hace falta) ingles|english (?:is )?not required", "no requiere"),
]

ANIOS = [
    (r"(\d+)\s*(?:a|-|–|al)\s*(\d+)\s*anos", "rango"),
    (r"(\d+)\s*(?:-|–|to)\s*(\d+)\s*years?", "rango"),
    (r"mas de (\d+)\s*anos", "minimo"),
    (r"(\d+)\s*\+?\s*anos (?:de )?(?:experiencia|trayectoria)", "minimo"),
    (r"(\d+)\+?\s*years? (?:of )?(?:experience|professional)", "minimo"),
    (r"sin experiencia|no se requiere experiencia|no experience (?:required|necessary)|no previa", "sin experiencia"),
]

SENIORITY = [
    (r"\b(?:trainee|pasante|pasantia|practicante|aprendiz|apprentice|internship|intern)\b", "entry"),
    (r"\b(?:junior|jr\.?|entry[- ]level|early[- ]career|primer empleo|recien recibido)\b", "entry"),
    (r"\bestudiantes?\b[^.\n]{0,45}\bavanzad[oa]s?\b", "avanzado-excluyente"),
    (r"\bavanzad[oa]s?\b[^.\n]{0,25}\b(?:carrera|estudios|universitari)", "avanzado-excluyente"),
    (r"\bproxim[oa]s?\s*(?:/as)?\s*a\s*(?:finalizar|recibirse|graduarse|egresar)", "avanzado-excluyente"),
    (r"\b(?:ultimo|ultimos)\s*(?:ano|anos)\b", "avanzado-excluyente"),
    (r"\bfinal[- ]year\b|\bgraduating\b|\babout to graduate\b", "avanzado-excluyente"),
    (r"\b(?:graduado|egresado|recibido)s?\b", "egresado-excluyente"),
    (r"\b(?:estudiante (?:en curso|regular|actual|activo|activa)|cursando|estudiante de)\b", "estudiante-en-curso"),
    (r"\bcarreras?\b[^.\n]{0,40}\ben curso\b", "estudiante-en-curso"),
    (r"\brecent(?:ly)? (?:graduate|graduated)\b", "entry"),
    (r"\b(?:semi[- ]?senior|ssr|senior|sr\.?|staff|principal|leader|lider|arquitecto|architect|head of)\b", "alto"),
]

MODALIDAD = [
    (r"\b(?:100\s*%\s*)?remoto\b|\bremote\b|\bteletrabajo\b", "remoto"),
    (r"\bhibrido\b|\bhybrid\b", "hibrido"),
    (r"\bpresencial\b|\bon[- ]?site\b|\boficina\b", "presencial"),
]

CIERRE = [
    (r"no longer accepting applications", "cerrada"),
    (r"ya no (?:acepta|recibe) (?:postulaciones|solicitudes)", "cerrada"),
    (r"aviso (?:cerrado|vencido)|busqueda cerrada", "cerrada"),
]

# riesgo de viaje desde Castelar (sin auto). Ver SKILL.md.
ZONAS = [
    ("casa", ["castelar", "moron", "haedo", "ituzaingo", "hurlingham", "ramos mejia", "san justo", "villa luzuriaga"]),
    ("alta", ["pilar", "escobar", "garin", "benavidez", "don torcuato", "tigre", "quilmes", "la plata",
              "berazategui", "ezeiza", "canning", "burzaco", "adrogue", "longchamps", "florencio varela",
              "san miguel", "jose c. paz", "jose paz"]),
    ("media", ["vicente lopez", "olivos", "martinez", "san isidro", "munro", "florida", "boulogne",
               "san martin", "caseros", "villa ballester", "merlo", "moreno", "la matanza",
               "lanus", "lomas de zamora", "avellaneda", "temperley", "wilde", "sarandi", "san fernando"]),
    ("baja", ["caba", "capital federal", "ciudad autonoma", "retiro", "once",
              "microcentro", "puerto madero", "chacarita", "belgrano", "nunez", "palermo",
              "caballito", "flores", "floresta", "liniers", "devoto", "villa crespo", "colegiales",
              "parque patricios", "barracas", "constitucion", "balvanera", "monserrat", "san telmo",
              "recoleta", "agronomia", "villa urquiza", "saavedra", "coghlan", "villa del parque",
              "paternal", "abasto", "parque centenario"]),
]


def buscar(patrones, texto_norm, maximo=4, excluir=None):
    """Devuelve [(etiqueta, fragmento)] únicos, con contexto.

    `excluir` descarta coincidencias cuyo entorno matchee ese regex (sirve para
    no marcar "senior" cuando el aviso dice "bajo supervisión de un senior").
    """
    salida, aceptados = [], []
    for patron, etiqueta in patrones:
        for m in re.finditer(patron, texto_norm):
            if any(a <= m.start() < b or a < m.end() <= b for a, b in aceptados):
                continue
            ini, fin = max(0, m.start() - 45), min(len(texto_norm), m.end() + 45)
            frag = texto_norm[ini:fin].strip()
            if excluir and re.search(excluir, frag):
                continue
            aceptados.append((m.start(), m.end()))
            salida.append((etiqueta, frag))
            if len(salida) >= maximo:
                return salida
    return salida


PALABRAS_ES = {"que", "de", "la", "el", "los", "las", "para", "con", "una", "por",
               "del", "se", "en", "es", "su", "al", "como", "mas", "pero", "sin"}
PALABRAS_EN = {"the", "and", "of", "to", "with", "you", "for", "will", "our", "your",
               "we", "are", "is", "in", "on", "as", "or", "be", "this", "that"}


def idioma(texto: str) -> str:
    """¿El aviso está en inglés? Importa: un aviso en inglés suele implicar leerlo."""
    palabras = re.findall(r"\b[a-z]{2,}\b", norm(texto))
    if len(palabras) < 20:
        return "?"
    es = sum(1 for p in palabras if p in PALABRAS_ES)
    en = sum(1 for p in palabras if p in PALABRAS_EN)
    total = es + en or 1
    if en / total > 0.65:
        return "ingles"
    if es / total > 0.65:
        return "espanol"
    return "mixto"


def dias_publicado(txt: str):
    t = norm(txt)
    if not t:
        return None
    if re.search(r"just now|hoy|recien publicado", t):
        return 0
    m = re.search(r"(\d+)\s*\+?\s*(minute|hour|day|week|month|year)s?\s*ago", t)
    if not m:
        m2 = re.search(r"hace\s*(?:un|una|\d+)\s*(minuto|hora|dia|semana|mes|ano)", t)
        if not m2:
            return None
        m = m2
        unidad = m.group(1)
        n = 1 if not re.search(r"\d+", t) else int(re.search(r"(\d+)", t).group(1))
    else:
        n, unidad = int(m.group(1)), m.group(2)
    factor = {"minute": 0, "hour": 0, "day": 1, "week": 7, "month": 30, "year": 365,
              "minuto": 0, "hora": 0, "dia": 1, "semana": 7, "mes": 30, "ano": 365}
    return n * factor.get(unidad, 0)


def cantidad_postulantes(txt: str):
    m = re.search(
        r"(\d[\d.,]*)\s*(?:applicants?|postulantes?|candidatos?|solicitudes|inscriptos|postulaciones)",
        norm(txt),
    )
    if not m:
        return None
    try:
        return int(re.sub(r"[.,]", "", m.group(1)))
    except ValueError:
        return None


def detectar_zona(texto: str):
    t = norm(texto)
    for riesgo, lugares in ZONAS:
        for lugar in lugares:
            if re.search(rf"\b{re.escape(lugar)}\b", t):
                return riesgo, lugar
    # "Buenos Aires" a secas puede ser CABA o provincia: no alcanza para decidir.
    if re.search(r"\b(?:buenos aires|gba|amba)\b", t):
        return "media", "buenos aires (ambiguo)"
    return "desconocida", ""


def evaluar(datos: dict):
    texto = datos.get("texto", "")
    completo = " ".join([datos.get("titulo", ""), datos.get("ubicacion", ""), texto])
    tn = norm(completo)

    modalidades = [e for e, _ in buscar(MODALIDAD, tn, maximo=6)]
    zona, lugar = detectar_zona(datos.get("ubicacion", "") + " " + texto)
    if "remoto" in modalidades:
        riesgo_zona = "no aplica (remoto)"
    else:
        riesgo_zona = zona

    return {
        **{k: v for k, v in datos.items() if k != "texto"},
        "dias_publicado": dias_publicado(datos.get("publicado", "")),
        "idioma_aviso": idioma(texto),
        "postulantes_n": cantidad_postulantes(
            f'{datos.get("postulantes", "")} {texto[:2000]}'
        ),
        "modalidad": modalidades,
        "zona": lugar,
        "zona_riesgo": riesgo_zona,
        "cerrada": bool(buscar(CIERRE, tn, maximo=1)),
        "senales": {
            "ingles": buscar(INGLES, tn),
            "anios": buscar(ANIOS, tn),
            "seniority": buscar(
                SENIORITY, tn, maximo=6,
                excluir=(
                    r"(?:senior|sr\.?)\s+(?:guidance|mentor|supervis|lead)"
                    r"|under (?:the )?(?:senior|supervision)"
                    r"|colaborar con|junto a (?:analistas|un senior|referentes)"
                    r"|global leader|leader in|world leader|lider en|referente del sector"
                ),
            ),
            "modalidad": buscar(MODALIDAD, tn),
            "cierre": buscar(CIERRE, tn, maximo=2),
        },
        "texto": texto,
    }


# ── salida ──────────────────────────────────────────────────────────────────

def ficha_md(d: dict) -> str:
    def linea(etiqueta, valor):
        return f"- **{etiqueta}**: {valor}" if valor not in (None, "", []) else None

    if d["zona_riesgo"].startswith("no aplica"):
        zona_txt = "remoto (sin viaje)"
    else:
        zona_txt = f'{d["zona"] or "no detectada"} → riesgo {d["zona_riesgo"]}'

    cab = [
        f'## {d["titulo"] or "(sin título)"}' + (f' — {d["empresa"]}' if d["empresa"] else ""),
        "",
        linea("URL", d["url"]),
        linea("Publicada", d["publicado"] + (f' (~{d["dias_publicado"]} días)' if d["dias_publicado"] is not None else "")),
        linea("Postulantes", d["postulantes_n"] if d["postulantes_n"] is not None else d["postulantes"]),
        linea("Ubicación", d["ubicacion"]),
        linea("Idioma del aviso", d["idioma_aviso"]),
        linea("Seniority (LinkedIn)", d["seniority_linkedin"]),
        linea("Modalidad", ", ".join(d["modalidad"])),
        linea("Zona", zona_txt),
        linea("Cerrada", "sí" if d["cerrada"] else None),
        "",
    ]
    cab = [l for l in cab if l is not None]

    sen = ["### Señales", ""]
    vacio = True
    for grupo, items in d["senales"].items():
        if items:
            vacio = False
            sen.append(f"**{grupo}**")
            for etiquieta, frag in items:
                sen.append(f'- `{etiquieta}` … {frag} …')
            sen.append("")
    if vacio:
        sen.append("_No se detectó ninguna señal. Leé la descripción completa: puede estar todo implícito._")
        sen.append("")

    return "\n".join(cab + sen + ["### Descripción", "", d["texto"] or "(vacía)", ""])


def main():
    p = argparse.ArgumentParser(description="Ficha y señales de un aviso de empleo.")
    p.add_argument("fuentes", nargs="*", help="URLs o - para stdin")
    p.add_argument("--archivo", help="HTML o texto ya bajado")
    p.add_argument("--json", action="store_true", help="salida JSON")
    p.add_argument("--cuerpo", action="store_true", help="solo el texto del aviso")
    a = p.parse_args()

    if not a.fuentes and not a.archivo:
        p.error("pasá al menos una URL, --archivo o -")

    resultados = []
    for f in a.fuentes or []:
        try:
            if f == "-":
                txt = sys.stdin.read()
                d = {"fuente": "stdin", "url": "", "titulo": "", "empresa": "", "ubicacion": "",
                     "publicado": "", "postulantes": "", "seniority_linkedin": "",
                     "criterios": {}, "texto": html_a_texto(txt)}
            elif es_linkedin(f):
                jid = id_linkedin(f)
                if not jid:
                    raise ValueError("no encontré el id del aviso en la URL de LinkedIn")
                d = bajar_linkedin(jid)
            else:
                d = bajar_generico(f)
            resultados.append(evaluar(d))
        except PermissionError:
            print(
                f"✗ {f}\n  Cloudflare bloqueó el fetch. Probá:\n"
                f"  ~/.pi/agent/skills/web-search/scripts/search.sh --url '{f}'\n"
                f"  o pegá el texto del aviso a mano.",
                file=sys.stderr,
            )
        except SinContenido as e:
            print(
                f"✗ {f}\n  {e}\n"
                f"  Probá search.sh --url '{f}' o pegá el texto del aviso a mano.",
                file=sys.stderr,
            )
        except (urllib.error.URLError, ValueError, TimeoutError) as e:
            print(f"✗ {f}\n  {e}", file=sys.stderr)

    if a.archivo:
        try:
            txt = open(a.archivo, encoding="utf-8", errors="replace").read()
            cuerpo = html_a_texto(txt)
            if len(cuerpo) < 400:
                raise SinContenido("el archivo no tiene texto de aviso (¿HTML de SPA o página de error?)")
            d = {"fuente": "archivo", "url": "", "titulo": "", "empresa": "", "ubicacion": "",
                 "publicado": "", "postulantes": "", "seniority_linkedin": "",
                 "criterios": {}, "texto": cuerpo}
            resultados.append(evaluar(d))
        except (OSError, SinContenido) as e:
            print(f"✗ {a.archivo}\n  {e}", file=sys.stderr)

    if not resultados:
        return 1

    if a.json:
        print(json.dumps(resultados if len(resultados) > 1 else resultados[0],
                         ensure_ascii=False, indent=2))
    elif a.cuerpo:
        print("\n\n".join(r["texto"] for r in resultados))
    else:
        print("\n\n---\n\n".join(ficha_md(r) for r in resultados))
    return 0


if __name__ == "__main__":
    sys.exit(main())
