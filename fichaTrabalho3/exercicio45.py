#Média Ponderada
#Peça ao utilizador para introduzir várias notas e os respetivos pesos. Calcule e apresente a média ponderada dessas notas.

media_final = 0
num_testes = int(input("Quantos testes foram realizados? "))

for x in range(1, num_testes + 1):
    nota = int(input(f"Introduza a nota do {x}º teste: "))
    peso = int(input(f"Introduza o peso do {x}º teste (ex: 30): "))
    media_teste = nota * (peso / 100)
    media_final += media_teste

print(media_final)
