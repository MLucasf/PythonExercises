num1=int(input("Digite um número inteiro (sem virgula):"))
num2=int(input("Digite outro número inteiro (sem vírgula):"))
num3=float(input("Digite um número real (com vírgula):"))
a=num1*(num2/2)
b=3*num1+num3
c=num3**3

print(a, b, "{:.2f}".format(c))