"""
5) Crie uma função contaPrimos() que receba dois valores inteiros
como argumentos e retorne o número de números primos entre estes
dois números, inclusive. P. Ex. contaPrimos(3,10) deverá retornar
o valor 3 (3, 5, 7). A função deverá ser testada sendo que os dois
valores são introduzidos pelo utilizador. 
"""

def contaPrimos(a, b):
    lista_primos = []

    for num in range(a, b + 1):
        primo = True
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    primo = False
                    break

            if primo:
                lista_primos.append(num)

    return lista_primos

# Início

n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))

resultado = contaPrimos(n1, n2)

print(f"Números primos entre {n1} e {n2}: {resultado}")