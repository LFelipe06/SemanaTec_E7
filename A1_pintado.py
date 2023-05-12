#Se importan las funciones de los módulos correspondientes
from turtle import *
from freegames import vector
import math

#Se define la función para el dibujado de una línea recta. La función up() hace que no se trace
# mientras el cursor se posiciona en las coordenadas de inicio. La función down() hace que se 
# trace mientras el cursor está en movimiento.
def line(start, end):
    "Draw line from start to end."
    up()
    #Se trazlada el cursor de dibujado a las coordenadas start.x y start.y
    goto(start.x, start.y)
    down()
    #Se trazlada el cursor de dibujado a las coordenadas end.x y end.y
    goto(end.x, end.y)

#Se define la función para el dibujado de un cuadrado. La función up() hace que no se trace
# mientras el cursor se posiciona en las coordenadas de inicio. La función down() hace que se 
# trace mientras el cursor está en movimiento.
def square(start, end):
    "Draw square from start to end."
    up()
    #Se trazlada el cursor de dibujado a las coordenadas start.x y start.y
    goto(start.x, start.y)
    down()
    #begin_fill() iniciara la función de rellenado de la figura dibujada 
    begin_fill()
    #El ciclo for trazará una línea recta de largo igual a la diferencia entre start.x y end.x .
    #Después del trazado, la dirección de dibujado rota 90 grados para posteriormente repetir el ciclo
    for count in range(4):
        forward(end.x - start.x)
        left(90)
    #Se llama a la función end_fill(), esta rellena la figura trazada
    end_fill()

#Se define la función para el dibujado de un circulo relleno. La función up() hace que no se trace
# mientras el cursor se posiciona en las coordenadas de inicio. La función down() hace que se 
# trace mientras el cursor está en movimiento.
def circle(start, end):
    "Draw circle from start to end."
    up()
    #Se desplaza el cursor al punto medio entre las coordenadas del tap inicial y final
    goto((start.x+end.x)/2,(start.y+end.y)/2)
    down()
    #Se calcula el diametro del circulo a trazar
    diametro=math.sqrt(math.pow(end.x-start.x,2)+math.pow(end.y-start.y,2))
    #Se traza el circulo con diametro delimitado por tap inicial y final
    dot(diametro, "black")

#Se define la función para el dibujado de un rectángulo. La función up() hace que no se trace
# mientras el cursor se posiciona en las coordenadas de inicio. La función down() hace que se 
# trace mientras el cursor está en movimiento. La función left() rota la dirección de trazado 
# el numero de grados declarado en su parámetro. La función forward() traslada el cursor la 
# distancia equivalente al valor declarado en su parámetro.
def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    #Se posiciona el cursor en las coordenadas del tap inicial
    goto(start.x,start.y)
    down()
    forward(end.x-start.x)
    left(90)
    forward(end.y-start.y)
    left(90)
    forward(end.x-start.x)
    left(90)
    forward(end.y-start.y)
    left(90)

#Se define la función para el trazado de un triángulo. La función up() hace que no se trace
# mientras el cursor se posiciona en las coordenadas de inicio. La función down() hace que se 
# trace mientras el cursor está en movimiento.
def triangle(start, end):
    "Draw triangle from start to end."
    up()
    #Se posiciona el cursor en las coordenadas del tap inicial
    goto(start.x,start.y)
    down()
    #Se calcula la distancia de los lados del triángulo
    lado=end.x-start.x
    #El ciclo for trazará una línea recta de largo igual a la diferencia entre start.x y end.x .
    #Después del trazado, la dirección de dibujado rota 120 grados para posteriormente repetir el ciclo
    for count in range(3):
        forward(lado)
        left(120)

#Para cada clic en el area de dibujado, se almacenaran las coordenadas x,y del cursor
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()