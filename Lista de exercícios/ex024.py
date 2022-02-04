num1=int(input("Digite um número: "))
num2=int(input("Digite outro número: "))
num3=int(input("Digite outro número: "))
if num3<num1>num2:
    if num2>num3:
        print("{} > {} > {}".format(num1,num2,num3))
    elif num3>num2:
        print("{} > {} > {}".format(num1,num3,num2))

elif num1<num2>num3:
    if num1>num3:
        print("{} > {} > {}".format(num2,num1,num3))
    elif num3>num1:
        print("{} > {} > {}".format(num2,num3,num1))

elif num1<num3>num2:
    if num2>num1:
        print("{} > {} > {}".format(num3,num2,num1))
    elif num1>num2:
        print("{} > {} > {}".format(num3,num1,num2))