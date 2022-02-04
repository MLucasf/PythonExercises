'''
1 - Pegar um nome
2 - diminuir a letra de todos os nomes
3 - tirar todos os acentos do nome
4 - tirar os espaços do nome
5 - dividir o nome em letras
6 - analisar as letras para saber quais são vogais
7 - dizer a quantidade de vogais presentes no nome
'''
'''nome=str(input("Digite um nome: ")).strip().lower()
nome=nome.replace("ã","a");nome=nome.replace("ã","a")
#nome=len(nome)-nome.count(" ")
letras=list(nome)
#print(letras)

if letras in "aeiou":
    print("{} tem vogais".format(nome))'''

nome=str(input("Digite uma palavra: ")).strip().lower()
nome=nome.replace("ã","a");nome=nome.replace("á","a");nome=nome.replace("â","a")
vogais="aeiou" #vogais
qtd_vogais=0 #acumulador da quantidade de vogais
for v in nome: #para cada variável 'v' na variável 'nome' (vai ser checado ver em todo o len(nome)+1
                #não to usando v in range() pois eu não quero que analise a posição, e sim as strings
                #da variável 'nome'
    if v in vogais: #se algum 'v' estiver em 'vogais'(aeiou)
        qtd_vogais+=1 #acumulador aumenta em 1juli
print("A quantidade de vogais nessa palavra é {}".format(qtd_vogais))