'''crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores'''

from datetime import date

quant_ma=0
quant_me=0

for i in range(1,8):
    ano=int(input("Ano de nascimento da {}ª pessoa: ".format(i)))
    idade=date.today().year-ano
    if idade>21:
        quant_ma+=1
    else:
        quant_me+=1
print("A quantidade de maiores de 21 é {}".format(quant_ma))
print("A quantidade de menores de 21 é {}".format(quant_me))