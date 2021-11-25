import math
quadratiPerfetti = [numero for numero in range(1,1000) if math.sqrt(numero)%1==0]

print(quadratiPerfetti)
