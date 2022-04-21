'''
Desenvolva um programa que leia o comprimento de três retas e diga ao
usuário se elas podem ou não formar um triângulo
'''
from time import sleep
print ("-="*20)
re1=int(input("Digite o comprimento de uma reta:"))
print ("-="*20)
re2=int(input("Digite o comprimento de outra reta:"))
print ("-="*20)
re3=int(input("Digite o comprimento de mais uma reta:"))
print ("-="*20)
sleep(2)
if re1+re2>re3 and re1+re3>re2 and re2+re3>re1:
    print("É possível fazer um triângulo com essas retas △")
else:
    print("Não é possível fazer um triângulo com essas retas ⨻")

    '''
    se a soma das medidas de dois deles é sempre maior que a medida do terceiro, 
    então, eles podem formar um triângulo.'''