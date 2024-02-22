sequencia_maior = 0
sequencia_atual = 0
num = -1
str_sequencia_maior = ""
str_sequencia_atual = ""


while True:
    num_consola = int(input("Introduza um número positivo: "))
    if num_consola == 0:
        break
    elif num_consola >= num:
        sequencia_atual += 1
        str_sequencia_atual += str(num_consola) + " "
        if sequencia_atual > sequencia_maior:
            sequencia_maior = sequencia_atual
            str_sequencia_maior = str_sequencia_atual
    elif num_consola < num:
        sequencia_atual = num_consola
        str_sequencia_atual = str(num_consola) + " "
    num = num_consola

if sequencia_maior > 1:
    print(f"A maior sequência de números crescentes teve um total de {sequencia_maior} números")
    print(f"A sequencia foi: {str_sequencia_maior}")
else:
    print("Não existiu nenhuma sequência crescente")