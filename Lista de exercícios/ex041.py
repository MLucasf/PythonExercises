from math import floor

print(f"{' Máquina de contas do Lucas ':*^70}")
num1=float(input("Digite um número: "))
num2=float(input("Digite um número: "))
dec=str(input("""Qual operação você quer fazer com esses números?
[A] - Adição
[S] - Subtração
[D] - Divisão
[M] - Multiplicação
[P] - Potênciação""")).strip().upper()
res=0
if dec=="A":
    res=num1+num2
    print("A soma de {} + {} = {}".format(num1,num2,res))
elif dec=="S":
    res=num1-num2
    print("A subtração de {} - {} = {}".format(num1,num2,res))
elif dec=="D":
    res=num1/num2
    print("A divisão de {} / {} = {}".format(num1,num2,res))
elif dec=="M":
    res=num1*num2
    print("A multiplicação de {} x {} = {}".format(num1,num2,res))
elif dec=="P":
    res=num1**num2
    print("A potência de {} elevado a {} equivale a {}".format(num1,num2,res))
else:
    print("Opção inválida")

if res%2==0:
    print("O resultado é par")
else:
    print("O resultado é ímpar")

if res>0:
    print("O resultado é positivo")
else:
    print("O resultado é negativo")

if floor(res)==res:
    print("O resultado é um número inteiro")
else:
    print("O resultado é um número decimal")
