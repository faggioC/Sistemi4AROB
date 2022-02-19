import PileCode as pc

coda = pc.Coda()
pila = pc.Pila()
coda1 = pc.Coda()
nElementi = 0
while True:
    nElementi += 1
    elemento = input("Inserisci elemento nella coda: ")
    coda.enqueue(elemento)
    if input("Vuoi continuare s/n? ") == "n":
        break

coda.print()
for _ in range(nElementi):
    pila.push(coda.dequeue())

pila.print()

for _ in range(nElementi):
    coda1.enqueue(pila.pop())

coda1.print()