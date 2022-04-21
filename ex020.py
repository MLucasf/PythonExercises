'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
'''
import random

alunos=["João", "Pedro", "Mariazinha", "Lucas"]

for i in alunos:
    i=random.shuffle(alunos)

print("A ordem de apresentação dos trabalhos será {}".format(alunos))
'''
import random

nom1=str(input("Primeiro aluno: "))
nom2=str(input("Segundo aluno: "))
nom3=str(input("Terceiro aluno: "))
nom4=str(input("Quarto aluno: "))
alunos=[nom1,nom2,nom3,nom4]
random.shuffle(alunos)
print("A ordem de apresentação será {}".format(alunos))