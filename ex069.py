'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:

a - quantas pessoas têm mais de 18 anos
b - quantos homens foram cadastrados
c - quantas mulheres têm menos de 20 anos
'''

idade=0
sex=""
homem=0
mais_18=0
sub_20=0

while True:
    idade=int(input("Idade: "))
    sex=" "
    while sex not in "MmFf":
        sex=str(input("Sexo: [M/F]"))
    if idade>18:
        mais_18+=1
    if sex in "Mm":
        homem+=1
    elif sex in "Ff":
        if idade<20:
            sub_20+=1
    opt=" "
    while opt not in "SsNn":
        opt=str(input("Deseja continuar? [S/N]"))
    if opt in "Nn":
       break
print(f"""- Foram cadastradas {mais_18} pessoas com mais de 18 anos\n
- Foram cadastrados {homem} homens\n
- {sub_20} mulheres cadastradas têm menos de 20 anos""")