'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
'''
#quadrado da hipotenusa = soma do quadrado dos catetos

from math import hypot

print("Vamos calcular o comprimento da hipotenusa de um triângulo retãngulo")
cat_op=float(input("Digite a medida do cateto oposto: "))
cat_adj=float(input("Digite a medida do cateto adjacente: "))
#hipot=math.sqrt(pow(cat_op,2)+pow(cat_adj,2))
hipot=hypot(cat_op,cat_adj) #calcula diretamente a hipotenusa dados os catetos

print("A hipotenusa do triângulo cujos catetos oposto e adjacente são {} e {} é {:.2f}"
      .format(cat_op,cat_adj,hipot))
