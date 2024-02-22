#[utilização de flags].
#Escreva um programa que leia n números (sendo n introduzido pelo utilizador) e indique se os números são todos iguais.

total_numeros = int(input("Introduza a quantidade de números a verificar: "))
num_anterior = 0
nums_iguais = 0

for x in range(1, total_numeros + 1):
    num_consola = int(input(f"Introduza o {x}º número: "))
    if num_consola == num_anterior:
        nums_iguais += 1
    num_anterior = num_consola
    
if nums_iguais == (total_numeros - 1):
    print("Os números são todos iguais")
else:
    print("Os números não são todos iguais")
