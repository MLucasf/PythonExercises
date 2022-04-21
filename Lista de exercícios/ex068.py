'''
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido
pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para
encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes
(divisões) executados.
'''

num=int(input("Digite um número: "))
div=0

print("Os números primos entre 1 e {} são: ".format(num),end=" ")
for i in range(1,num+1):
    for q in range(1,num+1):
        if i%q==0:
            div+=1
            if div==2:
                print(f"{q}")