#ler 100 valor e determinar max e min

num_max = 0
num_min = 10000000000000000
for x in range(1, 11):
    num_consola = int(input(f"Introduza o {x}º numero: "))
    if num_consola <= num_min:
        num_min = num_consola
    elif (num_consola >= num_max):
        num_max = num_consola

print (f"O número máximo é {num_max} e o número minimo é {num_min}")