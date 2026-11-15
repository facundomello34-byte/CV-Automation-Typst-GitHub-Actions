# 🗂️ Estado de búsqueda laboral — Facundo Mello

> **Documento vivo** — actualizado cada sesión. Última actualización: **15/11/2026**.
> Cuando vuelvas a trabajar con un asistente, empezá leyendo este archivo + `README.md`.
>
> ✅ **El 15/11 se enviaron 6 postulaciones:** PwC, Megatech, IBM, Fiserv, Digitas
> y EY. Se terminaron los 54 días sin postular. La próxima acción es el **follow-up
> del 23/11**; mientras tanto quedan 4 viables para el resto de la semana (DiDi,
> Flux, Universia y Nubax). Detalle en `reports/verificacion-2026-11-15.md` y
> `reports/plan-2026-11-16.md`.

---

## 1) Snapshot del perfil

- **Estudios:** Tecnicatura Universitaria en Desarrollo de Software (UADE), 2025–presente, promedio **8.67** · Graduación estimada: **fines de 2028** · Curso certificado Fundamentos de Ciberseguridad (48.5 h, Ago 2026)
- **Stack:** Python, JavaScript, HTML/CSS, FastAPI, Next.js · SQL, PostgreSQL · Linux (diario), bash, Git/GitHub, Docker, Playwright
- **Foco:** primer empleo formal en IT — QA/Testing, soporte IT, automatización, DevOps/trainee
- **Experiencia:** COTO Digital (Operador, Oct 2025–presente) · Bon Air Cafetería (Encargado Admin, Nov 2024–Sep 2025) · Havanna (Soporte Operativo IT, Feb–Jul 2024)
- **Ubicación:** **Castelar, zona oeste (GBA)** · CABA a 45-50 min en tren (Sarmiento) · **sin auto** · **Disponibilidad:** inmediata (avisando a empleador actual) · **Modalidad:** indistinta, pero híbrido en CABA o zona oeste
- **Idioma:** inglés **técnico básico** (lee documentación y código, no sostiene una entrevista oral). Curso de inglés a retomar **en 2027**. ⚠️ Este es el filtro que más ofertas descarta: en la verificación del 11/11, **11 de 20 avisos pedían inglés intermedio o avanzado**.

---

## 2) Pipeline automático (corriendo, pero el embudo se corta después)

- **08:15 (BA) todos los días** GitHub Actions: busca ofertas → **filtra y prioriza** → `reports/priorizadas-YYYY-MM-DD.md`.
- **Estado real al 15/11:** 647 ofertas vistas acumuladas, **7 postuladas** (6 hoy + Besysoft), 0 respuestas registradas todavía. El digest de hoy trajo **99 crudas → 47 priorizadas → 6 nuevas**, y la verificación manual dejó **10 viables**: 6 ya enviadas y 4 pendientes.
- El filtro descarta senior/spam/ofertas de otros países y puntúa el fit:
  junior/trainee **+5** · soporte/QA **+4** · linux/python/dev **+3** · devops/cloud **+2** · publicada ≤2 días **+2** · empresa preferida **+2/3**.
- ⚠️ **El scoring es por palabra clave, no por seniority.** Del top 7 de hoy, 4 no eran para primer empleo (COTO era calidad de alimentos, Confidencial pedía Mainframe/COBOL, Accenture pedía 2-4 años, Stefanini pedía estudiante avanzado excluyente). Revisá el aviso antes de gastar la carta. Por eso la lista de la semana se verificó a mano: `reports/abiertas-2026-11-11.md`.
- 💡 **Dato útil:** la API guest `linkedin.com/jobs-guest/jobs/api/jobPosting/<id>` devuelve la descripción completa y el número de postulantes sin login. Es la forma más rápida de verificar seniority.
- Marca **🆕 NUEVA** solo las ofertas nunca vistas (DB `reports/vistas.json`) — no vas a postular dos veces.

```bash
bash scripts/jobs.sh --days 7                          # refrescar digest ahora
python3 scripts/filter_jobs.py                         # genera priorizadas del día
python3 scripts/filter_jobs.py --mark-applied "URL"    # marcar postulación
python3 scripts/filter_jobs.py --stats                 # ver tracking
```

