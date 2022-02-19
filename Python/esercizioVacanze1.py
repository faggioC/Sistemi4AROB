lista = [1,1,5,4,5,4,6,2,1,3,8]
lista2 = []
lista2 = [elemento for elemento in lista if elemento not in lista2]

print(lista2)