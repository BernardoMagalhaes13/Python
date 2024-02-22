#Escreva um programa para imprimir todos os números inteiros entre dois valores introduzidos pelo utilizador. 
#O programa deverá verificar qual dos dois valores é o maior.    

num1 = int(input("Introduza o 1º numero: "))
num2 = int(input("Introduza o 2º numero: "))

if num1 > num2:
    print(f"{num1} > {num2}")
    # Ciclo decrescente
    for x in range(num1, num2 - 1, -1):
        print(x)
elif num1 < num2:
    print(f"{num1} < {num2}")
    # Ciclo crescente
    for y in range(num1, num2 + 1):
        print(y)
else:
    print("Os números são iguais. Não há intervalo para mostrar.")