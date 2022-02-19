#3)Scrivere un programma in Python nel quale utilizzando il modulo turtle: - sia presente una funzione che disegni una stella nelle coordinate x e y 
#(passate come parametri alla funzione) - disegni 50 stelle sullo screen posizionate in posizioni casuali. 
import turtle
import random

Stella=turtle.Turtle()
window = turtle.Screen()


def Disegno_stella(x,y):
    Stella.penup()
    Stella.setposition(x,y)#setta la posizione di partenza
    Stella.pendown()

    Stella.speed(50)#velocità

    for _ in range(5): #disegno stella
        Stella.forward(50)
        Stella.right(144)

for _ in range(50):
    Disegno_stella(random.randint(-480,480),random.randint(-480,480))
window.exitonclick()  
