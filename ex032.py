'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto
'''
'''ano=int(input("Digite um ano qualquer:"))
if ano%4==0:
    print("Este ano será bissexto")
else:
    print("Este ano não é um ano bissexto")'''
from datetime import date

ano=int(input("Digite um ano qualquer:"))
if ano==0:
    ano=date.today().year #se o ano for 0, ano = ano da data estipulada pelo computador
if ano%4==0 and ano%100!=0 or ano%400==0: #expressão com todas as exceções para anos bissextos
    print ("O ano {} será bissexto".format(ano))
else:
    print ("O ano {} não será bissexto".format(ano))
