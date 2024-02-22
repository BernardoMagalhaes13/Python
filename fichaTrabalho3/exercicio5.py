#Escreva um programa que peça ao utilizador um nome e um número inteiro (entre 1 e 20).
#Deverá mostrar esse nome um número de vezes igual a esse valor inteiro.

nome = str(input("Introduza o nome: "))
num = int(input("Introduza o nº de vezes que quer repetir o nome:"))

for x in range(1, num + 1):
    print(f"{x} - {nome}")