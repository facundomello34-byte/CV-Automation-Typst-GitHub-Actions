# 🔎 Búsqueda avanzada de empleos — 26/10/2026

_Búsqueda profunda hecha a mano (no es el digest automático). 48 queries a LinkedIn,
3 APIs de ATS, Exa, y verificación de la ficha real de cada oferta antes de puntuarla._

**Resultado: 8 ofertas para postular hoy, 5 de respaldo y 7 descartadas con motivo.**

---

## 0) Qué se hizo (para que sea repetible)

| Fuente | Cómo | Qué salió |
| --- | --- | --- |
| LinkedIn guest API | 48 queries nuevas (soporte N1, QA manual, automation, NOC, POS, SAP, dev junior, empresas puntuales) + 2 barridos | 78 ofertas crudas, 3 días |
| Ficha real de LinkedIn | endpoint `jobPosting/{id}`: descripción completa, seniority, postulantes, modalidad | permite descartar sin adivinar |
| Lever (Despegar) | `api.lever.co/v0/postings/despegar` | Pasaporte Trainee 2026 **cerrado**, solo queda Analista Jr Brasil |
| Breezy (Flux IT) | `fluxit.breezy.hr/json` | 6 búsquedas jr abiertas, incluida QA y DevOps Jr |
| Greenhouse | 17 boards (Ualá, Pomelo, Tiendanube, MODO, Ripio, PedidosYa…) | **0** ofertas jr/soporte/QA en Argentina |
| Bumeran / ZonaJobs / Computrabajo | Cloudflare bloquea el scraping; solo snippets | sirven como canal manual, no como fuente automática |

> Dato que cambia el ranking: el filtro automático puntúa por palabra clave y **no ve cuánta
> gente se postuló ni cuántos años piden**. Acá sí. Por eso hay ofertas con 10 pts del bot
> que quedaron descartadas y ofertas con 5 pts que subieron.

---

## 1) 🚨 Postular hoy (mañana 26/10, en este orden)

### 1. Soporte Técnico Jr — Megatech S.A. · **90% de fit**
`pub. 24/10 · +200 postulantes · presencial CABA 9–18 · full time`
https://ar.linkedin.com/jobs/view/soporte-tecnico-jr-caba-at-megatech-s-a-4483340664

Piden exactamente lo que tenés: instalación de PC y periféricos, Windows, redes básicas,
tickets, trato con usuario. "Estudios en curso en Sistemas" es **valorado**, no excluyente.
No piden años de experiencia.
→ Carta: variante **SOPORTE**. Único riesgo: el horario 9–18 choca con COTO; resolvelo en
la entrevista, no en el formulario.

### 2. Analista de Soporte Técnico Data – Trainee — Stefanini LATAM · **85%**
`pub. 20/10 · +200 postulantes · 100% remoto · 9–18`
https://ar.linkedin.com/jobs/view/analista-de-soporte-t%C3%A9cnico-data-trainee-at-stefanini-latam-4480266777

Trainee explícito, remoto, piden estudiante en curso y **SQL básico**. Es el mejor
combo perfil/modalidad de toda la lista y ya lleva 6 días publicada: cada día que pasa
pesa. Es la que menos excusa tiene para no salir hoy.
→ Carta: variante **SOPORTE** (mencioná SQL y validación de datos).

### 3. Junior Software Engineer — Canals · **80%**
`pub. 23/10 · +200 postulantes · remote-first (LATAM/US)`
https://ar.linkedin.com/jobs/view/junior-software-engineer-at-canals-4482812475

"Typically 0–2 years… **internships or projects count**", backend en Python/Node/Go,
empresa rentable de ~140 personas. Tu SaaS con FastAPI + PostgreSQL entra perfecto como
"projects count". Es la mejor oferta de desarrollo jr que apareció en tres semanas.
→ Carta: variante **DEV** (o `carta_generica_en.typ`, la empresa es en inglés).

