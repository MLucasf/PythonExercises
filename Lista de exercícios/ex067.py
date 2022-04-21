'''
Altere o programa de cálculo dos números primos, informando, caso o número não
seja primo, por quais número ele é divisível.
'''

num=int(input("Digite um número: "))
div=0

print("Divisores:",end=" ")
for i in range(1,num+1):
    if num%i==0:
        div += 1
        print("{}".format(i), end=" ")

if div==2:
    print("\nO número {} é primo".format(num))
if div>2:
    print("\nO número {} não é primo".format(num))