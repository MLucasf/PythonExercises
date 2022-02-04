'''Crie um programa que leia uma frase e diga se ela é um palíndromo, desconsiderando os espaços'''
'''apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona'''

print("{:*^100}".format("Vamos ver se essa frase é um palíndromo"))
word=str(input("Digite a frase que você quer analisar:")).strip().upper()
words=word.split() #separando a frase em várias palavras
juntar="".join(words) #unindo as palavras divididas sem espaço entre elas
palindromo=""
#print(juntar)
for i in range(len(juntar)-1,-1,-1): #word=abc
                                    #len(word)=3
                                    #a=[0]
                                    #b=[1]
                                    #c=[2]
                                    #apesar de 3 caracteres, só vai até o 2, por isso o len(var)-1
                                    #até o -1 pois ele deve considerar a primeira letra também
                                    #indo de -1 em -1 pois ele deve contar de trás para frente
    #print(juntar[i])
    palindromo+=juntar[i] #palindromo = espaço vazio + o inverso da variável word

if palindromo==juntar:
    print(palindromo)
    print("A frase é um palíndromo")
else:
    print(palindromo)
    print("A frase não é um palíndromo")

for i in range(20,-1,-1):
    print(i,end=" ")


'''frase=str(input("Digite uma frase))
if frase==frase[::-1]: #frase[::-1] = a frase vai do primeiro ao último caractere de -1 em -1, ou seja,
                        de trás para frente
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo)'''

