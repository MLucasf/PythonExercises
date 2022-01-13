'''
Faça um programa que leia uma frase pelo teclado e mostre:
- quantas vezes aparece a letra "A"
- em que posição ela aparece pela primeira vez
- Em que posição ela aparece pela última vez
'''
nome=str(input("Digite o seu nome: ")).strip()

#a função replace substitui as letras "ã" e "á" por "a"
nome=nome.replace("á","a")
nome=nome.replace("ã","a")

#função para excluir o espaço entre as palavras


#a função count conta o número de caracteres "A" no input
print("O número de letras 'A' que aparecem no seu nome é {}.".format(nome.upper().count("A")))

#a função find busca o primeiro caracter em que está a letra "A"
#+1 para facilitar a leitura, uma vez que a posição 0 não é utilizada pelos usuários
print("A primeira letra A aparece no caracter {}.".format(nome.upper().find("A")+1))

#a função rfind começa a busca da direita para a esquerda
#+1 para facilitar a leitura, uma vez que a posição 0 não é utilizada pelos usuários
print("A última letra A aparece no caracter {}.".format(nome.upper().rfind("A")+1 - nome.count(" ")))
