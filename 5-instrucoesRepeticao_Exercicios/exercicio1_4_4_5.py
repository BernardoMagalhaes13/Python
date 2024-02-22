perguntas = 2 #variavel controlo
nome_melhor_aluno = ""
nota_melhor_aluno = 0
soma_notas = 0
total_notas = 0

while True:
    if perguntas == 2:
        nome_consola = input ("Introduza o nome: ")
        if nome_consola == "stop" or nome_consola == "STOP":
            break
        if nome_consola == "":
            print("Aviso: Nome inválido!")
        else:
            perguntas -= 1
    
    if perguntas == 1:
        nota_consola = int(input(f"Introduza a sua nota do(a) {nome_consola}: "))
        if nota_consola > 0 and nota_consola<=20: 
            perguntas = 2
            soma_notas = nota_consola + nota_melhor_aluno
            total_notas += 1
            if nota_consola > nota_melhor_aluno:
                nota_melhor_aluno = nota_consola
                nome_melhor_aluno = nome_consola
        else:
            print("Aviso: nota inválida!")

media_notas = soma_notas/total_notas

if nome_melhor_aluno == "":
    print("Não foram introduzidos quaisquer registos")
else:
    print(f"A melhor nota da turma foi do(a) {nome_melhor_aluno} com {nota_melhor_aluno} valores")
    print(media_notas)