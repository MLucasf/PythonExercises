'''
Crie um algorítmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
'''
n1=int(input("Digite um número: "))
dob=n1*2
trip=n1*3
raiz=pow(n1,1/2)
print("O drobro desse número é {} o triplo é {} e a raiz quadrada é {:.2f}".format(dob, trip,raiz))
