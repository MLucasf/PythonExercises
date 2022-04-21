'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre a sua categoria, de acordo com a idade:
- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: junior
- até 25 anos: senior
- acima: master'''
from datetime import date

atual=date.today().year
ano=int(input("Ano de nascimento:"))
idade=atual-ano
if idade<=9:
    print("A idade é {} e por isso a sua categoria é a \033[31mmirim\033[m.".format(idade))
elif 9<idade<=14:
    print("A idade é {} e a sua categoria é a \033[32minfantil\033[m".format(idade))
elif 14<idade<=19:
    print("A idade é {} e a sua categoria é a \033[33mjunior\033[m".format(idade))
elif 19<idade<=25:
    print("A idade é {} e a sua categoria é a \033[34msênior\033[m".format(idade))
else:
    print("A idade é {} e a sua categoria é a \33[35mmaster\033[m".format(idade))