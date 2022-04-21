'''Escreva um programa que leia um número inteiro
qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binario
2 para octal
3 para hexadecimal'''
def prog():
    num=int(input("Digite um número:"))
    def conv():
        from time import sleep

        '''print("Você deseja converter o número para qual base de conversão?")'''
        '''print("[1] - Binário\n[2] - Octal\n[3] - Hexadecimal")'''
        print('''Você deseja converter o número para qual base de conversão?
        [1] - Binário
        [2] - Octal
        [3] - Hexadecimal''')
        dec=int(input())
        if dec==1:
            print("A conversão do número {} em binário é {}".format(num,bin(num)[2:])) #para começar a mostrar a partir do caracter 2
        elif dec==2:
            print("A conversão do número {} em octal é {}".format(num,oct(num)[2:]))
        elif dec==3:
            print("A conversão do número {} em hexadecimal é {}".format(num,hex(num)[2:]))
        else:
            print("Essa não é uma opção válida, tente outra opção.")
            sleep(1)
            conv()
        sleep(2)
        again=input("Deseja repetir?")
        again=again.upper()
        if again=="SIM":
            prog()
        else:
            print("Até mais!")

    conv()
prog()