'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''

'''numIn=int(input("Digite o número inicial: "))
quant=int(input("Digite a quantidade de termos que você quer ver: "))
numFi=quant+numIn
menor=maior=0
som=0

if numIn>=0 and numFi<=1000:
    for i in range(numIn,numFi+1):
        if i==numIn:
            maior=i
            menor=i
        if i!=numIn:
            if i>maior:
                maior=i
            if i<menor:
                menor=i
        som+=i
    print("""A - O menor valor é {}
B - O maior valor é {}
C - A soma dos valores é {}""".format(menor,maior,som))
else:
    print("Apenas insira valores entre 0 e 1000")'''

numIn = 0
som = 0
maior = menor = 0
quant=int(input("Quantidade de números que você deseja ver: "))
while True:
    numIn = int(input("Digite o número inicial da sequência: "))
    numFi=numIn+quant
    if numIn>=0 and numFi<=1000:
            for i in range(numIn,numFi+1):
                if i == numIn:
                    maior = menor = numIn
                if i != numIn:
                    if i > maior:
                        maior = i
                    if i < menor:
                        menor = i
                som+=i
            print("O maior termo é {}, o menor é {} e a soma dos termos entre {} e {} é {}"
                  .format(maior, menor, numIn, numFi, som))
            break
    else:
        print("Números inválidos. O número inicial deve ser maior que zero e o final, menor que 1000")
