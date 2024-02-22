import random
#pedra = 1
#papel = 2
#tesoura = 3

opcao_PC = random.randint (1,3) 

while True:
    opcao_user = int(input("Introduza a escolha (1- pedra / 2- papel / 3- tesoura / 0 - TERMINAR)"))
    if opcao_user < 4 and opcao_user > 0:
        if opcao_PC == 1: #PC escolheu pedra, ganho se escolher papel, perco de escolher tesoura
            if opcao_user == 1:
                print("EMPATE! (pedra = pedra)")
            elif opcao_user == 2:
                print("O user ganhou! (Pedra < papel)")
            elif opcao_user == 3:
                print("O PC ganhou! (Pedra > Tesoura)")
            
        if opcao_PC == 2: #PC escolheu papel, ganho se escolher tesoura, perco de escolher pedra
            if opcao_user == 1:
                print("O PC ganhou! (papel > pedra)")
            elif opcao_user == 2:
                print("EMPATE! (papel = papel)")
            elif opcao_user == 3:
                print("O user ganhou! (papel < Tesoura)")
            
        if opcao_PC == 3: #PC escolheu tesoura, ganho se escolher pedra, perco de escolher papel
            if opcao_user == 1:
                print("O user ganhou! (tesoura < pedra)")
            elif opcao_user == 2:
                print("O PC ganhou! (tesoura > papel)")
            elif opcao_user == 3:
                print("EMPATE! (tesoura = tesoura)")
    elif opcao_user == 0:
        break