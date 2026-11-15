# 🔬 Auditoría del CV — 26/10/2026

_Contra 16 avisos reales de soporte/QA/jr/trainee que verifiqué hoy. No es opinión: cada
punto sale de comparar el texto del CV con lo que piden los avisos._

**Veredicto:** el CV está bien escrito y es honesto, pero hoy **pierde filtros automáticos**
por tres razones: no tiene LinkedIn, no dice dónde vivís ni cuándo podés empezar, y su
primera línea vende "desarrollo" cuando la mayoría de los puestos a los que te conviene
apuntar son de soporte. Se arregla sin inventar nada.

---

## 1) Cobertura de requisitos (16 avisos, cuántos lo piden)

| Requisito | Avisos | ¿Está en tu CV? |
| --- | --- | --- |
| Tickets / ticketing | 8/16 | Sí, pero escondido en un bullet |
| Redes / Wi-Fi / conectividad | 8/16 | Sí ("redes Wi-Fi") |
| Inglés | 8/16 | Sí, pero ambiguo |
| Mesa de ayuda / help desk | 4/16 | **No aparece la palabra** |
| Monitoreo / NOC | 4/16 | No |
| Windows | 3/16 | Sí |
| Hardware | 3/16 | Sí |
| SQL | 3/16 | Sí |
| Python | 3/16 | Sí |
| Estudiante / carrera en curso | 5/16 | Sí |
| Soporte remoto (AnyDesk, TeamViewer) | 2/16 | No |
| Jira | 2/16 | No |
| Office 365 / Outlook / SharePoint | 2/16 | No |
| Active Directory | 1/16 | No |
| Gestión de usuarios y contraseñas | 1/16 | No |
| Cloud (AWS/Azure/GCP/OCI) | 6/16 | No (y no lo tenés) |

Traducción: en lo que **sí** tenés, el CV ya cubre el 80%. Lo que falta se concentra en
cuatro cosas de soporte empresarial (AD, M365, soporte remoto, Jira) que hoy no podés
poner porque no las usaste. La sección 5 las convierte en algo real en dos semanas.

---

## 2) Los 7 cambios que mueven la aguja

### 2.1 LinkedIn: está comentado en el archivo
`data_es.typ` y `data_en.typ` tienen la línea `#let linkedin` comentada, así que el PDF sale
sin LinkedIn. La plantilla ya lo soporta (el header une teléfono · GitHub · LinkedIn).
Para soporte y QA, el reclutador busca el perfil ahí antes de llamar. **Es el cambio más
grande y cuesta 2 minutos.**

### 2.2 Falta ubicación, disponibilidad y modalidad
Hoy el header no dice nada de eso. En los avisos de soporte N1 la presencialidad en CABA es
el primer filtro. Agregá al final del perfil:
> Disponibilidad inmediata. Presencial en CABA y GBA, híbrido o remoto.

### 2.3 El perfil apunta a "desarrollo" y a vos te conviene "soporte"
La primera línea dice "con foco en desarrollo de aplicaciones, QA Testing y automatización"
y después "Interés en infraestructura y DevOps". Para un aviso de mesa de ayuda eso suena a
que te vas en seis meses. El perfil tiene que nombrar el puesto al que aplicás. Abajo van
tres variantes para que elijas según el aviso.

### 2.4 La sección de tecnologías mezcla categorías
"Docker" no es una base de datos y "redes Wi-Fi" no es una competencia. Reordenada queda
más escaneable y mete las palabras que buscan los filtros:

```
*Lenguajes*: Python, JavaScript, HTML, CSS, SQL\
*Bases de datos*: PostgreSQL (consultas, validación de datos)\
*Infraestructura y herramientas*: Linux (uso diario), terminal/CLI (bash),
Git/GitHub, Docker\
*QA y testing*: Playwright (pruebas E2E), validación de datos, diseño de casos
de prueba\
*Soporte IT*: mesa de ayuda y ticketing, Windows, hardware, impresoras y
periféricos, redes y conectividad, resolución de incidencias\
*Idiomas*: inglés intermedio-avanzado (lectura técnica y conversación)
```

