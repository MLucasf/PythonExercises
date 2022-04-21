'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

num=int(input("Digite o número que você deseja checar se é primo: "))
div=0

for i in range(1,num+1):
    if num%i==0:
        div+=1
if div==2:
    print("O número {} é primo".format(num))
else:
    print("O número {} não é primo".format(num))