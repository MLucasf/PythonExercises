'''
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido
'''
while True:
    num=int(input("Digite um número entre 0 e 10: "))
    if 0>num or num>10:
        print("Número inválido")
    if 0<=num<=10:
        print("Número válido")
        break