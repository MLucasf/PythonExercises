notas=0
for i in range(0,4):
    nota=float(input("Digite a sua {}ª nota:".format(i+1)))
    notas+=nota

media=notas/4
if media>=9:
    print("""Média: {}
Conceito: A
Status: Aprovado""".format(media))
elif 7.5<=media<9:
    print("""Media: {}
Conceito: B
Status: Aprovado""".format(media))
elif 6<=media<7.5:
    print("""Media: {}
Conceito: C
Status: Aprovado""".format(media))
elif 4<=media<6:
    print("""Media: {}
Conceito: D
Status: Reprovado""".format(media))
else:
    print("""Media: {}
Conceito: E
Status: Reprovado""".format(media))