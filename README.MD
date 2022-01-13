A tener en cuenta para correr el programa

El proyecto está hecho 100% en python, creé un entorno virtual con Pycharm en el cual instalé el siguiente paquete: https://github.com/johejo/inputimeout.
El mismo permite poner un limite de tiempo al momento de leer el input del usuario. Una vez asegurado dicho paquete basta con correr el archivo main.py para correr la aplicación de consola (la base de datos se crea sola, preferí dejar escrito el código necesario para crear y llenar la misma que estarla subiendo github). 

Una breve explicación de la lógica del programa

El guardado de datos funciona mediante una base de datos sql gracias sqlite3.
El proyecto esta levemente basado en el patrón de diseño MVC, teniendo una entidad modelo que se encarga del manejo de datos, una entidad view  que se encarga de mostrar los mismos y el resto de las entidades reprsentando el control. 

Resumen del funcionamiento lógico: Al momento de iniciar el programa uno debe ingresar su nombre, esto se guardará en una instancia de la clase Player. El jugador puede navegar por la aplicación gracias a las distintas instancias de la clase Menu, la cual permite mostrar en pantalla una lista de opciones y seleccionar la deseada. Al momento de comenzar a jugar se iniciará la lógica de una instancia de la clase Game. Esta clase seleccionará al azar una de las categorías disponibles. La clase Game contiene varias instancias de la clase Round. Durante cada round se muestran preguntas (clase Question) que el jugador deberá responder. Al final de cada ronda se asigna puntaje en caso de que corresponda. Una vez finalizada la partida el jugador puede navegar hasta el menú Scoreboard, en el cual se deja un registro de todo puntaje mayor a cero obtenido por cada jugador que haya participado.

Lamentablemente el código está muy desordenado (desde ya pido disculpas a lo que verán sus ojos), un síntoma del querer abarcar demasiado y tener que terminar cortando esquinas a último momento.

Nota: en caso de que salga seleccionada la categoría "deportes" el sistema crashea.
