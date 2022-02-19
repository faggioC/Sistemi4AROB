def push(pila,elemento):
    pila.append(elemento)

def pop(pila):
    if len(pila) != 0:
        return pila.pop()

pila=[]
str = input("Inserisci stringa")
for i in len(str):
    push(pila,str[i])