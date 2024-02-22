print("Insira o maior numero:")
a = int(input())

print("Insira o menor numero:")
b = int(input())

if b%a:
    print("", a, "é multiplo de ", b)
else:
    print("", a, "não é multiplo de ", b)