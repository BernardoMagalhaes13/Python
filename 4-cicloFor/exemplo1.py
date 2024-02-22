num1 = num2 = 0

#ler dados
while num1 == num2:
    num1 = int(input("Introduza o número 1 -> "))
    num2 = int(input("Introduza o número 2 -> "))

#determinar max e min
minimo = min(num1, num2)
maximo = max(num1, num2)

somar = 0

#ciclo for
for x in range(minimo, maximo + 1):
    somar += x
    print (x)

print ("Soma: ", somar)