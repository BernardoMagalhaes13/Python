"""
3) Escreva um programa em que 5 valores inteiros entre 1 e 10 são introduzidos pelo utilizador num vetor. Depois, o utilizador deverá indicar um valor e o programa deverá indicar
 em que posição ou posições, este valor existe no vetor. Se o valor não existir no vetor o programa deverá dar a respetiva mensagem.
"""

#criar lista vazia
lista_nums = []
lista_nums_iguais = []

#colocar valores introduzidos na lista
for x in range (1, 6):
    num = int(input(f"Introduza o {x}º valor (entre 1 e 10): "))
    lista_nums.append(num)

num_procurado = int(input("Insira um valor a ser procurado no vetor: "))

#para cada posicao da lista_nums, verifica se é igual ao nº introduzido(num_procurado), se sim, adiciona-o à lista_nums_iguais
for i in range(len(lista_nums)):
    if lista_nums[i] == num_procurado:
        lista_nums_iguais.append(i)

if lista_nums_iguais:
    print(f"O número {num_procurado} está presente na(s) posição(ões): {lista_nums_iguais}")
else:
    print(f"O número {num_procurado} não está presente na lista de números.")