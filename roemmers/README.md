# Paquete de postulación a Roemmers

**Fecha:** 11/11/2026
**Estado:** borrador. No se envió ninguna candidatura, correo ni mensaje.

## Qué hay acá

| Archivo | Para qué sirve |
| --- | --- |
| `INFORME.md` | Investigación completa: empresa, vacantes, pasantías, canales, auditoría y plan |
| `postulacion.md` | Correo, mensajes de LinkedIn, respuesta para formularios y seguimiento |
| `Mello_Facundo_CV_IT.pdf` | CV principal final, una página A4, para IT, soporte, QA, análisis funcional y pasantías |
| `Mello_Facundo_CV_IT.docx` | CV principal editable |
| `Mello_Facundo_CV_Tecnologia_Roemmers.pdf` | Copia del CV principal para el paquete de Roemmers |
| `Mello_Facundo_CV_Tecnologia_Roemmers.docx` | Copia editable del CV principal |
| `Mello_Facundo_CV_Pasantias_Roemmers.pdf` | CV B final, una página A4, para pasantías administrativas u operaciones |
| `Mello_Facundo_CV_Pasantias_Roemmers.docx` | CV B editable |
| `CAMBIOS-CV.md` | Auditoría, cambios del rediseño y datos a confirmar |
| `cv_roemmers_texto.md` | Texto de ambos CV para copiar en formularios |
| `cv_master.typ` / `cv_master.docx` | Fuente y salida editable del CV principal rediseñado |
| `cv_roemmers_tech.typ` / `cv_roemmers_admin.typ` | Fuentes Typst de los CV del paquete Roemmers |
| `cv_roemmers_tech.docx` / `cv_roemmers_admin.docx` | Salidas del script de generación |
| `build_cv.py` | Script que genera los CV del paquete Roemmers |
| `build_master_cv.py` | Script que genera el CV principal rediseñado |

## Orden recomendado

1. Leer `INFORME.md`, secciones 0, 3 y 10.
2. Revisar `postulacion.md` y aprobar el correo.
3. Enviar el CV A a `gestionhumanacv@roemmers.com.ar`.
4. Cargar el CV en el Portal de Empleos de UADE.
5. Seguir a Roemmers en LinkedIn y activar la alerta de empleo.
6. Contactar a una sola persona de Gestión Humana, después del correo.

## Para regenerar los CV

```bash
cd roemmers
python3 -m venv /tmp/venv-docx
/tmp/venv-docx/bin/pip install python-docx
/tmp/venv-docx/bin/python build_cv.py
typst compile cv_roemmers_tech.typ
typst compile cv_roemmers_admin.typ
```

Los PDF están ignorados por `.gitignore` (`*.pdf`). Si querés versionarlos, hay que forzar el add o cambiar la regla.
