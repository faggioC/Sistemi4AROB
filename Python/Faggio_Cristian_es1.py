import random

def spostamento():
    c=False
    while(c==False):
        num = random.randint(-1,1)
        if num != 0:
            c=True
    return num

spostamenti = [spostamento() for _ in range(60*60*24*5)]
somma = 0

for i in range(60*60*24*5):
    somma += spostamenti[i]

print(f"Spostamento totale effettuato dopo 5 giorni: {somma} cm")