#Crie um jogo com 3 advinhas do tipo "Qual a cor do cavalo branco do Napoleão?",
#cada uma com 3 alternativas, apresentando o resultado final.

resposta_correta = 0
resposta_errada = 0

print("Qual a cor do cavalo branco do Napoleão? \n a - branco \n b - preto \n c - castanho")
while True:
    adv1 = str(input("Introduza a opção correta (a/b/c): "))
    if adv1 == "a":
        resposta_correta += 1
        break
    elif adv1 == "b" or adv1 == "c":
        resposta_errada += 1
        break
    else: 
        print("VALOR INVÁLIDO!")

print("Qual a cor do cavalo branco do Napoleão? \n a - branco \n b - preto \n c - castanho")
while True:
    adv2 = str(input("Introduza a opção correta (a/b/c): "))
    if adv2 == "a":
        resposta_correta += 1
        break
    elif adv2 == "b" or adv2 == "c":
        resposta_errada += 1
        break
    else: 
        print("VALOR INVÁLIDO!")

print("Qual a cor do cavalo branco do Napoleão? \n a - branco \n b - preto \n c - castanho")
while True:
    adv3 = str(input("Introduza a opção correta (a/b/c): "))
    if adv3 == "a":
        resposta_correta += 1
        break
    elif adv3 == "b" or adv3 == "c":
        resposta_errada += 1
        break
    else: 
        print("VALOR INVÁLIDO!")

print(f"Respostas corretas: {resposta_correta}")
print(f"Respostas erradas: {resposta_errada}")