- Ajustar filtro (palabras, empresas, umbrales): editar `scripts/perfil_filtro.json`.

---

## 3) Índice de archivos

| Archivo | Para qué |
|---|---|
| `reports/plan-2026-11-16.md` | ⭐ **LO PRIMERO QUE ABRÍS HOY** — plan día por día de la semana del 16/11: qué mandar, con qué carta y qué preguntar antes |
| `reports/verificacion-2026-11-15.md` | Verificación del 15/11: 10 viables, 10 descartes con cita y fit por oferta |
| `reports/abiertas-2026-11-11.md` | Verificación anterior (11/11) — historial, varias ya cerraron |
| `reports/investigacion-roemmers-2026-11-11.md` | Investigación de Roemmers: vacantes, pasantías, canales y plan. Paquete completo en `roemmers/` |
| `reports/abiertas-2026-11-07.md` | Verificación anterior (7/11) — sirve de historial, varias ya cerraron |
| `reports/busqueda-2026-11-07.md` | Búsqueda manual anterior: 7 ofertas verificadas, incluye algunas de octubre (Stefanini remoto ya cerrada) |
| `reports/priorizadas-YYYY-MM-DD.md` | Ofertas filtradas y priorizadas del día (scoring automático) |
| `reports/plan-2026-10-24.md` | Plan completo: diagnóstico, ranking de 25 ofertas verificadas, LinkedIn, calendario de contenido, plan de 30 días |
| `reports/postulaciones.csv` | Planilla de seguimiento: empresa, puesto, enlace, fecha, compatibilidad, contacto, estado, próxima acción |
| `reports/jobs-latest.md` | Digest crudo (LinkedIn + Exa), ~80 ofertas — mayoría ruido |
| `reports/vistas.json` | DB de ofertas vistas + postuladas |
| `scripts/jobs.sh` | Digest diario (LinkedIn guest API + Exa) |
| `scripts/filter_jobs.py` | Motor de filtrado y scoring |
| `scripts/perfil_filtro.json` | Perfil como datos — editar para afinar el filtro |
| `cv_es.typ` / `cv_en.typ` + `data_*.typ` | Fuente del CV (ES/EN) → PDFs (auto en GitHub Actions) |
| `carta_pwc_iam.typ` | **Nueva** — PwC IAM Associate (0 a 2 años), ES |
| `carta_dataxstream_en.typ` | **Nueva** — IT Support Tier 1, EN (mandar con `cv_en.pdf`) |
| `carta_stefanini_trainee.typ` | Soporte Data Trainee, ES — adaptar a “híbrido CABA” antes de usar |
| `carta_megatech.typ` | Soporte Técnico Jr CABA, ES — la oferta es del 31/10, sigue abierta |
| `carta_generica.typ` | Carta genérica + 3 variantes (QA/DevOps/Soporte) al final |
| `carta_generica_en.typ` | Carta genérica EN (ofertas remotas) |
| `carta_accenture.typ` / `carta_wetcom.typ` / `carta_ey.typ` | Cartas específicas ya compiladas |
| `perfil-bumeran.md` | Contenido listo para pegar en Bumeran |
| `fuentes-empleo.md` / `consultoras.md` | Portales, consultoras, trainee programs, canales |
| `.github/workflows/jobs-daily.yml` | Corre todo el pipeline diario 08:15 BA |
| `.pi/voice.md` | Perfil de voz: cómo suenan las cartas y qué no inventar (leer antes de escribir) |
| `.pi/skills/humanizar-textos/` | Skill: limpia y puntúa cartas / CV / perfil antes de enviarlos |
| `.pi/skills/evaluar-oferta/` | Skill: verifica un aviso antes de gastar la carta (seniority, inglés, zona, postulantes) |
| `.pi/skills/preparar-entrevista/` | Skill: arma el one-pager de entrevista con historias reales y guion de gaps |
| `emails/` | Seguimientos y mensajes a reclutadores, listos para copiar |

