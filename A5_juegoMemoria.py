# Codigo obtenido de colección de videojuegos simples implementados en python: Free Python Games (https://grantjenks.com/docs/freegames/)
# Editado por Luis Felipe Hernández Flores A01735939 y Cruz Daniel Pérez Jiménez A01736214 en el transcurso de Mayo 11 y Mayo 12 de 2023 
# para la UF: TC1001S.121 del semestre FJ 23 en ITESM C. Puebla 

#Se llaman las librerias para que el juego pueda ser ejecutado correctamente
from random import *
from turtle import *
from freegames import path
#Se declaran las variables a manera de contador.
taps = 0
descubiertos = 0
#Se almacena la direccion de la foto del carro
car = path('car.gif')
#Se declara la variable para generar una lista de numeros aleatorios entre 0 y 32
tiles = list(range(32)) * 2
#Se declara la funcion para declarar el estado de los recuadros
state = {'mark': None}
#Se declara la funcion para diferenciar las tiles que estan ocultas de las que no
hide = [True] * 64
#Un arreglo con los colores que se mostraran en los numeros
colorT=choice(['blue','gray', 'red', 'cyan', 'green', 'orange'])
#Con esta funcion se dibujan los cuadrados en los que iran los numeros
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', colorT)
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()
#Con esta funcion se le otorga un indice a los cuadrados del memorama conforme a su posicion
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)
#Esta funcion devuelve las coordenadas de una carta conforme a su indice
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200
#Esta funcion muestra los numeros de las tarjetas al momento de ser volteadas 
def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    # Se incrementa la variable correspondiente al numero de taps que el usuario a 
    # realizado. Se imprime en terminal.
    global taps
    taps+=1
    print("Numero de taps: " + str(taps))
    #Mientras que no este marcada o seleccionada se le otorgara el estado "spot"
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        
    else:
        #De lo contrario se muestra la tarjeta
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        # Se actualiza la variable correspondiente a los tiles descubiertos en caso 
        # de haber una coincidencia. Se imprime en terminal.
        global descubiertos
        descubiertos+=2
        print("Tiles descubiertos: " + str(descubiertos))
    #Se valida el numero de cuadrados descubiertos, si es 64 entonces se desplegara un mensaje
    if(descubiertos==64):
        print("Has desubierto todos los tiles")
#Esta funcion se encarga de dibujar las partes descubiertas del memorama, mostrando asi la imagen del carro
def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()
#se dibujan los 64 recuadros
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
#se les asigna su estado inicial
    mark = state['mark']
#si se selecciona la tarjeta, entonces se muestra el numero que tienen
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        # Se establece las coordenadas del cursor de trazado.
        goto(x + 25, y)
        #Se hace que los numeros tengan un color al azar
        color(choice(['gray', 'red', 'cyan', 'green', 'orange']))
        # A la funcion write() se le añade como parámtetro : align="center"
        write(tiles[mark], font=('Arial', 30, 'normal'), align="center")
    #Se mantiene actualizando el ambiente grafico
    update()
    ontimer(draw, 100)

shuffle(tiles)
#Se configura el tamaño de la ventana
setup(420, 420, 370, 0)
#Agrega la figura del carro
addshape(car)
#Oculta la tortuga
hideturtle()
#Se desactiva el tracer
tracer(False)
#Recibe los clicks en la ventana y ejecuta la funcion tap
onscreenclick(tap)
#llama a la funcion que dibuja los recuadros
draw()
done()