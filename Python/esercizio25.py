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

num = int(input("Inserisci un numero: "))
primo = isPrimo(num)

if primo == True:
    print("Il numero è primo")
else: print("Il numero non è primo")