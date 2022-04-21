'''val=399

cem=val//100
cinq=val%100//50
vint=val%50//20
dez=val%20//10
cin=val%10//5
um=val%5//1

print("""{} notas de 100
{} notas de 50
{} notas de 20
{} notas de 10
{} notas de 5
{} notas de 1""".format(cem,cinq,vint,dez,cin,um))'''

val=int(input("Digite o valor do saque: "))

if 10<=val<=600:
    
    cem=val//100
    cinq=val%100//50
    dez=val%50//10
    cin=val%10//5
    um=val%5//1

    print("""{} notas de 100
{} notas de 50
{} notas de 10
{} notas de 5
{} notas de 1""".format(cem,cinq,dez,cin,um))
else:
    print("Valor inválido. Max. 600 / Min. 10")