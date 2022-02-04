'''escreva um programa para aprovar o empréstimo bancário para
a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
em quantos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não pode exceder
30% do salário ou então o empréstimo será negado'''

from time import sleep
print("Olá. Para pedir um empréstimo, responda as seguintes perguntas:")
sleep(1)
val_casa=float(input("Qual é o valor da casa que você deseja financiar?"))
sal=float(input("Qual é o seu salário mensal?"))
num_prest=int(input("Em quantos anos você pretende pagar o financiamento?"))
num_prest=num_prest*12
prest=val_casa/num_prest
val_prest=val_casa/num_prest/sal*100
if val_prest>30:
    print("\033[31mVocê não tem renda o suficiente para financiar "
          "esta casa e pagar nesse número de parcelas. O valor das prestações será de"
          "R${:.2f} \ne isso equivale a {:.2f}% do seu salário".format(prest,val_prest))
else:
    print("\033[32mO seu empréstimo será aprovado!"
          "O valor da restação será R${:.2f} e isso equivale a \n{:.2f}% do seu salário"
          "\033[m".format(prest,val_prest))
