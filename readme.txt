# Documentación para Evidencia de Proyecto de Semana Tec: TC1001S.121 
## ITESM C. Puebla 
* André Rossell Manrique A01736035
* Cruz Daniel Pérez Jiménez A01736214
* Luis Felipe Hernández Flores A01735939
----
# Actividad 1. Pintado:
El juego "Paint" es más que nada un espacio en el que los usuarios pueden
dibujar figuras basado en clics. Mediante el teclado se pueden elegir
distintas formas y colores para variar los diseños realizados. 
Para hacer este funcionamiento posible, se definen diversas funciones que
corresponden al dibujado de las figuras que el juego ofrece. 
Comenzamos por line, que recibiendo como argumentos una coordenada de 
inicio y una de fin, traslada el píncel virtual con el que se realiza 
el dibujado sobre el ambiente gráfico hacia el punto de comienzo del 
trazado de la línea pedida por el usuario mientras lo tiene levantado para
evitar trazos indeseados. Lo baja en la posición inicial para luego
trasladarse a la posición final, con ello dibujado el segmento requerido 
por el usuario. 
Un protocolo similar sucede con el resto de figuras para las cuales se
implementa función de dibujado: cuadrado, círculo, rectángulo y 
triángulo; además contamos con la función tap, que almacena los clics del
usuario para poder enviar a las funciones de dibujado las coordenadas
de inicio y fin de trazado. 
Después de la definición de estas funciones auxiliares, en el programa
principal se inicializa el ambiente gráfico y se comienza la 
recepción de entradas para poder comenzar el dibujado.

# Actividad 2. Vibora:
El juego de la víbora consiste de darle al jugador el control de una víbora
en un ambiente 2D en donde va cazando objetivos para alimentarse. Mientras
más coma, más puntaje acumula pero, al mismo tiempo, su cuerpo se enlarguece
de manera que el jugador debe maniobrar para evitar comer su propia cola. 
Después de establecer las posiciones iniciales de la serpiente y la comida,
así como la dirección de la serpiente, se comienzan a definir las funciones de
control para las rutinas del juego. 
La funcion change, por ejemplo, es un auxiliar para actualizar la direccion de la serpiente. 
Inside se asegura de que la cabeza de la serpiente no abandone los límites del juego,
tiene una función análoga insidefood que garantiza que la comida nunca
se salga del escenario. 
La más importante es la función move, que, respondiendo a la posición de la
serpiente, valida su cambio de posición con su dirección actual y hace
los chequeos necesarios para garantizar que no ha colisionado. Además,
chequea la posición de la comida para determinar si la cabeza de la
serpiente está en la comida, para lo cual estará reubicando la comida
y haciendo a la serpiente crecer. 
Posterior a estos cálculos es que se pasa al dibujado de la serpiente completa y
de la comida, reflejando las actualizaciones que se hicieron a sus posiciones
e incluso tamaño, en el caso de la serpiente. 
La función de moveComida actualiza constantemente la posición de la
comida y la hace moverse continuamente para aumentar la dificultad del juego . 
Finalmente, el programa principal recibe los inputs del usuario para 
realizar cambios en la dirección de la serpiente y llama a las funciones
de control del resto de la escena para que el flujo del programa persista. 

