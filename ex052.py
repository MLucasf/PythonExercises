'''Faça um programa que leia um número inteiro e diga se ele é ou não um
número primo'''
num=int(input("Digite um número: "))
num_div=0
som=0
for i in range(1,num+1):
    if num%i==0: #ex: num = 10. 10/2 tem resto 0, logo 10 é divisível por 2. 10/3 tem resto 1,
        num_div+=1 #para cada número divisível, num_div irá ser somado a 1
        som+=i
        print("\033[32m", end=" ") #pintar os valores divisíveis de verde
    else:
        print("\033[31m", end=" ") #pintar os valores não divisíveis de vermelho

    print(i, end=" ") #printa todos os valores do i dentro do range 1,num+1


if num_div==2: #está fora do for para não ficar repetindo a mesma mensagem igual oa número do range
    #começa quebrando a linha (para anular o "end=" "") e cortando a cor para que ele não fique colorido
    print("\n\033[mO número {} é divisível por {} números, e é primo".format(num,num_div))
else:
    print("\n\033[mO número {} é divisível por {} números, e por isso não é primo".format(num,num_div))
print("A soma dos divisíveis do número {} é {}".format(num, som))

