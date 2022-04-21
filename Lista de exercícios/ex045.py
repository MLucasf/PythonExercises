'''
Tipo de carne
Quantidade da carne
Preço total
Tipo de pagamento
Valor de desconto (se houver)
valor a pagar
'''
print(f"{'Hipermercado Tabajara':*^54}")
tipo_carne=str(input("""Qual é o tipo de carne que você deseja comprar?
[A] - File Duplo
[B] - Alcatara
[C] - Picanha""")).strip().lower()
qnt_carne=float(input("Quanto dessa carne você deseja comprar, em quilogramas?"))
prec_total=0
valor_desc=0
prec_final=0

if tipo_carne=="a":
    tipo_carne="Filé Duplo"
    if qnt_carne<=5:
        prec_total=qnt_carne*4.9
    else:
        prec_total=qnt_carne*5.8
elif tipo_carne=="b":
    tipo_carne="Alcatara"
    if qnt_carne<=5:
        prec_total=qnt_carne*5.9
    else:
        prec_total=qnt_carne*6.8
elif tipo_carne=="c":
    tipo_carne="Picanha"
    if qnt_carne<=5:
        prec_total=qnt_carne*6.9
    else:
        prec_total=qnt_carne*7.8
else:
    print("Opção inválida.")

tipo_pagamento=str(input("""Qual é a forma de pagamento desejada?
[A] - Cartão
[B] - Dinheiro
[C] - Cartão Tabajara""")).strip().lower()

if tipo_pagamento=="a":
    tipo_pagamento="Cartão"
    valor_desc=0
elif tipo_pagamento=="b":
    tipo_pagamento="Dinheiro"
    valor_desc=prec_total*0.05
elif tipo_pagamento=="c":
    tipo_pagamento="Cartão Tabajara"
    valor_desc=prec_total*0.1
else:
    print("Opção Inválida.")

prec_final=prec_total-valor_desc

print(f"{'Nota Fiscal':=^50}")
print("""Tipo de Carne: {}
Quantidade: {:.1f}kg
Preço Total: R${:.2f}
Opção de Pagamento: {}
Valor do Desconto: R${:.2f}
Valor a Pagar: R${:.2f}""".format(tipo_carne,qnt_carne,prec_total,tipo_pagamento,valor_desc,prec_final))
print("="*50)


