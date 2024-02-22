num1 = float(input("Introduza o numero 1 -> "))
num2 = float(input("Introduza o numero 2 -> "))
num3 = float(input("Introduza o numero 3 -> "))

if num1 == num2 and num1 == num3:
    print("Numeros iguais")
else:
    if num1 > num2 and num1 > num3:
        print("%d é o maior de todos" % num1)
    elif num2 > num3:
        print("%d é o maior de todos" % num2)
    else:
        print("%d é o maior de todos" % num3)