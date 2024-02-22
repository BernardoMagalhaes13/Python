# import math
from math import sqrt as raizQ

# ler coordenadas ponto1
x1 = float(input("Introduza o valor de x no ponto 1: "))
y1 = float(input("Introduza o valor de y no ponto 1: "))

# ler coordenadas ponto2
x2 = float(input("Introduza o valor de x no ponto 2: "))
y2 = float(input("Introduza o valor de y no ponto 2: "))

distancia = raizQ((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("A distância entre os dois pontos é: %.2f" % distancia)
