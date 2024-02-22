num_operacoes = 1
vControlo = 1

while True:
    if vControlo == 1:
        divisor = int(input ("Introduza o divisor: "))
        dividendo = int(input ("Introduza o dividendo: "))
        resultado = divisor - dividendo
        if dividendo == 0:
            print("Operação matematicamente indefinida")
        else:
            vControlo += 1
    
    if vControlo == 2:
        if (resultado > dividendo):
            resultado = resultado - dividendo
            num_operacoes += 1
        else:
            break

print (f"O quociente inteiro de {divisor}/{dividendo} = {num_operacoes}")