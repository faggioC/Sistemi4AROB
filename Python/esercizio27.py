def isPrimo(num):
    k = 2
    trovato=True

    while k<num and trovato==True:
        r = num % k
        if r == 0:
            trovato = False
        k=k+1

    return trovato


"""
lista[]
for i in range(2,1000):   
    primo = isPrimo(i)

    if primo == True:
        lista.append(i)
"""
lista=[k for k in range(2,1003) if isPrimo(k)]
print(lista)

#lista=[k for k in range(2,1003) if isPrimo(k)]