# Mi CV — Facundo Octavio Mello

CV generado con [Typst](https://typst.app/) a partir de la plantilla
[typst-cv](https://github.com/Mc-Zen/typst-cv) (adaptación propia).

Cada cambio se compila automáticamente con **GitHub Actions** y se publica en
**GitHub Pages**.

## 🚀 Arrancá por acá (reanudar sesión)

1. Leé [`estado-busqueda.md`](estado-busqueda.md) — estado de la búsqueda,
   checklist pendiente y banco de respuestas para formularios.
2. Revisá [`reports/jobs-latest.md`](reports/jobs-latest.md) — ofertas nuevas
   del día (lo actualiza un bot todos los días a las 08:15).
3. Postulá usando [`fuentes-empleo.md`](fuentes-empleo.md) (sección 0 = ofertas
   activas para postular hoy) y [`perfil-bumeran.md`](perfil-bumeran.md) (contenido
   listo para pegar en Bumeran).
4. Antes de escribir una carta, verificá el aviso con `/skill:evaluar-oferta`.
   Si ya hay entrevista agendada, `/skill:preparar-entrevista`.

## Estructura

| Archivo              | Para qué sirve                                |
| -------------------- | --------------------------------------------- |
| `diseno.typ`         | **La única interfaz**: tipografía, colores, márgenes y macros de sección. No se duplica. |
| `contenido.typ`      | **El contenido**: perfil, competencias, experiencia, proyectos, educación. Se edita acá. |
| `cv.typ`             | CV base: arma el documento completo. Es el archivo que se copia para una variante. |
| `AGENTS.md`          | Reglas para el agente (inglés): una sola interfaz, cómo hacer una variante, cómo verificar. |
| `data_es.typ`        | ⚠️ Legado: datos del CV serif publicado en Pages |
| `data_en.typ`        | ⚠️ Legado: datos del CV serif en inglés |
| `template.typ`       | ⚠️ Legado: plantilla serif original (typst-cv) |
| `cv_es.typ`          | ⚠️ Legado: genera `cv_es.pdf` (sitio en Pages) |
| `cv_en.typ`          | ⚠️ Legado: genera `cv_en.pdf` (sitio en Pages) |
| `carta_ey.typ`       | Carta de presentación específica para EY      |
| `carta_generica.typ` | Carta genérica ES (placeholders + 3 variantes según el puesto) |
| `carta_generica_en.typ` | Carta genérica EN (ofertas remotas)        |
| `perfil-bumeran.md`  | Contenido listo para copiar y pegar en Bumeran |
| `entrevistas/`       | One-pagers de entrevista, uno por empresa (skill `preparar-entrevista`) |
| `consultoras.md`    | Guía de consultoras IT: canales, programas trainee, vacantes vivas, emails reales |
| `fuentes-empleo.md`  | Fuentes: ofertas activas, portales, trainee programs, correos de contacto |
| `estado-busqueda.md` | Estado vivo de la búsqueda + checklist + respuestas para formularios |
| `reports/`           | Digest diario automático de ofertas de empleo |
| `scripts/jobs.sh`    | Script del digest diario de ofertas (LinkedIn + Exa) |
| `*.svg`              | Iconos (email, teléfono, GitHub, LinkedIn…)  |
| `.pi/voice.md`       | Perfil de voz de las cartas (leer antes de redactar) |
| `.pi/skills/humanizar-textos/` | Skill para limpiar y puntuar un texto antes de enviarlo |
| `.pi/skills/evaluar-oferta/` | Skill para verificar un aviso antes de gastar la carta (seniority, inglés, zona, postulantes) |
| `.pi/skills/preparar-entrevista/` | Skill para preparar una entrevista: relato, historias reales, gaps, inglés y one-pager |

## Búsqueda laboral automática

El workflow [`.github/workflows/jobs-daily.yml`](.github/workflows/jobs-daily.yml)
corre todos los días a las **08:15 (hora de Buenos Aires)**:

```bash
bash scripts/jobs.sh --days 7 --commit "🤖 Digest laboral $(date -u +%F)"
```

Genera `reports/jobs-latest.md` con ofertas junior (DevOps, Cloud, SRE, Soporte
IT) de LinkedIn y boards argentinos (Bumeran, Computrabajo, etc.). Otras
búsquedas (QA, trainee, dev) se hacen con la skill web-search en la sesión.

## Una sola interfaz

El CV tiene **un solo diseño**: el del CV "IT" del 11/11/2026 (Lato, azul
petróleo, una columna, sin foto). Vive entero en `diseno.typ`.

Antes había tres interfaces conviviendo —`template.typ` (serif), el master
Lato y los CV de Roemmers en sans 9,8pt sin color— y cada postulación nacía de
copiar un `.typ` y retocar el formato. Eso se terminó: ahora una variante es
**contenido + 10 líneas**, y si algo no entra o no se lee, se corrige una sola
vez en `diseno.typ`.

```bash
typst compile cv.typ                    # CV base → cv.pdf
pdfinfo cv.pdf | grep Pages            # tiene que decir "Pages: 1"
```

Para una variante: copiá las 10 líneas de ejemplo de `AGENTS.md`, sección
*Creating a tailored CV*, y cambiá solo `headline`, el párrafo de perfil, qué
proyectos entran y en qué orden.

Reglas de contenido que no se negocian:

- Un proyecto sin terminar o sin desplegar no entra.
- Ningún bullet cierra con lo que falta ("quedan pendientes el testing y el despliegue").
- Un dato no se repite en dos secciones.
- Inglés: "lectura de documentación", sin fechas y sin "en curso".

## Compilar en tu máquina

```bash
typst compile cv.typ      # CV base (diseño vigente)
typst compile cv_es.typ   # CV serif del sitio en Pages (legado)
typst compile cv_en.typ   # CV serif en inglés del sitio (legado)
```

O para ver el resultado en vivo:

```bash
typst watch cv.typ
```

## Publicar en tu GitHub

Ya tenés las claves SSH configuradas (`facundomello34-byte`), así que solo
falta crear el repo y pushear:

```bash
# 1) Creá el repo en GitHub (una vez): con la web o con gh:
gh repo create facundomello34-byte/cv --public --source . --push

# 2) (si el repo ya existe) agregalo y pusheá:
git remote add origin git@github.com:facundomello34-byte/cv.git
git push -u origin main
```

Después, una vez:

1. Entrá a **repo → Settings → Pages**.
2. En *Source* elegí **GitHub Actions** (el workflow ya está configurado).
3. Tu CV va a quedar en: `https://facundomello34-byte.github.io/cv/`

Cada `git push` a `main` recompila y actualiza la página automáticamente.

> Si querés que la URL sea más corta (`https://facundomello34-byte.github.io`),
> nombrá el repo `facundomello34-byte.github.io` en vez de `cv`.

---

## 🧰 Entorno de trabajo (actualizado 24/10/2026)

| Qué | Versión / estado |
| --- | --- |
| pi (agente) | **1.4.0** (era 0.84.3; desde 1.0 la TUI es *fullscreen* por defecto, `--tui-mode regular` la vuelve atrás) |
| Provider | `ollama-cloud` (único autenticado) |
| Modelo por defecto | `deepseek-v4.1-flash:1017` · 1M contexto, visión, $0.15/$0.60 por millón |
| Extensión de subagentes | `pi-subagents` (actualizada) |
| Skills del proyecto | `.pi/skills/humanizar-textos/` → `/skill:humanizar-textos`<br>`.pi/skills/evaluar-oferta/` → `/skill:evaluar-oferta`<br>`.pi/skills/preparar-entrevista/` → `/skill:preparar-entrevista` |
| Perfil de voz | `.pi/voice.md` |

Para volver a poner todo al día en el futuro:

```bash
pi update            # agente
pi update --extensions
pi --list-models
```
