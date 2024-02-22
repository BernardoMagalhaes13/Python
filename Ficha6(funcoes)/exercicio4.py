"""
4) Crie uma função que receba um número inteiro como argumento e
retorne o maior valor primo inferior a esse argumento. Se o
argumento for negativo, a função deverá retornar o valor zero. 
"""

def e_primo(a):
    if a < 2:
        return False
    for x in range(2, a):
        if a % x == 0:
            return False
    return True

def maior_primo_inferior(a):
    if a < 0:
        return 0

    while a >= 2:
        a -= 1
        if e_primo(a):
            return a

    return 0

# Exemplo de uso
numero = int(input("Digite um número: "))
resultado = maior_primo_inferior(numero)

print(f"O maior valor primo inferior a {numero} é: {resultado}")