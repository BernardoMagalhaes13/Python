from math import sqrt as raizQ, pow

# ler as coordenadas do ponto 1
print("Indique as coordenadas do ponto 1 (x1/y1) -> ")
x1 = int(input())
y1 = int(input())

# ler as coordenadas do ponto 2
print("Indique as coordenadas do ponto 2 (x2/y2) -> ")
x2 = int(input())
y2 = int(input())

# ler as coordenadas do ponto 3
print("Indique as coordenadas do ponto 3 (x3/y3) -> ")
x3 = int(input())
y3 = int(input())

# calcular a media dos lados
lado1 = raizQ((x2 - x1) ** 2 + (y2 - y1) ** 2)
lado2 = raizQ((x3 - x2) ** 2 + (y3 - y2) ** 2)
lado3 = raizQ((x1 - x3) ** 2 + (y1 - y3) ** 2)

# validar triangulo de acordo com a formula
if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
    print("Os tres pontos podem formar um triangulo")
else:
    print("Os tres pontos nao podem formar um triangulo")