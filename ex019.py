'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
'''
'''
import random

alunos=["Joao","Pedro","Lucas","Mariazinha"]
for i in alunos:
    i=random.choice(alunos)

print("A pessoa que vai apagar a lousa é {}".format(i))
'''
import random

nom1=str(input("Primeiro aluno: "))
nom2=str(input("Segundo aluno: "))
nom3=str(input("Terceiro aluno: "))
nom4=str(input("Quarto aluno: "))
alunos=[nom1,nom2,nom3,nom4]
limpar=random.choice(alunos)
print("O aluno que irá limpar a lousa será {}".format(limpar))