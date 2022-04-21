'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
vai continuar. No final, mostre:

a - Qual é o total gasto na compra
b - Quantos produtos custam mais de R$1000
c - Qual é o nome do produto mais barato
'''

nome=""
preco=0
barato_nome=""
barato_preco=0
mais_1000=0
total=0
count=0
prog=True

print(f"{'Supermercado Blábláblá':-^20}")
while prog==True:
    nome=str(input("Nome do produto: "))
    preco=float(input("Preço do produto: R$"))
    count += 1
    total += preco
    if count==1 or preco<barato_preco: #pega o primeiro termo sempre
        barato_preco=preco
        barato_nome=nome
    '''if count!=0: #passará a considerar a partir do segundo termo
        if preco<barato_preco:
            barato_nome=nome        #foi colocado no if anterior, por fazerem a mesma coisa
            barato_preco=preco'''
    if preco>1000:
        mais_1000+=1
    opt = " " #deve ser iniciada dentro do while para que o input seja requerido toda vez
    while opt not in "SsNn":
        opt=str(input("Deseja adicionar outro produto? [S/N]"))[0]
        if opt in "Ss":
            prog=True
        elif opt in "Nn":
            prog=False
            break
        else:
            print("Opção não aceita")
print(f"""- O total gasto nas compras foi R${total:.2f}
- {mais_1000} produtos custam mais de R$1000.00
- O produto {barato_nome.capitalize()} é o mais barato""")