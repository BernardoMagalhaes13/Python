print("Insira um número:")
num = int(input())

if num > 999 and num < 10000:
    print("O número tem 4 algarismos")
elif num < 1000:
    print("O número tem menos de 4 algarismos")
elif num >= 10000:
    print("O número tem mais de 4 algarismos")