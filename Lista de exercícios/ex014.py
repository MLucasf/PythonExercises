peso=float(input("Digite o peso dos pescados do dia:"))
excesso=peso-50
multa=excesso*4
print("""O total de peixes pescados foi {:.1f}kg
O excesso pescado foi equivalente a {:.1f}kg
A multa que deverá ser paga equivale a R${:.2f}""".format(peso,excesso,multa))