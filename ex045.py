'''Crie um programa que faça o computador jogar jokenpô com você'''

from random import randint
from time import sleep
print("Olá, eu sou Bob!")
def inicio():
    print("Vamos jogar Jokenpo?")
    resp=str(input())
    resp=resp.upper()
    if resp=="SIM":
        def jogo():
            print("Então vamos jogar!")
            robo = ["Pedra", "Papel", "Tesoura"]
            robo_opt=randint(0,2)
            robo=robo[robo_opt]
            opt = str(input("Que posição você jogará?")).strip()
            opt = opt.lower()
            print("Jo....")
            sleep(1)
            print("Ken...")
            sleep(1)
            print("PO!!")
            print("Eu escolhi {}".format(robo))

            if opt == "pedra" and robo == "Pedra":
                print("Escolhemos a mesma posição! Empate!")
                inicio()
            elif opt == "pedra" and robo == "Papel":
                print("Ganhei!! Tente mais na próxima!")
                inicio()
            elif opt == "pedra" and robo == "Tesoura":
                print("Droga, perdi. Bom jogo.")
                inicio()
            elif opt == "papel" and robo == "Pedra":
                print("Droga, perdi. Bom jogo.")
                inicio()
            elif opt == "papel" and robo == "Papel":
                print("Escolhemos a mesma posição! Empate!")
                inicio()
            elif opt == "papel" and robo == "Tesoura":
                print("Ganhei!! Tente mais na próxima")
                inicio()
            elif opt == "tesoura" and robo == "Pedra":
                print("Ganhei! Tente mais na próxima!")
                inicio()
            elif opt == "tesoura" and robo == "Papel":
                print("Droga, perdi. Bom jogo.")
                inicio()
            elif opt == "tesoura" and robo == "Tesoura":
                print("Escolhemos a mesma posição. Empate!")
                inicio()
            else:
                print("Essa não é uma posição valida! Lembre-se, apenas Pedra, Papel ou Tesoura.")
                sleep(1)
                jogo()

        jogo()
    elif resp=="NAO" or resp=="NÃO":
        print("Ok, volte quando você quiser!")
        input()
    else:
        print("Essa não é uma resposta para a minha pergunta!")
        inicio()
inicio()


