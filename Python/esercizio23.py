lista = []
temp = 'S'
while temp == 'S' or temp == 's':
    num = int(input("Inserisci un numero: "))
    lista.append(num)
    
    temp = input("Vuoi continuare? (S/N): ")

print(lista)