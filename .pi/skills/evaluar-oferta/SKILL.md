---
name: evaluar-oferta
description: >-
  Verifica un aviso de empleo antes de gastar una carta: baja la descripción
  completa, detecta seniority real, años pedidos, nivel de inglés, modalidad,
  zona y postulantes, y devuelve un veredicto (APLICAR / APLICAR CON RIESGO /
  NO GASTAR CARTA) con el motivo y los gaps que la carta tiene que nombrar.
  Úsala cuando haya que revisar una oferta, decidir si vale la pena postular,
  o cuando el usuario diga "verificá este aviso", "¿me conviene postular?",
  "analizá esta oferta", "revisá las de hoy" o pegue una URL de LinkedIn,
  Bumeran o Computrabajo.
---

# evaluar-oferta

El embudo de este repo se corta entre leer el aviso y mandar el CV: 647
ofertas vistas, 1 postulada. El bot encuentra y el filtro puntúa por palabra
clave, así que un "Jr" en el título alcanza para que una oferta de 3 años
quede arriba. Esta skill hace el paso que hoy se hace a mano en
`reports/abiertas-*.md`: leer el aviso entero y decidir con datos.

No escribe cartas, no postula y no manda nada. Verifica.

## Antes de empezar: el perfil

Leé, en este orden:

1. `estado-busqueda.md` §1 — ubicación, inglés, estudios, disponibilidad.
2. `scripts/perfil_filtro.json` — stack y empresas (solo como referencia).
3. `reports/abiertas-YYYY-MM-DD.md` más reciente — si la oferta ya está
   verificada, no la vuelvas a hacer: actualizá postulantes y fecha.

Si hay conflicto entre esos archivos y esta skill, **gana `estado-busqueda.md`**.
Es el documento vivo. Y si cambia algo del perfil (nuevo curso, mudanza,
disponibilidad), decilo en la respuesta y proponé actualizar ese archivo.

## Paso 1 — traer el aviso completo

```bash
S=.pi/skills/evaluar-oferta/scripts
python3 $S/oferta.py URL                 # ficha + señales + descripción
python3 $S/oferta.py URL1 URL2 URL3      # lote
python3 $S/oferta.py URL --json          # campos sueltos, para leer
python3 $S/oferta.py - --cuerpo < aviso.txt
```

- **LinkedIn**: usa la API guest (`/jobs-guest/jobs/api/jobPosting/<id>`), sin
  login. Trae título, empresa, ubicación, fecha, **postulantes** y el criterio
  de seniority del propio LinkedIn. Tarda menos de un segundo.
- **Lever, Greenhouse, Workday, sitios propios**: fetch directo y HTML a texto.
- **Bumeran y Computrabajo**: son SPA con Cloudflare. El script te va a avisar.
  Ahí pasá por la skill `web-search` (`search.sh --url '<URL>'`). Si tampoco
  sale, pedile al usuario que pegue el texto del aviso. **No inventes el
  contenido ni completes con lo que "suele" decir un aviso parecido.**

Si el aviso no tiene URL (te lo pasaron por WhatsApp, o lo viste en un portal
sin link), pegá el texto con `-` o `--archivo`.

## Paso 2 — leer el cuerpo, no el título

El script marca señales, pero el veredicto lo das vos leyendo la descripción.
Estos son los datos que importan:

| Dato | De dónde sale | Ojo con |
| --- | --- | --- |
| Seniority real | "Requisitos" del aviso | El criterio de LinkedIn miente: dice "Associate" para un puesto de 0 a 2 años y "Entry level" para uno de 3 |
| Años pedidos | "X años de experiencia" | "0 a 2 años", "sin experiencia" y "recién recibido" son puerta abierta |
| Inglés | Requisitos y "nice to have" | Distinguí **oral** de **lectura de documentación**. No es lo mismo y es el filtro que más te saca ofertas |
| Estudios | Requisitos | "Estudiante avanzado" o "próximo a recibirse" es excluyente: vas por el 2.º año de 4 |
| Modalidad | Descripción | "Híbrido" sin decir cuántos días es una pregunta para el reclutador, no un dato |
| Zona | Ubicación + cuerpo | "Buenos Aires" a secas es ambiguo: puede ser CABA o Provincia. Anotá "confirmar sede" |
| Vigencia | Fecha + "ya no acepta" | LinkedIn deja avisos viejos con el botón muerto |

