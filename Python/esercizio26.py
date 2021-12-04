def isPrimo(num):
    k = 2
    trovato=True

    while k<num and trovato==True:
        r = num % k
        if r == 0:
            trovato = False
        k=k+1

    return trovato

conta = 0
for i in range(2,1000):   
    primo = isPrimo(i)

    if primo == True:
        conta=conta+1

print(f"Ci sono {conta} numeri primi minori di 1000")