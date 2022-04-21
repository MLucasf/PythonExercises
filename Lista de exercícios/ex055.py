'''
Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles
'''

num_in=int(input("Digite o número inicial: "))
num_fi=int(input("Digite o número final: "))

for i in range(num_in+1,num_fi):
    print(i)