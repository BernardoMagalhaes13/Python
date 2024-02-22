#Escreva um programa em que o utilizador vai introduzindo as idades dos alunos de uma determinada turma até ser introduzido o número -1.
#No fim deverá indicar o número de alunos e a média de idades. 
#O programa deverá garantir que apenas são introduzidos números positivos (com a exceção do -1 final).

idade = 0
tAlunos = 0
soma = 0

while True:
    idade = int(input("Introduza a idade do aluno (-1 para terminar): "))
    if idade >= 1:
        tAlunos += 1
        soma +=  idade
    elif idade < -1:
        print("A idade tem de ser positiva!")
    elif idade == -1:
        break

media = soma / tAlunos

print(f"Total de alunos: {tAlunos}\nMédia de idades: {media}")