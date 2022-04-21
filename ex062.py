'''melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns
termos. O programa encerra quando ele disser que quer que sejam mostrados 0 termos'''

'''from time import sleep

opt=1
count=1
while opt!=0:
    num = int(input("Digite o primeiro termo de uma PA: ")) #precisa estar dentro do while pois
                                                            #teremos que perguntar toda vez que o
                                                            #programa reiniciar
    raz = int(input("Digite a razão dessa PA: "))
    dec_num = num + (10 - 1) * raz
    n = num
    print("Os valores da PA de razão {} são: {}".format(raz,num),end=" ")
    while n!=dec_num: #enquanto n for diferente do décimo termo da PA
        n+=raz #n = n + razão
        count+=1
        print("{}".format(n),end=" ")

    reset="s"
    while reset!="n":
        reset=str(input("\nDeseja ver mais algum termo? [S/N] ")).strip().lower()
        if reset=="s":
            x_num=int(input("Quantos termos você deseja ver a mais?"))
            x_num=num+(x_num+10-1)*raz #quantidade de termos a mais + quantidade de termos já expressa - 1 * raiz
                                        #equivale ao último termo requerido da PA (fórmula de PA)

            while n!=x_num:
                n+=raz
                count+=1
                print("{}".format(n),end=" ")
        elif reset=="n":
            print("Foram mostrados {} termos da Progressão Aritmética".format(count))
            print("Volte quando desejar.")
        else:
            print("Opção inválida")
    opt=int(input("\nPara rodar o projeto novamente, digite 1. Para encerrá-lo, digite 0 "))

print("Obrigado por usar o nosso serviço")
sleep(2)'''

from time import sleep
opt="1"
while opt=="1":
    primeiro_num=int(input("Digite o primeiro termo de uma PA: "))
    raz=int(input("Digite a razão da PA: "))
    termos=primeiro_num
    i=0
    while i<10:
        print(termos,end=" ")
        termos+=raz
        i+=1

    denovo="s" #se denovo for algo diferente de "s" ele reseta completamente o programa
    while denovo=="s":
            denovo=str(input("\nDeseja ver outros números dessa PA? [S/N]")).strip().lower()
            if denovo=="s":
                nov_num=int(input("Você deseja ver quantos termos a mais?"))
                nov_num+=i
                while i<nov_num:
                    print(termos,end=" ")
                    termos+=raz
                    i+=1
            elif denovo=="n":
                print("Tudo bem. Até mais")
                print("Foram mostrados {} termos da PA".format(i))
            else:
                print("Opção inválida") #reseta completamente o programa
                sleep(1)
    opt=str(input("""Deseja reiniciar o programa?
[1] - SIM
[0] - NAO"""))

