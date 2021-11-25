isMaiuscola = lambda s: True if s[0].isupper() else False

s = input("Inserisci una stringa: ")
if isMaiuscola(s) == True:
    print("La prima lettera è maiuscola")
else:
    print("La prima lettera non è maiuscola")
