'''Escreva um programa que leia dois números inteiros e compare-os
mostrando na tela a mensagem:
-o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior, os dois são iguais'''
a=float(input("Digite um número:"))
b=float(input("Digite outro número:"))
if a>b:
    print("O primeiro númnero é maior que o segundo")
elif b>a:
    print("O segundo número é maior que o primeiro")
else:
    print("Não há valor maior, pois ambos são iguais")

