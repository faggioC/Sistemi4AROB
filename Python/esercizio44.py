import turtle

n = int(input("Inserisci numero lati: "))
disegno = turtle.Turtle()
window = turtle.Screen()
for i in range(n):
    disegno.forward(50)
    disegno.left(360/n)
window.exitonclick()
