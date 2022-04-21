'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
- se ele ainda vai se alistar ao serviço militar
- se é a hora de se alistar
- se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou.'''
from datetime import date
ano=int(input("Em que ano você nasceu?"))
atual=date.today().year
idade=atual-ano #ano atual do computador - ano de nascimento
if idade<18:
    tempo_rest=18-idade
    print("\033[35mVocê tem {}, e faltam {} anos para você se alistar, em {}\033[m"
          .format(idade, tempo_rest,atual+tempo_rest))
elif idade==18:
    print("\033[1;32mVocê já tem 18 anos, e deve se alistar esse ano\033[m")
else:
    tempo_rest=idade-18
    print("\033[1;31mVocê já tem {} anos, e fazem {} anos que você deveria ter se alistado, em {}\033[m"
          .format(idade,tempo_rest,atual-tempo_rest))