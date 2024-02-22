#Escreva um programa que leia 10 números inteiros e indique se um número é igual ao anterior.
#No final deverá indicar quantos números introduzidos são iguais ao anterior.

num_anterior = 99999999
nums_iguais = 0

for x in range(1, 11):
    num_consola = int(input(f"Introduza o {x}º número: "))
    if num_consola == num_anterior:
        print (f"Número igual ao anterior")
        nums_iguais += 1
    num_anterior = num_consola

print(f"Inseriu no total, {nums_iguais} iguais aos anteriores")