'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do aumento.
Para salários superiores a R$1250, calcule um aumento de 10%.
Para salários inferiores ou iguais, calcule um aumento de 15%
'''
sal=float(input("Qual é o seu salário? R$"))
if sal>1250:
    sal=sal+(sal*0.1)
    print("Seu salário com o aumento de 10% será equivalente a R${:.2f}".format(sal))
else:
    sal=sal+(sal*0.15)
    print("Seu salário com o aumento de 15% será equivalente a R${:.2f}".format(sal))