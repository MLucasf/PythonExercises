ano=int(input("Digite o ano a ser analisado: "))

if ano%4==0 and ano%100!=0 or ano%400==0:
    print("O ano será bissexto")
else:
    print("O ano não será bissexto")
