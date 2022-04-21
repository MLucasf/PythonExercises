'''Faça um programa que leia um número qualquer e mostre o seu fatorial'''

num=int(input("Digite um número:"))
fac=num
n=num
while n!=1:
    fac *= (n - 1) #se num=5 - fac=5*4*3*2*1
    print("{} x".format(n),end=" ")
    n -= 1
    if n==1:
        print("{} =".format(n), end=" ")

print("{}".format(fac))
print("O fatorial do número {} é {}".format(num,fac))

'''
n=int(input("Digite um número))
num=n
f=1

while num>0:
    print("{}".format(n),end=" ")
    print("x" if n>1 else "=", end=" ")
    f *= num #1 * o valor pedido 
    num-=1 #toda vez o valor pedido é diminuido em 1 
    
print("{}".format(fac))
    '''