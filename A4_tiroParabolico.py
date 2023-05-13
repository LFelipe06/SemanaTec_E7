# Codigo obtenido de colección de videojuegos simples implementados en python: Free Python Games (https://grantjenks.com/docs/freegames/)
# Editado por Luis Felipe Hernández Flores A01735939 en el transcurso de Mayo 11 y Mayo 12 de 2023 
# para la UF: TC1001S.121 del semestre FJ 23 en ITESM C. Puebla 

# Importan las funciones requeridas para que el programa se ejecute.
from random import randrange
from turtle import *
from freegames import vector

#Se definen los vectores de la pelota a lanzar y su velocidad
ball = vector(-200, -200)
speed = vector(0, 0)
#Se crea el vector que almacenara los objetivos a disparar
targets = []
#Con esta funcion se dibuja la bola que se tira parabolicamente de acuerdo al click
def tap(x, y):
    "Respond to screen tap."
    #Mientras la bola no se encuentre en pantalla
    if not inside(ball):
        #Se asignan los valores iniciales al vector de direccion y velocidad de la pelota
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

# La función inside() evalua si el clic se está efectuando 
# dentro de la ventana generada.
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

# La función draw() limpia la ventana generada e instancía los 
# objetos target y ball. Inicialmente estos parten de un punto específico.
def draw():
    "Draw ball and targets."
    #Se limpia la pantalla
    clear()
    #Se dibujan los circulos azules a disparar
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')
    #Se dibuja la bola que se dispara con color rojo
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')
    
    #Se actualiza el entorno grafico
    update()
#Con esta funcion se establece el movimiento de los objetivos y del disparo del jugador (bola roja)
def move():
    "Move ball and targets."
    #Si el valor aleatorio es cero
    if randrange(40) == 0:
        #Se establecen los valores de posicion de un objetivo
        y = randrange(-150, 150)
        #Se agrega el vector de posicion a targets
        target = vector(200, y)
        targets.append(target)
    #Se le resta 0.5 al componente en x del vector del objetivo
    for target in targets:
        target.x -= 0.5
    #Mientras la bola se lance, la velocidad de los objetivos disminuira
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)
    #Se almacena una copia de targets en copy
    dupe = targets.copy()
    #Se limpia targets
    targets.clear()
    #se le agregan los objetivos cuya distacia sea menor a 13
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()
    
    # Para hacer que el programa se ejecute infinitamente debemos 
    # eliminar la validación siguiente.
    #for target in targets:
        #if not inside(target):
            #return
    # Modificar los parámetros de ontime() variará la velocidad 
    # con la que se mueven los objetos en la ventana
    ontimer(move, 20)
#Se establen las dimensiones de la ventana de juego
setup(420, 420, 370, 0)
#Se oculta la tortuga
hideturtle()
up()
#Se desactiva el traser
tracer(False)
#Recibe los clicks de la pantalla y ejecuta la funcion tao
onscreenclick(tap)
#Hace que se muevan lo objetivos y la bala
move()
done()