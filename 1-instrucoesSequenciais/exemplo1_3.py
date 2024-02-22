#Variavel constante
Pi = 3.1415

#Ler valor do raio
raio = float(input("Introduza o valor do raio: "))

#Calcular
area = Pi * raio**2
perimetro = 2 * Pi * raio

#Imprimir resultados
print("area = %.2f" % area)
print("Perimetro = %.2f" % perimetro)