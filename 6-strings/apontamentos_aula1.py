"""
https://colab.research.google.com/drive/1uLx5n0Q8JLzToxl3OqAt49m308PLRlYQ?usp=sharing
"""


s = "Olá Mundo!"

print(s[0]) #print do primeiro caracter da string

n = len(s) #conta o nº de caracteres
print(n)

print(s[n-1]) #print do ultimo caracter da string

print(s[0:2]) #print do primeiro ao 2 caracter da string (exlusive), ou seja, posição 0(o) e 1(l)
print(s[0:8:2]) #print do primeiro ao 8 caracter da string (exlusive), de 2 em 2
print(s[3:]) #print do 3 caracter da string até ao final

for x in range (0, len(s)):   #ciclo for para imprimir letra a letra
    print(s[x])

for x in range (len(s) - 1, -1, -1):   #ciclo for para imprimir string ao contrario
   print(s[x])


################

novo_s = ""

for c in s:                 #alterar o "!" para "."
    if c == "!":
        novo_s += "."       #ou utilizar a função s = s.replace("!", ".")
    else:
        novo_s += c

print(novo_s)


a = "12"
if a.isdigit():
    print("É um número")
else:
    print("não é um número")

total_pontos = novo_s.count(".")
print("Total de pontos finais na frase:", total_pontos)