---

## 4) ✅ PLAN DE LA SEMANA (16 al 20/11)

**10 postulaciones viables**, verificadas el 15/11 en `reports/verificacion-2026-11-15.md`.
El detalle día por día está en `reports/plan-2026-11-16.md`.

**✅ Enviadas el 15/11:** PwC, Megatech, IBM, Fiserv, Digitas y EY.
**⏳ Quedan:** DiDi (lunes), Flux, Universia (si el turno no choca con COTO) y
Nubax (solo si es híbrido).

| # | Oferta | Veredicto | Carta |
|---|---|---|---|
| 1 | PwC — Associate IAM | ✅ Enviada · 82% · 40 postulantes | `carta_pwc_iam.pdf` |
| 2 | EY — Junior de IT | ✅ Enviada · 80% | `carta_ey.pdf` |
| 3 | IBM — Internship Generalist | ✅ Enviada · 82% | `carta_ibm.pdf` |
| 4 | Fiserv — Client Service | ✅ Enviada · 74% | `carta_fiserv.pdf` |
| 5 | DiDi — Operations Support | ⏳ Pendiente · 76% | nueva `carta_didi.typ` |
| 6 | Digitas — Data Engineer Trainee | ✅ Enviada · 72% | `carta_digitas.pdf` |
| 7 | Megatech — Soporte Jr CABA | ✅ Enviada · 74% | `carta_megatech.pdf` |
| 8 | Flux IT — QA Analyst Jr | ⏳ Pendiente · 62% · remoto | nueva `carta_flux_qa.typ` |
| 9 | Universia — QA Tester | ⏳ Pendiente · 62% · turno noche | nueva `carta_universia_qa.typ` |
| 10 | Nubax — SOC Jr | ⏳ Pendiente · 60% · preguntar modalidad | nueva `carta_nubax_soc.typ` |

### 🚨 Lo primero del lunes 16

- [ ] **Besysoft** — follow-up de **54 días**. Borrador en `emails/2026-10-24-seguimiento-besysoft.md` (DM + email).
- [ ] **PwC** — preguntar por el inglés del proceso y mandar igual: 40 postulantes, la mejor del mes.
- [ ] **EY Junior de IT** — banco de talentos, no vence, contacto no inmediato.
- [ ] **Megatech** — verificar que siga abierta y mandar: la carta ya está.
- [ ] **Wetcom** — confirmar que la postulación de la ed. 17 entró.

### ❌ Descartadas el 15/11 (no volver a evaluarlas sin motivo nuevo)

Stefanini (avanzado excluyente) · TIVIT (Trelew) · Sovos (Tucumán + inglés oral) ·
DXC (>2 años + inglés) · Lesaffre (Virrey del Pino + 2 años) · Claro (2 años +
avanzado + Java excluyente + Córdoba) · Randstad (Pilar presencial) · BETBY
(inglés intermedio) · EY Consultoría (avanzado + inglés avanzado) · G&L
(avanzado + inglés). Citas en `reports/verificacion-2026-11-15.md`.

---

## 5) 📋 Tabla de postulaciones (tracking)

### 11/11 — plan de la semana

| Fecha | Empresa | Puesto | Portal | Estado | Notas |
|---|---|---|---|---|---|
| 22/09 | Besysoft S.A. | Analista de Soporte y Operaciones TI Junior | LinkedIn | ✔️ Enviada | **Follow-up vencido hace 54 días** · borrador en `emails/2026-10-24-seguimiento-besysoft.md` |
| 11/11 | PwC | Associate Identity & Access Management | LinkedIn | ⏳ Pendiente | 39 postulantes · CABA · `carta_pwc_iam.pdf` |
| 11/11 | DiDi | Operations Support | LinkedIn | ⏳ Pendiente | Early-career · GBA · SQL/Excel · carta nueva |
| 12/11 | IBM | Internship Program Generalist | LinkedIn | ⏳ Pendiente | Sin experiencia previa · CABA · variante SOPORTE |
| 12/11 | Fiserv | Analista de Client Service (bancos) | LinkedIn | ⏳ Pendiente | **Retiro, tren directo** · variante SOPORTE |
| 13/11 | Nubax | Analista SOC Jr | LinkedIn | ⏳ Pendiente | Vicente López (~1 h 20) · confirmar modalidad |
| 13/11 | Confidencial | Desarrollador/a Backend Junior | Bumeran | ⏳ Pendiente | Node.js + SQL + IA · única apuesta DEV |
| 14/11 | Universia | Junior QA Tester (remoto) | LinkedIn | ⏳ Pendiente | Turno mié-dom 19 a 23:50 · choca con COTO |

