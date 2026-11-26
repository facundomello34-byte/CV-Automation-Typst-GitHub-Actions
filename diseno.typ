// =============================================================================
// diseno.typ — LA interfaz del CV de Facundo Mello.
//
// Este es el único archivo donde se define la parte visual: tipografía, color,
// márgenes, espaciado y las macros de sección. Ninguna variante de CV debe
// redeclarar `set page`, `set text`, `set list` ni escribir su propia versión
// de `section` / `entry`: si algo no entra en una página o no se lee bien, se
// corrige acá y se recompilan todas las variantes.
//
// Base: el diseño del CV "IT" del 11/11/2026 (Lato, azul petróleo, una columna).
// =============================================================================

// --- Paleta ---------------------------------------------------------------
#let petrol = rgb("#17324D")   // títulos y nombre
#let blue = rgb("#2563EB")     // links y bullets
#let gray = rgb("#374151")     // cuerpo
#let light = rgb("#E5E7EB")    // líneas
#let muted = rgb("#6B7280")    // fechas y notas al pie

// --- Medidas tipográficas -------------------------------------------------
#let font-family = ("Lato", "Liberation Sans")
#let body-size = 10.0pt
#let section-size = 10.5pt
#let name-size = 21pt
#let headline-size = 10.4pt
#let contact-size = 8.9pt
#let date-size = 8.8pt
#let note-size = 8.7pt
#let bullet-size = 8.5pt

// --- Aire entre bloques ---------------------------------------------------
// Como el texto es corto (un bullet por línea), la página se regula acá:
// subir `par-leading` y `section-gap` llena el aire que deja el texto.
#let par-leading = 0.62em
#let par-spacing = 0.62em
#let list-spacing = 0.32em
#let section-gap = 0.95em
#let entry-gap = 0.42em

// --- Encabezado -----------------------------------------------------------
// links: array de pares ("Etiqueta", "https://…"), en el orden en que se ven.
#let link-row(links) = {
  let out = ()
  for (i, (label, url)) in links.enumerate() {
    if i > 0 { out.push([ #text(fill: muted)[|] ]) }
    out.push(link(url)[#text(blue)[#label]])
  }
  out.join()
}

#let header(name: "FACUNDO OCTAVIO MELLO", headline: "", contact: "", links: (), body) = {
  align(center)[
    #text(size: name-size, weight: "black", fill: petrol, tracking: 0.01em)[#name]
    #v(-0.22em)
    #text(size: headline-size, weight: "medium", fill: gray)[#headline]
    #v(-0.16em)
    #text(size: contact-size, fill: gray)[#contact]
    #linebreak()
    #text(size: contact-size)[#link-row(links)]
  ]
  v(0.28em)
  line(length: 100%, stroke: 0.6pt + light)
  body
}

// --- Secciones ------------------------------------------------------------
#let section(title, body) = {
  v(section-gap)
  text(size: section-size, weight: "bold", fill: petrol, tracking: 0.08em)[#upper(title)]
  v(-0.42em)
  line(length: 100%, stroke: 0.5pt + light)
  v(0.24em)
  body
}

// --- Entradas (trabajo, proyecto, estudio) --------------------------------
// Una sola macro para las tres: título en negrita, subtítulo en gris, fecha
// al margen derecho y bullets opcionales. `note` es la línea chica de abajo
// (promedio, horas del curso, etc.).
#let entry(title: "", subtitle: none, dates: none, link-url: none, link-label: "demo", bullets: (), note: none) = {
  v(entry-gap)
  block(width: 100%)[
    #text(weight: "bold", fill: petrol)[#title]
    #if subtitle != none [#text(fill: gray)[ · #subtitle]]
    #if link-url != none [
      #h(0.45em)
      #link(link-url)[#text(size: date-size, fill: blue)[#link-label]]
    ]
    #h(1fr)
    #if dates != none [#text(size: date-size, fill: muted)[#dates]]
  ]
  if bullets.len() > 0 {
    list(..bullets)
  }
  if note != none {
    text(size: note-size, fill: muted)[#note]
  }
}

// Variante sin viñetas, para educación: deja la nota pegada al título.
#let row(title: "", subtitle: none, dates: none, note: none) = {
  entry(title: title, subtitle: subtitle, dates: dates, note: note)
}

// --- Cierre ---------------------------------------------------------------
#let footer(txt) = {
  v(0.9em)
  text(size: note-size, fill: muted)[#txt]
}

// --- Documento ------------------------------------------------------------
// Uso: #show: cv.with(headline: "…", contact: "…", links: (…))
#let cv(headline: "", contact: "", links: (), body) = {
  set document(title: "Facundo Octavio Mello · CV", author: "Facundo Octavio Mello")
  set page(paper: "a4", margin: (x: 1.5cm, y: 1.15cm))
  set text(font: font-family, size: body-size, fill: gray, lang: "es", hyphenate: false)
  set par(justify: false, leading: par-leading, spacing: par-spacing)
  set list(
    indent: 0.3em,
    body-indent: 0.25em,
    spacing: list-spacing,
    marker: text(fill: blue, size: bullet-size)[•],
  )

  header(headline: headline, contact: contact, links: links, body)
}
