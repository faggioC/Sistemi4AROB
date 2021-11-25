isPalindromo = lambda stringa: (stringa==stringa[::-1])

s = input("Inserisci una stringa: ")
if isPalindromo(s):
    print("Palindroma")
else:
    print("Non Palindroma")
