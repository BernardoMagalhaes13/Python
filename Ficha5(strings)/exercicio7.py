#Crie um programa que inverta uma string.

s = str(input("Intruduza a string a inverter: "))

for x in range (len(s) - 1, -1, -1):   #ciclo for para imprimir string ao contrario
   print(s[x], end="")