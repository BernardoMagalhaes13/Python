"""
Crie uma função que receba 2 valores inteiros como argumentos e retorne a sua soma. Se o valor da soma for negativo a função deverá
retornar o valor 0. 
"""

def soma(a, b):
  res_soma = a + b
  return res_soma

def negativo(n):
  return n < 0

# inicio do programa
n1 = int(input("Introduza o 1º número: "))
n2 = int(input("Introduza o 2º número: "))

somar = soma(n1, n2)

if negativo(somar):
  print("0")
else:
  print(f"{n1} + {n2} = {somar}")