"""
6) Crie um programa que leia um vetor de 10 valores inteiros do utilizador, não permitindo a introdução de valores repetidos.
"""

lista_nums = []

for x in range(10):
    num = int(input(f"Introduza o número da {x + 1}ª posição da lista: "))

    # Verifica se o número já está na lista
    while num in lista_nums:
        print("Número já existe na lista. Por favor, insira um número diferente.")
        num = int(input(f"Introduza o número da {x + 1}ª posição da lista: "))

    lista_nums.append(num)

print("Lista final:", lista_nums)