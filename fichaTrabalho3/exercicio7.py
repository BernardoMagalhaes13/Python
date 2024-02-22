#Escreva um programa que leia 10 números inteiros introduzidos pelo utilizador e 
#indique o máximo, a média, o mínimo e a soma dos valores.

soma = 0
maximo = 0
minimo = 9999999

for x in range(1, 11):
    num = int(input(f"Insira o {x}º número inteiro positivo: "))
    
    # Atualiza o máximo se o número inserido for maior
    if num > maximo:
        maximo = num
    
    # Atualiza o mínimo se o número inserido for menor
    if num < minimo:
        minimo = num
    
    # Soma os valores inseridos
    soma += num

# Calcula a média dos valores inseridos
media = soma / 10

# Exibe os resultados
print(f"Soma = {soma}")
print(f"Média = {media}")
print(f"Máximo = {maximo}")
print(f"Mínimo = {minimo}")
