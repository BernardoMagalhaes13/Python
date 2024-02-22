import math
from math import sqrt as raizQ

#ler catetos
c1 = float(input("Introduza o valor do 1º cateto: "))
c2 = float(input("Introduza o valor do 2º cateto: "))

#calcular
hipQuadrado = c1**2 + c2**2

#simplificar
hip = raizQ(hipQuadrado)

#imprimir resultados
print("hip = %.2f" % hip)