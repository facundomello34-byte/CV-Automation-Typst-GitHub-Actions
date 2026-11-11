# Rediseño del CV principal: cambios y control de calidad

**Archivo final:** `Mello_Facundo_CV_IT.pdf` y `Mello_Facundo_CV_IT.docx`
**Fecha:** 11/11/2026

## 1. Auditoría del CV anterior

El CV anterior era correcto en contenido, pero visualmente plano y con algunos puntos flojos:

- Tipografía Liberation Sans, sin jerarquía cromática.
- Encabezados en mayúsculas sin color ni separadores claros.
- Perfil de cuatro líneas densas, con poca respiración.
- Experiencias con viñetas que empezaban con sustantivos ("Operación diaria", "Manejo y soporte", "Responsable de caja").
- La palabra "tickets" aparecía sin aclarar que eran operativos, no de soporte IT.
- Los proyectos usaban descripciones más cercanas a un informe que a un CV.
- El encabezado mostraba URLs largas en lugar de enlaces con rótulos simples.
- No había metadatos de PDF ni hipervínculos con etiquetas limpias.

## 2. Rediseño visual

- **Tipografía:** Lato en todo el documento. Nombre en Lato Black, 21 pt. Encabezados en Lato Bold, 10,5 pt. Texto principal en Lato Regular, 10 pt.
- **Paleta:** azul petróleo `#17324D` para nombre, encabezados y empresas/proyectos; azul tecnológico `#2563EB` solo para enlaces y viñetas; gris oscuro `#374151` para el cuerpo; gris claro `#E5E7EB` para separadores; fondo blanco.
- **Jerarquía:** nombre centrado, subtítulo profesional, contacto en una línea, enlaces con rótulos `LinkedIn | GitHub | AVENOR`, regla fina bajo el encabezado.
- **Secciones:** títulos en mayúsculas, petróleo, con regla fina gris. Empresas y proyectos en negrita. Fechas alineadas a la derecha en gris.
- **Viñetas:** punto azul, texto gris, sangría uniforme.
- **Formato:** una página A4, una sola columna, sin foto, sin tablas, sin gráficos, sin barras de progreso, sin iconos.

## 3. Cambios de contenido

### Perfil

Se reescribió en cuatro líneas. Ahora dice:

- Estudiante de Desarrollo de Software en UADE, promedio 8.67.
- Experiencia operativa en sistemas de gestión, incidencias y automatización.
- Python, SQL, Linux, Git y Docker; SaaS propio con FastAPI, PostgreSQL y Playwright.
- Búsqueda de Trainee, Junior o pasantía en desarrollo, soporte IT, QA, análisis funcional o automatización.
- Inglés técnico en curso con clases particulares.

No dice "apasionado por la tecnología", "experto" ni "desarrollador profesional".

### Experiencia

Tres experiencias, tres viñetas cada una, con verbos de acción:

- **COTO Digital:** PDA, sistemas internos, comprobantes, tickets operativos, pedidos, fallas de impresoras y equipos, optimización de procesos.
- **Bon Air:** FUDO POS, ventas, inventario, cierres de caja, incidencias del sistema, automatización de registros.
- **Havanna:** MAXIREST, validación de información, asistencia técnica básica a computadoras, caja y operación.

Se aclaró "tickets operativos" para no confundirlos con tickets de soporte IT.

### Proyectos

Tres proyectos, tres viñetas cada uno:

- **AVENOR:** prototipo funcional de SaaS, lógica de negocio, PostgreSQL, FastAPI, módulos de pedidos e inventarios. Stack completo y pendientes de testing y despliegue.
- **Sistema de Stock Automatizado:** aplicación académica en Python, estructuras de datos, lógica de negocio, productos, clientes, ventas y reportes.
- **Chocolates Chiazza:** análisis de procesos, FODA, relevamiento, requerimientos funcionales, seguridad mínima, reportes y alertas por WhatsApp o Telegram. Aclarado como propuesta académica, no implementada ni desplegada.

### Competencias

Cuatro grupos, sin duplicaciones:

1. Desarrollo y bases de datos.
2. Soporte técnico y sistemas.
3. QA, análisis y automatización.
4. Herramientas y tecnologías.

No se agregaron SAP, Excel, Jira, ITIL, Active Directory, Intune, SCCM ni Power BI.

### Educación, certificaciones e idiomas

- Tecnicatura Universitaria en Desarrollo de Software, UADE, 2025 a 2028 (en curso), promedio 8.67, graduación estimada fines de 2028.
- Inglés técnico con clases particulares, 2026 a en curso.
- Fundamentos de Ciberseguridad, curso certificado, agosto 2026, 48.5 h.

### Contacto

- Castelar, Buenos Aires.
- Teléfono y email reales.
- Enlaces con rótulos `LinkedIn`, `GitHub` y `AVENOR`, todos hipervínculos funcionales.

## 4. Control de calidad

| Chequeo | Resultado |
| --- | --- |
| PDF de una página A4 | Sí |
| DOCX de una página A4 | Sí |
| Una sola columna | Sí |
| Sin tablas, imágenes ni gráficos | Sí |
| Texto seleccionable | Sí, verificado con `pdftotext` |
| Fuentes incrustadas en el PDF | Sí, Lato Black, Bold, Medium y Regular |
| Hipervínculos del PDF | Sí, verificados con `pdftohtml` |
| Hipervínculos del DOCX | Sí, verificados en `document.xml.rels` |
| Metadatos de PDF | Título y autor configurados |
| Fechas y cargos coherentes | Sí, según el CV original |
| Información inventada | No |
| Experiencia IT inflada | No |
| Palabras clave ATS | soporte técnico, QA, análisis funcional, Python, SQL, Linux, Docker, Git, Playwright, PostgreSQL, FastAPI, requerimientos, documentación, inventarios |
| Legibilidad visual | Revisada en PDF y en la conversión del DOCX |

## 5. Datos que necesitan confirmación

1. **Año de Chocolates Chiazza:** quedó sin fecha porque no se informó. Si fue 2025, se agrega.
2. **Nivel de inglés:** el CV dice "en curso con clases particulares". Si ya hay un nivel medido (A2, B1, B2), conviene reemplazarlo por el nivel real y la certificación, si existe.
3. **Promedio 8.67:** se conserva el dato del CV original. Confirmar que sigue siendo el promedio actual.
4. **Graduación estimada:** se usa "fines de 2028" según el estado de búsqueda del repositorio. Confirmar que sigue siendo la estimación.
5. **LinkedIn:** se usa `linkedin.com/in/facundo-octavio-mello-ferreira-8a4206265`. Confirmar que es el perfil correcto.
6. **AVENOR:** el CV dice que quedan pendientes la estrategia de testing y el despliegue productivo. Confirmar que sigue así.
7. **Tickets operativos en COTO:** se usó esa expresión para reflejar la emisión y el seguimiento de tickets comerciales/operativos, no tickets de mesa de ayuda. Confirmar que la descripción es correcta.

## 6. Archivos

- `Mello_Facundo_CV_IT.pdf`: CV principal final.
- `Mello_Facundo_CV_IT.docx`: versión editable.
- `Mello_Facundo_CV_Tecnologia_Roemmers.pdf`: copia del CV principal para el paquete de Roemmers.
- `cv_master.typ`: fuente Typst.
- `cv_master.docx`: salida editable del generador.
- `build_master_cv.py`: script que genera el CV desde los datos.
