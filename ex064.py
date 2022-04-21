'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando a condição de parada - flag)'''


flag=0
n=0
num=0
while flag!=999:
    flag=int(input("Digite um número: "))
    if flag!=999:
        n=flag+n
        num+=1


print("Foram digitados {} números, e a soma deles é {}".format(num,n))

'''num=0
count=-1
soma=0
while num!=999:
    count+=1 #zera a contagem na primeira vez
    soma+=num
    num=int(input('Num: ')) #modifica o valor de num -> se for igual 999 de primeira, terá a soma e a contagem como 0 
print('Quandade: {}\nSoma: {}'.format(count,soma))'''