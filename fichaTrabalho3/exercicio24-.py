# Sequencia de Fibonacci
 
nvezes = int(input("Quantos ciclos "))
 
# first two terms
n1, n2 = 0, 1
count = 0
 
# Verificar o numero de vezes
while nvezes <= 1:
   print("Introduza um numero de ciclo valido")
   nvezes = int(input("Quantos ciclos "))
 
# Gerar sequencia fibonacci
while count < nvezes:
    print(n1)
    nth = n1 + n2
    # Atualizar variaveis
    n1 = n2
    n2 = nth
    count += 1
    