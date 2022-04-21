'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro
número elevado ao segundo número. Não utilize a função de potência da linguagem.
'''

'''while True:
    base=int(input("Digit um número: "))
    exp=int(input("Digite um número: "))
    print(f"O número {base} elevado ao número {exp} tem como resultado o número {base**exp}")
    opt=" "
    while opt not in "SsNn":
        opt=str(input("Deseja colocar outros números? [S/N]"))
        if opt not in "SsNn":
            print("Resposta Inválida.")
    if opt in "Nn":
        print("Obrigado. Volte sempre.")
        break
'''
base = int(input("Digit um número: "))
exp = int(input("Digite um número: "))
potencia=1 #o primeiro número será a própria base. Portanto, multiplicá-la por 1 é o mesmo que repetí-la
count=0 #o primeiro número da potenciação sempre será a própria base.
        #ex: 3**3 = 3 (base) x 3 x 3 => há apenas duas multiplicações
while count<exp:
    potencia*=base
    count+=1
print(potencia)