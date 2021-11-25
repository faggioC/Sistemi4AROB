tavola = [(x*y) for x in range(1,11) for y in range (1,11)]
indice1=0
indice2=10

for _ in range(10):
    print(tavola[indice1:indice2])
    indice1+=10
    indice2+=10