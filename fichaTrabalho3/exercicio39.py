#Tabuada de Vários Números:
#Peça ao utilizador para inserir vários números separados por espaços. Mostre a tabuada de todos esses números.

numeros = input("Insira vários números separados por espaços: ")

# Separa os números fornecidos pelo usuário e itera sobre cada um
for x in numeros.split():
    numero = int(x)
    print(f"\nTabuada do número {numero}:")
    
    # Loop para calcular e exibir a tabuada de cada número inserido
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
