import turtle

n = int(input("inserisci numero lati: "))
disegno1 = turtle.Turtle()
disegno2 = turtle.Turtle()
lista = [disegno1, disegno2]
window = turtle.Screen()

lista[1].right(180)

for _ in range(n):
    for i in range(2):
        lista[i].forward(50)
        lista[i].left(360/n)

window.exitonclick()
