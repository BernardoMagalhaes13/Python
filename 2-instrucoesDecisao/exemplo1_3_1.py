#ler medidas dos lados
lado1 = int(input("Introduza o lado 1: "))
lado2 = int(input("Introduza o lado 2: "))

area = lado1 * lado2

if lado1 == lado2:
    print("Área do quadrado -> ", area)
else:
    print("Área do retangulo -> ", area)