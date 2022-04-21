'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
o seu IMC e mostre o seu status, de acordo com a tabela abaixo:
- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepreso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida'''

from math import pow

alt=float(input("Qual é a sua altura, em centímetros?"))
peso=float(input("Qual é o seu peso, em kg?"))
alt=alt/100 #passar a altura para metro
imc=peso/pow(alt,2) #(alt**2)
if imc<18.5:
    print("O seu IMC é {:.1f} e você está \033[31mabaixo do peso\033[m. Ser muito magro também é prejudicial.".format(imc))
elif 18.5<=imc<25:
    print("O seu IMC é {:.1f} e você está \033[32mno peso ideal\033[m. Mantenha a forma!".format(imc))
elif 25<=imc<30:
    print("O seu IMC é {:.1f} e você está com \033[35msobrepeso\033[m. Cuidado".format(imc))
elif 30<=imc<=40:
    print("O seu IMC é {:.1f} e você está com \033[31mobesidade\033[m. Você precisa de uma dieta".format(imc))
else:
    print("O seu IMC é {:.1f} e você está com \033[1;31mobesidade mórbida\033[m. Talvez valha a pena"
          "cogitar uma cirurgia bariátrica.".format(imc))
