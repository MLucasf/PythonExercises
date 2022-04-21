'''
Escreva um programa que leia um valor em metros e converta ele em contímetros e milímetros
'''
n1=float(input("Digite uma distância em metros: "))
cm=n1*100
ml=n1*1000
print("Essa distância equivale a {:.0f}cm e {:.0f}ml".format(cm,ml))

