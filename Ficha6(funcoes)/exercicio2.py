"""
Crie uma função que receba 3 valores float como argumento e retorne o maior valor absoluto.
"""

def maior_valor(abs_a, abs_b, abs_c):
  maior = max(abs_a, abs_b, abs_c)
  return maior

#inicio

n1 = float(input("Introduza o 1º número: "))
n2 = float(input("Introduza o 2º número: "))
n3 = float(input("Introduza o 3º número: "))

abs_n1 = abs(n1)
abs_n2 = abs(n2)
abs_n3 = abs(n3)

maximo = maior_valor(abs_n1, abs_n2, abs_n3)

print(f"O maior valor absoluto é: {maximo}")
