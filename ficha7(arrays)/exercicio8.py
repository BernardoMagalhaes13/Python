"""
8) Crie um programa que leia um vetor de n inteiros, sendo n um valor introduzido pelo utilizador, não havendo restrições. O
programa deverá converter todos os valores negativos do vetor para 0, imprimir o vetor resultante e indicar quantos valores foram
alterados.
"""

lista_nums = []
total_negativos = 0

total_lista = int(input(f"Introduza um número total de nºs da lista: "))

for x in range (0, total_lista):
    num = int(input(f"Introduza o {x}º número: ")) 
    if num < 0:
        total_negativos += 1
        simetrico_num = num * (-1)
        lista_nums.append(simetrico_num)
    else:
        lista_nums.append(num)

print("Lista final:", lista_nums)