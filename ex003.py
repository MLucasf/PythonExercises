
nome_usuario=input("Qual é o seu nome?")
print(nome_usuario)
idade_usuario=int(input("Digite a sua idade: "))
print(idade_usuario)
peso_usuario=float(input("Digite o seu peso: "))
print(peso_usuario)
peso_desejado=float(input("Digite o peso desejado: "))
vezesMalhou=0
def malhar (idade, peso):
#como a função sabe que idade = idade_usuario?
    if idade<28:
        peso=peso-2
    else:
        peso=peso-1
    return peso
while(peso_usuario>peso_desejado):
    peso_usuario=malhar(idade_usuario,peso_usuario)
    vezesMalhou=vezesMalhou+1
print("{}, você precisa malhar {} vezes para chegar no seu peso ideal {}"
      .format(nome_usuario, vezesMalhou, peso_desejado))
