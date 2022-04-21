'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar 999, que é a condição de parada. No final, mostre quantos números
foram digitados e qual a soma entre eles (desconsiderando a flag)
'''

count=som=0

while True:
    num=int(input("Digite um número: [Digite 999 para parar]"))
    if num==999: #o if vem antes do count e soma para que o valor 999 não seja incluido
        break #o break quebra o laço de repetição, portanto não ativaria o count e o som caso o numero
                #digitado seja o 999
    count+=1
    som+=num

if count==1:
    print("Foi digitado apenas um valor")
elif count==0:
    print("Não foi digitado nenhum valor")
else:
    print(f"Foram digitados {count} valores e a soma deles é {som}")