## Paso 3 — los cinco filtros duros

Cada uno da **pasa**, **no pasa** o **duda**. Un solo "no pasa" alcanza para
`NO GASTAR CARTA`, sin importar cuánto puntúe el resto.

| # | Filtro | No pasa | Duda |
| --- | --- | --- | --- |
| 1 | **Inglés** | pide intermedio/avanzado **y** entrevista oral, o "excluyente" | pide inglés pero solo para leer documentación, o el nivel no está claro |
| 2 | **Seniority y años** | pide 3+ años, o "semi senior/ssr/senior", o "experiencia previa en el sector" | pide 1-2 años sin decir "excluyente" |
| 3 | **Estudios** | "estudiante avanzado", "próximo a recibirse", "egresado/graduado" | pide carrera afín sin aclarar el año |
| 4 | **Distancia y modalidad** | presencial en Pilar, Escobar, Quilmes, La Plata, Ezeiza o Canning (sin auto) | híbrido en Vicente López / San Isidro / Martínez; presencial con horario que choca con COTO |
| 5 | **Vigencia y competencia** | aviso de +30 días, o "ya no acepta postulaciones" | +250 postulantes para un puesto de 0 años, o fecha dudosa |

Dos aclaraciones que evitan falsos negativos:

- **"Buenos Aires" a secas** no es una duda: el aviso puede ser CABA o
  provincia. Anotá "confirmar sede" como bullet y seguí. La duda es para zona
  norte o para una dirección concreta que te suma más de una hora.
- **Entre 100 y 250 postulantes** es una nota de competencia, no una duda. Un
  internship de IBM con 200 es normal; 200 para un puesto especializado, no.

Sobre el inglés: es tu filtro más caro. En la verificación del 11/11, **11 de
20 avisos** lo pedían intermedio o avanzado. Si el aviso dice "inglés
intermedio" y el día a día es ticket escrito, es `duda`, no `no pasa`. Si dice
"entrevista en inglés" o "fluido", es `no pasa`. No lo maquilles.

## Paso 4 — el fit, sin mentirte

Cuando ningún filtro duro falla, puntuá sobre 100:

- **Requisitos excluyentes (60)**: cuántos cumplís de los que el aviso marca
  como obligatorios. Cumplido = 1, parcial = 0.5, gap = 0.
- **Stack y experiencia (25)**: cuánto de lo que pedís sabés hacer de verdad,
  con evidencia en el CV (`data_es.typ`) o en un proyecto.
- **Logística (15)**: distancia, modalidad, horario compatible con COTO.

El número no rescata un excluyente. Si el fit da 85% pero pide "estudiante
avanzado", el veredicto es `NO GASTAR CARTA` y el 85% se muestra igual, para
que se vea que el problema no fue el fit.

**Nunca inventes un porcentaje de match.** Si falta información para calcular,
poné `?` en el criterio y bajá el veredicto a `APLICAR CON RIESGO` con la
pregunta concreta para el reclutador.

## Paso 5 — veredicto

| Veredicto | Cuándo | Qué sigue |
| --- | --- | --- |
| ✅ **APLICAR** | 70+ puntos y ningún filtro duro fallado | Escribir la carta o adaptar una existente |
| ⚠️ **APLICAR CON RIESGO** | 55-69 puntos, o un filtro en `duda`, o +250 postulantes | Decir el riesgo en una frase y qué habría que confirmar antes de mandar |
| ❌ **NO GASTAR CARTA** | Cualquier filtro duro en `no pasa`, o <55 puntos | Una línea con el motivo. Nada más |

El veredicto se escribe siempre con el motivo en una frase. "No" sin motivo no
sirve: la próxima sesión vuelve a evaluar la misma oferta.

