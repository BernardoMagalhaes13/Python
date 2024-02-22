#Crie um programa que leia 2 strings do utilizador e indique qual das strings está primeiro na ordem alfabética.

s1 = str(input("Introduza a primeira string: "))
s2 = str(input("Introduza a segunda string: "))

if s1 < s2:
    print("A 1ª string está primeiro na ordem alfabetica")
elif s2 < s1:
    print("A 2ª string está primeiro na ordem alfabetica")
else:
    print("A duas string estão igualmente classificadas na ordem alfabetica")