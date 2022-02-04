'''Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço normal e a condição de pagamento:
- à vista no dinheiro ou cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

from time import sleep

print("{:=^40}".format("Boca de fumo do Sako")) #string centralizada(^) com 40 espaços preenchidos por "="
global prec
prec=float(input("Qual é o preço do produto?"))
def pag():
    print("""Para o produto de preço R${:.2f}, temos essas opções de pagamento.
    [1] - à vista no dinheiro
    [2] - à vista no cartão
    [3] - parcelado em até 2x no cartão
    [4] - parcelado em 3x ou mais no cartão""".format(prec))
    opt = int(input("Que opção você deseja?"))

    if opt==1:
        print("Para pagamentos à vista no cartão você tem 10% de desconto. "
              "O valor devido será de R${:.2f}".format(prec-prec*0.1))
    elif opt==2:
        print("Para pagamentos à vista no cartão você tem 5% de desconto."
              "O valor devido será de R${:.2f}".format(prec-prec*0.05))
    elif opt==3:
        print("Para pagamentos parcelados em até 2x no cartão não há desconto."
              "O valor a ser pago será de R${:.2f}".format(prec))
    elif opt==4:
        nprec=prec+(prec*0.2)
        print("Para pagamentos parcelados em 3x ou mais no cartão há a cobrança de 20% de juros."
              "O valor devido será de R${:.2f}".format(nprec))
        parc=int(input("Em quantas parcelas você vai querer dividir?"))
        if parc<3:
            print("Nessa opção não é possível dividir em menos de três vezes. Para dividir em menos"
                  "vezes escolha a opção '3'")
            sleep(1)
            pag()
        else:
            print("O valor das parcelas será R${:.2f}".format(nprec/parc))
            sleep(1)
    else:
        print("Opção inválida. Tente novamente.")
        sleep(1)
        pag()
pag()