num1 = num2 = -1

while num1 == num2:
    num1 = int(input("Introduza o numero onde iniciar a soma -> "))
    num2 = int(input("Introduza até que numero pretenda que some -> "))

menor = min(num1, num2)
maior = max(num1, num2)

i = 2

while menor <= maior:
    print(menor, end=" ")  # end=" " imprime em linha
    menor += i
