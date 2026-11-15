---
name: preparar-entrevista
description: >-
  Prepara una entrevista de trabajo para el primer empleo IT de Facundo:
  arma el relato de "contame de vos", elige historias reales del banco (COTO,
  Havanna, Bon Air, el SaaS, el curso de ciberseguridad), prepara respuestas
  STAR sin inventar nada, guion para los gaps y para el inglés técnico, y deja
  un one-pager listo en entrevistas/. Úsala cuando haya una entrevista
  agendada, cuando pidan "preparame para la entrevista de X", "practiquemos",
  "simulacro", o cuando haya que responder "contame de vos" o "¿por qué esta
  empresa?".
---

# preparar-entrevista

Una entrevista para un primer empleo IT no se gana con currículum: se gana
**siendo claro con lo que falta** y mostrando que lo que hay es real. Esta
skill arma eso con material del repo, no con respuestas genéricas.

## Antes de empezar: qué leer

1. `estado-busqueda.md` §1 y §6 — perfil, disponibilidad, pretensión salarial,
   banco de respuestas para formularios.
2. `.pi/voice.md` — cómo habla Facundo. La entrevista suena como las cartas,
   no como un manual de RRHH.
3. `data_es.typ` — experiencia, proyectos, fechas, promedio. **Es la única
   fuente de datos verificable.**
4. La ficha de la oferta: `reports/verificacion-*.md` o
   `reports/abiertas-*.md`. Si no existe, correr antes `evaluar-oferta`.
5. `references/banco-historias.md` y `references/preguntas.md` de esta skill.

Si algo del aviso o del perfil no está en esos archivos, **no lo inventes**:
va `{{dato}}` y se pregunta.

## Paso 1 — entender qué van a evaluar

Del aviso, sacar las 3 o 4 competencias que se van a testear. Ejemplos:

| Puesto | Lo que prueban |
| --- | --- |
| Soporte N1 / Helpdesk | diagnóstico, trato con usuarios, registro de tickets, priorización |
| QA / Testing | método, criterio de calidad, herramienta, cómo reportás un bug |
| IAM / SOC | motivación por seguridad, concepto de mínimo privilegio, honestidad sobre herramientas que no usaste |
| Trainee / Dev jr | stack real, cómo aprendés, qué proyecto propio podés defender |

No preparar 20 respuestas: preparar **5 historias** que cubran esas
competencias. En `references/banco-historias.md` ya están las siete.

## Paso 2 — elegir y adaptar las historias

Para cada competencia, una historia del banco. Adaptar el **énfasis**, nunca los
hechos:

- Soporte: la impresora de COTO, el salón de Havanna.
- Procesos/automatización: el cierre de caja de Bon Air.
- Técnico/dev: el SaaS con FastAPI/Docker/Playwright, el stock en Python.
- Seguridad: el curso de 48.5 h, sin decir que fue experiencia laboral.

Cada historia va en dos versiones: **larga** (~2 min) y **corta** (~60 s). Si no
hay número real para el resultado, se dice "no medí eso" o se deja `{{dato}}`.
Nunca "reduje un 30%" inventado.

## Paso 3 — el relato de "contame de vos" (90 segundos)

Estructura fija, en primera persona:

1. **Quién soy:** estudiante de la Tecnicatura en Desarrollo de Software
   (UADE, 2.º año, promedio 8.67).
2. **Qué hago hoy:** COTO Digital (operación y soporte de primera línea) +
   proyecto propio de SaaS.
3. **Qué sé:** Python, SQL/PostgreSQL, Linux, Docker, Playwright.
4. **Por qué este puesto:** una frase específica del aviso, no "porque me
   interesa la tecnología".
5. **Cierre:** "Estoy buscando mi primer empleo formal en IT y este puesto
   encaja con lo que vengo practicando."

Se escribe una versión y se prueba en voz alta. Si dura más de 2 minutos, se
corta. Si suena a LinkedIn, está mal: tiene que sonar a `.pi/voice.md`.

## Paso 4 — los gaps, dichos sin pedir perdón

La carta ya declara la falta de experiencia en el primer párrafo; la entrevista
hace lo mismo. Fórmula:

