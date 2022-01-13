'''
Faça um programa que leia um ângulo qualquer, e mostre na tela o seu seno, cosseno e tangente
'''
from math import sin, tan, cos,radians

ang = float(input("Digite o ângulo que você deseja saber: "))
ang=radians(ang) #para encontrar o radiano do angulo
sen = sin(ang) #sen, cos e tan devem ser calculados em radiano
coss = cos(ang)
tang = tan(ang)
print("O seno do ângulo {:.2f}º é {:.2f}º, o cosseno é {:.2f}º, e a tangente é {:.2f}º"
      .format(ang, sen, coss, tang))

