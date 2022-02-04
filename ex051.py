'''Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética.
No final, mostre os 10 primeiros termos dessa progressão.'''
num1=int(input("Digite o valor inicial da Progressão Aritmética: "))
raz=int(input("Digite a razão da Progressão Aritmética: "))
'''enésimo termo de uma PA:
primeiro termo + (10[posição do número da PA que eu quero]-1)*razão'''
fim=num1+(10-1)*raz
for i in range(num1,fim+raz,raz): #pois o python ignoraria o décimo termo, então precisa somar ele à razão
    print("-> {}".format(i),end=" ")