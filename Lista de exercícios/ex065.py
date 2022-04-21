'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias
vezes e limitando o fatorial a números inteiros positivos e menores que 16.
'''

while True:
    num = int(input("Digite um número que você deseja calcular o fatorial: "))
    fac = 1
    if 0<num<=16:
        for i in range(num,0,-1):
            fac*=i
            if i==1:
                print(f"{i} =",end=" ")
            else:
                print(f"{i} x",end=" ")
        print(f"{fac}")
    else:
        print("Número inválido. Apenas números entre 0 e 16")
    opt=" "
    while opt not in "SsNn":
        opt=str(input("Deseja calcular o fatorial de outro número?"))
        if opt in "Ss":
            print("Calculando...")
        elif opt not in "SsNn":
            print("Opção inválida")
    if opt in "Nn":
        print("Programa encerrando...")
        break