### 4. Quality Analyst Associate Engineer — Caylent · **72%**
`pub. 24/10 · 69 postulantes · 100% remoto · pago en USD`
https://ar.linkedin.com/jobs/view/quality-analyst-associate-engineer-at-caylent-4481970256

Piden **0–2 años en testing**, remoto total, AWS/Amazon Connect (contact center: IVR, chat).
No tenés QA formal, pero sí Playwright E2E, casos de prueba y el sistema de stock. 69
postulantes es la mitad que el resto: ventana buena.
→ Carta: variante **QA** en inglés.

### 5. Analista Jr de Automatización — Empresa Confidencial · **70%**
`pub. hoy 26/10 · 88 postulantes · híbrido Saavedra (3+2) · 9–18`
https://ar.linkedin.com/jobs/view/analista-jr-de-automatizaci%C3%B3n-at-empresa-confidencial-4481447266

Entry level, "al menos 1 año en desarrollo y automatización" (tu proyecto propio cubre
buena parte), Python/JS/SQL como **plus**, herramientas de IA, marketplaces y ERP.
Publicada hace 2 horas: es la más fresca de la lista.
→ Carta: variante **DEV**, con una línea sobre automatizar procesos de comercio (Bon Air).

### 6. Tester Manual — Napse Global · **55%, pero la de menor competencia**
`pub. hace 1 hora · 43 postulantes · Buenos Aires`
https://ar.linkedin.com/jobs/view/tester-manual-at-napse-global-4481454321

Piden testing manual + **retail y POS** + Jira. Vos tenés POS de verdad (FUDO, MAXIREST) y
el requisito de "testing" es lo que te falta. Con 43 postulantes y una hora de publicada,
es la mejor relación esfuerzo/probabilidad del día.
→ Carta: variante **QA**, apoyate en POS y en Playwright, sin decir que hiciste QA formal.

### 7. Technical Product Support Engineer (Remote AMER) — Telnyx · **60%**
`pub. 23/10 · 118–151 postulantes · 100% remoto desde Argentina`
https://ar.linkedin.com/jobs/view/technical-product-support-engineer-remote-amer-at-telnyx-4474744304

**No piden años.** Piden Linux terminal, REST APIs, DNS/routing/HTTP, inglés proficiente.
Tenés 5 de 6. El inglés es el filtro real: si podés sostener una llamada técnica, aplicá.
→ Carta: `carta_generica_en.typ` variante **SOPORTE**.

### 8. QA Analyst Jr — Flux IT · **50%, pero es gratis**
`pipeline abierto (Breezy) · 100% remoto`
https://fluxit.breezy.hr/p/7d6df5000801-qa-analyst-jr

Piden 1 año en diseño/ejecución de casos de prueba + Jira. No lo tenés, pero el formulario
es de 5 minutos, la búsqueda está abierta desde septiembre y es remota. Mandala igual:
el costo de aplicar es cero y Flux IT ya estaba en tu lista de pendientes.
→ Carta: variante **QA**.

---

## 2) ⭐ Respaldo (si te quedan 20 minutos, o mañana)

