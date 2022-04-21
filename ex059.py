'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números #digitar novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

n=0
val1=int(input("Digite um valor: "))
val2=int(input("Digite um valor: "))
valf=0
while n != 5:
    print("""Selecione uma das opções:
    [1] - Soma
    [2] - multiplicação
    [3] - Maior
    [4] - Novos valores
    [5] - Encerrar programa""")
    n=int(input())
    if n == 1:
        valf=val1+val2
        print("A soma dos valores é {}\n".format(valf))
    elif n==2:
        valf=val1*val2
        print("A multiplicação dos valores é {}\n".format(valf))
    elif n==3:
        if val1>val2:
            print("{} é maior do que {}\n".format(val1,val2))
        elif val1==val2:
            print("Os valores são iguais.")
        else:
            print("{} é maior do que {}\n".format(val2,val1))
    elif n==4:
        print("digite novos números")
        val1=int(input("Digite o novo valor: "))
        val2=int(input("Digite o novo valor: "))
        print(" ")
    elif n==5:
        print("Finalizando...")
    else:
        print("Opção inválida\n")
    sleep(1)

print("Obrigado pelo uso do serviço.")