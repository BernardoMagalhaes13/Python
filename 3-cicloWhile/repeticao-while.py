nota = -1

while nota < 0 or nota > 20:
    nota = int(input("Introduzir nota entre 0-20 -> "))

print("Nota:", nota)
nota = -1

while not (nota >= 0 and nota <=20):
    nota = int(input("Introduzir nota entre 0-20 -> "))