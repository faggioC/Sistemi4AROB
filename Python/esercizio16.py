lista = []

n1 = float(input("Inserisci primo numero: "))
n2 = float(input("Inserisci secondo numero:"))


lista.append((n1*n1)+(n2*n2))

lista.append((n1+n2)*(n1+n2))

lista.append((n1*n1)-(n2*n2))

lista.append((n1-n2)*(n1-n2))

print(lista)