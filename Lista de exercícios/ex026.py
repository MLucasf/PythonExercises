print("{:*^100}".format("Bem vindo ao Ajudante Pessoal"))
prod1=str(input("Digite o nome do produto: "))
prec1=float(input("Digite o preço: "))
prod2=str(input("Digite o nome do produto: "))
prec2=float(input("Digite o preço: "))
prod3=str(input("Digite o nome do produto: "))
prec3=float(input("Digite o preço: "))

menor=prec1

if prec2<prec1 and prec2<prec3:
    menor=prec2
elif prec3<prec1 and prec3<prec2:
    menor=prec3

if menor==prec1:
    print("É recomendável comprar o produto {}, pois seu valor é mais baixo, sendo R${:.2f}".format(prod1,menor))
elif menor==prec2:
    print("É recomendável comprar o produto {}, pois seu valor é mais baixo, sendo R${:.2f}".format(prod2,menor))
else:
    print("É recomendável comprar o produto {}, pois seu valor é mais baixo, sendo R${:.2f}".format(prod3,menor))