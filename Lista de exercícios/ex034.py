print("{:*^54}".format("Vamos calcular uma Equação de Segundo Grau"))
a = float(input("Digite um número para ser o primeiro termo da equação: "))
if a==0:
    print("A equação não é de segundo grau")
else:
    b = float(input("Digite um número para ser o segundo termo da equação: "))
    c = float(input("Digite um número para ser o segundo termo da equação: "))

    delta = b ** 2 - 4 * a * c
    #delta=delta**(1/2)
    divisor=2*a

    x1 = (-b + (delta ** (1 / 2))) / (2 * a)
    x2 = (-b - (delta ** (1 / 2))) / (2 * a)

    print("A equação dada será {}x² + {}x + {} = 0".format(a,b,c))
    if delta<0:
        print("O delta é {}".format(delta))
        print("A equação não possui raízes reais.")

    elif delta==0:
        print("O delta é {}".format(delta))
        print("Na equação, x será equivalente a {}".format(x1))
    else:
        print("O delta é {}".format(delta))
        print("Na equação, x terá dois possíveis valores: {} e {}".format(x1,x2))