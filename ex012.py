'''
Faça um algorítmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
'''
preco=float(input("Qual é o preço do produto? "))
desc=preco-(preco*5/100) #por terem a mesma importância/prioridade, os calculos serão feitos na ordem em que estão escritos
print("O preço do produto com o desconto de 5% é {:.2f}".format(desc))
