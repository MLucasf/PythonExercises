sal_hr=float(input("Digite o valor recebido por hora trabalhada: "))
hora_dia=int(input("Digite o número de horas trabalhadas por dia: "))
sal_mes=sal_hr*hora_dia
sind=sal_mes*0.03
fgts=sal_mes*0.11
ir=0
ir_quant=0
sal_liq=0

if sal_mes<=900:
    ir=0
elif sal_mes<=1500:
    ir_quant=5
    ir=sal_mes*ir_quant/100
elif sal_mes<=2500:
    ir_quant=10
    ir=sal_mes*ir_quant/100
else:
    ir_quant=20
    ir=sal_mes*ir_quant/100

sal_liq=sal_mes-ir-fgts-sind
total_desc=ir+fgts+sind

print("""Salário Bruto: R${:.2f}
(-) IR ({}%): R${:.2f}
(-) Sindicado (3%): R${:.2f}
FGTS (11%): R${:.2f}
Total de Descontos: R${:.2f}
Salário Líquido: R${:.2f}""".format(sal_mes,ir_quant,ir,sind,fgts,total_desc,sal_liq))