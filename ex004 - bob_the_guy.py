'''Fazer um jogo de pedra, papel e tesoura'''
'''
1 - gerar randômicamente a posição da máquina (pedra, papel ou tesoura)
2 - receber a posição do jogador
3 - comparar a posição da máquina e a do jogador
4 - decidir o ganhador da partida de acordo com a combinação de posições:
    pedra ganha de tesoura, que ganha de papel, que ganha de pedra
5 - mostrar na tela quem ganhou a partida
'''


#diálogo para introduzir o jogador ao jogo
nome=str(input("Qual é o seu nome?"))
print("Olá, {}. Eu sou Bob. Vamos jogar um jogo de Pedra, Papel e Tesoura?".format(nome.title()))
global escolha
escolha=str(input("Responda com sim ou não:")) #essa pergunta não pode repetir

#função do código inteiro
def bobtheboy():
    from random import choice

    # gerar randomicamente a posição da máquina
    opt = ["Pedra", "Papel", "Tesoura"]
    #escolha=str(input("Responda com sim ou não:")) #essa pergunta não pode repetir
    if escolha.upper()=="SIM":


    # manter o jogo rodando até o jogador ganhar
        acertou = False
        while acertou == False:

            opt = choice(opt)

        # receber a posição do jogador
            pos = str(input("Pedra, papel ou tesoura?")).strip()


        # comparar posições
            if opt.upper() == pos.upper():
                print("Empate!")
                acertou = True
                input()

            elif opt.upper() == "PEDRA" and pos.upper() == "PAPEL":
                print("Você ganhou!")
                print("Bob jogou {}".format(opt))
                acertou = True
                #manter o programa aberto até o jogador clicar em alguma tecla
                input()

            elif opt.upper()=="PEDRA" and pos.upper()=="TESOURA":
                print ("Você perdeu!")
                acertou = True
                input()

            elif opt.upper()=="PAPEL" and pos.upper()=="TESOURA":
                print("Você ganhou!")
                print("Bob jogou {}".format(opt))
                acertou = True
                input()

            elif opt.upper()=="PAPEL" and pos.upper()=="PEDRA":
                print("Você perdeu!")
                acertou = True
                input()

            elif opt.upper()=="TESOURA" and pos.upper()=="PEDRA":
                print("Você ganhou!")
                print("Bob jogou {}".format(opt))
                acertou = True
                input()

            elif opt.upper()=="TESOURA" and pos.upper()=="PAPEL":
                print("Você perdeu")
                acertou = True
                input()

            elif opt.upper()=="PEDRA" and pos.upper()=="PAPEL":
                print("Você ganhou!")
                print("Bob jogou {}".format(opt))
                acertou = True
                input()

            else:
                print("Essa não é uma opção válida.") #quando dá uma opção inválida
                input() #todas as opções seguintes se tornam inválidas

    else:
        print("Tudo bem, nos vemos quando você quiser perder para mim!")
        input()

    restart=str(input("Você quer jogar de novo?"))
    if restart.upper()=="SIM":
        bobtheboy()
    else:
        print("Tudo bem, volte de novo quando quiser perder!")

#chama a função bobtheboy antes de todo o resto
bobtheboy()