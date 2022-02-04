from math import ceil,floor
altura=float(input("Qual é a altura do quarto que será pintado?"))
comprimento=float(input("Qual é o comprimento do quarto que será pintado?"))
area=altura*comprimento
litros=area/6 #quantidade, em litros, necessária para pintar a area
litros+=litros*0.1 #acréscimo de 10% na quantidade de tinta necessária
litros=ceil(litros)
dezoito=litros/18 #quantidade de galões
tresemeio=litros/3.6 #quantidade de latas
dezoito_int=ceil(dezoito) #arredondando a quantidade de galões para cima
tresemeio_int=ceil(tresemeio) #arredondando a quantidade de latas para cima
preco_dezoito=dezoito_int*80 #calculando a quantidade de galões * o preço da cada galão
preco_tresemeio=tresemeio_int*25 #calculando a quantidade de latas * o preço de cada lata

resto_18=litros%18
quant_lata=resto_18/3.6
quant_18_mist=floor(dezoito) #arredondar para baixo o valor
quant_lata_mist=ceil(quant_lata)
valor_18_mist=quant_18_mist*80
val_lata_mist=quant_lata_mist*25
val_mist=val_lata_mist+valor_18_mist

print("A área do quarto é {}m²".format(area))
print("A quantidade de latas de 18L necessárias será {}, no valor de R${:.2f}".format(dezoito_int,preco_dezoito))
print("A quantidade de latas de 3.6L necessárias será de {}, no valor de R${:.2f}".format(tresemeio_int,preco_tresemeio))
print("A quantiade de galões necessárias seria {} e de latas seria {}, e o valor seria R${:.2f}".format(quant_18_mist,quant_lata_mist,val_mist))