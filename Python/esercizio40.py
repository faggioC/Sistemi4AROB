import turtle

def disegnaGriglia(Griglia):
    Griglia.up()
    Griglia.goto(-50,150)
    Griglia.down()
    Griglia.right(90)
    Griglia.forward(300)
    Griglia.up()
    Griglia.goto(50,150)
    Griglia.down()
    Griglia.forward(300)
    Griglia.up()
    Griglia.goto(-150,50)
    Griglia.down()
    Griglia.left(90)
    Griglia.forward(300)
    Griglia.up()
    Griglia.goto(-150,-50)
    Griglia.down()
    Griglia.forward(300)

def disegnaCerchio(c,Griglia):
    if c == 0:
        x=-100
        y=100
    elif c == 1:
        x=0
        y=100
    elif c == 2:
        x=100
        y=100
    elif c == 3:
        x=-100
        y=0
    elif c == 4:
        x=0
        y=0
    elif c == 5:
        x=100
        y=0
    elif c == 6:
        x=-100
        y=-100
    elif c == 7:
        x=0
        y=-100
    elif c == 8:
        x=100
        y=-100
    
    Griglia.up()
    Griglia.goto(x,y-25)
    Griglia.down()
    Griglia.circle(25)
    Griglia.up()

def disegnaX(c,Griglia):
    if c == 0:
        x=-100
        y=100
    elif c == 1:
        x=0
        y=100
    elif c == 2:
        x=100
        y=100
    elif c == 3:
        x=-100
        y=0
    elif c == 4:
        x=0
        y=0
    elif c == 5:
        x=100
        y=0
    elif c == 6:
        x=-100
        y=-100
    elif c == 7:
        x=0
        y=-100
    elif c == 8:
        x=100
        y=-100
    
    Griglia.up()
    Griglia.goto(x,y)
    Griglia.down()
    Griglia.left(45)
    for _ in range(4):
        Griglia.forward(25)
        Griglia.backward(25)
        Griglia.left(90)    
    Griglia.right(45)

def controlloVittoria(griglia):
    vittoria = False
    if griglia[0]==griglia[1]==griglia[2] and griglia[0]!=None:
        vittoria = True
    elif  griglia[3]==griglia[4]==griglia[5] and griglia[3]!=None:
       vittoria = True
    elif  griglia[6]==griglia[7]==griglia[8] and griglia[6]!=None:
        vittoria = True
    elif griglia[0]==griglia[3]==griglia[6] and griglia[0]!=None:
        vittoria = True
    elif griglia[1]==griglia[4]==griglia[7] and griglia[1]!=None:
        vittoria = True
    elif griglia[2]==griglia[5]==griglia[8] and griglia[2]!=None:
        vittoria = True
    elif griglia[0]==griglia[4]==griglia[8] and griglia[0]!=None:
        vittoria = True
    elif griglia[2]==griglia[4]==griglia[6] and griglia[2]!=None:
        vittoria = True
    return vittoria


g1 = input("Inserisci giocatore 1: ")
g2 = input("Inserisci giocatore 2: ")
griglia = {0:None, 1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None}
conta=0
Griglia = turtle.Turtle()

disegnaGriglia(Griglia)

partitaFinita = False
while(partitaFinita==False):
    
    #ciclo
    c1=False
    print(f"{g1}:")
    while(c1==False):
        #chiedere mossa a giocatore 1
        cella=int(input("Inserisci la cella: "))
        #controllo cella libera
        if cella >= 0 and cella < 9:
            if griglia[cella]==None:
                griglia[cella]=g1
                c1=True
                disegnaCerchio(cella,Griglia)
                conta=conta+1
        
    
    #disegna griglia    
    #controllo della vittoria
    vittoria = controlloVittoria(griglia)
    if vittoria == True:
        print(f"Ha vinto {g1}")
        partitaFinita=True
        break
    elif conta == 9:
        print("Pareggio")
        break

    #ciclo
    c2=False
    print(f"{g2}:")
    while(c2==False):
        #chiedere mossa a giocatore 2
        cella=int(input("Inserisci la cella: "))
        #controllo cella libera
        if cella >= 0 and cella < 9:
            if griglia[cella]==None:
                griglia[cella]=g2
                c2=True
                disegnaX(cella,Griglia)
                conta=conta+1
    #disegna griglia
    
    vittoria = controlloVittoria(griglia)
    if vittoria == True:
        print(f"Ha vinto {g2}")
        partitaFinita=True
        break
    elif conta == 9:
        print("Pareggio")
        break
    
    
    #controllo della vittoria