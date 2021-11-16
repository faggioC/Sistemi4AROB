def minMax(lista):
    min=lista[0]
    max=lista[0]
    j=0
    for i in lista:
        if min > lista[j]:
            min=lista[j]
        j=j+1
    
    j=0
    for k in lista:
        if max < lista[j]:
            max=lista[j]
        j=j+1
    
    return min, max


lista=[6,2,12,3,43]
min, max = minMax(lista)

print(f"Minimo: {min}, Massimo: {max}")