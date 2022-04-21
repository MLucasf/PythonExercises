'''Faça um programa que leia o sexo de uma pessoa, mas só aceite valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sex=" "
tent=0
while sex != "M" and sex != "F":
    sex=str(input("Qual é o seu sexo? [M/F]")).upper()
    tent+=1

if sex=="M":
    sex="masculino"
elif sex=="F":
    sex="feminino"

if tent>6:
    print("Você com certeza tem demência, já que levou {} tentativcas para acertar a tecla".format(tent))
elif tent>3:
    print("Você tem um certo retardo, afinal levou {} tentativas para acertar a tecla".format(tent))

print("Seu sexo é {}".format(sex))

'''sex=str(input("Digite o seu sexo: [M/F])).strip().upper()[0] #fatiamento pegando apenas o primeiro 
                                                                #valor da string
while sex not in "MF":
    sex=str(input("Opção inválida. Digite o seu sexo: [M/F])).strip().upper()[0]
print("Sexo {} validado com sucesso".format(sex))'''