> "No hice X en producción. Sé qué es y para qué sirve. Lo que sí hice fue Y,
> que es lo más parecido que tengo. Aprender X con documentación y práctica es
> lo que vengo haciendo con cada tecnología del CV."

Gaps típicos por puesto: Jira/ServiceNow, Active Directory/LDAP,
SailPoint/CyberArk, SIEM, GCP/BigQuery, Java, inglés oral. Escribir el guion de
cada uno en el archivo de la entrevista.

**Nunca** decir "sí, lo usé" para pasar el filtro. Si el puesto lo exige como
excluyente, no era para este momento.

## Paso 5 — el inglés, sin maquillaje

Si el proceso puede tener una parte oral:

- Guion de cinco frases en `references/preguntas.md` → "En inglés".
- Práctica: 3 preguntas probables respondidas en voz alta, en inglés simple.
  No hace falta acento: hace falta claridad y no quedarse mudo.
- Plan B: pedir responder en español y ofrecer un resumen corto en inglés. Es
  mejor que improvisar y trabarse.
- El CV y `estado-busqueda.md` dicen inglés técnico. La entrevista no puede
  contradecir eso.

## Paso 6 — preguntas para hacer

Elegir **tres** de `references/preguntas.md`. Siempre al menos una sobre
modalidad/horario y una sobre cómo es el día a día. Preguntar es parte de la
entrevista: también se evalúa.

## Paso 7 — el one-pager

Escribir `entrevistas/<empresa>-<YYYY-MM-DD>.md`:

```markdown
# Entrevista — {PUESTO} en {EMPRESA}

**Cuándo:** {fecha, hora, canal} · **Con quién:** {nombre/rol si se sabe}
**Oferta:** {URL} · **Verificación:** reports/verificacion-...md

## Lo que van a evaluar
1. ... (del aviso)

## Relato de "contame de vos" (90 s)
{texto completo, para leer en voz alta}

## Historias elegidas
### {competencia}
- **Historia:** {n del banco}
- **Larga (2 min):** ...
- **Corta (60 s):** ...

## Los gaps
| Gap | Guion | Qué NO decir |
| --- | --- | --- |

## Preguntas probables
| Pregunta | Respuesta en bullets | Historia |
| --- | --- | --- |

## Preguntas para hacerles
1. ...

## Inglés (si aplica)
- Frases clave
- Respuestas cortas ensayadas

## Checklist 24 h antes
- [ ] Releer aviso, CV y carta: que los datos coincidan
- [ ] Probar cámara, micrófono y conexión (si es virtual)
- [ ] Confirmar dirección y viaje (si es presencial): Castelar → ...
- [ ] Llevar CV impreso y anotador
- [ ] Ropa lista
- [ ] Dormir. No estudiar hasta las 3 AM
```

## Paso 8 — simulacro (opcional, pero recomendado)

Si el usuario quiere practicar, hacer de entrevistador:

1. Una pregunta por vez, sin dar la respuesta.
2. Escuchar la respuesta completa.
3. Devolver tres cosas: qué sonó sólido, qué quedó vago, qué dato faltó.
4. Repetir solo la respuesta floja.

No dar una respuesta modelo larga: él tiene que decirla con sus palabras. Si
una respuesta inventa algo que no está en el CV, frenar y corregirlo en el acto.

## Reglas duras

1. **Nada inventado.** Ni herramientas, ni métricas, ni clientes, ni "lideré un
   equipo". Todo sale de `data_es.typ` o de una respuesta textual de Facundo.
2. **No contradecir el CV.** Fechas, promedio, disponibilidad, nivel de inglés.
3. **Métricas:** si no hay, se dice "no lo medí". Nunca un porcentaje estimado.
4. **La entrevista también es para preguntar.** No es un examen.
5. **Un archivo por entrevista.** No reutilizar el one-pager de otra empresa
   sin cambiar al menos el puesto, la empresa y las preguntas.

## Archivos

```
references/banco-historias.md   las 7 historias reales, con versión larga y corta
references/preguntas.md         preguntas por tipo de puesto + inglés + para hacerles
```
