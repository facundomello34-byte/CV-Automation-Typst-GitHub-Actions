// =============================================================================
// cv.typ — CV base (el "master"): todo el contenido, todo el diseño.
//
// Es el archivo que se copia para armar una variante. Una variante cambia
// SOLO tres cosas: el `headline`, qué proyectos entran (y en qué orden) y el
// texto del perfil. Nada de `set page`, `set text` ni macros propias.
//
//   #show: cv.with(headline: headline, contact: contacto, links: links)
//
// Compilar:  typst compile cv.typ
// =============================================================================
#import "diseno.typ": *
#import "contenido.typ": *

#show: cv.with(headline: headline, contact: contacto, links: links)

#section("Perfil")[#perfil]

#section("Competencias")[
  #for (i, (label, items)) in competencias.enumerate() {
    if i > 0 { linebreak() }
    [ #text(weight: "bold", fill: petrol)[#label:] #items ]
  }
]

#section("Experiencia")[
  #for e in experiencia { entry(..e) }
]

#section("Proyectos")[
  #for key in ("av", "fleetops", "stock", "chiazza") {
    entry(..proyectos.at(key))
  }
]

#section("Educación")[
  #for e in educacion { row(..e) }
]

#footer(disponibilidad)
