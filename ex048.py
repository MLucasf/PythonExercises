'''Faça um programa que calcule a soma entre todos os números ímpares que são
multiplos de três e se encontram no intervalo entre 1 e 500'''

soma=0
cont=0
for mult in range(1,501):
    if mult%2==1:
        if mult%3==0:
            cont+=1 #para cada valor encontrado será somado 1
            soma += mult
print("soma dos valores {}".format(soma)) #o valor da variável sempre será o último valor encontrado
print("Quantidade de valores encontrados {}".format(cont))
