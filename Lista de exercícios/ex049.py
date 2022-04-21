'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com
uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com
uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.
'''

popA=80000
popB=200000
count=0
while popA<popB: #se a popA não for menor que popB, ela será maior ou igual
    cresA = popA * 0.03
    cresB = popB * 0.015
    popA+=cresA
    popB+=cresB
    count += 1
    print("""População A - {}
    População B - {}
    Anos - {}""".format(popA,popB,count))
print(f"Demoraria {count} anos para que a população do país A ultrapasse ou se iguale à do país B")