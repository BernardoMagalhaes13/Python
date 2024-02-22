"""
3) Crie uma função que receba dois valores float como argumentos e
retorne o valor da raiz quadrada da soma dos quadrados.
"""

import math

def calculos(a, b):
  soma_quadrados = a**2 + b**2
  raiz_quadrada_soma = math.sqrt(soma_quadrados)
  return raiz_quadrada_soma

#inicio

n1 = float(input("Introduza o 1º número: "))
n2 = float(input("Introduza o 2º número: "))

resultado = calculos(n1, n2)

print(f"O valor da raiz quadrada da soma dos quadrados é: {resultado}")