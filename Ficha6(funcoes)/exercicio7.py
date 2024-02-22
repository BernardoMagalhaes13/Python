'''
7) Crie uma função que receba dois valores inteiros como argumentos
e retorne um valor booleano indicando se os números são divisíveis. 
'''

def sao_divisiveis(a, b):
    if a % b == 0 or b % a == 0:
        return True
    else:
        return False
    
#inicio
    
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))

final = sao_divisiveis(n1, n2)

if final:
    print("Os números são divisiveis")
else:
    print("Os números não são divisiveis")