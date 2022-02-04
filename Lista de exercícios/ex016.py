from math import ceil

altura=float(input("Qual é a altura do quarto que será pintado?"))
largura=float(input("Qual é a largura do quarto que será pintado?"))
area=altura*largura
lata_tinta=54 #total da área pintada por uma lata
total_lata=area/lata_tinta #area total do imóvel dividido pelo total da área pintada pela lata
total_lata=ceil(total_lata) #quantidade de latas necessárias arredondado para cima
valor_total=total_lata*80 #total de latas * valor da lata

print("Para pintar um quarto de {}m² serão necessárias {} latas de tinta e custará R${:.2f}"
      .format(area,total_lata,valor_total))





'''
1 lata pinta 54 de área
para cada 54m de area é necessário uma lata
'''

