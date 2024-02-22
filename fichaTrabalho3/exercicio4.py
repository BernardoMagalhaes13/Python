#Crie um programa que escreva os números inteiros entre 0 e 100 em intervalos (incremento) dados pelo utilizador.
#O intervalo deverá ser um número entre 1 e 10. (Por exemplo, com intervalos de 4).

intervalo = int(input("Introduza um intervalo (entre 1 e 10): "))

for x in range(0, 101, intervalo):
    print(x)