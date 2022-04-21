'''Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número
de 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer'''

from random import randint
from time import sleep

num_maq=randint(0,10)

print("Vamos jogar um jogo?")
start=str(input("[S/N] ")).strip().upper()

if start=="S":
    print("Eu pensei em um número de 0 a 10")
    sleep(1)
    tent=0
    opt=999
    while opt!=num_maq:
        opt = int(input("Digite o número que você acha que eu pensei:"))
        if opt!=num_maq:
            print("Não foi esse, tente novamente.")
        tent+=1
    if opt==num_maq:
        print("Parabéns! Você acertou! O número de tentativas até acertar foi {}".format(tent))
elif start=="N":
    print("Volte quanto você quiser jogar!")
else:
    print("Não sei o que você quer dizer com isso")

'''
from random import randint
acertou=False
palpites=0
computador=randint(0,10)

while not acertou: #enquanto acertou é False
    jogador=int(input(Dê o seu palpite))
    palpites+=1
    if jogador==computador:
        acertou=True
    else:
        if jogador>computador:
            print("Tente um pouco menos")
        else:
            print("Tente um pouco mais")
print("Parabéns. Foram necessárias {} tentativas".format(palpites))'''