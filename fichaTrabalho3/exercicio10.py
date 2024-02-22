#Escreva um programa para ler as notas de n alunos (sendo n introduzido pelo utilizador).
#As notas deverão estar entre 1 e 5. O programa deverá contar quantos alunos tiveram cada uma das notas possíveis.

notas_validas = 0
num_alunos = int(input("Introduza o número total de alunos: "))

for x in range(1, num_alunos + 1):
    nota = int(input(f"Introduza a nota do {x}º aluno: "))
    if nota >= 1 and nota <= 5:
        notas_validas += 1
    
print(f"Das {num_alunos} notas introduzidas, {notas_validas} foram validas (entre 1 e 5)")