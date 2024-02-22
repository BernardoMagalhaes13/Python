"""
5) Escreva um programa que determine o 2º maior valor de um vetor.
"""

lista = [10,2,3,1,5,6,9,8,11,5]
max1 = 0
max2 = 0

for x in range(0, len(lista)):
    if lista[x] > max1:
            max2 = max1
            max1 = lista[x]
    elif lista[x] > max2 and lista[x] != max1:
            max2 = lista[x]

print(max2)