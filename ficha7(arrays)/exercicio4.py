"""
4) Crie um programa que apresente a soma de todos os valores de um vetor de inteiros de 10 posições. Os valores devem ser introduzidos
pelo utilizador. 
"""

lista_nums = []
soma = 0

for x in range (0, 10):
    num = int(input(f"Introduza o nª da {x}ª posição da lista: "))
    lista_nums.append(num)
  
soma = sum(lista_nums)
print (soma)