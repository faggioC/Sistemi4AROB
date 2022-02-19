#2)Scrivere una funzione Python ricorsiva che permetta di stampare i numeri di Fibonacci minori di un valore scelto dall'utente. 

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

limite = int(input("Inserisci il numero di valori della serie che desideri vedere: "))

for num in range(1, limite+1):
    print(fibonacci(num))