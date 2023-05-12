# Codigo obtenido de colección de videojuegos simples implementados en python: Free Python Games (https://grantjenks.com/docs/freegames/)
# Editado por Luis Felipe Hernández Flores A01735939 en el transcurso de Mayo 11 y Mayo 12 de 2023 
# para la UF: TC1001S.121 del semestre FJ 23 en ITESM C. Puebla 

# Importan las funciones requeridas para que el programa se ejecute.
from random import randrange
from turtle import *
from freegames import vector

#Se definen los vectores de 
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
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
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

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

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()