'''
Faça um programa que leia a altura e a largura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta
pinta uma área de 2m²
'''
alt=float(input("Qual é a altura do cômodo? "))
larg=float(input("Qual é a largura do cômodo? "))
area=alt*larg
quant_tinta=area/2
print("Serão necessários {:.1f} litros de tinta para pintar o cômodo de {:.0f}m²"
      .format(quant_tinta,area))
