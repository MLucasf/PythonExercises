'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50'''
from time import sleep
for par in range(1,51):
    if par%2==0:
        print(par)
        sleep(0.5)

'''for par in range(2,51,2): #gasta menos memória, começando do 2 e pulando de dois em dois até o 51
        print(par)
        sleep(0.5)'''