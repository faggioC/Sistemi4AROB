def isPalindromo(s):
    if s == "".join(reversed(s)):
        return True
    else:
        return False

def isMaiuscolo(s):
    return True if s[0].isupper() else False


lista=["ciao","oppo","Cane","Muso","anna"]
palindrome=[]
maiuscole=[]

for parola in lista:
    if(isPalindromo(parola)):
        palindrome.append(parola)
    
    if(isMaiuscolo(parola)):
        maiuscole.append(parola)

print(palindrome)
print(maiuscole)