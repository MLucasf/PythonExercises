num1=int(input("Digite um número: "))
num2=int(input("Digite um número: "))
num3=int(input("Digite um número: "))


if num2>num3 and num2>num1:
    if num1>num3:
        menor=num3
        print("""Ascendente: {} > {} > {}
        Descendente: {} < {} < {}""".format(num3,num1,num2,num2,num1,num3))
    elif num3>num1:
        print("""Ascendente: {} > {} > {}
        Descendente: {} < {} < {}""".format(num1,num3,num2,num2,num3,num1))
elif num3<num1>num2:
    if num2>num3:
        print("""Ascendente: {} > {} > {}
        Descendente: {} < {} < {}""".format(num3,num2,num1,num1,num2,num3))
    elif num3>num2:
        print("""Ascendente: {} > {} > {}
        Descendente: {} < {} < {}""".format(num2,num3,num1,num1,num3,num2))
else:
    if num1>num2:
        print("""Ascendente: {} > {} > {}
        Descendente: {} < {} < {}""".format(num2,num1,num3,num3,num1,num2))
    elif num2>num1:
        print("""Ascendente: {} > {} > {}
        Descendente: {} < {} < {}""".format(num1,num2,num3,num3,num2,num1))


