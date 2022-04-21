'''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
'''
n1=float(input("Qual foi a sua primeira nota?"))
n2=float(input("Qual foi a sua segunda nota?"))
n3=float(input("Qual foi a sua terceira nota?"))
n4=float(input("Qual foi a sua quarta nota?"))
med=(n1+n2+n3+n4)/4
if med>6:
    print("A média é {:.1f} e você passou! Parabéns!".format(med))
else:
    print("A média é {:.1f} e você não passou. Tente novamente ano que vem.".format(med))
