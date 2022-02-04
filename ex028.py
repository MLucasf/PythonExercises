'''
Escreva um programa que faça o computador "pensar" em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
escolhido.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import choice
from time import sleep
numR=choice(range(0,5)) #seleciona um número aleatório entre 0 e 5
print("Olá, sou Bobby.")
num1=int(input("Adivinhe o número em que estou pensando de 0 a 5."))
print("PROCESSANDO...")
sleep(3) #faz o programa aguardar 3 segundos para continuar rodando
if num1==numR:
    print("Parabéns, você acertou!!")
else:
    print("Errou, o número que eu estava pensando era {}".format(numR))
