def isDivisibile(numero, div):
    if (numero % div == 0):
        return True
    else:
        return False


numero = int(input("Inserisci un numero: "))

esiste = False
for i in range(2, 6):
    if i != 4:
        if(isDivisibile(numero, i)):
            print(f"Il numero è divisibile per {i}")
            esiste = True

if esiste == False:
    print("Non è divisibile per nessun numero tra 2,3,5")
