dia=int(input("Digite uma data: "))
mes=int(input("Digite um mês: "))
ano=int(input("Digite um ano: "))

if mes<=12:
    if mes==2 or mes==4 or mes==6 or mes==9 or mes==11:
        if dia>30:
            print("A data não é válida")
        else:
            print("A data é {}/{}/{}".format(dia, mes, ano))
    elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        if dia>31:
            print("A data não é válida")
        else:
            print("A data é {}/{}/{}".format(dia,mes,ano))
else:
    print("A data não é válida")
