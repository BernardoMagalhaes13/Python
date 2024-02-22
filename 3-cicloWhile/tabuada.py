# ler o numero para o qual será apresentada a tabuada
num = int(input("Escreva o número para a tabuada que pretende -> "))

# escrever a tabuada
i = 1
while i <= 10:
    res = num * i
    print(num,"X", i, "=", res)
    i += 1
