'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

while True:
    nome=str(input("Nome: "))
    idade=int(input("Idade: "))
    salario=float(input("Salário: "))
    sexo=str(input("Sexo [M/F]: "))
    est_civ=str(input("Estado Civil [S/C/V/D]:"))
    if len(nome)>3 and 0<=idade<=150 and salario>0 and sexo in "MmFf" and est_civ in "SsCcVvDd":
        print("Dados validados")
        break
    else:
        print("Dados não validados")
