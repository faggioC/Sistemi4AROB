def disegnaGriglia(g, g1, g2):
    for i in range(9):
        if g[i] == None:
            print("   ",end="")
        elif g[i] == g1:
            print(" O ",end="")
        elif g[i] == g2:
            print(" X ",end="")
        
        if(i==2 or i==5):
            print("\n------------")
        elif i==8:
            print("\n")
        else: print("|",end="")

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
disegnaGriglia(griglia,g1,g2)
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
        
    
    #disegna griglia
    disegnaGriglia(griglia,g1,g2)
    
    #controllo della vittoria
    vittoria = controlloVittoria(griglia)
    if vittoria == True:
        print(f"Ha vinto {g1}")
        partitaFinita=True
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
    
    #disegna griglia
    disegnaGriglia(griglia,g1,g2)
    
    vittoria = controlloVittoria(griglia)
    if vittoria == True:
        print(f"Ha vinto {g2}")
        partitaFinita=True
        break
    
    
    #controllo della vittoria