'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro
custa R$60,00 por dia e R#0,15 por km rodado
'''
dia=int(input("Por quantos dias o carro foi alugado? "))
dist_rodada=float(input("Qual foi a distância percorrida com o carro? "))
custo_dia=dia*60
custo_dist=dist_rodada*0.15
aluguel=custo_dist+custo_dia
#aluguel=(dia*60)+(dist_rodada*0.15)
print("O valor devido, de aluguel, por {} dias e {:.1f}km rodados é R${:.2f}"
        .format(dia, dist_rodada, aluguel))
