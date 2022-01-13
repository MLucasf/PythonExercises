'''
Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
'''
sal=float(input("Qual é o seu salário? "))
sal_novo=sal+(sal*0.15) #sal+(sal*(15/100))
print("O seu salário acrescido de 15% equivale a {:.2f}".format(sal_novo))

