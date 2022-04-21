'''refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10
primeiros termos de uma progressão aritmética usando o while'''

num1=int(input("Digite o primeiro número da progressão aritmética: "))
raz=int(input("Digite a razão dessa progressão aritmética: "))
pa=num1
dec_num=num1+(10-1)*raz
print("Os números da pa são:",end=" ")
print("{}".format(num1),end=" ") #unica forma de printar o primeiro termo
while pa!=dec_num: #enquanto pa for diferente do ultimo termo
    pa+=raz #pa = primeiro termo + razão
    print("{}".format(pa),end=" ") #printa o valor de pa (valor dos termos da PA)


'''primeiro=int(input("Digite o primeiro termo da PA: "))
razao=int(input("Digite a razão da PA: "))
termo=primeiro
cont=1
while cont<=10:
    print("{}".format(termo),end=" ")
    termo+=razao
    cont+=1'''
