import turtle

snow = turtle.Turtle()
finestra=turtle.Screen()

snow.color("blue")
finestra.bgcolor("cyan")
snow.hideturtle()
snow.speed(0)

for _ in range(8):
    snow.forward(100)
    for _ in range(5):
        snow.right(45)
        snow.forward(20)
        snow.backward(20)
        snow.left(90)
        snow.forward(20)
        snow.backward(20)
        snow.right(45)
        snow.backward(20)
    snow.goto(0,0)
    snow.right(45)

finestra.exitonclick()