### 16/11 — plan de la semana

| Fecha | Empresa | Puesto | Portal | Estado | Notas |
|---|---|---|---|---|---|
| 15/11 | PwC | Associate IAM | LinkedIn | ✔️ Enviada | 40 postulantes · preguntar inglés · follow-up 23/11 |
| 15/11 | EY | Junior de IT | EY Careers | ✔️ Enviada | Banco de talentos: **sin follow-up**, revisar marzo 2027 |
| 15/11 | MegaTech | Soporte Técnico Jr | LinkedIn | ✔️ Enviada | CABA presencial · follow-up 23/11 |
| 15/11 | IBM | Internship Generalist | LinkedIn | ✔️ Enviada | 200 postulantes · follow-up 23/11 |
| 15/11 | Fiserv | Client Service | LinkedIn | ✔️ Enviada | Retiro · follow-up 23/11 |
| 16/11 | DiDi | Operations Support | LinkedIn | ⏳ Pendiente | early-career · SQL/Excel · confirmar oficina |
| 15/11 | Digitas | Data Engineer Trainee | LinkedIn | ✔️ Enviada | Pasantía · gap GCP · follow-up 23/11 |
| 17/11 | Flux IT | QA Analyst Jr | Breezy | ⏳ Pendiente | Remoto · pide 1 año |
| 17/11 | Universia | QA Tester | LinkedIn | ⏳ Pendiente | Turno noche · confirmar choque con COTO |
| 18/11 | Nubax | SOC Jr | LinkedIn | ⏳ Pendiente | Preguntar modalidad **antes** de escribir |

### ❌ Fuera por inglés (verificado 11/11)

| Empresa | Puesto | Motivo |
|---|---|---|
| Kaizen Gaming | Junior Backoffice Agent | Inglés y español **avanzados** |
| Acronis | Software Support Specialist | Inglés fluido + 1 año de soporte |
| Assurant | Associate Technical Support Analyst | **Inglés avanzado excluyente** |
| Baufest | QA Analyst Jr | Inglés avanzado |
| MRM | QA Analyst Jr (12 a 21 h) | Inglés avanzado |
| ecoPortal | Implementation Technician | Inglés + 1 año en SaaS |
| SAP | Intern Intelligent Contracting | Inglés proficiente |
| Cloudbeds | Customer Support Coach | Inglés alto |
| InvGate | Bilingual Application Support | 2+ años SaaS + horario 12 a 23 |
| NCR Atleos | Software Support Analyst II | Nivel II + inglés corporativo |
| Sezzle / Canonical | DEV | Procesos íntegros en inglés |

### ❌ Fuera por distancia desde Castelar

| Empresa | Puesto | Motivo |
|---|---|---|
| Randstad Digital | Helpdesk N1-N2 | **Pilar**, presencial 8 a 17, sin auto: ~2 h por tramo |
| NovaStar | Technical Support Engineer | **Pilar** |
| Empleos IT | Soporte on site | **Quilmes** + auto propio excluyente |

### Cerradas o descartadas en la verificación del 11/11

