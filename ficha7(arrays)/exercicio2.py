"""
2) Escreva um programa que procure e indique o maior valor (e a respetiva posição) de um vetor de 10 posições introduzido pelo utilizador.
"""
#criar lista vazia
lista_num = []

#colocar valores introduzidos na lista
for x in range (1, 11):
    num = int(input(f"Introduza o {x}º valor: "))
    lista_num += [num]
    
maior_valor = max(lista_num)
posicao = lista_num.index(maior_valor)

print(f"O maior valor na lista é {maior_valor} e está na posição {posicao}.")
