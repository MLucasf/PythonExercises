'''
Crie um programa que leia um número real qualquer pelo teclado
e mostre na tela a sua porção inteira
'''
'''
from math import trunc

num=float(input("Digite um número real: "))
print("A parte inteira de {} é {}".format(num, trunc(num)))
'''
num=float(input("Digite um número real: "))
print("A parte inteira de {} é {}".format(num,int(num))) #pega apenas a parte inteira do número sem
                                                        #a necessidade de importar a biblioteca math