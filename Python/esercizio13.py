#le liste sono contenitori mutabili

lista=[3,3.1415,"ciao"] #lista eterogenea
print(lista)

numeri_primi=[2,3,5,7,11,13]

print(lista[-1])

lista[0]=1
print(lista)

altri_numeri_primi=[19,23,29]
molti_numeri_primi=numeri_primi+altri_numeri_primi
print(molti_numeri_primi)

print(5*altri_numeri_primi)

for numero_primo in numeri_primi: 
    print(numero_primo,end="-")