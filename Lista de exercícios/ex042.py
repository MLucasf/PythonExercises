r1=str(input("Telefonou para a vítima?")).lower()
r2=str(input("Esteve no local do crime?")).lower()
r3=str(input("Mora perto da vítima?")).lower()
r4=str(input("Devia para a vítima?")).lower()
r5=str(input("Já trabalhou com a vítima?")).lower()

#acumulador também pode ser usado para "if"s !!!!!!
sim=0

#aqui eu usei "if" e não "elif" pois eu quero que a checagem do código seja feita em todas as
#variáveis. Se eu colocasse "elif", ele ia parar na primeira True
if r1=="sim":
    sim+=1
if r2=="sim":
    sim+=1
if r3=="sim":
    sim+=1
if r4=="sim":
    sim+=1
if r5=="sim":
    sim+=1


if sim==5:
    print("Você é o assassino!")
elif 3<=sim<=4:
    print("Você é cúmplice!")
elif sim==2:
    print("Você é suspeita!")
else:
    print("Você é inocente")
