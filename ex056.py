'''Desenvolva um programa que leia nome, idade e sexo de quatro pessoas. No final do programa,
mostre:
A média de idade do grupo;
Qual é o nome do homem mais velho;
Quantas mulheres têm menos de 20 anos'''

count_wo=0
count_ma=0
nom_hom=""
med=0
for i in range(1,5):
    print("{:=^20}".format("{}ª pessoa").format(i))
    name = str(input("Nome:")).strip()
    age = int(input("Idade:"))
    sex=str(input("Sexo: [M/F]")).strip().lower()
    if sex=="m":
        if age>count_ma:
            count_ma=age
            nom_hom=name #como o nome vem junto da idade, sempre que uma idade for maior do que a
                        #idade anterior, o nome se tornará a variável "nom_hom"
    med+=age/4
    if sex=="f":
        if age<20:
            count_wo+=1
nom_hom=nom_hom.capitalize()
print("A média das idades é {:.1f}".format(med))
print("O número de mulheres com menos é 20 anos é {}".format(count_wo))
print("O nome do homem mais velho é {}, com {} anos".format(nom_hom,count_ma))


