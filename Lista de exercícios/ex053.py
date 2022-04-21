'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

som=0
med=0
count=0
while count<5:
    num=int(input("Digite um número: "))
    som+=num
    med=som/5
    count+=1
print("A soma dos números é {}, e a média é {}".format(som, med))
