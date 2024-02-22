def fibonacci(n):
    fib_sequence = [0, 1]

    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

# Solicita ao usuário o termo desejado
termo_limite = int(input("Digite o número de termos desejado para a sequência de Fibonacci: "))

# Imprime a sequência de Fibonacci até o termo inserido pelo usuário
print(f"Sequência de Fibonacci até o termo {termo_limite}: {fibonacci(termo_limite)}")
