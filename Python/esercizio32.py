isPalindromo = lambda stringa: (stringa==stringa[::-1])
isMaiuscola = lambda s: s[0].isupper()

lista=["ciao","ora","Cane","oro","anna"]
palindrome=[]
maiuscole=[]

for parola in lista:
    if(isPalindromo(parola)):
        palindrome.append(parola)
    
    if(isMaiuscola(parola)):
        maiuscole.append(parola)

print(palindrome)
print(maiuscole)