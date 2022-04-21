'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor
'''
num1=int(input("Digite um número:"))
num2=int(input("Digite mais um número:"))
num3=(int(input("Digite um último número:")))
'''if num1>num2>num3:
    print("Os números, em ordem do maior para o menor, são {},{},{}".format(num1,num2,num3))
elif num1>num3>num2:
    print("Os números, em ordem do maior para o menor, são {},{},{}".format(num1,num3,num2))
elif num2>num1>num3:
    print("Os números, em ordem do maior para o menor, são {},{},{}".format(num2,num1,num3))
elif num2>num3>num1:
    print("Os números, em ordem do maior para o menor, são {},{},{}".format(num2,num3,num1))
elif num3>num1>num2:
    print("Os números, em ordem do maior para o menor, são {},{},{}".format(num3,num1,num2))
else:
    print("Os números, em ordem do maior para o menor, são {},{},{}".format(num3,num2,num1))'''
#testando o menor valor
menor=num1
if num2<num1 and num2<num3:
    menor = num2
elif num3<num1 and num3<num2:
    menor = num3
#testando o maior valor
maior = num1
if num2>num1 and num2>num3:
    maior=num2
elif num3>num2 and num3>num1:
    maior = num3
print("O menor valor é {} e o maior é {}".format(menor,maior))