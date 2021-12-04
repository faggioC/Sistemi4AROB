import turtle

f=open("./File/esercizio38.txt","r")
snow = turtle.Turtle()
finestra=turtle.Screen()

snow.color("blue")
finestra.bgcolor("cyan")
snow.hideturtle()
snow.speed(0)

righe = f.readlines()
for _ in range (8):
    for riga in righe:
        ls = riga.split(":")
        print(ls)
        if ls[0] == "forward":
            snow.forward(int(ls[1]))
        if ls[0] == "backward":
            snow.backward(int(ls[1]))
        if ls[0] == "right":
            snow.right(int(ls[1]))
        if ls[0] == "left":
            snow.left(int(ls[1]))
        if ls[0] == "goto":
            snow.goto(int(ls[1]),int(ls[2]))

finestra.exitonclick()