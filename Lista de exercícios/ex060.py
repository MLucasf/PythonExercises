'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
'''

n1=0
n2=1
num=int(input("Até qual termo da sequência de Fibonacci você quer ver? "))
print(f"0 1",end=" ")
for i in range(2,num): #de range 1 a "num" pois eu já começo printando o primeiro termo (1)
    n3 = n2 + n1
    n1 = n2
    n2=n3
    print(f"{n3}",end=" ")

    #OR

'''n1=0
n2=1
termo=0
num=int(input("Até que termo da sequencia de Fibonacci você quer ver? "))
print(f"Os {num} termos da Sequência de Fibonacci são: 1",end=" ")
while termo<(num-1):
    n3=n2+n1
    n1=n2
    n2=n3
    termo+=1
    print(f"{n3}",end=" ")'''