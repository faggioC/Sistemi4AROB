parole=["ciaooooo","come","va","beni"]

max=parole[0]
for parola in parole:
    if len(max)<len(parola):
        max=parola

print(max)