| Empresa | Puesto | Estado | Notas |
|---|---|---|---|
| DataXstream | IT Support Specialist (Tier 1) | ❌ Cerrada | Ya no acepta solicitudes |
| Stefanini LATAM | Data Support Analyst Jr / Trainee | ❌ Descartada | Pide estudiantes **avanzados** (excluyente) |
| Confidencial | QA Engineer Jr (Contable) | ❌ Descartada | Mainframe/COBOL/Control-M + inglés B2 |
| COTO | Analista de control de calidad | ❌ Descartada | Calidad de alimentos, no QA de software |
| Accenture | DevOps Engineer / Network Analyst | ❌ Descartada | Rancher/SAST-DAST · 2-4 años en redes |
| Allata | Test Harness Engineer | ❌ Descartada | Nivel senior, mentoreo y frameworks |
| InvGate | Bilingual Application Support | ❌ Descartada | 2+ años SaaS · horario 12 a 23 |
| Strix / Coderio / COELSA | Seguridad y SOC | ❌ Descartadas | Experiencia previa en SOC/SIEM o AD (3-5 años) |
| Megatech | Soporte Técnico Jr – CABA | ✅ Abierta (31/10) | Carta `carta_megatech.pdf` lista como excepción |
| Clipboard | Client Support Specialist B2B | ✅ Abierta (4/11) | Remoto, todos los niveles, inglés oral y escrito |

### Historial (sin postular — archivar)

Las 19 de la lista del 30/09 y las 18 del 31/10 quedaron en ⏳ y nunca se enviaron. No se borran para no perder los datos, pero **no cuentan como postulaciones activas**. Hasta el 14/11 la tasa era **1 enviada en 54 días**; el 15/11 se enviaron 6 de una vez. La prueba de esta semana es sostener el ritmo, no el arranque.

> Al postular, marcar en la DB: `python3 scripts/filter_jobs.py --mark-applied "URL"` — así el filtro muestra "ya postulada" y no la repite.

---

## 6) 💬 Banco de respuestas para formularios

**Disponibilidad** (`¿Cuál es tu disponibilidad?`):
> "Disponibilidad inmediata. Además de estudiar la Tecnicatura en Desarrollo de Software, actualmente trabajo en COTO Digital, por lo que puedo coordinar la fecha de ingreso avisando con la anticipación que corresponda a mi empleador. Me adapto a los horarios que necesite la empresa."
> (Corta: "Disponibilidad inmediata. Puedo coordinar el ingreso con mi empleador actual y adaptarme al horario.")

**Fecha de graduación estimada** (`¿Cuándo te recibís?`):
> "Graduación estimada: finales de 2028. Actualmente curso la Tecnicatura Universitaria en Desarrollo de Software en UADE (promedio 8.67)."

**CNC/materiales u otra experiencia que NO tengo** → responder con honestidad:
> "No tengo experiencia con [X]. Mi experiencia es en soporte IT y sistemas (Windows/Linux, resolución de incidencias, sistemas POS) y desarrollo de software (Python, Linux, Docker, Playwright). Estoy buscando mi primer empleo en el sector IT."

**¿Usaste Jira / macOS / Intune / Control-M / SailPoint?** (frecuente en soporte e IAM):
> "Todavía no. Registraba incidencias en los sistemas internos de cada empresa y hacía el seguimiento ahí. Manejo Windows y Linux, y aprendo la herramienta nueva rápido."

**Pretensión salarial:** $900.000–$1.200.000 ARS brutos/mes (negociable) — referencia: mediana dev junior Sysarmy 2026 ≈ $1.538.500; primera experiencia/soporte está por debajo. Si el puesto es dev junior: pedir ~$1.300.000–$1.500.000.

**Palabras clave Bumeran:** `soporte técnico` · `QA` · `tester` · `junior` · `trainee` · `help desk`/`mesa de ayuda` · `soporte de aplicaciones` · `DevOps` (filtrar junior) · `desarrollador` + filtros (Últimos 7 días, Categoría Sistemas, CABA/GBA).

---

## 7) Reglas de oro (no borrar)

