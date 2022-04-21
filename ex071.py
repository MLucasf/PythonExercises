'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada
valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
'''

'''val=int(input("Digite o valor que você deseja sacar: R$"))

while True:
    nota_50 = val / 50
    val%=50
    nota_20 = val / 20
    val%=20
    nota_10 = val / 10
    val%=10
    nota_1 = val / 1
    break

print(f"""Notas de 50: {nota_50:.0f}
Notas de 20: {nota_20:.0f} #arredonda para cima, o que faz com que o valor sacado seja maior do que o desejado
Notas de 10: {nota_10:.0f}
Notas de 1: {nota_1:.0f}""")'''

valor = int(input("informe o valor a ser sacado : "))
nota50 = valor // 50
valor %=  50
nota20 = valor // 20 #divisão inteira (pega apenas a parte inteira da divisão)
valor %= 20
nota10 = valor // 10
valor %= 10
nota1 = valor // 1
print(f"notas de 50 = {nota50}")
print(f"notas de 20 = {nota20}")
print(f"notas de 10 = {nota10}")
print(f"notas de 1 = {nota1}")

'''valorSaque = int(input('Valor do saque: R$ '))
print('-' * 40)
for nota in [50, 20, 10, 1]:
    quantidade = valorSaque // nota
    valorSaque = valorSaque % nota
    if quantidade > 0:
        print(f'{quantidade} notas de R$ {nota}')'''


'''
val=float(input("Digite o valor que será sacado: R$"))
total=val
ced=50
totced=0
while True:
    if total>=ced:
        total-=ced
        totced+=1
    else:
        if totced>0: #mostrará apenas as cédulas que foram utilizadas
            print(f"Total de {totced} cédulas de R${ced}")
        if ced==50:
            ced=20
        elif ced==20:
            ced = 10
        elif ced==10:
            ced=1
        totced=0
        if total==0:
            break
print("Volte sempre ao banco do Lucas")
'''