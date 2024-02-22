#Escreva um programa em que o utilizador vai introduzindo números positivos até ser introduzido o valor 0 (zero). 
#No fim o programa indicará a percentagem de números pares introduzidos.

nPares = 0
tNumeros = 0

while True:
    num = int(input("Introduza um número: "))
    if num > 0:
        if num % 2 == 0:
            nPares += 1
            tNumeros += 1
        else:
            tNumeros += 1
    elif num < 0:
        print("Só aceitamos números positivos!")
    elif num == 0:
        break

percentagemPares = (nPares/tNumeros) * 100

print(f"Dos {tNumeros} números introduzidos, {percentagemPares}% são pares")