1. Postular en **24–48 h** de publicada la oferta (el filtro marca 🆕 para esto).
2. **Nunca inventar** experiencia/herramientas que no estén en el CV (Jira, Terraform, macOS, SailPoint, Control-M, CNC, etc.).
3. **Coherencia total** entre CV, cartas, Bumeran, LinkedIn y entrevistas (datos, fechas, promedio, disponibilidad).
4. Follow-up a los **7–10 días** sin respuesta.
5. Volumen: mínimo **10 postulaciones/semana** — cada postulación es un ticket de lotería.
6. Aplicar aunque no cumplís 100% — con **60-70%** de requisitos, aplica igual.
7. **Verificar el aviso antes de escribir la carta.** Si no dice junior/trainee/N1/entry-level/associate y pide 2+ años, es un no.
8. **Inglés:** si el aviso dice “intermedio”, “avanzado”, “fluido” o “excluyente”, es un no. Solo aplica a los que piden inglés para **leer documentación**. No inventes nivel en el CV: poné *“inglés técnico (lectura), en formación”*.
9. **Distancia:** nada presencial fuera de CABA o zona oeste salvo que sea híbrido. Pilar, Quilmes y La Plata quedan fuera sin auto.

---

## 8) 📌 Próximos pasos (próxima sesión)

1. **Follow-up el lunes 23/11** (8 días) a las 5 que tienen proceso activo: PwC, Megatech, IBM, Fiserv y Digitas. EY es banco de talentos, no se sigue. Plantilla lista en `emails/2026-11-23-seguimiento-postulaciones.md`.
2. **Completar la semana:** DiDi (lunes), Flux (martes), Universia (si el turno no choca con COTO) y Nubax (solo si es híbrido, preguntar antes). Son las 4 que quedan de las 10 viables.
3. **Preparar la entrevista antes de que llegue:** el one-pager de PwC ya está en `entrevistas/pwc-2026-11.md`. Para Megatech, IBM o Fiserv: `/skill:preparar-entrevista <empresa>`.
4. **Viernes 20/11:** contar enviadas (meta: 10), respuestas y entrevistas. Si no hay ninguna respuesta a los 10 envíos, el problema es el CV o el canal, no la cantidad.
5. **No tocar `perfil_filtro.json`** esta semana. Primero 10 enviadas y medir respuestas.
6. El digest sigue corriendo solo a las 08:15. Revisar `reports/priorizadas-<fecha>.md` solo cuando haya que sumar ofertas, no todos los días.

### Verificar antes de postular (método rápido)

```bash
# Descripción completa + postulantes, sin login
curl -s -A "Mozilla/5.0" \
  "https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/<ID>" \
  | grep -o 'no longer accepting' | head -1   # si aparece: cerrada
```

El ID son los últimos dígitos de la URL del aviso.

### Pendiente de decisión (no lo resuelvo solo)

- **Inglés: adelantar el curso.** Es el filtro que más ofertas descarta (11 de 20 avisos del 11/11). Esperar a 2027 cuesta, conservadoramente, media búsqueda. Alternativa inmediata y gratuita: **EF SET** (test de 50 min, certificado) para tener un nivel medido y no una autopercepción. Si da B1, se puede escribir “B1 (EF SET)” en el CV, que es honesto y verificable.
- **Zona oeste:** los portales indexan mal Morón/Haedo/San Justo/Castelar. Vale la pena una búsqueda manual semanal en Bumeran, Computrabajo, ZonaJobs, el **portal de empleo de UADE** y la **bolsa de la UTN Haedo**.
- **COTO como puerta interna:** con un año adentro, averiguar si hay pases a sistemas/administración antes de irse. Es la vía más rápida a “experiencia IT formal” sin cambiar de empleador.
- **Pretensión salarial:** `perfil-bumeran.md` usa la mediana junior de la **Encuesta Sysarmy 2026.1** ($1.538.500) para fijar el rango $900.000–$1.200.000. Con ~19% de inflación semestral, ese rango puede estar corto. Decisión tuya: mantenerlo o subirlo ~15% y arriesgar filtros por precio.
- **Volumen real:** con 647 ofertas vistas y 1 postulación, añadir fuentes no cambia nada. Antes de tocar `scripts/perfil_filtro.json`, hacé 10 postulaciones en una semana y medí respuestas.
- **DEV vs. soporte:** esta semana el mercado de desarrollo junior no ofreció nada nuevo que cierre. Las apuestas DEV están en la sección 4; el volumen realista está en soporte/QA/IAM.