## Paso 6 — la ficha

Mostrá en el chat el veredicto, el fit y tres bullets (por qué sí, qué gap
nombrar, qué confirmar). Después agregá la ficha completa al final de
`reports/verificacion-YYYY-MM-DD.md` (creá el archivo si no existe) con este
formato:

```markdown
## {EMPRESA} — {PUESTO}

**Veredicto:** ✅ APLICAR · **Fit:** 78% · **Verificado:** 15/11 13:40
**URL:** ...
**Publicada:** 6/11 (~9 días) · **Postulantes:** 193 · **Zona:** CABA (riesgo bajo)
**Modalidad:** híbrido (3 días oficina, sin confirmar)

| Filtro | Estado | Evidencia |
| --- | --- | --- |
| Inglés | ✅ pasa | "English is not required"; sólo lectura de documentación |
| Seniority | ✅ pasa | "sin experiencia previa", programa de internship |
| Estudios | ✅ pasa | "estudiante en curso" |
| Distancia | ✅ pasa | CABA, Retiro, Sarmiento directo |
| Vigencia | ⚠️ duda | 193 postulantes y 9 días de publicado |

**Fortalezas:** ...
**Gaps que la carta tiene que nombrar:** ...
**Confirmar antes de mandar:** ...
```

Al final del archivo, una tabla resumen con todas las verificadas del día,
ordenadas por veredicto y después por fit. Si la oferta ya figuraba en un
`abiertas-*.md`, actualizá postulantes y fecha en esa tabla en vez de
duplicarla.

**No edites `estado-busqueda.md` sin pedir ok**: lo leen otras sesiones y es
fácil desincronizar el plan de la semana. Proponé la fila y esperá.

## Paso 7 — el pase a la carta

Si el veredicto es APLICAR o CON RIESGO, cerrá con esto:

1. Qué carta usar: una existente (`carta_*.typ`), una variante de
   `carta_generica.typ` (QA / DevOps / SOPORTE) o una nueva.
2. Los **2 o 3 gaps** que la carta tiene que nombrar sin mentir.
3. Si pide inglés y no es excluyente, si conviene mandar `cv_en.pdf` y
   `carta_*.typ` en inglés.
4. Recordá que el texto pasa por `humanizar-textos` y `typst compile` antes de
   enviarse. Eso no lo hace esta skill.

## Casos que ya nos mordieron

| Caso | Lección |
| --- | --- |
| COTO — "Analista de control de calidad" | "Calidad" no es QA de software: era calidad de alimentos (BPM, POES, MIP). Leé el cuerpo |
| Stefanini — Data Support Analyst Jr | El título decía "Jr", el cuerpo pedía "estudiantes avanzados próximos a finalizar (excluyente)" |
| PwC — Associate IAM | Dos avisos del mismo puesto (4488473548 y 4435845749): gana el de menos postulantes |
| DataXstream — IT Support Tier 1 | Tenía carta lista y el aviso ya no aceptaba solicitudes. Verificá vigencia antes de escribir |
| Accenture — DevOps | El filtro la puntuó alto, el aviso pedía 2-4 años en redes. El scoring por keyword no ve seniority |
| Nubax — SOC Jr | "Jr" de verdad, pero Vicente López son ~1 h 20 desde Castelar. El fit técnico no compensa 2 h 40 por día |

## Reglas duras

1. **No inventar.** Ni el contenido del aviso, ni la fecha, ni los postulantes.
   Si no lo pudiste bajar, decilo y usá el fallback.
2. **Citar el fragmento** que justifica cada filtro. Sin cita, es opinión.
3. **Anotar la hora** de la verificación: los postulantes y la vigencia cambian
   en horas.
4. **No postular, no enviar, no completar formularios.** Esta skill termina en
   el veredicto y la ficha.
5. **Un aviso, una ficha.** No resumas cinco ofertas en un párrafo: cada una
   tiene su motivo.

## Archivos

```
scripts/oferta.py       baja el aviso y saca ficha + señales (stdlib, sin deps)
scripts/oferta.py --json  campos para procesar
```
