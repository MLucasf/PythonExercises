'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/hr, mostre uma mensagem dizendo que ele foi multado e o valor da multa.
A multa custa R$7,00 por cada km acima do limite
'''

from random import randrange
from time import sleep

velR=randrange(60,180)
print(("Você estava dirigindo a {}km em uma pista de 80km".format(velR)))
sleep(3)
if velR>80:
    print("Você será multado em R${:.2f}".format(7*(velR-80)))
else:
    print("Você não será multado!")

input()