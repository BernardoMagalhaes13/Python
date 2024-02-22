'''
12) Escreva um programa que indique se todos os valores de um
vetor são iguais, se são todos diferentes, ou se há valores
repetidos no vetor. Para testar utilize um vetor cujo tamanho e
valores inteiros são introduzidos pelo utilizador.  
'''

numeros_vistos = []

def todosIguais (array):
    primeiro_elemento = array[0]

    for elemento in array:
        if elemento != primeiro_elemento:
            return False  # Retorna False se encontrar um elemento diferente

    return True  # Retorna True se todos os elementos forem iguais

def todosDiferentes(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                return False  # Se encontrar dois valores iguais, a lista não possui todos os elementos diferentes
    return True  # Se nenhum par de elementos iguais foi encontrado, a lista possui todos os elementos diferentes


def valoresRepetidos (array):
    for elemento in array:
        if elemento in numeros_vistos:
            return True  # Retorna True se encontrar um número repetido
        numeros_vistos.append(elemento)

#inicio

lista_nums = []

tamanho_array = int(input(f"Introduza o tamanho do array: "))
for x in range (1, tamanho_array + 1):
    valor_consola = int(input(f"Introduza o {x}º número: "))
    lista_nums.append(valor_consola)

iguais = todosIguais(lista_nums)
diferentes = todosDiferentes(lista_nums)
repetidos = valoresRepetidos(lista_nums)

if iguais:
    print("Os números do array são todos iguais")
elif diferentes:
    print("Os números do array são todos diferentes")
    if repetidos:
        print("Existem números repetidos")
    else:
        print("Não existem números repetidos")
else:
    print("Os números do array nem são todos iguais nem são todos diferentes")
    if repetidos:
        print("Existem números repetidos")
    else:
        print("Não existem números repetidos")
