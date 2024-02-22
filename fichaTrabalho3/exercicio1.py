linha1 = ""
linha2 = ""

for x in range(1, 11):
    x_string = str(x)
    linha1 += f"{x_string} "

for y in range(10, 0, -1): # o -1 indica que o ciclo for começa no 10 e decrementa de -1 em -1 até ao 1
    y_string = str(y)
    linha2 += f"{y_string} "
    
print (linha1)
print (linha2)