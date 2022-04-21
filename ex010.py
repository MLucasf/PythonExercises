'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
'''
real=float(input("Quanto dinheiro você tem?"))
dol=5.7
dol_comp=real/dol
print("Com essa quantia você pode comprar {:.2f} dólares na cotação de {} reais".format(dol_comp,dol))
