#[utilização de flags (ou não…)].
#Escreva um programa que leia n números (sendo n introduzido pelo utilizador)
#e indique se os números são todos pares, se são todos ímpares ou se há ambos os tipos.

total_numeros = int(input("Introduza a quantidade de números a verificar: "))
total_pares = 0
total_impares = 0

for x in range(1, total_numeros + 1):
    num = int(input(f"Introduza o {x}º número: "))
    if num % 2 == 0:
        total_pares += 1
        print("Nº PAR")
    else:
        total_impares += 1
        print("Nº IMPAR")

if total_pares == (total_numeros):
    print("Os números são todos pares")
elif total_impares == (total_numeros):
    print("Os números são todos impares")
else:
    print("Existem números pares e impares")
