ganho_hora=float(input("Quanto você recebe por hora? R$"))
hora_trab=int(input("Quantas horas você trabalha por dia?"))
hora_trab=hora_trab*30
print("O seu salário mensal, recebendo R${:.2f} e trabalhando {} horas por mês equivale a {}"
      .format(ganho_hora,hora_trab,ganho_hora*hora_trab))
