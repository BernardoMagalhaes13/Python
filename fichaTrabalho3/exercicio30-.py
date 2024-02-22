from random import randint

tentativa = 1
numAleatorio = randint(1, 100)
numConsola = int(input("Adivinhe o número entre 1 e 100: "))

while True:
    if numAleatorio == numConsola:
        print(f"PARABÉNS! Acertou o número em {tentativa} tentativas")
        break
    elif numConsola > numAleatorio:
        print (f"\nO número aleatório é menor que {numConsola}")
        numConsola = int(input("Introduza um novo número: "))
        tentativa += 1
    elif numConsola < numAleatorio:
        print (f"\nO número aleatório é maior que {numConsola}")
        numConsola = int(input("Introduza um novo número: "))
        tentativa += 1