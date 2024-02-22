#Dois números são amigos se a soma dos divisores de um for igual ao outro número e vice-versa

num1, num2 = 0, 0
soma1 = 0
soma2 = 0
 
while num1 <= 0 or num2 <= 0:
    try:
        num1 = int(input("Introduza o 1º numero: "))
        num2 = int(input("Introduza o 2º numero: "))
    except ValueError:
        print("Dados invalidos!")
 
for x in range(1, max(num1, num1)):
    if x < num1 and num1 % x == 0:
        soma1 += x
    if x < num2 and num2 % x == 0:
        soma2 += x
 
if soma1 == num2 and soma2 == num1:
    print(f"Os numeros {num1} e {num2} sao numeros amigos.")
else:
    print(f"Os numeros {num1} e {num2} nao sao numeros amigos.")