import itertools
import random

lista = [1, 2, 3]
perm = list(itertools.permutations(lista))
n = random.randint(0, len(lista)+1)

print(perm[n])