| Fit | Oferta | Datos | Link |
| --- | --- | --- | --- |
| 62% | **Analista Help Desk Jr — SMS Buenos Aires** | SQL + tickets + estudiante avanzado, Crystal Reports deseable · +200 post. · 1 semana | [ver](https://ar.linkedin.com/jobs/view/analista-help-desk-junior-at-sms-buenos-aires-4476506404) |
| 60% | **Soporte Técnico — Radio Mitre** | 1–3 años, inglés B1/B2, presencial CABA, hardware/redes/AD · +200 post. | [ver](https://ar.linkedin.com/jobs/view/soporte-tecnico-at-radio-mitre-4482644971) |
| 55% | **Analista MDA — Ecosistemas** | 100% remoto, N1, Windows/M365/VPN/MFA, **ServiceNow** y guardias rotativas · +200 post. | [ver](https://ar.linkedin.com/jobs/view/analista-mda-at-ecosistemas-4483328462) |
| 45% | **Payroll Technology Support Staff — EY GDS** | Piden 2–4 años, pero **solo 42 postulantes** y EY está en tu banco de talentos | [ver](https://ar.linkedin.com/jobs/view/payroll-technology-support-staff-ey-global-delivery-services-at-ey-4472844427) |
| — | **DevOps Jr / React Jr / Java Jr / Angular Jr — Flux IT** | Todas abiertas en Breezy, 100% remoto, pipeline permanente | [ver](https://fluxit.breezy.hr/) |

---

## 3) 🗑 Descartadas con motivo (el bot las puntuó alto)

Estas consumen tiempo y no son para primer empleo. Verificado en la ficha, no en el título:

| Oferta | Por qué no |
| --- | --- |
| Acciona IT — Analista Funcional Junior | "Al menos 2 años como Analista Funcional **(excluyente)**", medios de pago/POS |
| Grupo Hasar — Analista de Mesa de Ayuda | 3 años + InvGate |
| MaxIT — QA Tester SAP UAT | 3 años como tester + 1 año en módulo SAP |
| Claro — Analista QA Automatización | Córdoba + 2 años + frameworks propios |
| Novatium — Soporte IT y Audiovisual | **Cerrada** (404 en la ficha) |
| Sovos — QA Intern | Tucumán presencial, no remoto |
| Personal — Mi Primer Empleo Técnico | Exige residencia en La Plata y registro B1 |
| OneInfo — Soporte Cloud N1 | 100% presencial + turnos nocturnos rotativos: incompatible con COTO |
| BM Global — Network Operations Engineer | 2–4 años + CCNA/Network+ |
| Mandü — Technical Customer Care | Perfil de post-venta con diagnóstico de ERP y upselling, no mesa de ayuda |

---

## 4) Canales que valen más que otra búsqueda

1. **Bumeran junior** (bloquea scraping, hay que entrar a mano): 42 avisos jr de tecnología en
   Buenos Aires → https://www.bumeran.com.ar/en-buenos-aires/empleos-area-tecnologia-sistemas-y-telecomunicaciones-seniority-junior.html
   Filtrá por "Últimos 7 días" y subá `cv_es.pdf`.
2. **Flux IT (Breezy)**: es un ATS con búsquedas permanentes jr. Entrá una vez, dejá el CV y
   quedás en el pipeline de todas: https://fluxit.breezy.hr/
3. **Despegar (Lever)**: Pasaporte Trainee 2026 ya no está publicado. La única jr abierta es
   en Brasil. Volver a mirar en feb–mar 2027.
4. **Computrabajo**: la búsqueda `soporte tecnico junior` devuelve ofertas que LinkedIn no
   muestra (Yel Solutions, Field Support IT CABA). Se lee en el navegador, no por script:
   https://ar.computrabajo.com/trabajo-de-soporte-tecnico-junior
5. **Trainee programs**: Stellantis GPS 2027 (30 vacantes AR/BR, recién graduados) y Quilmes
   GMT 2027 abrieron inscripción; Techint Verano 2027 también. Ninguno encaja con
   "estudiante en curso" salvo Techint, pero conviene tenerlos en el calendario 2027.
6. **Endava** The Americas Internship (QA Automation, Python): abre **febrero 2027**.

---

## 5) Después de postular (2 minutos, no lo saltees)

```bash
python3 scripts/filter_jobs.py --mark-applied "<URL>"
```

Y actualizá `reports/postulaciones.csv`: sin eso, en la próxima sesión no hay forma de saber
qué se mandó. Las 8 de arriba son 8 filas nuevas.

**Regla que sigue sin cumplirse:** 1 postulación en 34 días. Con estas 8, la semana cierra
en 8 de 10. Las 3 primeras (Megatech, Stefanini, Canals) son las que más chances reales
tienen: no las dejes para mañana.
