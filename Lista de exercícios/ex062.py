'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120
'''

num=int(input("Digite um número que você deseja ver o fatorial: "))
fatorial=num
print(f"O fatorial do número {num} é: 5",end=" ")
for i in range(1,num): 
    num-=1
    fatorial*=num
    print(f"x {num}",end=" ")
print(f" = {fatorial}")

'''num=int(input("Digite um número que você deseja ver o fatorial: "))
fatorial=1
print(f"O fatorial do número {num} é:",end=" ")
for i in range(num, 0,-1):
    fatorial*=i
    if i==1:
        print(f"{i} =",end=" ")
    elif i!=1:
        print(f"{i} x",end=" ")
print(f"{fatorial}")'''
