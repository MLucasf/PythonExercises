'''Faça um programa que leia um número qualquer e mostre o seu fatorial utilizando o for'''

num=int(input("Digite um número: "))
num_fix=num
fac_x=num
fac=0

for i in range(num,1,-1):
    fac=num*(fac_x-1)
    fac_x -= 1
    print("{} x {} = {}".format(num, fac_x, fac))
    num = fac
print("O fatorial de {} é {}".format(num_fix,fac))


