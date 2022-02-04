'''Faça um programa que mostre na tela a contagem regressiva para o estouro
de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles'''
from time import sleep

print("{:*^40}".format("Feliz ANO NOVO"))

for boom in range(10,-1,-1): #vai de 10 até o caracter -1 (no caso o 0), diminuindo 1 valor
    print(boom)
    sleep(1)
print("BOOOOOM!! ***")

for i in range(0,10,2): #vai do 0 ao 10 contando ed dois em dois
    print(i)