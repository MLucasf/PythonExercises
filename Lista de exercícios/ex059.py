'''
Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares e a quantidade de números impares.
'''
par=0
impar=0
for i in range(1,11):
    num=int(input("Digite um número: "))
    if num%2==0:
        par+=1
    elif num%2!=0:
        impar+=1
print("A quantidade de números ímpares é {} e a quantidade de números pares é {}".format(impar,par))