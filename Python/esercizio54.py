import random
import turtle
turtle1 = turtle.Turtle()

class Stella():
    def __init__(self,x,y,dim):
        self.x = x
        self.y = y
        self.dim = dim

    def Disegna(self):
        turtle1.penup()
        turtle1.setposition(self.x,self.y)
        turtle1.pendown()

        turtle1.speed(50)

        for _ in range(5):
            turtle1.forward(self.dim)
            turtle1.right(144)
    
def main():
    for _ in range(50):
        s = Stella(random.randint(-300,300),random.randint(-300,300),10)
        s.Disegna()
    turtle1.exitonclick()

if __name__ == "__main__":
    main()