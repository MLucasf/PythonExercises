'''
Leia um programa que leia um número de 0 a 9999 e mostre na tela cada um dos seus digitos separados

ex: 1834
unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
'''
num=int(input("Digite um número: "))
#// -> divide e exclui tudo após a vírgula
#% -> divide e exclui tudo antes da vírgula
# 123//10 = 12.3 -> exclui o 3
# 12%10 = 1.2 -> exclui o 1. Logo 123//10%10 = 2
un=num//1%10
dez=num//10%10
cent=num//100%10
mil=num//1000%10
millhao=num//10000%10
print("A unidade do número é {} \nA dezana do número é: {} \nA centena do número é: {} \nO milhar do número é {}"
      " \nO milhão do número é {}".format(un,dez,cent,mil,millhao))