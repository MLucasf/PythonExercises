'''
Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas que ela conquistou no final do jogo
'''

from random import randint

def gameplay():

    game=str(input("Você quer jogar um jogo de par ou ímpar? [S/N]"))
    count = 0

    if game in "Ss":
        game=True
    elif game in "Nn":
        game=False
        print("Tudo bem, volte quando quiser!")
    else:
        print("Não reconheço essa opção, tente de novo")
        gameplay()


    while game==True:
        rbt=randint(0,10)
        num=int(input("Digite um número, de 0 a 10: "))
        res=(rbt+num)%2
        if num>10:
            print("Você tem mais de 10 dedos? Escolha um número entre 0 e 10!")
        else:
            opt = str(input("Você quer par ou ímpar? [P/I]"))
            if opt in "Pp":
                if res==0:
                    print(f"O computador jogou {rbt} e você jogou {num}")
                    print("Parabéns, você ganhou!")
                    count+=1
                else:
                    print(f"O computador jogou {rbt} e você jogou {num}")
                    print("Aah, você perdeu!")
                    break
            elif opt in "Ii":
                if res!=0:
                    print(f"O computador jogou {rbt} e você jogou {num}")
                    print("Parabéns, você ganhou!")
                    count+=1
                else:
                    print(f"O computador jogou {rbt} e você jogou {num}")
                    print("Aah, você perdeu!")
                    break
            else:
                print("Essa opção não é válida, tente nvamente.")


    print(f"Você ganhou {count} rodadas")
gameplay()
