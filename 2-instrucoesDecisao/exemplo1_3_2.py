# ler letra
letra = input("Introduza letra (L/D/F): ")

if letra == "l" or letra == "L":
    print("Ligar")
elif letra == "d" or letra == "D":
    print("Desligar")
elif letra == "f" or letra == "F":
    print("Furar")
else:
    print("Operação inválida")