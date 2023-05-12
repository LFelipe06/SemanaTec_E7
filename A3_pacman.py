"""Pacman, classic arcade game.

Exercises

1. Change the board -listo 
2. Change the number of ghosts. -listo
3. Change where pacman starts. -listo
4. Make the ghosts faster/slower. -listo
5. Make the ghosts smarter.
"""
#Codigo obtenido de colección de videojuegos simples implementados en python: Free Python Games (https://grantjenks.com/docs/freegames/)
#Editado por Andre Rossell Manrique A01736035 en el transcuro de Mayo 11 y Mayo 12 de 2023 
#para la UF: TC1001S.121 del semestre FJ 23 en ITESM C. Puebla 


from random import choice #funcion para elegir algun elemento de un enumerable
from turtle import * #se importa el módulo turtle para el uso de funciones graficas

from freegames import floor, vector  #importación de metodos floor y vector. 
                                    #el primero reduce a un numeor cualquiera al más pequeño cada x incremento desde -200 
                                    # (pj. si mandaramos (10,100) hallaría: -200,-100,0,100,200 y ubicaria a 10 entre 0 y 100, reducinendolo a 0)
                                    #el segundo es una implementación de estructura de datos en tipo vector, es decir, con dos coordenadas. 

state = {'score': 0} 
path = Turtle(visible=False) #las siguientes dos lineas ocultan a la tortuga del módulo para solo permitir el dibujado 
writer = Turtle(visible=False)
aim = vector(0, 0) #vector de direccion inicial de pacman - modificacion: la direccion inicial no es ninguna para moverlo como usuario
pacman = vector(-20, -40) #Coordenadas x y de pacman - ya modificadas 
ghosts = [ #tuplas de coordenadas y direcciones de cada fantasma - actualizada velocidad más alta
    [vector(-180, 160), vector(7, 0)],
    [vector(-180, -160), vector(0, 7)],
    [vector(100, 160), vector(0, -7)],
    [vector(100, -160), vector(-7, 0)],
    [vector(40,100), vector(7,0)] # anadi nuevo fantasma completamente funcional con esta linea
]
# fmt: off
tiles = [ # actualizado para hacer una modificacion en el tablero
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
# fmt: on

#funcion para dibujado de un cuadrado 
def square(x, y):
    """Draw square using path at (x, y)."""
    path.up() #levanta el lapiz
    path.goto(x, y) #se traslada a la posicion donde se pidio el cuadrado 
    path.down() #baja el lapiz para empezar a dibujar
    path.begin_fill() #comienza el rellenado, la proxima figura dibujada tendrá un relleno 

    for count in range(4): #loopea 4 veces para hacer en cada arista del cuadrado 
        path.forward(20) #avanza veinte unidades 
        path.left(90) # gira en angulo recto a la izquierda 

    path.end_fill() #se desactiva el modo de fill 

#Reduce cualquier dado punto reducido para aproximarlo a la coordenada de una intersección en tablero 
def offset(point):
    """Return offset of point in tiles."""
    x = (floor(point.x, 20) + 200) / 20 #conversion de x con funcion floor
    y = (180 - floor(point.y, 20)) / 20 #conversion de y con funcion floor 
    index = int(x + y * 20)
    return index #indice es el valor de ambos componentes de la coordenada. 

def valid(point):
    """Return True if point is valid in tiles."""
    index = offset(point) #reduce el punto 

    if tiles[index] == 0:
        return False

    index = offset(point + 19) #recorre el punto a el próximo nivel 

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0 # valida en ambas dimensiones que se pueda realizar el giro 

#utiliza al objeto de Turtle para dibujar el escenario
def world():
    """Draw world using path."""
    bgcolor('black') #definicion de color de background
    path.color('blue') #definición de color de dibujado 

    for index in range(len(tiles)): #realiza un recorrido por cada elemento del arreglo de intersecciones
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y) #manda a dibujar un cuadrado en las coordendas 

        if tile == 1:
            path.up()
            path.goto(x + 10, y + 10)
            path.dot(2, 'white') #traslada el punto de dibujado cada vez que encuentra un 1 y posiciona el punto de la pastilla para comer 

#funcion de movimiento general
def move():
    """Move pacman and all ghosts."""
    writer.undo()
    writer.write(state['score'])#se actualiza la impresión con respecto del valor actual de score

    clear()

    if valid(pacman + aim): #se valida la dirección de pacman para que respete los límites del mapa y si es correcta, le permite el movimiento.
        pacman.move(aim)

    index = offset(pacman) #encuentra el pasar del pacman 

    if tiles[index] == 1: #si encuentra una pastilla en la posición de pacman
        tiles[index] = 2 #transfiere su estado a comido
        state['score'] += 1 #aumenta el score
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y) #genera un cuadro negro para tapar a la pastilla

    up() #levanta pincel para realizar movimiento del mismo
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow') #despues de encontrar al pacman, pinta el putno de su posicion 

    for point, course in ghosts: #loopea por cada uno de los fantasmas para dibujarlos
        if valid(point + course): #valida su trayectoria y aplica movimiento 
            point.move(course)
        else: #genera una decision aleatoria que decida un proximo movimiento 
            options = [ #velocidad actualizada
                vector(7, 0),
                vector(-7, 0),
                vector(0, 7),
                vector(0, -7),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red') #dibuja al fantasma en su posicion

    update()

    for point, course in ghosts: #tomando en cuenta la posicion de cada fantasma
        if abs(pacman - point) < 20: #si detecta colision respecto de las posiciones
            return #pora toda la ejecucion

    ontimer(move, 100) #vuelve a llamar al movimiento 


def change(x, y): #recalcula la direccion de pacman si es valido 
    """Change pacman aim if valid."""
    if valid(pacman + vector(x, y)): #valida que la direccion sea posible 
        aim.x = x
        aim.y = y #realiza el cambio de direccion 

#programa principal
setup(420, 420, 370, 0) #se inicializan las dimensiones del tablero 
hideturtle()
tracer(False)
writer.goto(160, 160) #se define el lugar donde se escribe la puntuacion
writer.color('white')
writer.write(state['score'])
listen() #deteccion de inputs del teclado
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world() #dibujado de mundo
move() #actualizacion de posiciones
done()
