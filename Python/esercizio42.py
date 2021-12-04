import random

f = open("./esercizio42.txt", "w")

alice = [random.randint(1, 6) for n in range(10)]
bob = [random.randint(1, 6) for n in range(10)]

for i in range(10):
    f.write(str(alice[i])+","+str(bob[i])+"\n")

f.close()
