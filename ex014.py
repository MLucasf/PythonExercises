'''
Escreva um programa que conversa uma temperatura digitada em ºC para ºF
'''
temp=float(input("Digite uma temporatura emºC: "))
temp_nova=(temp*9/5)+32
print("A temperatura {:.0f}ºC equivale a {:.1f}ºF".format(temp,float(temp_nova)))
