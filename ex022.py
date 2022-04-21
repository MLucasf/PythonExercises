'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- quantas letras tem ao todo (sem considerar espaços)
- quantas letras tem o primeiro nome
'''
nome=str(input("Qual é o seu nome completo?")).strip()
print("Nome em letras maiúsculas: {}".format(nome.upper()))
print("Nome em letras minúsculas: {}".format(nome.lower()))
print("Número de letras no nome: {}".format(len(nome)-nome.count(" "))) #variável nome - espaço
#é possível subtrair qualquer caracter da palavra desta forma
nome_separado=nome.split() #jogous os nomes separados para a variável nomes
print("Primeiro nome: {}, possui {} letras".format(nome_separado[0], len(nome_separado[0])))
#primeiro elemento do split da variável nome, tamanho do primeiro elemento da variavel nomes

'''como contar apenas o número de vogais na palavra?? '''

