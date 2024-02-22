#determinar a quantidade de numeros primos entre 2 e 999
num_primos = 0

for num in range(1, 101):
    primo = True
    for x in range(2, num):
        if (num % x == 0):
            primo = False
            break  # Se encontrarmos um divisor, não é primo, então podemos sair do loop interno
    if primo:
        num_primos += 1

print(f"Existem {num_primos} números primos")
