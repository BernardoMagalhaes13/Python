#Crie um programa para escrever a série de quadrados entre 1 e um valor inteiro inferior a 100 introduzido pelo utilizador. (1, 4, 9, 25...)

num = int(input("Introduza um número (entre 1 e 100): "))

while num < 1 or num > 100:
    num = int(input("NÚMERO INVÁLIDO! Introduza um número (entre 1 e 100): "))

for x in range(1, num):
    quadrado = x * x
    print(f"{x}^2 = {quadrado}")