# Actividad 3. Pacman:
El videojuego Pac-Man consiste de dar al jugador el control de Pac-Man, 
un personaje capaz de moverse en un tablero bidimensional de tipo laberito
con el objetivo de comer todas las pastillas dispuestas el él. El obstáculo 
es que en el tablero hay fantasmas que, de colisionar con el personaje, 
causarían el final del juego. 
Para crear el tablero donde pueden transitar los personajes se utiliza una
matriz de adyacencia en la que se declaran como 0 las intersecciones por
donde no pueden pasar y como 1 las intersecciones en las que sí.
Se definen funciones auxiliares como square para dibujar cuadrados con los 
que se marcan las divisiones del tablero, u offset que reduce los puntos para
adecuarlos a un marcador de tablero. 
La funcion valid calcula una posicion point y la adapta a las dimensiones 
del tablero, mientras que world es el dibujado general del mundo con 
cuadrados de divisón y puntos de pastillas para que Pac-Man coma. 
Nuevamente se cuenta con una función move, que ajusta la posición de
los objetos del tablero: el Pac-Man y los fantasmas, analizando la posición
del Pac-Man para registrar si come pastilla en su ubicación, actualizar 
la puntuación y desaparecer a la pastilla. Adicionalmente, realiza
el ajuste en la dirección de los fantasmas para que estos tomen dirección
hacia el Pac-Man y validan si se ha generado una colisión entre Pac-Man y 
los fantasmas para detener la ejecución del juego. 
Finalmente, la función de control de movimiento de pac-man valida que un intento
de cambio de dirección sea posible para la posición en la que se encuentre.
En la función principal se encuentran las declaraciones usuales del ambiente
gráfico, la designación de la ubicación del puntaje y se abre la detección de
input del usuario para realizar el cambio de dirección. Por último, se llama
a world() y a move() para comenzar el loop de ejecución. 

# Actividad 4. Cannon:
La mecánica principal del juego de Tiro Libre consiste en que el
usuario haga clic en algun lugar de la pantalla para generar un tiro
parabólico. Durante toda la ejecución hay diversas bolas azules flotando
a través de la pantalla y el objetivo es usar el tiro parabólico para
desaparecerlas. Después de realizar la declaración de valores iniciales
para los vectores usados en el programa, se pasa a la declaración de funciones
de control y auxiliares para las rutinas.
La función tap detecta el clic del usuario para generar un disparo en esa
dirección, validando que no haya ya un disparo todavía en el aire. 
La función inside es una función auxiliar que detecta si un par de coordenadas
se encuentra adentro del tablero y regresa un booleano que representa la respuesta.
Draw, una de las rutinas principales, genera el dibujado del proyectil 
en cada llamada y de la misma forma de los objetivos. Sus posiciones
son variables globales dado que se deben actualizar y seguir dibujando para
reflejar su movimiento. 
La función de move realiza los calculos necesarios para desplegar el numero
aleatorio de targets y para calcular el cambio de posicion del proyectil, así 
como reflejar el cambio constante sobre el entorno. 
Ya en la función principal, se abre la recepción de input por mouse y se llama a 
la función de movimiento, que a su vez llama a draw, para comenzar el ciclo de
ejecución del entorno.

# Actividad 5. Memory:
El juego de memoria consiste de la dinámica del juego comúnmente apodado
"Memorama". El jugador debe explorar "cartas" volteadas que tienen números detrás
y recordando las posiciones de algunas, ir encontrando pares iguales para dejar
los pares volteados y poco a poco revelar la imagen escondida. 
El código para ello empieza por definir variables de estado y ambiente y
procede a definir las funciones auxiliares y de rutina que estarán ayudando
a la ejecución del programa. 
La primera de ellas es square, que dibuja los cuadrados blancos en las posiciones
de cada una de las tarjetas. Le sigue index, que convierte pares ordenados
en recuadros de la distrbución generada para las tarjetas. La función de
xy, por su parte, realiza el proceso contrario.
Resta tap, que basado en las coordenadas del clic de un usuario, encuentra 
la tarjeta asociada y la voltea. Esta condicionada de manera que 
cada intento se registre en un contador y detecte cuando dos taps
consecutivos encuentren un par de tarjetas con valores iguales. Al encontrar
un par de tarjetas, imprime en pantalla el numero de tarjetas descubiertas y,
cuando el usuario ha ganado el juego, imprime una leyenda de felicitación. 
Por último está la función draw, que se encarga de dibujar el escenario general, 
monta la imagen del auto detras de las tarjetas y rellena los espacios de 
los pares que no han sido descubiertos. Además, si hay una tarjeta seleccionada, 
escribe sobre ella su valor asociado para poder simular que está "volteada".
La función principal se encarga de inaugurar el ambiente gráfico y llamar a las
rutinas de ejecución para poder iniciar el ciclo del programa. 

