perguntas = 2 #variavel controlo
nome_mais_jovem = ""
idade_mais_jovem = 131

while True:
    if perguntas == 2:
        nome_consola = input ("Introduza o nome: ")
        if nome_consola == "stop" or nome_consola == "STOP":
            break
        if nome_consola == "":
            print("Aviso: Nome inválido!")
        else:
            perguntas -= 1
    
    if perguntas == 1:
        idade_consola = int(input(f"{nome_consola}, introduza a sua idade: "))
        if idade_consola > 0 and idade_consola<=130: 
            perguntas = 2
            if idade_consola < idade_mais_jovem:
                idade_mais_jovem = idade_consola
                nome_mais_jovem = nome_consola
        else:
            print("Aviso: Idade inválida!")

if nome_mais_jovem == "":
    print("Não foram introduzidos quaisquer registos")
else:
    print(f"O nome da pessoa mais jovem é {nome_mais_jovem} e tem {idade_mais_jovem} anos")