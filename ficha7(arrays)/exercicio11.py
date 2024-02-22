'''
11) Crie um programa que leia um vetor de 10 inteiros. Os valores
deverão estar no intervalo [0,100]. O programa não deverá aceitar
valores fora deste intervalo. O programa deverá indicar a soma dos
inteiros múltiplos de 5 existentes no vetor. 
'''

lista_numeros = []
soma_div5 = 0

for x in range (1, 11):
    valor_consola = int(input(f"Introduza o {x}º número: "))
    lista_numeros.append(valor_consola)

for elemento in lista_numeros:
    if elemento % 5 == 0:
        soma_div5 += elemento

print(soma_div5)