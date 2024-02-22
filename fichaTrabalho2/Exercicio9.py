a1 = float(input("Introduza a amplitude do 1º angulo do triangulo -> "))
a2 = float(input("Introduza a amplitude do 2º angulo do triangulo -> "))

a3 = 180 - a1 - a2

if a3 < 180 and a3 > 0:
    print("É um triangulo, e o 3º angulo é de ", a3)
else:
    print("Não é um triangulo")