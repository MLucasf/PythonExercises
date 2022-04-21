'''Escreva um programa que leia um número 'n' inteiro qualquer e mostre na tela
os 'n' primeiros elementos de uma sequência de fibonacci'''

'''se n = 10, mostre os 10 primeiros elementos da sequencia de fibo
n1 = 1
n2 = 1
n3 = n1+n2
    {
    n4=n3+n2
    if n2=n1 and n1=num
        n4= (novo)n1 + (novo)n2
    }
        ex: 
            n1 = 1
            n2 = 1
            n3=1 + 1
            n3 = 2
            n2 passa a ser 1
            e n1 passa a ser 2
            n4 = n1 + n2 (2 e 1 respectivamente)
            n4 = 3
            n2 passa a ser 2
            n1 passa a ser 3
            n5 = n1 + n2
            n5 = 5 
            
n1 = n3-n2
n10 = n9+n8
n10 = n12-n11
'''

n=int(input("Quantos termos da sequência de fibonacci você quer ver?"))
num1=0
num2=1
ele=0
print("Os {} primeiros termos da seqência de fibonacci são: 0".format(n),end=" ")
while ele<(n-1):
    num=num1+num2 #número que eu quero saber
    num2=num1 #para manter o calculo sendo feito, os termos devem "voltar" uma casa
    num1=num #o n3 sempre passará a ser o n2, e o n2 sempre passará a ser o n1
            #uma vez que eu só tenho essas três variáveis para trabalhar
    ele+=1
    print("{}".format(num),end=" ")