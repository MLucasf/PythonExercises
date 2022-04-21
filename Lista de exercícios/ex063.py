'''
Faça um programa que, dado um conjunto de N números, determine:
A - o menor valor
B - o maior valor
C - a soma dos valores
'''

numIn=int(input("Digite o número inicial: "))
numFi=int(input("Digite o número final: "))
menor=maior=0
som=0

for i in range(numIn,numFi+1):
    if i==numIn:
        maior=i
        menor=i
    if i!=numIn:
        if i>maior:
            maior=i
        if i<menor:
            menor=i
    som+=i
print("""A - O menor valor é {}
B - O maior valor é {}
C - A soma dos valores é {}""".format(menor,maior,som))