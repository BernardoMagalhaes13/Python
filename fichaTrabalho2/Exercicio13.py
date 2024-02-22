red = float(input("Introduza o valor da cor vermelha -> "))
green = float(input("Introduza o valor da cor verde -> "))
blue = float(input("Introduza o valor da cor azul -> "))

if red == green and red == blue:
    print("Não existe uma cor predominante")
else:
    if red > green and red > blue:
        print("A cor predominante é vermelho")
    elif green > blue:
        print("A cor predominante é verde")
    else:
        print("A cor predominante é azul")