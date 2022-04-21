'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o
maior e o menor peso lidos'''

maior = 0
menor = 999
for i in range(1, 6):
    peso = int(input("Qual é o seu peso, {}?".format(i)))
    if peso > maior:  # todo input será maior do que 0
        # ele ficará comparando inputs até encontrar o maior dos inputs
        maior = peso
        #esse if fica dentro do outro pois todo valor será maior do que 0
        #e se ele cair do crivo do if anterior, não será utilizado no elif.
        #Era necessário outro if para compará-lo com o valor da variável "menor"
        if peso < menor:  # todo input será menor do que 999
            # ele ficará comparando até encontrar o menor dos inputs
            menor = peso

print(maior, menor)


'''
maior=0
menor=0
for i in range(1,6):
    peso=float(input("Digite o peso:"))
    if i==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        elif peso< menor:
            menor=peso

print(maior, menor)
'''