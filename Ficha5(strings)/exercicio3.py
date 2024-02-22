#Altere o programa anterior para que a mensagem surja para todos os nomes terminados em "eu". Exemplo:> Olá Zebedeu! Dá cá o meu!

nome = str(input("Introduza o nome: "))

n = len(nome)

if nome[n-1] == "u" and nome[n-2] == "e":
    print("Dá cá o meu!")
else: 
    print(f"Olá {nome}!")