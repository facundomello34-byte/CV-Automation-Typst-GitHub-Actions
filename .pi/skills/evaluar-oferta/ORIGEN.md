# Origen y decisiones

## Inspiración

El checklist de evaluación sale de dos skills públicas, ambas MIT, sin código
copiado:

- [`art2url/career-agent-skills`](https://github.com/art2url/career-agent-skills)
  → `skills/job-fit-analyzer/SKILL.md`
  commit `d7cce4b7eada07d08e094165aafbbb03a9928e58` (rama `develop`).
  De ahí salen la separación required/preferred, la tabla de gaps y la idea de
  que un filtro duro anula el puntaje.
- [`Paramchoudhary/ResumeSkills`](https://github.com/Paramchoudhary/ResumeSkills)
  → `.agents/skills/job-description-analyzer/SKILL.md`
  commit `74ae19e7c62b0516d1c298328e5544976c12da5d` (rama `main`).
  De ahí sale el orden de la ficha: requisitos, fortalezas, gaps, estrategia.

`scripts/oferta.py` es propio: usa solo la biblioteca estándar de Python, no
tiene dependencias y no ejecuta nada del upstream.

## Qué se adaptó y qué no

| Del upstream | Acá |
| --- | --- |
| Match score required 70% / preferred 30% | 60 / 25 / 15 (requisitos, stack, logística) |
| "90%+ = overqualified" | No aplica: para un primer empleo, sobrecalificado no es un riesgo |
| Red flags de cultura ("rockstar", "hustle") | Fuera: no son el cuello de botella de esta búsqueda |
| ATS, keywords, formato de CV | Fuera: el CV es Typst de una columna y los ATS de acá no son Workday |
| Cover letter, salary, LinkedIn optimizer | Fuera: ya hay `humanizar-textos` y el perfil está armado |

## Por qué los cinco filtros son esos

Salen de los errores documentados en `estado-busqueda.md`, no de una lista
genérica:

1. **Inglés** — 11 de 20 avisos del 11/11 lo pedían intermedio/avanzado.
2. **Seniority real** — el scoring por palabra clave puntuó alto COTO (calidad
   de alimentos), Stefanini (estudiante avanzado) y Accenture (2-4 años).
3. **Estudios** — "avanzado/egresado" es excluyente y va por el 2.º año de 4.
4. **Distancia** — Castelar sin auto: Pilar son 2 h por tramo, Vicente López
   1 h 20.
5. **Vigencia** — había una carta lista para DataXstream cuando el aviso ya
   estaba cerrado.

## Fuentes de datos

- LinkedIn: API guest `/jobs-guest/jobs/api/jobPosting/<id>`, sin login. Trae
  descripción completa, fecha, postulantes y criterios del aviso.
- Bumeran y Computrabajo: SPA detrás de Cloudflare. El script avisa y hay que
  usar la skill `web-search` o pegar el texto. No se inventa nada.
