frut=str(input("""Que fruta deseja comprar?
[MA] - Maçã
[MO] - Morango
[MM] - Morango e Maçã""")).strip().lower()
quant=0
prec=0
desc=0
prec1=0
prec2=0
quant1=0
quant2=0
if frut=="mo":
    quant = float(input("Qual quantidade você deseja comprar, em quilogramas?"))
    if quant<=5:
        prec=2.5*quant
    elif quant>5:
        prec=2.2*quant
        if quant>8 or prec>25:
            print("Você tem direito a um desconto de 10%")
            desc=prec*0.1
            prec-=desc
elif frut=="ma":
    quant = float(input("Qual quantidade você deseja comprar, em quilogramas?"))
    if quant<=5:
        prec=quant*1.8
    elif quant>5:
        prec=quant*1.5
        if quant>8 or prec>25:
            print("Você tem direito a um desconto de 10%")
            desc=prec*0.1
            prec-=desc

elif frut=="mm":
    quant1 = float(input("Qual quantidade de maçã você deseja comprar, em quilogramas?"))
    quant2=float(input("Qual quantidade de morango você deseja comprar, em quilogramas?"))
    if quant1<=5:
        prec1=quant1*1.8
#nesse caso foi necessário limitar o valor máximo de "quant1" e "quant2" para possibilitar a checagem
#por parte do programa, do outro "if" com relação ao peso
    elif 8>=quant1>5:
        prec1=quant1*1.5
    if quant2<=5:
        prec2=2.5*quant2

    elif 8>=quant2>5:
        prec2=2.2*quant2

#necessário ser outro "if" ao invés de um elif, pois é necessário que seja feita a checagem das duas
#hipóteses anteriores, e não se encaixando, aí sim será checada essa hipótese
    if quant1+quant2>8 or prec1+prec2>25:
        print("Você tem direito a um desconto de 10%")
        prec=prec2+prec1
        desc=prec*0.1
        prec-=desc

    prec=prec1+prec2

    if frut=="mo":
        frut="morango"
    elif frut=="ma":
        frut="maçã"
    elif frut=="mm":
        frut="maça e morango"

    if frut=="maçã" or frut=="morango":
        print("Foi desejado comprar {}kg de {}, no valor de R${:.2f}".format(quant, frut, prec))
    else:
        print("Foi desejado comprar {}kg de maçã e {}kg de morango, no valor de R${:.2f}"
              .format(quant1, quant2,prec))

else:
    print("Opção inválida")