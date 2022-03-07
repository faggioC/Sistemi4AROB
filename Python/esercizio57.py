import turtle

class Quadrato:
    def __init__(self,lato,x,y):
        self.lato = lato
        self.x = x
        self.y = y
    
    def perimetro(self):
        return self.lato*4
    
    def area(self):
        return self.lato**2

    def punto(self,cordX,cordY):
        if cordX > self.x+self.lato or cordX < self.x or cordY > self.y+self.lato or cordY < self.y:
            return True     #esterno al quadrato
        else: return False  #interno al quadrato
    
    def disegnaQuadrato(self):
        pen = turtle.Turtle()
        bg = turtle.Screen()
        for _ in range(4):
            pen.forward(self.lato)
            pen.right(90)
        bg.exitonclick()

def main():
    q = Quadrato(100,0,0)
    print(q.perimetro())
    print(q.area())
    if q.punto(2,0):
        print("Esterno")
    else: print("Interno")
    q.disegnaQuadrato()

if __name__ == "__main__":
    main()