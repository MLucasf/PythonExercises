'''Desenvolva um programa queleia seis números inteiros e mostre a soma daqueles
que forem pares. Se o valor digitado for impar, desconsidere-o'''
som=0
for i in range(1,7):
    num1=int(input("Digite um número:"))
    if num1%2==0:
        som+=num1 #soma é a variável da soma dos valores, e num1 são os valores
                #para cada input, num1 irá aumentar. Ex: input 1=2; input2=4
                #som = 0 + 2
                #som = 2 + 4, por que na linha anterior soma virou 2
print(som) #quero que mostre apenas a soma final dos valores
            #logo, é o último valor atribuido à variável "som"
