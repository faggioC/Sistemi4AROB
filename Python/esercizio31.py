s = input("Inserisci una stringa")
if s == "".join(reversed(s)):
    print("Palindrome")
else:
    print("Not Palindrome")
