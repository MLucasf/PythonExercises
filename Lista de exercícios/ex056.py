'''
Altere o programa anterior para mostrar no final a soma dos números.
'''
num_in=int(input("Digite o número inicial: "))
num_fi=int(input("Digite o número final: "))
som=0

for i in range(num_in+1,num_fi):
    som+=i
print(f"A soma dos valores entre {num_in} e {num_fi} é {som}")