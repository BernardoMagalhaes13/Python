#Altere o programa de modo a que se o nome for "Bartolomeu", o programa imprima "Dá cá o meu!".

nome = str(input("Introduza o nome: "))
if nome == "bartolomeu" or nome == "Bartolomeu":
    print("Dá cá o meu!")
else: 
    print(f"Olá {nome}!")