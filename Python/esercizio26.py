def isPrimo(num):
    k = 2
    trovato=True

    while k<num and trovato==True:
        r = num % k
        if r == 0:
            trovato = False
        k=k+1
    if num == 1:
        return False
    return trovato

conta = 0
i=1
while i<1000:   
    primo = isPrimo(i)

    if primo == True:
        conta=conta+1
    i=i+1

print(f"Ci sono {conta} numeri primi minori di 1000")