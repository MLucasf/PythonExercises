num=int(input("Digite um número: "))
uni=num//1%10
dez=num//10%10
cent=num//100%10
mil=num//1000%10

print("{} unidades, {} dezenas, {} centenas e {} milhares".format(uni,dez,cent,mil))