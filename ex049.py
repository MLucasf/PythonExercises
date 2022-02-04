'''Refaça o exercicio 009 mostrando a tabuada de um número escolhido pelo usuário
utilizando o laço de repetição "for"'''

num=int(input("Digite um numero: ")) #é um número imutável, então não deve ficar edntro do for
for mat in range(1,11):
   '''print(num*mat) #o número que estará sempre mudando do 1 ao 10 será o mat
                    #tabuada = número imutável * numero variável de 1 a 10'''
   tab=num*mat
   print("{} x {} = {}".format(num,mat,tab))
