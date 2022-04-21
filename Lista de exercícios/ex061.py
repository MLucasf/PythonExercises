'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500
'''

n1=0
n2=1
termo=2 #já possuo o primeiro termo (1)
n3=0

print("0 1",end=" ")

while n3<=500:
    n3=n2+n1
    n1=n2
    n2=n3
    print(f"{n3}",end=" ")
    termo+=1

print("\nO termo que supera o valor de 500 é o termo de número {}".format(termo))