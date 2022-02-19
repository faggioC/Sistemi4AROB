f = open("covid-19_gen1.txt", "r")
righe = f.readlines()
lista = ["A", "T", "C", "G"]
contA = 0
contT = 0
contC = 0
contG = 0


for riga in righe:
    for elemento in lista:
        if elemento == "A":
            contA = contA + riga.count(elemento)
        elif elemento == "T":
            contT = contT + riga.count(elemento)
        elif elemento == "C":
            contC = contC + riga.count(elemento)
        elif elemento == "G":
            contG = contG + riga.count(elemento)


dizionario = {lista[0]: contA, lista[1]: contT, lista[2]: contC, lista[3]: contG}
print(dizionario)