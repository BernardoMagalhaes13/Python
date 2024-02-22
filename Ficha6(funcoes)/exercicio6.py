""""
6) Crie uma função que receba 2 notas (F1 e F2) de um aluno e
retorne um booleano indicando se o aluno passou. Para passar, a
soma das notas deve ser igual ou superior a 19 e ambas devem ser
superiores a 7.
"""

def aluno(a, b):
    soma_notas = a + b

    if (a > 7) and (b > 7):
        if soma_notas >= 19:
            return True
        else:
            return False

#Inicio
            
f1 = int(input("Digite a 1ª nota: "))
f2 = int(input("Digite a 2ª nota: "))

final = aluno(f1, f2)

if final:
    print("O Aluno passou")
else:
    print("O Aluno não passou")
