"""
1) Escreva um programa que preencha um vetor de 100 posições com os primeiros 100 números pares.
"""
#criar lista vazia
nums_pares = []

#criar função que verifica se o nº é par
def verificar_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

#ciclo for para verificar de cada um dos números é par
for num in range (1, 101):
    if verificar_par(num):
        nums_pares += [num]

print(nums_pares)