Tres cosas para revisar antes de pegarlo: "diseño de casos de prueba" solo si efectivamente
armaste casos y no solo corrés Playwright; "conversación" solo si podés sostener una
llamada; "impresoras y periféricos" es verdad y hoy no aparece.

### 2.5 Los bullets de experiencia no nombran el soporte
Hoy el primer bullet habla de "operación logística y vouchers". Vos hacés soporte de primera
línea todos los días y eso está en el cuarto bullet. Reordená para que lo primero que lea sea
lo que el aviso pide:

```
- Primera línea de soporte del sector: resuelvo fallas de impresoras, PDA y
  equipos para que la operación no se detenga.
- Emisión y seguimiento de tickets de pedidos, con control del estado hasta el
  cierre.
- Preparación de pedidos y vouchers con PDA y sistemas internos.
- Optimización de tareas repetitivas del puesto con las herramientas del sistema.
```

Y en Havanna, subí el soporte a usuarios:
```
- Soporte técnico a las computadoras del salón: configuración, validación de
  datos y resolución de fallas en el momento.
- Operación y soporte de MAXIREST, el sistema interno de gestión del local.
- Responsable de caja y del funcionamiento del sector.
```

### 2.6 "Lógica de programación" no lo busca nadie
Está en Competencias y ocupa lugar. Cambialo por lo que sí filtra un reclutador de soporte:
> Atención a usuarios, resolución de incidencias, trabajo en equipo, documentación de
> procedimientos.

### 2.7 El inglés está dicho de forma ambigua
"inglés técnico (intermedio/avanzado)" deja la duda de si podés hablar. Poné el nivel y para
qué: "intermedio-avanzado (lectura técnica y conversación)". Si no te animás a una entrevista
en inglés, dejalo en "lectura técnica" y listo. No inflarlo: 8 de 16 avisos lo piden y te van
a probar.

---

## 3) Perfil: las tres variantes

Elegí una, no las mezcles. La estructura es la misma: qué estudiás, qué puesto buscás, tres
pruebas concretas, diferencial, disponibilidad.

**SOPORTE (Megatech, Stefanini, SMS, Radio Mitre, Ecosistemas):**
> Estudiante de la Tecnicatura en Desarrollo de Software (UADE, promedio 8.67), en busca de
> mi primer empleo formal en IT como soporte técnico o mesa de ayuda. Vengo de operaciones:
> en COTO Digital resuelvo a diario fallas de PDA, impresoras y equipos del sector; en Bon
> Air administraba el FUDO POS y destrababa las incidencias del sistema; en Havanna daba
> soporte a las computadoras del salón. Uso Linux a diario y automatizo tareas repetitivas
> con Python y bash. Disponibilidad inmediata. Presencial en CABA y GBA, híbrido o remoto.

**QA (Napse, Flux IT, Caylent):**
> Estudiante de la Tecnicatura en Desarrollo de Software (UADE, promedio 8.67), en busca de
> mi primer empleo formal en IT como QA. Automatizo pruebas E2E con Playwright sobre un SaaS
> propio (FastAPI, PostgreSQL, Docker) y armé el sistema de stock de una cafetería, donde
> validaba datos e inconsistencias antes de que llegaran al local. Mi paso por operaciones
> (POS, PDA, impresoras) me dio el ojo de quien vio sistemas romperse en producción. SQL y
> Linux para leer logs y reproducir errores. Disponibilidad inmediata.

