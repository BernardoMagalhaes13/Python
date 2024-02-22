from math import floor 
dias = int(input("Introduza a quantidade de dias a converter em semanas -> "))

semanas = dias / 7
restoSemana = dias % 7

print(dias, "dias são", floor(semanas), "semanas e", restoSemana, " dias")