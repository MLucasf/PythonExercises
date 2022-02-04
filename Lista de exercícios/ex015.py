horas_dia=int(input("Quantas horas você trabalha por dia?"))
sal_hora=float(input("Quanto você recebe por hora trabalhada?"))
sal_mes=sal_hora*horas_dia*30
ir=sal_mes*0.11
inss=sal_mes*0.08
sindicato=sal_mes*0.05
sal_liquido=sal_mes-ir-inss-sindicato
print("""Sabendo que você recebe R${:.2f} por mês, serão descontados dele:
- Imposto de Renda (11%) - R${:.2f}
- INSS (8%) - R${:.2f}
- Sindicato (5%) - R${:.2f}
Sendo assim, após os descontos o seu salário líquido é R${:.2f}""".format(sal_mes,ir,inss,sindicato,sal_liquido))