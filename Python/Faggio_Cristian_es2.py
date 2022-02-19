import turtle

griglia = turtle.Turtle()
finestra = turtle.Screen()

for i in range(2):
    y=0
    x=0
    
    griglia.goto(x,y)
    griglia.down()
    for _ in range(5):
        if(i==0):
            y=y-20
        else: x=x+20

        griglia.forward(80)
        griglia.up()
        griglia.goto(x,y)
        griglia.down()
    
    griglia.up()
    griglia.right(90)

finestra.exitonclick()