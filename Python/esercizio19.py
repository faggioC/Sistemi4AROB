import math
x1 = float(input("Inserisci X del primo punto: "))
y1 = float(input("Inserisci Y del primo punto: "))
x2 = float(input("Inserisci X del secondo punto: "))
y2 = float(input("Inserisci X del secondo punto: "))

tuple=(x1,y1,x2,y2)
distanza= math.sqrt((tuple[0]-tuple[2])**2 + (tuple[1]-tuple[3])**2)
print(distanza)