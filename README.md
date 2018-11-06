
es un simple juego que consiste en llegar a una meta establecida teniendo diversas opciones cuando se llega a un cierto punto del juego(la mitad), está implementado en python 3.5.

¿Cómo se obtiene el juego?

el juego se obtiene de una forma sencilla, consiste en clonar el repositorio "https://github.com/Rach2520st/laberinto2" en un computador que posea python de preferencia la versión 3.5 y activado el entorno virtual, luego  dentro de la carpeta contenedora del archivo "laberinto2" ejecutar "python lab.py"

¿En qué consiste el juego?

este juego consiste en llegar a una meta establecida mediante diversos caminos aleatorios pero que presentan una solución directa estándar y algunos de estos caminos dificultan al jugador en su camino hacia la meta, aumentando la complejidad del juego, cuando el jugador llega a la mitad del camino aparece un menú que le da cuatro posibles opciones: seguir con el juego, escoger la ruta estándar, llegar lentamente a la meta o tomar la ruta más corta.

¿Cuáles son sus controles?

los principales controles de este juego son la flechas del teclado y cuando el jugador llega a la mitad del laberinto sus controles son los numeros(opciones que le entrega el juego) y enter.

sobre el código:
el programa contiene 4 librerías, tambien contiene 7 funciones que trabajan en la efectividad de este programa.

la función principal contiene diferentes funciones que le permiten jugar al usuario hasta que este llega a la mitad del laberinto y ofrece diversas opciones, la opcion del camino más lento consiste en ir guardando movimientos al azar en un archivo json y luego ejecutar los movimientos en el juego. la opcion del camino estándar consiste en volver a redibujar el laberinto pero con el camino estandar marcado por guiones "-", y la otra opción consiste en reanudar el juego en el mismo lugar en el que se encontraba llamando nuevamente a la funcion juego.
lamentablemente este código no funciona y requiere de arreglos que lo hagan mucho más eficiente.
autor: Rachell Scarlett Aravena Martínez.