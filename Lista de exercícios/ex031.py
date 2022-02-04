def num_dia():
    dia=int(input("Digite um número de 1 a 7: "))

    if dia==1:
        print("1 - Domingo")
        num_dia()
    elif dia==2:
        print("2 - Segunda-feira")
        num_dia()
    elif dia==3:
        print("3 - Terça-feira")
        num_dia()
    elif dia==4:
        print("4 - Quarta-feira")
        num_dia()
    elif dia==5:
        print("5 - Quinta-feira")
        num_dia()
    elif dia==6:
        print("6 - Sexta-feira")
        num_dia()
    elif dia==7:
        print("7 - Sábado")
        num_dia()
    else:
        print("Número inválido")
        num_dia()

num_dia()