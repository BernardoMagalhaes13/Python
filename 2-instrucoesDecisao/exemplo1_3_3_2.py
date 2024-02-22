notaMatematica = float(input("Introduza a nota de Matematica -> "))
notaPortugues = float(input("Introduza a nota de Portugues -> "))
notaIngles = float(input("Introduza a nota de Ingles -> "))
notaGeografia = float(input("Introduza a nota de Geografia -> "))

media = (notaMatematica + notaPortugues + notaIngles + notaGeografia) / 4

if media >= 9.5:
    print("Aprovado (%.2f valores)" % media)
else:
    print("Reprovado (%.2f valores)" % media)