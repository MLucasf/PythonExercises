'''
Faça um programa que leia 5 números e informe o maior número.
'''

count=0
maior=0
while count<5:
    num=int(input("Digite um número: "))
    if count==0:
        maior=num
    if count!=0:
        if num>maior:
            maior = num
    count+=1
print("O maior número da sequência é {}".format(maior))
