#Escreva um programa que apresente a tabuada dum número inteiro entre 1 e 9 dado pelo utilizador. 
#Se o número estiver fora dessa gama, o programa deverá dar uma mensagem.

num = int(input("Introduza um número (entre 1 e 9): "))

while num < 1 or num > 9:
    num = int(input("NÚMERO INVÁLIDO! Introduza um número (entre 1 e 9): "))
        
for x in range (0, 11):
    res = num * x
    print (num,"X", x, "=", res)
    x += 1   