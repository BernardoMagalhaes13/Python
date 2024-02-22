# import math
from math import sqrt as raizQ, pow

# ler as coordenadas do ponto 1
print("Indique as coordenadas do ponto 1 (x1/y1) -> ")
x1 = int(input())
y1 = int(input())

# ler as coordenadas do ponto 2
print("Indique as coordenadas do ponto 2 (x2/y2) -> ")
x2 = int(input())
y2 = int(input())

# calcular as distancias euclideanas
dist = raizQ((x2 - x1) ** 2 + (y2 - y1) ** 2)  # (x2 -x1)**2 <=> pow(x2 -  x1, 2)

# mostrar o resultado
if dist == 0:
    print("Ospontos são coincidentes!")
else:
    print("Distancia = %.2f" % dist)  # %.2f arredonda com 2 casas decimais