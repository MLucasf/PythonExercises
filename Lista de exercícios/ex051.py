'''
Faça um programa que imprima na tela os números de 1 a 20,
um abaixo do outro. Depois modifique o programa para que ele mostre
os números um ao lado do outro.
'''
i=0
lado=str(input("Digite L para um do lado do outro e B para um embaixo do outro: "))
while i<=19:
    i+=1
    if lado in "Ll":
        print(i,end=" ")
    elif lado in "Cc":
        print(i)
    else:
        print("Opção iválida")
