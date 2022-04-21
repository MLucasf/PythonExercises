ld1=float(input("Digite o comprimento do lado 1: "))
ld2=float(input("Digite o comprimento do lado 2: "))
ld3=float(input("Digite o comprimento do lado 3: "))

if ld1+ld2>ld3 and ld2+ld3>ld1 and ld1+ld3>ld2:
    if ld1==ld2==ld3==ld1:
        print("O triângulo é equilátero")
    elif ld1!=ld2!=ld3!=ld1:
        print("O triângulo é escaleno")
    else:
        print("O triângulo é isósceles")
else:
    print("Não é possível formar um triângulo com essas medidas")