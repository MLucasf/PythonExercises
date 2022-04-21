'''
Altere o programa anterior permitindo ao usuário
informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''

popA=int(input("População inicial da cidade A: "))
popB=int(input("População inicial da cidade B: "))
cresA=float(input("Taxa de crescimento da população da cidade A: "))
cresA/=100 #porcentagem para decimal
cresB=float(input("Taxa de crescimento da população da cidade B: "))
cresB/=100 #porcentagem para decimal
anos=0

while popA<popB:
    cres_A=cresA*popA
    cres_B=cresB*popB
    popA+=cres_A
    popB+=cres_B
    anos+=1

print("Demoraria {} anos para que a população da cidade A se igualasse ou superasse a população da cidade B"
      .format(anos))

