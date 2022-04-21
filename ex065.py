'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor
valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores.'''

opt = True
maior = 0
menor = 0
som = 0
qtd_num = 0


while opt==True:
    num=int(input("Digite um número: "))
    qtd_num += 1 #todo número digitado deverá contar +1
    som += num
    if qtd_num==1: #o primeiro termo da variável "num" sempre terá qtd_num=1
        maior=menor=num #maior e menor serão iguais ao primeiro valor atribuído à variável
    if qtd_num!=1:
        if num>maior:
            maior=num
        if num<menor:
            menor=num

    opt=str(input("Deseja digitar outro número? [S/N]"))
    if opt in "Ss":
        opt=True
    elif opt in "Nn":
        print("Tudo bem, vamos aos resultados")
        opt=False
    else:
        print("Opção inválida")
med=som/qtd_num
print("O maior dos valores é {}, o menor é {} e a média dos valores é {:.2f}".format(maior,menor,med))