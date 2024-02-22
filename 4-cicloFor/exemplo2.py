#ler num
num = -1
while not num >= 0:
    num = int(input("Introduza um número positivo -> "))

#calcular fatorial
if num == 0:
    print(num, "= 1")
else:
    fatorial = num
    for x in range(num - 1, 1, -1):
        fatorial *= x 
    print ("O fatorial de", num, " é igual a", fatorial)