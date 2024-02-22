#let config(
  autores: (),
  logo: none,
  materia: none,
  titulo: "Titulo del documento",
  simple: false,
  tipo: none,
  palabras-clave: (),
  secciones: (),
  subtitulo: "Subtitulo del documento",
  subtitulo-corto: "Subtitulo corto",
  tema: blue,
  margen: (),
  fecha: datetime.today(),
  url: none,
  doc,
) = {
  show link: it => { text(fill: tema, it) }

  set text(10pt, font: "Noto Sans", lang: "es")
  set document(title: titulo, author: autores.map(autor => autor.nombre))

  let separador = text(fill: gray)[#h(8pt) | #h(8pt)]
  let fechas = if type(fecha) == "datetime" {
    ((titulo: "Entrega", fecha: fecha),)
  } else if type(fecha) == "dictionary" {
    (fecha,)
  } else {
    fecha
  }
  fecha = fechas.at(0).fecha

  set page(
    margin: if simple { auto } else { (left: 25%) },
    header: if not simple {
      locate(loc => block(
        width: 100%,
        {
          if loc.page() == 1 {
            let encabezados = (
              if materia != none { smallcaps(materia) },
              if url != none { link(url) }
            )
            align(left, text(8pt, gray, weight: "semibold",
              encabezados.filter(enc => enc != none).join(separador)
            ))
          } else {
            align(right, text(8pt, gray.darken(50%),
              (
                subtitulo-corto, fecha.display("[day]/[month]/[year]"),
              ).join(separador)
            ))
          }
        }
      ))
    },
    footer: if simple {
      align(center, text(gray.darken(50%),
        counter(page).display("1 de 1", both: true)
      ))
    } else {
      block(
        inset: (top: 8pt),
        stroke: if simple { none } else { (top: 1pt + gray.darken(50%)) },
        width: 100%,
        grid(
          columns: (25%, 75%),
          align(left, text(gray.darken(50%),
            counter(page).display(
              (n, m) => [ Página #n de #m ],
              both: true,
            )
          )),
          align(right, text(gray.darken(50%),
            locate(loc => {
              let f = fecha.display("[day]/[month]/[year]")
              let pie-pagina = if loc.page() == 1 {
                (f, )
              } else {
                (materia, f, )
              }
              pie-pagina.join(separador)
            })
          )),
        )
      )
    },
  )

  if not simple and logo != none {
    place(
      top,
      dx: -33%,
      float: false,
      box(
        width: 27%,
        {
          let type-logo = type(logo)
          if type-logo == content {
            logo
          } else if type-logo == str {
            image(logo)
          } else {
            panic("logo debe ser un contenido o una imagen")
          }
        },
      )
    )
  }

  box(inset: (bottom: 2pt), text(17pt, weight: "bold", fill: tema, titulo))
  if subtitulo != none {
    parbreak()
    box(text(14pt, weight: "semibold", fill: tema.darken(30%), subtitulo))
  }

  if autores.len() > 0 {
    v(0pt, weak: true)
    box(inset: (y: 10pt), {
      autores.map(autor => {
        text(11pt, weight: "semibold", autor.nombre)
        h(2pt)
        link("mailto:" + autor.email)[
          #let email-svg = {
            "<?xml version='1.0' encoding='iso-8859-1'?>"
            "<svg fill='#000000' height='800px' width='800px' version='1.1' id='Layer_1' xmlns='http://www.w3.org/2000/svg'"
            "    xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 330.001 330.001' xml:space='preserve'>"
            "  <g id='XMLID_348_'>"
            "  <path id='XMLID_350_' d='M173.871,177.097c-2.641,1.936-5.756,2.903-8.87,2.903c-3.116,0-6.23-0.967-8.871-2.903L30,84.602"
            "        L0.001,62.603L0,275.001c0.001,8.284,6.716,15,15,15L315.001,290c8.285,0,15-6.716,15-14.999V62.602l-30.001,22L173.871,177.097z'/>"
            "  <polygon id='XMLID_351_' points='165.001,146.4 310.087,40.001 19.911,40'/>"
            "  </g>"
            "</svg>"
          }
          #box(
            height: 1.1em,
            image.decode(email-svg.replace("#000000", tema.to-hex()))
          )
        ]
      }).join(", ", last: " y ")
    })
  }

  place(
    left + horizon,
    dx: -33%,
    dy: -10pt,
    box(width: 27%, {
      if tipo != none {
        show par: set block(spacing: 0em)
        text(11pt, fill: tema, weight: "semibold", smallcaps(tipo))
        parbreak()
      }
      if fechas != none {
        grid(columns: (40%, 60%), gutter: 7pt,
          ..fechas.zip(range(fechas.len())).map((formatted-fechas) => {
            let (d, i) = formatted-fechas
            let weight = "light"
            if i == 0 {
              weight = "bold"
            }
            return (
              text(size: 7pt, fill: tema, weight: weight, d.titulo),
              text(size: 7pt, d.fecha.display("[day]/[month]/[year]"))
            )
          }).flatten()
        )
      }
      v(2em)
      grid(columns: 1, gutter: 2em, ..margen.map(side => {
        text(size: 7pt, {
          if "titulo" in side {
            text(fill: tema, weight: "bold", side.titulo)
            [\ ]
          }
          set enum(indent: 0.1em, body-indent: 0.25em)
          set list(indent: 0.1em, body-indent: 0.25em)
          side.contenido
        })
      }))
    }),
  )

  let secciones = if type(secciones) == content or type(secciones) == str {
    ((title: "Resumen", content: secciones),)
  } else {
    secciones
  }

  if secciones.len() > 0 {
    box(inset: (top: 16pt, bottom: 16pt), stroke: (top: 1pt + gray), width: 100%, {
      secciones.map(abs => {
        set par(justify: true)
        text(fill: tema, weight: "semibold", size: 9pt, abs.titulo)
        parbreak()
        abs.contenido
      }).join(parbreak())
    })
  }
  if palabras-clave.len() > 0 {
    parbreak()
    text(size: 9pt, {
      text(fill: tema, weight: "semibold", "Palabras clave")
      h(8pt)
      palabras-clave.join(", ")
    })
  }
  v(10pt)

  line(stroke: gray, length: 100%)

  doc
}
