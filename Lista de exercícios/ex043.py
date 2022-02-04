comb=str(input("""Com qual combustível deseja abastecer? 
[A] - Álcool
[G] - Gasolina""")).strip().lower()
quant=0
prec=0
desc=0

if comb=="a":
    quant=int(input("Qual a quantidade de alcool (em litros)?"))
    prec=1.9*quant
    if quant<=20:
        desc = quant * 0.03
        prec-=desc
    elif quant>20:
        desc=quant*0.05
        prec-=desc
elif comb=="g":
    quant=int(input("Qual a quantidade de gasolina (em litros)?"))
    prec=2.5*quant
    if quant<=20:
        desc=quant*0.04
        prec-=desc
    elif quant>20:
        desc=quant*0.06
        prec-=desc

print("O valor de abastecer {}L com o desconto de {}% será de R${:.2f}".format(quant,desc,prec))