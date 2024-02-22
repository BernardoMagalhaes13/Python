#ler dados
peso = float(input("Introduza o seu peso (em kilos): "))
altura = float(input("Introduza a sua altura (em metros): "))

#calcular
imc = peso / altura**2

#imprimir resultados
print("O seu IMC é = ", imc)