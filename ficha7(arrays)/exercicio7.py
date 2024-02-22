"""
7) Crie um programa que leia um conjunto de valores inteiros do utilizador e os coloque num vetor. O programa deverá terminar a
leitura quando for introduzido um número que já exista no vetor, ou seja, quando for introduzido um número repetido. No final deverá
apresentar o vetor.
"""

lista_nums = []

while True:
    num = int(input(f"Introduza um número: "))

    # Verifica se o número já está na lista
    if num in lista_nums:
        break

    lista_nums.append(num)

print("Lista final:", lista_nums)