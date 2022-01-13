'''
faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.

ex. Ana Maria de Souza
Primeiro: Ana
ùltimo: Souza
'''
'''
1 - input nome completo
2 - dividir nome.split
3 - print nome[0]
4 - print nome[x]
'''
nome=str(input("Digite o seu nome completo:"))
nome=nome.strip().split()

#para mostrar o último nome a função deverá pegar a lista e diminuir por um
#ex. Lucas Martins Machado -> Primeiro nome = 0
#ultimo nome = 3 (número de objetos na lista - 1 -> Posição 2
print("Seu primeiro nome é {} \nSeu último nome é {}".format(nome[0],nome[len(nome)-1]))
#nome[-1] -> também se refere ao último objeto da lista
#nome[-2] -> se refere ao penúltimo objeto da lista