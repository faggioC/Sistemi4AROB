operazione=int(input("Quale operazione vuoi fare(0: somma, 1: sottrazione, 2: moltiplicazione, 3: divisione): "))
if operazione >3:
    print("Hai inserito un numero non corretto")
else:  
    num1=int(input("Inserisci primo numero: "))
    num2=int(input("Inserisci secondo numero: "))

    if operazione==0:
        tot=num1+num2
    elif operazione==1:
        tot=num1-num2
    elif operazione==2:
        tot=num1*num2
    elif operazione==3:
        tot=num1/num2

    print(tot)


