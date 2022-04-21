num1=int(input("Digite um número: "))
num2=int(input("Digite um número: "))
sub=num1-num2
if sub<0:
    print("O resultado da subtração {} - {} é {}, um número negativo".format(num1,num2,sub))
else:
    print("O resultado da subtração {} - {} é {}, um número positivo".format(num1,num2,sub))