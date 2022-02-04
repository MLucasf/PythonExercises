'''
Desenvolva um programa que pergunte a distancia de uma viagem em km.
Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200km
e R$0.45 poara viagens mais longas
'''
from time import sleep

dist=float(input("Qual é a distância da cidade para onde você vai?"))
sleep(2)
'''if dist<=200:
    preco=dist*0.5
    print("O valor da viagem será R${:.2f}".format(preco))
else:
    preco=dist*0.45'''
preco=dist*0.5 if dist<=200 else dist*0.45 #if ternário
print("O valor da viagem será de R${:.2f}".format(preco))