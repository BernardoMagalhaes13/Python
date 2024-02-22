#Crie um programa que, numa string substitua todas as letras “v” por “b” e todas as ocorrências de “ão” por “om”. 

s = str(input("Introduza a string: "))

s = s.replace("v", "b")
s = s.replace("ão", "om")

print (s)