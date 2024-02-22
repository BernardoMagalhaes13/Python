# ler o numero para o qual será apresentada a tabuada
num = int(input("Escreva o número para a tabuada que pretende -> "))

# escrever a tabuada
for x in range (0, 11):
    res = num * x
    print (num,"X", x, "=", res)
    x += 1