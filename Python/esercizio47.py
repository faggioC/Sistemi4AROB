continua = False
f = open("./File/esercizio47.txt","w")


while continua == False:
    cognome = input("Inserisci cognome: ")
    voto = float(input("Inserisci il voto: "))
    f.write(cognome[0] + '*'*(cognome.__len__()-1) + " Voto: "+ str(voto))
    f.write("\n")
    if input("Vuoi continuare: (S/N) ") == "S":
        continua = False
    else: continua = True

f.close