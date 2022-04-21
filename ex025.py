'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
'''
nome=str(input("Qual é o seu nome completo?")).strip().upper()
if "SILVA" in nome:
    print("Seu nome possui Silva.")
else:
    print("Seu nome nao tem Silva")
