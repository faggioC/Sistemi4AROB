#slicing
stringa = "Classe quarta A Robotica"
print(f"Il primo carattere della stringa è {stringa[0]}")
print(f"L'ultimo carattere della striga è {stringa[-1]}")

#prende i caratteri a partire da indice 3 fino a 9 escluso
print(stringa[3:9])

#prende i caratteri a partire da indice 6 fino alla fine
print(stringa[6:])

#prende tutti i caratteri tranne gli ultimi due
print(stringa[:-2])

#prende da 2 a 13 balzando di 2
print(stringa[2:14:2])

#prende tutti i caratteri ma parte dal fondo
print(stringa[::-1])

#le stringhe in pyton sono IMMUTABILI
#TypeError: 'str' object does not support item assignment
#stringa[15]="B"

stringaNuova = stringa[0:14] + "B" + stringa[15:]
print(stringaNuova)
print(f"La stringa Nuova è: {stringaNuova}")

#stampa la funzione
print(print)
