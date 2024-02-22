"""
9) Crie um programa que leia 10 números float, coloque-os num vetor e calcule a sua média.
"""

lista_num = []

for x in range (1, 11):
    num = float(input(f"Introduza o {x}º valor: "))
    lista_num.append(num)

soma = sum(lista_num)
tamanho = len(lista_num)

media = soma / tamanho

print(f"A Média dos valores introduzidos é {media}")