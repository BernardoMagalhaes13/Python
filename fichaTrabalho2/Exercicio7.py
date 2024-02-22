import math

# ler valores dos lados
cont = 1
a = float(input(f"Introduza o valor do lado {cont} -> "))
cont = cont + 1  # <=> cont += 1
b = float(input(f"Introduza o valor do lado {cont} -> "))
cont += 1
c = float(input(f"Introduza o valor do lado {cont} -> "))

# verificar se podem formar um triangulo
if a + b > c and a + c > b and b + c > a:
    saida = "Os valores dos lados podem formar um triangulo "
    if a == b and a == c:
        saida += "equilatero."
    elif a == b or b == c or a == c:
        saida += "isosceleso."
    else:
        saida += "escaleno."
        if a > b and a > c:
            maior = a
            soma_quad = b**2 + c**2
        elif b > a and b > c:
            maior = b
            soma_quad = a**2 + c**2
        else:
            maior = c
            soma_quad = a**2 + b**2

        # classificar o triangulo
        if maior**2 == soma_quad:
            saida += "\nTiangulo retangulo"
        elif maior**2 > soma_quad:
            saida += "\nTriangulo obtusangulo"
        else:
            saida += "\n Triangulo acutangulo"

        # calcular a area usando a formula heron
        # semi «-perimetro (s) = (a + b + c) / 2
        # area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        saida += f"\n Area do Triangulo: {area}"
        print(saida)

        # calcular os angulos (opcional)
        angulo_a = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angulo_b = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angulo_c = 180 - angulo_a - angulo_b

        print(
            "\nAngulo A: %.2f \nAngulo B: %.2f \nAngulo C: %.2f"
            % (angulo_a, angulo_b, angulo_c)
        )

else:
    print("Os valores dos lados não podem formar um triangulo.")
