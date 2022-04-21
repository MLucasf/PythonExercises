'''Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes'''
a=float(input("Qual é o tamanho do lado A do triângulo?"))
b=float(input("Qual é o tamanho do lado B do triângulo?"))
c=float(input("Qual é o tamanho do lado C do triângulo?"))

if a+b>c and b+c>a and c+a>b:
    if a==b and b!=c or a==c and b!=c or b==c and b!=a: #deve ter apenas dois lados iguais
        print("O triângulo formado com essas lados será isósceles")
    elif a==b==c: #tem todos os lados iguais
        print("O triângulo formado com esses lados será equilátero")
    else: #tem todos os lados diferentes (a!=b!=c!=a)
        print("O triângulo formado com esses lados será escaleno")
else:
    print("Não é possível formar um triângulo com esses lados")