# Banco de historias — material real, sin inventar

> Todo lo de acá sale de `data_es.typ`, las cartas y `estado-busqueda.md`.
> Donde falta un número va `{{dato}}`: se completa con lo que Facundo recuerde
> o se deja afuera. **No se estima "más o menos".**

Cada historia tiene dos versiones: **larga** (~2 min, para "contame una vez
que...") y **corta** (~60 s, para repreguntas). La estructura es STAR:
Situación, Tarea, Acción, Resultado.

---

## 1. La impresora que frenaba la operación — COTO Digital

**Cuándo usarla:** soporte N1/N2, helpdesk, field service, "contame un problema
técnico que resolviste", "cómo trabajás bajo presión".

- **S:** Operador en COTO Digital desde octubre 2025. La operación logística
  depende de PDA, sistemas internos y vouchers impresos: si una impresora o un
  equipo del sector se cae, se frena la preparación de pedidos.
- **T:** Resolver los inconvenientes técnicos básicos del sector sin depender
  de que venga alguien de sistemas.
- **A:** Diagnóstico inicial (conexión, cola de impresión, configuración,
  reinicio del equipo), resolución autónoma cuando estaba a mi alcance y
  registro del caso en el sistema cuando había que escalar. Seguimiento del
  ticket hasta que se cerraba.
- **R:** La operación seguía. Cualitativo: **no tengo el número de tickets ni
  de equipos**; si me lo piden, digo `{{cuántos equipos / tickets por día}}` y
  aclaro que no llevaba la métrica.

**Versión corta:** "En COTO la operación se frena si falla una impresora o un
PDA. Resolvía lo básico en el momento y lo que no, lo documentaba y seguía el
ticket. Lo que aprendí es que en soporte el registro importa tanto como la
reparación."

**Lo que NO digo:** que administraba la red, que hacía soporte de segundo
nivel, ni que era el referente técnico del turno.

---

## 2. Automatizar el cierre de caja — Bon Air Cafetería

**Cuándo usarla:** automatización, mejora de procesos, iniciativa, "contame
algo que hayas mejorado", DevOps/trainee.

- **S:** Encargado administrativo en Bon Air (nov 2024 – sep 2025). El local
  usaba FUDO POS; el registro de ventas, el control de stock y los cierres de
  caja diarios se hacían a mano.
- **T:** Sacar trabajo repetitivo y errores de carga de la operación diaria.
- **A:** Implementé soluciones con las herramientas que había —planillas y el
  propio sistema de gestión— para automatizar el registro de ventas, el stock
  y el cierre de caja. No desarrollé software a medida ahí: armé el proceso.
- **R:** Menos tiempo en tareas repetitivas y cierres más prolijos. **No tengo
  el número de horas ahorradas** → `{{horas por semana que se ahorraban}}`.

**Versión corta:** "En Bon Air el cierre de caja era manual. Armé el proceso
para que el sistema registrara ventas y stock y el cierre saliera solo. Ahí
entendí que automatizar no siempre es programar: a veces es ordenar el flujo."

**Lo que NO digo:** que fue un desarrollo propio, ni que usé Python ahí.

---

## 3. Soporte en hora pico — Havanna

**Cuándo usarla:** atención al usuario, priorización, trabajo bajo presión,
clientes internos, "contame un día difícil".

- **S:** Soporte operativo orientado a IT en Havanna (feb – jul 2024), con el
  sistema interno MAXIREST y las computadoras que usaban los mozos.
- **T:** Que el salón siguiera funcionando cuando había un problema con el
  sistema o con un equipo, en el momento de más gente.
- **A:** Validación de información, soporte técnico directo a los mozos,
  resolución de lo que estaba a mi alcance y coordinación con quien
  correspondía para lo demás. Además estaba a cargo de caja.
- **R:** Servicio sin cortes en el horario pico. Cualitativo.

**Versión corta:** "En Havanna el mozo no puede esperar diez minutos a que
alguien de sistemas aparezca. Aprendí a resolver rápido, a preguntar bien y a
distinguir qué se arregla en el momento y qué se escala."

**Lo que NO digo:** que era el área de IT de Havanna. Era soporte operativo
orientado a IT, y así lo digo.

---

## 4. El SaaS que armé de punta a punta — proyecto propio

**Cuándo usarla:** DEV trainee/junior, QA automation, "qué construiste",
"cómo testeás", "qué stack usás".

- **S:** Proyecto propio, en curso: plataforma SaaS de automatización de
  procesos para comercios.
- **T:** Prototipo funcional, con backend, frontend, base de datos y pruebas.
- **A:** Python + FastAPI para la API, PostgreSQL para datos, Docker para
  contenedorizar, JavaScript/Next.js para el frontend y Playwright para pruebas
  E2E. Integración de servicios y automatización de procesos administrativos.
- **R:** Prototipo funcional y contenedorizado. **Honestidad:** la estrategia de
  testing y el despliegue en producción están pendientes; no está en producción.

**Versión corta:** "Armé un SaaS para comercios con FastAPI, PostgreSQL y
Docker, y lo probé con Playwright. Lo que más aprendí fue el ciclo completo:
no es solo que compile, es que se pueda desplegar y probar."

**Lo que NO digo:** que tiene usuarios, que escala, ni que está en producción.

---

## 5. Control de stock en Python — proyecto UADE

**Cuándo usarla:** lógica de negocio, bases de datos, trabajo académico,
"contame un proyecto de la facultad".

- **S:** Proyecto de la facultad (2025), gestión de stock para una cafetería.
- **T:** Modelar productos, clientes y ventas, con reportes y automatización de
  inventario.
- **A:** Backend en Python con la lógica de negocio y el modelo de datos.
- **R:** Sistema funcional de gestión. Sin métricas de uso: fue académico.

**Versión corta:** "Hice un backend en Python para stock de una cafetería:
productos, ventas, reportes y actualización automática de inventario. Ahí
practiqué modelado de datos y lógica de negocio."

---

## 6. El incidente empieza en un permiso de más — curso de ciberseguridad

**Cuándo usarla:** IAM, SOC, seguridad, "por qué te interesa", PwC/Nubax.

- **S:** Curso certificado Fundamentos de Ciberseguridad, 48.5 h, agosto 2026.
- **T:** Entender por dónde empiezan los incidentes.
- **A:** Lo que más me quedó: la mayoría arranca por algo simple —alguien con
  más permisos de los que necesita—. Me interesa el control de accesos: quién
  entra a qué y por qué queda registrado.
- **R:** Certificado del curso. **No es experiencia laboral** y lo digo así.

**Versión corta:** "El curso me dejó una idea fija: el incidente suele empezar
en un permiso de más. Por eso me interesa IAM, que es menos vistoso que otros
temas de seguridad y sostiene todo lo demás."

**Lo que NO digo:** que administré Active Directory, LDAP, SailPoint, CyberArk
ni Delinea. Sé qué son; no los usé en producción.

---

## 7. Estudiar y trabajar — UADE + COTO

**Cuándo usarla:** "cómo organizás el tiempo", "por qué tu promedio",
"contame de vos".

- **S:** Tecnicatura Universitaria en Desarrollo de Software en UADE
  (2025–2028), promedio 8.67, trabajando en COTO Digital.
- **T:** Sostener las dos cosas sin que ninguna se caiga.
- **A:** Horarios fijos de estudio, entregas con anticipación, y usar el trabajo
  como laboratorio: lo que veo en la facultad lo pruebo en el proyecto propio.
- **R:** Promedio 8.67 y 2.º año en curso, con trabajo en paralelo.

**Lo que NO digo:** que soy el mejor alumno ni que la facultad es fácil.

---

## Historias que faltan (para completar cuando pase)

- **Un error propio.** El banco no tiene una historia de fracaso real. Hace
  falta una: un ticket que cerré mal, un cierre de caja que no cuadró, un
  deploy que rompió algo. Sin eso, "contame de un error" se responde con una
  debilidad disfrazada y se nota.
- **Un conflicto con un compañero o un cliente enojado.** Para soporte y
  atención al cliente es la pregunta más probable y no hay material.
