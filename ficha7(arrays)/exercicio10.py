"""
10) Escreva um programa que preencha um vetor de 20 posições com os primeiros 20 números primos. 
"""

lista_num = []
num = 1

while len(lista_num) < 20:
    primo = 1 #se nao for primo, passa a 0
    
    if num <= 1:
        primo = 0
    for x in range(2, num):
        if (num % x == 0):
            primo = 0
    
    if primo == 1:
        lista_num.append(num)

    num += 1

print("Os primeiros 20 números primos são:", lista_num)