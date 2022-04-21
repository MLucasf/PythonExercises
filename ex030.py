'''
Crie um programa que leia um número inteiro
e mostre na tela se ele é par ou impar
'''
num=int(input("Digite um número:"))
if num%2==0: #se o num/2 tiver resto 0, fale que ele é par
    print("O número {} é par".format(num))
else:
    print("O número {} é ímpar".format(num))
