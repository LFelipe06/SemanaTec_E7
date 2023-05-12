#Se llaman las librerias que ayudan a la ejecucion grafica y logica del juego
from turtle import *
from random import randrange
from freegames import square, vector
#Se establecen las variables de control para la ubicacion de la comida de la serpiente, la ubicacion de la serpiente y su direccion
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Con esta funcion se cambian los valores del vector de direccion de la serpiente en base a las variables en x y y
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y
#Con esta funcion se asegura de que la cabeza de la serpiente siempre se encuentre dentro de los limites del juego regresando un true. 
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190
#Con esta funcion se mantiene a la serpiente avanzando sobre el segmento en el que se encuentre
#primero se le asigna a la cabeza el valor de la ubicacion de la serpiente
#se mueve la serpiente con el vector de direccion aim
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
#Con esta funcion se determina si la cabeza se encuentra dentro del mapa o si no ha chocado son su cuerpo
    if not inside(head) or head in snake:
        #si choco, entonces se terminara el juego y la cabeza de la serpiente se tornara roja
        square(head.x, head.y, 9, 'red')
        update()
        return
#De lo contrario el cuerpo de la serpiente agregara las direcciones de la cabeza
    snake.append(head)
#Si la cabeza coincide con la ubicacion de la comida, entonces el cuerpo de la serpiente crecera, se imprime su tamaño y se reubicara a la comida
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
    #De lo contrario no se añade nada
        snake.pop(0)

    clear()
    #Se dibuja el cuerpo de la serpiente
    for body in snake:
        square(body.x, body.y, 9, 'black')
    #Se dibuja la comida de color verde
    square(food.x, food.y, 9, 'green')
    #Se actualiza el ambiente grafico
    update()
    #Mueve a la serpiente agregandole valores al vector de direccion de la serpiente
    ontimer(move, 100)
#Se configura el tamaño de la ventana del juego
setup(420, 420, 370, 0)
#Se esconde la tortuga que viene en la libreria turtle
hideturtle()
#Se apaga para mantener la funcion update funcionando adecuadamente, de acuerdo al ritmo de actualizacion que se ha configurado
tracer(False)
#Esta funcion recibe el input de las teclas
listen()
#Si se presiona derecha, entonces cambia el vector a la derecha
onkey(lambda: change(10, 0), 'Right')
#Si se presiona izquierda, entonces cambia el vector a la izquierda
onkey(lambda: change(-10, 0), 'Left')
#Si se presiona arriba, entonces cambia el vector hacia arriba
onkey(lambda: change(0, 10), 'Up')
#Si se presiona abajo, entonces cambia el vector hacia abajo
onkey(lambda: change(0, -10), 'Down')
#Se llama la funcion move en el main
move()
done()