#ler num
num = int(input("Introduza um número -> "))

if num < 2:
    print (f"{num} não é primo")
else:
#verificar se não é divisivel por qualquer numero entre 2 e o numero (se é primo)
    for x in range(2, num):
        if (num % x == 0):
            print("não é primo")
            break
    else:
        print ("primo")
        