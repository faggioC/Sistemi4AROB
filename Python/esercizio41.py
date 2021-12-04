valore = int(input("Inserisci un valore: "))
lista = [2**n for n in range(valore) if 2**n < valore]
print(lista)
