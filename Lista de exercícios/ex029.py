print("{:=^100}".format("Organizações TABAJARA"))
sal=float(input("Digite o salário: "))
sal_amt=0
amt=0
if sal<280:
    sal_amt=sal+sal*0.2 #aumento de 20%
    amt=20
elif 700>sal>=280:
    sal_amt=sal+sal*0.15
    amt=15
elif 1500>sal>=700:
    sal_amt=sal+sal*0.1
    amt=10
else:
    sal_amt=sal+sal*0.05
    amt=5

print("""Salário anterior: R${:.2f}
Salário atual: R${:.2f}
Aumento: {}%""".format(sal,sal_amt,amt))

