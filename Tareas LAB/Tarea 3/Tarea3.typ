= Comportamiento por desarrollar
El objetivo del chatbot es entablar un dialogo con el usuario con la finalidad de dialogar acerca de peliculas y series y brindar datos e información especifíca; como el año, titulo, imagenes, director, genero, entre otros.
= Los intents que utilizan
Algunos de los intents junto con sus expresiones regulares, son los siguientes:

- Intent de bienvenida
  #figure(
    ```python
    {
      'intent': 'bienvenida',
      'regex': [
          r'.*hola.*',
          r'.*buen(a|o)s (dias|tardes|noches).*',
      ],
      'respuesta': [
          '¡Hola Cinéfilo!, ¿de que quieres hablar hoy?',
          '¡Hola! ¿quieres conversar acerca de una película?',
      ]
    },
    ```,
    caption: [
      Intent de bienvenida.
    ]
  )
- Intent de genero:
  #figure(
    ```python
    {
      'intent': 'genero',
      'regex': [
          r'.*(di|da)me un genero.*',
          r'.*(recomienda|sugiere)(|me) un genero.*',
          r'.*que genero prefieres.*',
      ],
      'respuesta': [
          'Aquí está un genero que te puede gustar: ',
          'El genéro que más me gusta es: ',
          'Este es el genero que te recomiendo: '
      ]
    },
    ```,
    caption: [
      Intent de genero.
    ]
  )
- Intent de pelicula:
  #figure(
    ```python
    {
      'intent': 'pelicula',
      'regex': [
          r'.*(di|da)me una pelicula.*',
          r'.*(que|cual) pelicula (me recomiendas|prefieres|te gusta).*',
      ],
      'respuesta': [
          'La pelicula que yo prefiero es: ',
          'Te recomiendo la pelicula: ',
          'Una elección de pelicula sería: '
      ]
    },
    ```,
    caption: [
      Intent de genero.
    ]
  )