**DEV (Canals, Analista Jr de Automatización):**
> Estudiante de la Tecnicatura en Desarrollo de Software (UADE, promedio 8.67), buscando mi
> primer empleo formal en IT como desarrollador backend junior. Construí y contenericé un
> SaaS de automatización para comercios: FastAPI, PostgreSQL, Next.js, pruebas E2E con
> Playwright y todo corriendo en Docker. Antes programé el sistema de stock de una cafetería.
> Trabajo con Git y Linux a diario. Disponibilidad inmediata, remoto o híbrido.

---

## 4) Lo que NO hay que agregar

- **Jira, Active Directory, Office 365, ServiceNow**: no los usaste. Si el aviso los pide y
  los ponés, se cae en la primera pregunta de la entrevista. Se consiguen en dos semanas
  (sección 5).
- **"Manejo de redes"** cuando tenés Wi-Fi y conectividad básica. "Redes y conectividad" es
  exacto; "administración de redes" es mentira.
- **Años de experiencia inventados.** Tenés desde feb 2024 en operaciones con soporte; eso se
  dice como "dos años en operaciones resolviendo incidencias técnicas", no como "2 años en IT".
- **Métricas que no mediste** ("reduje un 30% los tiempos"). Si no lo mediste, no va.

---

## 5) Las 4 skills que faltan y cómo tenerlas de verdad (14 días)

Ninguna requiere pagar. Todas dejan evidencia que podés mostrar en la entrevista.

| Días | Skill | Cómo, concreto | Qué podés escribir después |
| --- | --- | --- | --- |
| 1–2 | **Jira** | Plan free. Cargá el backlog del SaaS: épicas, tickets, sprint, estados. | "Jira (gestión de tickets y backlog del proyecto propio)" |
| 3–5 | **Active Directory** | VM Windows Server 2022 (eval) + cliente Windows 11 en VirtualBox: OU, usuarios, grupos, GPO, reseteo de contraseñas, DNS y DHCP. | "Active Directory en laboratorio: altas y bajas, grupos, GPO, reseteo de contraseñas" |
| 6–7 | **PowerShell** | Scripts de altas masivas de usuarios, inventario de equipos, limpieza de discos. Subilo a GitHub. | "PowerShell: altas masivas e inventario" |
| 8–9 | **Soporte remoto** | AnyDesk y TeamViewer en el lab, y escribí el procedimiento de atención. | "Soporte remoto (AnyDesk, TeamViewer)" |
| 10–11 | **Microsoft 365** | Tenant de desarrollador gratuito: usuarios, licencias, Outlook, Teams. | "Microsoft 365: gestión de usuarios y licencias" |
| 12–14 | **ITIL (fundamentos)** | Gestión de incidentes, SLA, escalamiento. Certificar es pago; leer y documentar es gratis. | "Fundamentos de ITIL: incidentes, SLA y escalamiento" |

Con eso, el CV suma una sección corta:

```
#let projectstitle = [ Laboratorio de Soporte IT ]
```
...con dos o tres bullets que apunten a lo mismo que piden los avisos (AD, PowerShell,
soporte remoto, ticketing). Eso es lo que separa tu CV del de otro estudiante sin
experiencia: no dice "me interesa", dice "esto lo hice".

---

## 6) Cómo validar el cambio

```bash
typst compile cv_es.typ && typst compile cv_en.typ
pdfinfo cv_es.pdf | grep Pages        # tiene que seguir en 1
```

Después, espejar los mismos cambios en `data_en.typ` (el CV en inglés se manda a Caylent y
Telnyx). El panel de `humanizar-textos` no aplica acá: un CV va impersonal y da bajo en VOZ a
propósito.

---

## 7) Prioridad si tenés 10 minutos

1. Descomentar LinkedIn en los dos `data_*.typ` (2 min).
2. Agregar ubicación y disponibilidad al perfil (1 min).
3. Cambiar el perfil a la variante SOPORTE (3 min).
4. Reordenar la sección de tecnologías (3 min).
5. Recién después, el laboratorio de 14 días. Eso es lo que te va a hacer llamar en 2027,
   no una palabra más en la lista de hoy.
